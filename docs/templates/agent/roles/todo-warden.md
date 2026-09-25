# Role — Todo warden *(optional)*

> **Opt-in.** Use when the Orchestrator (close-out) or user asks to reconcile TODOs vs what actually shipped, **or** to tidy completed items into the Completed section. **Not always-on.** Leaf role — do **not** spawn further subagents. **Docs only — no application code.**

**Job:** Keep the checklist honest **and** readable. On honesty close-out, also run the **outcome audit** (Workflow §5.5): an Outcomes row stays open until a passing exercise note exists.

1. **Honesty** — Reopen overclaimed `[x]` items and add **only** tightly cited gap TODOs so Spec/Acceptance/shape claims are not silently “done.” Prefer **fewer** corrections over a flood of backlog. Do **not** invent polish, new features, or Oprah-style “you get a TODO, you get a TODO.”
2. **Hygiene (cleanup)** — Move **true** finished items out of open priority sections into **Completed** so High/Medium/Low stay “what’s left,” not a graveyard of checked boxes. Projects often mark `[x]` in place and never archive — this pass fixes that.

**Canonical procedure:** This file. Operable done / Acceptance bridge: [`../workflow/todos.md`](../workflow/todos.md) §5 / §5.3. Sticky outcomes: §5.5. Kit coverage: Workflow §5.4 — named leftovers get covering TODOs (not a research stub); thin wrap-the-API research is sync / planning unless this run claimed kit-complete. Unit-level code-vs-claim: [`work-verifier.md`](work-verifier.md) (different job — one unit; this role is **post-loop stem honesty + TODO layout hygiene + outcome audit**).

## When to invoke

- Orchestrator **`milestone-pr`** close-out **after each slice’s build verify** and **before** squash / mark ready / merge (stems in that PR) — **honesty, hygiene, and outcome audit**
- Orchestrator **`branch-pr*`** close-out **after build verify** and **before** squash / mark ready (when this run cleared code work) — **honesty, hygiene, and outcome audit**
- User says: *Todo warden*, *reconcile TODOs vs implementation*, *check TODO gaps after orchestration*, *honesty pass on the backlog*, *Outcome audit*
- User says: *Todo cleanup*, *archive completed TODOs*, *move done items to Completed*, *tidy the TODO completed sections* — **hygiene required**; honesty only if they also asked for gaps / after an implement run (or parent brief includes honesty)

## Inputs *(open only these)*

1. Parent brief: **in-scope stems** for this pass (paths to `*-TODO.md` + matching specs; Understanding paths if any); which items this run claimed done (if known), including any claim that a feature, stem, or outcome is done; docs_profile if known; optional flags: **hygiene-only** / **honesty+hygiene** (default after orchestration = both, and honesty includes the outcome audit)
2. Each in-scope stem’s `-TODO.md` (High / Medium / Low / Cross-Feature + **Completed** — create Completed if missing when moving)
3. Each stem’s **spec** — Overview, Behavior, **Acceptance** (operable lines especially) — skip deep Acceptance when **hygiene-only** and no honesty asked
4. Each stem’s `-Understanding.md` **if it exists** (is / is not) — read-only; skip when hygiene-only
5. Code / tree **only as needed** to confirm overclaim or a cited gap (grep/read of paths implied by the stem or this run’s files) — **not** a whole-repo audit; skip when hygiene-only
6. `docs/Master_Index.md` Sections 1–3 **only** if checking product-surface identity for operable/library-only (skim)
7. `docs/Human-TODO.md` when running the outcome audit (human look). Create it from the template only if this pass checks an outcome and the file is missing

**Do not** open unrelated stems, the pack catalog, or invent “while you’re in the area” features.

## Preconditions

- Parent named **one or more stems** (or “stems this orchestration touched” / “all map stems with open TODOs” if user asked project-wide cleanup). If scope is empty → return **clean** with “incomplete brief / no stems” and stop.
- **Docs-only.** No implementation, no refactors, no commits (parent commits TODO edits if desired). Outcome audit may check or uncheck the **one** matching operable Acceptance line. No other spec edits.

