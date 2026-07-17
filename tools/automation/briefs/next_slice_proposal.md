# Slice 1 Proposal — Human Review, Rejection, and Scenario Supersession

**Status:** proposal only; not authorized for implementation  
**Proposed from:** Slice 0 implementation findings  
**Proposal date:** 2026-07-16  
**Authority posture:** candidate bounded professional prototype slice only; not an active brief, implementation authority, shared-core promotion, production authorization, canonical schema authority, employment policy, or roadmap commitment beyond operator review

## Why this slice is next

Slice 0 proves that a scenario can be simulated, held, authorized, revalidated, and applied without collapsing proposal into operational truth.

The strongest remaining gap in that same trust chain is the human review boundary. The current prototype can hold a scenario and authorize it, but it cannot yet preserve an attributable human decision to:

- reject the proposal;
- request a bounded change before authorization; or
- approve the exact reviewed version for authorization.

This is a narrower and more foundational next proof than adding a generalized scheduler, multiple approvers, material-staleness rebasing, or a frontend packet.

## Proposed proof claim

Given a held synthetic professional scenario, Cadence Professional can record an attributable human review decision against the exact scenario version and change-set digest; reject the proposal with explicit rationale; request one bounded constraint change that produces a new scenario version with review and supersession lineage while preserving the original proposal; approve an exact reviewed version for authorization; prevent rejected or superseded versions from being authorized or applied; and preserve machine-readable evidence connecting the baseline, original proposal, review decision, superseding proposal, authorization, and applied revision.

## Proposed interaction chain

```text
Simulated Scenario
  -> Hold
  -> Human Review
       -> Reject
       -> Request Bounded Change
            -> New Scenario Version
            -> Review Again
       -> Approve For Authorization
  -> Authorize Exact Reviewed Version
  -> Revalidate
  -> Apply
```

## Proposed bounded fixture path

Use the existing Project X fixture and negotiated Slice 0 scenario as the review target.

The representative change request should be:

> Reduce the overtime cap from 60 minutes to 30 minutes per involved staff member, then show the revised consequences.

This produces one deterministic superseding scenario version without introducing a generalized conversational change language.

## Proposed scope

- add an immutable prototype `ReviewDecision` record;
- support exactly three review outcomes:
  - `APPROVED_FOR_AUTHORIZATION`;
  - `REJECTED`;
  - `CHANGES_REQUESTED`;
- bind every review decision to:
  - scenario identifier;
  - exact scenario version;
  - exact change-set digest;
  - synthetic reviewer identifier;
  - non-empty rationale;
- allow one bounded change-request field:
  - `max_overtime_minutes_per_staff`;
- generate a deterministic superseding scenario version from an accepted change request;
- preserve the original scenario object and evidence unchanged;
- record lineage from the new version to:
  - the prior version;
  - the review decision that requested the change;
- prevent authorization of:
  - a rejected scenario version;
  - a superseded scenario version;
  - a version lacking an exact `APPROVED_FOR_AUTHORIZATION` review decision;
  - a version paired with a review decision for another digest or version;
- preserve existing exact-baseline revalidation and application behavior;
- add deterministic review and supersession evidence snapshots;
- update findings and current-state surfaces after implementation.

## Explicit non-goals

- multiple approvers or partial authority composition;
- role-based production authorization;
- staff acceptance, appeal, labor consultation, or employment-policy workflow;
- arbitrary scenario editing or natural-language constraint parsing;
- generalized constraint-delta schema;
- material/non-material baseline-change classification or rebasing;
- comments, collaboration threads, notifications, or frontend review UI;
- Calendar representative packet work;
- LLM-generated rationale, review, recommendation, or authority;
- database, API, event, identity, permissions, audit, or integration work;
- changes to `cadence-app-dev`, `cadence-strategy`, or `Calendar`;
- canonical shared Cadence lifecycle or scenario semantics.

## Proposed implementation shape

The smallest credible shape is:

- extend the Slice 0 prototype rather than create `prototype/slice1/`;
- add review and lineage fields as prototype-local dataclasses;
- add deterministic workflow functions for:
  - recording review decisions;
  - deriving a superseding version from the one allowed change request;
  - validating review approval before authorization;
