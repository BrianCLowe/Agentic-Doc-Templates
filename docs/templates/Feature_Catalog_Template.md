# [Feature or Shared Component Name] — Catalog

> Never edit this template unless the user asks you to. Optional sibling for **list-heavy** stems. Create under `docs/features/` or `docs/_shared/`. Spec owns rules/identity; this file owns **design-intent rows**. Humans: [`help/SCAFFOLDS.md`](../templates/help/SCAFFOLDS.md). Agents: [`agent/workflow/extensions.md`](../templates/agent/workflow/extensions.md) §7.1.

**Last Updated**: [YYYY-MM-DD]  
**Related Spec**: [FeatureName.md](FeatureName.md)  
**Related Understanding**: [FeatureName-Understanding.md](FeatureName-Understanding.md)  
**Related TODO**: [FeatureName-TODO.md](FeatureName-TODO.md)

---

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

Fill the row table. Procedure: [`workflow/extensions.md`](../templates/agent/workflow/extensions.md) §7.1.

**Instructions for Humans**

- Skim readiness to see what is invented vs agreed vs shipped.
- Correct wrong rows in chat; ask the agent to update this file (and the spec pointer if needed).
