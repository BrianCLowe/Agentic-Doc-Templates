> **Workflow module.** Open from the [workflow index](../Modular_Docs_Workflow.md) for TODO layout, Current focus, exploration vs shipping, operable-done / Acceptance bridge, or sticky outcomes.

# TODO management

## 5. TODO Management

Every feature **must** have at least one companion `-TODO.md` file (core). InEditor / Asset TODOs only when Project Profile game extensions apply or the user asks — most non-game features need the core TODO only.

Every substantial `_shared/` component gets the **same TODO file set as a feature** (§1) unless the user explicitly excepted specific files (Master Index §3.0).

**File naming**:

- Core gameplay/systems: `FeatureName-TODO.md` or `_shared/ComponentName-TODO.md`
- In-Editor work: `FeatureName-InEditor-TODO.md` or `_shared/ComponentName-InEditor-TODO.md` (rename per §7)
- Assets & content: `FeatureName-Asset-TODO.md` or `_shared/ComponentName-Asset-TODO.md`

**Shared vs feature — cross-links**:

When a feature depends on shared foundation work, the feature TODO gets a **dependency note**, not a duplicate of the foundation tasks:

> Blocked until shared editor API exists (see [_shared/BlockEditor-TODO.md](../_shared/BlockEditor-TODO.md) — "Expose shared editing API")

**Cross-feature interactions**: Add a note in the TODO with a direct link when work depends on or affects another feature.

**Dynamic TODO creation**: Add new items as you work. See [`TODO_Template.md`](../../TODO_Template.md) for format.

**Workflow**:

- **High Priority sizing:** Prefer one item (or a tight cluster) that lands the **confirmed target architecture**. Sub-bullets / Medium Priority = verify slices or follow-ups — not “ship the wrong architecture first.” If Current focus fights confirmed Understanding, rewrite the TODO before coding ([`Agent_Timescale_Planning_Rule.mdc`](../Agent_Timescale_Planning_Rule.mdc)).
- **Operable done / dual track:** See §5.3 — user-facing stems need domain **and** exercise-path rows; library-only stems must say so.
- **Sticky outcomes:** See §5.5 — an outcome row stays open until a passing exercise note. Child tasks do not close it or the matching Acceptance line.
- **Exploration vs shipping:** See §5.2.
- **Session start:** Docs freshness first (Workflow §0.3 — `git status` + worktrees; sibling `docs/` drift → stop). Then read the active TODO's **Current focus** block (§5.1) — then High Priority.
- While working: Add new items as you discover them (including exercise-path rows when domain work reveals a missing run path — §5.3).
- After finishing a **plotted** task: Mark `[x]`, add completion date/note, and **move** the item into **## Completed** (do not leave long `[x]` lists under High/Medium/Low). **Completed is not a repair log.** Skip a new row for an incidental fix (review patch, Bugbot finding, copy or typo). Git already has that change. If the fix changes an observable an Outcome names, run the §5.5 reopen: uncheck that outcome and its Acceptance line, one sentence on the outcome, one Exercise. Do not leave the outcome `[x]` with only a sentence. Do not add a checkbox. A copy or typo fix stays checked. Sync pass `optional-todo-completed-cleanout` removes a Completed checkbox that git shows was never an open `[ ]` task and is not an exercise note.
- **Session end:** Update **Current focus** for the next session.
- **Todo warden** ([`roles/todo-warden.md`](../roles/todo-warden.md)): post-loop honesty **and** hygiene — moves parked `[x]` items into Completed when agents forgot. Outcome audit on that same close-out (§5.5).

### 5.1 Session handoff — Current focus

Each active `-TODO.md` should keep a short **Current focus** block at the top (see [`TODO_Template.md`](../../TODO_Template.md)):

- One active task (or "blocked by …")
- Blockers with links
- Optional: last session date / agent tool

This gives the next agent (or a different tool) a 5-second orientation without re-reading everything.

