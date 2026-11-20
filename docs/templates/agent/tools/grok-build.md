# Tool install — Grok Build

> **Status key:** `grok-build`  
> Open only when installing or refreshing Grok Build for this project.  
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

## Retired rules *(delete on refresh)*

The pack no longer ships timescale or build-verify rules. **Delete** an `## Agent timescale planning` or `## Agent build & verify` section in `AGENTS.md`, and delete `.grok/rules/agent-timescale-planning.md` and `.grok/rules/agent-build-verify.md` if present.

## Optional — Template update check

Only if `optional_rules.template-update-check.status` is `enabled` in `docs/ADT-settings.yaml`. Requires an `upstream:` block in that file. A session check with no interval does not write it.

| | |
|--|--|
| **Source** | Rule body from `docs/templates/agent/Template_Update_Check_Rule.mdc` (no Cursor frontmatter) |
| **Install to** | `AGENTS.md` section `## Template update check` and/or `.grok/rules/template-update-check.md` |

## Optional — Doc roles

Only if `optional_rules.doc-roles.status` is `enabled`.

**Install path:** `.grok/agents/` — real product path from Grok Build’s local CLI docs (`~/.grok/README.md`, user-guide subagents/config), not a Cursor analogy. Public docs.x.ai stress `AGENTS.md` / `.grok/rules/` more clearly than named agent folders, so treat discovery as **CLI-documented + verify**, not “obvious on the marketing site.”

| | |
|--|--|
| **Adapter source** | `docs/templates/agent/roles/grok/*.md` *(generated from [`../roles/adapter-src/`](../roles/adapter-src/README.md); frontmatter aligned with bundled agents under `~/.grok/bundled/agents/` — e.g. `name`, `description`, `prompt_mode`, …)* |
| **Install to** | Project `.grok/agents/` (same filenames); user-global alternate is `~/.grok/agents/` — prefer project for this pack |
| **Parent delegates** | If `.grok/agents/<name>.md` exists **and** appears as a spawnable type → `spawn_subagent` with `subagent_type: <name>` and a self-contained prompt |
| **Fallback** | If names do not show in `grok inspect` / `/config-agents` → follow `docs/templates/agent/roles/<role>.md` in-session (or spawn `general-purpose` with that playbook path). Do not fail bootstrap; do not invent a second folder |
| **Do not** | Treat `.cursor/agents/` as Grok spawn types; paste full role bodies into always-on `AGENTS.md` |

Files: `understanding-author.md`, `doc-graduate.md`, `docs-template-sync.md`.

**Do not** install a `docs-bootstrap` adapter — bootstrap runs in the **parent** session (`BOOTSTRAP.md`). Delete leftover `docs-bootstrap.md`, `feature-implementer.md`, `work-verifier.md`, `todo-warden.md`, and `orchestrator.md` if present.

## Skills

Copy each pack skill folder `docs/templates/agent/skills/<name>/` (every adt-* folder named in `docs/templates/agent/skills/README.md`, with all its files) to `.grok/skills/<name>/` byte-identical. Refresh replaces pack-owned folders only; leave every other folder under `.grok/skills` alone. Do not put doc-role adapters there.

## Verify

- Modular rule listed by `grok inspect` from `AGENTS.md` and/or `.grok/rules/`
- Timescale and build-verify sections are **absent**
- If doc-roles enabled: three files under `.grok/agents/` (`understanding-author.md`, `doc-graduate.md`, `docs-template-sync.md`). No `docs-bootstrap` adapter. Confirm names appear under **agents** in `grok inspect --json` or `/config-agents` (non-builtin source). If missing → playbook fallback above
- Remind: short asks are enough. Subagents are **enabled by default**; only check `GROK_SUBAGENTS=0` / `[subagents] enabled = false` if spawning fails or the user disabled them
- All 9 adt-* folders under .grok/skills, each with SKILL.md.


## For humans

No-project brainstorms: export chats -> `docs/reference/` - [`../../help/IDEA_CAPTURE_TIPS.md`](../../help/IDEA_CAPTURE_TIPS.md#recommended-export-idea-chats-into-docsreference) (chat-only AGENT.md path is paused).

## Do not

- Install Cursor `roles/cursor/` adapters into `.grok/agents/` (wrong frontmatter)
- Install Grok adapters into `.cursor/agents/` or `.github/agents/` as a substitute for `.grok/agents/`
- Abort rule install if inspect does not list custom types yet — keep files + use playbook fallback
