# [Feature or Shared Component Name]

> Never edit this template unless the user asks you to. Use under `docs/features/` for features or `docs/_shared/` for shared components (adjust paths). Create from [`Feature_Understanding_Template.md`](Feature_Understanding_Template.md) after Understanding is `confirmed` — see [`Modular_Docs_Workflow.md`](agent/Modular_Docs_Workflow.md) §2.

**Last Updated**: [YYYY-MM-DD]  
**Related Understanding**: [FeatureName-Understanding.md](FeatureName-Understanding.md)  
**Related TODO**: [FeatureName-TODO.md](FeatureName-TODO.md)

*(Shared components only — omit for features if not useful)*  
**Maturity**: draft | usable | stable  
**Consumers**: [FeatureA.md](../features/FeatureA.md), … *(who depends on this shared piece)*

---

> **Contract home:** Understanding stays thin (shape / guardrails). **This file** holds durable behavior, architecture, APIs, and **Visual references**. A short Understanding is **not** a reason to write a short spec — do not compress contract detail to match Understanding’s length.

## Overview

[1–3 short paragraphs: what this is, why it exists, how it fits the project. High-level only — depth belongs in Architecture / Behavior below.]

*Example (shared): Reusable block-based text editing core — API, document model, and save hooks. Role-specific UIs wrap this; they do not reimplement editing.*

---

## Architecture / Contract

[Stable design: modules, boundaries, data flow, public surface. What callers can rely on. Include enough that an implementer does not have to re-derive from chat.]

- **Owns**: [what this piece is responsible for]
- **Does not own**: [explicit non-responsibilities]
- **Public API / entry points**: [functions, routes, classes, events — or link to code]

*(Optional — only if clearer than bullets.)* A small **Mermaid** diagram for module boundaries or data flow is fine. Agent decides; one chart max here unless the user asks for more. Not required.

---

## Behavior (stable)

**Contract completeness here — not in Understanding.** Understanding holds shape only (no How-it-should-work section). Put durable flows, modes, edge cases, and product rules the user (or confirmed decisions) established **here**. Prefer the user’s words for product rules; do not invent. Do **not** omit confirmed contract detail to “keep the pack lean” — lean applies to Understanding and to avoiding filler, not to dropping behavior callers need.

[Behavior that should stay true across refactors.]

---

## Decisions

Record **why** — especially choices made when confirming Understanding shape or later tradeoffs. Cross-cutting decisions that affect multiple features can also go in `docs/decisions/`.

| Date | Decision | Rationale |
|------|----------|-----------|
| YYYY-MM-DD | [e.g. Reuse existing editor core, no second engine] | [User confirmed in Understanding review] |
| YYYY-MM-DD | [e.g. SQLite for v1] | [Scope / simplicity] |

---

## Dependencies

| Piece | Relationship |
|-------|--------------|
| [_shared/BlockEditor.md](../_shared/BlockEditor.md) | **Blocked by** until `usable` — needs "Expose shared editing API" |
| [OtherFeature.md](OtherFeature.md) | **Integrates with** — … |

*(Shared components: list **Consumers** here or in frontmatter — features that must not break when this API changes.)*

---

## Acceptance *(coarse outcomes — not a TODO twin)*

**Lives here, not in Understanding.** Few observable outcomes (usually **3–7**) that mean the contract destination is met. **Not** a mirror of High Priority in `-TODO.md` — the living work checklist is the TODO only. Prefer plain bullets; optional checkboxes only if useful when reconciling with code (do not dual-maintain every TODO row here).

- [ ] [Observable outcome, e.g. "User can enter focus mode from document list and return with Esc"]
- [ ] [Another coarse outcome]
- [ ] [One critical edge that defines the product, if any]

Update when product definition changes; uncheck if code no longer matches. Task breakdown stays in the TODO.

---

## Visual references

**Lives here (the contract), not in Understanding.** Store screenshots in `docs/features/assets/`, `docs/_shared/assets/`, or `docs/reference/visuals/`. Link so vision-capable agents can reuse them in later sessions. Always note **similar** vs **different** — a reference is not a pixel-perfect copy target.

| File | Similar (borrow) | Different (our idea) |
|------|------------------|----------------------|
| [assets/FeatureName-reference-label.png](assets/FeatureName-reference-label.png) | [e.g. full-width text, minimal chrome] | [e.g. our Save top-left; no slash menu] |
| [assets/FeatureName-our-existing-panel.png](assets/FeatureName-our-existing-panel.png) | [match this panel from our app] | [new feature hides sidebar] |

*Example row:* `[assets/RoleEditor-notion-focus.png](assets/RoleEditor-notion-focus.png)` — similar: focus layout; different: reuse our editor toolbar.

Omit this section only when there are no visual references yet — add it when the first screenshot arrives (including during Understanding draft; the stub spec can hold the table early).

---

## Current status *(optional, keep short)*

- **In progress**: [one line]
- **Blocked by**: [link to TODO item or shared maturity]
- **Last reconciled with code**: [YYYY-MM-DD] *(update when spec matches shipped behavior)*

---

## Instructions for AI Agents

- **Do not** treat this as a substitute for `-Understanding.md` during scoping — draft Understanding first (shape only); populate or update this spec after `confirmed`.
- After Understanding is confirmed, **graduate** the durable **contract** into this file ([`Modular_Docs_Workflow.md`](agent/Modular_Docs_Workflow.md) §2). Synthesize from confirmed Understanding **plus** conversation / decisions / already-agreed behavior — **do not** only copy the thin Understanding and stop. Spec may (and should) hold detail that was never in Understanding. Move any old Understanding **Done when** lists into **Acceptance** here.
- **Anti-compression:** Understanding’s brevity is intentional. Do not thin Architecture / Behavior / Acceptance to match it. Omit speculation and filler; keep confirmed contract detail.
- When implementation diverges from the spec, update this file **or** flag Understanding as needing reconciliation — do not silently drift.
- **Shared components**: keep **Maturity** accurate (`draft` → foundation incomplete; `usable` → features may integrate; `stable` → breaking changes need explicit discussion).
- Record non-obvious **Decisions** when the user chooses between options — not every TODO item, only choices with lasting impact.
- When the user provides UI screenshots, persist under `assets/` and maintain **Visual references** here (similar vs different). Do not put the screenshot table on `-Understanding.md`.
- Do **not** put a **Done when** section on `-Understanding.md` — acceptance lives here; work queue in `-TODO.md`.
- **Mermaid:** add only when a diagram communicates architecture/flow better than a short paragraph. Prefer one small chart; skip if prose is enough. Never add decorative diagrams.

**Instructions for Humans**

- Skim this for **what we're actually building** after you confirm Understanding **shape** — this is the contract home; Understanding was only guardrails.
- Fix wrong **Decisions** or **Maturity** when the agent misjudges readiness; tell the agent to update the spec. If durable behavior, acceptance outcomes, or visual refs you agreed are missing here, tell the agent to add them (do not expect them to live only in Understanding).
- Skim **Visual references** before UI work — similar vs different is the authority for what to borrow vs change.
- **Acceptance** is the coarse “done” picture; the day-to-day checklist is the **TODO**.
