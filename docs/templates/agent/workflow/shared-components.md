<!-- pack-version: 2.7.17 -->

> **Workflow module.** Open from the [workflow index](../Modular_Docs_Workflow.md) when deciding `_shared/` vs feature, or placing foundation tasks. Do not load other modules unless the index routes you there.

# Shared components

## 1. Shared Components — Foundation vs Consumption

**Gate — only create `_shared/` docs when something is actually shared.**

| Put in `_shared/` | Do **not** put in `_shared/` |
|-------------------|------------------------------|
| A **project-owned** piece (code, UI kit, subsystem) that **two or more features** will consume, or that the user named as shared | Engine/framework general knowledge (e.g. “how Unreal works”, UE project-settings overview, generic Godot/Unity primers) |
| Extracted reusable core the user agreed to share | A single feature’s systems dumped into `_shared/` because “nowhere else fit” |
| | Filler Document Map rows so §3.1 is not empty |

**Empty `_shared/` and an empty §3.1 table are normal and preferred** when the project is feature-shaped (many puzzle/game/apps never need shared docs). Prefer `features/` for mode/level/puzzle-specific work. If you must keep engine primers or pasted UE notes, use `docs/reference/` — not fake shared components.

Only when a real shared piece exists: `_shared/` often needs **foundation work first** — code, APIs, or patterns that multiple features will consume later.

**Each substantial shared component** (that passed the gate) gets the **same default file set as a feature** for the active docs profile (§0.1) — unless the user explicitly says otherwise for that component:

- `_shared/ComponentName.md` — spec / contract / architecture **(always)**
- `_shared/ComponentName-Understanding.md` — shape guardrails (§4) — **per profile** (required under `prevent`; situational under `balanced`; optional under `ship-first`)
- `_shared/ComponentName-TODO.md` — core / systems / foundation tasks **(always)**
- `_shared/ComponentName-InEditor-TODO.md` — engine editor work *(game extensions / user asked)*
- `_shared/ComponentName-Asset-TODO.md` — assets & content *(game extensions / user asked)*

**Exceptions:** If the user **explicitly** says a component or feature does not need a particular note type (e.g. "BlockEditor has no asset work"), omit that file and record the exception in Master Index **§3.0** with who said it and when. Project-wide ceremony is **`docs_profile`**, not a §3.0 “no Understanding for the whole project” invention.

**Do not invent exceptions** for rows that *should* exist under the active profile. Under **`prevent`**, missing files or “we’ll add Understanding later” are **not** reasons to skip Understanding — create the default set. Under **`ship-first` / `balanced`**, not creating Understanding when the profile allows is **correct**, not an exception. Do **not** invent §3.1 shared rows (or §3.0 excuses) to fill empty space.

**Maturity** *(shared components only)*: Set on the shared **spec** (`draft` | `usable` | `stable`) so consumer features know whether integration is safe. Update when foundation work progresses — see [`Feature_Spec_Template.md`](../../Feature_Spec_Template.md).

**Where tasks go** (agents often get this wrong):

| Work type | Put tasks in | Not in |
|-----------|--------------|--------|
| Building or refactoring the shared component itself | `_shared/ComponentName-TODO.md` | A consumer feature's TODO |
| Feature blocked until shared work is done | Consumer feature TODO — **dependency note + link** only | Duplicating foundation tasks in the feature TODO |
| Feature-specific wiring / UI using the shared piece | That feature's TODO | `_shared/ComponentName-TODO.md` |

**Example**: Extract a reusable text-editor core into `_shared/BlockEditor.md`. Tasks to create that core → `_shared/BlockEditor-TODO.md`. A role-specific UI that *uses* the core → `RoleEditor-TODO.md` with a note: *Depends on [BlockEditor-TODO.md](BlockEditor-TODO.md) item "Expose shared editing API"* — not the extraction tasks themselves.

Optional: `_shared/_Foundation-TODO.md` for cross-cutting shared work that does not belong to one component file yet.

---
