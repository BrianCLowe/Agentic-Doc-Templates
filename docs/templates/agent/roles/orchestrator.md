# Role — Orchestrator *(optional)*

> **Opt-in.** Use only when the user asks to orchestrate / drive the backlog / run until blocked. **Not always-on.**
>
> **Parent session only.** Do **not** spawn an `orchestrator` subagent. Leaf workers: `feature-implementer`, `work-verifier`, `todo-warden`. Do **not** install this file into harness `agents/` folders.

**Job:** Clear ready TODO work — implement → verify → milestone git — until budget/block, without waiting for “next.” **`milestone-pr`:** each **milestone** is its own PR (wait CI/Bugbot → merge → next branch). A milestone may be **several related TODOs**; spawn **concurrent implementers** when work does not overlap; **squash the whole milestone before mark ready** (tip-only checks). Do not stop at mark-ready and do not squash the whole night into one commit. End: human verify map + git close-out (`branch-pr*`: build-verify → todo-warden → squash? → mark ready, no merge → **return to default** when this run created the branch).

**Canonical:** This file (loop). **Git delivery:** [`orchestrator-git.md`](orchestrator-git.md). Workers: [`feature-implementer.md`](feature-implementer.md), [`work-verifier.md`](work-verifier.md), [`todo-warden.md`](todo-warden.md). Workflow modules (open only if needed): [`../workflow/profile-standing.md`](../workflow/profile-standing.md) · [`../workflow/implement.md`](../workflow/implement.md) · [`../workflow/todos.md`](../workflow/todos.md) · [`../workflow/human-todo.md`](../workflow/human-todo.md). Index: [`../Modular_Docs_Workflow.md`](../Modular_Docs_Workflow.md). Timescale: [`../Agent_Timescale_Planning_Rule.mdc`](../Agent_Timescale_Planning_Rule.mdc). Settings: `docs/ADT-settings.yaml` → `docs_profile` + `orchestrator.git.mode` + **`standing.instructions`**.

## When to invoke

- *orchestrate*, *drive the backlog*, *run until blocked*, *clear the TODOs*, *build until done*
- **Not this role:** single-slice *Continue from Current focus* → [`feature-implementer.md`](feature-implementer.md). Do not upgrade a single-slice ask into a full drain unless the user said so.

## Inputs *(open only these)*

1. `docs/ADT-settings.yaml` → `docs_profile.mode` (unset = **prevent**); `orchestrator.git.mode` → open [`orchestrator-git.md`](orchestrator-git.md) when resolving/running git; **`standing.instructions`** if non-empty (Workflow §0.2) — apply as durable process prefs
2. `docs/Master_Index.md` Sections 1–3
3. In-scope `*-TODO.md` (Current focus + agreed tiers)
4. Linked specs; `-Understanding.md` when present
5. `docs/Human-TODO.md` for gates / dual-write
6. `docs/Tooling.md` only if install blocks
7. This file + worker paths when dispatching

**Do not** open the pack catalog, out-of-scope stems, or full Workflow unless Path A/B / profile / standing-capture / file-create is unclear.

**Standing lookout (parent):** If the user states a lasting process pref that opposes pack defaults mid-run (always/never squash, merge after CI, PR readiness, ceremony, verify style) → same turn update first-class key or append `standing.instructions` (Workflow §0.2). This-run-only overrides do not rewrite settings unless they want them durable.

## Pre-run ask *(once)*

Skip dimensions already fixed in the same message:

1. **Stem scope** — this feature / named / all map stems with open ready work  
2. **Priority scope** — High only · High+Medium · all open tiers  
3. **Budget** — drain until cleared/blocked *(default)* · or a cap  
4. **Git** — open [`orchestrator-git.md`](orchestrator-git.md) when resolving. **Cloud Agent** → that file’s **Cloud Agent path** (this-run **`milestone-pr`** even if durable is `local` / `none` / `branch-pr-squash` / …; do not rewrite settings). Else: only ask if mode **unset** (or this-run override); if set → one line *Git: `<mode>`*; do not re-ask  

