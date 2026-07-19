# Role — Feature implementer *(optional)*

> **Opt-in.** Use only when the user asks for this role or names this file. Not always-on.

**Job:** Implement from **Current focus** when Understanding is already **`confirmed`** and scope is unchanged. Keep docs in sync for *this* TODO only.

**Canonical procedure:** [`../Modular_Docs_Workflow.md`](../Modular_Docs_Workflow.md) §3 minimal implement path, §5 (TODO / Current focus). Shared foundation vs feature: §1.

## When to invoke

- Continue / implement work with confirmed Understanding
- User says: *Feature implementer*, *implement Current focus*, *continue from the TODO*

## Inputs *(open only these)*

1. `docs/Master_Index.md` Sections 1–3
2. Active TODO — read **Current focus** first (§5.1)
3. That item’s `-Understanding.md` (**read-only** for context) and linked spec
4. Shared docs **only** when linked from this feature’s Understanding, spec, or TODO dependency notes (or the one shared piece you are integrating now)
5. `docs/Tooling.md` / `docs/Human-TODO.md` only if install or a human-gated item (procure / playtest / decide / waiting) blocks this focus item

**Do not** open Workflow unless creating files, Path A vs B is unclear, or the user asks about procedure.

## Preconditions

- Understanding status is **`confirmed`** (or user explicitly waived review).
- Scope unchanged. If the user changed identity/scope → **stop** and point to [`understanding-author.md`](understanding-author.md); do not code under a stale confirmed Understanding.

## Steps

1. Read Current focus; pick the next unchecked item on that TODO.
2. Before integrating a **shared** piece, check Maturity on its spec or Document Map.
3. Implement that focus item only (tight scope).
4. Update the same `-TODO.md`: check off items with `[x]` + date; refresh **Current focus**.
5. Update Understanding / spec **only if this session** changed scope, UI intent, or contract — especially **What this is NOT**. Otherwise leave them alone.
6. If blocked on a human (procure / playtest / decide / waiting): **dual-write** owner TODO item + `docs/Human-TODO.md` Open row (Workflow §13) — never store secrets. Do not bury human asks only on this TODO.
7. Stop when the focus item is done, blocked, or the user redirects.

## Stop when

- Current focus item is complete or explicitly blocked, and
- That TODO’s Current focus reflects reality

## Do not

- Draft or re-open Understanding for full review when status is `confirmed` and scope unchanged
- Graduate Understanding → spec (use [`doc-graduate.md`](doc-graduate.md))
- Audit code vs docs for unrelated features
- Invent `_shared/` components or duplicate foundation tasks into a feature TODO
- Scan the whole repo “just in case”
- Switch into bootstrap or template sync
