> **Workflow module.** Open from the [workflow index](../Modular_Docs_Workflow.md) when drafting or confirming **whole-product** identity / the end-state picture. Feature is / is not stays in [`understanding.md`](understanding.md) §4.

# Product vision *(whole-product end-state)*

## 4.5 Product vision

Live file: **`docs/Product-Vision.md`** (from [`Product_Vision_Template.md`](../../Product_Vision_Template.md)).

The Document Map + per-feature Understandings can be complete and still miss **what the product is**. This file is the cohesive **end-state picture** — one target the stems must fit. It is **not** a second spec, **not** a feature checklist, and **not** Master Index §1 (that stays a short overview + map).

**Lock gate** (obvious defaults vs real forks; examples are not the target): [`understanding.md`](understanding.md) §4. Do not restate it here. Empty Assumptions is success.

### When to create

| Profile | Create `Product-Vision.md` |
|---------|----------------------------|
| **`prevent`** | **Yes** at bootstrap / first live-docs build (even one stem — the product still has an end state) |
| **`balanced`** | When **2+ feature stems** exist, or whole-product identity is fuzzy, or the user asked *lock product shape* |
| **`ship-first`** | **No** unless the user asked *lock product shape* / identity fights start / the file already exists |

**Unset profile → prevent** → create. Do **not** silent-create on `ship-first`.

If the file should exist and is missing → create from the template and draft from conversation / `docs/reference/` (lock obvious; do not invent a quiz). Fill **How the map fits** from existing Document Map rows only — one line each. Do not invent stems to fill the table.

### Shape sections only

| Section | Put here | Do not put here |
|---------|----------|-----------------|
| **What this product is** | Whole-product category, who it is for, metaphor, “feels like” as **one** thing | Per-feature flows, APIs, acceptance, module diagrams |
| **What this product is NOT** | Wrong **product** category / whole-product surface | “Not built yet,” phased backlog, one feature’s is-not |
| **End-state picture** | One cohesive image when the product is **whole** — one sitting, one product feel | Feature checklist, MVP → later rewrite, sprint roadmap |
| **How the map fits** | Each **existing** stem → one-line role in the whole | New map rows, foundation task lists, copy of every Understanding |
| **Assumptions** | Real whole-product forks only | Invented quizzes, examples-as-target |
| **Confirmed with user** | Date + what they confirmed or corrected | Relocated contract prose |

**End-state picture is the point.** If is / is not is filled but the picture is a bullet list of features, the file failed. Rewrite until a stranger could see **one product**, not a kit.

### Coding vs confirm

- Feature Understanding `draft` still blocks **that stem’s** code (Workflow §0.1). Product vision `draft` does **not** add a second hard coding gate.
- **`confirmed` product vision:** do **not** implement a feature (or draft a feature Understanding) that **fights** it. Fix the fight first — update the feature, or de-confirm the vision if the **whole product** changed.
- **`draft` / missing (when required):** draft or update it the same turn you add the second stem or bootstrap under prevent. Ask the user to confirm **product** shape (is / is not + end-state picture). Do not invent Assumption quizzes.
- De-confirm product vision **only** on a significant **whole-product** identity change. Adding a feature that still fits the picture is **not** a de-confirm.

### Feature Understanding vs this file

| File | Job |
|------|-----|
| `Product-Vision.md` | The **whole** — end-state picture + product is / is not |
| `*-Understanding.md` | **One stem** — must fit the vision when the vision is confirmed |
| Master Index §1 | Short overview + map — not the end-state essay |
| Feature spec | Contract for that stem |

Do **not** paste the product vision into every Understanding. One line in a feature is / is not is enough when it inherits (“this stem is the X surface of [product]”).

### Stale picture

When the user changes what the **whole product** is (or a stem’s role in the whole), update **this file** the same turn. Refresh **How the map fits** when Document Map rows are added/split/removed. Do not leave yesterday’s end-state.

### Phrases

*Lock product shape* · *Draft the product vision / end-state picture* · *What’s the product vision?* · *The product is one [X], not a pile of [Y]*

---
