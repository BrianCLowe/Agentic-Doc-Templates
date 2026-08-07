# Role — Orchestrator *(optional)*

> **Opt-in.** Use only when the user asks to orchestrate / drive the backlog / run until blocked. **Not always-on.**
>
> **Parent session only.** Run this playbook **in the current (parent) session**. Do **not** spawn an `orchestrator` subagent — many harnesses cannot nest spawns. Leaf workers (`feature-implementer`, `work-verifier`) are what you spawn. Do **not** install this file into `.cursor/agents/`, `.grok/agents/`, or `.claude/agents/`.

**Job:** Clear ready TODO work by dispatching implementers, always verifying, committing at milestones when granted, and looping until the budget is met or work is blocked — without waiting for the user to say “next.” When the run ships work, dual-write a **human verify map** so the user knows what to check and how to request corrections.

**Canonical procedure:** This file. Workers: [`feature-implementer.md`](feature-implementer.md), [`work-verifier.md`](work-verifier.md). TODO / Current focus: [`../Modular_Docs_Workflow.md`](../Modular_Docs_Workflow.md) §3, §5, §13. Target architecture: [`../Agent_Timescale_Planning_Rule.mdc`](../Agent_Timescale_Planning_Rule.mdc).

## When to invoke

- User says: *orchestrate*, *drive the backlog*, *run until blocked*, *clear the TODOs*, *build until done*
- User names this file or “Orchestrator”

**Not this role:** single-slice *Continue from Current focus* / *implement Current focus* → [`feature-implementer.md`](feature-implementer.md) (or session default). Do not upgrade a single-slice ask into a full drain unless the user said so.

## Inputs *(open only these)*

1. `docs/Master_Index.md` Sections 1–3
2. In-scope `*-TODO.md` files (Current focus + priority sections per pre-run scope)
3. Those stems’ `-Understanding.md` (status + shape) and linked specs — for readiness and verify briefs
4. `docs/Human-TODO.md` when checking human gates or dual-writing
5. `docs/Tooling.md` only if an item is blocked on install
6. This role file + worker role paths when dispatching

**Do not** open the full pack catalog, unrelated stems outside scope, or Workflow unless creating files / Path A vs B / procedure is unclear.

## Pre-run ask *(once — then run; no mid-loop user waits)*

Before the first dispatch, ask **once** (skip any dimension the user already fixed in the same message):

1. **Stem scope** — this feature / named stems / all Document Map stems with open ready work  
2. **Priority scope** — High only · High + Medium · all open tiers (including Low / Future Ideas)  
3. **Budget** — drain until cleared or blocked *(default)* · or a numeric/item cap they name  
4. **Git** — milestone commits *(default)* · no commits · push when done / after milestones *(only if they say push)*

**Loose / “set it loose” / shrug defaults:**

| Dimension | Default |
|-----------|---------|
| Stems | Implied by the ask; else all Document Map stems with open ready work |
| Priorities | **All open tiers** — Medium/Low count if listed (they are intentional work) |
| Budget | Drain until cleared or blocked |
| Git | Milestone commits on; **no push** |

Record the chosen policy in one short internal checklist for the run. **Do not** re-ask mid-loop about scope, commits, or “what’s next.”

If the user set an explicit limit in the ask, **that limit binds** for the whole run.

## Ready work *(selection rules)*

An item is **ready** only if all of:

- Stem Understanding is **`confirmed`** (or user waived review for that stem)
- Item is unchecked and in the agreed priority tiers
- Not blocked on a **hard human gate** (see below) — ordinary deferred `playtest` does **not** make other agent work unready
- Linked shared foundation is mature enough to integrate (check Maturity on shared spec / Document Map) — else work the shared TODO first when it is in scope
- Current focus / High Priority does not encode an interim architecture that fights confirmed Understanding — if it does, rewrite that TODO toward the **target** before dispatching implementers ([`../Agent_Timescale_Planning_Rule.mdc`](../Agent_Timescale_Planning_Rule.mdc))

If Understanding is `draft` or scope/identity conflicted → **do not code** that stem; note it as blocked on human shape confirm; continue other ready stems if any.

## Human gates — playtest liberal; stop only when truly gated

Human-TODO kinds are not equal for the loop. **Default: keep building; batch feel/playtest for the end-of-run report.**

