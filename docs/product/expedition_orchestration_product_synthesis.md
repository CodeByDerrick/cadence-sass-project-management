# Expedition Orchestration Product Synthesis

**Status:** Early product synthesis  
**Derived from:** `docs/origin/project_manager_expedition_scenario.md`  
**Authority posture:** Product interpretation only; not implementation authority, final UX doctrine, pricing/market authority, or a complete requirements specification

## 1. Executive synthesis

The scenario reveals a product concept more consequential than an AI-enhanced Gantt chart or conversational task manager.

The emerging product is a **portfolio-level operational reasoning and orchestration system**. It maintains a shared model of projects, task dependencies, staff capability, availability, deadlines, costs, approvals, and competing priorities; lets a project manager ask natural-language questions about that operational reality; generates counterfactual scheduling strategies; explains the consequences; holds a selected strategy without mutating live work; and applies it only after appropriate authorization.

The distinctive interaction is:

> **Ask in natural language. See the operational reality change as a reversible simulation. Inspect why. Negotiate constraints. Approve deliberately. Then execute.**

This is the primary product insight carried forward from the source scenario.

## 2. Product thesis exposed by the scenario

Traditional project-management systems generally ask people to maintain plans. The scenario points toward a system that can also **reason over the plan as a living organizational model**.

The project manager does not manually drag dozens of bars to test an urgent request. Instead, they state the operational change:

> Expedite Project X. Show me how we might do that and the implications.

Cadence then needs enough grounded understanding to answer several classes of question at once:

- What work is required to complete Project X?
- Which tasks can safely happen in parallel?
- Which dependencies create unavoidable sequence?
- Which staff members are qualified for each task?
- Who is actually available?
- What other work must move to create capacity?
- Which deadlines or commitments become endangered?
- How much overtime or additional cost is introduced?
- What assumptions make the plan possible?
- What requires human approval before anything changes?

The value is therefore not merely automation. It is **decision compression with retained visibility**: helping a human understand a complex portfolio tradeoff quickly without hiding the causal structure or surrendering authority.

## 3. Core experience loop

The scenario produces a reusable seven-stage interaction loop.

### 3.1 Observe

The manager begins with a portfolio-level view of current projects, tasks, assignments, timing, and gaps.

### 3.2 Focus

The manager identifies a target concern through speech or another input method:

> Bring up Project X and help me understand how to expedite it.

The system isolates the relevant project while retaining portfolio context.

### 3.3 Simulate

Cadence generates one or more feasible alternatives under current organizational constraints.

The important behavior is not the number of alternatives. It is the existence of **counterfactual plans that do not alter live state**.

### 3.4 Explain and negotiate

The manager asks why gaps remain, changes overtime boundaries, investigates project delays, checks deadline effects, and refines constraints.

The plan becomes a conversational object of reasoning rather than a static generated answer.

### 3.5 Hold

The chosen strategy can be retained in a stable pending state without being applied.

This prevents a dangerous collapse between:

- proposal,
- review,
- approval, and
- execution.

### 3.6 Authorize

The appropriate person or approval chain explicitly authorizes the consequences that require approval, such as cost, overtime, deadline movement, or portfolio reprioritization.

### 3.7 Execute and observe

The system applies the authorized changes to live assignments and projections, records what changed, and exposes remaining spillover capacity or downstream recovery work.

## 4. Product capabilities revealed by the scenario

### 4.1 Portfolio-wide operational model

The system needs to reason over more than a single project. It must understand the active portfolio sufficiently to determine how advancing one project affects others.

A project should therefore be treated as part of a shared operational environment rather than an isolated island.

### 4.2 Task and dependency graph

The source scenario repeatedly assumes that some tasks can move or parallelize while others cannot.

That requires a model capable of representing at least:

- tasks and sub-tasks,
- dependency relationships,
- sequencing constraints,
- blocking conditions,
- estimated effort or duration,
- earliest feasible start,
- deadline or target date, and
- project membership.

The exact schema remains open.

### 4.3 Staff capability and eligibility

The scheduler cannot treat people as interchangeable capacity units. Some staff members can perform certain tasks and others cannot.

The product therefore needs a reviewable representation of task eligibility, which may eventually include:

- skills,
- qualifications,
- certifications,
- role boundaries,
- experience,
- equipment or access requirements,
- location restrictions, and
- organizational policy constraints.

