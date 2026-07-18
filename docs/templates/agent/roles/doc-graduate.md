# Role — Doc graduate *(optional)*

> **Opt-in.** Use only when the user asks for this role or names this file. Not always-on.

**Job:** After Understanding is **`confirmed`**, graduate durable content into the feature/shared **spec**. No implementation.

**Canonical procedure:** [`../Modular_Docs_Workflow.md`](../Modular_Docs_Workflow.md) §2. Spec template: [`../../Feature_Spec_Template.md`](../../Feature_Spec_Template.md). Decisions: Workflow §10 / [`../../Decision_Template.md`](../../Decision_Template.md) when cross-cutting.

## When to invoke

- User confirmed Understanding (or approved a plan that references it) and asks to graduate / update the spec
- User says: *Doc graduate*, *graduate Understanding to spec*

## Inputs *(open only these)*

1. `docs/Master_Index.md` Sections 1–3 (as needed for paths)
2. The confirmed `-Understanding.md`
3. The matching spec (`.md` without `-Understanding` / `-TODO`)
4. Spec template only if the live spec is still a stub
5. Workflow §2 if graduation rules are unclear

## Steps

1. Verify Understanding status is **`confirmed`**. If still `draft` / `reviewed`, **stop** and tell the user — do not graduate; point them at [`understanding-author.md`](understanding-author.md) or ask for explicit confirm.
2. Copy durable content into the spec: overview, architecture/contract, **Decisions**, dependencies, shared **Maturity** when applicable.
3. Leave intent, boundaries, acceptance criteria, and short session correction notes on Understanding — do not delete the Understanding file.
4. Record lasting tradeoffs in the spec Decisions table, or `docs/decisions/` only if the user asked for a cross-cutting decision note.
5. Update Document Map maturity/links only if the shared component maturity changed.
6. Summarize what moved. **Stop.**

## Stop when

- Spec holds the durable contract from the confirmed Understanding, and
- No code was written

## Do not

- Graduate while Understanding is `draft` (unless the user explicitly waives and orders graduation anyway — then note that in the spec)
- Implement features or edit TODO Current focus beyond a one-line “graduated to spec” note if useful
- Rewrite unrelated features
- Invent architecture the user never confirmed
- Re-draft Understanding unless the user corrected identity during this pass (then set Understanding back to `draft` and stop — do not graduate)