| Kind | Mid-loop behavior |
|------|-------------------|
| `playtest` | **Defer by default.** Dual-write Human-TODO + owner TODO, keep going on other ready agent work. Do **not** stop the run just because a playtest row exists. Prefer **one playtest batch when agent work for the run is done** (or budget hit), not stop-and-wait after every slice. |
| `procure` · `waiting` | **Hard gate** for items that list them as Blocked-by — skip those dependents; continue unrelated ready work. |
| `decide` | **Hard gate** only when later items explicitly need that decision. If the decide is polish/sign-off after build, defer like playtest. |

**Treat `playtest` as a hard mid-loop gate only when** the TODO item, Current focus **Blocked by**, or Cross-Feature note **explicitly** says further implementation cannot proceed without that playtest result (e.g. “blocked on playtest feedback before X”). Vague “should playtest” / feel / smoke after a slice → **defer**, do not stop.

When an implementer surfaces a new playtest need: dual-write (Workflow §13), mark it **deferred playtest** for the run, refresh Current focus past it if other agent items remain, and continue. Do **not** invent a hard gate to “be safe.”

## Loop *(parent conducts)*

Repeat until a **stop condition**:

1. **Survey** — in-scope TODOs: Current focus, open items in agreed tiers, Human-TODO blockers, Understanding status.
2. **Partition** — pick the next ready unit(s):
   - **Parallel** only across different stems with no shared hot-file / same `_shared/` foundation overlap
   - **Serial** for the same stem, same shared component, or overlapping files
   - Prefer shared foundation before blocked consumers; optimize build path when budget is loose
3. **Dispatch implementer(s)** — for each unit, spawn/delegate `feature-implementer` if installed, else follow [`feature-implementer.md`](feature-implementer.md) in a leaf Task/child **or** (if the harness cannot spawn) run that worker playbook to completion for one unit before the next. Self-contained brief: stem name, TODO path, exact checklist item / Current focus text, Understanding + spec paths, “implement this unit only; update that TODO; stop when the unit is done or blocked.”
4. **Always verify** — after each implementer finishes a unit (or after a coherent parallel batch), spawn/delegate `work-verifier` if installed, else follow [`work-verifier.md`](work-verifier.md). Brief: stem paths, which TODO item was claimed done, what changed. **Do not** mark the TODO done or commit until verify **passes**.
5. **On verify fail** — one fix pass (re-dispatch implementer with the fail notes), then verify again. **Second fail on the same item** → stop that item; record failure cause; continue other ready work if any.
6. **Bookkeep** — on verify pass: ensure `[x]` + date and Current focus refresh on that TODO (implementer should have done this; fix if missing). Dual-write Human-TODO if a human gate appeared (Workflow §13). New `playtest` rows → **defer** (continue) unless they meet the hard-gate test above.
7. **Milestone git** *(if commits granted)* — parent commits the verify-clean unit (code + that stem’s doc/TODO updates that belong to the unit). Implementer/verifier leaves **do not** commit. Then continue the loop.
8. **Push** — only if granted in the pre-run policy; otherwise never push. Do not ask mid-run.

**Current focus** is the in-loop “what to do next” pointer — refresh it as units complete. It is **not** a reason to stop and wait for the user. Skipping past deferred playtest to the next agent item is correct.

## Git policy *(execute; never pause to ask)*

| Pre-run choice | During the run |
|----------------|----------------|
| Milestone commits *(default)* | After verify **pass** for a unit → commit → continue |
| No commits | Loop only; report dirty/uncommitted tree at end |
| Push when done / after milestones | Only if granted up front; then push without re-asking |

- No secrets in commits; no amend unless the session’s normal amend safety rules allow it
- Prefer one milestone commit per verify-clean unit (or clean parallel batch), not one mega-commit at the end
- Invoking this role with default/loose git is an **implicit grant to milestone-commit for this run only** — it does **not** authorize auto-commit outside orchestration (template sync and other playbooks keep their own ask-first rules)

## Stop when *(any)*

- In-scope **agent-completable** items in the agreed tiers are **cleared** (deferred playtest / end-batch human feel may still be open — that is success, not a mid-loop block), or
- No ready **agent** work remains (only hard gates, draft Understanding, shared maturity, or deferred playtest left), or
- User-set budget/cap hit, or
- Verify failed twice on an item and no other ready work remains, or
- User said stay here / skip subagents / cancel orchestration

**Do not** stop solely because Human-TODO has open `playtest` rows. Finish agent work first; then run **end-of-run human verify map** (below) and the report.

