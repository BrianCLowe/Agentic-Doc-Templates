# Role — Doc graduate *(optional)*

> **Opt-in.** Use only when the user asks for this role or names this file. Not always-on.

**Job:** After Understanding is **`confirmed`** (shape approved), graduate durable **contract** content into the feature/shared **spec**. Spec may hold detail that was never in Understanding. No implementation.

**Canonical procedure:** [`../Modular_Docs_Workflow.md`](../Modular_Docs_Workflow.md) §2. Spec template: [`../../Feature_Spec_Template.md`](../../Feature_Spec_Template.md). Decisions: Workflow §10 / [`../../Decision_Template.md`](../../Decision_Template.md) when cross-cutting.

## When to invoke

- User confirmed Understanding (or approved a plan that references it) and asks to graduate / update the spec
- User says: *Doc graduate*, *graduate Understanding to spec*
- **Not** under pure **ship-first** with no Understanding — grow the spec during implement instead; only run this role if an Understanding exists

## Inputs *(open only these)*

1. `docs/Master_Index.md` Sections 1–3 (as needed for paths)
2. The confirmed `-Understanding.md`
3. The matching spec (`.md` without `-Understanding` / `-TODO`)
4. Spec template only if the live spec is still a stub
5. Workflow §2 if graduation rules are unclear

## Steps

1. Verify Understanding status is **`confirmed`**. If still `draft` / `reviewed`, **stop** — do not graduate; point at [`understanding-author.md`](understanding-author.md) or ask for explicit confirm.
2. Populate the spec as **contract home** per Workflow §2 + Spec template (overview, architecture, Behavior, Acceptance, Visual references, Decisions, dependencies, shared Maturity). Synthesize Understanding **plus** conversation / decisions — do not only copy thin Understanding; do not compress to match Understanding’s length. Move any leftover How-it-should-work / Done when / screenshot tables off Understanding into the spec.
3. Leave shape-only sections on Understanding. Do not delete the Understanding file.
4. Record lasting tradeoffs in the spec Decisions table, or `docs/decisions/` only if the user asked for a cross-cutting note.
5. Update Document Map maturity/links only if shared maturity changed.
6. Summarize what landed in the spec (especially anything never in Understanding). **Stop.**

## Stop when

- Spec holds a usable durable contract (not a stub that merely restates thin Understanding), and
- No code was written

## Do not

- Graduate while Understanding is `draft` (unless the user explicitly waives and orders graduation — note that in the spec)
- Copy only Understanding into the spec and stop
- Thin Architecture / Behavior to “keep docs lean” when confirmed product rules or APIs exist
- Implement features or edit TODO Current focus beyond a one-line “graduated to spec” note if useful
- Rewrite unrelated features; invent architecture/behavior the user never confirmed
- Re-draft Understanding unless the user corrected identity during this pass (then set Understanding back to `draft` and stop — do not graduate)
