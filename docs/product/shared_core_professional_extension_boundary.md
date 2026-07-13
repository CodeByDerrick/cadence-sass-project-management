# Shared Core / Professional Extension Boundary

**Status:** Current professional-product boundary  
**Date:** 2026-07-13  
**Authority posture:** Professional product interpretation and cross-repository boundary only; not shared Cadence doctrine authority, implementation truth, schema/API authority, roadmap authority, legal advice, security guarantee, or public copy

## 1. Purpose

This document reconciles the professional project-management scenario work with current Cadence Strategy doctrine.

The controlling boundary is:

> **Project management belongs to the shared Cadence core. This repository owns the professional, multi-user organizational extension of that core.**

The professional product should not create a separate semantic universe for projects, tasks, dependencies, schedules, constraints, scenarios, or lenses merely because the environment includes multiple staff members.

## 2. Shared Cadence foundation inherited here

The professional product inherits shared doctrine for concepts such as:

- projects;
- tasks and sub-tasks;
- dependencies;
- sequencing;
- estimates and duration pressure;
- priority and relevance;
- milestones and target dates;
- schedules and temporal placement;
- current, planned, projected, and completed state;
- hard and soft constraints;
- gaps and unavailable intervals;
- alternate scenarios;
- baseline versus proposed state;
- consequences of moving, accelerating, delaying, or pausing work;
- grounded explanations;
- conversational manipulation through voice or text;
- lenses and projections over the same underlying material.

The canonical shared doctrine lives in:

- `CodeByDerrick/cadence-strategy:docs/doctrine/shared_project_management_and_lensing_core_v0.md`

This repository may contribute professional lessons back to that doctrine through explicit reconciliation, but should not silently redefine it.

## 3. Professional specialization owned here

This repository owns the professional extension, including pressure around:

- multiple people and teams;
- task eligibility and qualification;
- staffing and assignment;
- organizational ownership;
- shared operational truth;
- permissions and privilege layers;
- role-based authority;
- approval chains;
- overtime and cost;
- organizational policy;
- portfolio-wide allocation;
- cross-project displacement;
- multi-user collaboration;
- execution governance;
- offboarding;
- professional trust-domain policy;
- employer confidence that corporate information is not leaking into personal Cadence.

These concerns are not merely larger versions of personal planning. They introduce new authority, ownership, privacy, labor, employment, and governance pressures.

## 4. Personal and professional products remain fundamentally compatible

Personal Cadence and professional Cadence should remain fundamentally compatible where their semantics are truly shared.

A personal project may have:

- one primary person available to do the work;
- dependencies;
- schedule pressure;
- competing projects;
- alternate scenarios;
- deadlines;
- gaps;
- energy/capacity constraints;
- calendar conflicts;
- questions such as "What happens if I move this forward?" or "Why is there a gap here?"

A professional project may use the same foundations while expanding the resource pool and authority model across many people, teams, rules, and approvals.

The distinction is therefore not:

```text
personal = simple task app
professional = real project management
```

The preferred distinction is:

```text
shared Cadence core = project/task/dependency/scheduling/scenario/lens foundation
personal interpretation = one human across a messy life
professional interpretation = many humans inside organizational authority and governance
```

## 5. The expedition scenario reinterpreted

The original Project X expedition scenario remains valid as professional product evidence.

What changes is its ownership interpretation.

The following are shared-core capabilities in principle:

- project/task/dependency representation;
- schedule projection;
- gap visibility;
- scenario generation;
- baseline-versus-proposal comparison;
- conversational constraint changes;
- explanation of why a schedule looks the way it does.

The following are professional extensions:

- distributing tasks across multiple staff members;
- checking capability and task eligibility;
- respecting staff PTO as organizational availability data;
- comparing impacts across an organizational portfolio;
- overtime authorization;
- added cost;
- approval chains;
- manager authority;
- execution against shared staff assignments;
- organizational offboarding and role changes.

This means the scenario is not the source of a separate professional project-management core. It is the first strong professional orchestration scenario built on top of the shared Cadence foundation.

## 6. Lens relationship

The project-manager view described in the expedition scenario is a professional lens over shared operational material.

Possible projections include:

- portfolio view;
- focused project view;
- staff-lane view;
- dependency overlay;
- gap explanation view;
- baseline-versus-scenario overlay;
- cost impact view;
- deadline-risk view;
- approval view.

The Cadence Lens Prototype Lab at `CodeByDerrick/Calendar` remains a cross-ecosystem test ground for lens behavior.

This repository may adapt lessons from that lab for professional staffing, portfolio, project, and timeline views. It may also contribute lessons back. Neither repository should treat its prototype packet or view shape as canonical Cadence truth without explicit reconciliation.

## 7. Shared executable core