The system should distinguish confirmed capability from inferred capability. Hidden inference should not silently become staffing authority.

### 4.4 Availability and protected time

Jill's PTO is not merely an empty calendar block. It is a constraint with meaning and authority.

The system should be able to explain that a visible gap exists because a person is unavailable and should not imply that every empty-looking interval is waste to be optimized away.

Availability may eventually include:

- work schedules,
- PTO,
- holidays,
- approved leave,
- focus blocks,
- training,
- meetings,
- travel,
- location or time-zone limitations, and
- policy-based rest constraints.

The scenario directly evidences PTO; the broader list is future capability pressure, not approved scope.

### 4.5 Counterfactual schedule simulation

The AI must be able to ask, in effect:

> What would the portfolio look like if Project X became more important than it is now?

The simulator should be able to generate alternatives under different objectives and constraints without mutating the operational plan.

Possible strategy dimensions include:

- target completion date,
- priority weight,
- maximum tolerable delay to other projects,
- overtime ceiling,
- budget ceiling,
- deadline protection rules,
- protected staff or teams,
- minimum staffing continuity, and
- willingness to pause other projects.

Only the first several are directly evidenced by the source scenario. Others remain exploratory.

### 4.6 Portfolio impact analysis

A useful acceleration plan must explain what is displaced.

The product should surface consequences such as:

- projects delayed,
- amount of projected delay,
- deadlines newly at risk or crossed,
- staff whose work changes,
- overtime introduced,
- incremental cost,
- assumptions used,
- tasks left unassigned, and
- capacity created elsewhere.

A strategy that shows only the target project's improvement is incomplete.

### 4.7 Explainable schedule gaps

A gap is not automatically a defect.

It may exist because of:

- PTO,
- dependency wait time,
- missing qualification,
- external deliverable wait time,
- equipment or location constraints,
- policy limits,
- preserved recovery time, or
- deliberate risk management.

The product should let the manager ask, **Why is this gap here?** and receive a grounded explanation linked to the actual constraint.

### 4.8 Conversational constraint negotiation

The source scenario shows the manager modifying the problem through conversation:

> Overtime is allowed, but only one hour per staff member involved.

This is a crucial interaction primitive. The user should be able to refine a simulation by adding, removing, or tightening constraints conversationally while the visible projection updates accordingly.

### 4.9 Approval hold and execution boundary

The phrase **hold this strategy in place and wait for approval** reveals a first-class product state.

A scenario should be able to exist as a durable, inspectable proposal that is:

- derived from a known portfolio state,
- not yet live,
- reviewable by authorized people,
- attributable to its assumptions and constraints,
- stable enough to approve,
- revalidated if source conditions materially change, and
- executable only after the required authorization.

This boundary is central to trustworthy AI orchestration.

### 4.10 Operational execution

After approval, Cadence is expected to do more than write a report. The source scenario expects authorized changes to become actual operational assignments and projections.

That introduces a major product boundary between:

- advisory AI,
- proposed operational change, and
- authorized execution.

The system must keep those states visibly distinct.

## 5. Product invariants

The following invariants are strongly supported by the scenario and existing Cadence philosophy.

### Invariant 1: Simulate before mutation

A proposed plan must not silently alter live operational truth.

### Invariant 2: Preserve the baseline

The manager must be able to understand the current state, the proposed state, and the delta between them.

### Invariant 3: Show displacement

Optimizing one project must not hide damage to another.

### Invariant 4: Respect hard constraints

PTO, task eligibility, required dependencies, and authorization limits must not be treated as suggestions merely because violating them improves a schedule.

### Invariant 5: Distinguish hard and soft constraints

A deadline target, preference, optimization goal, legal prohibition, approved leave period, and certification requirement are not equivalent. The system must know which constraints may be traded and which may not.

### Invariant 6: Explain consequential outputs

The manager should be able to ask why a task moved, why a person was selected, why a gap remains, why a deadline slipped, or why a scenario was rejected.

### Invariant 7: Human authority remains explicit

A model-generated proposal is not equivalent to organizational authorization.

### Invariant 8: Held scenarios are durable but provisional

A held plan should remain inspectable without pretending to be current operational truth.

### Invariant 9: Revalidate before execution when reality changes

