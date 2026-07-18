# Tool install — Grok Build

> **Status key:** `grok-build`  
> Open only when installing or refreshing Grok Build for this repo.

Grok Build does **not** treat `.cursor/agents/*.md` as spawnable types. Doc-role adapters must live under **`.grok/agents/`**.

## Modular rule

| | |
|--|--|
| **Source** | Rule body from `docs/templates/agent/Modular_Documentation_Rule.mdc` (**strip** Cursor YAML frontmatter) |
| **Install to** | Root `AGENTS.md` section `## Documentation workflow` *(preferred)* — and/or `.grok/rules/modular-documentation.md` if the project uses Grok rules |
| **Notes** | Parent must load orchestration text (Optional subagents table) so it knows to `spawn_subagent`. Prefer `AGENTS.md` so other tools can share the baseline. Never overwrite custom `AGENTS.md` sections without asking — append/merge. |

Also consider installing status key `agents-md` if the user wants a shared cross-tool `AGENTS.md` (see [`agents-md.md`](agents-md.md)) — do not duplicate the same section twice.

## Optional — Template update check

Only if `optional_rules.template-update-check.status` is `enabled`. Requires live `docs/upstream-status.yaml`.

| | |
|--|--|
| **Source** | Rule body from `docs/templates/agent/Template_Update_Check_Rule.mdc` (no Cursor frontmatter) |
| **Install to** | `AGENTS.md` section `## Template update check` and/or `.grok/rules/template-update-check.md` |

## Optional — Doc roles

Only if `optional_rules.doc-roles.status` is `enabled`.

| | |
|--|--|
| **Adapter source** | `docs/templates/agent/roles/grok/*.md` *(Grok frontmatter — not the Cursor copies)* |
| **Install to** | `.grok/agents/` (same filenames) |
| **Parent delegates** | If `.grok/agents/<name>.md` exists → `spawn_subagent` with `subagent_type: <name>` and a self-contained prompt (feature paths + user ask). Else follow `docs/templates/agent/roles/<role>.md` in the parent (or spawn `general-purpose` with that playbook path). |
| **Do not** | Expect `.cursor/agents/` to register as Grok types; paste full role bodies into always-on `AGENTS.md` |

Files: `understanding-author.md`, `doc-graduate.md`, `feature-implementer.md`, `docs-bootstrap.md`, `docs-template-sync.md`.

## Verify

- Modular rule present in `AGENTS.md` and/or `.grok/rules/`
- If doc-roles enabled: five files under `.grok/agents/`
- Optional: `grok inspect` shows instruction sources
- Remind: short asks are enough; parent spawns named types when installed

## For humans

Docs: [Grok Build overview](https://docs.x.ai/build/overview). Chat-only (no repo): [`../../chat-ui/README.md`](../../chat-ui/README.md) — not this file.

## Do not

- Install Cursor `roles/cursor/` adapters into `.grok/agents/` (wrong frontmatter)
- Install Grok adapters into `.cursor/agents/`
