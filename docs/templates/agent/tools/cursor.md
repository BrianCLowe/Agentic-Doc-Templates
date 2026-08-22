# Tool install — Cursor

> **Status key:** `cursor`  
> Open only when installing or refreshing Cursor for this repo.  
> Docs: [Rules](https://cursor.com/docs/context/rules) · [Subagents](https://cursor.com/docs/subagents)

## Modular rule

| | |
|--|--|
| **Source** | `docs/templates/agent/Modular_Documentation_Rule.mdc` |
| **Install to** | `.cursor/rules/modular-documentation.mdc` |
| **Notes** | Keep `alwaysApply: true` for this workflow (applies before a doc file is open). Never overwrite a customized file without showing the diff and asking. |

## Agent timescale planning *(core — always install with modular rule)*

| | |
|--|--|
| **Source** | `docs/templates/agent/Agent_Timescale_Planning_Rule.mdc` |
| **Install to** | `.cursor/rules/agent-timescale-planning.mdc` |
| **Notes** | `alwaysApply: true`. Target architecture at agent speed; users should not need to remind. |

## Agent build & verify *(core — always install with modular rule)*

| | |
|--|--|
| **Source** | `docs/templates/agent/Agent_Build_Verify_Rule.mdc` |
| **Install to** | `.cursor/rules/agent-build-verify.mdc` |
| **Notes** | `alwaysApply: true`. Run project build/typecheck/container/engine verify before “you can test”; fix failures. |

## Optional — Template update check

Only if `optional_rules.template-update-check.status` is `enabled` in `docs/ADT-settings.yaml`. Requires `upstream:` stamps in that file.

| | |
|--|--|
| **Source** | `docs/templates/agent/Template_Update_Check_Rule.mdc` |
| **Install to** | `.cursor/rules/template-update-check.mdc` |

## Optional — Doc roles

Only if `optional_rules.doc-roles.status` is `enabled`. These are [Cursor subagents](https://cursor.com/docs/subagents), **not** Agent Skills.

| | |
|--|--|
| **Adapter source** | `docs/templates/agent/roles/cursor/*.md` *(generated from [`../roles/adapter-src/`](../roles/adapter-src/README.md) — do not hand-edit)* |
| **Install to** | `.cursor/agents/` (same filenames) |
| **Parent delegates** | If `.cursor/agents/<name>.md` exists → launch that subagent with a self-contained prompt |
| **Do not** | Install under `.cursor/skills/`; add “use proactively” / “always use for” to descriptions |

Files: `understanding-author.md`, `doc-graduate.md`, `feature-implementer.md`, `work-verifier.md`, `todo-warden.md`, `docs-bootstrap.md`, `docs-template-sync.md`.

**Do not** install an `orchestrator` adapter — orchestration runs in the **parent** session via `docs/templates/agent/roles/orchestrator.md` (spawns leaf workers only).

## Conflicts

**Compound Engineering** and **Superpowers** often override the modular rule (skip Master Index / Understanding). Recommend disabling them for this workspace.

## Verify

- `.cursor/rules/modular-documentation.mdc` exists
- `.cursor/rules/agent-timescale-planning.mdc` exists
- `.cursor/rules/agent-build-verify.mdc` exists
- If doc-roles enabled: seven files under `.cursor/agents/` (no `orchestrator.md`; includes `todo-warden.md`)
- Remind user: short asks are enough; parent rule delegates; `/name` optional

## For humans

Scoped rule only: set `alwaysApply: false` and `globs: docs/**` — usually worse for this pack. Details: [`../../help/USING_WITH_AGENTS.md`](../../help/USING_WITH_AGENTS.md).

## Do not

- Paste role playbook bodies into the always-on rule
- Treat `.grok/agents/`, `.claude/agents/`, or `.github/agents/` as Cursor install targets (other tool files own those)