If PTO, staffing, task completion, cost, deadlines, or other material inputs change while a scenario waits for approval, the system should detect that the proposal may be stale before execution.

### Invariant 10: Accessibility is foundational

Voice-first interaction should reduce interaction burden, but the system must not be voice-only. All consequential information, controls, explanations, and approvals should remain accessible through multiple equivalent interaction surfaces.

## 6. Visual experience shape

The source scenario suggests a coordinated visual-conversational workspace rather than a separate AI panel detached from the plan.

A likely experience shape is:

- **Portfolio view:** all active projects, major milestones, current risk, and staff allocation.
- **Focused project lens:** Project X highlighted without losing the effects on surrounding work.
- **Staff lanes:** assignments over time, including visible protected or unavailable periods.
- **Dependency overlay:** why some work cannot begin yet.
- **Gap visibility:** intervals that can be inspected conversationally.
- **Scenario overlay:** proposed changes shown against the baseline rather than overwriting it.
- **Impact panel:** changed completion dates, delayed projects, deadline risks, cost, overtime, and assumptions.
- **Conversation surface:** the manager asks questions, changes constraints, and requests alternative strategies.
- **Approval state:** clear separation among draft, held, pending approval, authorized, and applied states.

The exact UI remains open. The deeper principle is consistent with Cadence's view/lens direction: a schedule visualization should be treated as a projection over underlying operational truth, not as the truth itself.

## 7. Operational object pressures

The scenario suggests a set of domain concepts that deserve later modeling. These are **object pressures**, not an approved schema.

### Foundational operational objects

- Organization
- Workspace
- Project
- Task
- Dependency
- Staff member
- Capability or qualification
- Availability constraint
- Assignment
- Work calendar
- Deadline or milestone
- Estimate

### Scenario and decision objects

- Expedition request
- Scheduling objective
- Scenario
- Scenario constraint
- Proposed assignment
- Portfolio impact
- Cost projection
- Deadline risk
- Assumption
- Explanation
- Approval requirement
- Approval decision
- Execution decision

### Provenance and history pressures

- Baseline schedule revision
- Derived-from relationship
- Scenario creation source
- User constraint supplied during conversation
- AI-generated recommendation
- Human-authored modification
- Approval identity and timestamp
- Execution result
- Superseded or invalidated scenario state

Exact names and storage choices should be validated later rather than inherited automatically from this list.

## 8. Scheduling is a multi-objective problem

The system should not optimize for the shortest possible completion time as a universal goal.

The source scenario exposes competing objectives:

- finish Project X earlier,
- minimize delay to other projects,
- preserve hard deadlines,
- honor PTO,
- use only qualified staff,
- limit overtime,
- limit added cost, and
- maximize parallel throughput.

This implies a multi-objective decision surface where some constraints are absolute, some are organization policy, some are user-provided limits, and some are preferences.

A future scheduler should therefore be able to explain not only **what plan won**, but also **what it was optimizing and what it refused to violate**.

## 9. AI role and trust boundary

The AI in this scenario has several distinct roles:

1. **Interpreter** — understands the manager's intent.
2. **Retriever** — brings the relevant operational context into focus.
3. **Simulator** — generates feasible counterfactual plans.
4. **Analyst** — calculates impact across the portfolio.
5. **Explainer** — answers why a gap, assignment, delay, or risk exists.
6. **Negotiator** — accepts revised constraints and recomputes proposals.
7. **Custodian** — holds a strategy without applying it.
8. **Executor** — applies only the authorized plan within approved scope.

These roles should not collapse into one opaque agent action. Different authority levels and audit expectations apply to each.

## 10. Accessibility-first interpretation

The voice-first interaction is especially important because the manager is dealing with a cognitively dense operational problem.

An accessibility-first version of this experience should aim to:

- let the user state intent without learning query syntax,
- allow follow-up questions in ordinary language,
- synchronize speech with visual change,
- expose one consequential tradeoff at a time when useful,
- avoid requiring the user to remember hidden constraints,
- support keyboard, pointer, touch, text, and screen-reader equivalents,
- avoid using color alone to encode urgency or status,
- make uncertainty and pending approval visible, and
- preserve a reviewable history of what the AI proposed versus what a human approved.

This follows the broader Cadence principle of designing around users under the greatest cognitive or accessibility pressure without splitting them into a separate product.

## 11. Relationship to the Cadence family

