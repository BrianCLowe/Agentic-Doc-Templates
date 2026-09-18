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

## Agent timescale planning *(core — always install with modular rule)*

| | |
|--|--|
| **Source** | Rule body from `docs/templates/agent/Agent_Timescale_Planning_Rule.mdc` (**strip** Cursor YAML frontmatter) |
| **Install to** | Root `AGENTS.md` section `## Agent timescale planning` *(preferred)* **and/or** `.grok/rules/agent-timescale-planning.md` |

Do not duplicate the section if `agents-md` already installed it.

## Agent build & verify *(core — always install with modular rule)*

| | |
|--|--|
| **Source** | Rule body from `docs/templates/agent/Agent_Build_Verify_Rule.mdc` (**strip** Cursor YAML frontmatter) |
| **Install to** | Root `AGENTS.md` section `## Agent build & verify` *(preferred)* **and/or** `.grok/rules/agent-build-verify.md` |

Do not duplicate the section if `agents-md` already installed it.

## Optional — Template update check

Only if `optional_rules.template-update-check.status` is `enabled` in `docs/ADT-settings.yaml`. Requires `upstream:` stamps in that file.

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

Files: `understanding-author.md`, `doc-graduate.md`, `feature-implementer.md`, `work-verifier.md`, `todo-warden.md`, `docs-template-sync.md`.

**Do not** install an `orchestrator` or `docs-bootstrap` adapter — those run in the **parent** session (`roles/orchestrator.md` / `BOOTSTRAP.md`). Delete leftover `docs-bootstrap.md` if present.

## Successive issues *(parent — do not fan out PRs)*

Grok parents often `spawn_subagent` a new coding agent per complaint. Live docs (`*-TODO.md` Current focus, spec, Understanding) are rewritten every session — **docs overlap ≠ code overlap**.

When the user files another issue / complaint in this parent session:

1. `gh pr list --state open` (or forge equivalent).
2. Open PR already touches this stem’s TODO/spec/Understanding → **do not spawn** a new agent+branch+PR. Re-brief the in-flight agent or add commits to that PR. Remember stem → PR for the rest of this session.
3. Different stem **and** you will not edit the other PR’s live docs → a new PR is OK.

Policy: [`../workflow/session-freshness.md`](../workflow/session-freshness.md) **Docs-overlapping PRs**. The always-loaded modular rule (installed into `AGENTS.md`) is what the parent sees at spawn time — do not leave this only in this install file.

## Host isolation *(orchestrator parallel implementers)*

Parent opens this only when spawning concurrent implementers ([`../roles/orchestrator-git.md`](../roles/orchestrator-git.md) **Host worktrees**).

| | |
|--|--|
| **Can isolate?** | **Yes** — `spawn_subagent` with `isolation: worktree` (do **not** also pass `cwd`; they are mutually exclusive) |
| **Cannot** | Isolation denied / subagents disabled → parent stays **serial** |
| **Already in one** | cwd under `~/.grok/worktrees` or `grok -w` / `/fork --worktree` session → **stay**; do not `grok worktree rm` this tree |
| **Do not** | `git worktree add`; invent `.adt-worktrees/` |

Compat (secondary, when enabled): **Claude** `.claude/agents/` can load as spawnable types. **Cursor** `compat.cursor.agents` is for named instruction files under Cursor paths — **not** “load `.cursor/agents/*.md` as Grok spawn types.” Always install this pack’s roles under `.grok/agents/`.

## Verify

- Modular rule listed by `grok inspect` from `AGENTS.md` and/or `.grok/rules/`
- Agent timescale planning present in `AGENTS.md` and/or `.grok/rules/`
- Agent build & verify present in `AGENTS.md` and/or `.grok/rules/`
- If doc-roles enabled: six files under `.grok/agents/` (no `orchestrator.md` / `docs-bootstrap.md`; includes `todo-warden.md`); confirm names appear under **agents** in `grok inspect --json` or `/config-agents` (non-builtin source). If missing → playbook fallback above
- Remind: short asks are enough. Subagents are **enabled by default**; only check `GROK_SUBAGENTS=0` / `[subagents] enabled = false` if spawning fails or the user disabled them

## For humans

No-repo brainstorms: export chats → `docs/reference/` — [`../../help/IDEA_CAPTURE_TIPS.md`](../../help/IDEA_CAPTURE_TIPS.md#recommended-export-idea-chats-into-docsreference) (chat-only AGENT.md path is paused).

## Do not

- Install Cursor `roles/cursor/` adapters into `.grok/agents/` (wrong frontmatter)
- Install Grok adapters into `.cursor/agents/` or `.github/agents/` as a substitute for `.grok/agents/`
- Abort rule install if inspect does not list custom types yet — keep files + use playbook fallback
