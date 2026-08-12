<!-- pack-version: 2.7.17 -->

> **Workflow module.** Open from the [workflow index](../Modular_Docs_Workflow.md) when creating files or Document Map rows. Do not load other modules unless the index routes you there.

# Naming & file layout

## 0. Naming & file layout *(read before creating files)*

**Layout:** **Flat sibling files** in `docs/features/` and `docs/_shared/` — one **file set** per feature or shared component. Match the **Document Map** paths in `Master_Index.md` §3.

| Kind | Create this path |
|------|------------------|
| Feature spec | `docs/features/FeatureName.md` |
| Feature Understanding | `docs/features/FeatureName-Understanding.md` |
| Feature TODO | `docs/features/FeatureName-TODO.md` |
| Feature Catalog *(optional — §7 / list-heavy)* | `docs/features/FeatureName-Catalog.md` |
| Shared spec | `docs/_shared/ComponentName.md` |
| Shared Understanding | `docs/_shared/ComponentName-Understanding.md` |
| Shared TODO | `docs/_shared/ComponentName-TODO.md` |
| Shared Catalog *(optional)* | `docs/_shared/ComponentName-Catalog.md` |
| Sub-index *(large feature only)* | `docs/features/FeatureName-Index.md` |
| Screenshots | `docs/features/assets/…` or `docs/_shared/assets/…` |

**Use the same name stem** across the set (`MainWorkspace`, `BlockEditor`, …). Copy spelling from the Document Map when adding to an existing project.

**Case:** Pick one convention per project (PascalCase or kebab-case) in Project Profile (Master Index §1.1) and stay consistent.

**When adding a new feature or shared component:**

1. Add a row to Master Index §3.1 or §3.2 with the exact paths (**working markdown links** — not “planned” placeholders with nowhere to click).
2. Create the **default file set for the active docs profile** (§0.1) at those paths **in the same turn**:
   - **Always:** [`Feature_Spec_Template.md`](../../Feature_Spec_Template.md) + [`TODO_Template.md`](../../TODO_Template.md)
   - **+ Understanding** ([`Feature_Understanding_Template.md`](../../Feature_Understanding_Template.md)): required under **`prevent`**; under **`balanced`** when identity is ambiguous / multi-surface / split / user asked; under **`ship-first`** only if user asked *lock shape* or an Understanding already exists for that stem
   - Add [`Feature_Catalog_Template.md`](../../Feature_Catalog_Template.md) only when §7 / list-heavy rules apply
3. All files for one feature live **directly** in `features/` (or `_shared/`), not in a subfolder named after the feature.

**Map without files = incomplete work.** Do not add Document Map rows and defer file creation “until the user picks where to start.” Bootstrap Step 3d and this section require the profile’s default file set on disk. Under **`prevent`**, Understanding status `draft` means **do not implement code** yet — it does **not** mean skip creating `-Understanding.md`.

**`docs/reference/`:** Drop zone for **source** materials. **Recommended habit:** markdown **chat exports** of idea threads (often many files) — they preserve user whys/motives better than polished-only design docs ([`../help/IDEA_CAPTURE_TIPS.md`](../../help/IDEA_CAPTURE_TIPS.md)). Also fine: PRDs, legacy specs. Not Document Map rows. Read when the user points at a file or asks to convert / **build or update** live docs from them. Optional `docs/reference/visuals/` for inspiration screenshots. Do **not** send users to a chat-only `AGENT.md` attach flow — that path is paused; export → `reference/` is the supported route.

**One identity per stem:** If conversation or `reference/` material describes **two (or more) finished-feature identities** that do different jobs (different category, product surface, or ownership) — **split**. Add separate Document Map rows + default file sets (§0) in the same turn; move misplaced shape/contract content into the correct stem. Do **not** keep unlike things in one Understanding to avoid creating files or because the user mentioned them together. Prefer asking one clarifying question over silently merging. User correction (“those are two features”) → split immediately — do not wait for them to name paths.

---