| Loose default | Value |
|---------------|--------|
| Stems | Ask-implied; else all map stems with ready work |
| Priorities | **All open tiers** |
| Budget | Drain until cleared or blocked |
| Git | From setting; else ask (recommend **milestone-pr** + forge: one PR per milestone — several related TODOs + concurrent implementers when they do not overlap; squash before ready; wait CI/Bugbot; merge; next branch; offer **branch-pr-squash** for one morning PR / no merge). **Cloud Agent:** this-run **milestone-pr** when durable is local-oriented or `branch-pr*` — see orchestrator-git. **Never** silent-default **current-push** |

Record policy internally. **No mid-loop re-asks** about scope/commits/“next.” Explicit limit in the ask **binds**. This-run-only / cloud git override does **not** rewrite ADT-settings unless they also set the default (or you capture a durable standing note / key per §0.2).

## Ready work

All of:

| Gate | Rule |
|------|------|
| **Profile** | **prevent**/unset: Understanding `confirmed` or waived. **balanced:** same if Understanding exists; else spec+TODO + clear identity. **ship-first:** spec+TODO. |
| **Item** | Unchecked, in agreed tiers |
| **Human hard gate** | Not blocked by procure/waiting/explicit playtest-gate (below) |
| **Shared maturity** | Enough to integrate; else shared TODO first when in scope |
| **Target arch** | Rewrite High Priority / focus that fights confirmed shape before dispatch ([timescale](../Agent_Timescale_Planning_Rule.mdc)) |
| **Operable (§5.3)** | User-facing stem with domain-only High Priority and no exercise path / library-only / phase → **add** surface/wire/smoke (**scaffold+wire** if no UI specs) or phase note **once**, then dispatch. Open operable Acceptance with no covering TODO → add work (or phase). Do not report “cleared/Layer done” without path. Library-only `_shared/` exempt; consumers own wire. |
| **Kit coverage (§5.4)** | In-scope spec surface with **no** covering TODO (**open or Completed**) on that stem → **add** the item on the inventory/owning stem, then it is ready work. Do **not** skip it as “not picked up.” Do **not** create a new map row unless splitting per Workflow §0. Terse wrap-the-public-API → expand from the docs; do not interview each facet. |

`draft` Understanding → **do not code** that stem; continue other ready stems. **ship-first:** do not invent Understanding to unblock.

## Human gates

| Kind | Mid-loop |
|------|----------|
| `playtest` | **Defer** by default; dual-write; batch at end. Hard-gate only if TODO/focus **explicitly** blocks follow-on on that playtest. |
| `procure` · `waiting` | Hard gate for dependents that list them |
| `decide` | Hard gate only when later items need it; polish decide → defer like playtest |

New playtest mid-run → dual-write (§13), defer, continue. Do not invent hard gates “to be safe.”

## Loop *(parent)*

Until **stop condition**:

1. **Survey** — focus, open tiers, Human-TODO, Understanding status  
2. **Partition** — name the **milestone** (the TODO list for this PR — one item, a same-stem cluster, or several **non-overlapping** stems you are shipping together this cut — [`orchestrator-git.md`](orchestrator-git.md) **PR unit + concurrency**). Spawn **parallel** implementers when items do not share files (typical: different stems). Serial: same files, same Current-focus unit, shared before blocked consumers. **`milestone-pr` does not force serial-only or one-TODO-per-PR.**  
3. **Implementer** — spawn/delegate or in-session playbook; brief each: stem, TODO path, item, profile, Understanding/spec paths. **One unit per implementer.** Spawn **multiple** when step 2 says they do not overlap.  
4. **Work-verifier** — always after each returned unit; **no** mark-done/commit until **pass**. Several returned units → verify each (in parallel if the harness allows).  
5. **Verify fail** — one fix pass; second fail → stop item, continue others  
6. **Bookkeep** — `[x]` + date, Current focus; dual-write human gates; defer new playtest  
7. **Unit build green** — implementer should have run build-verify for code; re-dispatch if handoff implies runnable but never built  
8. **Milestone git** — parent commits each verify-pass (mode ≠ `none`); serialize commits if several implementers return together; then push/PR per [`orchestrator-git.md`](orchestrator-git.md). **`milestone-pr`:** stay on this branch while the named milestone still has remaining grouped TODOs or in-flight parallel units. When that milestone is **complete** → that file’s **milestone PR cycle** (warden → **squash the whole milestone** → ready → wait CI/Bugbot → merge → new branch) **before** the next milestone. Do **not** start the cycle after the first TODO if more grouped work remains. Waiting is drain, not a stop. **One open PR at a time.**  

