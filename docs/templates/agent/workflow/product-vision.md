> **Workflow module.** Open from the [workflow index](../Modular_Docs_Workflow.md) when drafting or confirming **whole-product** identity / the end-state picture. Feature is / is not stays in [`understanding.md`](understanding.md) §4.

# Product vision *(whole-product end-state)*

## 4.5 Product vision

Live file: **`docs/Product-Vision.md`** (from [`Product_Vision_Template.md`](../../Product_Vision_Template.md)).

The Document Map + per-feature Understandings can be complete and still miss **what the product is**. This file is the cohesive **end-state picture** — one target the stems must fit. It is **not** a second spec, **not** a feature checklist, and **not** Master Index §1 (that stays a short overview + map).

**Lock gate** (obvious defaults vs real forks; examples are not the target): [`understanding.md`](understanding.md) §4. Do not restate it here. Empty Assumptions is success.

### When to create

| Profile | Create `Product-Vision.md` | Implementation gate |
|---------|----------------------------|---------------------|
| **`prevent`** | **Always** at bootstrap / first live-docs (even one stem). Status starts `draft`; user confirms product shape. | Feature Understanding confirm still gates that stem. **Confirmed** vision: do not implement a fighting feature. |
| **`balanced`** | **Always** create a **lightweight** file. Deepen when **2+ feature stems**, whole-product identity is fuzzy, or the user asked *lock product shape*. | Unchanged: Understanding only when identity is fuzzy / user locks a stem. Draft vision is **not** a coding gate. |
| **`build-first`** | **Always** create a **lightweight** file at bootstrap / first live-docs (and on TEMPLATE_SYNC if missing). | **Not a gate.** File is informative and evolving. Read it for destination; do **not** wait for confirm before coding. Spec + TODO remain the work path. *Lock product shape* only when a change needs explicit confirmation (identity fight, whole-product fork). After lock + confirm, do not implement a fighting feature. |

**Unset profile → prevent** → create + confirm gate. Destination file is created **without** *lock product shape*.

If the file is missing → create from the template and draft per **Draft source** below.

### Draft source *(sync / bootstrap — do not rebuild from the map)*

The feature map is **what exists**, not **what the product is**. Building the end-state picture by summarizing Document Map rows / feature Understandings / specs is the miss this file exists to prevent.

**When drafting or filling a missing `Product-Vision.md` (TEMPLATE_SYNC Step B, bootstrap Step 3v, first live-docs, *lock product shape*):**

1. **Peek `docs/reference/` first** if that folder has files. List names. Open **idea / identity** sources — chat exports, PRDs, “what this is” notes. If there are many files, open the **newest 3–5** identity-ish files (or ones the user pointed at). Do **not** skip the folder because the map looks complete. Do **not** open every vendor/API dump as vision source. Do **not** inventory the whole repo.
2. Draft **What this product is / is NOT** + **End-state picture** from those files + this-turn conversation. Lock obvious defaults. Examples in `reference/` are **not** the target unless the user clearly set them as the target (Workflow §4). Empty Assumptions is success.
3. **Then** fill **How the map fits** from **existing** Document Map rows only (one line each). The map is the **fit** table, not the source of the picture. Do not invent stems.

**Do not:** Reconstruct the vision from Master Index §3 + `*-Understanding.md` + specs alone. Do not write a feature-checklist “end-state.” Do not skip `reference/` when it has idea threads.

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
- **`build-first`:** `draft` vision is destination-only — do **not** wait for confirm before spec/TODO implementation.
- **`confirmed` product vision** (after *lock product shape* + user confirm, or prevent’s confirm): do **not** implement a feature (or draft a feature Understanding) that **fights** it. Fix the fight first — update the feature, or de-confirm the vision if the **whole product** changed.
- **`prevent` `draft` / missing:** draft the same turn you bootstrap / first live-docs. Ask the user to confirm **product** shape (is / is not + end-state picture). Do not invent Assumption quizzes.
- **`balanced` `draft`:** deepen when 2+ stems / fuzzy whole / *lock product shape*. Do not invent quizzes.
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

*Lock product shape* — confirm / freeze the vision (gate starts). Destination file is created without this phrase.

Also: *Draft the product vision / end-state picture* · *What’s the product vision?* · *The product is one [X], not a pile of [Y]*

---