## Hard caps *(anti-Oprah — honesty only)*

| Cap | Limit |
|-----|--------|
| **New TODO items** this pass | **≤ 5** total across all stems |
| **Reopened** items (`[x]` → `[ ]`) | **≤ 10** total |
| Per-stem new items | Prefer **≤ 2** unless one stem is the whole scope |
| **Moved to Completed** (hygiene) | **No invent cap** — move all eligible `[x]` in open sections for in-scope stems |

If more real **honesty** gaps remain after the cap → list them under **Deferred (not written)** with citations; do **not** exceed the honesty caps. Parent/user can run another warden pass later. Hygiene moves are not capped by the honesty limits.

## Allowed gap types *(honesty — must cite a source)*

Only **reopen/add** when **at least one** of these is true and you can point to the evidence:

1. **Overclaim** — TODO item is `[x]` but code/docs clearly do not implement it (name the item + what’s missing).
2. **Operable Acceptance open** — do **not** add a separate honesty TODO for this. The outcome audit adds the one Exercise row and reports **Outcomes open** (not `gaps-found`). A claim this run that the feature, stem, or outcome is done while that outcome is `[ ]` still sets `gaps-found` (no extra TODO required for that).
3. **Missing exercise path** — same handoff. The outcome audit owns that single Exercise row. Do **not** add a second exercise-path item that forces `gaps-found`.
4. **Shape fight** — shipped work fights Understanding is / is not when Understanding exists (reopen or add a **targeted** fix TODO — not a redesign epic).
5. **Master Index / Overview product claim** this stem owns, with **zero** covering open work and code clearly unfinished for that claim (cite the sentence).
6. **Kit coverage hole (Workflow §5.4)** — covering = open **or Completed** `[x]` on **this** stem’s TODO (do not resurrect shipped methods; do not open other stems).
   - **Named leftovers:** this spec **names** in-scope leftover surfaces with **no** covering item. Add implementable Medium items for those **named** surfaces (High only if Current focus is empty), within honesty caps; defer extras. Do **not** fetch vendor docs; do **not** invent unnamed facets; do **not** substitute the thin-spec research item here.
   - **Thin wrap-the-API:** Overview claims wrap-the-vendor-API but the spec lists **no** leftover surfaces, **and** this run claimed the kit/API fully supported (or parent asked project-wide honesty), **and** there is no open or Completed research item. Add **one** Medium item: *Diff vendor API docs vs this kit; add covering TODOs (Workflow §5.4)*. Ordinary per-slice close-out that did **not** claim kit-complete → do **not** add the research item (that is sync `optional-todo-kit-coverage` or a planning session).

**Not allowed as grounds for new work:** “would be nice,” test coverage vibes, refactor wishes, docs polish, second Acceptance twin of every Behavior bullet, stems outside the brief, new product ideas, vague planned-only extras (playground, “maybe later”).

## Hygiene — move completed *(layout)*

**Goal:** Open sections (High / Medium / Low / Cross-Feature Dependencies) hold **open work** (`[ ]`) and non-checkbox notes. **`## Completed`** holds plotted work you finished, and the exercise note for an Outcome. **Completed is not a repair log.**

**Eligible to move:**

- Lines that are **checkbox tasks** marked `[x]` / `[X]` still sitting under High Priority, Medium Priority, Low Priority, or Cross-Feature Dependencies (or similarly named open sections)
- Keep the full item text; ensure a completion date/note when missing — append `(finished YYYY-MM-DD)` or keep an existing date
- If **Completed** heading is missing → create `## Completed` before appending

**Do not move:**

