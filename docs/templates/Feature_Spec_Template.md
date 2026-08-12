# [Feature or Shared Component Name]

> Never edit this template unless the user asks you to. Use under `docs/features/` for features or `docs/_shared/` for shared components (adjust paths). Under **`prevent`**, grow from [`Feature_Understanding_Template.md`](Feature_Understanding_Template.md) after Understanding is `confirmed` ([`workflow/understanding.md`](agent/workflow/understanding.md) §2). Under **`ship-first`**, this file is the contract home from day one ([`workflow/profile-standing.md`](agent/workflow/profile-standing.md) §0.1).

**Last Updated**: [YYYY-MM-DD]  
**Related Understanding**: [FeatureName-Understanding.md](FeatureName-Understanding.md)  
**Related TODO**: [FeatureName-TODO.md](FeatureName-TODO.md)  
**Related Catalog** *(optional — list-heavy / Workflow §7.1)*: [FeatureName-Catalog.md](FeatureName-Catalog.md)

*(Shared components only — omit for features if not useful)*  
**Maturity**: draft | usable | stable  
**Consumers**: [FeatureA.md](../features/FeatureA.md), … *(who depends on this shared piece)*

---

> **Contract home:** Understanding stays thin (shape / guardrails — including product-defining surface identity). **This file** holds durable behavior, **module/API architecture**, and **Visual references**. Product surface locked in Understanding (“one manuscript feel”) is not reopened here as an interim; deepen *how* it works. A short Understanding is **not** a reason to write a short spec — do not compress contract detail to match Understanding’s length. **Do not** dump unbounded content registries (units, fuels, tech goals, recipes…) into Behavior — use a sibling [`Feature_Catalog_Template.md`](Feature_Catalog_Template.md) / `-Catalog.md` (Workflow §7.1).

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
| YYYY-MM-DD | [e.g. Reuse existing editor core, no second engine] | [User confirmed in Understanding review] |
| YYYY-MM-DD | [e.g. Proximity fade for seam chrome, not divider-hover sprout] | [User preference during polish — avoid “improving” back to always-on] |
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

Graduation / anti-compression: [`workflow/understanding.md`](agent/workflow/understanding.md) §2. Optional role: [`agent/roles/doc-graduate.md`](agent/roles/doc-graduate.md).

- **Do not** use this as a substitute for `-Understanding.md` during scoping — draft Understanding first (shape only); populate this file after `confirmed`.
- **Graduate** the durable contract here (Workflow §2): synthesize Understanding **plus** conversation / decisions — do not only copy thin Understanding. Do not thin Architecture / Behavior / Acceptance to match Understanding’s length. Deepen *how* the confirmed product surface works — do not reopen a fighting interim architecture as the contract.
- Acceptance + Visual references live **here**; work queue in `-TODO.md`; row registries in optional `-Catalog.md` (not Understanding). Screenshots → this file’s **Visual references**, not Understanding.
- On drift: update this file **or** reconcile Understanding — do not silently diverge. Shared **Maturity** stays accurate. Lasting choices → **Decisions** (or `docs/decisions/` if cross-cutting). Preference corrections during implement/polish → **same-turn** Decisions rows + fix stale Behavior / Acceptance / Visual refs (Workflow §10) — do not wait for a session wrap.
- **Mermaid:** only when clearer than prose; one small chart max; never decorative.

**Instructions for Humans**

- Skim this for **what we're actually building** after you confirm Understanding **shape** — this is the contract home; Understanding was only guardrails.
- Fix wrong **Decisions** or **Maturity** when the agent misjudges readiness; tell the agent to update the spec. If durable behavior, acceptance outcomes, or visual refs you agreed are missing here, tell the agent to add them (do not expect them to live only in Understanding).
- Skim **Visual references** before UI work — similar vs different is the authority for what to borrow vs change.
- **Acceptance** is the coarse “done” picture; the day-to-day checklist is the **TODO**. Open operable Acceptance + domain-only TODOs = incomplete bridge (Workflow §5.3) — tell the agent if the stem should be library-only, phased, or needs surface TODOs.
