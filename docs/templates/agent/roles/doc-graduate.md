# Role — Doc graduate *(optional)*

> **Opt-in.** Use only when the user asks for this role or names this file. Not always-on.

**Job:** After Understanding is **`confirmed`** (shape approved), graduate durable **contract** content into the feature/shared **spec**. Spec may hold detail that was never in Understanding. No implementation.

**Canonical procedure:** [`../workflow/understanding.md`](../workflow/understanding.md) §2 (graduation). Spec template: [`../../Feature_Spec_Template.md`](../../Feature_Spec_Template.md). Decisions: [`../workflow/decisions.md`](../workflow/decisions.md) / [`../../Decision_Template.md`](../../Decision_Template.md) when cross-cutting.

## When to invoke

- User confirmed Understanding (or approved a plan that references it) and asks to graduate / update the spec
- User says: *Doc graduate*, *graduate Understanding to spec*
- **Not** under pure **ship-first** with no Understanding — grow the spec during implement instead; only run this role if an Understanding exists

## Inputs *(open only these)*

1. `docs/Master_Index.md` Sections 1–3 (as needed for paths)
2. The confirmed `-Understanding.md`
3. The matching spec (`.md` without `-Understanding` / `-TODO`)
4. That stem’s `-TODO.md` (Workflow §5.3 bridge after product Acceptance lands)
5. Spec template only if the live spec is still a stub
6. Workflow §2 / §5.3 if graduation or operable-bridge rules are unclear

## Steps

1. Verify Understanding status is **`confirmed`**. If still `draft` / `reviewed`, **stop** — do not graduate; point at [`understanding-author.md`](understanding-author.md) or ask for explicit confirm.
2. Populate the spec as **contract home** per Workflow §2 + Spec template (overview, architecture, Behavior, Acceptance, Visual references, Decisions, dependencies, shared Maturity). Synthesize Understanding **plus** conversation / decisions — do not only copy thin Understanding; do not compress to match Understanding’s length. Move any leftover How-it-should-work / Done when / screenshot tables off Understanding into the spec. For user/operator-facing stems, Acceptance includes ≥1 **operable** outcome (Workflow §5.3).
3. **TODO bridge (Workflow §5.3):** Open that stem’s `-TODO.md`. If Overview/Acceptance are product-shaped and High Priority is only packages/tests with no exercise path → **add** dual-track surface/wire/smoke items (include **scaffold + wire** minimal surface when UI was never specified) **or** a loud phased note (`library foundation first · exercise path: …`) only when domain-before-surface is intentional **or** **library-only** if the stem truly has no operator surface. Do not leave product Acceptance with silent domain-only TODOs. Do not invent “await UI design” for blank canvas.
4. Leave shape-only sections on Understanding. Do not delete the Understanding file.
5. Record lasting tradeoffs in the spec Decisions table, or `docs/decisions/` only if the user asked for a cross-cutting note.
6. Update Document Map maturity/links only if shared maturity changed.
7. Summarize what landed in the spec (especially anything never in Understanding) and any TODO bridge edits. **Stop.**

## Stop when

- Spec holds a usable durable contract (not a stub that merely restates thin Understanding), and
- User-facing stems have TODO dual-track, phase bridge, or library-only when Acceptance is operable, and
- No code was written

## Do not

- Graduate while Understanding is `draft` (unless the user explicitly waives and orders graduation — note that in the spec)
- Copy only Understanding into the spec and stop
- Thin Architecture / Behavior to “keep docs lean” when confirmed product rules or APIs exist
- Leave product-shaped Acceptance with domain-only High Priority and no phase / library-only / exercise path (Workflow §5.3)
- Implement features or rewrite High Priority beyond the §5.3 bridge (dual-track / phase / library-only) and an optional one-line “graduated to spec” note
- Rewrite unrelated features; invent architecture/behavior the user never confirmed
- Re-draft Understanding unless the user corrected identity during this pass (then set Understanding back to `draft` and stop — do not graduate)
