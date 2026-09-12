# Scaffolds vs teaching

Live files under `docs/` are **fill-in blanks**. Teaching, examples, and “how to write this” live here in `help/` (humans) and in [`../agent/workflow/`](../agent/workflow/README.md) (agents). Do not copy sermons into a live Understanding, spec, TODO, or Master Index At a Glance.

| Live file | What you fill in | Humans read | Agents re-open when context is thin |
|-----------|------------------|-------------|-------------------------------------|
| `*-Understanding.md` | Shape blanks: is / is not, Relationship, Assumptions | This page + [`IDEA_CAPTURE_TIPS.md`](IDEA_CAPTURE_TIPS.md) | [`workflow/understanding.md`](../agent/workflow/understanding.md) |
| Feature / shared **spec** | Contract: Architecture, Behavior, Acceptance, Decisions, Visual refs | [`USAGE.md`](USAGE.md) | [`workflow/understanding.md`](../agent/workflow/understanding.md) §2 |
| `*-TODO.md` | Current focus + work list (operable / kit coverage) | [`USAGE.md`](USAGE.md) | [`workflow/todos.md`](../agent/workflow/todos.md) |
| `Master_Index.md` | Overview + Document Map | [`SETUP.md`](SETUP.md) | [`workflow/naming-layout.md`](../agent/workflow/naming-layout.md) |
| `Human-TODO.md` / `Tooling.md` | Inbox / machine tools | This pack’s help | [`workflow/human-todo.md`](../agent/workflow/human-todo.md) · [`workflow/tooling.md`](../agent/workflow/tooling.md) |
| `docs/decisions/` | Cross-cutting **why** | [`USAGE.md`](USAGE.md) | [`workflow/decisions.md`](../agent/workflow/decisions.md) |

**Compaction / new session / memory loss:** Agents re-open the [workflow index](../agent/Modular_Docs_Workflow.md), then **only** the matching router module. Do not reconstruct procedure from the scaffold or from chat memory. Humans stay in `help/` — you do not need the playbooks.

---

## Reviewing Understanding *(shape, not the spec)*

The agent drafts this file. You confirm **general feature shape**:

1. **What this is** — category, metaphor, “feels like,” ownership, product-defining surface.
2. **What this is NOT** — wrong category / wrong architecture identity. Not a backlog of “not built yet.”
3. **Relationship** — extends / wraps / reuses vs greenfield.
4. **Assumptions** — **real forks only.** Empty is correct when obvious defaults were locked in is / is not. Examples in `docs/reference/` are not the target unless you clearly set them as the target. You may be **offered** an Assumptions clean-out pass (agent lock gate: [`workflow/understanding.md`](../agent/workflow/understanding.md) §4).

You are **not** signing off flows, API tables, acceptance, or the TODO. Missing spec detail here is normal.

When shape looks right, set **Status** to `confirmed` (or tell the agent to). If a TODO is marked done but the build is the wrong *kind of thing*, say so — the agent should uncheck and reopen.

Worked examples (too thin / right size / mini-spec, good vs bad is-not, lock vs invented assumption): [`workflow/understanding.md`](../agent/workflow/understanding.md) §4.

---

## Spec, TODO, decisions

- **Spec** = durable contract after shape confirm (or from day one under **ship-first**).
- **TODO** = living work list. User-facing stems need an **exercise path**, not library-only “done.”
- **Decisions** on the spec (or `docs/decisions/` if cross-cutting) = why we chose X, so a later session cannot silently undo it.

Day-to-day asks: [`USAGE.md`](USAGE.md). First install: [`SETUP.md`](SETUP.md).
