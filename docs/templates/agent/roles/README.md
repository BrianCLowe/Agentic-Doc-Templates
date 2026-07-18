# Optional doc roles

> **Opt-in only.** These roles are **not** always-on and must not compete with the modular documentation rule. Default project work still uses one agent + the modular rule (installed via [`../tools/`](../tools/README.md)).

Thin, playbook-bound roles for heavier moments (intent capture, graduation, bootstrap, sync). Each role points at an existing playbook — it does **not** restate the workflow.

## Roles

| Role | File | Job | Stop when |
|------|------|-----|-----------|
| **Understanding author** | [`understanding-author.md`](understanding-author.md) | Capture **user intention** first; draft/revise `-Understanding.md` | Ready for human review (`draft`) — **no code** |
| **Doc graduate** | [`doc-graduate.md`](doc-graduate.md) | Confirmed Understanding → durable spec | Spec updated — **no code** |
| **Feature implementer** | [`feature-implementer.md`](feature-implementer.md) | Current focus → code; update that TODO | Focus item done or blocked |
| **Bootstrap** | [`bootstrap.md`](bootstrap.md) | First-time modular docs layout | [`../BOOTSTRAP.md`](../BOOTSTRAP.md) complete |
| **Template sync** | [`template-sync.md`](template-sync.md) | Pack refresh + live Master Index Step B | [`../TEMPLATE_SYNC.md`](../TEMPLATE_SYNC.md) complete |

## How to use *(no install required)*

Short asks are enough — the main agent routes by intent:

- *Draft Understanding for [Feature] from what I said — I’ll review.*
- *Continue from Current focus.*
- *Update the doc templates and sync our live docs.*

## Harness adapters *(optional install)*

Bootstrap Step 4c / [`../RULE_INSTALL.md`](../RULE_INSTALL.md) → each [`../tools/<key>.md`](../tools/README.md) installs adapters when `doc-roles` is enabled:

| Harness | Adapter source | Install to |
|---------|----------------|------------|
| Cursor | [`cursor/`](cursor/) | `.cursor/agents/` |
| Grok Build | [`grok/`](grok/) | `.grok/agents/` |
| Claude Code | `cursor/` copies (compatible shape) | `.claude/agents/` |
| Copilot / Continue / Cline | — | No agents folder; parent follows playbooks in-session |

**Parent orchestration** (in the modular rule / `AGENTS.md`): if `<name>.md` exists under a known agents folder, delegate/spawn; else follow the role playbook. Grok Build must use `.grok/agents/` — it does **not** load `.cursor/agents/` as spawn types.

`/` commands (Cursor) remain optional overrides. Descriptions use gated **Use when …**, not “use proactively.”

## Disable / remove

1. Stop naming roles / say *skip subagents*.
2. Set `optional_rules.doc-roles.status: declined` and delete installed files under `.cursor/agents/`, `.grok/agents/`, `.claude/agents/` as applicable (ask before deleting).
3. Keep the lean modular rule alone.

## Design rules *(for maintainers)*

- Roles **point** at playbooks; do not duplicate Workflow prose.
- Harness adapters only differ by **frontmatter / install path** — same body pointing at `roles/<role>.md`.
- Tool-specific install steps live in [`../tools/`](../tools/README.md), not here.