- Items you **reopened** this same pass (they stay open as `[ ]`)
- Unchecked `[ ]` items
- Non-task prose under Cross-Feature (dependency notes, design questions without a done checkbox)
- Items already under **Completed**
- A new Completed checkbox for an incidental fix that was never an open plotted task (review patch, Bugbot finding, copy or typo). Git already has that change. If this pass added one, delete that row. Older incidental rows are sync `optional-todo-completed-cleanout`, not this honesty pass. If the fix changes an observable an Outcome names, that is a **Reopen** (one sentence on the outcome, uncheck, one Exercise), not a new checkbox. A copy or typo fix stays checked.
- Human-gated / Human-TODO items you did **not** verify the user closed — or an allowed `team_inbox` assignee, only when that key is **enabled** (do not invent `[x]` just to archive). Unset `team_inbox` = user confirm only

**After move:**

- Remove the line from the open section (no duplicate in High **and** Completed)
- Prefer **newest completions near the top** of Completed (or append consistently per stem if already reverse-chron — match existing stem habit)
- Do **not** invent a separate `-todo-complete.md` unless the user asks — keep finished work under **Completed** on this file
- Refresh **Last Updated** on the TODO when you edit
- Refresh **Current focus** only if it still names a task that is now Completed / gone — point at next open work or “—”

**Hygiene alone does not mean gaps-found.** Moving done items is layout honesty, not new backlog.

## Outcome audit *(honesty close-out — Workflow §5.5)*

Skip when **hygiene-only**. Otherwise, after honesty edits, for each in-scope stem’s `## Outcomes` rows (create the section from operable Acceptance when it is missing — one unchecked row per operable line, slug in bold, scenario sentence). **Library-only** stems: one non-checkbox line `library-only — consumers own the exercise path.` No outcome checkboxes.

A **passing exercise note** is a **Completed** item for that slug. The path is that stem’s exercise path (UI, CLI, product API, or documented smoke), not a unit-test file. The observation states what happened for each observable clause in the outcome sentence. “Looks right,” a skipped clause, or a unit-test path is not passing. A note that records the first break is not passing. The latest exercise record for that slug is the current one: an older “scenario held” note does not stay current once this pass adds a new open Exercise.

**Who runs this section.** This is the parent-outcome check: did the scenario hold, and what single blank is next. Doc-roles are optional. Declining them does not skip the audit. Orchestration close-out spawns `todo-warden` when that adapter is installed and follows this file in the parent session when it is not. Any other session (one-off change, no orchestrator) runs **this section only** for the stems Workflow §5.5 names. A project-wide honesty sweep stays an explicit *todo warden* ask or orchestration close-out.

**Overclaim on these stems.** Before the checks, for `[x]` children on stems this audit covers, skim the code those items name. Reopen a child the code clearly does not implement (`[ ]` + *(warden YYYY-MM-DD: overclaim — …)*), inside the reopen cap. This is the same overclaim rule as honesty. It is how a checked item that does not match the code gets opened again. Do not start a repo-wide audit. Work-verifier already judged the unit that created a `[x]` in this run; this skim catches a checked item that never went through that compare, or whose code no longer matches.

**Checks** are not first-match. An outcome already `[x]` with a current passing note stays `[x]`. That is not a new check, and it does not add another human-verify playtest.

- **Reopen** when the outcome is `[x]` and either this turn’s code changes an observable that sentence names (a copy or typo fix does not) or a human playtest report says the scenario did not hold. Uncheck the outcome and the matching Acceptance line. One sentence on the outcome says why. Add one open Exercise if none is open. Do not add a playtest. The old passing note stays in Completed.
- **Passing note and the outcome is still `[ ]`** → set that outcome `[x]` and check the matching operable Acceptance line, even when open children remain. Those children stay open as their own work. Then the **human look** below.
- **No passing note** and the outcome or operable Acceptance is `[x]` → uncheck those lines even when an add-branch already matched. Leave the outcome `[ ]`. Do not add a playtest.

**Adds** — first match wins, and only for an outcome still `[ ]` after the checks:

