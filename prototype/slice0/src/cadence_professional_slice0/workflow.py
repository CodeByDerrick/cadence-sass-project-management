from __future__ import annotations

from dataclasses import replace
from decimal import Decimal
from pathlib import Path
from typing import Any

from .model import (
    MINUTES_PER_DAY,
    AppliedOperationalRevision,
    Authorization,
    ConstraintSet,
    Explanation,
    ExpeditionRequest,
    Portfolio,
    PortfolioImpact,
    RevalidationResult,
    Scenario,
    Schedule,
    canonical_json,
    flatten_intervals,
    load_portfolio,
    load_request,
    money,
    stable_digest,
    to_primitive,
)
from .scheduler import schedule_portfolio

SCHEMA_VERSION = "prototype.slice0.v0"
SCENARIO_ID = "scenario-expedite-project-x"


class AuthorizationError(RuntimeError):
    """Raised when authorization does not exactly cover a scenario."""


class StaleBaselineError(RuntimeError):
    """Raised when an authorized scenario targets a stale baseline."""


def _project_order_for_target(portfolio: Portfolio, target_project_id: str) -> tuple[str, ...]:
    remaining = [
        project_id
        for project_id in portfolio.baseline_project_order
        if project_id != target_project_id
    ]
    return (target_project_id, *remaining)


def _intervals_by_task(schedule: Schedule) -> dict[str, tuple[dict[str, Any], ...]]:
    result: dict[str, tuple[dict[str, Any], ...]] = {}
    for task_id in schedule.task_completion_minutes:
        result[task_id] = flatten_intervals(
            interval for interval in schedule.intervals if interval.task_id == task_id
        )
    return result


def _proposed_changes(
    baseline: Schedule,
    proposal: Schedule,
) -> tuple[dict[str, Any], ...]:
    baseline_by_task = _intervals_by_task(baseline)
    proposal_by_task = _intervals_by_task(proposal)
    changes: list[dict[str, Any]] = []
    for task_id in sorted(set(baseline_by_task) | set(proposal_by_task)):
        before = baseline_by_task.get(task_id, ())
        after = proposal_by_task.get(task_id, ())
        if before != after:
            changes.append({"task_id": task_id, "before": before, "after": after})
    return tuple(changes)


def _calculate_impact(
    portfolio: Portfolio,
    baseline: Schedule,
    proposal: Schedule,
    target_project_id: str,
) -> PortfolioImpact:
    deltas = {
        project_id: proposal.project_completion_minutes[project_id]
        - baseline.project_completion_minutes[project_id]
        for project_id in sorted(baseline.project_completion_minutes)
    }
    deadlines_crossed = tuple(
        sorted(
            project.id
            for project in portfolio.projects
            if baseline.project_completion_minutes[project.id] <= project.deadline_minute
            < proposal.project_completion_minutes[project.id]
        )
    )
    displaced_projects = tuple(
        project_id
        for project_id, delta in sorted(deltas.items())
        if project_id != target_project_id and delta > 0
    )

    overtime_compensation = Decimal("0")
    regular_equivalent = Decimal("0")
    for staff_id, minutes in proposal.overtime_minutes_by_staff.items():
        staff = portfolio.staff_by_id[staff_id]
        hours = Decimal(minutes) / Decimal(60)
        overtime_compensation += hours * staff.hourly_rate * portfolio.overtime_multiplier
        regular_equivalent += hours * staff.hourly_rate

    return PortfolioImpact(
        target_completion_delta_minutes=deltas[target_project_id],
        project_completion_deltas=deltas,
        deadlines_crossed=deadlines_crossed,
        overtime_minutes_by_staff=proposal.overtime_minutes_by_staff,
        overtime_compensation=money(overtime_compensation),
        incremental_overtime_premium=money(overtime_compensation - regular_equivalent),
        displaced_projects=displaced_projects,
    )


def _format_minute(value: int) -> str:
    day = value // MINUTES_PER_DAY
    minute_of_day = value % MINUTES_PER_DAY
    hour = minute_of_day // 60
    minute = minute_of_day % 60
    return f"day {day} at {hour:02d}:{minute:02d}"


