# Tool install — AGENTS.md (cross-tool)

> **Status key:** `agents-md`  
> Open only when installing or refreshing a root `AGENTS.md` documentation section.  
> Spec: [agents.md](https://agents.md/) · Grok: [project rules](https://docs.x.ai/build/features/project-rules)

Many harnesses read [`AGENTS.md`](https://agents.md/) (Grok Build, Codex, Cline, Cursor, Copilot, others). Useful as a **shared baseline** alongside tool-specific installs.

**Claude Code caveat:** Claude loads `CLAUDE.md` / `.claude/rules/`, **not** `AGENTS.md` by default. If this section is the shared source of truth, add `@AGENTS.md` near the top of `CLAUDE.md` (see [Claude Code memory](https://code.claude.com/docs/en/memory#agentsmd)) or install via [`claude-code.md`](claude-code.md).

## Modular rule

| | |
|--|--|
| **Source** | Rule body from `docs/templates/agent/Modular_Documentation_Rule.mdc` (**strip** Cursor YAML frontmatter) |
| **Install to** | Root `AGENTS.md` — section titled `## Documentation workflow` |
| **Notes** | Append if the file already has content; do not delete unrelated sections. Include the **Optional subagents** orchestration table so parents that only load `AGENTS.md` still know to delegate/spawn. |

## Optional — Template update check

Only if `optional_rules.template-update-check.status` is `enabled`.

| | |
|--|--|
| **Source** | Rule body from `docs/templates/agent/Template_Update_Check_Rule.mdc` (no Cursor frontmatter) |
| **Install to** | `AGENTS.md` section `## Template update check` |

## Optional — Doc roles

`AGENTS.md` is **not** an agents-folder install target.

| | |
|--|--|
| **Install** | **None** here |
| **Runtime** | Orchestration text in the modular rule section tells the parent to look for harness agent folders (`.cursor/agents/`, `.grok/agents/`, …) or fall back to role playbooks |
| **Adapters** | Install via [`cursor.md`](cursor.md), [`grok-build.md`](grok-build.md), or [`claude-code.md`](claude-code.md) when those tools are `installed` |

## Verify

- `AGENTS.md` contains `## Documentation workflow`
- Section still points at `docs/Master_Index.md` + Workflow / roles paths

## For humans

Nested `AGENTS.md` in monorepo subfolders can override root. Keep this section short — long files compete with other context.

## Do not

- Paste full `roles/*.md` playbooks into `AGENTS.md`
- Remove the user’s Build/test or project-specific sections when merging
