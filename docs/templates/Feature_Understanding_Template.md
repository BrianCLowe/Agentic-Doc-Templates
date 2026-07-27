# [Feature or Shared Component Name] — Understanding

> Never edit this template unless the user asks you to. Use under `docs/features/` for features or `docs/_shared/` for shared components (adjust Related Spec/TODO paths). Shared components get this file by default unless the user excepted it.

**Status**: draft | reviewed | confirmed | superseded — **`confirmed`** means the user approved **feature shape** (is / is not + Assumptions); agents may continue without re-asking for review.
**Last Updated**: [YYYY-MM-DD]  
**Last reconciled with code**: [YYYY-MM-DD or "—"]  
**Related Spec**: [FeatureName.md](FeatureName.md)  
**Related TODO**: [FeatureName-TODO.md](FeatureName-TODO.md)

---

> **For humans reviewing this file:** You are confirming **general feature shape** — guardrails (what it is / isn’t), **Relationship to existing work**, and open **Assumptions**. This is **not** a full spec review and **not** a completion checklist. Flows, UI specs, acceptance, and the work backlog live in the **spec** and **TODO**. Spec detail missing here is normal and expected.

This file is the agent’s model of **feature shape** — identity and boundaries — so you can catch category mistakes before build. **The agent writes this file first** (status `draft`). The user **reviews and corrects** shape — they do not need to author it from scratch, and they should **not** treat it as the durable contract or the definition of done.