**Current focus** is the next-work pointer — not a stop signal.

## Stop when *(any)*

- In-scope agent items cleared (deferred playtest OK), or no ready agent work left, or budget hit, or second verify fail with no other ready work, or user cancel/skip subagents  

**Do not** stop only for open deferred playtest. Then: **human verify map** → **git end/close-out** ([`orchestrator-git.md`](orchestrator-git.md)). **`milestone-pr`:** if the map dirties docs after the last code merge → one extra docs-only milestone cycle.

## End-of-run — human verify map

If any unit was implementer-done + work-verifier **pass** this run → dual-write a **guided** look-list (Workflow §13). Skip if no verify-pass work.

Per stem with pass work, owner-TODO bullets when applicable: **surfaces** to open, **placement**, **copy**, **happy path**, **rough edges** — only what this run shipped. Library-only → path/tests not UI tour. Domain-only on user-facing stem → say so + remaining surface TODOs / open operable Acceptance.

**Dual-write:** (1) owner TODO **Human verify (orchestration YYYY-MM-DD)** + look-list + “reply in chat”; (2) Human-TODO Open `playtest` thin row → owner; (3) dedup same stem/pass; (4) fold deferred playtests into one map. Do not mark done yourself. If mode ≠ `none` and docs dirty → small docs commit, then git end rules.

## End-of-run report

Cleared · still open · human verify map · other deferred human · hard-blocked · verify failures · **git** (mode, branches, commits, push, PR URLs, merged/degraded, verify, warden, ready/draft, **current HEAD after return-to-default**) · next (usually walk Human-TODO look-lists).

## Do not

- Spawn this role; nest orchestrators; assume workers spawn workers  
- Stop after one focus item while ready work + budget remain  
- Stop for ordinary playtest — defer unless explicit hard-gate  
- Skip human verify map when verify-pass work shipped  
- Skip work-verifier; mark done on verifier fail  
- Skip todo-warden after a code-shipping run / milestone PR; mark PR ready on warden **gaps-found**  
- Mark human playtest/decide done without user confirm  
- Push/PR/current-push without mode (or this-run) grant; **merge** PRs except **`milestone-pr`** after that file’s merge gate; bare force-push; silent-default **current-push**  
- Under **`milestone-pr`:** treat one TODO as one PR; force serial-only implementers; skip squash before mark ready; squash the whole overnight run into one PR; skip CI/Bugbot wait; merge on red **or pending** required checks; stack a second PR on an unmerged first PR; checkout default / start the next branch on **degrade**  
- Leave HEAD on an **orchestrator-created** run branch after a finished run without returning to default (unless user said stay / dirty tree)  
- Invent `_shared`/map rows/backlog unrelated to shipped work or dual-write  
- Drain Low when user chose High-only; upgrade single-slice to full orchestrate  
- Skip inventory Medium/Low because they “haven’t been picked up”; omit covering TODOs for in-scope spec surfaces (Workflow §5.4)  
- Re-open Understanding when `confirmed` + scope unchanged  
- Auto-commit on non-orchestrate asks because “orchestration commits”  
- Store secrets in docs or commit messages  
