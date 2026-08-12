# [Feature Name] — TODO
> Never edit this template unless the user asks you to.

**Last Updated**: [YYYY-MM-DD]  
**Feature Owner**: [Name or "Team"] (optional omit if not specified) 
**Related Spec**: [Link to FeatureName.md](../features/FeatureName.md) *(update path as needed)*  
**Related Understanding**: [Link to FeatureName-Understanding.md](../features/FeatureName-Understanding.md) *(agent drafts before implementation; user reviews)*

---

## Current focus *(session handoff — update every session)*

**Active task:** [One sentence — what to do next, or "blocked"]  
**Blocked by:** [Link to TODO item, shared maturity, `Human-TODO.md` row, or "—"]  
**Last session:** [YYYY-MM-DD — optional tool/note]

*Next agent: read this block first, then High Priority.*

---

## High Priority / Next Actions
*(User-facing stems: dual-track — domain **and** exercise path (UI / CLI / product API / documented smoke). Label pure foundation **library-only**, or phase loudly: **library foundation first · exercise path: …**. Product Overview/Acceptance without this bridge is under-authored — Workflow §5.3.)*
- [ ] **Task title** — short description of what needs to be done and why it matters
- [ ] **Exercise path** — e.g. wire control plane / CLI so a human can run the happy path *(omit only if library-only / covered by phase note + later items)*
- [ ] Another high-priority item

## Medium Priority
- [ ] Task that can wait a bit

## Low Priority / Future Ideas
- [ ] Nice-to-have improvement

## Cross-Feature Dependencies & Integration Notes

Use the right pattern:

**Feature depends on another feature or shared work (not doing the foundation yourself):**
- Blocked until shared editor API exists (see [_shared/BlockEditor-TODO.md](../_shared/BlockEditor-TODO.md) — "Expose shared editing API")
- Requires `DiffWorkflow` first (see [DiffWorkflow-TODO.md](../features/DiffWorkflow-TODO.md))

**Needs a human** *(procure / playtest / decide / waiting — dual-write with [`Human-TODO.md`](../Human-TODO.md); Workflow §13):*
- **Owner here** (`playtest` / `decide`): keep the full item and outcome notes on *this* TODO; add a thin checkbox row on Human-TODO with **Owner** linking to this item — e.g. Needs human playtest: tune win target (see [Human-TODO.md](../Human-TODO.md) — "Score Target feel")
- **Owner on Human-TODO** (`procure` / `waiting`): short link only — Blocked until [need] exists (see [Human-TODO.md](../Human-TODO.md) — "[row name]") — do not put the full portal checklist here

**You are building the shared foundation itself** — do not list those tasks here. Add them to `_shared/ComponentName-TODO.md` and link from here only if a feature is waiting.

**Shared spec change needed:**
- Update [_shared/SomeComponent.md](../_shared/SomeComponent.md) — track implementation in [_shared/SomeComponent-TODO.md](../_shared/SomeComponent-TODO.md)

- Design question for user: [brief question here]

## Completed
- [x] Example completed task (finished 2026-05-04 by Cursor) — brief note if useful

---

**Instructions for AI Agents**:

- **If this TODO is in `_shared/`** — tracks foundation work on the shared component (same note-type set as features unless the user excepted files). Consumer features link here; do not duplicate these tasks in feature TODOs.
- **If this TODO is for a feature or shared component** — read Understanding first (shape guardrails). Do not implement until status is `confirmed` or the user waives. **If `confirmed`**, proceed — do not re-prompt Understanding review unless scope changes. Coarse **Acceptance** lives on the **spec**, not Understanding — this file is the living work checklist.
- **Agent timescale:** Size High Priority / Current focus for the **target architecture** matching confirmed shape. Stepped checklists = verify order inside one cut — not human-sprint interim architectures. Rewrite fighting TODOs before implementing. Label disposable spikes as **exploration** (Workflow §5.2); do not promote spike interims to the paved path once shape is known. Do not ask the user to remind you.
- **Finished kit (Workflow §5.4):** If the spec names an in-scope surface, this file (or the owning stem’s TODO) must have an implementable item for it. Filling those rows is **not** inventing work. “Picked up” = Current focus / orchestrate starts the unit — not when the row is first written. Do not wait for a human to choose leftovers. A terse wrap-the-public-API goal is actionable: expand from the docs. New map rows only when that slice is next — never for vague planned-only items (Workflow §0 inventory).
- **Operable done (Workflow §5.3):** User/operator-facing stems are not done when only domain/library/tests land. High Priority needs ≥1 **exercise path** (UI, CLI, product-facing API, or documented smoke) unless **library-only** or a **phased bridge** names the later path. **No UI specs ≠ defer:** scaffold + wire a minimal boring surface (or CLI/smoke) on High Priority — do not park UI for “design later” unless the user explicitly gated that. Spec **Acceptance** (operable lines) is not a second checklist — but open operable Acceptance with no open TODO that addresses them means incomplete product work; when a TODO meets an Acceptance line, update Acceptance same turn. Clearing domain checkboxes without path/phase/Acceptance bridge is incomplete — **add** surface/wire/smoke items when you discover the gap. Tight scope ≠ skip the run path for *this* stem.
- Add new items as you discover them; **update Current focus** at session end. On finish: `[x]` + date **and move** the item into **Completed** (do not leave done tasks under High/Medium/Low). Lasting preference corrections → that stem’s spec **Decisions** (same turn — Workflow §10), not this block.
- **Human-gated items:** when adding a task only a human can close (`playtest`, `decide`, `procure`, `waiting`), **dual-write** in the same edit — owner item here (or Blocked-by link for procure/waiting) **and** an Open row on [`Human-TODO.md`](../Human-TODO.md). Do not bury human asks only on this file.
- When the user reports human-TODO progress, update this owner item (`[x]` + feedback) and sync Human-TODO Done (Workflow §13).
- Foundation tasks belong in `_shared/Component-TODO.md`, not in a feature TODO — see [`workflow/shared-components.md`](agent/workflow/shared-components.md) §1.
- In-Editor feature TODOs: rename to engine-specific version per Workflow §7.

**Instructions for Humans**:
- **Your inbox** is [`Human-TODO.md`](../Human-TODO.md) — everything waiting on you (playtest, decide, procure, waiting). Tell the agent in chat when you finish or have feedback; they sync this file.
- **Current focus** is the agent's "where we left off" — skim it when resuming or switching agents.
- Shared TODO: what's left to build the reusable piece.
- Feature TODO: what's left for this feature (including dependency links to shared work).

---

*Keep High Priority to roughly one screen — finished work belongs under **Completed**, not under open priority sections.*
