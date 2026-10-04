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

## Retired rules *(delete on refresh)*

The pack no longer ships timescale or build-verify rules. If these files exist, **delete** them:

- `.cursor/rules/agent-timescale-planning.mdc`
- `.cursor/rules/agent-build-verify.mdc`

## Optional — Template update check

Only if `optional_rules.template-update-check.status` is `enabled` in `docs/ADT-settings.yaml`. Requires an `upstream:` block in that file. A session check with no interval does not write it.

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

Files: `understanding-author.md`, `doc-graduate.md`, `docs-template-sync.md`.

**Do not** install a `docs-bootstrap` adapter — bootstrap runs in the **parent** session (`BOOTSTRAP.md`). Bootstrap *installs* adapters, so a bootstrap adapter cannot exist until after the job it was meant to do. Delete leftover `docs-bootstrap.md`, `feature-implementer.md`, `work-verifier.md`, `todo-warden.md`, and `orchestrator.md` if present.

## Optional — Slash commands

Only if `optional_rules.slash-commands.status` is `enabled`. These are Cursor slash commands, not rules and not skills.

| | |
|--|--|
| **Source** | `docs/templates/agent/commands/sync.md` |
| **Install to** | `.cursor/commands/sync.md` |
| **Do not** | Paste the sync playbook into the command file. Delete a leftover `orchestrate.md` |

`/sync` runs the same playbook as the short ask.

## Conflicts

**Compound Engineering** and **Superpowers** often override the modular rule (skip Master Index / Understanding). Recommend disabling them for this workspace.

## Verify

- `.cursor/rules/modular-documentation.mdc` exists
- Timescale and build-verify rules are **absent**
- If doc-roles enabled: three files under `.cursor/agents/` (`understanding-author.md`, `doc-graduate.md`, `docs-template-sync.md`). No `docs-bootstrap` adapter
- If slash-commands enabled: `.cursor/commands/sync.md` only. No orchestrate command
- Remind user: short asks are enough; parent rule delegates; `/name` optional

## For humans

Scoped rule only: set `alwaysApply: false` and `globs: docs/**` — usually worse for this pack. Details: [`../../help/USING_WITH_AGENTS.md`](../../help/USING_WITH_AGENTS.md).

## Do not

- Paste role playbook bodies into the always-on rule
- Treat `.grok/agents/`, `.claude/agents/`, or `.github/agents/` as Cursor install targets (other tool files own those)
