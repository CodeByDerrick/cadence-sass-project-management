# Expedition Simulation System Shape

**Status:** Provisional architecture synthesis  
**Derived from:** `docs/origin/project_manager_expedition_scenario.md` and `docs/product/expedition_orchestration_product_synthesis.md`  
**Authority posture:** Architecture pressure map only; not implementation authority, final schema, algorithm selection, security guarantee, or roadmap commitment

## 1. Purpose

The project-manager expedition scenario requires more than a conversational interface attached to a project database. It implies a system that can safely distinguish and coordinate:

1. current operational reality,
2. user intent,
3. inferred and explicit constraints,
4. counterfactual schedules,
5. portfolio impacts,
6. human review,
7. organizational authorization, and
8. execution into live state.

The core architectural danger is a collapse between **simulation and mutation**.

A generated plan must not become a live assignment merely because a model produced it. A held scenario must not masquerade as the current schedule. An approval must be attributable to an authorized actor. An executable plan must be revalidated when its baseline has materially changed.

This document sketches the minimum system shape implied by those pressures.

## 2. Architectural center

The system can be understood as four truth layers and a controlled transition path between them.

### Layer A: Operational source truth

The best available record of the organization's current projects, tasks, dependencies, assignments, availability, deadlines, work calendars, and other authoritative constraints.

Examples:

- Project X contains tasks A, B, C, and D.
- Task C depends on Task B.
- Jill is unavailable on Tuesday and Wednesday due to approved PTO.
- Sam is qualified for Task D; Alex is not.
- Project Y has a committed deadline on July 24.

This layer should not be silently rewritten by simulation.

### Layer B: Derived operational model

A normalized graph or model used for reasoning.

It may combine authoritative records from multiple sources into a structure suitable for scheduling and impact analysis. Derived normalization must retain provenance to the operational records from which it came.

### Layer C: Scenario state

A counterfactual proposal built from a known baseline revision.

A scenario may contain:

- changed priority,
- user-supplied constraints,
- algorithmic assumptions,
- proposed assignments,
- projected completion dates,
- portfolio displacement,
- overtime,
- cost change,
- deadline effects,
- explanations,
- confidence or uncertainty indicators, and
- approval requirements.

A scenario is not live operational truth.

### Layer D: Authorized operational change

A reviewed and authorized change set that is allowed to mutate live assignments or other operational records within explicit scope.

The transition from Layer C to Layer D is the critical governance boundary.

## 3. Conceptual subsystem map

The scenario suggests the following subsystem responsibilities.

### 3.1 Operational data adapters

Purpose: ingest or synchronize authoritative project and workforce context from internal sources.

Potential inputs may eventually include:

- native Cadence project records,
- calendars,
- HR or PTO systems,
- project-management platforms,
- time tracking,
- payroll or cost systems,
- identity and access systems,
- skills or qualification records, and
- manually maintained organization policy.

Only project, task, staff capability, PTO, deadline, overtime, and cost pressures are directly evidenced by the scenario. Specific integrations remain undecided.

### 3.2 Operational graph / planning model

Purpose: produce a normalized reasoning surface from current records.

The model likely needs to represent relationships among:

- organization,
- workspace,
- project,
- task,
- dependency,
- staff member,
- capability,
- qualification,
- availability,
- assignment,
- work interval,
- milestone,
- deadline,
- cost rule,
- overtime rule,
- policy constraint, and
- approval requirement.

The exact data model remains open.

### 3.3 Constraint classifier

Purpose: determine how each scheduling constraint should behave.

At minimum, constraints should not be treated as one undifferentiated list. A useful provisional taxonomy is:

#### Hard constraint

Must not be violated by the scheduler.

Examples may include:

- approved PTO,
- missing mandatory qualification,
- impossible dependency order,
- legal or policy prohibition,
- maximum authorized overtime.

#### Soft constraint

May be traded when producing a scenario, but the tradeoff must be visible.

Examples may include:

- preferred task continuity,
- target completion date,
- preferred assignee,
- minimizing context switching.

#### Objective

Something the scheduler is actively trying to improve.

Examples:

- finish Project X earlier,
- minimize delay to other projects,
- minimize added cost,
- maximize parallel throughput.

#### Guardrail

A policy that may sit above individual scenarios and define what the system is never allowed to propose or execute without higher authority.

Examples may eventually include:

- protected rest requirements,
- fairness limits,
- labor rules,
- budget ceilings,
- restricted assignment classes.

The system must preserve the source and authority behind each constraint classification.

### 3.4 Scheduling and optimization engine

Purpose: produce feasible plans under a supplied objective and constraint set.

