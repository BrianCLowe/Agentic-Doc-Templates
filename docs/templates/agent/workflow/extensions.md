<!-- pack-version: 2.7.17 -->

> **Workflow module.** Open from the [workflow index](../Modular_Docs_Workflow.md) only for sub-indexes, game extensions / catalogs, document splits, lean status, or Mermaid judgment. Skip unless Project Profile or the ask triggers these.

# Extensions & rare procedures

## 6. Complex Features — Optional Sub-Indexes

When a single feature grows large or has many distinct sub-components, you **may** create `FeatureName-Index.md`:

- Acts as a mini Master_Index for that feature
- Lists sub-components and links to their spec and TODO files
- Only when the main feature file + TODO would become hard to navigate

**Document Map entry** — link to the sub-index in Master Index §3.2.

**Example sub-index structure**:

```markdown
# World Building — Index

**Parent Feature**: [WorldBuilding.md](WorldBuilding.md)

## Sub-Components
| Component   | Spec                          | Gameplay TODO                  | InEditor TODO                     | Asset TODO                     |
|-------------|-------------------------------|--------------------------------|-----------------------------------|--------------------------------|
| Characters  | [Characters.md](Characters.md) | [Characters-TODO.md](...)     | [Characters-InEditor-TODO.md](...) | [Characters-Asset-TODO.md](...) |
```

---

## 7. Game Development Extensions (Unreal / Godot / Unity)

Skip this section if Project Profile says so (Master Index §1.1).

Most game features use three TODO areas:

- `FeatureName-TODO.md` — Core gameplay, systems logic, rules, simulation
- `FeatureName-InEditor-TODO.md` — Engine editor work (DataAssets, Blueprints, inspectors, etc.)
- `FeatureName-Asset-TODO.md` — Assets, import pipelines, materials, animations

Project-level: `Project-InEditor-TODO.md`, `Project-Asset-TODO.md`

Rename In-Editor TODO files to engine-specific versions and update all links:

- Unreal Engine → `FeatureName-UE-TODO.md`
- Godot → `FeatureName-Godot-TODO.md`
- Unity → `FeatureName-Unity-TODO.md`

### 7.1 Catalog companions *(list-heavy content)*

**When:** Project Profile is game-style **or** a stem’s durable content is a growing **registry of rows** (units, fuels, tech goals, recipes, deployables, orbitals, loot tables) that would bloat the spec’s Behavior section.

**Create:** sibling `FeatureName-Catalog.md` (or `_shared/ComponentName-Catalog.md`) from [`Feature_Catalog_Template.md`](../../Feature_Catalog_Template.md). Link it from the Document Map (**Catalog** column) and from a short **Catalog** pointer on the spec.

**Rules:**
- **Understanding** stays shape-only — never dump row tables there.
- **Spec** owns identity, rules, taxonomy, progression philosophy — not unbounded registries.
- **Catalog** = design-intent rows (ids, tiers, depends-on, unlock, readiness). Not a TODO. Not Acceptance.
- **Readiness** on rows: `stub` \| `sketched` \| `design-ready` \| `in-code`.
- Cross-catalog links use **ids** (e.g. `unit.stillfold_pigeon` → `drive.stillfold`), not duplicated prose.
- Code-first games: Catalog is design intent; runtime truth may live in source — note `in-code:` path when implemented. Do not invent Content CSV/DataTable pipelines unless the project asks.
- Catalog is **optional** — omit until list pressure appears. Creating a Document Map Catalog link requires the file on disk the same turn.

---

## 8. How to Split a Large Document

When a file starts feeling unwieldy:

1. Identify clean section boundaries.
2. Create a new focused file in the correct folder (`_shared/`, `features/`, etc.).
3. In the original file, replace the section with a short link to the new file.
4. Add the new file to the Document Map in `Master_Index.md`.
5. Create matching files as needed (spec, Understanding, TODOs) unless the **user** recorded an omission in Master Index §3.0 — do not invent a §3.0 row to skip them.
6. Update cross-references in other files.

---

## 9. Status Tracking (Lean Approach)

**Primary mechanism**: Each feature's and shared component's `-TODO.md` (and InEditor/Asset TODOs).

- High Priority = in progress / planned
- Completed section = done

Optional: add a small "Current Status" block at the top of the main feature `.md` spec.

Do not add a central `STATUS.md` unless the project truly needs a dashboard.

---

## 12. Mermaid diagrams *(optional, agent judgment)*

Use Mermaid in **specs** or Master Index overview when a **small** diagram explains structure or flow better than prose — e.g. happy-path flow, feature ↔ `_shared/` ownership, module boundaries. Do **not** put flowcharts on `-Understanding.md` (shape only).

| Do | Do not |
|----|--------|
| One focused chart when it clarifies | Diagrams in every file by default |
| Prefer Mermaid for structure/flow | Replace UI screenshots with Mermaid |
| Leave it out when bullets are enough | Decorative or huge multi-subgraph charts |

**Agent decides.** Users should not need to ask for Mermaid. Do not splash charts everywhere just because the format is available.

---
