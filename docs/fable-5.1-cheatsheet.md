# Fable 5.1 Workflow Cheatsheet

This is a fast FableBridge interpretation of transferable workflow behaviors discussed in public Claude Fable 5.1 guidance.

## Do

- Finish the requested implementation before ending the turn when it is already authorized.
- Batch independent reads/tool calls where the harness supports it.
- Keep the user's requested scope intact.
- Prefer targeted edits for small and medium changes.
- Keep the lead agent productive while independent subagents run.
- Preserve constraints, decisions, blockers, exact paths, and next state across long tasks.
- Give brief progress updates during long tool chains.
- Verify work before claiming success.
- Complete independent work even if one part becomes blocked.

## Don't

- Stop at “next I would…” when you can do that step now.
- Ask “shall I?” for a reversible step the user already requested.
- Rewrite an entire file for a tiny change without reason.
- Sneak unrelated cleanup into the same change.
- Claim tests/builds passed without running them.
- Idle solely because a subagent is running when other useful work is available.
- Treat an instruction profile as a substitute for model capability.

## Mental completion gate

Before finishing: **scope → diff → tests → evidence → blockers**.

For detailed rules, use the canonical [`FABLE51.md`](../FABLE51.md).
