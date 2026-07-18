# Tool install — Grok Build

> **Status key:** `grok-build`  
> Open only when installing or refreshing Grok Build for this repo.  
> Docs: [Overview](https://docs.x.ai/build/overview) · [AGENTS.md / project rules](https://docs.x.ai/build/features/project-rules) · [Skills & compat](https://docs.x.ai/build/features/skills-plugins-marketplaces)

**Documented instruction discovery** (from xAI project-rules docs): `AGENTS.md` / `CLAUDE.md` family, plus every `*.md` in `.grok/rules/` (and compat: `.claude/rules/`, `.cursor/rules/`). Verify with `grok inspect`.

## Modular rule

| | |
|--|--|
| **Source** | Rule body from `docs/templates/agent/Modular_Documentation_Rule.mdc` (**strip** Cursor YAML frontmatter) |
| **Install to** | Root `AGENTS.md` section `## Documentation workflow` *(preferred — officially documented)* **and/or** `.grok/rules/modular-documentation.md` |
| **Notes** | Parent must load orchestration text (Optional subagents table) so it can spawn named types when present. Prefer `AGENTS.md` so other tools can share the baseline. Never overwrite custom `AGENTS.md` sections without asking — append/merge. |

Also consider status key `agents-md` for the same `AGENTS.md` — do not duplicate the section twice.

## Optional — Template update check

Only if `optional_rules.template-update-check.status` is `enabled`. Requires live `docs/upstream-status.yaml`.

| | |
|--|--|
| **Source** | Rule body from `docs/templates/agent/Template_Update_Check_Rule.mdc` (no Cursor frontmatter) |
| **Install to** | `AGENTS.md` section `## Template update check` and/or `.grok/rules/template-update-check.md` |

## Optional — Doc roles

Only if `optional_rules.doc-roles.status` is `enabled`.

xAI public docs document **instruction** paths clearly; **named custom agent files** are managed via `/config-agents` (alias `/agents`) and compat scanners. This pack’s primary install for Grok-named types:

| | |
|--|--|
| **Adapter source** | `docs/templates/agent/roles/grok/*.md` |
| **Install to** | `.grok/agents/` (same filenames) |
| **Parent delegates** | If `.grok/agents/<name>.md` exists → `spawn_subagent` with `subagent_type: <name>` and a self-contained prompt. Else follow `docs/templates/agent/roles/<role>.md` in-session (or spawn `general-purpose` with that playbook path). |
| **Compat alternates** *(officially scanned)* | Grok also reads Claude agents (`.claude/agents/`) and can scan Cursor agents when `GROK_CURSOR_AGENTS_ENABLED` / `[compat.cursor] agents` is on — do **not** rely on that instead of `.grok/agents/` unless `grok inspect` / `/config-agents` shows the types |
| **Do not** | Paste full role bodies into always-on `AGENTS.md` |

Files: `understanding-author.md`, `doc-graduate.md`, `feature-implementer.md`, `docs-bootstrap.md`, `docs-template-sync.md`.

After install: run **`grok inspect`** and/or **`/config-agents`** so the five names appear as spawnable types. If they do not, fall back to playbooks in-session and file an issue — do not invent a second folder.

## Verify

- Modular rule listed by `grok inspect` from `AGENTS.md` and/or `.grok/rules/`
- If doc-roles enabled: five files under `.grok/agents/` **and** visible in `/config-agents` (or inspect)
- Remind: short asks are enough; parent spawns named types when installed; `GROK_SUBAGENTS=1` / `[subagents] enabled` may be required for spawning

## For humans

Chat-only (no repo): [`../../chat-ui/README.md`](../../chat-ui/README.md) — not this file.

## Do not

- Install Cursor `roles/cursor/` adapters into `.grok/agents/` (wrong frontmatter)
- Assume `.cursor/agents/` alone is enough for Grok without verifying inspect/config-agents
