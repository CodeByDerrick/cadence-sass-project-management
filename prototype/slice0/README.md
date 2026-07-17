# Cadence Professional Slice 0

This directory contains a **prototype-only**, headless Python proof of the professional orchestration chain:

```text
Observe -> Simulate -> Explain -> Negotiate Constraints -> Hold -> Authorize -> Revalidate -> Apply
```

It uses synthetic people, tasks, projects, rates, deadlines, PTO, and authority. It does not provide production scheduling, employment decisions, authentication, databases, integrations, billing, multi-tenancy, or a canonical Cadence schema.

## Run

From this directory:

```bash
python -m pip install -e ".[dev]"
python -m pytest
python -m cadence_professional_slice0 --fixtures fixtures --output evidence
```

The second command regenerates the committed evidence snapshots deterministically.

## Proof boundary

The prototype demonstrates that:

- simulation does not mutate the baseline;
- task eligibility and PTO are hard constraints;
- accelerating Project X exposes effects on Project Y and Project Z;
- a one-hour total overtime allowance per involved staff member changes the proposal and cost;
- explanations cite explicit fixture facts;
- a held scenario is not authorization;
- authorization binds to one exact scenario version and change-set digest;
- an exact baseline revision mismatch rejects application;
- successful application produces a new operational revision with lineage.

## Important assumption

For Slice 0, “one hour of overtime for each staff member involved” means **at most 60 total overtime minutes per staff member across the scenario**. This is a deliberately simple prototype rule, not a product or labor-policy decision.
