#!/usr/bin/env python3
"""Safely install one FableBridge adapter into a target repository."""

from __future__ import annotations

import argparse
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

ADAPTERS = {
    "claude-code": (ROOT / "adapters" / "claude-code" / "CLAUDE.md", Path("CLAUDE.md")),
    "codex": (ROOT / "adapters" / "codex" / "AGENTS.md", Path("AGENTS.md")),
    "opencode": (ROOT / "adapters" / "opencode" / "AGENTS.md", Path("AGENTS.md")),
    "cursor": (ROOT / "adapters" / "cursor" / "fable51.mdc", Path(".cursor/rules/fable51.mdc")),
    "github-copilot": (ROOT / "adapters" / "github-copilot" / "copilot-instructions.md", Path(".github/copilot-instructions.md")),
}


def install(agent: str, destination_root: Path, *, force: bool = False, dry_run: bool = False) -> Path:
    source, relative_destination = ADAPTERS[agent]
    destination_root = destination_root.resolve()
    destination = destination_root / relative_destination

    if not source.is_file():
        raise FileNotFoundError(f"Adapter missing: {source}")

    if destination.exists() and not force:
        raise FileExistsError(
            f"Refusing to overwrite existing {relative_destination}. "
            "Merge FableBridge manually, or rerun with --force for explicit replacement."
        )

    if dry_run:
        return destination

    destination.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(source, destination)
    return destination


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("agent", choices=sorted(ADAPTERS))
    parser.add_argument("--target", type=Path, default=Path.cwd(), help="repository root to install into (default: current directory)")
    parser.add_argument("--force", action="store_true", help="explicitly replace an existing destination file")
    parser.add_argument("--dry-run", action="store_true", help="show destination without writing")
    args = parser.parse_args()

    try:
        destination = install(args.agent, args.target, force=args.force, dry_run=args.dry_run)
    except (FileExistsError, FileNotFoundError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2

    verb = "Would install" if args.dry_run else "Installed"
    print(f"{verb} FableBridge {args.agent} adapter -> {destination}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
