# Optional doc roles

> **Opt-in only.** These roles are **not** always-on and must not compete with the modular documentation rule. Default project work still uses one agent + the modular rule (installed via [`../tools/`](../tools/README.md)).

Thin, playbook-bound roles for heavier moments (intent capture, graduation, bootstrap, sync, backlog orchestration). Each role points at an existing playbook — it does **not** restate the workflow.

## Roles

| Role | File | Job | Stop when |
|------|------|-----|-----------|
| **Understanding author** | [`understanding-author.md`](understanding-author.md) | Capture **feature shape** first (is / is not); draft/revise `-Understanding.md` (required under **prevent**; on demand under build-first via *lock shape*) | Ready for human **shape** review (`draft`) — **no code** |
| **Doc graduate** | [`doc-graduate.md`](doc-graduate.md) | Confirmed shape → durable **contract** spec (when Understanding exists) | Spec updated — **no code** |
| **Feature implementer** | [`feature-implementer.md`](feature-implementer.md) | Current focus → code when stem is ready under **docs profile**; update that TODO | Focus item done or blocked |
| **Orchestrator** | [`orchestrator.md`](orchestrator.md) + [`orchestrator-git.md`](orchestrator-git.md) | **Parent-only** loop + git delivery (**`milestone-pr`:** per-milestone PR — several related TODOs + concurrent implementers when they do not overlap **and** the host can isolate → CI/Bugbot → merge → next branch; Bugbot reads the PR until ready — squash-before-ready is not required; **host worktree:** stay, do not checkout default in that tree; **`branch-pr*`:** build-verify → outcome audit → squash? → ready → **return to default** if run created the branch **in the main checkout**) | Agent work cleared / hard-blocked / budget — report. The outcome audit owns the parent-outcome check |
| **Work verifier** | [`work-verifier.md`](work-verifier.md) | One unit vs spec + TODO (+ Understanding when present) | Pass or fail with reasons — **no code** |
| **Todo warden** | [`todo-warden.md`](todo-warden.md) | Post-loop **docs-only** honesty + **hygiene** + **outcome audit** (check the parent outcome, fill one Exercise or cited follow-ups). The same audit section runs in the parent session when this adapter is not installed | Report clean / gaps-found — **no code**; hygiene-only stays **clean** |
| **Bootstrap** | [`bootstrap.md`](bootstrap.md) | **Parent-only** first-time layout (no harness adapter — bootstrap *installs* the adapters) | [`../BOOTSTRAP.md`](../BOOTSTRAP.md) complete |
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
| Copilot (CLI / Agents window / Chat) | [`copilot/`](copilot/) (`*.agent.md`) | `.github/agents/` |
| OpenClaw / Continue / Cline | — | No agents folder; parent follows playbooks in-session — still **ask** when `optional_rules.doc-roles` is unset (record enabled/declined); “no adapters” ≠ “nothing to offer” |

**Parent orchestration** (in the modular rule / `AGENTS.md`): if `<name>.md` exists under a known agents folder — or `<name>.agent.md` under `.github/agents/` — delegate/spawn; else follow the role playbook. Grok Build must use `.grok/agents/` — it does **not** load `.cursor/agents/` as spawn types. Copilot must use `.github/agents/` — it does **not** load `.cursor/agents/` as custom agents.

**Orchestrator is parent-only:** follow [`orchestrator.md`](orchestrator.md) (+ [`orchestrator-git.md`](orchestrator-git.md) for git) in the **current session**. Do **not** install or spawn an `orchestrator` harness adapter — it dispatches leaf workers (`feature-implementer`, `work-verifier`, `todo-warden`) that *are* installed when doc-roles are enabled.

**Bootstrap is parent-only:** follow [`../BOOTSTRAP.md`](../BOOTSTRAP.md) (or [`bootstrap.md`](bootstrap.md)) in the **current session**. Do **not** install or spawn a `docs-bootstrap` adapter — that playbook is what *installs* doc-roles, so the adapter would not exist until after bootstrap finished.

`/` commands (Cursor) remain optional overrides. Descriptions use gated **Use when …**, not “use proactively.”

## Disable / remove

1. Stop naming roles / say *skip subagents*.
2. Set `optional_rules.doc-roles.status: declined` and delete installed files under `.cursor/agents/`, `.grok/agents/`, `.claude/agents/`, `.github/agents/` as applicable (ask before deleting).
3. Keep the lean modular rule alone.

## Design rules *(for maintainers)*

- Roles **point** at playbooks / **workflow modules**; do not duplicate Workflow prose.
- Prefer links to [`../workflow/<module>.md`](../workflow/README.md) over the whole index when the role needs one topic.
- **De-confirm / additive-vs-shape** lives only in [`../workflow/understanding.md`](../workflow/understanding.md) §4 — roles and adapters use **one-line pointers**.
- Harness adapters are **generated** from [`adapter-src/`](adapter-src/README.md) via [`../GENERATE_ROLE_ADAPTERS.md`](../GENERATE_ROLE_ADAPTERS.md) — do not hand-edit `cursor/`, `grok/`, or `copilot/` as source of truth.
- **Never** add a harness adapter for `orchestrator` or `docs-bootstrap` — parent-only by design (bootstrap installs the adapters).
- Tool-specific install steps live in [`../tools/`](../tools/README.md), not here.