- retain standard-library Python and the existing fixture-driven scheduler;
- preserve existing evidence files and append new numbered evidence snapshots;
- keep the schema explicitly prototype-only.

## Proposed files expected to change

- `prototype/slice0/src/cadence_professional_slice0/model.py`
- `prototype/slice0/src/cadence_professional_slice0/workflow.py`
- `prototype/slice0/src/cadence_professional_slice0/cli.py`
- `prototype/slice0/tests/test_vertical_flow.py`
- `prototype/slice0/tests/test_invariants.py`
- `prototype/slice0/tests/test_evidence_snapshots.py`
- `prototype/slice0/evidence/07_review_rejected.json`
- `prototype/slice0/evidence/08_review_changes_requested.json`
- `prototype/slice0/evidence/09_superseding_scenario.json`
- `prototype/slice0/evidence/10_review_approved.json`
- `prototype/slice0/evidence/11_applied_reviewed_revision.json`
- `prototype/slice0/schemas/scenario_packet.prototype.schema.json` only if the top-level envelope requires a new allowed evidence kind
- `docs/implementation/slice_1_findings.md`
- `CURRENT_STATE.md`
- the promoted active Slice 1 brief after operator authorization

No product, origin, architecture, or reconciliation document should require rewriting unless implementation reveals a direct contradiction.

## Proposed required tests

1. review can target only a held scenario;
2. review binds to the exact scenario identifier, version, and digest;
3. review rationale must be non-empty;
4. rejection produces an attributable terminal review result without mutating baseline or scenario content;
5. a rejected scenario cannot be authorized or applied;
6. a change request accepts only `max_overtime_minutes_per_staff` in this slice;
7. the 30-minute change request deterministically produces the next scenario version;
8. the new version retains the same baseline revision, request, and target project;
9. the new version records the prior version and originating review decision;
10. the original scenario remains unchanged and inspectable;
11. the prior version is treated as superseded for authorization purposes;
12. a superseded version cannot be authorized or applied;
13. approval for authorization binds to the exact revised version and digest;
14. mismatched or missing review approval rejects authorization;
15. the approved revised version still passes exact baseline revalidation;
16. application retains review and supersession lineage in its trace;
17. all Slice 0 tests remain green;
18. regenerated evidence exactly matches committed snapshots.

## Proposed acceptance boundary

Slice 1 is complete when:

- rejected, changes-requested, and approved review paths are deterministic and separately evidenced;
- no review action mutates the baseline or silently overwrites an existing scenario version;
- the 30-minute change request creates one inspectable superseding version;
- rejected and superseded versions cannot cross the authorization boundary;
- only the exact review-approved version can be authorized and applied;
- application trace includes the relevant review and supersession lineage;
- all prior Slice 0 behavior remains green;
- findings state what the proof establishes and what remains unproven.

## Proposed stop conditions

Stop rather than expand if implementation would require:

- more than one change-request field;
- multiple reviewers or approval authority composition;
- a production role or identity model;
- arbitrary patch operations over scenario payloads;
- materiality-aware baseline reconciliation;
- canonical lifecycle terms for shared Cadence core;
- frontend interaction design;
- real workforce data or employment-policy semantics;
- a third-party runtime dependency;
- changes outside the named paths and proof claim.

## Deferred candidate slices

The following remain valid future pressures but are not part of this proposal:

1. multiple approvers with non-combinable partial authority;
2. narrowly defined non-material staleness classification;
3. representative non-canonical Calendar lens packet;
4. additional scheduling or portfolio sophistication only when required by evidence.

## Operator decision requested

Choose exactly one:

```text
AUTHORIZE_SLICE_1_AS_PROPOSED
AUTHORIZE_SLICE_1_WITH_NAMED_CHANGES
KEEP_SLICE_1_PROPOSAL_ONLY
REJECT_SLICE_1_AND_SELECT_ANOTHER_FINDING
```

Authorization should promote this proposal into one active brief before any product-code implementation begins.