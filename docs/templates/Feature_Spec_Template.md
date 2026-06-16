# [Feature or Shared Component Name]

> Never edit this template unless the user asks you to. Use under `docs/features/` for features or `docs/_shared/` for shared components (adjust paths). Create from [`Feature_Understanding_Template.md`](Feature_Understanding_Template.md) after Understanding is `confirmed` — see [`Modular_Docs_Workflow.md`](Modular_Docs_Workflow.md) §2.

**Last Updated**: [YYYY-MM-DD]  
**Related Understanding**: [FeatureName-Understanding.md](FeatureName-Understanding.md)  
**Related TODO**: [FeatureName-TODO.md](FeatureName-TODO.md)

*(Shared components only — omit for features if not useful)*  
**Maturity**: draft | usable | stable  
**Consumers**: [FeatureA.md](../features/FeatureA.md), … *(who depends on this shared piece)*

---

## Overview

[1–3 short paragraphs: what this is, why it exists, how it fits the project. Durable facts — not pre-build negotiation. That lives in Understanding.]

*Example (shared): Reusable block-based text editing core — API, document model, and save hooks. Role-specific UIs wrap this; they do not reimplement editing.*

---

## Architecture / Contract

[Stable design: modules, boundaries, data flow, public surface. What callers can rely on.]

- **Owns**: [what this piece is responsible for]
- **Does not own**: [explicit non-responsibilities]
- **Public API / entry points**: [functions, routes, classes, events — or link to code]

---

## Behavior (stable)

[Behavior that should stay true across refactors. Detailed pre-build flows stay in Understanding until confirmed, then distill the durable parts here.]

---

## Decisions

Record **why** — especially choices made during Understanding review. Cross-cutting decisions that affect multiple features can also go in `docs/decisions/`.

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

## Current status *(optional, keep short)*

- **In progress**: [one line]
- **Blocked by**: [link to TODO item or shared maturity]
- **Last reconciled with code**: [YYYY-MM-DD] *(update when spec matches shipped behavior)*

---

## Instructions for AI Agents

- **Do not** treat this as a substitute for `-Understanding.md` during scoping — draft Understanding first; populate or update this spec after `confirmed`.
- After Understanding is confirmed, **graduate** durable architecture, contracts, and decisions from Understanding into this file ([`Modular_Docs_Workflow.md`](Modular_Docs_Workflow.md) §2).
- When implementation diverges from the spec, update this file **or** flag Understanding as needing reconciliation — do not silently drift.
- **Shared components**: keep **Maturity** accurate (`draft` → foundation incomplete; `usable` → features may integrate; `stable` → breaking changes need explicit discussion).
- Record non-obvious **Decisions** when the user chooses between options — not every TODO item, only choices with lasting impact.

**Instructions for Humans**

- Skim this for **what we're actually building** after you confirm Understanding — not for first-pass intent review.
- Fix wrong **Decisions** or **Maturity** when the agent misjudges readiness; tell the agent to update the spec.
