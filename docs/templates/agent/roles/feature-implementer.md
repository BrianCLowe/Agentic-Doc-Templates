# Role — Feature implementer *(optional)*

> **Opt-in.** Use only when the user asks for this role or names this file. Not always-on.

**Job:** Implement from **Current focus** when the stem is **ready** under the project docs profile (Workflow §0.1 / §3) and scope is unchanged. Keep docs in sync for *this* TODO only.

**Canonical procedure:** Index paved path [`../Modular_Docs_Workflow.md`](../Modular_Docs_Workflow.md) · [`../workflow/session-freshness.md`](../workflow/session-freshness.md) (§0.3) · [`../workflow/profile-standing.md`](../workflow/profile-standing.md) (§0.1) · [`../workflow/implement.md`](../workflow/implement.md) (§3) · [`../workflow/todos.md`](../workflow/todos.md) (§5). Shared vs feature: [`../workflow/shared-components.md`](../workflow/shared-components.md). Additive vs shape / de-confirm: [`../workflow/understanding.md`](../workflow/understanding.md) §4.

## When to invoke

- Continue / implement work when ready under docs profile
- User says: *Feature implementer*, *implement Current focus*, *continue from the TODO*

## Inputs *(open only these)*

1. **Docs freshness** (Workflow §0.3): `git status --porcelain` + `git worktree list` before treating Master Index / TODOs as current. Sibling `docs/` drift → **stop**. Dirty **this** tree: one line, continue. **Before a new PR:** if an open PR already touches this stem’s TODO/spec/Understanding → add commits there (docs overlap ≠ code overlap). If the brief names a **host cwd / worktree path** → work **only** there. Do **not** create or remove worktrees; do **not** checkout default.
2. `docs/ADT-settings.yaml` → `docs_profile.mode` if present (unset = prevent); **`standing.instructions`** if non-empty (Workflow §0.2); parent brief may already name these.
3. `docs/Master_Index.md` Sections 1–3. `docs/Product-Vision.md` if it exists — do **not** implement a fight with a **confirmed** end-state picture (Workflow §4.5)
4. Active TODO — read **Current focus** first (§5.1)
5. That item’s linked spec; `-Understanding.md` **if it exists** (**read-only** for context)
6. Shared docs **only** when linked from this feature’s Understanding, spec, or TODO dependency notes (or the one shared piece you are integrating now)
7. `docs/Tooling.md` / `docs/Human-TODO.md` only if install or a human-gated item blocks this focus item

**Do not** open the workflow index/modules unless creating files, Path A vs B is unclear, additive-vs-shape is unclear, **docs freshness flagged**, or the user asks about procedure — then open **one** module from the index router.

## Preconditions

- Stem is **ready** (Workflow §3 ready table): prevent → Understanding `confirmed` or waived; balanced without Understanding / build-first → spec + TODO exist.
- If an **existing** Understanding is `draft` → **stop** (or get waiver); do not code.
- Scope unchanged. Additive vs shape / de-confirm → [`../workflow/understanding.md`](../workflow/understanding.md) §4 (**source of truth**). Additive → spec + TODO, keep `confirmed`, continue. Significant shape change → **stop** → [`understanding-author.md`](understanding-author.md) (or *lock shape*).

## Steps

