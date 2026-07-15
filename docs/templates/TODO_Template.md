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
- [ ] **Task title** — short description of what needs to be done and why it matters
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

**Feature depends on human procurement (API key, cloud bot, account):**
- Blocked until [need] exists (see [Human-TODO.md](../Human-TODO.md) — "[row name]") — do not put the full procurement checklist here

**You are building the shared foundation itself** — do not list those tasks here. Add them to `_shared/ComponentName-TODO.md` and link from here only if a feature is waiting.

**Shared spec change needed:**
- Update [_shared/SomeComponent.md](../_shared/SomeComponent.md) — track implementation in [_shared/SomeComponent-TODO.md](../_shared/SomeComponent-TODO.md)

- Design question for user: [brief question here]

## Completed (Archive, create a -todo-complete.md file if the list gets too long)
- [x] Example completed task (finished 2026-05-04 by Cursor) — brief note if useful

---

**Instructions for AI Agents**:

- **If this TODO is in `_shared/`** — tracks foundation work on the shared component (same note-type set as features unless the user excepted files). Consumer features link here; do not duplicate these tasks in feature TODOs.
- **If this TODO is for a feature or shared component** — read `FeatureName-Understanding.md` or `_shared/ComponentName-Understanding.md` first. Do not implement until status is `confirmed` or the user waives review. **If `confirmed`**, read for context and proceed — do not re-prompt the user to review that Understanding unless scope changes.
- Add new items as you discover them; **update Current focus** at session end (`[x]` + date on completed items).
- Foundation tasks belong in `_shared/Component-TODO.md`, not in a feature TODO — see [`Modular_Docs_Workflow.md`](Modular_Docs_Workflow.md) §1.
- In-Editor feature TODOs: rename to engine-specific version per Workflow §7.

**Instructions for Humans**:
- **Current focus** is your "where we left off" — skim it when resuming or switching agents.
- Shared TODO: what's left to build the reusable piece.
- Feature TODO: what's left for this feature (including dependency links to shared work).

---

*This template is part of the Lean Modular Documentation system. Keep it concise — aim for 1 screen of high-priority items.*