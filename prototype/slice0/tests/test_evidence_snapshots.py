import json

from cadence_professional_slice0.model import canonical_json
from cadence_professional_slice0.workflow import SCHEMA_VERSION, run_slice0


def test_committed_evidence_matches_deterministic_generation(slice0_root, fixtures_dir):
    generated = run_slice0(fixtures_dir)
    evidence_dir = slice0_root / "evidence"
    assert sorted(generated) == sorted(path.name for path in evidence_dir.glob("*.json"))

    for filename, payload in generated.items():
        committed = json.loads((evidence_dir / filename).read_text(encoding="utf-8"))
        assert canonical_json(committed) == canonical_json(payload)


def test_evidence_envelopes_use_prototype_schema_marker(fixtures_dir):
    for payload in run_slice0(fixtures_dir).values():
        assert payload["schema_version"] == SCHEMA_VERSION
        assert payload["kind"]
        assert isinstance(payload["payload"], dict)
