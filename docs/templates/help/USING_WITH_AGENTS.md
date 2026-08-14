# Using These Templates With AI Coding Agents

The modular documentation **workflow is tool-agnostic**. What differs is **where each harness expects instructions**.

**Agents:** Install via [`../agent/RULE_INSTALL.md`](../agent/RULE_INSTALL.md) — ask which tools, record `docs/ADT-settings.yaml`, then open **only** [`../agent/tools/<key>.md`](../agent/tools/README.md) for each confirmed tool.

**Humans:** Use the table below. Detailed install/verify steps live in the tool playbooks (single source of truth — do not duplicate long essays here).

## Tool index

| Tool | Status key | Agent install playbook | Rule lands in |
|------|------------|------------------------|---------------|
| [Cursor](https://cursor.com) | `cursor` | [`../agent/tools/cursor.md`](../agent/tools/cursor.md) | `.cursor/rules/` |
| [Grok Build](https://docs.x.ai/build/overview) | `grok-build` | [`../agent/tools/grok-build.md`](../agent/tools/grok-build.md) | `AGENTS.md` / `.grok/rules/` · roles → `.grok/agents/` |
| [GitHub Copilot](https://github.com/features/copilot) | `github-copilot` | [`../agent/tools/github-copilot.md`](../agent/tools/github-copilot.md) | `.github/instructions/` |
| [Claude Code](https://code.claude.com) | `claude-code` | [`../agent/tools/claude-code.md`](../agent/tools/claude-code.md) | `.claude/rules/` or `CLAUDE.md` |
| Cross-tool [`AGENTS.md`](https://agents.md/) | `agents-md` | [`../agent/tools/agents-md.md`](../agent/tools/agents-md.md) | root `AGENTS.md` |
| [OpenClaw](https://docs.openclaw.ai/concepts/agent-workspace) | `openclaw` | [`../agent/tools/openclaw.md`](../agent/tools/openclaw.md) | workspace `AGENTS.md` (prefer project as workspace) |
| [Continue](https://continue.dev) | `continue` | [`../agent/tools/continue.md`](../agent/tools/continue.md) | `.continue/rules/` |
| [Cline](https://cline.bot) | `cline` | [`../agent/tools/cline.md`](../agent/tools/cline.md) | `.clinerules/` |

**No-repo brainstorms:** export chat threads to markdown → `docs/reference/` (do not attach a chat-only AGENT.md — that path is paused). See [`IDEA_CAPTURE_TIPS.md`](IDEA_CAPTURE_TIPS.md#recommended-export-idea-chats-into-docsreference).

**Recommended:** `agents-md` (shared baseline) **plus** the tool-specific playbook for your daily harness.

The modular rule guards itself: *"If `docs/Master_Index.md` does not exist, ignore this entire rule."*

**Core with every modular-rule install:**

- [`../agent/Agent_Timescale_Planning_Rule.mdc`](../agent/Agent_Timescale_Planning_Rule.mdc) — plan/ship at agent speed (target architecture first; exploration ≠ paved path). Always-on; users should not need to remind agents. When Understanding (or a clear contract) locks product-defining surface, TODOs/plans follow that target.
- [`../agent/Agent_Build_Verify_Rule.mdc`](../agent/Agent_Build_Verify_Rule.mdc) — after code changes, run the project’s build/typecheck/container/engine verify (`docs/Tooling.md` **Project verify** when filled); fix failures before “you can test.” Stack-agnostic (apps, Docker, UE, etc.).

## Optional extras

| Extra | What | Where |
|-------|------|--------|
| **Project prefs (batch)** | Docs profile, update-check, doc-roles, sync mode, orchestrator git — **one** bootstrap ask; standing notes optional | Bootstrap **Step 3p** · live keys in [`docs/ADT-settings.yaml`](../agent/ADT-settings.example.yaml) |
| **Docs profile** | `prevent` (default: Understanding + confirm), `balanced` (Understanding when identity fuzzy), `ship-first` (Spec+TODO only) | Workflow [§0.1](../agent/workflow/profile-standing.md#01-docs-profile-ceremony-modes) · `docs_profile` |
| **Standing instructions** | Freeform durable **agent process** prefs (opposes pack defaults / always-never workflow). Agents **lookout-capture** same turn | Workflow [§0.2](../agent/workflow/profile-standing.md#02-standing-workflow-instructions-user-workflow-not-pack-enums) · `standing.instructions` |
| Template update check | Upstream `VERSION` ping — default every session; interval optional | Step 3p · [`../agent/TEMPLATE_UPDATE_CHECK.md`](../agent/TEMPLATE_UPDATE_CHECK.md) |
| Doc roles | Understanding author, implementer, work verifier, … | Step 3p · [`../agent/roles/README.md`](../agent/roles/README.md) — Cursor → `.cursor/agents/`; Grok Build → `.grok/agents/` |
| Orchestrator | Parent-only backlog loop (implement → verify → next); readiness follows docs profile | [`../agent/roles/orchestrator.md`](../agent/roles/orchestrator.md) — **not** installed as a harness subagent |
| **Orchestrator git** | `local` · **`milestone-pr`** *(recommend + forge; several related TODOs + concurrent implementers when they do not overlap; squash before ready)* · `branch-pr` · `branch-pr-squash` · `branch-push` · `current-push` · `none` — ask if unset; forge probe on pick; **Cloud Agent** this-runs milestone-pr if durable is local-oriented or `branch-pr*` | Step 3p / B0.6 · [`orchestrator-git.md`](../agent/roles/orchestrator-git.md) |
| Sync mode | `auto` / `auto-all` / `choose` — dirty tree before sync still hard-stops; **git mode still asked** under auto-all if unset | Step 3p · `sync.mode` |

Parent agents **orchestrate** role delegation when asks match; `/` commands are optional. Role playbooks stay under `roles/*.md` — never paste them into always-on rules. *Orchestrate / drive the backlog* stays in the parent session and dispatches leaf workers. Settings live in **`docs/ADT-settings.yaml`** (docs profile, orchestrator git, **standing.instructions**, tools, optionals, sync mode, upstream stamps).

## Cursor conflict note

**Compound Engineering** and **Superpowers** often override the modular rule. Disable them for workspaces that rely on this pack. Details: [`../agent/tools/cursor.md`](../agent/tools/cursor.md).

## Grok Build note

`.cursor/agents/` is **not** a Grok spawn path. Use [`../agent/tools/grok-build.md`](../agent/tools/grok-build.md) so doc roles install under `.grok/agents/`.

## OpenClaw note

OpenClaw loads workspace bootstrap files (especially `AGENTS.md`), not `.cursor/rules/`. Prefer pointing the agent workspace at the **project root**, then install via [`../agent/tools/openclaw.md`](../agent/tools/openclaw.md). Do not confuse OpenClaw’s workspace `TOOLS.md` with project `docs/Tooling.md`.

## What to expect

| Expectation | Reality |
|-------------|---------|
| Agent always reads Master_Index first | Usually, if the rule is loaded — not guaranteed |
| Agent always updates TODOs | Best when the rule is active *and* you remind at session end |
| Agent plans at human sprint size | Core timescale rule pushes **target architecture** cuts; still not guaranteed every session |
| Agent says “you can test” but build is red | Core **build-verify** rule — fill Tooling **Project verify**; agent must run/fix before handoff |
| Preference polish sticks across sessions | Rule captures lasting UI choices into spec **Decisions** same turn (no wrap-up ask needed) |
| Process prefs that fight pack defaults stick | Agents lookout-capture into `standing.instructions` (or first-class keys) same turn — Workflow §0.2 |
| Same behavior across tools | Similar, not identical |
| Rules affect inline autocomplete | Generally **no** — chat/agent sessions only |

## Updating from this repo

Ask: *Update the doc templates from Agentic Doc Templates and sync our live docs.* — [`../agent/TEMPLATE_SYNC.md`](../agent/TEMPLATE_SYNC.md).

When the changelog tags `rules`, refresh **only** tools with `status: installed` by re-opening each `tools/<key>.md`. Version-only ping: *Check for template updates.* — [`../agent/TEMPLATE_UPDATE_CHECK.md`](../agent/TEMPLATE_UPDATE_CHECK.md).
