from dataclasses import replace

import pytest

from cadence_professional_slice0.model import ConstraintSet, load_portfolio, load_request
from cadence_professional_slice0.scheduler import schedule_portfolio
from cadence_professional_slice0.workflow import (
    AuthorizationError,
    StaleBaselineError,
    apply_authorized_scenario,
    authorize_scenario,
    hold_scenario,
    revalidate_scenario,
    required_authorization_scopes,
    simulate,
)


def test_observe_simulate_negotiate_hold_authorize_revalidate_apply(fixtures_dir):
    portfolio = load_portfolio(fixtures_dir / "project_x_portfolio_v0.json")
    request = load_request(fixtures_dir / "expedite_project_x_request_v0.json")
    no_overtime = ConstraintSet(max_overtime_minutes_per_staff=0)
    one_hour_overtime = ConstraintSet(max_overtime_minutes_per_staff=60)

    baseline = schedule_portfolio(portfolio, portfolio.baseline_project_order, no_overtime)
    scenario_v1 = simulate(portfolio, request, baseline, 1, no_overtime)
    scenario_v2 = simulate(portfolio, request, baseline, 2, one_hour_overtime)

    assert scenario_v1.state == "SIMULATED"
    assert scenario_v2.state == "SIMULATED"
    assert scenario_v2.schedule.project_completion_minutes["project-x"] < scenario_v1.schedule.project_completion_minutes["project-x"]
    assert scenario_v2.impacts.incremental_overtime_premium == "42.50"
    assert scenario_v2.impacts.deadlines_crossed == ("project-y",)
    assert scenario_v2.impacts.displaced_projects == ("project-y", "project-z")
    assert scenario_v2.change_set_digest != scenario_v1.change_set_digest

    held = hold_scenario(scenario_v2)
    assert held.state == "HELD_PENDING_AUTHORIZATION"
    assert held.baseline_revision_id == portfolio.revision_id

    scopes = required_authorization_scopes(held)
    authorization = authorize_scenario(
        held,
        authorized_by="synthetic-budget-owner",
        scopes=scopes,
    )
    assert authorization.scenario_version == 2
    assert authorization.change_set_digest == held.change_set_digest

    valid = revalidate_scenario(held, portfolio.revision_id)
    assert valid.status == "VALID"
    applied = apply_authorized_scenario(held, authorization, valid)
    assert applied.prior_revision_id == portfolio.revision_id
    assert applied.scenario_version == held.version
    assert applied.authorization_id == authorization.authorization_id
    assert applied.change_set_digest == held.change_set_digest
    assert applied.revision_id != portfolio.revision_id


def test_stale_baseline_and_exact_authorization_are_enforced(fixtures_dir):
    portfolio = load_portfolio(fixtures_dir / "project_x_portfolio_v0.json")
    request = load_request(fixtures_dir / "expedite_project_x_request_v0.json")
    baseline = schedule_portfolio(
        portfolio,
        portfolio.baseline_project_order,
        ConstraintSet(max_overtime_minutes_per_staff=0),
    )
    scenario = hold_scenario(
        simulate(
            portfolio,
            request,
            baseline,
            2,
            ConstraintSet(max_overtime_minutes_per_staff=60),
        )
    )
    authorization = authorize_scenario(
        scenario,
        authorized_by="synthetic-budget-owner",
        scopes=required_authorization_scopes(scenario),
    )

    stale = revalidate_scenario(scenario, "portfolio-r2")
    with pytest.raises(StaleBaselineError):
        apply_authorized_scenario(scenario, authorization, stale)

    wrong_version = replace(authorization, scenario_version=1)
    valid = revalidate_scenario(scenario, portfolio.revision_id)
    with pytest.raises(AuthorizationError):
        apply_authorized_scenario(scenario, wrong_version, valid)

    wrong_digest = replace(authorization, change_set_digest="not-the-approved-change-set")
    with pytest.raises(AuthorizationError):
        apply_authorized_scenario(scenario, wrong_digest, valid)


def test_authorization_requires_all_consequence_scopes(fixtures_dir):
    portfolio = load_portfolio(fixtures_dir / "project_x_portfolio_v0.json")
    request = load_request(fixtures_dir / "expedite_project_x_request_v0.json")
    baseline = schedule_portfolio(
        portfolio,
        portfolio.baseline_project_order,
        ConstraintSet(max_overtime_minutes_per_staff=0),
    )
    held = hold_scenario(
        simulate(
            portfolio,
            request,
            baseline,
            2,
            ConstraintSet(max_overtime_minutes_per_staff=60),
        )
    )

    with pytest.raises(AuthorizationError, match="overtime"):
        authorize_scenario(
            held,
            authorized_by="synthetic-project-manager",
            scopes=("assignment_changes", "portfolio_displacement"),
        )
