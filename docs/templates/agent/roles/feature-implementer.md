# Role — Feature implementer *(optional)*

> **Opt-in.** Use only when the user asks for this role or names this file. Not always-on.

**Job:** Implement from **Current focus** when the stem is **ready** under the project docs profile (Workflow §0.1 / §3) and scope is unchanged. Keep docs in sync for *this* TODO only.

**Canonical procedure:** Index paved path [`../Modular_Docs_Workflow.md`](../Modular_Docs_Workflow.md) · [`../workflow/profile-standing.md`](../workflow/profile-standing.md) (§0.1) · [`../workflow/implement.md`](../workflow/implement.md) (§3) · [`../workflow/todos.md`](../workflow/todos.md) (§5). Shared vs feature: [`../workflow/shared-components.md`](../workflow/shared-components.md). Additive vs shape / de-confirm: [`../workflow/understanding.md`](../workflow/understanding.md) §4.

## When to invoke

- Continue / implement work when ready under docs profile
- User says: *Feature implementer*, *implement Current focus*, *continue from the TODO*

## Inputs *(open only these)*

1. `docs/ADT-settings.yaml` → `docs_profile.mode` if present (unset = prevent); **`standing.instructions`** if non-empty (Workflow §0.2); parent brief may already name these
2. `docs/Master_Index.md` Sections 1–3
3. Active TODO — read **Current focus** first (§5.1)
4. That item’s linked spec; `-Understanding.md` **if it exists** (**read-only** for context)
5. Shared docs **only** when linked from this feature’s Understanding, spec, or TODO dependency notes (or the one shared piece you are integrating now)
6. `docs/Tooling.md` / `docs/Human-TODO.md` only if install or a human-gated item blocks this focus item

**Do not** open the workflow index/modules unless creating files, Path A vs B is unclear, additive-vs-shape is unclear, or the user asks about procedure — then open **one** module from the index router.

## Preconditions

- Stem is **ready** (Workflow §3 ready table): prevent → Understanding `confirmed` or waived; balanced without Understanding / ship-first → spec + TODO exist.
- If an **existing** Understanding is `draft` → **stop** (or get waiver); do not code.
- Scope unchanged. Additive vs shape / de-confirm → [`../workflow/understanding.md`](../workflow/understanding.md) §4 (**source of truth**). Additive → spec + TODO, keep `confirmed`, continue. Significant shape change → **stop** → [`understanding-author.md`](understanding-author.md) (or *lock shape*).

## Steps

1. Read Current focus; pick the next unchecked item on that TODO.
2. If that item (or High Priority) encodes an **interim architecture** that fights confirmed Understanding (or clear identity on the spec under ship-first), rewrite the TODO toward the **target** first — then implement ([`../Agent_Timescale_Planning_Rule.mdc`](../Agent_Timescale_Planning_Rule.mdc)). Do not ask the user to remind you.
3. Before integrating a **shared** piece, check Maturity on its spec or Document Map.
4. Implement that focus item only (tight scope = don’t wander unrelated; a focus item may still be a full target-arch cut).
5. **Operable gap (Workflow §5.3):** If this stem is user/operator-facing (not **library-only** / not phased with a later exercise path) and finishing the item leaves **no** exercise path (UI / CLI / product API / documented smoke) while High Priority is only domain/library or empty — **add** surface/wire/smoke TODO item(s) (or a loud phase note + later items) and set Current focus when appropriate. Do not treat domain-only clearance as “feature done.” **No UI specs** is not a stop: scaffold a **minimal boring** surface and **wire** domain into it (or CLI/smoke); do not dual-write Human-TODO “design the UI” for a blank canvas unless the user explicitly gated design-first.
6. **Acceptance bridge:** If this unit clearly meets a coarse **Acceptance** outcome on the spec → check/update that line the same turn. If High Priority is now empty/domain-cleared but operable Acceptance lines for a claimed milestone remain open with no open TODO → **add** work items that close them (or phase); do not report feature/stem complete.
7. Update the same `-TODO.md`: `[x]` + date, **move** finished items into **Completed** (do not leave `[x]` under High/Medium/Low); refresh **Current focus**.
8. Update Understanding / spec **only if this session** changed shape or contract (Acceptance updates from step 6 count). **Preference corrections that could be “improved away” are contract** — same turn, append 1-line **Decisions** row(s) and fix contradicting Behavior / Acceptance / Visual refs (Workflow §10). **Pack/process prefs that oppose pack defaults** (always/never git, ceremony, verify style) → same-turn first-class ADT-settings key or `standing.instructions` (Workflow §0.2). Do **not** wait for the user to ask for a session wrap; do **not** put these in Current focus. If you update Understanding, run relocate + TODO uncheck (Workflow §4). Otherwise leave Understanding alone.
9. **Build & verify** (code changes): run project handoff verify per [`../Agent_Build_Verify_Rule.mdc`](../Agent_Build_Verify_Rule.mdc) / `docs/Tooling.md` **Project verify** — fix failures before claiming the unit done or telling the user they can test. Skip only for pure docs/no-build edits.
10. If blocked on a human (procure / playtest / decide / waiting): **dual-write** owner TODO + `docs/Human-TODO.md` Open row (Workflow §13) — never store secrets.
11. Stop when the focus item is done, blocked, or the user redirects.

## Stop when

- Current focus item is complete or explicitly blocked, and
- That TODO’s Current focus reflects reality (including any new exercise-path / Acceptance-bridge items from steps 5–6), and
- Code changes: handoff verify passed or blocked with a clear external reason (not “didn’t run build”)

## Do not

- Draft or re-open Understanding for an additive ask on `confirmed` — see [`../workflow/understanding.md`](../workflow/understanding.md) §4
- Invent Understanding files under **ship-first** unless the user asked to lock shape
- Graduate Understanding → spec (use [`doc-graduate.md`](doc-graduate.md))
- Implement a known-wrong interim architecture because the honest cut “looks multi-concern”
- Call a user-facing stem done after domain/tests only with no exercise path, no **library-only**/phased bridge, or open operable Acceptance and no TODO that addresses it (Workflow §5.3)
- Defer scaffold/wire of the exercise path only because the user never specified UI (Workflow §5.3 **No UI specs**)
- Hand off “you can test” after code changes without running project verify / fixing build errors ([`../Agent_Build_Verify_Rule.mdc`](../Agent_Build_Verify_Rule.mdc))
- Defer Decisions or standing capture to a bedtime / session-wrap ask when the user already corrected a lasting product or process preference this turn
- Create `docs/decisions/` ADRs for feature-local polish; put product UI prefs only in standing; overload Current focus with every choice
- Audit code vs docs for unrelated features; invent `_shared/` components; duplicate foundation tasks into a feature TODO
- Scan the whole repo “just in case”; switch into bootstrap or template sync
