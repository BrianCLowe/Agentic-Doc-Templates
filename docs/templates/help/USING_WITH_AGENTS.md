# Using These Templates With AI Coding Agents

The modular documentation **workflow is tool-agnostic**. What differs is **where each harness expects instructions**.

**Agents:** Install via [`../agent/RULE_INSTALL.md`](../agent/RULE_INSTALL.md) — ask which tools, record `docs/rule-install-status.yaml`, then open **only** [`../agent/tools/<key>.md`](../agent/tools/README.md) for each confirmed tool.

**Humans:** Use the table below. Detailed install/verify steps live in the tool playbooks (single source of truth — do not duplicate long essays here).

## Tool index

| Tool | Status key | Agent install playbook | Rule lands in |
|------|------------|------------------------|---------------|
| [Cursor](https://cursor.com) | `cursor` | [`../agent/tools/cursor.md`](../agent/tools/cursor.md) | `.cursor/rules/` |
| [Grok Build](https://docs.x.ai/build/overview) | `grok-build` | [`../agent/tools/grok-build.md`](../agent/tools/grok-build.md) | `AGENTS.md` / `.grok/rules/` · roles → `.grok/agents/` |
| [GitHub Copilot](https://github.com/features/copilot) | `github-copilot` | [`../agent/tools/github-copilot.md`](../agent/tools/github-copilot.md) | `.github/instructions/` |
| [Claude Code](https://code.claude.com) | `claude-code` | [`../agent/tools/claude-code.md`](../agent/tools/claude-code.md) | `.claude/rules/` or `CLAUDE.md` |
| Cross-tool [`AGENTS.md`](https://agents.md/) | `agents-md` | [`../agent/tools/agents-md.md`](../agent/tools/agents-md.md) | root `AGENTS.md` |
| [Continue](https://continue.dev) | `continue` | [`../agent/tools/continue.md`](../agent/tools/continue.md) | `.continue/rules/` |
| [Cline](https://cline.bot) | `cline` | [`../agent/tools/cline.md`](../agent/tools/cline.md) | `.clinerules/` |
| Chat UI (no repo) | — | [`../chat-ui/README.md`](../chat-ui/README.md) | Attach `chat-ui/AGENT.md` only |

**Recommended:** `agents-md` (shared baseline) **plus** the tool-specific playbook for your daily harness.

The modular rule guards itself: *"If `docs/Master_Index.md` does not exist, ignore this entire rule."*

## Optional extras

| Extra | What | Where |
|-------|------|--------|
| Template update check | Weekly upstream `VERSION` ping | Bootstrap Step 4b · [`../agent/TEMPLATE_UPDATE_CHECK.md`](../agent/TEMPLATE_UPDATE_CHECK.md) |
| Doc roles | Understanding author, implementer, … | Bootstrap Step 4c · [`../agent/roles/README.md`](../agent/roles/README.md) — Cursor → `.cursor/agents/`; Grok Build → `.grok/agents/` |

Parent agents **orchestrate** role delegation when asks match; `/` commands are optional. Role playbooks stay under `roles/*.md` — never paste them into always-on rules.

## Cursor conflict note

**Compound Engineering** and **Superpowers** often override the modular rule. Disable them for workspaces that rely on this pack. Details: [`../agent/tools/cursor.md`](../agent/tools/cursor.md).

## Grok Build note

`.cursor/agents/` is **not** a Grok spawn path. Use [`../agent/tools/grok-build.md`](../agent/tools/grok-build.md) so doc roles install under `.grok/agents/`.

## What to expect

| Expectation | Reality |
|-------------|---------|
| Agent always reads Master_Index first | Usually, if the rule is loaded — not guaranteed |
| Agent always updates TODOs | Best when the rule is active *and* you remind at session end |
| Same behavior across tools | Similar, not identical |
| Rules affect inline autocomplete | Generally **no** — chat/agent sessions only |

## Updating from this repo

Ask: *Update the doc templates from Agentic Doc Templates and sync our live docs.* — [`../agent/TEMPLATE_SYNC.md`](../agent/TEMPLATE_SYNC.md).

When the changelog tags `rules`, refresh **only** tools with `status: installed` by re-opening each `tools/<key>.md`. Version-only ping: *Check for template updates.* — [`../agent/TEMPLATE_UPDATE_CHECK.md`](../agent/TEMPLATE_UPDATE_CHECK.md).