## End-of-run — human verify map *(required when this run cleared agent work)*

After the loop stops, if **any** in-scope unit was implementer-done + work-verifier **pass** this run → dual-write a **guided verify list** so the user can walk what is new, question placement/copy/flow, and send adjustments (Workflow §13). Work-verifier checks “matches the docs”; this map is for **human product judgment** the agent cannot close (“why is that button there?”, “we need that control here”).

**Skip** this section only when the run cleared nothing (cancelled early, only hard-blocked, or no verify-pass units).

### What to put on the list *(guided, not vague)*

Build from **what this run actually changed** (TODO items cleared, files/surfaces touched). Prefer concrete look/try bullets over “smoke test the feature.”

For **each stem** with verify-pass work this run, owner-TODO bullets should cover, when applicable:

| Cue | Ask the human to… |
|-----|--------------------|
| **Surfaces** | Open each new/changed screen, route, panel, or flow the run touched (name them) |
| **Placement** | Notice controls, CTAs, nav, empty states — does each sit where they’d put it? |
| **Copy / hierarchy** | Skim labels and prominence — anything wrong or overpowering? |
| **Happy path** | Do the main action once end-to-end |
| **Rough edges** | Note feel bugs, missing affordances, “should be over there” |

Omit rows that do not apply (e.g. pure backend stem → path + outcome check, not UI placement). **Do not** invent a tour of the whole app — only what this orchestration shipped.

### Dual-write

1. **Owner TODO** — add (or refresh) one High/Medium item titled like **Human verify (orchestration YYYY-MM-DD)** with the guided bullets above + “Reply in chat: what felt wrong / where it should move / copy fixes.”
2. **Human-TODO Open** — thin `- [ ]` row, kind **`playtest`**, Owner → that owner TODO item, Blocks → stem name. Title like **Walk [Stem] — review what landed**. Notes: short pointer (“see owner TODO for the look-list”).
3. **Dedup** — if an Open `playtest` for the same stem already covers this pass, **update** notes / owner bullets instead of duplicating.
4. Fold deferred mid-run playtest rows for those stems into this map so the user gets **one guided pass**, not a scatter.

Prompt in the end-of-run report: open **Human-TODO**, walk the owner look-lists, then reply (e.g. *Checked [Stem] — move Save under …* / *Adjust: …*). Do **not** mark these done yourself.

If milestone commits are on and these doc dual-writes dirty the tree after the last code commit → one small **docs: human verify map** commit (no push unless granted).

## End-of-run report *(required)*

- **Cleared** — stems / items done  
- **Still open** — remaining in-scope agent items  
- **Human verify map** — Human-TODO Open rows + owner look-lists (surfaces to open); invite placement/copy/flow corrections in chat  
- **Other deferred human** — any `decide` / leftover playtest not folded into the verify map  
- **Hard-blocked** — item → reason (`procure` / `waiting` / explicit playtest-gated follow-on / draft Understanding / shared maturity)  
- **Verify failures** — item → what failed and why (if determinable)  
- **Git** — commits made (subjects/hashes) · push status (`not pushed` / `pushed` / `skipped — no commits`)  
- **Next** — one line (usually: walk the Human-TODO verify look-lists)

## Do not

- Spawn this role as a subagent; nest orchestrators; assume workers can spawn workers
- Stop after one Current focus item and wait for “next” while ready work and budget remain
- Stop the loop for ordinary `playtest` / feel / smoke — defer and batch at end unless a TODO **explicitly** hard-gates follow-on work
- Skip the end-of-run human verify map when this run cleared verify-pass work
- Duplicate Open playtest rows for the same stem/pass — update notes instead
- Ask mid-loop about commits, push, priority tier, playtest now-vs-later, or whether to continue
- Skip work-verifier
- Mark TODO items done when work-verifier failed
- Mark human `playtest` / `decide` done without user confirmation
- Push unless the pre-run policy granted it
- Invent `_shared/` components, new Document Map rows, or product backlog items unrelated to shipped work / dual-write rules
- Drain Low/Future when the user chose High-only (or High+Medium)
- Upgrade a single-slice implement ask into full orchestration
- Re-open Understanding review when status is `confirmed` and scope unchanged
- Auto-commit because “orchestration sometimes commits” when the user is on template sync or a non-orchestrate ask
- Store secrets in docs or commit messages
