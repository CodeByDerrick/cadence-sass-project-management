from __future__ import annotations

from dataclasses import asdict, dataclass
from decimal import Decimal
from hashlib import sha256
import json
from pathlib import Path
from typing import Any, Iterable

MINUTES_PER_DAY = 24 * 60
WORKDAY_START_MINUTE = 9 * 60
REGULAR_DAY_MINUTES = 8 * 60
OVERTIME_WINDOW_MINUTES = 60


@dataclass(frozen=True)
class StaffMember:
    id: str
    name: str
    capabilities: tuple[str, ...]
    pto_days: tuple[int, ...]
    hourly_rate: Decimal


@dataclass(frozen=True)
class Task:
    id: str
    project_id: str
    name: str
    required_capability: str
    effort_minutes: int
    dependencies: tuple[str, ...] = ()
    eligible_staff_ids: tuple[str, ...] = ()
    preferred_staff_id: str | None = None


@dataclass(frozen=True)
class Project:
    id: str
    name: str
    priority: int
    deadline_minute: int
    task_ids: tuple[str, ...]


@dataclass(frozen=True)
class Portfolio:
    organization_id: str
    workspace_id: str
    revision_id: str
    horizon_days: int
    overtime_multiplier: Decimal
    staff: tuple[StaffMember, ...]
    projects: tuple[Project, ...]
    tasks: tuple[Task, ...]
    baseline_project_order: tuple[str, ...]

    @property
    def staff_by_id(self) -> dict[str, StaffMember]:
        return {member.id: member for member in self.staff}

    @property
    def project_by_id(self) -> dict[str, Project]:
        return {project.id: project for project in self.projects}

    @property
    def task_by_id(self) -> dict[str, Task]:
        return {task.id: task for task in self.tasks}


@dataclass(frozen=True)
class ExpeditionRequest:
    request_id: str
    requested_by: str
    target_project_id: str
    objective: str
    preserve_hard_constraints: bool


@dataclass(frozen=True)
class WorkInterval:
    staff_id: str
    task_id: str
    project_id: str
    start_minute: int
    end_minute: int
    overtime: bool

    @property
    def duration_minutes(self) -> int:
        return self.end_minute - self.start_minute


@dataclass(frozen=True)
class Schedule:
    intervals: tuple[WorkInterval, ...]
    project_completion_minutes: dict[str, int]
    task_completion_minutes: dict[str, int]
    overtime_minutes_by_staff: dict[str, int]


@dataclass(frozen=True)
class ConstraintSet:
    max_overtime_minutes_per_staff: int
    explicit_eligibility_only: bool = True
    pto_is_hard: bool = True
    dependencies_are_hard: bool = True


@dataclass(frozen=True)
class PortfolioImpact:
    target_completion_delta_minutes: int
    project_completion_deltas: dict[str, int]
    deadlines_crossed: tuple[str, ...]
    overtime_minutes_by_staff: dict[str, int]
    overtime_compensation: str
    incremental_overtime_premium: str
    displaced_projects: tuple[str, ...]


@dataclass(frozen=True)
class Explanation:
    code: str
    summary: str
    fact_refs: tuple[str, ...]


@dataclass(frozen=True)
class Scenario:
    scenario_id: str
    version: int
    baseline_revision_id: str
    request_id: str
    target_project_id: str
    state: str
    constraints: ConstraintSet
    schedule: Schedule
    impacts: PortfolioImpact
    explanations: tuple[Explanation, ...]
    proposed_changes: tuple[dict[str, Any], ...]
    change_set_digest: str


@dataclass(frozen=True)
class Authorization:
    authorization_id: str
    scenario_id: str
    scenario_version: int
    change_set_digest: str
    authorized_by: str
    scopes: tuple[str, ...]
    state: str = "AUTHORIZED"


@dataclass(frozen=True)
class RevalidationResult:
    scenario_id: str
    scenario_version: int
    expected_baseline_revision_id: str
    observed_baseline_revision_id: str
    status: str
    reasons: tuple[str, ...]


@dataclass(frozen=True)
class AppliedOperationalRevision:
    revision_id: str
    prior_revision_id: str
    scenario_id: str
    scenario_version: int
    authorization_id: str
    change_set_digest: str
    assignments: tuple[dict[str, Any], ...]
    trace: dict[str, Any]


def canonical_json(value: Any) -> str:
    return json.dumps(to_primitive(value), sort_keys=True, separators=(",", ":"), ensure_ascii=False)


def stable_digest(value: Any) -> str:
    return sha256(canonical_json(value).encode("utf-8")).hexdigest()


def to_primitive(value: Any) -> Any:
    if isinstance(value, Decimal):
        return format(value, "f")
    if hasattr(value, "__dataclass_fields__"):
        return to_primitive(asdict(value))
    if isinstance(value, dict):
        return {str(key): to_primitive(item) for key, item in value.items()}
    if isinstance(value, tuple):
        return [to_primitive(item) for item in value]
    if isinstance(value, list):
        return [to_primitive(item) for item in value]
    return value


def load_json(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as handle:
        payload = json.load(handle)
    if not isinstance(payload, dict):
        raise ValueError(f"Expected object in {path}")
    return payload


def load_portfolio(path: Path) -> Portfolio:
    data = load_json(path)
    staff = tuple(
        StaffMember(
            id=item["id"],
            name=item["name"],
            capabilities=tuple(item["capabilities"]),
            pto_days=tuple(item.get("pto_days", [])),
            hourly_rate=Decimal(str(item["hourly_rate"])),
        )
        for item in data["staff"]
    )
    projects = tuple(
        Project(
            id=item["id"],
            name=item["name"],
            priority=int(item["priority"]),
            deadline_minute=int(item["deadline_minute"]),
            task_ids=tuple(item["task_ids"]),
        )
        for item in data["projects"]
    )
    tasks = tuple(
        Task(
            id=item["id"],
            project_id=item["project_id"],
            name=item["name"],
            required_capability=item["required_capability"],
            effort_minutes=int(item["effort_minutes"]),
            dependencies=tuple(item.get("dependencies", [])),
            eligible_staff_ids=tuple(item["eligible_staff_ids"]),
            preferred_staff_id=item.get("preferred_staff_id"),
        )
        for item in data["tasks"]
    )
    return Portfolio(
        organization_id=data["organization_id"],
        workspace_id=data["workspace_id"],
        revision_id=data["revision_id"],
        horizon_days=int(data["horizon_days"]),
        overtime_multiplier=Decimal(str(data["overtime_multiplier"])),
        staff=staff,
        projects=projects,
        tasks=tasks,
        baseline_project_order=tuple(data["baseline_project_order"]),
    )


def load_request(path: Path) -> ExpeditionRequest:
    data = load_json(path)
    return ExpeditionRequest(
        request_id=data["request_id"],
        requested_by=data["requested_by"],
        target_project_id=data["target_project_id"],
        objective=data["objective"],
        preserve_hard_constraints=bool(data["preserve_hard_constraints"]),
    )


def money(value: Decimal) -> str:
    return format(value.quantize(Decimal("0.01")), "f")


def flatten_intervals(intervals: Iterable[WorkInterval]) -> tuple[dict[str, Any], ...]:
    return tuple(
        {
            "staff_id": interval.staff_id,
            "task_id": interval.task_id,
            "project_id": interval.project_id,
            "start_minute": interval.start_minute,
            "end_minute": interval.end_minute,
            "overtime": interval.overtime,
        }
        for interval in sorted(
            intervals,
            key=lambda item: (item.start_minute, item.staff_id, item.task_id, item.end_minute),
        )
    )
