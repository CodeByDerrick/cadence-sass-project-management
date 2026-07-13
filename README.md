# Cadence SaaS Project Management

Cadence SaaS Project Management is the organizational, multi-user evolution of the Cadence product family for coordinated project execution.

It is not a generic task tracker with an AI chat box added on top. The product direction explored here is an AI-mediated operational system that can understand projects, tasks, dependencies, staff capabilities, availability, deadlines, costs, approvals, and organizational priorities well enough to help people reason about tradeoffs and safely reshape work.

## Product relationship

This repository is intentionally distinct from, but conceptually compatible with:

- `cadence-strategy` — foundational product doctrine, conceptual architecture, and long-horizon Cadence direction.
- `cadence-app-dev` — implementation evidence and engineering lessons from the personal Cadence application.
- `cadence-sass-project-management` — the organizational project-management product line, including multi-user scheduling, shared operational truth, staffing constraints, simulation, approvals, and execution governance.

Cadence Core helps a person think, capture, organize, and act. This SaaS product extends the same artifact-centered and accessibility-first philosophy into shared organizational work, where many people, projects, constraints, and decisions must be coordinated together.

## Foundational product posture

The current direction assumes:

- **Voice-first, not voice-only.** A project manager should be able to reason conversationally with the system while seeing the consequences visually.
- **Simulation before mutation.** Proposed changes to schedules and assignments should be modeled as scenarios before any live plan is altered.
- **Human authorization before execution.** The AI may propose, explain, and hold a strategy, but consequential reassignment or cost changes require appropriate approval.
- **Constraint-aware planning.** Skills, task eligibility, dependencies, PTO, deadlines, overtime limits, costs, and competing project priorities are first-class scheduling inputs.
- **Organizational throughput over isolated project optimization.** A project has no dedicated human lane by default; tasks may be distributed across qualified staff to maximize safe parallel throughput.
- **Explainable gaps and tradeoffs.** Idle periods, delays, blocked work, and downstream effects should be inspectable and explainable in plain language.
- **Artifact-centered operational truth.** Projects, tasks, decisions, approvals, scenarios, staffing constraints, and execution changes should remain durable, attributable records rather than ephemeral chat state.
- **Privacy-aware AI routing.** The broader Cadence direction favors local-first reasoning where practical, privacy-preserving preparation of sensitive context, and selective escalation to cloud models when heavier reasoning is justified.

## Repository structure

- `docs/origin/` — source scenarios, narratives, and intent evidence supplied by the product owner.
- `docs/product/` — synthesized product behavior, UX models, capability boundaries, and product invariants.
- `docs/architecture/` — provisional system shapes and architectural implications derived from product evidence.

## Current foundation

The first scenario captured in this repository describes a project manager who is asked to expedite an urgent project. Through a voice-first interface, the manager asks Cadence to isolate the project, simulate increasingly aggressive acceleration plans, account for staff capability, PTO, overtime, cost, deadlines, and effects on other projects, hold the selected strategy pending approval, and then execute the reassignment only after authorization.

See:

- `docs/origin/project_manager_expedition_scenario.md`
- `docs/product/expedition_orchestration_product_synthesis.md`
- `docs/architecture/expedition_simulation_system_shape.md`

## Status

Early product-definition repository. The current documents preserve and interpret product intent; they are not yet implementation commitments or a complete product specification.
