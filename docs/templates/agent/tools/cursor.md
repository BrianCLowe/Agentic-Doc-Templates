# Tool install — Cursor

> **Status key:** `cursor`  
> Open only when installing or refreshing Cursor for this repo.

## Modular rule

| | |
|--|--|
| **Source** | `docs/templates/agent/Modular_Documentation_Rule.mdc` |
| **Install to** | `.cursor/rules/modular-documentation.mdc` |
| **Notes** | Keep `alwaysApply: true` for this workflow (applies before a doc file is open). Never overwrite a customized file without showing the diff and asking. |

## Optional — Template update check

Only if `optional_rules.template-update-check.status` is `enabled`. Requires live `docs/upstream-status.yaml`.

| | |
|--|--|
| **Source** | `docs/templates/agent/Template_Update_Check_Rule.mdc` |
| **Install to** | `.cursor/rules/template-update-check.mdc` |

## Optional — Doc roles

Only if `optional_rules.doc-roles.status` is `enabled`. These are [Cursor subagents](https://cursor.com/docs/subagents), **not** Agent Skills.

| | |
|--|--|
| **Adapter source** | `docs/templates/agent/roles/cursor/*.md` |
| **Install to** | `.cursor/agents/` (same filenames) |
| **Parent delegates** | If `.cursor/agents/<name>.md` exists → launch that subagent with a self-contained prompt |
| **Do not** | Install under `.cursor/skills/`; add “use proactively” / “always use for” to descriptions |

Files: `understanding-author.md`, `doc-graduate.md`, `feature-implementer.md`, `docs-bootstrap.md`, `docs-template-sync.md`.

## Conflicts

**Compound Engineering** and **Superpowers** often override the modular rule (skip Master Index / Understanding). Recommend disabling them for this workspace.

## Verify

- `.cursor/rules/modular-documentation.mdc` exists
- If doc-roles enabled: five files under `.cursor/agents/`
- Remind user: short asks are enough; parent rule delegates; `/name` optional

## For humans

Scoped rule only: set `alwaysApply: false` and `globs: docs/**` — usually worse for this pack. Details: [`../../help/USING_WITH_AGENTS.md`](../../help/USING_WITH_AGENTS.md).

## Do not

- Paste role playbook bodies into the always-on rule
- Treat `.grok/agents/` or `.claude/agents/` as Cursor install targets (other tool files own those)
