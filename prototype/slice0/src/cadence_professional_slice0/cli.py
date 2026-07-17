from __future__ import annotations

import argparse
from pathlib import Path

from .workflow import write_evidence


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Generate deterministic Cadence Professional Slice 0 evidence snapshots."
    )
    parser.add_argument(
        "--fixtures",
        type=Path,
        default=Path("fixtures"),
        help="Directory containing the synthetic portfolio and request fixtures.",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=Path("evidence"),
        help="Directory where evidence snapshots will be written.",
    )
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    evidence = write_evidence(args.fixtures, args.output)
    print(f"Generated {len(evidence)} deterministic evidence snapshots in {args.output}")
    return 0
