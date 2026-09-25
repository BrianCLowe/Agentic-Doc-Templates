# [Feature or Shared Component Name]

> Copy under `docs/features/` or `docs/_shared/` (adjust paths). Do not edit this template unless the user asks.

**Last Updated**: [YYYY-MM-DD]  
**Related Understanding**: [FeatureName-Understanding.md](FeatureName-Understanding.md)  
**Related TODO**: [FeatureName-TODO.md](FeatureName-TODO.md)  
**Related Catalog** *(optional)*: [FeatureName-Catalog.md](FeatureName-Catalog.md)

*(Shared components only — omit for features if not useful)*  
**Maturity**: draft | usable | stable  
**Consumers**: [FeatureA.md](../features/FeatureA.md), …

---

**Humans:** This is the contract. How to read it: [`help/SCAFFOLDS.md`](../templates/help/SCAFFOLDS.md) · [`help/USAGE.md`](../templates/help/USAGE.md).

**Agents:** Fill-in blanks — not a tutorial. If context is thin, re-open [`agent/workflow/understanding.md`](../templates/agent/workflow/understanding.md) §2. Catalog: [`agent/workflow/extensions.md`](../templates/agent/workflow/extensions.md) §7.1. Decisions: [`agent/workflow/decisions.md`](../templates/agent/workflow/decisions.md). Operable Acceptance: [`agent/workflow/todos.md`](../templates/agent/workflow/todos.md) §5.3. build-first (no Understanding): [`agent/workflow/profile-standing.md`](../templates/agent/workflow/profile-standing.md) §0.1.

---

## Overview

[1–3 short paragraphs: what this is, why it exists, how it fits the project.]

---

## Architecture / Contract

[Stable design: modules, boundaries, data flow, public surface.]

- **Owns**: [what this piece is responsible for]
- **Does not own**: [explicit non-responsibilities]
- **Public API / entry points**: [functions, routes, classes, events — or link to code]

---

## Behavior (stable)

[Flows, modes, edge cases, and product rules that should stay true across refactors. User’s words. Do not invent.]

---

## Catalog *(optional — omit until a Catalog file exists)*

- **Rows:** [FeatureName-Catalog.md](FeatureName-Catalog.md)

---

## Decisions

| Date | Decision | Rationale |
|------|----------|-----------|
| YYYY-MM-DD | [Choice] | [Why — so a later session cannot silently undo it] |

---

## Dependencies

| Piece | Relationship |
|-------|--------------|
| [_shared/BlockEditor.md](../_shared/BlockEditor.md) | **Blocked by** until `usable` — needs "Expose shared editing API" |
| [OtherFeature.md](OtherFeature.md) | **Integrates with** — … |

---

## Acceptance

- [ ] [Observable outcome]
- [ ] [Another coarse outcome]
- [ ] [One critical edge that defines the product, if any]

---

## Visual references

| File | Similar (borrow) | Different (our idea) |
|------|------------------|----------------------|
| [assets/FeatureName-reference-label.png](assets/FeatureName-reference-label.png) | [what to borrow] | [what is ours] |

---

## Current status *(optional, keep short)*

- **In progress**: [one line]
- **Blocked by**: [link to TODO item or shared maturity]
- **Last reconciled with code**: [YYYY-MM-DD]
