# Tool install — Grok Build

> **Status key:** `grok-build`  
> Open only when installing or refreshing Grok Build for this repo.  
> Docs: [Overview](https://docs.x.ai/build/overview) · [AGENTS.md / project rules](https://docs.x.ai/build/features/project-rules) · [Skills & compat](https://docs.x.ai/build/features/skills-plugins-marketplaces)  
> **Note:** Grok Build’s **local** docs can be ahead of the public site — prefer local/`grok inspect` when they disagree.

**Instructions:** `AGENTS.md` / `CLAUDE.md` family, plus every `*.md` in `.grok/rules/` (compat also reads `.claude/rules/`, `.cursor/rules/`).

## Modular rule

| | |
|--|--|
| **Source** | Rule body from `docs/templates/agent/Modular_Documentation_Rule.mdc` (**strip** Cursor YAML frontmatter) |
| **Install to** | Root `AGENTS.md` section `## Documentation workflow` *(preferred)* **and/or** `.grok/rules/modular-documentation.md` |
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

**Correct install path:** `.grok/agents/` (confirmed against Grok Build local docs; public web docs may lag). Manage/list with `/config-agents` (alias `/agents`).

| | |
|--|--|
| **Adapter source** | `docs/templates/agent/roles/grok/*.md` *(Grok frontmatter — not the Cursor copies)* |
| **Install to** | `.grok/agents/` (same filenames) |
| **Parent delegates** | If `.grok/agents/<name>.md` exists → `spawn_subagent` with `subagent_type: <name>` and a self-contained prompt. Else follow `docs/templates/agent/roles/<role>.md` in-session (or spawn `general-purpose` with that playbook path). |
| **Do not** | Treat `.cursor/agents/` as Grok spawn types; paste full role bodies into always-on `AGENTS.md` |

Files: `understanding-author.md`, `doc-graduate.md`, `feature-implementer.md`, `docs-bootstrap.md`, `docs-template-sync.md`.

Compat (secondary): Grok can also read Claude/Cursor agent folders when compat scanners are on — still install this pack’s roles under `.grok/agents/`.

## Verify

- Modular rule listed by `grok inspect` from `AGENTS.md` and/or `.grok/rules/`
- If doc-roles enabled: five files under `.grok/agents/` (optional: confirm in `/config-agents`)
- Remind: short asks are enough; parent spawns named types when installed; `GROK_SUBAGENTS=1` / `[subagents] enabled` may be required for spawning

## For humans

Chat-only (no repo): [`../../chat-ui/README.md`](../../chat-ui/README.md) — not this file.

## Do not

- Install Cursor `roles/cursor/` adapters into `.grok/agents/` (wrong frontmatter)
- Install Grok adapters into `.cursor/agents/` as a substitute for `.grok/agents/`