def _build_explanations(
    portfolio: Portfolio,
    baseline: Schedule,
    proposal: Schedule,
    impacts: PortfolioImpact,
    target_project_id: str,
) -> tuple[Explanation, ...]:
    explanations: list[Explanation] = []
    target_project = portfolio.project_by_id[target_project_id]
    baseline_finish = baseline.project_completion_minutes[target_project_id]
    proposal_finish = proposal.project_completion_minutes[target_project_id]
    explanations.append(
        Explanation(
            code="TARGET_ACCELERATION",
            summary=(
                f"{target_project.name} moves from {_format_minute(baseline_finish)} "
                f"to {_format_minute(proposal_finish)} because its tasks are scheduled "
                "ahead of lower-priority portfolio work while preserving explicit "
                "dependencies and task eligibility."
            ),
            fact_refs=(
                f"project:{target_project_id}:priority",
                f"baseline:{portfolio.revision_id}",
                "constraint:dependencies_are_hard",
                "constraint:explicit_eligibility_only",
            ),
        )
    )

    x2_intervals = [item for item in proposal.intervals if item.task_id == "x-2"]
    if x2_intervals and x2_intervals[0].staff_id == "alex":
        explanations.append(
            Explanation(
                code="JILL_PTO_GAP",
                summary=(
                    "Jill is explicitly eligible for Project X assembly work, but her "
                    "approved PTO on days 1 and 2 removes the earliest execution window. "
                    "Alex is selected because Alex is explicitly eligible and can complete "
                    "the task sooner without violating Jill's protected availability."
                ),
                fact_refs=(
                    "staff:jill:pto_days",
                    "task:x-2:eligible_staff_ids",
                    "staff:alex:capabilities",
                    "constraint:pto_is_hard",
                ),
            )
        )

    for project_id in impacts.displaced_projects:
        delta = impacts.project_completion_deltas[project_id]
        explanations.append(
            Explanation(
                code="PORTFOLIO_DISPLACEMENT",
                summary=(
                    f"{portfolio.project_by_id[project_id].name} completes {delta} minutes "
                    "later because shared staff capacity is reassigned to Project X."
                ),
                fact_refs=(
                    f"project:{project_id}:baseline_completion",
                    f"project:{project_id}:scenario_completion",
                    f"scenario:{SCENARIO_ID}:proposed_changes",
                ),
            )
        )

    if impacts.overtime_minutes_by_staff:
        staff_summary = ", ".join(
            f"{portfolio.staff_by_id[staff_id].name}: {minutes} minutes"
            for staff_id, minutes in sorted(impacts.overtime_minutes_by_staff.items())
        )
        explanations.append(
            Explanation(
                code="OVERTIME_COST",
                summary=(
                    f"The scenario uses bounded overtime ({staff_summary}). The synthetic "
                    f"overtime compensation is ${impacts.overtime_compensation}, including "
                    f"an incremental premium of ${impacts.incremental_overtime_premium}."
                ),
                fact_refs=(
                    "constraint:max_overtime_minutes_per_staff",
                    "portfolio:overtime_multiplier",
                    "staff:hourly_rates",
                ),
            )
        )
    return tuple(explanations)


def simulate(
    portfolio: Portfolio,
    request: ExpeditionRequest,
    baseline: Schedule,
    version: int,
    constraints: ConstraintSet,
) -> Scenario:
    proposal = schedule_portfolio(
        portfolio,
        _project_order_for_target(portfolio, request.target_project_id),
        constraints,
        overtime_project_id=request.target_project_id,
    )
    impacts = _calculate_impact(portfolio, baseline, proposal, request.target_project_id)
    changes = _proposed_changes(baseline, proposal)
    return Scenario(
        scenario_id=SCENARIO_ID,
        version=version,
        baseline_revision_id=portfolio.revision_id,
        request_id=request.request_id,
        target_project_id=request.target_project_id,
        state="SIMULATED",
        constraints=constraints,
        schedule=proposal,
        impacts=impacts,
        explanations=_build_explanations(
            portfolio, baseline, proposal, impacts, request.target_project_id
        ),
        proposed_changes=changes,
        change_set_digest=stable_digest(changes),
    )