Current direction assumes the professional product will use the same core being developed in `CodeByDerrick/cadence-app-dev` where semantics are shared.

Current Dev evidence does **not** yet prove production project management, scheduling, workflow, persistence, orchestration, professional trust domains, or offboarding.

This repo should therefore distinguish:

- Strategy doctrine;
- professional product pressure;
- prototype findings;
- implementation plans;
- actual Dev truth.

A later architecture change may justify a new shape, package, service, repository, or runtime boundary. That decision should be earned by implementation and scale pressure rather than assumed in advance.

## 8. Personal / professional trust-domain inheritance

This repository also inherits the current Strategy doctrine:

- `CodeByDerrick/cadence-strategy:docs/doctrine/personal_professional_continuity_and_trust_domains_v0.md`

Key implications for the professional product:

- personal and professional Cadence may coexist on the same mobile device;
- data, permissions, memory, artifacts, ownership, and AI context must not bleed across trust domains by default;
- same-device availability does not imply cross-domain permission;
- Professional Light may graduate into multi-user Professional structure;
- reverse downgrade from a multi-user professional environment is a governed administrative transition;
- mixed-context captures may contain both personal and professional meaning;
- offboarding should distinguish the continuing person from organizational access and organization-owned records;
- work-managed devices can provide strong policy boundaries without replacing domain-aware identity and access controls.

## 9. Mobile first, voice first, desktop rich

Professional Cadence remains:

- mobile first;
- voice first, not voice only;
- continuously accessible;
- compatible with richer desktop use where complexity benefits from screen space.

The expected professional usage pattern may be more desktop-heavy than personal Cadence, especially for dense portfolio planning, staffing lanes, timelines, and scenario comparison.

That does not make mobile secondary. Capture, approvals, urgent reprioritization, questions, status checks, and context recovery may happen anywhere.

## 10. Professional Light and business lifecycle

The professional audience is not only formal companies with established staff.

The ecosystem should anticipate:

- gig workers;
- freelancers;
- creators;
- side hustles;
- consultants;
- sole proprietors;
- very small businesses;
- businesses transitioning into multi-user operations;
- organizations later shrinking back to solo control.

A user may begin with mixed personal/professional material, gradually create professional structure, and later promote selected professional projects, workflows, clients, records, and operational knowledge into a multi-user domain.

That promotion should not automatically transfer unrelated personal source or private reflections into organizational ownership.

Reverse transition should not silently extract shared organizational records into a personal domain.

## 11. Cross-repository ownership

### `cadence-strategy`

Owns shared doctrine, including:

- project-management core;
- lens philosophy;
- personal/professional continuity;
- trust-domain principles;
- architecture design intent;
- evidence boundaries.

### `cadence-app-dev`

Owns executable core truth:

- code;
- tests;
- actual models;
- APIs;
- runtime behavior;
- validation evidence.

### `Calendar`

Owns bounded lens prototype experiments and frontend evidence.

### This repository

Owns:

- professional scenarios;
- professional product synthesis;
- multi-user orchestration pressure;
- organizational governance pressure;
- professional lens requirements;
- professional architecture implications;
- professional-specific evidence and prototypes when created.

## 12. Controlling clarification for earlier repository documents

This document narrows one earlier framing in `docs/product/expedition_orchestration_product_synthesis.md`.

Where that synthesis says the professional product should remain distinct from the personal Cadence app, interpret **distinct** as:

> distinct product interpretation, trust domain, governance model, and user experience where needed — **not** a separate foundational project-management core.

The earlier synthesis remains active for the expedition scenario's professional capabilities, invariants, UX pressures, and orchestration implications.

This boundary document controls where the earlier text could otherwise imply a deeper product fork.

## 13. Non-authorizations

This boundary does not authorize:

- shared-core implementation work;
- a new Dev repository;
- a separate scheduler implementation;
- a canonical schema;
- a production permissions model;
- a final Professional Light package;
- offboarding behavior;
- employment-policy defaults;
- legal ownership determinations;
- privacy or security guarantees;
- cross-domain AI retrieval;
- a final frontend architecture;
- roadmap sequencing;
- public claims.

## 14. Current disposition

```text
SHARED_PROJECT_MANAGEMENT_CORE_INHERITED
PROFESSIONAL_MULTI_USER_EXTENSION_OWNED_HERE
PERSONAL_PROFESSIONAL_TRUST_DOCTRINE_INHERITED
CALENDAR_LENS_LAB_RECOGNIZED_AS_CROSS_ECOSYSTEM_TEST_GROUND
CADENCE_APP_DEV_REMAINS_EXECUTABLE_CORE_OWNER
NO_IMPLEMENTATION_AUTHORIZED_BY_THIS_RECONCILIATION
```
