from collections import defaultdict

from cadence_professional_slice0.model import (
    MINUTES_PER_DAY,
    REGULAR_DAY_MINUTES,
    WORKDAY_START_MINUTE,
    ConstraintSet,
    canonical_json,
    load_portfolio,
    load_request,
)
from cadence_professional_slice0.scheduler import schedule_portfolio
from cadence_professional_slice0.workflow import simulate


def _assert_schedule_invariants(portfolio, schedule, constraints):
    task_by_id = portfolio.task_by_id
    staff_by_id = portfolio.staff_by_id

    intervals_by_staff = defaultdict(list)
    intervals_by_task = defaultdict(list)
    for interval in schedule.intervals:
        intervals_by_staff[interval.staff_id].append(interval)
        intervals_by_task[interval.task_id].append(interval)
        task = task_by_id[interval.task_id]
        staff = staff_by_id[interval.staff_id]
        assert interval.staff_id in task.eligible_staff_ids
        assert task.required_capability in staff.capabilities

        day = interval.start_minute // MINUTES_PER_DAY
        assert day not in staff.pto_days
        regular_start = day * MINUTES_PER_DAY + WORKDAY_START_MINUTE
        regular_end = regular_start + REGULAR_DAY_MINUTES
        if interval.overtime:
            assert interval.start_minute >= regular_end
        else:
            assert regular_start <= interval.start_minute < regular_end
            assert interval.end_minute <= regular_end

    for staff_intervals in intervals_by_staff.values():
        ordered = sorted(staff_intervals, key=lambda item: item.start_minute)
        for left, right in zip(ordered, ordered[1:]):
            assert left.end_minute <= right.start_minute

    for task in portfolio.tasks:
        intervals = sorted(intervals_by_task[task.id], key=lambda item: item.start_minute)
        assert sum(item.duration_minutes for item in intervals) == task.effort_minutes
        if task.dependencies:
            dependency_finish = max(schedule.task_completion_minutes[item] for item in task.dependencies)
            assert intervals[0].start_minute >= dependency_finish

    for staff_id, minutes in schedule.overtime_minutes_by_staff.items():
        assert minutes <= constraints.max_overtime_minutes_per_staff
        assert staff_id in staff_by_id


def test_baseline_and_scenarios_preserve_hard_constraints(fixtures_dir):
    portfolio = load_portfolio(fixtures_dir / "project_x_portfolio_v0.json")
    request = load_request(fixtures_dir / "expedite_project_x_request_v0.json")
    no_overtime = ConstraintSet(max_overtime_minutes_per_staff=0)
    one_hour_overtime = ConstraintSet(max_overtime_minutes_per_staff=60)

    baseline = schedule_portfolio(portfolio, portfolio.baseline_project_order, no_overtime)
    baseline_before = canonical_json(baseline)
    scenario_v1 = simulate(portfolio, request, baseline, 1, no_overtime)
    scenario_v2 = simulate(portfolio, request, baseline, 2, one_hour_overtime)

    assert canonical_json(baseline) == baseline_before
    _assert_schedule_invariants(portfolio, baseline, no_overtime)
    _assert_schedule_invariants(portfolio, scenario_v1.schedule, no_overtime)
    _assert_schedule_invariants(portfolio, scenario_v2.schedule, one_hour_overtime)

    assert all(
        interval.project_id == "project-x"
        for interval in scenario_v2.schedule.intervals
        if interval.overtime
    )


def test_explanations_are_grounded_in_explicit_fixture_facts(fixtures_dir):
    portfolio = load_portfolio(fixtures_dir / "project_x_portfolio_v0.json")
    request = load_request(fixtures_dir / "expedite_project_x_request_v0.json")
    baseline = schedule_portfolio(
        portfolio,
        portfolio.baseline_project_order,
        ConstraintSet(max_overtime_minutes_per_staff=0),
    )
    scenario = simulate(
        portfolio,
        request,
        baseline,
        2,
        ConstraintSet(max_overtime_minutes_per_staff=60),
    )

    by_code = {item.code: item for item in scenario.explanations}
    assert "staff:jill:pto_days" in by_code["JILL_PTO_GAP"].fact_refs
    assert "constraint:explicit_eligibility_only" in by_code["TARGET_ACCELERATION"].fact_refs
    assert "staff:hourly_rates" in by_code["OVERTIME_COST"].fact_refs
