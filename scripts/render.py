#!/usr/bin/env python3
"""Deterministically render native FableBridge adapter files."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CANONICAL = ROOT / "FABLE51.md"

TARGETS = {
    "claude-code": ROOT / "adapters" / "claude-code" / "CLAUDE.md",
    "codex": ROOT / "adapters" / "codex" / "AGENTS.md",
    "opencode": ROOT / "adapters" / "opencode" / "AGENTS.md",
    "cursor": ROOT / "adapters" / "cursor" / "fable51.mdc",
    "github-copilot": ROOT / "adapters" / "github-copilot" / "copilot-instructions.md",
}

HEADERS = {
    "claude-code": "# FableBridge for Claude Code\n\n",
    "codex": "# FableBridge for Codex\n\n",
    "opencode": "# FableBridge for OpenCode\n\n",
    "github-copilot": "# FableBridge for GitHub Copilot\n\n",
}

CURSOR_FRONTMATTER = "---\ndescription: Fable 5.1-inspired agentic workflow discipline\nalwaysApply: true\n---\n\n# FableBridge for Cursor\n\n"

GENERATED_NOTE = "<!-- Generated from FABLE51.md by scripts/render.py. Edit the canonical profile, then re-render. -->\n\n"


def canonical_body() -> str:
    text = CANONICAL.read_text(encoding="utf-8").replace("\r\n", "\n").rstrip() + "\n"
    return text


def render(target: str) -> str:
    if target == "cursor":
        prefix = CURSOR_FRONTMATTER
    else:
        prefix = HEADERS[target]
    return GENERATED_NOTE + prefix + canonical_body()


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="fail if committed adapters differ from deterministic render")
    args = parser.parse_args()

    mismatches: list[str] = []
    for name, path in TARGETS.items():
        expected = render(name)
        if args.check:
            actual = path.read_text(encoding="utf-8") if path.exists() else None
            if actual != expected:
                mismatches.append(str(path.relative_to(ROOT)))
        else:
            path.parent.mkdir(parents=True, exist_ok=True)
            with path.open("w", encoding="utf-8", newline="\n") as handle:
                handle.write(expected)

    if mismatches:
        print("Adapters out of sync:", file=sys.stderr)
        for path in mismatches:
            print(f"  - {path}", file=sys.stderr)
        print("Run: python scripts/render.py", file=sys.stderr)
        return 1

    if args.check:
        print(f"OK: {len(TARGETS)} adapters match FABLE51.md")
    else:
        print(f"Rendered {len(TARGETS)} adapters")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
