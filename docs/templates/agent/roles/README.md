# Optional doc roles

> **Opt-in only.** These roles are **not** always-on and must not compete with the modular documentation rule. Default project work still uses one agent + the modular rule (installed via [`../tools/`](../tools/README.md)).

Thin, playbook-bound roles for documentation moments (intent capture, graduation, sync). Each role points at an existing playbook — it does **not** restate the workflow. The pack does not ship an implementation role or a git-delivery role.

## Roles

| Role | File | Job | Stop when |
|------|------|-----|-----------|
| **Understanding author** | [`understanding-author.md`](understanding-author.md) | Capture **feature shape** first (is / is not); draft/revise `-Understanding.md` (required under **prevent**; on demand under build-first via *lock shape*) | Ready for human **shape** review (`draft`) |
| **Doc graduate** | [`doc-graduate.md`](doc-graduate.md) | Confirmed shape → durable **contract** spec (when Understanding exists) | Spec updated |
| **Bootstrap** | [`bootstrap.md`](bootstrap.md) | **Parent-only** first-time layout (no harness adapter — bootstrap *installs* the adapters) | [`../BOOTSTRAP.md`](../BOOTSTRAP.md) complete |
| **Template sync** | [`template-sync.md`](template-sync.md) | Pack refresh (A) then live Step B | [`../TEMPLATE_SYNC.md`](../TEMPLATE_SYNC.md) → A → B |

## How to use *(no install required)*

Short asks are enough — the main agent routes by intent:

- *Draft Understanding for [Feature] from what I said — I’ll review.*
- *Graduate this Understanding into the spec.*
- *Update the doc templates and sync our live docs.*

## Harness adapters *(optional install)*

Bootstrap Step 3p (doc-roles enable) / [`../RULE_INSTALL.md`](../RULE_INSTALL.md) → each [`../tools/<key>.md`](../tools/README.md) installs adapters when `doc-roles` is enabled:

| Harness | Adapter source | Install to |
|---------|----------------|------------|
| Cursor | [`cursor/`](cursor/) | `.cursor/agents/` |
| Grok Build | [`grok/`](grok/) | `.grok/agents/` |
| Claude Code | `cursor/` copies (compatible shape) | `.claude/agents/` |
| Copilot (CLI / Agents window / Chat) | [`copilot/`](copilot/) (`*.agent.md`) | `.github/agents/` |
| OpenClaw / Continue / Cline | — | No agents folder; parent follows playbooks in-session — still **ask** when `optional_rules.doc-roles` is unset (record enabled/declined); “no adapters” ≠ “nothing to offer” |

Installed adapters: `understanding-author`, `doc-graduate`, `docs-template-sync`. Delete leftover `feature-implementer`, `work-verifier`, `todo-warden`, `orchestrator`, and `docs-bootstrap` if a previous pack left them.