This engine should not be assumed to be an LLM.

A robust system may use combinations of:

- deterministic dependency analysis,
- critical-path methods,
- constraint programming,
- mixed-integer optimization,
- heuristic search,
- simulation,
- learned estimators, and
- LLM reasoning for interpretation or explanation.

No algorithm is selected by this document.

The important boundary is that a language model should not invent feasibility merely because a proposal sounds plausible. Schedule feasibility should be grounded in explicit operational constraints and validated by an appropriate planning mechanism.

### 3.5 Scenario simulator

Purpose: generate one or more counterfactual schedule states without modifying live operations.

Each scenario should be tied to:

- a baseline revision,
- a triggering request or objective,
- the constraint set used,
- assumptions,
- proposed changes,
- projected outputs,
- portfolio impacts,
- generation timestamp,
- derivation lineage, and
- current validity state.

Multiple scenarios may coexist for comparison.

### 3.6 Portfolio impact analyzer

Purpose: determine the consequences of a proposed schedule beyond the target project.

Potential outputs:

- target project completion delta,
- other projects delayed,
- amount of delay,
- newly threatened deadlines,
- deadlines crossed,
- assignments changed,
- unassigned tasks,
- overtime introduced,
- incremental cost,
- staff utilization changes,
- protected time conflicts,
- unresolved constraints,
- risks and assumptions.

The system should be able to answer both aggregate and specific questions, such as:

> Which projects are delayed the most?

and:

> Why is Jill unscheduled on Tuesday and Wednesday?

### 3.7 Explanation engine

Purpose: translate schedule structure and constraint causes into grounded explanations.

An explanation should ideally identify:

1. the visible outcome,
2. the causal constraint or optimization choice,
3. the source record or policy behind it,
4. whether it was hard, soft, assumed, inferred, or user-supplied, and
5. what would need to change for a different outcome to become feasible.

Example:

> Jill is not scheduled on Tuesday or Wednesday because approved PTO marks her unavailable during those work periods. The simulator treated that availability record as a hard constraint. Removing it would require an authorized change to the underlying availability record, not a scheduling override.

This is stronger than a generic natural-language justification because it remains tied to actual system state.

### 3.8 Conversational orchestration layer

Purpose: translate human intent into inspectable operations without giving the language model hidden execution authority.

Example interaction:

> Expedite Project X.

may become a structured request such as:

- target project: Project X,
- objective: earliest feasible completion,
- preserve current hard constraints: yes,
- portfolio impact: calculate,
- mutation permission: none,
- result mode: generate scenarios.

A follow-up such as:

> Overtime is allowed, but only one hour for each staff member involved.

should become an explicit scenario constraint rather than remaining buried in chat history.

### 3.9 Scenario repository

Purpose: store durable proposals separately from live operational state.

A held strategy should remain inspectable as a first-class record.

A provisional scenario record may need:

- scenario identifier,
- organization/workspace,
- target objective,
- baseline revision identifier,
- originating source or conversation reference,
- created by,
- created at,
- constraints,
- assumptions,
- proposed changes,
- projected outcomes,
- portfolio impacts,
- explanations,
- required approvals,
- review state,
- validity state,
- authorization state,
- expiration or revalidation policy,
- execution state,
- supersession lineage.

Exact fields remain undecided.

### 3.10 Approval and authorization service

Purpose: determine whether a proposal has the necessary human authority to progress toward execution.

Approval requirements may be conditional.

For example:

- ordinary reassignment may require project-manager authority,
- overtime may require department approval,
- added cost above a threshold may require budget-owner approval,
- moving a contractual deadline may require executive or client approval,
- pausing an entire portfolio may require higher authority.

The source scenario directly evidences approval for overtime, cost, and delay consequences. More complex role rules remain future pressure.

### 3.11 Execution coordinator

Purpose: convert an authorized scenario into bounded operational mutations.

Responsibilities may include:

- final baseline validation,
- stale-scenario detection,
- authorization validation,
- change-set generation,
- transactional or compensating update handling,
- assignment updates,
- schedule projection updates,
- downstream integration calls,
- partial-failure reporting,
- resulting operational revision creation, and
- traceability back to the authorized scenario.

Execution should use the exact approved scope rather than asking the AI to reinterpret authorization at the moment of mutation.

### 3.12 Audit and provenance layer

Purpose: make consequential operational change reviewable.

A minimum trace should answer:

- What was the baseline?
- What request triggered the scenario?
- Which constraints were used?
- What did the AI or planner propose?
- What did a human change?
- What consequences were shown?
- Who approved what?
- What exact changes were authorized?
- What was executed?
- What failed or changed afterward?

