<!-- pack-version: 2.7.17 -->

> **Workflow module.** Open from the [workflow index](../Modular_Docs_Workflow.md) for TODO layout, Current focus, exploration vs shipping, or operable-done / Acceptance bridge.

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
- **Exploration vs shipping:** See §5.2.
- **Session start:** Read the active TODO's **Current focus** block first (§5.1) — then High Priority.
- While working: Add new items as you discover them (including exercise-path rows when domain work reveals a missing run path — §5.3).
- After finishing a task: Mark `[x]`, add completion date/note, and **move** the item into **## Completed** (do not leave long `[x]` lists under High/Medium/Low).
- **Session end:** Update **Current focus** for the next session.
- **Todo warden** ([`roles/todo-warden.md`](../roles/todo-warden.md)): post-loop honesty **and** hygiene — moves parked `[x]` items into Completed when agents forgot.

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

**Acceptance:** not a second checklist. Open **operable** lines = remaining work. When a TODO meets a line → update Acceptance same turn. “All TODOs `[x]`” + open operable Acceptance + no covering work = **incomplete** (stem drained / Layer done claims fail).

**Implement / verify / orchestrate:** add missing exercise-path TODOs when discovered; domain-only clearance without path/phase/library-only is not stem-done. Work-verifier **fails** claimed feature/Layer done that is domain-only without bridge, or that leaves matching operable Acceptance open with no TODO.

### 5.4 Finished-kit contract ⇒ covering TODOs *(not wait-for-pickup)*

**Failure mode:** Agent can write the **finished product** spec (kit contract, remaining APIs, owning stems) but then **omits TODO items** for those in-scope surfaces — citing “do not invent work,” “no planned-only map rows,” “until someone picks one up,” or treating a **terse but actionable** goal as a stub that needs hand-holding through each facet. Overnight **orchestrate** then has nothing to drain except Current focus.

**Rule:** If this stem’s spec (or the confirmed kit contract) names a surface as **in-scope for the product**, that surface needs an **implementable TODO** on an **existing** stem (this inventory TODO, or the owning stem already on the map) — **open or Completed**. Writing missing **open** items is **not** inventing work. **Inventing** is adding APIs, products, or map rows the user never included. Do **not** resurrect surfaces that already have a Completed covering item.

**Terse + public contract = expand, don’t interview.** “Fully support this vendor’s API” (or equivalent) is actionable when the vendor docs / OpenAPI / upstream SDK are available: **diff those against current code** and add covering TODOs for gaps. Do **not** wait for the user to name Files, embeddings, batch, … one by one. Do **not** treat that plan as vague or as a Catalog `stub`. Vague = cannot implement without a **product decision the docs don’t answer** (playground UI, private app names, “maybe later”).

**Pickup ≠ backlog:** “Picked up” = Current focus / orchestrator **starts that unit**. It is **not** when the TODO row is first written. Do **not** leave in-scope spec surfaces off the TODO until a human chooses them.

**Order on the inventory TODO:** High / Current focus = the next winner (target architecture for **that** cut). Medium / Low = the rest of the finished kit, unordered until promoted. Orchestrate drains High through Low unless the user capped tiers.

**Still do not:** new Document Map rows for leftovers or for vague planned-only ideas ([`naming-layout.md`](naming-layout.md) §0 inventory rule); TODOs for out-of-kit future APIs; one mega-commit for the whole kit (git: `milestone-pr` — many verified units).

**Timescale:** Spec the **finished product**, not an intermediate architecture. Backlog that product as **many verify-order units**. Overnight drain = implement those units, not wait, not one dump.

---
