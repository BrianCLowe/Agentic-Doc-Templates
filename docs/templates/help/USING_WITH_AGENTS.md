# Using These Templates With AI Coding Agents

The modular documentation **workflow is tool-agnostic**. The rule content is the same everywhere: read `docs/Master_Index.md` (Sections 1–3), follow `docs/templates/Modular_Docs_Workflow.md` for procedure, update TODOs after changes.

What differs is **where each tool expects instructions** and how reliably it follows them. No agent treats project rules like a linter — they are guidance loaded into context, not hard enforcement.

**Installing the rule:** Agents should follow [`../agent/RULE_INSTALL.md`](../agent/RULE_INSTALL.md) — ask which tool(s) you use, record the answer in `docs/rule-install-status.yaml` (so each tool is only asked once), never overwrite existing instructions without confirmation, and support multiple tools on the same repo without conflict.

## Quick reference

| Tool | Where to put the rule | Template file |
|------|------------------------|---------------|
| [Cursor](https://cursor.com) | `.cursor/rules/` | [`../agent/Modular_Documentation_Rule.mdc`](../agent/Modular_Documentation_Rule.mdc) |
| [GitHub Copilot](https://github.com/features/copilot) (VS Code) | `.github/copilot-instructions.md` or `.github/instructions/` | [`../agent/Modular_Documentation_Rule.instructions.md`](../agent/Modular_Documentation_Rule.instructions.md) |
| [Claude Code](https://code.claude.com) | `CLAUDE.md` or `.claude/rules/` | Copy rule body into a new `.md` file |
| [Continue](https://continue.dev) | `.continue/rules/` | Copy rule body; use Cursor-style frontmatter |
| [Cline](https://cline.bot) | `.clinerules/` or `.cline/rules/` | Copy rule body into a new `.md` file |
| [Grok.com / ChatGPT / Claude web](../chat-ui/README.md) | Attach [`../chat-ui/AGENT.md`](../chat-ui/AGENT.md) only | Short chat-only instructions — save-as output |
| [Grok Build](https://x.ai/news/grok-build-cli) | `AGENTS.md` (also reads `CLAUDE.md`) | Copy rule body into `AGENTS.md` |
| [OpenAI Codex](https://developers.openai.com/codex) | `AGENTS.md` | Copy rule body into `AGENTS.md` |
| Cross-tool (recommended) | Root `AGENTS.md` | Copy rule body — see below |

Tools change quickly. If a path above stops working, check that tool's docs for "custom instructions", "rules", or `AGENTS.md` support.

## Recommended approach: one rule, two layers

1. **Cross-tool:** Add the rule to root [`AGENTS.md`](https://agents.md/) so Copilot, Claude Code, Grok Build, Cline, and others that read it get the same baseline.
2. **Tool-specific:** Copy the matching template file when a tool needs its own format (Cursor `.mdc`, Copilot `.instructions.md`, etc.).

The rule already guards itself: *"If `docs/Master_Index.md` does not exist, ignore this entire rule."* That makes it safe to install before a project has adopted modular docs.

---

## GitHub Copilot (VS Code)

Copilot uses **custom instructions**, not Cursor-style rules. They apply to **Chat and Agent mode**, not inline autocomplete as you type.

**Option A — project-wide (simplest at work):**  
Paste the rule into `.github/copilot-instructions.md` at the repo root.

**Option B — scoped file:**  
Copy [`../agent/Modular_Documentation_Rule.instructions.md`](../agent/Modular_Documentation_Rule.instructions.md) to `.github/instructions/modular-documentation.instructions.md`.

Ensure `.github/instructions` is enabled in workspace settings if needed:

```json
"chat.instructionsFilesLocations": {
  ".github/instructions": true
}
```

**Tips:**
- Run `/init` in Copilot Chat to scaffold a starter instructions file, then add the modular docs section.
- If you open a subfolder of a monorepo, enable `chat.useCustomizationsInParentRepositories` so root instructions are discovered.
- Copilot may still need an occasional nudge: *"Follow the modular docs workflow — start from Master_Index."*

Docs: [VS Code custom instructions](https://code.visualstudio.com/docs/copilot/customization/custom-instructions)

---

## Cursor

Copy [`../agent/Modular_Documentation_Rule.mdc`](../agent/Modular_Documentation_Rule.mdc) to `.cursor/rules/`.

The file uses `alwaysApply: true` so the rule is included every session. To scope it to documentation work only, set `alwaysApply: false` and add `globs: docs/**` — but for this workflow, always-on is usually better because the rule applies *before* you open a doc file.

---

## Claude Code

Copy the rule body into either:

- **`CLAUDE.md`** at the project root (team-shared, simple), or
- **`.claude/rules/modular-documentation.md`** (modular; supports path-scoped frontmatter)

Run `/init` to generate a starter `CLAUDE.md`, then add the modular docs section. Use `/memory` to verify what loaded.

Keep instruction files concise — long files compete with other context. This rule is short enough to include whole.

Docs: [Claude Code memory](https://code.claude.com/docs/en/memory)

---

## Continue.dev

Create `.continue/rules/modular-documentation.md` with the rule body and frontmatter:

```markdown
---
name: Modular Documentation
description: Read Master_Index first; use feature TODOs as living task lists
alwaysApply: true
---
```

Rules in `.continue/rules/` load automatically for that workspace.

Docs: [Continue rules](https://docs.continue.dev/customize/deep-dives/rules)

---

## Cline

Copy the rule into `.clinerules/modular-documentation.md` (or `.cline/rules/` depending on your Cline version).

Optional path scoping via frontmatter:

```markdown
---
paths:
  - "docs/**"
---
```

Rules without frontmatter are always active. Cline also reads root `AGENTS.md` for cross-tool compatibility.

Docs: [Cline rules](https://docs.cline.bot/customization/cline-rules)

---

## Grok.com / chat UI (no workspace)

When brainstorming in **Grok.com**, ChatGPT, Claude web, or similar — **before you have a repo** or when the agent cannot write files — do **not** attach the whole `docs/templates/` folder. Too many files dilute focus; use the short chat pack instead.

**Use instead:**

| Priority | File |
|----------|------|
| **Required** | [`../chat-ui/AGENT.md`](../chat-ui/AGENT.md) — flat paths, file set table, save-as output format |
| Optional | `../Master_Index_Template.md`, `../Feature_Understanding_Template.md` |

Human guide: [`../chat-ui/README.md`](../chat-ui/README.md). Workflows: [`USAGE.md`](USAGE.md) Pattern 1.

**Example prompt:**

> Follow `AGENT.md`. Turn our conversation into modular docs for [app name]. Each file must start with **Save as:** `docs/...` so I can download them. Draft `-Understanding.md` first.

After you paste files into your project, copy `docs/templates/` and use IDE rules or Grok Build below for ongoing work.

---

## Grok Build

Grok Build picks up **`AGENTS.md`** and **`CLAUDE.md`** from the repo automatically. Add the rule to root `AGENTS.md` (or a section in `CLAUDE.md`).

Run `grok inspect` in the project to see which instruction sources were discovered.

Docs: [Grok Build overview](https://docs.x.ai/build/overview)

---

## OpenClaw

OpenClaw is a different category: a **personal agent gateway** (chat channels, cron, skills) configured mainly via `~/.openclaw/openclaw.json` and per-agent `agent.md` files — not typical repo-local coding rules.

If you use OpenClaw to work on a codebase, point its agent workspace at your repo and add the modular docs workflow to that agent's identity/instructions manually. There is no standard `.openclaw/rules/` drop-in equivalent to Cursor or Copilot today.

Docs: [OpenClaw configuration](https://docs.openclaw.ai/gateway/configuration)

---

## AGENTS.md (cross-tool)

[`AGENTS.md`](https://agents.md/) is plain Markdown with no required frontmatter. Many tools read it automatically. A minimal project file might look like:

```markdown
# AGENTS.md

## Documentation workflow

[Paste the Modular Documentation Rule section here]

## Build and test

[Your project commands]
```

For monorepos, nested `AGENTS.md` files in subfolders can override or extend root rules.

---

## What to expect

| Expectation | Reality |
|-------------|---------|
| Agent always reads Master_Index first | Usually, if the rule is loaded — not guaranteed |
| Agent always updates TODOs | Works best when the rule is active *and* you remind it at session end |
| Same behavior across tools | Similar, not identical — each tool merges instructions differently |
| Rules affect inline autocomplete | Generally **no** (Copilot inline, etc.) — chat/agent sessions only |

Treat the rule as **institutional memory for the agent**, not a substitute for good prompts on complex tasks.

---

## Updating from this repo

You can just ask the agent to update the doc templates. It follows [`../agent/TEMPLATE_SYNC.md`](../agent/TEMPLATE_SYNC.md):

1. **Download the pack** — Replace project `docs/templates/` only (ZIP/copy). Do **not** use git to update live docs from upstream.
2. **Update live docs from the local pack as needed** — use files under `docs/templates/` to update `Master_Index.md`, Understanding, specs, and TODOs.
3. **Rules** — Update installed copies if the rule body in the local pack changed.
4. **TODO / Understanding format** — Add missing sections from the local templates only.

**Example:** *Update the doc templates from Agentic Doc Templates and sync our live docs.*

Keep tool-specific rule copies in sync, or maintain a single `AGENTS.md` section and copy to tool paths if your team uses multiple agents.
