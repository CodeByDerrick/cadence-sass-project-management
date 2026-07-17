from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable

from .model import (
    MINUTES_PER_DAY,
    OVERTIME_WINDOW_MINUTES,
    REGULAR_DAY_MINUTES,
    WORKDAY_START_MINUTE,
    ConstraintSet,
    Portfolio,
    Schedule,
    StaffMember,
    Task,
    WorkInterval,
)


class InfeasibleScheduleError(RuntimeError):
    """Raised when the prototype cannot produce a feasible schedule."""


@dataclass(frozen=True)
class _AvailabilityChunk:
    start_minute: int
    end_minute: int
    overtime: bool


@dataclass(frozen=True)
class _TaskPlan:
    staff_id: str
    intervals: tuple[WorkInterval, ...]
    completion_minute: int
    overtime_minutes: int


def _subtract_reservations(
    chunk: _AvailabilityChunk,
    reservations: Iterable[WorkInterval],
) -> tuple[_AvailabilityChunk, ...]:
    segments = [(chunk.start_minute, chunk.end_minute)]
    for reservation in sorted(reservations, key=lambda item: item.start_minute):
        next_segments: list[tuple[int, int]] = []
        for start, end in segments:
            if reservation.end_minute <= start or reservation.start_minute >= end:
                next_segments.append((start, end))
                continue
            if reservation.start_minute > start:
                next_segments.append((start, reservation.start_minute))
            if reservation.end_minute < end:
                next_segments.append((reservation.end_minute, end))
        segments = next_segments
    return tuple(
        _AvailabilityChunk(start, end, chunk.overtime)
        for start, end in segments
        if end > start
    )


def _availability_chunks(
    portfolio: Portfolio,
    staff: StaffMember,
    reservations: Iterable[WorkInterval],
    earliest_start: int,
    allow_overtime: bool,
    overtime_budget_remaining: int,
) -> tuple[_AvailabilityChunk, ...]:
    chunks: list[_AvailabilityChunk] = []
    overtime_remaining = overtime_budget_remaining
    staff_reservations = tuple(item for item in reservations if item.staff_id == staff.id)

    for day in range(portfolio.horizon_days):
        if day in staff.pto_days:
            continue
        regular_start = day * MINUTES_PER_DAY + WORKDAY_START_MINUTE
        regular_end = regular_start + REGULAR_DAY_MINUTES
        regular_chunk = _AvailabilityChunk(
            max(regular_start, earliest_start),
            regular_end,
            False,
        )
        if regular_chunk.end_minute > regular_chunk.start_minute:
            chunks.extend(_subtract_reservations(regular_chunk, staff_reservations))

        if allow_overtime and overtime_remaining > 0:
            overtime_start = regular_end
            overtime_end = overtime_start + min(OVERTIME_WINDOW_MINUTES, overtime_remaining)
            overtime_chunk = _AvailabilityChunk(
                max(overtime_start, earliest_start),
                overtime_end,
                True,
            )
            if overtime_chunk.end_minute > overtime_chunk.start_minute:
                free_overtime = _subtract_reservations(overtime_chunk, staff_reservations)
                chunks.extend(free_overtime)
                overtime_remaining -= sum(
                    item.end_minute - item.start_minute for item in free_overtime
                )

    return tuple(sorted(chunks, key=lambda item: (item.start_minute, item.overtime)))


def _plan_task_for_staff(
    portfolio: Portfolio,
    task: Task,
    staff: StaffMember,
    reservations: tuple[WorkInterval, ...],
    earliest_start: int,
    allow_overtime: bool,
    overtime_budget_remaining: int,
) -> _TaskPlan | None:
    remaining = task.effort_minutes
    intervals: list[WorkInterval] = []
    overtime_minutes = 0

    for chunk in _availability_chunks(
        portfolio,
        staff,
        reservations,
        earliest_start,
        allow_overtime,
        overtime_budget_remaining,
    ):
        if remaining <= 0:
            break
        available = chunk.end_minute - chunk.start_minute
        used = min(remaining, available)
        interval = WorkInterval(
            staff_id=staff.id,
            task_id=task.id,
            project_id=task.project_id,
            start_minute=chunk.start_minute,
            end_minute=chunk.start_minute + used,
            overtime=chunk.overtime,
        )
        intervals.append(interval)
        if chunk.overtime:
            overtime_minutes += used
        remaining -= used

    if remaining > 0 or not intervals:
        return None
    return _TaskPlan(
        staff_id=staff.id,
        intervals=tuple(intervals),
        completion_minute=intervals[-1].end_minute,
        overtime_minutes=overtime_minutes,
    )


