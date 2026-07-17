# Slice 0 — Professional Orchestration Trust Boundary Proof

**Status:** Implemented; awaiting operator review and acceptance  
**Authorized by:** Derrick Ortiz  
**Authorization date:** 2026-07-16  
**Authority posture:** bounded professional prototype implementation only; not shared-core promotion, production authorization, canonical schema authority, employment policy, or roadmap authority beyond this slice

## Proof claim

Given a deterministic synthetic professional portfolio, Cadence Professional can generate a counterfactual proposal to accelerate Project X without mutating its baseline; calculate assignment, schedule, overtime, cost, deadline, and cross-project displacement effects; explain those effects from explicit fixture facts; accept a bounded constraint negotiation; hold the resulting scenario as a versioned non-operational record; authorize an exact scenario version and change set; reject execution when its baseline is stale or its authorization does not match; and apply only the authorized changes to produce a new operational revision traceable to the baseline, proposal, review, and authorization.

## Goal

Create the smallest executable professional proof of:

```text
Observe -> Simulate -> Explain -> Negotiate Constraints
        -> Hold -> Authorize -> Revalidate -> Apply
```

The slice should convert the existing Project X scenario and architecture pressure into deterministic implementation evidence without claiming production readiness or creating a separate shared Cadence project-management core.

## Scope

- synthetic portfolio with Project X and two competing projects;
- three synthetic staff members with explicit capabilities, rates, and availability;
- Jill PTO as a hard constraint;
- explicit task dependencies and task eligibility;
- deterministic baseline and expedited scenario generation;
- current-constraint and negotiated-overtime scenario versions;
- Project X completion delta;
- Project Y and Project Z displacement;
- deadline crossing detection;
- synthetic overtime compensation and incremental premium;
- fact-linked explanations;
- held scenario state;
- exact scenario-version and change-set authorization;
- exact baseline revision revalidation;
- stale execution rejection;
- bounded application into a new traceable operational revision;
- unit tests, snapshot tests, evidence snapshots, and CI.

## Explicit non-goals

- canonical Cadence project, task, schedule, scenario, or constraint schema;
- production optimization, solver selection, or generalized scheduling;
- production authentication, authorization, permissions, policy, or audit;
- databases, APIs, events, cloud services, integrations, billing, or multi-tenancy;
- real employee, compensation, PTO, qualification, performance, or protected data;
- legal, labor, fairness, privacy, retention, accessibility, or employment-policy claims;
- LLM interpretation, explanation, recommendation, approval, or execution authority;
- frontend, mobile, voice, or Calendar rendering work;
- emergent-role recognition, portable worker evidence, license incentives, or ad-hoc group mode;
- implementation in or modification of `cadence-app-dev`, `cadence-strategy`, or `Calendar`.

## Prototype assumptions

- Time uses deterministic integer minutes over an eight-day synthetic horizon.
- A regular workday is 09:00–17:00.
- A synthetic overtime window is 17:00–18:00.
- “One hour of overtime for each staff member involved” means at most 60 total overtime minutes per staff member across the scenario.
- Tasks may be split across available intervals but are performed by one explicitly eligible staff member.
- Overtime is available only to Project X tasks in the negotiated scenario.
- Slice 0 uses exact revision equality: any baseline revision mismatch rejects application.
- Costs use synthetic hourly rates and a flat 1.5 overtime multiplier.
- Explanations are deterministic templates over explicit fixture facts and calculated outputs.

## Files expected to change

- `README.md`
- `AGENTS.md`
- `CURRENT_STATE.md`
- `.gitignore`
- `.github/workflows/slice0.yml`
- `docs/implementation/slice_0_findings.md`
- `tools/automation/briefs/active/slice_0_professional_orchestration_proof.md`
- `tools/automation/templates/slice_brief_template.md`
- `tools/automation/checklists/slice_completion_checklist.md`
- `prototype/slice0/**`

No other existing product, architecture, origin, or reconciliation document should be rewritten by this slice.

## Required tests and deterministic checks

1. simulation does not mutate the baseline;
2. every assignment uses explicit task eligibility and a matching capability;
3. no work is assigned during PTO;
4. dependencies remain satisfied;
5. staff assignments do not overlap;
6. the no-overtime scenario accelerates Project X and exposes displacement;
7. the one-hour overtime negotiation changes the proposal deterministically;
8. overtime stays within the explicit cap and applies only to Project X;
9. explanations reference fixture facts or calculated state;
10. holding does not authorize or apply;
11. missing consequence scopes reject authorization;
12. mismatched scenario version or digest rejects application;
13. stale baseline revision rejects application without mutation;
14. valid application creates a new revision with complete lineage;
15. regenerated evidence exactly matches committed snapshots.

Validation commands:

```bash
cd prototype/slice0
python -m pytest
python -m cadence_professional_slice0 --fixtures fixtures --output evidence
git diff --exit-code -- evidence
```

## Acceptance boundary

The slice is complete when:

- the full vertical proof runs deterministically;
- all required tests pass;
- seven evidence snapshots regenerate without drift;
- state classes are structurally separate;
- the applied revision references the baseline, scenario, authorization, and exact digest;
- the repository can be re-entered through `README.md`, `CURRENT_STATE.md`, and `AGENTS.md`;
- CI repeats the objective validation;
- findings state both what was proven and what remains unproven.

## Stop conditions

Stop rather than expand if implementation would require:

- inferred capability or hidden employment judgment;
- a canonical shared-core decision;
- production identity, permissions, policy, security, or legal semantics;
- a generalized solver or new third-party runtime dependency;
- real data or integrations;
- frontend behavior;
- silent rebasing of an authorized scenario;
- additional product concepts not required by the proof claim.

## Evidence classification

```text
CODE_AND_UNIT_TEST_EVIDENCE
FIXTURE_DRIVEN_PROTOTYPE_EVIDENCE
DETERMINISTIC_MACHINE_READABLE_EVIDENCE
NOT_PRODUCTION_EVIDENCE
NOT_PRODUCT_VALUE_EVIDENCE
NOT_CANONICAL_SHARED_CORE_TRUTH
```

## Operator attention

**Operator attention:** Medium  
**Reason:** The implementation is bounded and testable, but the operator should review whether the fixture, overtime assumption, and exact-revision authorization boundary faithfully represent the intended first professional proof before merge.

## Notes and cautions

- This brief remains active until operator acceptance. Merge does not automatically authorize Slice 1.
- After acceptance, archive this brief rather than editing history in place.
- New implementation pressure should be selected from `docs/implementation/slice_0_findings.md`, not from the full conceptual backlog.
