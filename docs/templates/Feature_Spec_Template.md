# [Feature or Shared Component Name]

> Copy under `docs/features/` or `docs/_shared/` (adjust paths). Do not edit this template unless the user asks.
>
> **Humans:** [`help/SCAFFOLDS.md`](help/SCAFFOLDS.md) · [`help/USAGE.md`](help/USAGE.md). **Agents:** fill blanks; re-open [`agent/workflow/understanding.md`](agent/workflow/understanding.md) §2 (graduation) or [`agent/workflow/profile-standing.md`](agent/workflow/profile-standing.md) §0.1 (`ship-first`) if context is thin.

**Last Updated**: [YYYY-MM-DD]  
**Related Understanding**: [FeatureName-Understanding.md](FeatureName-Understanding.md)  
**Related TODO**: [FeatureName-TODO.md](FeatureName-TODO.md)  
**Related Catalog** *(optional — list-heavy / Workflow §7.1)*: [FeatureName-Catalog.md](FeatureName-Catalog.md)

*(Shared components only — omit for features if not useful)*  
**Maturity**: draft | usable | stable  
**Consumers**: [FeatureA.md](../features/FeatureA.md), … *(who depends on this shared piece)*

---

> **Contract home** (not Understanding). Unbounded row registries → sibling [`Feature_Catalog_Template.md`](Feature_Catalog_Template.md) (Workflow §7.1).

## Overview

[1–3 short paragraphs: what this is, why it exists, how it fits the project.]

---

## Architecture / Contract

[Stable design: modules, boundaries, data flow, public surface. What callers can rely on. Include enough that an implementer does not have to re-derive from chat.]

- **Owns**: [what this piece is responsible for]
- **Does not own**: [explicit non-responsibilities]
- **Public API / entry points**: [functions, routes, classes, events — or link to code]

*(Optional — only if clearer than bullets.)* A small **Mermaid** diagram for module boundaries or data flow is fine. Agent decides; one chart max here unless the user asks for more. Not required.

---

## Behavior (stable)

**Contract completeness here — not in Understanding.** Understanding holds shape only (no How-it-should-work section). Put durable flows, modes, edge cases, and product rules the user (or confirmed decisions) established **here**. Prefer the user’s words for product rules; do not invent. Do **not** omit confirmed contract detail to “keep the pack lean” — lean applies to Understanding and to avoiding filler, not to dropping behavior callers need. **In-scope surfaces named here** need covering TODOs on this stem or the owning stem already on the map (Workflow §5.4) — a complete spec is not a reason to skip the backlog.

[Behavior that should stay true across refactors.]

---

## Catalog *(optional)*

When this stem is **list-heavy** (growing row registries), keep **identity and rules here** and put rows in the sibling catalog:

- **Rows:** [FeatureName-Catalog.md](FeatureName-Catalog.md) — design-intent table + readiness (`stub` \| `sketched` \| `design-ready` \| `in-code`)
- **This section:** one short pointer only — do not re-paste the full table.

Omit this section until a Catalog exists. Creating a Document Map Catalog link requires the file on disk the same turn.

---

## Decisions

Record **why** — Understanding-review tradeoffs **and** implement/polish preference corrections (same turn — Workflow §10). Cross-cutting decisions that affect multiple features can also go in `docs/decisions/`.

| Date | Decision | Rationale |
|------|----------|-----------|
| YYYY-MM-DD | [Choice] | [Why — so a later session cannot silently undo it] |

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

For **user/operator-facing** stems, include ≥1 **operable** outcome (human can exercise the happy path via UI, CLI, or documented smoke) — not only library/test invariants. Pure library stems may omit that (Workflow §5.3).

**Bridge to TODOs (Workflow §5.3):** Open operable Acceptance lines mean remaining product work unless a TODO already covers them. Do **not** treat “all domain TODOs `[x]`” as stem complete while these stay unchecked. When work clearly meets a line, check it the same turn. If Architecture/TODOs are library-first on purpose, High Priority / Current focus must say so (**library foundation first · exercise path: …**) — product Overview alone is not the bridge. Missing UI mockups does **not** remove operable outcomes — agents should still scaffold + wire a minimal surface (or CLI/smoke) unless you explicitly said library-only / design-first.

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

Fill the sections above. Procedure is **not** in this scaffold — if context is thin, re-open [`workflow/understanding.md`](agent/workflow/understanding.md) §2, [`workflow/decisions.md`](agent/workflow/decisions.md) §10, [`workflow/todos.md`](agent/workflow/todos.md) §5.3. Optional role: [`agent/roles/doc-graduate.md`](agent/roles/doc-graduate.md).

**Instructions for Humans**

This is the contract home after you confirm Understanding shape (or from day one under **ship-first**). How to read it: [`help/SCAFFOLDS.md`](help/SCAFFOLDS.md).
