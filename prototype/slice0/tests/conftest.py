from pathlib import Path

import pytest


@pytest.fixture(scope="session")
def slice0_root() -> Path:
    return Path(__file__).resolve().parents[1]


@pytest.fixture(scope="session")
def fixtures_dir(slice0_root: Path) -> Path:
    return slice0_root / "fixtures"
