# Slice 0 Implementation Findings

**Date:** 2026-07-16  
**Status:** accepted and merged through PR #3  
**Evidence source:** `prototype/slice0/` code, tests, fixtures, and committed evidence snapshots

## Objective

Test whether the existing professional architecture is concrete enough to support a bounded executable proof without adding another broad conceptual layer.

## Result

```text
SLICE_0_PROOF_IMPLEMENTED
SLICE_0_ACCEPTED_AND_MERGED
7_TESTS_PASS
7_DETERMINISTIC_EVIDENCE_SNAPSHOTS_GENERATED
BASELINE_SCENARIO_AUTHORIZATION_AND_APPLIED_STATE_SEPARATED
STALE_BASELINE_REJECTED
NO_PRODUCTION_CLAIM
```

The conceptual foundation was sufficient. No architecture blocker required additional product scaffolding before code.

## What the implementation demonstrates

- A small deterministic scheduler can express the Project X pressure without using an LLM or a production optimization system.
- The baseline remains unchanged while multiple scenario versions are generated.
- Explicit task eligibility prevents staff from being treated as interchangeable capacity.
- Jill's PTO can remain a hard availability fact while the system explains why Alex was selected.
- Accelerating Project X visibly delays Project Y and Project Z rather than hiding portfolio displacement.
- A bounded overtime constraint changes completion timing and produces inspectable synthetic cost.
- The held proposal remains non-operational.
- Authorization can bind to an exact scenario version and stable change-set digest.
- Exact baseline revision revalidation provides a simple, conservative stale-scenario safety boundary.
- Application can produce a new operational revision with lineage to baseline, scenario, authorization, and digest.
- Machine-readable snapshots provide useful review and future lens-packet evidence without becoming canonical schema authority.

## Concrete fixture outcome

Under baseline priority, Project X completes on synthetic day 5 at 16:00.

With Project X moved ahead of lower-priority work and no overtime, it completes on day 3 at 16:00.

After negotiating at most 60 overtime minutes per involved staff member, it completes on day 3 at 14:00. Alex and Sam each use 60 overtime minutes. The synthetic incremental overtime premium is `$42.50`.

The accelerated scenario crosses Project Y's synthetic deadline and delays Project Z without crossing Project Z's deadline.

These values are fixture results, not product targets or performance claims.

## Important implementation decisions

### Deterministic standard-library Python

The slice uses no scheduling, optimization, schema-validation, persistence, or LLM dependency. This keeps the proof legible and prevents a library choice from becoming accidental architecture authority.

### Explicit eligibility only

Capability and task eligibility are fixture facts. The scheduler does not infer qualifications from titles, work history, or adjacent evidence.

### Exact revision staleness

Any baseline revision mismatch rejects application. This is stricter than a future materiality-aware rebase policy, but it proves the trust boundary without inventing reconciliation semantics.

### Prototype-only evidence envelope

The JSON schema validates only the top-level evidence envelope and is explicitly marked `prototype.slice0.v0`. The nested payload remains implementation evidence rather than a canonical Cadence contract.

### Thin harness rather than full harness copy

The repository now has:

- a concise `AGENTS.md` map;
- `CURRENT_STATE.md` for re-entry;
- an accepted Slice 0 brief in archive;
- a proposal-only next-slice surface;
- a brief template and completion checklist;
- deterministic CI.

It does not copy the mature `cadence-app-dev` skill suite, prompt library, inventories, caution system, journals, or portable bootstrap kit. Those surfaces have not yet earned maintenance cost here.

## Limitations

This implementation does not prove:

- optimal scheduling;
- arbitrary portfolio support;
- production performance or scale;
- correct labor, payroll, overtime, employment, privacy, security, or fairness behavior;
- production authorization or identity;
- usability, accessibility, product value, or stakeholder acceptance;
- real-world integration behavior;
- safe LLM interpretation or explanation;
- canonical shared-core object semantics;
- readiness to move scheduling code into `cadence-app-dev`.

## Pressure revealed by implementation

The next executable boundary should be selected from:

1. **Review and rejection pressure:** human review modifies or rejects a proposed change before authorization.
2. **Authorization-scope pressure:** multiple approvers own different consequences and partial authority must not combine accidentally.
3. **Staleness pressure:** classify a narrowly defined non-material baseline change without silently rebasing the approved change set.
4. **Representative lens packet:** emit a stable, explicitly non-canonical packet for `Calendar` to render.

Exactly one should be active at a time.

The proposal-only selection is now review and rejection pressure:

- `tools/automation/briefs/next_slice_proposal.md`

This selection is not implementation authorization.

## Cross-repository reconciliation read

```text
NO_RECONCILIATION_REQUIRED
```

The evidence supports existing professional architecture claims and does not contradict a named Strategy or Dev surface.

A reconciliation trigger should be reconsidered when:

- the scheduler or state model is proposed as shared Cadence core;
- code reuse in `cadence-app-dev` is requested;
- the prototype packet is proposed as a canonical contract;
- `Calendar` needs a representative professional packet;
- implementation evidence materially changes a named Strategy claim.

## Current operator gate

Review `tools/automation/briefs/next_slice_proposal.md` and explicitly authorize, revise, keep, or reject the proposed Slice 1. No product-code implementation is authorized while the active brief directory is empty.