def hold_scenario(scenario: Scenario) -> Scenario:
    if scenario.state != "SIMULATED":
        raise ValueError("Only a simulated scenario can be held")
    return replace(scenario, state="HELD_PENDING_AUTHORIZATION")


def required_authorization_scopes(scenario: Scenario) -> tuple[str, ...]:
    scopes = {"assignment_changes"}
    if scenario.impacts.displaced_projects:
        scopes.add("portfolio_displacement")
    if scenario.impacts.overtime_minutes_by_staff:
        scopes.add("overtime")
    return tuple(sorted(scopes))


def authorize_scenario(
    scenario: Scenario,
    authorized_by: str,
    scopes: tuple[str, ...],
) -> Authorization:
    if scenario.state != "HELD_PENDING_AUTHORIZATION":
        raise AuthorizationError("Scenario must be held before authorization")
    required = set(required_authorization_scopes(scenario))
    supplied = set(scopes)
    if not required.issubset(supplied):
        missing = ", ".join(sorted(required - supplied))
        raise AuthorizationError(f"Authorization is missing scopes: {missing}")
    payload = {
        "scenario_id": scenario.scenario_id,
        "scenario_version": scenario.version,
        "change_set_digest": scenario.change_set_digest,
        "authorized_by": authorized_by,
        "scopes": sorted(scopes),
    }
    return Authorization(
        authorization_id=f"auth-{stable_digest(payload)[:12]}",
        scenario_id=scenario.scenario_id,
        scenario_version=scenario.version,
        change_set_digest=scenario.change_set_digest,
        authorized_by=authorized_by,
        scopes=tuple(sorted(scopes)),
    )


def revalidate_scenario(
    scenario: Scenario,
    observed_baseline_revision_id: str,
) -> RevalidationResult:
    if observed_baseline_revision_id != scenario.baseline_revision_id:
        return RevalidationResult(
            scenario_id=scenario.scenario_id,
            scenario_version=scenario.version,
            expected_baseline_revision_id=scenario.baseline_revision_id,
            observed_baseline_revision_id=observed_baseline_revision_id,
            status="STALE_REJECTED",
            reasons=(
                "Observed operational revision does not match the scenario baseline.",
                "Slice 0 uses a conservative exact-revision policy and does not rebase authorization.",
            ),
        )
    return RevalidationResult(
        scenario_id=scenario.scenario_id,
        scenario_version=scenario.version,
        expected_baseline_revision_id=scenario.baseline_revision_id,
        observed_baseline_revision_id=observed_baseline_revision_id,
        status="VALID",
        reasons=("Exact baseline revision match confirmed.",),
    )


def apply_authorized_scenario(
    scenario: Scenario,
    authorization: Authorization,
    revalidation: RevalidationResult,
) -> AppliedOperationalRevision:
    if authorization.scenario_id != scenario.scenario_id:
        raise AuthorizationError("Authorization targets a different scenario")
    if authorization.scenario_version != scenario.version:
        raise AuthorizationError("Authorization targets a different scenario version")
    if authorization.change_set_digest != scenario.change_set_digest:
        raise AuthorizationError("Authorization targets a different change set")
    if not set(required_authorization_scopes(scenario)).issubset(authorization.scopes):
        raise AuthorizationError("Authorization scopes no longer cover the scenario")
    if revalidation.status != "VALID":
        raise StaleBaselineError("Scenario baseline is stale")
    if (
        revalidation.scenario_id != scenario.scenario_id
        or revalidation.scenario_version != scenario.version
    ):
        raise StaleBaselineError("Revalidation does not cover this exact scenario version")

    assignments = flatten_intervals(scenario.schedule.intervals)
    trace = {
        "baseline_revision_id": scenario.baseline_revision_id,
        "scenario_id": scenario.scenario_id,
        "scenario_version": scenario.version,
        "authorization_id": authorization.authorization_id,
        "change_set_digest": scenario.change_set_digest,
        "applied_change_count": len(scenario.proposed_changes),
    }
    return AppliedOperationalRevision(
        revision_id=f"operational-{stable_digest({'trace': trace, 'assignments': assignments})[:12]}",
        prior_revision_id=scenario.baseline_revision_id,
        scenario_id=scenario.scenario_id,
        scenario_version=scenario.version,
        authorization_id=authorization.authorization_id,
        change_set_digest=scenario.change_set_digest,
        assignments=assignments,
        trace=trace,
    )


