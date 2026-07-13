# Origin Scenario: Project Manager Expedites an Urgent Project

**Source type:** User-provided spoken product scenario  
**Captured:** 2026-07-13  
**Status:** Origin evidence, not yet a complete product specification or implementation commitment

## Why this document exists

This document preserves the product-owner intent expressed in a narrated scenario. It is intentionally separated from derived product and architecture documents so future implementation work can distinguish:

1. what was actually envisioned,
2. what has been inferred from that vision, and
3. what has later been explicitly approved as product or engineering doctrine.

The wording below is normalized for readability while preserving the scenario's substantive behavior.

## Scenario

A project manager is sitting at a desk looking at a web dashboard containing all active projects and their task trees. Work is distributed across the staff portfolio rather than treating each project or task tree as the exclusive responsibility of one individual. Tasks across projects are assigned in ways intended to maximize safe parallel throughput.

The project manager receives a call from a superior: **Project X has suddenly become urgent and needs to be expedited.** The manager replies that they will determine what can be done and provide a revised completion projection.

After the call, the manager turns to the project-management software, which is voice-first, activates the conversational interface, and says:

> I've just been given notice to expedite Project X. Bring it up for me so that we can discuss how we might do that and the implications.

Visually, Project X is isolated and highlighted across a two-dimensional timeline. The manager can see:

- the project's task tree,
- which tasks are assigned to which staff members,
- each person's work lane over time,
- the projected duration and completion date of the project, and
- gaps where the project is not being worked on or where a staff member finishes one task but is not scheduled to begin another Project X task until later.

As the view changes, the AI responds that it has isolated Project X and believes there is room to expedite it. The manager asks to see the plan.

A simulation runs in the background. Tasks across the portfolio may be reorganized so that more Project X work can happen sooner and in parallel. The resulting proposals are not limited to rearranging Project X in isolation; they may move tasks from other projects when doing so is necessary to create capacity.

The AI presents several possible strategies, for example:

- a **light expedition** that shortens Project X by about one week,
- a **more aggressive approach** that shortens it by about three weeks, and
- an **extreme approach** that could complete Project X by the end of the current week but would place other projects on hold.

These labels and time savings are illustrative scenario outputs, not assumed permanent product tiers.

The manager decides that Project X may justify the fastest feasible approach. The AI asks whether overtime is authorized. The manager obtains approval and specifies a narrow overtime constraint:

> Yes, but I only want to approve one hour of overtime for each staff member involved.

The AI then generates and displays a new condensed task tree and schedule. Tasks are distributed across staff lanes according to actual constraints. Some staff members can perform certain tasks but not others. Dependencies may require one task to finish before another can begin. Some gaps therefore remain.

The manager notices one such gap and asks:

> Why does Jill have this gap on these couple of days? Why haven't we assigned her anything?

The AI explains that Jill has requested PTO for those days. The manager agrees that nothing should be assigned to her during that absence.

The manager continues the review by asking questions about the impact on the rest of the portfolio, including:

- which projects are delayed,
- which projects are delayed the most,
- whether any project will cross an existing deadline,
- how much the expedition will cost, and
- whether the tradeoff remains acceptable.

After review, the manager accepts the proposed strategy but does not yet authorize execution. The AI responds in substance:

> I will hold this strategy in place and wait for approval.

The manager then receives approval for the projected cost and the consequences to other projects and gives the AI authorization to execute.

Only at that point does the system apply the plan: staff projections and assignments are changed for the urgent period, Project X is accelerated, and affected work from other projects is deferred or reorganized accordingly.

Any remaining staff capacity may then be used to absorb spillover work from the delayed projects through a separate allocation process.

## Product intent preserved by the scenario

The scenario strongly signals the following product intentions:

- The unit of reasoning is the **whole portfolio**, not an isolated project.
- Work should be capable of moving across qualified staff to maximize organizational throughput.
- The interaction model is **conversational and visual at the same time**.
- The AI should **simulate before changing live work**.
- Project acceleration is a multi-constraint optimization problem involving skills, dependencies, availability, deadlines, overtime, cost, and competing priorities.
- Gaps should be visible and explainable rather than silently optimized away.
- The system should expose the consequences of a proposal to other projects before execution.
- A proposed strategy can be **held without being applied**.
- Consequential changes require an explicit authorization boundary.
- Once authorized, the system is expected to update operational assignments rather than merely produce advice.

## Interpretation cautions

The following details should not be hardened into permanent product requirements without separate review:

- the exact number of scenario options,
- the labels `light`, `aggressive`, and `extreme`,
- the example savings of one week, three weeks, or completion by the end of the week,
- whether approval occurs inside or outside the product,
- whether all staff assignments are automatically mutable in every organization,
- the exact visualization used for every project type, and
- whether spillover reallocation is automatic, suggested, or separately authorized.

These are useful scenario details, but the deeper requirement is the system's ability to model, explain, hold, authorize, and execute portfolio-level schedule changes under real constraints.