This does not require prematurely designing a compliance-grade event-sourcing platform. It does require preserving the distinction between proposal, approval, and execution.

## 4. Scenario lifecycle

A provisional lifecycle is:

`DRAFT -> SIMULATED -> UNDER_REVIEW -> HELD_PENDING_APPROVAL -> AUTHORIZED -> READY_FOR_EXECUTION -> EXECUTING -> APPLIED`

Alternative terminal or side states may include:

- `REJECTED`
- `CANCELLED`
- `SUPERSEDED`
- `STALE`
- `INVALIDATED`
- `PARTIALLY_APPLIED`
- `FAILED`

These names are not final schema terms. The deeper requirement is explicit state separation.

### 4.1 DRAFT

The scenario objective or constraints are still being assembled.

### 4.2 SIMULATED

At least one feasible or infeasible result has been computed against a known baseline.

### 4.3 UNDER_REVIEW

The manager is inspecting consequences and negotiating constraints.

### 4.4 HELD_PENDING_APPROVAL

The scenario is intentionally preserved but cannot mutate live operations.

### 4.5 AUTHORIZED

Required approval has been recorded for a specific proposal version and scope.

### 4.6 READY_FOR_EXECUTION

The system has revalidated the baseline and confirmed that the authorized change remains executable.

### 4.7 EXECUTING

The bounded change set is being applied.

### 4.8 APPLIED

The authorized changes were successfully incorporated into operational state, producing a new operational revision.

## 5. Baseline revision and stale-scenario detection

The phrase **hold this strategy in place and wait for approval** creates a temporal problem.

While approval is pending:

- tasks may finish,
- estimates may change,
- new urgent work may arrive,
- staff may call out,
- PTO may be added,
- costs may change,
- deadlines may move,
- another scenario may already have been executed.

A held proposal therefore needs a known baseline revision.

Before execution, the system should compare the current operational state with that baseline and determine whether changes are:

### Non-material

The scenario remains safe to execute.

### Material but reconcilable

The scenario can be recomputed or rebased, with consequences shown again.

### Invalidating

The proposal can no longer be executed as approved and must return to review.

The classification policy remains open, but silent execution against materially changed reality should be avoided.

## 6. Proposed scenario contract pressure

A scenario should conceptually answer the following questions.

### Identity

- Which scenario is this?
- Which version is being reviewed?
- Which organization and workspace does it belong to?

### Origin

- Who or what requested it?
- What user intent triggered it?
- Which source conversation or operation created it?

### Baseline

- Against which operational revision was it simulated?
- Is that baseline still current enough to execute?

### Objective

- What is the scenario trying to improve?
- How is success measured?

### Constraints

- Which hard constraints are enforced?
- Which soft constraints are considered?
- Which constraints were added by a human during conversation?
- Which came from organization policy?
- Which were inferred and therefore require review?

### Proposal

- Which assignments, start dates, or project states would change?
- Which tasks remain unchanged?

### Impact

- What improves?
- What gets worse?
- Which deadlines are threatened?
- What does it cost?
- Who is affected?

### Explanation

- Why is the proposal feasible?
- Why do gaps remain?
- Why were particular people selected?

### Approval

- What specific consequences require approval?
- Who has authority?
- Which exact scenario version was approved?

### Execution

- What exact mutations are authorized?
- What happened when they were applied?

## 7. Visual projections should not become truth

The source scenario describes a two-dimensional timeline with project tasks distributed across staff lanes.

This is best treated as a **projection** over the operational and scenario models.

Possible visual states include:

- current portfolio projection,
- focused Project X projection,
- baseline schedule projection,
- proposed scenario overlay,
- delta view,
- staff-lane view,
- dependency view,
- cost impact view,
- deadline-risk view,
- approval view.

The same underlying records may support many views. A bar dragged on a screen should not silently become authoritative unless the resulting operation passes through the appropriate change boundary.

This aligns with the companion Cadence strategy principle that views and lenses organize or emphasize underlying material without becoming source truth themselves.

## 8. AI operating layer implications

The scenario contains several different reasoning workloads. They should not necessarily use the same model, execution environment, or reasoning depth.

Possible routing classes include:

### Lightweight local or deterministic work

- selecting Project X,
- filtering visible tasks,
- identifying existing PTO,
- formatting known deadline deltas,
- basic constraint lookup.

### Optimization work

- dependency analysis,
- capacity allocation,
- schedule feasibility,
- scenario generation,
- portfolio impact calculation.

This may be better served by deterministic optimization systems than by an LLM.

### Language reasoning

- interpreting the manager's intent,
- converting conversation into explicit constraints,
- summarizing tradeoffs,
- answering grounded why-questions.

