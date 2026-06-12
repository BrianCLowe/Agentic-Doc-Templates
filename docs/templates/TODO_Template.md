# [Feature Name] — TODO
> Never edit this template unless the user asks you to.

**Last Updated**: [YYYY-MM-DD]  
**Feature Owner**: [Name or "Team"] (optional omit if not specified) 
**Related Spec**: [Link to FeatureName.md](../features/FeatureName.md) *(update path as needed)*  
**Related Understanding**: [Link to FeatureName-Understanding.md](../features/FeatureName-Understanding.md) *(create before implementation)*

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

**You are building the shared foundation itself** — do not list those tasks here. Add them to `_shared/ComponentName-TODO.md` and link from here only if a feature is waiting.

**Shared spec change needed:**
- Update [_shared/SomeComponent.md](../_shared/SomeComponent.md) — track implementation in [_shared/SomeComponent-TODO.md](../_shared/SomeComponent-TODO.md)

- Design question for user: [brief question here]

## Completed (Archive, create a -todo-complete.md file if the list gets too long)
- [x] Example completed task (finished 2026-05-04 by Cursor) — brief note if useful

---

**Instructions for AI Agents**:

- **If this TODO is in `_shared/`** — tracks foundation work on the shared component. Consumer features link here; do not duplicate these tasks in feature TODOs.
- **If this TODO is for a feature** — read `FeatureName-Understanding.md` first; do not implement until Understanding is `confirmed` or the user waives review.
- Add new items as you discover them; end each session by updating this file (`[x]` + date on completed items).
- Foundation tasks belong in `_shared/Component-TODO.md`, not in a feature TODO — see Master Index Section 2.4.
- In-Editor feature TODOs: rename to engine-specific version per Master Index Section 7.

**Instructions for Humans**:
- Shared TODO: what’s left to build the reusable piece.
- Feature TODO: what’s left for this feature (including dependency links to shared work).

---

*This template is part of the Lean Modular Documentation system. Keep it concise — aim for 1 screen of high-priority items.*