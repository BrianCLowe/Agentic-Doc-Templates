# [Feature Name] — TODO

> Copy under `docs/features/` or `docs/_shared/`. Do not edit this template unless the user asks.
>
> **Humans:** [`help/SCAFFOLDS.md`](help/SCAFFOLDS.md). **Agents:** fill blanks; re-open [`agent/workflow/todos.md`](agent/workflow/todos.md) if context is thin (operable done §5.3 · kit coverage §5.4 · Current focus §5.1).

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

**Instructions for AI Agents**

Fill the lists. Do not restate operable / kit / dual-write rules here — re-open [`workflow/todos.md`](agent/workflow/todos.md), [`workflow/human-todo.md`](agent/workflow/human-todo.md), [`workflow/shared-components.md`](agent/workflow/shared-components.md) when context is thin.

**Instructions for Humans**

Your inbox is [`Human-TODO.md`](../Human-TODO.md). Current focus is where the agent left off. How to read this file: [`help/SCAFFOLDS.md`](help/SCAFFOLDS.md).

---

*Keep High Priority to roughly one screen — finished work belongs under **Completed**.*
