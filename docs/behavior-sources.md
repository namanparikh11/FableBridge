# Behavior Sources

FableBridge distinguishes between behaviors supported by **public Claude Fable 5.1 material** and additional **FableBridge engineering discipline**. This prevents accidental model-equivalence or proprietary-system claims.

## Primary public sources

1. **Anthropic — Prompting Claude Fable 5.1**  
   https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-fable-5-1

2. **Anthropic — Claude Fable 5.1 model overview**  
   https://platform.claude.com/docs/en/models/fable-5-1/overview

3. **Anthropic — Claude Fable product page / Fable 5.1 announcement**  
   https://www.anthropic.com/claude/fable

4. **GitHub — Claude Fable 5.1 in GitHub Copilot**  
   https://github.blog/changelog/2026-09-01-claude-fable-5-1-generally-available-in-github-copilot/

Sources were checked for V0.1 on **2026-09-03**.

## Mapping

| FableBridge behavior | Public Fable 5.1 grounding | Classification |
| --- | --- | --- |
| Finish requested work instead of stopping at a plan | Anthropic prompting guide: “Finish the whole task” | Directly grounded |
| Do not re-ask permission for reversible work already requested | Same section on autonomous completion | Directly grounded |
| Batch independent tool calls | Anthropic prompting guide: “Batch independent tool calls in agent loops” | Directly grounded |
| Concise progress reporting | Anthropic prompting guide: “Ask for user-facing progress updates” | Directly grounded |
| Preserve scope; avoid unrequested extensions | Anthropic prompting guide sections on delivering work and keeping changes/tests to the task | Directly grounded |
| Prefer targeted/surgical edits | Anthropic prompting guide: “Prefer targeted edits over whole-file rewrites” | Directly grounded |
| Keep lead agent working while subagents run | Anthropic prompting guide: “Let the lead agent keep working while subagents run” | Directly grounded |
| Preserve continuity through long tasks | Anthropic prompting guide on append-only history and compaction summaries | Directly grounded |
| Recover from failed steps and surface blockers | Consistent with long-horizon agent operation and FableBridge completion discipline | Adapted / generalized |
| Inspect diffs before finalizing | General software-engineering discipline | FableBridge-added |
| Focused tests first, broader validation where justified | General software-engineering discipline; Anthropic guidance also emphasizes verification without gratuitous permanent tests | Adapted / generalized |
| Never fabricate test or benchmark results | General evidence discipline | FableBridge-added |

## What this source map does **not** claim

It does not claim that these instructions reproduce Anthropic's private system prompt, hidden reasoning, training data, model weights, safety stack, or intelligence. Some FableBridge rules are deliberately generalized so they remain useful in agents other than Claude.