### 5.2 Exploration vs shipping

When product shape is still unknown, a short **spike** (branch, throwaway prototype, learning pass) is fine. Label it clearly in Current focus / High Priority as **exploration** — not the destination architecture.

**Rules:**

- Spikes teach product rules; they are **optional**, not a required stage before the honest cut.
- Once Understanding (or the user) locks shape, the **paved path** is the target architecture. Do **not** promote the spike’s interim (e.g. caret bridging, dual systems) into High Priority milestones.
- After shape is clear: either land the target cut, or keep a named spike item explicitly disposable — never “Phase 1 wrong arch → Phase 2 correct” as the default plan when UX already implied the correct one.
- Lock 3–4 product rules when shape is ambiguous, then cut — do not use ambiguity as cover for shipping a known-wrong interim once rules are known.

### 5.3 Operable done — exercise path *(not library-by-default)*

**Failure mode:** Product-shaped Index / Understanding / Overview / Acceptance + domain-only TODOs/Architecture → agents clear packages and call the stem done. **Allowed only with an explicit bridge.**

**User/operator-facing milestone “done” requires:**

1. Domain work for that cut, **and**  
2. An **exercise path** (UI · CLI · product API · documented smoke) matching how the product is used, **and**  
3. Operable **Acceptance** for that claim closed **or** still covered by open TODOs  

| Bridge | When | How |
|--------|------|-----|
| **Dual-track TODOs** | Default for user-facing stems | High Priority = domain **and** surface/wire/smoke |
| **`library-only`** | Pure package / no operator surface on **this** stem | Label TODO/focus once; consumers own wire |
| **Phased** | Domain before surface **on purpose** | Loud: `library foundation first · exercise path: <named path>` — not silent package-only High Priority |
| **Scaffold + wire** | Product needs a surface but **no UI specs** | Minimal boring UI/CLI/smoke on High Priority / same cut — **not** Human-TODO “await design” unless user gated design-first / no UI / library-only |

**Do not:** invent a phase only because mockups are missing; treat blank canvas as a hard decide; twin every High Priority row onto Acceptance.

**Acceptance:** not a second checklist. Open **operable** lines = remaining work. An operable Acceptance line stays `[ ]` until the outcome audit records a passing exercise (§5.5). A slice that meets a Behavior bullet does not check that line. “All TODOs `[x]`” + an open outcome or open operable Acceptance + no covering work = **incomplete** (stem drained / Layer done claims fail).

**Implement / verify / orchestrate:** add missing exercise-path TODOs when discovered; domain-only clearance without path/phase/library-only is not stem-done. Work-verifier **fails** claimed feature/Layer done that is domain-only without bridge, that leaves matching operable Acceptance open with no TODO, or that checks an operable Acceptance line or an Outcomes row without a passing exercise note (§5.5).

### 5.4 Finished-kit contract ⇒ covering TODOs *(not wait-for-pickup)*

**Failure mode:** Agent can write the **finished product** spec (kit contract, remaining APIs, owning stems) but then **omits TODO items** for those in-scope surfaces — citing “do not invent work,” “no planned-only map rows,” “until someone picks one up,” or treating a **terse but actionable** goal as a stub that needs hand-holding through each facet. Overnight **orchestrate** then has nothing to drain except Current focus.

**Rule:** If this stem’s spec (or the confirmed kit contract) names a surface as **in-scope for the product**, that surface needs an **implementable TODO** on an **existing** stem (this inventory TODO, or the owning stem already on the map) — **open or Completed**. Writing missing **open** items is **not** inventing work. **Inventing** is adding APIs, products, or map rows the user never included. Do **not** resurrect surfaces that already have a Completed covering item.