**Not sure what to ask the user?** See [`../help/IDEA_CAPTURE_TIPS.md`](../help/IDEA_CAPTURE_TIPS.md) — plain-language interview questions about UI, flows, and scope (no coding knowledge required on the user's part).

**Do not start implementation** while status is `draft` and assumptions remain unchecked, unless the user explicitly says to proceed.

---

## What this is

**Feature shape, not the spec.** Capture **identity-defining** detail the user stated: category, metaphors, naming, “feels like,” ownership, and constraints that decide *what kind of thing* this is. Prefer the user’s words. Include brief feel/layout only when it defines the product (one short clause or bullet) — not a UI walkthrough. Do **not** omit those for brevity — and do **not** expand into flows, architecture, APIs, edge cases, acceptance checklists, or step-by-step behavior (work → **TODO**; durable contract, Behavior, Acceptance, Visual references → **spec**).

Length should match the shape detail the user gave — not a telegram summary, and **not** a parallel feature narrative or padded essay. Do not pad, speculate, or invent.

*Too thin (drops shape):* “A role-specific view of the existing text editor.”

*Right size (shape):* Same framing **plus** identity detail they actually gave — e.g. same editing core (not a second engine); chrome differs for this workflow; metaphors / “feels like”; product-defining constraints. Not implementation steps, prop tables, happy-path numbered flows, or a full behavior rewrite.

*Wrong size (mini-spec):* Restating Core Behavior, API/prop tables, scene-break matrices, acceptance checklists, How-it-should-work flows, or every edge case — that belongs in the **spec** / **TODO**.

---

## What this is NOT

**Identity boundaries for the finished feature** — what *kind of thing* this is not, even when the feature is fully built. Prevents category mistakes (e.g. treating a variant UI as a brand-new subsystem). These are the primary **guardrails** the user confirms.

**Do put here:** wrong product category, wrong architecture, wrong ownership of a concern.

**Do not put here:** work that is still planned for this feature, phased later, or “not implemented yet.” Those belong in the **TODO**, **Current focus**, or the **spec** (roadmap / later goals) — not in this section. Understanding describes destination **shape**, not the gap between now and later.

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

## Assumptions (needs user confirmation)

- [ ] [Assumption the agent is making]
- [ ] [Another assumption]

When the user confirms or corrects an item, move it to **Confirmed with user** and update the relevant section above. Answering Assumptions is part of **shape** confirmation — not a full spec sign-off.

---

## Confirmed with user

Short correction / confirmation notes only — not a parking lot for contract prose. Relocated behavior/API/acceptance/UI detail goes in the **spec**; work items go in the **TODO**.

- [YYYY-MM-DD] — [What was confirmed or corrected, e.g. "Separate UI only — same editor core as BlockEditor"]

---

## Instructions for AI Agents

- **Write this file first** when the user discusses, plans, or scopes a feature or shared component — before writing implementation code.
- This file is **shape / guardrails** only: **What this is / is NOT**, **Relationship**, **Assumptions**, **Confirmed with user**. Not a second spec, not flows, not UI walkthroughs, not Done when.
- Draft from the conversation (or a short interview using [`../help/IDEA_CAPTURE_TIPS.md`](../help/IDEA_CAPTURE_TIPS.md) if vague). Set status to `draft` and **show the user the file** for review.
- **What this is** — feature shape, not the spec. Keep identity-defining user detail (including brief “feels like” if they said it); do not drop it for brevity; do not pad into a mini-spec.
- Do **not** add **How it should work**, **UI / UX intent**, **Visual references**, or **Done when** sections — those belong on the **spec** (Behavior / Visual references / Acceptance) or **TODO**.
- After updating, surface it to the user — reveal *your* interpretation of **shape** so they can correct category mistakes early.
- When planning: include this file (or its path) in the plan **before** implementation steps, and state that confirmation is for **shape**, not the full contract.
- When the user corrects you (in chat or by editing the file), update this file immediately — especially **What this is** / **What this is NOT** and **Relationship to existing work**.
- **What this is NOT** = finished-feature identity only. Never list “not built yet,” “phase 2,” or “long-term in the spec” here — put those in TODO / Current focus / spec roadmap. Keep NOT bullets tight; put the user’s shape detail in **What this is**.
- **Relocate, don’t delete:** When trimming this file to shape, any durable contract detail that does **not** belong here (flows, How-it-should-work, UI/UX sections, APIs, Visual references, Done when / acceptance lists) must be **moved into the related spec** if missing there — then remove it from Understanding. Do not drop user-stated or already-documented contract detail on the floor. Do not invent new contract content while trimming.
- **Confirmed with user** notes stay short (what was corrected). Do not park relocated contract prose there — put it in the spec.
- **When updating this file:** Also open the related `-TODO.md` and re-verify TODO `[x]` items against code vs the updated Understanding / spec destination. **Uncheck** anything that no longer matches; refresh **Current focus** if work reopened. Do not leave premature “done” marks. This is scoped to *this* stem — not a repo-wide audit.
- When the user provides reference screenshots, persist under `docs/features/assets/` (or `_shared/assets/`) and link in the related **spec** **Visual references**. Optionally one short “feels like” clause under **What this is** if it defines shape.
- Set status to `confirmed` only after the user explicitly approves **shape** (or approves a plan that references this file for shape). Then **graduate** durable contract content to the spec ([`Modular_Docs_Workflow.md`](agent/Modular_Docs_Workflow.md) §2).
- **When status is `confirmed`:** read for guardrails and implement from the TODO/spec — **do not** ask the user to review this Understanding again unless scope/shape changes or you set `superseded` / back to `draft`.
- If code or plan diverges from this file’s **shape**, set `superseded` or update **Last reconciled with code** after aligning spec and Understanding — do not leave both stale. Uncheck mismatched TODO items in the same pass.
- Read this file before implementation alongside the spec and TODO — Understanding for guardrails; spec for contract + visuals + acceptance; TODO for work.
- **Mermaid:** do not add flowcharts to Understanding — put durable flow diagrams on the **spec** if needed.

**Instructions for Humans**

- **You do not write this file from scratch** — the agent drafts it; you review.
- **Confirm shape, not the full spec.** Focus on **What this is / is NOT**, **Relationship**, and **Assumptions**. You do **not** need to approve flows, UI walkthroughs, architecture, or acceptance here.
- If something you said about *what kind of thing this is* is missing, tell the agent; if it padded into a mini-spec, tell them to trim to shape.
- Correct wrong assumptions in **What this is** / **What this is NOT** — those sections are guardrails for *what the feature is meant to be*, not a backlog of unimplemented ideas.
- If a TODO item is marked done but the build does not match what you meant, tell the agent — they should uncheck it and reopen the work.
- When **shape** looks right, set **Status** to `confirmed` (or tell the agent to).
- Use [`../help/IDEA_CAPTURE_TIPS.md`](../help/IDEA_CAPTURE_TIPS.md) if you are stuck describing the idea — answer in chat; the agent translates into this file.
- Screenshots go on the **spec** **Visual references**, not here.