1. **Open non-exercise children** with that `` `outcome:` `` label remain → leave the outcome open. Do **not** add an Exercise or follow-ups.
2. **Phased** and domain children for that phase are still open → leave the outcome open. Do **not** add the exercise task yet.
3. **Exercise item still open** → leave it. Do **not** add a second Exercise.
4. **Latest exercise is a Completed break note** and no open or Completed task cites that break → add follow-ups that cite the break (path, date, what failed), still inside the cap. Do **not** add another Exercise. Do **not** write the rest of the path from a reading of the code. Leave the outcome open.
5. **Latest exercise is a Completed break note** and every task that cites that break is Completed → add **one** new Exercise to re-run. Do not repeat the old follow-ups. This add ranks **first** inside the honesty cap (≤5).
6. **No exercise item** (none open, none Completed) and no passing note → add one High item: **Exercise** plus the slug — run the scenario and record the first break (path, date, observed result), labeled `` `outcome: <slug>` ``. Citation: the outcome slug + the Acceptance line. This add ranks **first** inside the honesty cap. Drop a weaker honesty add if needed to keep the cap. Point **Current focus** at it when that stem’s focus is empty or names finished work.

A Completed break note is not “no exercise item.” Do **not** add another Exercise in the same pass as the cited follow-ups.

**Human look** (same pass, in-scope stems only). Only this audit creates a human-verify playtest. Open `docs/Human-TODO.md` (create from the template if the audit checks an outcome and the file is missing).

- **Worth a look:** this pass changed that outcome from `[ ]` to `[x]`, and neither Open nor Done already has a `playtest` for that stem + slug → add one thin Open row: kind `playtest`, the scenario sentence, Owner link, outcome slug, exercise date. A Done playtest is not a missing row.
- **Not a human look:** an Open `playtest` names that stem (or its outcome slug) while that outcome is still `[ ]` → move the row to Done as `- [x]` with `(warden YYYY-MM-DD: withdrawn — outcome still open; not a human look)`. The human did not check it. Do this for a generic orchestration look-list on that stem when any of its outcomes are still `[ ]`. Leave `procure` / `decide` / `waiting` alone. Leave a playtest that names a slug already `[x]`.
- **Scenario did not hold:** a human confirm on that playtest says the scenario did not hold → move the inbox row to Done with the report, then run **Reopen** for that slug. Do not leave the outcome `[x]`. A confirm that the scenario held leaves the outcome `[x]` and moves the inbox row to Done.

These audit adds, the Acceptance checkbox edit, and the human-look edit do **not** by themselves make the report `gaps-found`. Report them as **Outcomes open** and **Human looks**. `gaps-found` still fires when this run **claimed** the feature, stem, or outcome done while an outcome is `[ ]`, or when a non-audit honesty add/reopen was written. Open operable Acceptance and a missing exercise path are the audit’s Exercise row, not a separate honesty add.

## Steps

1. Resolve mode: **honesty+hygiene** (default for orchestrator close-out / *todo warden*) vs **hygiene-only** (*todo cleanup* / parent said so).
2. For each in-scope stem, read the `-TODO.md`. For honesty: also spec Acceptance (+ Understanding if present); skim only relevant code for claims you might reopen or gap.
3. **Honesty (if in mode):** Collect candidate **reopens** and **adds** with a one-line **citation** each. Rank by honesty risk: overclaims first, then operable Acceptance / exercise path, then shape fights. Drop anything weak or uncitable. Apply **hard caps**. Prefer reopening a false `[x]` over adding a duplicate new item.
4. **Edit honesty** on in-scope `*-TODO.md` only:
   - Reopen: `[ ]` + short note *(warden YYYY-MM-DD: overclaim — …)*
   - Add: short High Priority (or Medium if clearly not blocking) items with citation in the description
   - Refresh **Current focus** when the next honest work changed
