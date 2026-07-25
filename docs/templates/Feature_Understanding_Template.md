# [Feature or Shared Component Name] — Understanding

> Never edit this template unless the user asks you to. Use under `docs/features/` for features or `docs/_shared/` for shared components (adjust Related Spec/TODO paths). Shared components get this file by default unless the user excepted it.

**Status**: draft | reviewed | confirmed | superseded — **`confirmed`** means the user approved scope; agents may continue without re-asking for review.
**Last Updated**: [YYYY-MM-DD]  
**Last reconciled with code**: [YYYY-MM-DD or "—"]  
**Related Spec**: [FeatureName.md](FeatureName.md)  
**Related TODO**: [FeatureName-TODO.md](FeatureName-TODO.md)

---

This file captures **what the agent believes the user wants the feature to be when complete** — identity, behavior, UI, and ties to existing work. **The agent writes this file first** (status `draft`). The user **reviews and corrects** it before implementation — they do not need to author it from scratch.

**Not sure what to ask the user?** See [`../help/IDEA_CAPTURE_TIPS.md`](../help/IDEA_CAPTURE_TIPS.md) — plain-language interview questions about UI, flows, and scope (no coding knowledge required on the user's part).

**Do not start implementation** while status is `draft` and assumptions remain unchecked, unless the user explicitly says to proceed.

---

## What this is

**Completeness over compression.** Elsewhere the pack stays lean; here do **not** drop details the user stated just to keep the section short — that defeats the purpose of Understanding. Reflect everything they want the finished feature *to be*: product identity, metaphors, constraints that define the thing, naming, and distinctions that matter. Prefer the user's words.

Length should match what the user said — not a telegram summary, and **not** padded essays, speculation, or invented detail. Omit only what belongs elsewhere (flows → **How it should work**; look → **UI / UX intent**; acceptance → **Done when**).

*Too thin (drops user detail):* “A role-specific view of the existing text editor.”

*Right size:* Same framing **plus** the details they actually gave — e.g. same editing core and document model; surrounding chrome for this workflow; what stays identical vs what changes; their metaphors / “feels like”; product-defining constraints (not implementation steps or filler).

---

## What this is NOT

**Identity boundaries for the finished feature** — what *kind of thing* this is not, even when Done when is fully met. Prevents category mistakes (e.g. treating a variant UI as a brand-new subsystem).

**Do put here:** wrong product category, wrong architecture, wrong ownership of a concern.

**Do not put here:** work that is still planned for this feature, phased later, or “not implemented yet.” Those belong in the **TODO**, **Current focus**, or the **spec** (roadmap / later goals) — not in this section. Understanding describes the destination, not the gap between now and later.

- NOT a new standalone [X] — it reuses [existing component/feature]
- NOT a [wrong category, e.g. file manager / second editor / OS desktop] — it is [correct category]
- NOT [common misinterpretation of *what the feature is*]

*Bad example (do not write this):* “NOT freeform multi-window Desktop Mode — that is long-term in the spec.” That is deferred work for the same feature, not an identity boundary.

*Good example:* “NOT a freeform multi-window desktop OS — Main Workspace is a document-centric layout (panels / side-by-side), not overlapping OS windows.” *(Only if that is truly never what this feature is meant to be.)*

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

*(Optional — only if clearer than the list.)* A small **Mermaid** flowchart for the happy path (or feature ↔ shared relationships) is fine. Agent decides whether it helps; do not add charts by default. Screenshots for UI look stay under **Visual references**.

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

The user should be able to judge "is this feature/component done?" without reading every TODO. Check a box only when **implemented code matches the destination** in this file / the spec — not when a partial or lookalike ship exists.

- [ ] [Observable outcome, e.g. "User can enter focus mode from document list and return with Esc"]
- [ ] [Another acceptance criterion]
- [ ] [Edge case that must work, e.g. "Save failure shows toast; text is not lost"]

Move checked items to **Confirmed with user** when verified in a build; update spec **Last reconciled with code** when shipped.

**On every Understanding update:** Re-check each `[x]` against code vs this file / the spec. **Uncheck** any item where the implementation no longer matches (partial, wrong behavior, or destination changed). Do the same for the related `-TODO.md` — uncheck completed tasks that are no longer true; add or reopen work in **Current focus** when needed. Note the correction under **Confirmed with user**.

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
- **What this is** — completeness over compression. Reflect everything the user stated about the finished feature; do not drop details to “keep docs short.” Do not pad or invent. Conciseness still applies to other sections and files.
- After updating, surface it to the user — the goal is to reveal *your* interpretation so they can correct misunderstandings early.
- When planning: include this file (or its path) in the plan **before** implementation steps.
- When the user corrects you (in chat or by editing the file), update this file immediately — especially **What this is** / **What this is NOT** (identity) and **Relationship to existing work**.
- **What this is NOT** = finished-feature identity only. Never list “not built yet,” “phase 2,” or “long-term in the spec” here — put those in TODO / Current focus / spec roadmap. Keep NOT bullets tight; put the user’s detail in **What this is**.
- **When updating this file:** Also open the related `-TODO.md` and re-verify **Done when** + TODO `[x]` items against code vs this file / the spec. **Uncheck** anything that no longer matches; refresh **Current focus** if work reopened. Do not leave premature “done” marks. This is scoped to *this* stem — not a repo-wide audit.
- When the user provides reference screenshots, persist under `docs/features/assets/`: copy from disk when a path exists; if only pasted in chat, ask the user to save the file into `assets/` or record similar/different from vision and note re-attach if needed. Link in **Visual references**.
- Set status to `confirmed` only after the user explicitly approves (or approves a plan that references this file). Then **graduate** durable content to the spec ([`Modular_Docs_Workflow.md`](agent/Modular_Docs_Workflow.md) §2) — Decisions, architecture, maturity (shared).
- **When status is `confirmed`:** read for context and implement from the TODO — **do not** ask the user to review this Understanding again unless scope changes or you set `superseded` / back to `draft`.
- If code or plan diverges from this file, set `superseded` or update **Last reconciled with code** after aligning spec and Understanding — do not leave both stale. Uncheck mismatched **Done when** / TODO items in the same pass.
- Read this file before implementation alongside the spec and TODO.
- **Mermaid:** optional. Add a small diagram only when flow or relationships are clearer that way than prose/steps. Your judgment — do not add charts to every Understanding “because we can.”

**Instructions for Humans**

- **You do not write this file from scratch** — the agent drafts it; you review.
- Skim the draft before approving a plan or agent work session — especially **What this is**. If something you said is missing, tell the agent; if it padded or invented, tell them to trim to what you meant.
- Correct wrong assumptions in **What this is** / **What this is NOT** — those sections are about *what the feature is meant to be*, not a backlog of unimplemented ideas. Edit the file directly or tell the agent what to fix; either way, the agent should update the file.
- If a **Done when** or TODO item is marked done but the build does not match what you meant, tell the agent — they should uncheck it and reopen the work.
- When scope looks right, set **Status** to `confirmed` (or tell the agent to) — that signals agents can continue without asking you to review this file again.
- Use [`../help/IDEA_CAPTURE_TIPS.md`](../help/IDEA_CAPTURE_TIPS.md) if you are stuck describing the idea — answer in chat; the agent translates into this file.
- Add reference screenshots to `docs/features/assets/` (or ask the agent to) and ensure **Visual references** notes what to copy vs what to change.
