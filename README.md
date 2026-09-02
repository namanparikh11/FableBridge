# FableBridge

### Make your coding agents work more like Fable 5.1.

**Portable Fable 5.1-inspired agentic discipline for Codex, Claude Code, OpenCode, Cursor, and GitHub Copilot.**

One behavior profile. Native instruction files for every agent. No fake “model swap” claims.

> **FableBridge transfers workflow behavior — not model intelligence.** It cannot turn another model into Claude Fable 5.1 or reproduce capabilities the underlying model does not have.

## Why FableBridge?

Claude Fable 5.1 launched with public guidance for long-horizon agentic work: finish the whole task, batch independent tool calls, keep scope tight, prefer targeted edits, preserve continuity, and keep the lead agent productive while subagents run.

Those are useful **operating behaviors** even when you use a different coding agent.

FableBridge packages the transferable parts into native instruction files you can drop into your repo.

| Behavior | FableBridge default |
| --- | --- |
| Finish implementation instead of stopping at analysis | ✅ |
| Avoid re-asking permission for already-authorized reversible work | ✅ |
| Batch independent tool calls | ✅ |
| Prefer surgical edits over whole-file rewrites | ✅ |
| Avoid unrelated scope creep | ✅ |
| Inspect changes and verify before claiming success | ✅ |
| Keep useful lead-agent work moving while subagents run | ✅ |
| Preserve continuity through long tasks | ✅ |
| Give concise progress updates | ✅ |
| Surface blockers instead of silently abandoning work | ✅ |

## 30-second install

Clone/download FableBridge, then run this **from the project where you want the instructions installed**:

```bash
python /path/to/FableBridge/scripts/install.py codex
```

Supported targets:

```text
claude-code
codex
opencode
cursor
github-copilot
```

Example:

```bash
python /path/to/FableBridge/scripts/install.py cursor
```

The installer **refuses to overwrite an existing instruction file by default**. Preview first with `--dry-run`, or use `--force` only when you explicitly want replacement.

```bash
python /path/to/FableBridge/scripts/install.py codex --dry-run
python /path/to/FableBridge/scripts/install.py codex --force
```

No installer? Just copy the matching adapter:

| Agent | Copy | To your repo |
| --- | --- | --- |
| Claude Code | `adapters/claude-code/CLAUDE.md` | `CLAUDE.md` |
| Codex | `adapters/codex/AGENTS.md` | `AGENTS.md` |
| OpenCode | `adapters/opencode/AGENTS.md` | `AGENTS.md` |
| Cursor | `adapters/cursor/fable51.mdc` | `.cursor/rules/fable51.mdc` |
| GitHub Copilot | `adapters/github-copilot/copilot-instructions.md` | `.github/copilot-instructions.md` |

If your repo already has an instruction file, **merge the FableBridge behavior profile into it** instead of overwriting project-specific rules.

## What gets installed?

The canonical profile lives in [`FABLE51.md`](FABLE51.md). Each adapter is a deterministic rendering of that same behavior contract for its native agent format.

Core rules:

1. Finish requested work unless genuinely blocked.
2. Treat the requested scope as the deliverable.
3. Parallelize independent tool work without creating write races.
4. Inspect before editing.
5. Prefer surgical changes.
6. Verify before declaring success.
7. Maintain continuity through long tasks.
8. Report progress concisely.
9. Respect evidence and safety boundaries.

## Is this a “Fable 5.1 prompt leak”?

**No.**

FableBridge is deliberately not a leaked system prompt, model imitation claim, jailbreak, fine-tune, proxy, or benchmark claim. It distills **publicly documented and generally transferable agent-workflow practices** into portable repo instructions.

Anthropic's public Fable 5.1 prompting guidance discusses, among other things, finishing whole tasks, batching independent tool calls, limiting unrequested changes, preferring targeted edits, progress updates, preserving long-context state, and allowing the lead agent to keep working while subagents run. See [`docs/behavior-sources.md`](docs/behavior-sources.md).

## What FableBridge cannot transfer

Instruction files cannot transfer:

- model weights or training;
- raw reasoning ability;
- context-window size;
- tool quality supplied by the host agent;
- hidden system instructions;
- proprietary infrastructure;
- latency, pricing, or safety architecture;
- capabilities the underlying model simply does not have.

That distinction is the point: **portable discipline, honest limits.**

## Deterministic adapters

Adapters are generated from the canonical profile:

```bash
python scripts/render.py
```

Verify that committed adapters are in sync:

```bash
python scripts/render.py --check
```

## Tests

V0.1 uses Python's standard library only:

```bash
python -m unittest discover -s tests -v
```

CI runs the adapter consistency check and the test suite on pushes and pull requests.

## Source map

- [`docs/fable-5.1-cheatsheet.md`](docs/fable-5.1-cheatsheet.md) — fast behavior summary
- [`docs/behavior-sources.md`](docs/behavior-sources.md) — what is directly grounded in public Fable 5.1 guidance vs FableBridge-added engineering discipline
- [`docs/launch-kit.md`](docs/launch-kit.md) — launch copy and checklist

## Roadmap

V0.1 stays intentionally small. Possible later versions:

- benchmark/evaluation harness;
- behavior compiler and composable profiles;
- automatic agent detection;
- more agent adapters;
- comparative evaluation across agents;
- additional frontier-model behavior profiles.

None of those are required to use FableBridge today.

## Contributing

Issues and pull requests are welcome after launch. See [`CONTRIBUTING.md`](CONTRIBUTING.md).

## License

MIT. See [`LICENSE`](LICENSE).

---

**FableBridge is an independent open-source project and is not affiliated with or endorsed by Anthropic. “Claude” and related model names belong to their respective owners.**