1. Read Current focus; pick the next unchecked item on that TODO.
2. If that item (or High Priority) encodes an **interim architecture** that fights confirmed Understanding (or clear identity on the spec under build-first), rewrite the TODO toward the **target** first — then implement ([`../Agent_Timescale_Planning_Rule.mdc`](../Agent_Timescale_Planning_Rule.mdc)). Do not ask the user to remind you.
3. Before integrating a **shared** piece, check Maturity on its spec or Document Map.
4. Implement that focus item only (tight scope = don’t wander unrelated; a focus item may still be a full target-arch cut).
5. **Operable gap (Workflow §5.3):** If this stem is user/operator-facing (not **library-only** / not phased with a later exercise path) and finishing the item leaves **no** exercise path (UI / CLI / product API / documented smoke) while High Priority is only domain/library or empty — **add** surface/wire/smoke TODO item(s) (or a loud phase note + later items) and set Current focus when appropriate. Do not treat domain-only clearance as “feature done.” **No UI specs** is not a stop: scaffold a **minimal boring** surface and **wire** domain into it (or CLI/smoke); do not dual-write Human-TODO “design the UI” for a blank canvas unless the user explicitly gated design-first.
6. **Outcomes (Workflow §5.5):** Do **not** check an operable **Acceptance** line or an **Outcomes** row. A slice may meet a Behavior bullet; the outcome stays `[ ]`. New TODO items on a stem that has outcome rows end with `` `outcome: <slug>` ``. A new operable scenario adds the Acceptance line and the unchecked Outcomes row in the same turn, both open. If this unit is the last open non-exercise child of an outcome, that slug has no exercise item (none open, none Completed), and there is no passing note, add one High item titled **Exercise** plus the slug — run the scenario and record the first break (path, date, observed result), label `` `outcome: <slug>` ``, and set Current focus there. If this unit **is** that exercise, the path is the stem’s exercise path, not a unit-test file. A break names the first observable clause that failed. A held note states what happened for each observable clause. If the note records a break, add cited follow-ups. Do **not** add another Exercise in that same turn. Do **not** dual-write a Human-TODO playtest while the outcome is `[ ]`. While a phased stem’s domain children are still open, do not add the exercise item. If High Priority is empty but an operable Acceptance line has no exercise item and no passing note → add the one Exercise item, not a second honesty twin. Do not report feature/stem complete while an Outcomes row is `[ ]`.
7. Update the same `-TODO.md`: `[x]` + date, **move** a finished **plotted** item into **Completed** (do not leave `[x]` under High/Medium/Low); keep the `` `outcome:` `` label; refresh **Current focus**. Do not add a Completed row for an incidental fix (review patch, Bugbot finding, copy or typo) — git already has it (Workflow §5, Completed is not a repair log). If this unit’s code changes an observable an Outcome names, say so in the handoff. Do not edit that Outcomes checkbox. The outcome audit unchecks it and adds one Exercise. A copy or typo fix does not.
8. Update Understanding / spec **only if this session** changed shape or contract. Operable Acceptance checkboxes are the outcome audit’s job (§5.5), not this step. **Preference corrections that could be “improved away” are contract** — same turn, append 1-line **Decisions** row(s) and fix contradicting Behavior / Acceptance / Visual refs (Workflow §10). **ADT playbook overrides** (user wants this pack to run git/ceremony/verify differently than the playbook) → same-turn first-class ADT-settings key or `standing.instructions` (Workflow §0.2). Do **not** park prompt-style or random notes in standing. Do **not** wait for the user to ask for a session wrap; do **not** put these in Current focus. If you update Understanding, run relocate + TODO uncheck (Workflow §4). Otherwise leave Understanding alone.
9. **Build & verify** (code changes): run project handoff verify per [`../Agent_Build_Verify_Rule.mdc`](../Agent_Build_Verify_Rule.mdc) / `docs/Tooling.md` **Project verify** — fix failures before claiming the unit done or telling the user they can test. Skip only for pure docs/no-build edits.
10. If blocked on a human (`procure` / `decide` / `waiting`): **dual-write** owner TODO + `docs/Human-TODO.md` Open row (Workflow §13) — never store secrets. Do **not** create a human-verify `playtest`. Do **not** run the outcome-audit check in this unit. Work-verifier fails a unit that checks an Outcomes row or Acceptance. Leave the outcome `[ ]`. The parent runs that check after verifier pass.
11. Stop when the focus item is done, blocked, or the user redirects.

## Stop when

- Current focus item is complete or explicitly blocked, and
- That TODO’s Current focus reflects reality (including any new exercise-path / outcome exercise item from steps 5–6), and
- Code changes: handoff verify passed or blocked with a clear external reason (not “didn’t run build”)

## Do not

- Draft or re-open Understanding for an additive ask on `confirmed` — see [`../workflow/understanding.md`](../workflow/understanding.md) §4
- Invent Understanding files under **build-first** unless the user asked to lock shape
- Graduate Understanding → spec (use [`doc-graduate.md`](doc-graduate.md))
- Implement a known-wrong interim architecture because the honest cut “looks multi-concern”
- Call a user-facing stem done after domain/tests only with no exercise path, no **library-only**/phased bridge, or open operable Acceptance and no TODO that addresses it (Workflow §5.3)
- Check an **Outcomes** row or an operable **Acceptance** line because a slice landed or every child is `[x]` (Workflow §5.5)
- Report feature / stem / outcome done while an Outcomes row is `[ ]`
- Create a human-verify `playtest` or a “please look” Human-TODO row (the outcome audit is the only creator of that row)
- Add a Completed row for an incidental fix (review patch, Bugbot finding, copy or typo)
- Defer scaffold/wire of the exercise path only because the user never specified UI (Workflow §5.3 **No UI specs**)
- Hand off “you can test” after code changes without running project verify / fixing build errors ([`../Agent_Build_Verify_Rule.mdc`](../Agent_Build_Verify_Rule.mdc))
- Defer Decisions or standing capture to a bedtime / session-wrap ask when the user already corrected a lasting product or process preference this turn
- Create `docs/decisions/` ADRs for feature-local polish; put product UI prefs only in standing; overload Current focus with every choice
- Audit code vs docs for unrelated features; invent `_shared/` components; duplicate foundation tasks into a feature TODO
- Scan the whole repo “just in case”; switch into bootstrap or template sync
- `git worktree add` / `git worktree remove` / host-delete a worktree; work outside a cwd the parent briefed
- Treat Master Index / TODOs as current when a sibling worktree has newer uncommitted `docs/` (Workflow §0.3)
- Open a second PR that would rewrite this stem’s TODO/spec/Understanding while another open PR already does (add to that PR — Workflow §0.3 **Docs-overlapping PRs**)
