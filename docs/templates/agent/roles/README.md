# Optional doc roles

> **Opt-in only.** These roles are **not** always-on and must not compete with the modular documentation rule. Default project work still uses one agent + the modular rule (installed via [`../tools/`](../tools/README.md)).

Thin, playbook-bound roles for heavier moments (intent capture, graduation, bootstrap, sync, backlog orchestration). Each role points at an existing playbook — it does **not** restate the workflow.

## Roles

| Role | File | Job | Stop when |
|------|------|-----|-----------|
| **Understanding author** | [`understanding-author.md`](understanding-author.md) | Capture **feature shape** first (is / is not); draft/revise `-Understanding.md` (required under **prevent**; on demand under ship-first via *lock shape*) | Ready for human **shape** review (`draft`) — **no code** |
| **Doc graduate** | [`doc-graduate.md`](doc-graduate.md) | Confirmed shape → durable **contract** spec (when Understanding exists) | Spec updated — **no code** |
| **Feature implementer** | [`feature-implementer.md`](feature-implementer.md) | Current focus → code when stem is ready under **docs profile**; update that TODO | Focus item done or blocked |
| **Orchestrator** | [`orchestrator.md`](orchestrator.md) + [`orchestrator-git.md`](orchestrator-git.md) | **Parent-only** loop + git delivery (close-out: build-verify → todo-warden → squash? → ready → **return to default** if run created the branch) | Agent work cleared / hard-blocked / budget — report + human verify inbox |
| **Work verifier** | [`work-verifier.md`](work-verifier.md) | One unit vs spec + TODO (+ Understanding when present) | Pass or fail with reasons — **no code** |
| **Todo warden** | [`todo-warden.md`](todo-warden.md) | Post-loop **docs-only** honesty + **hygiene**: reopen overclaims, cited gap TODOs (hard caps), **move** finished `[x]` into Completed | Report clean / gaps-found — **no code**; hygiene-only stays **clean** |
| **Bootstrap** | [`bootstrap.md`](bootstrap.md) | First-time modular docs layout | [`../BOOTSTRAP.md`](../BOOTSTRAP.md) complete |
| **Template sync** | [`template-sync.md`](template-sync.md) | Pack refresh (A) then live Step B | [`../TEMPLATE_SYNC.md`](../TEMPLATE_SYNC.md) → A → B |

## How to use *(no install required)*

Short asks are enough — the main agent routes by intent:

- *Draft Understanding for [Feature] from what I said — I’ll review.*
- *Continue from Current focus.*
- *Orchestrate — clear ready TODOs until blocked.*
- *Update the doc templates and sync our live docs.*

## Harness adapters *(optional install)*

Bootstrap Step 3p (doc-roles enable) / [`../RULE_INSTALL.md`](../RULE_INSTALL.md) → each [`../tools/<key>.md`](../tools/README.md) installs adapters when `doc-roles` is enabled:

| Harness | Adapter source | Install to |
|---------|----------------|------------|
| Cursor | [`cursor/`](cursor/) | `.cursor/agents/` |
| Grok Build | [`grok/`](grok/) | `.grok/agents/` |
| Claude Code | `cursor/` copies (compatible shape) | `.claude/agents/` |
| Copilot / OpenClaw / Continue / Cline | — | No agents folder; parent follows playbooks in-session — still **ask** when `optional_rules.doc-roles` is unset (record enabled/declined); “no adapters” ≠ “nothing to offer” |

**Parent orchestration** (in the modular rule / `AGENTS.md`): if `<name>.md` exists under a known agents folder, delegate/spawn; else follow the role playbook. Grok Build must use `.grok/agents/` — it does **not** load `.cursor/agents/` as spawn types.

**Orchestrator is parent-only:** follow [`orchestrator.md`](orchestrator.md) (+ [`orchestrator-git.md`](orchestrator-git.md) for git) in the **current session**. Do **not** install or spawn an `orchestrator` harness adapter — it dispatches leaf workers (`feature-implementer`, `work-verifier`, `todo-warden`) that *are* installed when doc-roles are enabled.

`/` commands (Cursor) remain optional overrides. Descriptions use gated **Use when …**, not “use proactively.”

## Disable / remove

1. Stop naming roles / say *skip subagents*.
2. Set `optional_rules.doc-roles.status: declined` and delete installed files under `.cursor/agents/`, `.grok/agents/`, `.claude/agents/` as applicable (ask before deleting).
3. Keep the lean modular rule alone.

## Design rules *(for maintainers)*

- Roles **point** at playbooks / **workflow modules**; do not duplicate Workflow prose.
- Prefer links to [`../workflow/<module>.md`](../workflow/README.md) over the whole index when the role needs one topic.
- **De-confirm / additive-vs-shape** lives only in [`../workflow/understanding.md`](../workflow/understanding.md) §4 — roles and adapters use **one-line pointers**.
- Harness adapters are **generated** from [`adapter-src/`](adapter-src/README.md) via [`../GENERATE_ROLE_ADAPTERS.md`](../GENERATE_ROLE_ADAPTERS.md) — do not hand-edit `cursor/` or `grok/` as source of truth.
- **Never** add a harness adapter for `orchestrator` — parent-only by design.
- Tool-specific install steps live in [`../tools/`](../tools/README.md), not here.
