# Tool install — Grok Build

> **Status key:** `grok-build`  
> Open only when installing or refreshing Grok Build for this repo.  
> Public docs: [Overview](https://docs.x.ai/build/overview) · [AGENTS.md / project rules](https://docs.x.ai/build/features/project-rules) · [Skills & compat](https://docs.x.ai/build/features/skills-plugins-marketplaces)  
> **Local CLI docs** (`~/.grok/README.md`, `~/.grok/docs/…`) can be ahead of docs.x.ai — prefer local + `grok inspect` when they disagree.

**Instructions (public + local):** `AGENTS.md` / `CLAUDE.md` family, plus every `*.md` in `.grok/rules/` (compat also reads `.claude/rules/`, `.cursor/rules/`).

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

**Install path:** `.grok/agents/` — real product path from Grok Build’s local CLI docs (`~/.grok/README.md`, user-guide subagents/config), not a Cursor analogy. Public docs.x.ai stress `AGENTS.md` / `.grok/rules/` more clearly than named agent folders, so treat discovery as **CLI-documented + verify**, not “obvious on the marketing site.”

| | |
|--|--|
| **Adapter source** | `docs/templates/agent/roles/grok/*.md` *(frontmatter aligned with bundled agents under `~/.grok/bundled/agents/` — e.g. `name`, `description`, `prompt_mode`, …)* |
| **Install to** | Project `.grok/agents/` (same filenames); user-global alternate is `~/.grok/agents/` — prefer project for this pack |
| **Parent delegates** | If `.grok/agents/<name>.md` exists **and** appears as a spawnable type → `spawn_subagent` with `subagent_type: <name>` and a self-contained prompt |
| **Fallback** | If names do not show in `grok inspect` / `/config-agents` → follow `docs/templates/agent/roles/<role>.md` in-session (or spawn `general-purpose` with that playbook path). Do not fail bootstrap; do not invent a second folder |
| **Do not** | Treat `.cursor/agents/` as Grok spawn types; paste full role bodies into always-on `AGENTS.md` |

Files: `understanding-author.md`, `doc-graduate.md`, `feature-implementer.md`, `docs-bootstrap.md`, `docs-template-sync.md`.

Compat (secondary): Claude/Cursor agent folders may also be scanned when compat is on — still install this pack’s roles under `.grok/agents/`.

## Verify

- Modular rule listed by `grok inspect` from `AGENTS.md` and/or `.grok/rules/`
- If doc-roles enabled: five files under `.grok/agents/`; confirm names appear under **agents** in `grok inspect --json` or `/config-agents` (non-builtin source). If missing → playbook fallback above
- Remind: short asks are enough; `GROK_SUBAGENTS=1` / `[subagents] enabled` may be required for spawning

## For humans

Chat-only (no repo): [`../../chat-ui/README.md`](../../chat-ui/README.md) — not this file.

## Do not

- Install Cursor `roles/cursor/` adapters into `.grok/agents/` (wrong frontmatter)
- Install Grok adapters into `.cursor/agents/` as a substitute for `.grok/agents/`
- Abort rule install if inspect does not list custom types yet — keep files + use playbook fallback