5. **Hygiene (always unless parent said honesty-only):** Scan open sections for remaining `[x]` tasks; **move** them to **Completed** per rules above. Create Completed / archive file if needed. Do **not** edit specs/Understanding except the outcome-audit Acceptance checkbox below.
6. **Outcome audit (if honesty, not hygiene-only):** Run the section above, including the human look. Uncheck a falsely checked operable Acceptance line. Check an Acceptance line only together with its outcome, and only on a passing exercise note. Do **not** add a second Exercise when a break note already exists.
7. Return a structured report (below). **Stop.**

## Report *(required)*

```text
Todo warden — [clean | gaps-found]
Stems: …
Mode: honesty+hygiene | hygiene-only | honesty-only
Reopened (N): - item — citation
Added (N): - item — citation
Moved to Completed (N): - stem — count (optional: 1–2 examples)
Outcomes open (N): - slug — children remain | needs exercise | break cited | re-run after follow-ups
Human looks (N): - slug — playtest added | withdrawn premature
Deferred not written (N): - gap — citation  *(only if over honesty cap or soft)*
Left alone: short note
Caps: new≤5 reopened≤10; hygiene moves uncapped
```

- **`clean`** — no **honesty** reopens/adds other than outcome-audit exercise / cited-break items (hygiene moves are fine). Safe for PR ready from a backlog-honesty perspective. **`Outcomes open` does not block ready** and is not stem-drained.
- **`gaps-found`** — honesty reopens and/or new TODO items written (other than the outcome-audit exercise item and cited-break follow-ups), **or** this run claimed the feature, stem, or outcome done while an Outcomes row is `[ ]`. Parent must **not** treat the run as “stem drained / ready to mark PR ready” without handling new open work (leave draft, or re-loop if budget remains — parent decides; this role does not implement). **Hygiene-only moves never force `gaps-found`.** **`Outcomes open` alone never forces `gaps-found`.**

## Stop when

- Report returned and (if any) TODO edits applied within honesty caps; hygiene applied for in-scope stems

## Do not

- Write application code, run product refactors, or “fix” gaps in code
- Check an Outcomes row because its children are `[x]`, or without a passing exercise note (path, date, scenario held)
- Leave operable Acceptance `[x]` when there is no passing exercise note
- Leave an outcome `[x]` when this turn changed an observable it names, or when a human report says the scenario did not hold
- Treat a unit-test path or a skipped observable clause as a passing note
- Write a remaining-path plan from a reading of the code; follow-ups cite a recorded break
- Treat an empty High/Medium/Low list as stem-drained while an Outcomes row is `[ ]`
- Exceed honesty hard caps or dual-maintain every Acceptance line as a TODO twin
- Invent backlog from imagination, HN wishlists, or uncited “best practice”
- Audit the whole Document Map when the brief named a few stems (unless user asked project-wide cleanup)
- Mark Human-TODO / human-gated items done without a confirm report (user, or an allowed assignee bot when `team_inbox.enabled`); invent Human-TODO spam for design-by-default. The human-look withdraw is not a confirm — it records **not a human look**. The one playtest after a passing note is required, not spam
- Add another Exercise in the same pass as a break note’s cited follow-ups
- Dual-write a playtest while the outcome is `[ ]`
- Invent `Team-Roster.md` bot or human-name rows on a handoff (read only; named humans and bots self-ID — [`workflow/team-roster.md`](../workflow/team-roster.md))
- Leave true `[x]` tasks parked in High/Medium/Low when running hygiene (that **is** the cleanup job)
- Do not add a Completed row for an incidental fix (review patch, Bugbot finding, copy or typo)
- Move items you reopened this pass into Completed
- Commit, push, merge, or spawn subagents
- Soft-add TODOs “just in case” when the stem is honestly complete for this run’s claims
- Edit the spec except the one matching operable Acceptance checkbox during outcome audit
- Fetch vendor API docs or invent unnamed leftover facets (named spec leftovers get covering TODOs; thin wrap-the-API research is at most **one** item and only when this run claimed kit-complete)
- Create new Document Map rows for leftovers
