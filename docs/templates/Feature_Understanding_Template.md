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

**Feature shape, not the spec.** Capture **identity-defining** detail the user stated: category, metaphors, naming, “feels like,” ownership, and constraints that decide *what kind of thing* this is. Prefer the user’s words. Include brief feel/layout only when it defines the product (one short clause or bullet) — not a UI walkthrough.

**Product-defining surface / architecture belongs here when it decides identity** — e.g. “one continuous manuscript surface; seams are visual; notes stay separate storage.” That is shape, not a module diagram. Once confirmed, agents must plan/build that **target** (agent timescale) — not park a fighting interim as the paved path.

Do **not** omit identity detail for brevity — and do **not** expand into flows, module/API architecture, edge cases, acceptance checklists, or step-by-step behavior (work → **TODO**; durable contract, Behavior, Acceptance, Visual references, module boundaries → **spec**).

Length should match the shape detail the user gave — not a telegram summary, and **not** a parallel feature narrative or padded essay. Do not pad, speculate, or invent.

*Too thin (drops shape):* “A role-specific view of the existing text editor.”

*Right size (shape):* Same framing **plus** identity detail they actually gave — e.g. same editing core (not a second engine); one continuous surface vs N separate editors; chrome differs for this workflow; metaphors / “feels like”; product-defining constraints. Not implementation steps, prop tables, happy-path numbered flows, or a full behavior rewrite.

*Wrong size (mini-spec):* Restating Core Behavior, API/prop tables, scene-break matrices, acceptance checklists, How-it-should-work flows, or every edge case — that belongs in the **spec** / **TODO**.

---

## What this is NOT

**Identity boundaries for the finished feature** — what *kind of thing* this is not, even when the feature is fully built. Prevents category mistakes (e.g. treating a variant UI as a brand-new subsystem). These are the primary **guardrails** the user confirms.

**Do put here:** wrong product category, wrong **product surface / architecture identity**, wrong ownership of a concern (e.g. NOT N independent editors with caret bridging when the product is one manuscript feel).

**Do not put here:** work that is still planned for this feature, phased later, or “not implemented yet.” Those belong in the **TODO**, **Current focus**, or the **spec** (roadmap / later goals) — not in this section. Understanding describes destination **shape**, not the gap between now and later. Do not use this section to excuse shipping a known-wrong interim (“NOT the final single-doc editor yet”).

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

Full procedure: [`workflow/understanding.md`](agent/workflow/understanding.md) §4 (shape) and §2 (graduation) — index: [`Modular_Docs_Workflow.md`](agent/Modular_Docs_Workflow.md). Optional role: [`agent/roles/understanding-author.md`](agent/roles/understanding-author.md).

1. **Write this file first** when scoping — before implementation code. Shape sections only (above); not a second spec.
2. Draft from the conversation (or a short [`IDEA_CAPTURE_TIPS.md`](../help/IDEA_CAPTURE_TIPS.md) interview if vague). Status `draft`. Capture product-defining surface/architecture identity in is / is not when the user stated it (or as Assumptions). **Show the user** and ask them to confirm **shape** (is / is not + Assumptions) — not the full contract.
3. **On update:** relocate trimmed contract detail into the related **spec** if missing, then remove it here; re-check this stem’s `-TODO.md` and **uncheck** mismatches (Workflow §4). Screenshots → spec **Visual references**.
4. Set `confirmed` only after the user approves **shape**. Then graduate contract to the spec (Workflow §2). When `confirmed`, do **not** re-ask for Understanding review unless shape/scope changes. **De-confirm / additive vs shape:** follow [`agent/workflow/understanding.md`](agent/workflow/understanding.md) §4 (source of truth) — do not invent a local rule. Plans/TODOs must target that shape — not human-sprint interim architectures ([`Agent_Timescale_Planning_Rule.mdc`](agent/Agent_Timescale_Planning_Rule.mdc)).
5. **Mermaid / flows / module diagrams:** never on Understanding — put on the **spec** if needed.

**Instructions for Humans**

- **You do not write this file from scratch** — the agent drafts it; you review.
- **Confirm shape, not the full spec.** Focus on **What this is / is NOT**, **Relationship**, and **Assumptions** — including product-defining surface (“feels like one document,” same engine, etc.). You do **not** need to approve flows, UI walkthroughs, module/API architecture, or acceptance here.
- If something you said about *what kind of thing this is* is missing, tell the agent; if it padded into a mini-spec, tell them to trim to shape.
- Correct wrong assumptions in **What this is** / **What this is NOT** — those sections are guardrails for *what the feature is meant to be*, not a backlog of unimplemented ideas.
- If a TODO item is marked done but the build does not match what you meant, tell the agent — they should uncheck it and reopen the work.
- When **shape** looks right, set **Status** to `confirmed` (or tell the agent to).
- Use [`../help/IDEA_CAPTURE_TIPS.md`](../help/IDEA_CAPTURE_TIPS.md) if you are stuck describing the idea — answer in chat; the agent translates into this file.
- Screenshots go on the **spec** **Visual references**, not here.
