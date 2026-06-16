---
name: Modular Documentation
description: Read Master_Index first; use feature TODOs as living task lists
applyTo: "**"
---

# Modular Documentation Rule

First, check if `docs/Master_Index.md` exists. If it does not exist, ignore this entire rule and work normally.

This project uses a lean modular documentation system. `docs/Master_Index.md` is the single entry point.

**Always follow this order when starting work:**
1. Read `docs/Master_Index.md` first.
2. Follow the Quick Start section exactly — use **Path A** for `_shared/` foundation work, **Path B** for feature work.
3. Open the relevant `-Understanding.md` when discussing, planning, or implementing a **feature or shared component**. **If missing, draft it first** from the conversation (status `draft`) and show the user for review — do not wait for the user to write it (shared components get Understanding by default unless the user excepted it — see Master Index Section 2.4).
4. Open the correct TODO before making changes — read **Current focus** first (Master Index Section 6.1):
   - Shared foundation → `_shared/ComponentName-TODO.md` (and InEditor/Asset TODOs as needed, unless recorded in Section 3.0)
   - Feature work → `features/FeatureName-TODO.md` (and InEditor/Asset TODOs as needed)
5. Before integrating a **shared** piece, check its **Maturity** on the spec or Document Map (`draft` | `usable` | `stable`).

**Shared foundation (critical):**
- Shared components get the **same note types as features** unless the user explicitly excepted specific files — record exceptions in Master Index **Section 3.0**.
- Tasks that **build or refactor** a shared component go in `_shared/ComponentName-TODO.md` (and related shared TODOs) — **not** in a consumer feature's TODO.
- Feature TODOs only **link** to shared TODOs when blocked or integrating (dependency note), they do not duplicate foundation tasks.

**Before implementation:**
- **Draft `-Understanding.md` first** when scoping new work — show the user how you interpreted their request; do not expect them to write it.
- Do not treat a feature as greenfield if Understanding says it extends or reuses existing work.
- Do not start coding while Understanding status is `draft` unless the user explicitly waives review.
- When producing a plan, include the Understanding file path so the user can correct scope and UI intent first.
- If the user's idea is vague, ask brief questions from `docs/templates/IDEA_CAPTURE_TIPS.md` (or project copy), then **draft** `-Understanding.md` for their review.
- When the user confirms Understanding, **graduate** durable content to the spec (`Feature_Spec_Template.md`) — Decisions, architecture, shared **Maturity**.
- Record lasting tradeoffs in the spec **Decisions** table or `docs/decisions/` (Section 10).
- When the user provides UI reference screenshots, persist to `docs/features/assets/` or `docs/_shared/assets/` (copy from path when available; if paste-only chat image, ask user to save file or document from vision). Link from `-Understanding.md` **Visual references** with similar vs different.

**While working:**
- **Session start:** Read the active TODO's **Current focus** block first.
- Treat the active TODO as the living task list.
- Add new items as you discover them (new steps, clarifications, cross-feature dependencies, edge cases, refactoring needs).
- Use the "Cross-Feature Dependencies & Integration Notes" section when features interact.

**After changes (mandatory):**
- Update **Current focus** and the relevant `-TODO.md` — mark completed items with `[x]` + date.
- Update `-Understanding.md` when the user corrects scope, UI intent, or assumptions — especially **What this is NOT**.
- If code diverges from confirmed Understanding, reconcile spec + Understanding or set Understanding to `superseded`.
- Move finished items to Completed when the list gets long.
- Only read other files when they are explicitly linked from Master_Index or the current TODO/spec.

**Clarification Protocol:**
If the user says "review spec", "check for gaps", "ask questions", or "confidence check":
- Re-read the feature or shared spec, Understanding, and TODO
- Identify areas that are vague, missing, or open to interpretation
- Ask targeted clarifying questions instead of assuming
- Only proceed after user confirmation

**Philosophy:** Keep documentation small and accurate. TODO **Current focus** + checklists are your primary memory across sessions.