**Terse + public contract = expand, don’t interview.** “Fully support this vendor’s API” (or equivalent) is actionable when the vendor docs / OpenAPI / upstream SDK are available: **diff those against current code** and add covering TODOs for gaps. Do **not** wait for the user to name Files, embeddings, batch, … one by one. Do **not** treat that plan as vague or as a Catalog `stub`. Vague = cannot implement without a **product decision the docs don’t answer** (playground UI, private app names, “maybe later”).

**Pickup ≠ backlog:** “Picked up” = Current focus / orchestrator **starts that unit**. It is **not** when the TODO row is first written. Do **not** leave in-scope spec surfaces off the TODO until a human chooses them.

**Order on the inventory TODO:** High / Current focus = the next winner (target architecture for **that** cut). Medium / Low = the rest of the finished kit, unordered until promoted. Orchestrate drains High through Low unless the user capped tiers.

**Still do not:** new Document Map rows for leftovers or for vague planned-only ideas ([`naming-layout.md`](naming-layout.md) §0 inventory rule); TODOs for out-of-kit future APIs; one mega-commit for the whole kit (git: `milestone-pr` — many milestones; a milestone may be several related TODOs, then squash that PR).

**Timescale:** Spec the **finished product**, not an intermediate architecture. Backlog that product as **many verify-order units**. Overnight drain = implement those units (group into milestones when they belong together; parallelize when they do not overlap **and** the host can isolate), not wait, not one dump. See [`roles/orchestrator-git.md`](../roles/orchestrator-git.md) **PR unit + concurrency** + **Host worktrees**.

### 5.5 Sticky outcomes *(children do not close the capability)*

**Failure mode:** Generated tasks are locally true and the TODO list drains, while the capability is still false. Agents check Acceptance because a slice looked close. Warden then reports `clean`.

**Outcome row.** On each user-facing stem’s `-TODO.md`, `## Outcomes` holds one checkbox per operable Acceptance line. The text is that scenario: who acts, what they do, what is observable. Stable slug in bold, then the sentence.

```markdown
## Outcomes

- [ ] **paper-auto-trade** — Operator starts a paper auto-trade and sees simulated orders, fills, and P&L.
```

**Children stay flat.** High / Medium / Low items are not indented under the outcome. Each child that serves an outcome ends with `` `outcome: paper-auto-trade` ``. Completing every child does not check the outcome or the matching Acceptance line.

**Who runs the audit.** The procedure is the Outcome audit in [`roles/todo-warden.md`](../roles/todo-warden.md). It checks the parent outcome and fills the next blank (one Exercise, or cited follow-ups after a break). Doc-roles are optional. Declining doc-roles does not skip the audit.

- Orchestration close-out spawns `todo-warden` when that adapter is installed, and follows the playbook in the parent session when it is not.
- Any other session — a one-off change, doc-roles declined, or staying in this session — runs **that section only** for stems this turn touched when this turn finished the last open non-exercise child of an outcome, finished an exercise item, would claim the feature, stem, or outcome done, or this turn’s code changed an observable a checked outcome names. That is not full orchestration and not a project-wide honesty sweep. The check that sets the outcome `[x]` waits until after work-verifier **pass** when this turn has a verifier. The implementer unit leaves the outcome `[ ]`. Reopen of an already `[x]` outcome runs in that same audit.

**Passing note.** A **Completed** exercise item for that slug. The path is that stem’s exercise path (UI, CLI, product API, or documented smoke), not a unit-test file. The observation states what happened for **each observable clause** in the outcome sentence. “Looks right,” a skipped clause, or a unit-test path is not passing. A break note names the first clause that failed and is not passing.

**Who may check.** Only that audit. It may set the outcome `[x]` and check the matching Acceptance line only when a current passing note exists and the outcome is still `[ ]`. A passing note checks the outcome even when other children remain. An outcome already `[x]` stays `[x]` while that note is still current. A later pass does not check it again. A note that records the first break leaves both open. A slice that only looks close does not check either line. Work-verifier fails a unit that checks them, and fails an exercise item marked done when the note is not a passing note.

