# Cadence Professional Agent Instructions

Cadence Professional owns professional multi-user product specialization and bounded professional-specific prototype evidence. Shared doctrine remains in `cadence-strategy`; shared executable core truth remains in `cadence-app-dev` when semantics graduate beyond a local prototype.

## Required reading

Before changing this repository, read:

1. `README.md`
2. `CURRENT_STATE.md`
3. `docs/product/shared_core_professional_extension_boundary.md`
4. `docs/architecture/expedition_simulation_system_shape.md`
5. the single active brief under `tools/automation/briefs/active/`, when one exists
6. otherwise `tools/automation/briefs/next_slice_proposal.md` for the proposal-only gate
7. the relevant prototype README, tests, fixtures, evidence, and implementation findings

## Authority hierarchy

1. An operator-authorized active brief controls the exact implementation slice.
2. Executable code and tests define implemented prototype behavior.
3. Product and architecture documents define professional pressure and boundaries without becoming executable truth.
4. Evidence snapshots demonstrate deterministic fixture behavior only.
5. Proposals, discussion, and inferred future needs do not authorize expansion.

A prototype packet is not a canonical Cadence schema. A recommendation is not authorization. A proposal is not an active brief.

## Current gate

```text
SLICE_0_ACCEPTED_AND_MERGED
SLICE_0_BRIEF_ARCHIVED
NO_ACTIVE_BRIEF
SLICE_1_PROPOSAL_ONLY
NO_SLICE_1_IMPLEMENTATION_AUTHORIZED
NO_PRODUCTION_IMPLEMENTATION_AUTHORIZED
```

## Roles

- **Human operator:** product direction, slice authorization, scope changes, risk acceptance, cross-repository promotion, and final merge decisions.
- **ChatGPT reasoning layer:** re-anchor, compare repository evidence, author or refine bounded proposals, briefs, and documentation, interpret findings, and prepare safe handoffs.
- **Codex execution layer:** implement exactly one active brief, run tests, regenerate evidence, make bounded mechanical documentation updates, and report validation.
- **Deterministic automation:** run tests, regenerate snapshots, detect drift, and enforce objective repository checks. It does not choose product direction.

## Slice workflow

```text
proposal only
  -> operator authorization
  -> one active brief
  -> preflight and expected-file review
  -> tests or narrow proof first
  -> smallest implementation
  -> new-slice validation
  -> relevant regression validation
  -> deterministic evidence regeneration
  -> implementation findings
  -> operator review
  -> archive brief only after acceptance
```

Keep one active implementation brief by default. When no active brief exists, product-code implementation must stop at proposal or brief preparation.

## Commands

From `prototype/slice0/`:

```bash
python -m pip install -e ".[dev]"
python -m pytest
python -m cadence_professional_slice0 --fixtures fixtures --output evidence
git diff --exit-code -- evidence
```

The evidence command must be deterministic. Generated cache, coverage, build, or environment artifacts must not be committed.

## Implementation boundaries

- Use synthetic data only.
- Keep baseline, scenario, review, authorization, revalidation, and applied revision structurally distinct when those states are in an authorized slice.
- Use explicit fixture eligibility; do not infer staffing authority.
- Preserve PTO and dependencies as hard constraints in the current prototype.
- Expose cross-project displacement and overtime cost.
- Bind consequential decisions to exact scenario versions and change-set digests.
- Reject baseline revision mismatch unless an active brief explicitly authorizes a narrower reconciliation proof.
- Keep explanations grounded in explicit fixture facts and calculated outputs.
- Prefer standard-library Python unless the active brief authorizes a dependency.

## Repository boundaries

Stop and report rather than expanding when:

- no active brief authorizes product-code work;
- a change would define canonical shared project, task, schedule, scenario, review, or constraint semantics;
- shared executable behavior should move to `cadence-app-dev`;
- frontend lens experimentation belongs in `Calendar`;
- Strategy meaning or doctrine must change;
- real workforce data, production authorization, security, privacy, labor, legal, or employment policy would be required;
- the active brief does not name the behavior, path, dependency, or claim;
- passing fixture tests are being represented as usability, accessibility, safety, product-value, or production evidence.

## Completion report

For substantial work, report:

- active brief or proposal and authority status;
- files changed;
- behavior implemented or explicitly unchanged;
- tests and deterministic checks run;
- evidence class and limitations;
- bounded refactor decision;
- deferred and non-authorized work;
- cross-repository reconciliation result when material;
- next operator gate and correct actor.