### High-complexity escalated reasoning

- comparing many conflicting objectives,
- analyzing ambiguous organizational policy,
- constructing executive decision summaries,
- performing deeper research when external information is required.

The broader Cadence direction supports an AI operating layer that chooses reasoning level and model based on task, with local-first handling where practical and privacy-preserving cloud escalation when justified. For this SaaS product, the same principle should be examined against organizational data sensitivity, performance, auditability, and customer deployment needs.

No routing architecture is approved here.

## 9. Privacy and workforce sensitivity pressure

This product may handle information about:

- staff availability,
- PTO,
- qualifications,
- productivity estimates,
- assignments,
- overtime,
- compensation-related cost,
- performance-relevant work history,
- potentially protected leave or other sensitive employment context.

The scenario only explicitly names PTO, skills/capability, overtime, and cost. The broader category list is a warning about likely architectural pressure.

The system should avoid casually exposing more sensitive context than a manager needs to make the scheduling decision.

For example, an explanation may need to say:

> Jill is unavailable due to approved protected time.

rather than exposing private underlying details that are irrelevant to assignment planning.

Exact privacy, employment, labor, retention, and legal requirements require separate analysis.

## 10. Fairness, burnout, and optimization risk

A scheduler that maximizes throughput can still create harmful outcomes.

Possible failure modes include:

- repeatedly assigning urgent work to the fastest staff member,
- overloading highly qualified people,
- creating excessive context switching,
- penalizing staff for PTO or protected leave,
- using inferred capability as hidden employment judgment,
- optimizing cost by systematically disadvantaging certain people,
- treating every visible gap as inefficiency,
- creating mathematically feasible but culturally impossible schedules.

Therefore, organizational throughput should not be the only objective.

Future design should consider explicit guardrails around:

- workload distribution,
- fatigue and rest,
- context switching,
- continuity,
- fairness,
- protected time,
- manager override,
- staff visibility, and
- appeal or correction mechanisms.

These are design pressures, not yet approved product features.

## 11. Failure and uncertainty behavior

The system must be able to say when no feasible plan exists.

Examples:

- Project X cannot finish by Friday without violating Jill's PTO and a mandatory dependency.
- The requested one-hour overtime cap is insufficient to achieve the target date.
- The cost impact cannot be calculated because current rate data is unavailable.
- Staff capability records are incomplete.
- The schedule changed materially while approval was pending.

A trustworthy system should surface the blocking facts and possible next decisions rather than fabricate a plan.

## 12. Minimum execution safety boundary

Before an authorized scenario mutates live operations, the execution coordinator should conceptually verify:

1. The scenario version is the one that was approved.
2. The approver had authority for the consequences authorized.
3. Required approvals are complete.
4. The baseline has not changed in a material unreviewed way.
5. Hard constraints are still satisfied.
6. The exact change set is bounded and inspectable.
7. Downstream systems required for execution are available or failure behavior is understood.
8. Execution results will remain attributable to the scenario and approval.

This is the minimum trust shape implied by the narrative.

## 13. Architectural non-decisions

This document does not select:

- programming language,
- framework,
- database,
- event bus,
- cloud provider,
- model provider,
- local model,
- optimization library,
- solver,
- agent framework,
- multi-tenant design,
- deployment model,
- data residency policy,
- authorization framework,
- integration platform,
- event-sourcing architecture,
- vector database,
- schema,
- API design,
- UI framework,
- mobile architecture, or
- implementation sequence.

Those decisions should be earned by validated product requirements and technical evidence.

## 14. Recommended conceptual architecture chain

The scenario can be summarized as the following controlled chain:

`Operational Records`

-> `Normalized Operational Model`

-> `User Intent + Explicit Constraints`

-> `Constraint Classification`

-> `Scenario Simulation`

-> `Portfolio Impact Analysis`

-> `Grounded Explanation`

-> `Human Review and Constraint Negotiation`

-> `Held Scenario`

-> `Required Approval`

-> `Baseline Revalidation`

-> `Bounded Authorized Change Set`

-> `Execution`

-> `New Operational Revision + Traceability`

The most important architectural rule is:

> **No arrow in this chain should be treated as implicit permission to skip the next trust boundary.**

## 15. Strongest architecture conclusion

The source scenario does not merely call for smarter scheduling.

It calls for a system capable of maintaining a disciplined separation among:

- what is true now,
- what might be possible,
- what the AI recommends,
- what the human prefers,
- what the organization authorizes, and
- what the system actually changes.

That separation is the architectural heart of trustworthy project orchestration in Cadence SaaS Project Management.