This product should remain distinct from the personal Cadence app while preserving compatible principles.

### Shared conceptual inheritance

- Source and provenance matter.
- Derived structure should not silently replace underlying truth.
- Views are projections, not canonical truth.
- Human review and promotion boundaries matter.
- AI should not overclaim certainty or authority.
- Accessibility and cognitive load are product-shaping pressures.

### SaaS-specific extension

The organizational product introduces pressures that are not safely inherited from personal Cadence without separate design:

- multiple users and roles,
- permissions,
- organizational authority,
- shared operational records,
- workforce capability data,
- staff availability,
- cost and overtime,
- cross-project optimization,
- approval chains,
- execution governance,
- audit expectations, and
- potentially regulated employment or labor considerations.

The products may share concepts and infrastructure where justified, but the SaaS line should not become a shallow multi-user wrapper around personal Cadence.

## 12. Alignment with current Cadence evidence

The companion Cadence repositories already establish several useful compatibility anchors:

- `cadence-strategy/product_definition.md` emphasizes source grounding, meaning preservation, provenance visibility, evidence honesty, and non-overclaim discipline.
- `cadence-strategy/docs/manual/views_and_lenses_v0.md` distinguishes underlying material from user-facing projections.
- `cadence-strategy/docs/thesis/non_destructive_artifact_lifecycle_v0.md` argues that source, artifact, derived plan, task, and action should not collapse into one indistinguishable object.
- `cadence-app-dev/docs/planning/mvp_confidence_pack/contracts/source_truth_and_provenance_contract.md` provides implementation-adjacent evidence for preserving source truth, derivation lineage, projection non-authority, and explicit promotion boundaries.

For this SaaS product, the equivalent operational caution is:

> **Current plan, simulated scenario, approved decision, and executed schedule must remain distinguishable and traceable.**

That is a conceptual compatibility statement, not a claim that the personal app's exact artifact model or implementation should be copied into this repository.

## 13. Boundaries and non-claims

This synthesis does not yet decide:

- the final product name,
- the final schema,
- the scheduling algorithm,
- whether optimization is local, cloud-based, or hybrid,
- the model provider or reasoning stack,
- final approval mechanics,
- payroll or HR integrations,
- legal/compliance posture,
- labor-rule handling,
- exact overtime calculation,
- pricing or market positioning,
- final frontend design,
- real-time collaboration behavior,
- notification design,
- mobile/offline behavior,
- whether staff can accept, reject, negotiate, or appeal reassignments,
- whether all organizations should permit AI-executed reassignment, or
- implementation sequencing.

The broader Cadence direction favors local-first reasoning where practical, privacy-preserving preparation of sensitive context, and selective escalation to stronger cloud models when justified. That remains a relevant architectural pressure here, especially because staff, availability, cost, and organizational data may be sensitive, but it is not yet an implementation commitment for this repository.

## 14. Most important open product questions

1. What is the authoritative operational object model for projects, tasks, dependencies, assignments, people, constraints, and schedules?
2. Which scheduling constraints are always hard, which are organization-configurable, and which may be negotiated per scenario?
3. What constitutes sufficient explanation for a schedule change?
4. Who is allowed to create, hold, approve, authorize, execute, or cancel a scenario?
5. How should a held scenario detect staleness when real work changes underneath it?
6. What happens when the best mathematical schedule is harmful to staff continuity, fairness, burnout risk, or organizational norms?
7. How should staff capability be asserted and reviewed without turning hidden AI inference into employment authority?
8. How are cost and overtime modeled when payroll rules are more complex than a flat hourly multiplier?
9. What does the staff member see when their work is reassigned?
10. How should the system distinguish a projection, a commitment, a promise, and a deadline?
11. What portions of reasoning can happen locally or inside an organization's trust boundary, and what may be escalated externally?
12. What evidence must remain attached to an executed change for later review?

## 15. Product center emerging from this scenario

The clearest durable formulation is:

> **Cadence SaaS Project Management helps organizations reason over shared operational reality, simulate changes before making them, understand portfolio-wide consequences, preserve human authority, and execute approved plans with traceability.**

The signature experience is not "AI makes a schedule."

It is:

> **The manager and AI examine the same operational reality, explore counterfactual futures together, make constraints and consequences visible, and convert an approved decision into coordinated action without confusing proposal with truth or automation with authority.**
