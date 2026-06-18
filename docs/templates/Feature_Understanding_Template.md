# [Feature or Shared Component Name] — Understanding

> Never edit this template unless the user asks you to. Use under `docs/features/` for features or `docs/_shared/` for shared components (adjust Related Spec/TODO paths). Shared components get this file by default unless the user excepted it.

**Status**: draft | reviewed | confirmed | superseded  
**Last Updated**: [YYYY-MM-DD]  
**Last reconciled with code**: [YYYY-MM-DD or "—"]  
**Related Spec**: [FeatureName.md](FeatureName.md)  
**Related TODO**: [FeatureName-TODO.md](FeatureName-TODO.md)

---

This file captures **what the agent believes the user wants** — scope, behavior, UI, and ties to existing work. **The agent writes this file first** (status `draft`). The user **reviews and corrects** it before implementation — they do not need to author it from scratch.

**Not sure what to ask the user?** See [`../help/IDEA_CAPTURE_TIPS.md`](../help/IDEA_CAPTURE_TIPS.md) — plain-language interview questions about UI, flows, and scope (no coding knowledge required on the user's part).

**Do not start implementation** while status is `draft` and assumptions remain unchecked, unless the user explicitly says to proceed.

---

## What this is

[Plain-language summary in the user's terms. One short paragraph.]

*Example: A role-specific view of the existing text editor — same editing core, different surrounding UI for this workflow.*

---

## What this is NOT

[Explicit scope boundaries. Prevents treating extensions, variants, or modes as greenfield features.]

- NOT a new standalone [X] — it reuses [existing component/feature]
- NOT [common misinterpretation the agent might make]
- [Add more as needed]

---

## Relationship to existing work

| Existing piece | Relationship |
|----------------|--------------|
| [ExistingFeature.md](ExistingFeature.md) | [Extends / wraps / alternate UI for / configures — be specific] |
| [_shared/SomePattern.md](../_shared/SomePattern.md) | [Consumes / blocked by / extends — not "building" unless Path A] |

---

## How it should work

[Behavior, flows, edge cases the user cares about. Prose or numbered steps.]

1. User does X → system does Y
2. …

---

## UI / UX intent

[What it looks like, layout, what to reuse from existing UI, references to similar screens in the app.]

- Reuse: [existing panel, toolbar, editor chrome, etc.]
- Differs from default: [only these elements]

---

## Visual references

Store screenshots in `docs/features/assets/`, `docs/_shared/assets/`, or `docs/reference/visuals/`. Link here so vision-capable agents can reuse them in later sessions. Always note **similar** vs **different** — a reference is not a spec to copy blindly.

| File | Similar (borrow) | Different (our idea) |
|------|------------------|----------------------|
| [assets/FeatureName-reference-label.png](assets/FeatureName-reference-label.png) | [e.g. full-width text, minimal chrome] | [e.g. our Save top-left; no slash menu] |
| [assets/FeatureName-our-existing-panel.png](assets/FeatureName-our-existing-panel.png) | [match this panel from our app] | [new feature hides sidebar] |

*Example row:* `[assets/RoleEditor-notion-focus.png](assets/RoleEditor-notion-focus.png)` — similar: focus layout; different: reuse our editor toolbar.

---

## Done when *(acceptance — agent drafts, user confirms)*

The user should be able to judge "is this feature/component done?" without reading every TODO.

- [ ] [Observable outcome, e.g. "User can enter focus mode from document list and return with Esc"]
- [ ] [Another acceptance criterion]
- [ ] [Edge case that must work, e.g. "Save failure shows toast; text is not lost"]

Move checked items to **Confirmed with user** when verified in a build; update spec **Last reconciled with code** when shipped.

---

## Assumptions (needs user confirmation)

- [ ] [Assumption the agent is making]
- [ ] [Another assumption]

When the user confirms or corrects an item, move it to **Confirmed with user** and update the relevant section above.

---

## Confirmed with user

- [YYYY-MM-DD] — [What was confirmed or corrected, e.g. "Separate UI only — same editor core as BlockEditor"]

---

## Instructions for AI Agents

- **Write this file first** when the user discusses, plans, or scopes a feature or shared component — before writing implementation code.
- Draft from the conversation (or a short interview using [`../help/IDEA_CAPTURE_TIPS.md`](../help/IDEA_CAPTURE_TIPS.md) if vague). Set status to `draft` and **show the user the file** for review.
- After updating, surface it to the user — the goal is to reveal *your* interpretation so they can correct misunderstandings early.
- When planning: include this file (or its path) in the plan **before** implementation steps.
- When the user corrects you (in chat or by editing the file), update this file immediately — especially **What this is NOT** and **Relationship to existing work**.
- When the user provides reference screenshots, persist under `docs/features/assets/`: copy from disk when a path exists; if only pasted in chat, ask the user to save the file into `assets/` or record similar/different from vision and note re-attach if needed. Link in **Visual references**.
- Set status to `confirmed` only after the user explicitly approves (or approves a plan that references this file). Then **graduate** durable content to the spec ([`Modular_Docs_Workflow.md`](Modular_Docs_Workflow.md) §2) — Decisions, architecture, maturity (shared).
- If code or plan diverges from this file, set `superseded` or update **Last reconciled with code** after aligning spec and Understanding — do not leave both stale.
- Read this file before implementation alongside the spec and TODO.

**Instructions for Humans**

- **You do not write this file from scratch** — the agent drafts it; you review.
- Skim the draft before approving a plan or agent work session.
- Correct wrong assumptions in **What this is NOT** — that section prevents the "completely new feature" mistake. Edit the file directly or tell the agent what to fix; either way, the agent should update the file.
- Use [`../help/IDEA_CAPTURE_TIPS.md`](../help/IDEA_CAPTURE_TIPS.md) if you are stuck describing the idea — answer in chat; the agent translates into this file.
- Add reference screenshots to `docs/features/assets/` (or ask the agent to) and ensure **Visual references** notes what to copy vs what to change.
