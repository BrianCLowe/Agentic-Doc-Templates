> **Workflow module.** Open from the [workflow index](../Modular_Docs_Workflow.md) when keeping the project tooling doc accurate.

# Tooling

## 11. Tooling *(project tools and services)*

Live file: **`docs/Tooling.md`** (from [`Tooling_Template.md`](../../Tooling_Template.md)).

`docs/Tooling.md` describes the **machine / workflow tools** (CLIs, SDKs, runtimes, engines) - **not** package-manager dependencies.

**Services this app consumes** *(same file, not an install row)*: external APIs and services the running app calls. Columns: service, why, credential **name** only, docs link. Omit the section when the app calls none. Do **not** put these in Required / Optional. A `procure` errand for one of these still belongs on Human-TODO (Workflow §13); this section is the list that stays after that errand is done.

Do not invent tools; update the file when the stack changes.

---