**Reopen.** Uncheck the outcome and the matching Acceptance line, put one sentence on the outcome, and add one open **Exercise** when one is not already open. Do that when this turn’s code changes an observable the outcome names (a copy or typo fix does not), or when a human playtest report says the scenario did not hold. The old passing note stays in Completed. The new Exercise is the next unit. That reopen does not add a playtest.

**Code versus the checklist.** Work-verifier compares one claimed TODO item to that unit’s diff. The diff does not implement the item → fail. It does not walk older checked rows. Warden honesty reopens a checked item whose code does not implement it. Declining doc-roles does not skip either compare: the parent runs that unit’s verifier steps before mark-done, and the outcome audit reopens a clear overclaim on the stems it already covers.

**Exercise task.** Add one High item, and point Current focus at it, only when this outcome has **no exercise item yet** (none open, none Completed) and no passing note, and it is not waiting on open children or an intentional phase:

```markdown
- [ ] **Exercise paper-auto-trade** — Run the scenario and record the first break (path, date, observed result). `outcome: paper-auto-trade`
```

A Completed exercise that records a first break is not a passing note and is not “no exercise item.” Do **not** add another Exercise in that pass. Add follow-ups that cite the break. After those follow-ups are Completed, the next unit is **one** new Exercise to re-run, not a copy of the old follow-ups.

Do not write the rest of the path from a reading of the code.

**Human look.** Only the outcome audit creates a human-verify playtest ([`human-todo.md`](human-todo.md) §13), and only when this pass changed that outcome from `[ ]` to `[x]`. Dedup against Open and Done. An outcome already `[x]` does not get another row. The orchestrator, implementer, graduate, and sync do **not** write that row on their own. A parent that is running the audit does. While the outcome is `[ ]`, do not ask the human to look. An answer of “it doesn’t work” only restates agent work that should already be a TODO. The audit withdraws an Open playtest that asks for a look at an outcome still `[ ]` (move to Done with a warden note; the human did not check it). A playtest confirm that says the scenario did not hold moves that inbox row to Done with the report, then follows **Reopen**. Leave `procure` / `decide` / `waiting` alone.

**Passing note** (on the exercise item, then move it to Completed):

```markdown
- [x] **Exercise paper-auto-trade** — (exercised YYYY-MM-DD: `<smoke command or operator path>`; scenario held — orders: …; fills: …; P&L: …). `outcome: paper-auto-trade`
```

**Library-only.** `## Outcomes` is one non-checkbox line: `library-only — consumers own the exercise path.` No outcome checkboxes. Children need no `outcome:` label.

**Phased.** The outcome stays `[ ]`. While domain children for that phase are still open, do not add the exercise task. When they are done, add it. A loud `library foundation first · exercise path: …` note is not stem-done.

**Orphans.** An item that serves no outcome stays unlabeled. Do not invent an outcome to house it.

**New work.** A new task on a stem that has outcome rows names one existing outcome. A new operable scenario adds the Acceptance line and the unchecked Outcomes row in the same turn. Implementers do not check either.

**Not stem-drained.** An empty High / Medium / Low list while any Outcomes row is `[ ]` is not feature done. The next unit is the exercise task when none exists, or the cited-break follow-up when the latest exercise recorded a break. Milestone PRs of honest child work may still merge. Claiming feature / stem / outcome done while an outcome is open is a gap.

**Do not:** nest children under a parent checkbox; check an outcome because its children are `[x]`; check operable Acceptance from a slice; treat a unit-test path or a skipped observable clause as a passing note; leave an outcome `[x]` after this turn changes an observable it names; leave an outcome `[x]` after a human report that the scenario did not hold; add another Exercise because a break note is not a passing note; mint a task per architecture bullet to map the remaining path without a cited break; reopen Completed items just to relabel them; ask the human to look at an outcome that is still `[ ]`.

---
