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
| **Runtime** | Orchestration text in the modular rule section tells the parent to look for harness agent folders (`.cursor/agents/`, `.grok/agents/`, `.github/agents/`, …) or fall back to role playbooks |
| **Adapters** | Install via [`cursor.md`](cursor.md), [`grok-build.md`](grok-build.md), [`claude-code.md`](claude-code.md), or [`github-copilot.md`](github-copilot.md) when those tools are `installed` |

## Skills

Install to: root `AGENTS.md`, section `## Skills` (create it if missing). Add or refresh the 9 pack rows below, matched by the Skill column. Keep every other row and line already in that section.

Do not paste skill bodies into AGENTS.md.

| Skill | Path | Use when |
| --- | --- | --- |
| adt-bootstrap | `docs/templates/agent/skills/adt-bootstrap/SKILL.md` | Use when the user says bootstrap, init modular docs, or Bootstrap the doc templates. Parent session only. |
| adt-template-sync | `docs/templates/agent/skills/adt-template-sync/SKILL.md` | Use when the user says update or sync the doc templates, update the doc templates, update ADT, or sync ADT. |
| adt-template-update-check | `docs/templates/agent/skills/adt-template-update-check/SKILL.md` | Use when the user says check for template updates or check for ADT updates. |
| adt-rule-install | `docs/templates/agent/skills/adt-rule-install/SKILL.md` | Use when the user says install agent rules, or install Cursor, Claude, or Grok rules. |
| adt-generate-role-adapters | `docs/templates/agent/skills/adt-generate-role-adapters/SKILL.md` | Use when the user says regenerate role adapters, or sync cursor or grok agents from adapter-src. |
| adt-understanding | `docs/templates/agent/skills/adt-understanding/SKILL.md` | Use when the user says draft or revise Understanding, new idea, capture intent, correct What this is / is not, or build live docs from docs/reference/. |
| adt-doc-graduate | `docs/templates/agent/skills/adt-doc-graduate/SKILL.md` | Use when the user says graduate a confirmed Understanding to a spec. |
| adt-product-vision | `docs/templates/agent/skills/adt-product-vision/SKILL.md` | Use when the user says lock product shape, draft Product-Vision, or the product vision is missing or fights a feature. |
| adt-docs-profile | `docs/templates/agent/skills/adt-docs-profile/SKILL.md` | Use when docs_profile is unset, the user says set docs profile, or standing instructions need a cleanout or an upgrade. |

## Verify

- `AGENTS.md` contains `## Documentation workflow`
- Section still points at `docs/Master_Index.md` + Workflow / roles paths
- Root `AGENTS.md` has `## Skills` with all 9 pack skill rows, and every non-pack row that was there before is still there.

## For humans

Nested `AGENTS.md` in monorepo subfolders can override root. Keep this section short — long files compete with other context.

## Do not

- Paste full `roles/*.md` playbooks into `AGENTS.md`
- Remove the user’s Build/test or project-specific sections when merging
