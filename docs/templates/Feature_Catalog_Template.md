# [Feature or Shared Component Name] — Catalog

> Never edit this template unless the user asks you to. Optional sibling for **list-heavy** stems (Workflow §7.1). Create from this file under `docs/features/` or `docs/_shared/`. Spec owns rules/identity; this file owns **design-intent rows**.

**Last Updated**: [YYYY-MM-DD]  
**Related Spec**: [FeatureName.md](FeatureName.md)  
**Related Understanding**: [FeatureName-Understanding.md](FeatureName-Understanding.md)  
**Related TODO**: [FeatureName-TODO.md](FeatureName-TODO.md)

---

> **Not Understanding. Not TODO. Not Acceptance.** Row registry only. Prefer stable **ids** for cross-links. Runtime/code-first projects: mark `in-code` when implemented; docs stay design intent until then.

## Readiness legend

| Value | Meaning |
|-------|---------|
| `stub` | Named / placeholder only |
| `sketched` | Enough to discuss; not locked |
| `design-ready` | Agreed for implementation |
| `in-code` | Present in source of truth (note path if useful) |

## Rows

| id | display | era / tier | depends-on | unlock | readiness | notes |
|----|---------|------------|------------|--------|-----------|-------|
| `example.item` | Example Item | early | — | material goal / tech id | sketched | [short note] |

*(Add columns only when the stem needs them — e.g. `fuel`, `stillfold`, `in-code`. Keep the table scannable.)*

## Cross-links

| This id | Needs |
|---------|--------|
| `example.item` | `other.catalog_id` |

---

## Instructions for AI Agents

- Do **not** put catalog rows in `-Understanding.md`.
- Do **not** treat this file as the work queue — tasks stay in `-TODO.md`.
- When adding a Document Map **Catalog** cell, create this file the same turn.
- Prefer updating an existing row’s **readiness** over inventing parallel lists in the spec.
- Code-first: after implementing a row, set readiness `in-code` and optionally note source path — do not silently diverge.

**Instructions for Humans**

- Skim readiness to see what is invented vs agreed vs shipped.
- Correct wrong rows in chat; ask the agent to update this file (and the spec pointer if needed).
