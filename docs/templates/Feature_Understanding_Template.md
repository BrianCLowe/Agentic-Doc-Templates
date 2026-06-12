# [Feature Name] — Understanding

> Never edit this template unless the user asks you to.

**Status**: draft | reviewed | confirmed  
**Last Updated**: [YYYY-MM-DD]  
**Related Spec**: [FeatureName.md](FeatureName.md)  
**Related TODO**: [FeatureName-TODO.md](FeatureName-TODO.md)

---

This file captures **what the agent believes the user wants** — scope, behavior, UI, and ties to existing work. The user reads and corrects it **before implementation**, not after.

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
- Reference: [link to screenshot, Figma, or `OtherFeature.md` section if similar]

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

- Create or update this file when the user **discusses**, **plans**, or **scopes** a feature — before writing implementation code.
- After updating, set status to `draft` and surface it to the user for review.
- When planning: include this file (or its path) in the plan so the user can correct misunderstandings early.
- If the user corrects you, update this file immediately — especially **What this is NOT** and **Relationship to existing work**.
- Set status to `confirmed` only after the user explicitly approves (or approves a plan that references this file).
- Read this file before implementation alongside the spec and TODO.

**Instructions for Humans**

- Skim this before approving a plan or agent work session.
- Fix wrong assumptions in **What this is NOT** — that section prevents the "completely new feature" mistake.
