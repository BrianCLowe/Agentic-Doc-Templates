# Tool install — OpenClaw

> **Status key:** `openclaw`  
> Open only when installing or refreshing OpenClaw for this repo.
>
> OpenClaw is a **personal agent gateway** (channels, cron, workspace bootstrap files) — not a drop-in `.cursor/rules/` IDE harness. Config/credentials live under `~/.openclaw/`; the **workspace** is separate (default `~/.openclaw/workspace`). Docs: [Agent workspace](https://docs.openclaw.ai/concepts/agent-workspace).

## Before installing

**Ask which workspace** will run against this project (do not guess-write into `~/.openclaw/`):

1. **Preferred for coding this repo:** set that agent’s workspace to **this project root** (`agents.defaults.workspace` or `agents.list[].workspace` in `~/.openclaw/openclaw.json` — ask before editing config). Then install into the project’s `AGENTS.md`.
2. **Alternate:** keep the default OpenClaw workspace and append the modular-docs section there — only if the user wants OpenClaw’s home workspace (not the repo) to carry the rule. Remind them `docs/Master_Index.md` paths only resolve when the workspace/cwd is the project (or they open files by absolute path).

Record the chosen workspace path under `tools.openclaw.path` / `note` in `docs/rule-install-status.yaml`.

## Modular rule

| | |
|--|--|
| **Source** | Rule body from `docs/templates/agent/Modular_Documentation_Rule.mdc` (**strip** Cursor YAML frontmatter) |
| **Install to** | Workspace `AGENTS.md` — section titled `## Documentation workflow` |
| **Notes** | OpenClaw injects workspace `AGENTS.md` every session. **Append/merge** — never wipe SOUL/USER/IDENTITY content or the user’s existing operating rules. Include the **Optional subagents** orchestration table. Keep the section lean (bootstrap files have size limits). |

If the project also uses status key `agents-md` for the same `AGENTS.md`, do **not** duplicate the section — one `## Documentation workflow` is enough; mark both tools `installed` with a shared path note if useful.

## Optional — Template update check

Only if `optional_rules.template-update-check.status` is `enabled`.

| | |
|--|--|
| **Source** | Rule body from `docs/templates/agent/Template_Update_Check_Rule.mdc` (no Cursor frontmatter) |
| **Install to** | Same workspace `AGENTS.md` — section `## Template update check` |

Skip if the user only wants OpenClaw for chat/ops and will sync templates from an IDE agent instead.

## Optional — Doc roles

OpenClaw has **no** pack-supported `.openclaw/agents/` (or `.cursor/agents/`) install target.

| | |
|--|--|
| **Install** | **None** for adapter files |
| **Runtime** | Parent follows `docs/templates/agent/roles/<role>.md` in-session when the modular rule’s ask matches (same fallback as Copilot) |
| **Optional** | If the user also uses Cursor or Grok Build on this repo, install named subagents via those tool files |

## Conflicts / naming traps

| OpenClaw file | Not the same as |
|---------------|-----------------|
| Workspace `TOOLS.md` | Project `docs/Tooling.md` (machine/CLI install list for *this* app) |
| Workspace `BOOTSTRAP.md` | Pack [`../BOOTSTRAP.md`](../BOOTSTRAP.md) (modular docs first-time layout) |
| `~/.openclaw/` config & credentials | Must **not** be committed into the project or workspace git |

Do **not** put secrets, API keys, or `~/.openclaw/` state into the project repo.

## Verify

- Chosen workspace `AGENTS.md` contains `## Documentation workflow`
- If workspace is the project root: `docs/Master_Index.md` is reachable as a relative path
- If workspace is `~/.openclaw/workspace`: user confirmed they understand path/cwd limits
- Status yaml records `openclaw` with `path` = that `AGENTS.md`

## For humans

- Setup: `openclaw setup` / `openclaw onboard` seeds missing workspace bootstrap files without overwriting existing ones
- Treat the OpenClaw workspace as private memory if it is not the project repo
- Chat-only (no OpenClaw workspace): [`../../chat-ui/README.md`](../../chat-ui/README.md)

## Do not

- Auto-edit `~/.openclaw/openclaw.json` without an explicit user yes
- Install Cursor/Grok agent adapters into the OpenClaw workspace `skills/` folder as a substitute for doc roles
- Paste full role playbooks into always-on `AGENTS.md`
- Confuse this pack’s `docs/templates/agent/BOOTSTRAP.md` with OpenClaw’s workspace `BOOTSTRAP.md`