def _envelope(kind: str, payload: Any) -> dict[str, Any]:
    return {
        "schema_version": SCHEMA_VERSION,
        "kind": kind,
        "payload": to_primitive(payload),
    }


def _scenario_evidence(scenario: Scenario) -> dict[str, Any]:
    return {
        "scenario_id": scenario.scenario_id,
        "version": scenario.version,
        "state": scenario.state,
        "baseline_revision_id": scenario.baseline_revision_id,
        "request_id": scenario.request_id,
        "target_project_id": scenario.target_project_id,
        "constraints": scenario.constraints,
        "project_completion_minutes": scenario.schedule.project_completion_minutes,
        "overtime_minutes_by_staff": scenario.schedule.overtime_minutes_by_staff,
        "impacts": scenario.impacts,
        "explanations": scenario.explanations,
        "proposed_change_count": len(scenario.proposed_changes),
        "change_set_digest": scenario.change_set_digest,
        "operational_truth": False,
    }


def run_slice0(fixtures_dir: Path) -> dict[str, dict[str, Any]]:
    portfolio = load_portfolio(fixtures_dir / "project_x_portfolio_v0.json")
    request = load_request(fixtures_dir / "expedite_project_x_request_v0.json")

    no_overtime = ConstraintSet(max_overtime_minutes_per_staff=0)
    negotiated_overtime = ConstraintSet(max_overtime_minutes_per_staff=60)
    baseline = schedule_portfolio(
        portfolio, portfolio.baseline_project_order, no_overtime
    )
    scenario_v1 = simulate(portfolio, request, baseline, 1, no_overtime)
    scenario_v2 = simulate(portfolio, request, baseline, 2, negotiated_overtime)
    held = hold_scenario(scenario_v2)
    authorization = authorize_scenario(
        held,
        authorized_by="synthetic-budget-owner",
        scopes=("assignment_changes", "overtime", "portfolio_displacement"),
    )
    stale_revalidation = revalidate_scenario(held, "portfolio-r2-unreviewed-change")
    valid_revalidation = revalidate_scenario(held, portfolio.revision_id)
    applied = apply_authorized_scenario(held, authorization, valid_revalidation)

    baseline_payload = {
        "revision_id": portfolio.revision_id,
        "organization_id": portfolio.organization_id,
        "workspace_id": portfolio.workspace_id,
        "baseline_project_order": portfolio.baseline_project_order,
        "project_completion_minutes": baseline.project_completion_minutes,
        "assignments": flatten_intervals(baseline.intervals),
        "operational_truth": True,
        "derived_reasoning_state": False,
    }
    held_payload = {
        **_scenario_evidence(held),
        "authorization_present": False,
        "applied": False,
    }
    stale_payload = {
        "revalidation": to_primitive(stale_revalidation),
        "application_attempt": {
            "status": "REJECTED",
            "reason": "STALE_BASELINE",
            "operational_state_mutated": False,
        },
    }

    return {
        "00_baseline.json": _envelope("baseline", baseline_payload),
        "01_simulated_current_constraints.json": _envelope(
            "scenario", _scenario_evidence(scenario_v1)
        ),
        "02_simulated_overtime_one_hour.json": _envelope(
            "scenario", _scenario_evidence(scenario_v2)
        ),
        "03_held_scenario.json": _envelope("held_scenario", held_payload),
        "04_authorized_change_set.json": _envelope("authorization", authorization),
        "05_stale_execution_rejected.json": _envelope("revalidation", stale_payload),
        "06_applied_operational_revision.json": _envelope("applied_revision", applied),
    }


def write_evidence(fixtures_dir: Path, output_dir: Path) -> dict[str, dict[str, Any]]:
    evidence = run_slice0(fixtures_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    for filename, payload in evidence.items():
        (output_dir / filename).write_text(
            canonical_json(payload) + "\n", encoding="utf-8"
        )
    return evidence