def _choose_task_plan(
    portfolio: Portfolio,
    task: Task,
    reservations: tuple[WorkInterval, ...],
    earliest_start: int,
    constraints: ConstraintSet,
    overtime_used: dict[str, int],
    overtime_project_id: str | None,
) -> _TaskPlan:
    candidates: list[_TaskPlan] = []
    for staff_id in task.eligible_staff_ids:
        staff = portfolio.staff_by_id[staff_id]
        if task.required_capability not in staff.capabilities:
            continue
        if constraints.explicit_eligibility_only and staff_id not in task.eligible_staff_ids:
            continue
        allow_overtime = (
            overtime_project_id == task.project_id
            and constraints.max_overtime_minutes_per_staff > 0
        )
        remaining_budget = max(
            0,
            constraints.max_overtime_minutes_per_staff - overtime_used.get(staff_id, 0),
        )
        plan = _plan_task_for_staff(
            portfolio,
            task,
            staff,
            reservations,
            earliest_start,
            allow_overtime,
            remaining_budget,
        )
        if plan is not None:
            candidates.append(plan)

    if not candidates:
        raise InfeasibleScheduleError(
            f"No eligible staff can complete task {task.id} within the fixture horizon"
        )

    def sort_key(plan: _TaskPlan) -> tuple[int, int, str]:
        preferred_rank = 0 if plan.staff_id == task.preferred_staff_id else 1
        return (plan.completion_minute, preferred_rank, plan.staff_id)

    return min(candidates, key=sort_key)


def schedule_portfolio(
    portfolio: Portfolio,
    project_order: tuple[str, ...],
    constraints: ConstraintSet,
    overtime_project_id: str | None = None,
) -> Schedule:
    if set(project_order) != set(portfolio.project_by_id):
        raise ValueError("Project order must contain each fixture project exactly once")

    reservations: tuple[WorkInterval, ...] = ()
    task_completion: dict[str, int] = {}
    overtime_used = {staff.id: 0 for staff in portfolio.staff}

    for project_id in project_order:
        project = portfolio.project_by_id[project_id]
        for task_id in project.task_ids:
            task = portfolio.task_by_id[task_id]
            missing_dependencies = [
                dependency
                for dependency in task.dependencies
                if dependency not in task_completion
            ]
            if missing_dependencies:
                raise InfeasibleScheduleError(
                    f"Task {task.id} was ordered before dependencies {missing_dependencies}"
                )
            earliest_start = max(
                (task_completion[dependency] for dependency in task.dependencies),
                default=0,
            )
            plan = _choose_task_plan(
                portfolio,
                task,
                reservations,
                earliest_start,
                constraints,
                overtime_used,
                overtime_project_id,
            )
            reservations = reservations + plan.intervals
            task_completion[task.id] = plan.completion_minute
            overtime_used[plan.staff_id] += plan.overtime_minutes

    project_completion = {
        project.id: max(task_completion[task_id] for task_id in project.task_ids)
        for project in portfolio.projects
    }
    return Schedule(
        intervals=tuple(
            sorted(
                reservations,
                key=lambda item: (
                    item.start_minute,
                    item.staff_id,
                    item.task_id,
                    item.end_minute,
                ),
            )
        ),
        project_completion_minutes=project_completion,
        task_completion_minutes=task_completion,
        overtime_minutes_by_staff={
            staff_id: minutes
            for staff_id, minutes in sorted(overtime_used.items())
            if minutes > 0
        },
    )
