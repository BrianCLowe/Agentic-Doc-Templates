# Tool install — Claude Code

> **Status key:** `claude-code`  
> Open only when installing or refreshing Claude Code for this repo.  
> Docs: [Memory](https://code.claude.com/docs/en/memory) · [Subagents](https://code.claude.com/docs/en/sub-agents)

## Modular rule

| | |
|--|--|
| **Source** | Rule body from `docs/templates/agent/Modular_Documentation_Rule.mdc` (**strip** Cursor YAML frontmatter) |
| **Install to** | `.claude/rules/modular-documentation.md` *(preferred for modular rules)* **or** section in `./CLAUDE.md` / `./.claude/CLAUDE.md` |
| **Notes** | Ask before merging into an existing `CLAUDE.md`. Keep concise (Claude recommends short instruction files). Claude does **not** auto-load root `AGENTS.md` — if using [`agents-md.md`](agents-md.md), put `@AGENTS.md` in `CLAUDE.md`. |

## Retired rules *(delete on refresh)*

The pack no longer ships timescale or build-verify rules. **Delete** `.claude/rules/agent-timescale-planning.md`, `.claude/rules/agent-build-verify.md`, and those labeled sections in `CLAUDE.md` if present.

## Optional — Template update check

Only if `optional_rules.template-update-check.status` is `enabled`.

| | |
|--|--|
| **Source** | Rule body from `docs/templates/agent/Template_Update_Check_Rule.mdc` (no Cursor frontmatter) |
| **Install to** | `.claude/rules/template-update-check.md` or labeled section in `CLAUDE.md` |

## Optional — Doc roles

Only if `optional_rules.doc-roles.status` is `enabled`. Claude project subagents: [Create custom subagents](https://code.claude.com/docs/en/sub-agents) → `.claude/agents/`.

| | |
|--|--|
| **Adapter source** | `docs/templates/agent/roles/cursor/*.md` *(name + description + body; Claude also accepts `model: inherit`)* |
| **Install to** | `.claude/agents/` (same filenames) |
| **Parent delegates** | If `.claude/agents/<name>.md` exists → Task/delegate to that subagent with a self-contained prompt; else role playbook fallback |
| **Note** | User-scope `~/.claude/agents/` is personal — prefer project `.claude/agents/` for this pack |

Copy the three `roles/cursor/*.md` adapters (`understanding-author.md`, `doc-graduate.md`, `docs-template-sync.md`). **Do not** invent a `docs-bootstrap` adapter — bootstrap is parent-only. Delete leftover `docs-bootstrap.md`, `feature-implementer.md`, `work-verifier.md`, `todo-warden.md`, and `orchestrator.md` if present.

## Optional — Slash commands

Only if `optional_rules.slash-commands.status` is `enabled`.

| | |
|--|--|
| **Source** | `docs/templates/agent/commands/sync.md` |
| **Install to** | `.claude/commands/sync.md` |
| **Do not** | Paste the sync playbook into the command file. Delete a leftover `orchestrate.md` |

## Verify

- Modular rule file or `CLAUDE.md` section exists
- Timescale and build-verify rules are **absent**
- Optional: `/memory` shows the modular docs section
- If doc-roles enabled: three files under `.claude/agents/` (`understanding-author.md`, `doc-graduate.md`, `docs-template-sync.md`). No `docs-bootstrap` adapter
- If slash-commands enabled: `.claude/commands/sync.md` only

## For humans

Docs: [Claude Code memory](https://code.claude.com/docs/en/memory). Cross-tool baseline: consider [`agents-md.md`](agents-md.md).

## Do not

- Paste full role playbooks into always-on `CLAUDE.md`
- Use Grok-only frontmatter from `roles/grok/` here
