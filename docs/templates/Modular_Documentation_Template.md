# Lean Modular Documentation Template
> Never edit this template unless the user asks you to.

**Core Idea**: Large documentation sets are split into a lightweight index + many small, purpose-built files. This keeps context windows manageable and makes navigation trivial.

---

This template:
- Keeps only what’s useful for documentation-heavy workflows
- Adds explicit support for per-feature TODO.md files
- Provides a clear process for splitting large docs

---

## Recommended Folder Structure

```
docs/                          # All documentation lives here
├── Master_Index.md            # ← Always read first
├── _shared/                   # Reusable concepts, schemas, patterns
│   ├── NestedNotes.md
│   ├── BlockEditor.md
│   └── LLM_Integration.md
├── features/                  # One folder per major feature/module
│   ├── MainWorkspace.md
│   ├── MainWorkspace-TODO.md
│   ├── MainWorkspace-InEditor-TODO.md
│   ├── MainWorkspace-Asset-TODO.md
│   ├── DiffWorkflow.md
│   ├── DiffWorkflow-TODO.md
│   └── ...
├── reference/                 # Legacy specs, detailed deep-dives, external links
│   └── Old_Rivenquill_Spec.md
└── templates/                 # Reusable starters - Never edit without instructions to do so.
    ├── TODO_Template.md
    └── Feature_Spec_Template.md
```

**Naming Rules**:
- Kebab-case for files and folders
- Feature files: `FeatureName.md`
- TODO files: `FeatureName-TODO.md` (core gameplay/systems), `FeatureName-InEditor-TODO.md` (Unreal Editor / engine editor work), `FeatureName-Asset-TODO.md` (models, textures, import, hooking up)
- Shared files live in `_shared/` (underscore prefix = “don’t treat as a feature”)
- Project-level files: `Project-InEditor-TODO.md` and `Project-Asset-TODO.md`

---

## Master_Index.md — The Template

Copy the structure below into your project’s `docs/Master_Index.md`. Replace bracketed placeholders.

```markdown
# [Project Name] — Master Index

**Purpose**: Single entry point for all documentation. Designed so AI agents and humans only ever read the files relevant to the current task.

## 1. Project Overview
[1–3 short paragraphs describing what the project is, its core architecture, and primary goals. Keep it high-level — details live in feature files.]

## 2. Project Structure & Philosophy
### 2.1 Key Locations
| Path              | Purpose |
|-------------------|---------|
| `docs/`           | All specs, architecture, and tracking |
| `docs/_shared/`   | Reusable components & patterns |
| `docs/features/`  | Feature-specific specs + TODOs (+ optional sub-indexes) |
| `src/` / `backend/` / `frontend/` | Actual code (reference only) |

### 2.2 Modular Rules
- No file should exceed ~800–1000 lines.
- Shared concepts → `_shared/`
- Every major feature gets its own `.md` plus up to three focused TODO files: `FeatureName-TODO.md` (gameplay/systems), `FeatureName-InEditor-TODO.md` (engine editor work), and `FeatureName-Asset-TODO.md` (assets & content)
- Large docs are split on first sign of bloat (see Section 6)

### 2.3 For Complex / "Beefy" Features: Optional Sub-Indexes (AI Discretion)

When a single feature grows large or has many distinct sub-components (example: a "WorldBuilding" feature that contains Characters, Places, Items, Groups, Lore, Relationships, etc.), the AI or human **may** create a dedicated sub-index:

**File name**: `FeatureName-Index.md` (e.g., `world-building-Index.md`)

**Purpose**:
- Acts as a mini Master_Index just for that feature
- Lists all sub-components + links to their individual `.md` spec and `-TODO.md` files
- Keeps the main feature file from becoming a giant table of contents

**When to create one**:
- Only when the main feature file + its TODO would become hard to navigate
- **Left entirely to the discretion** of the AI or person doing the work
- No pressure to create one for every feature — most will stay simple (just `.md` + `-TODO.md`)

**How it appears in the main Document Map**:
In the Features table, you can link to the sub-index instead of (or in addition to) the main spec:

| Feature          | Spec / Index                          | Gameplay TODO | InEditor TODO | Asset TODO |
|------------------|---------------------------------------|---------------|---------------|------------|
| World Building   | [features/WorldBuilding-Index.md](...) | [features/WorldBuilding-TODO.md](...) | [features/WorldBuilding-InEditor-TODO.md](...) | [features/WorldBuilding-Asset-TODO.md](...) |

**Example sub-index structure** (keep it short):
```markdown
# World Building — Index

**Parent Feature**: [WorldBuilding.md](WorldBuilding.md)

## Sub-Components
| Component   | Spec                          | Gameplay TODO                  | InEditor TODO                     | Asset TODO                     |
|-------------|-------------------------------|--------------------------------|-----------------------------------|--------------------------------|
| Characters  | [Characters.md](Characters.md) | [Characters-TODO.md](...)     | [Characters-InEditor-TODO.md](...) | [Characters-Asset-TODO.md](...) |
| Places      | [Places.md](Places.md)         | [Places-TODO.md](...)         | [Places-InEditor-TODO.md](...)     | [Places-Asset-TODO.md](...)     |
| Lore        | [Lore.md](Lore.md)             | [Lore-TODO.md](...)           | [Lore-InEditor-TODO.md](...)       | [Lore-Asset-TODO.md](...)       |
```

This pattern scales the modular philosophy down one more level without forcing complexity on simpler features.

## 3. Document Map

### 3.1 Shared / Core Components
| Document | Description |
|----------|-------------|
| [_shared/CoreConcept1.md](_shared/CoreConcept1.md) | ... |
| [_shared/CoreConcept2.md](_shared/CoreConcept2.md) | ... |

### 3.2 Features & Modules
| Feature          | Spec / Index                                      | Gameplay TODO | InEditor TODO | Asset TODO |
|------------------|---------------------------------------------------|---------------|---------------|------------|
| Main Workspace   | [features/MainWorkspace.md](features/MainWorkspace.md) | [features/MainWorkspace-TODO.md](features/MainWorkspace-TODO.md) | [features/MainWorkspace-InEditor-TODO.md](features/MainWorkspace-InEditor-TODO.md) | [features/MainWorkspace-Asset-TODO.md](features/MainWorkspace-Asset-TODO.md) |
| Diff Workflow    | [features/DiffWorkflow.md](features/DiffWorkflow.md)     | [features/DiffWorkflow-TODO.md](features/DiffWorkflow-TODO.md) | [features/DiffWorkflow-InEditor-TODO.md](features/DiffWorkflow-InEditor-TODO.md) | [features/DiffWorkflow-Asset-TODO.md](features/DiffWorkflow-Asset-TODO.md) |
| World Building   | [features/WorldBuilding-Index.md](...) *(sub-index for complex feature)* | [features/WorldBuilding-TODO.md](...) | [features/WorldBuilding-InEditor-TODO.md](...) | [features/WorldBuilding-Asset-TODO.md](...) |
| [Add more rows as needed] | | | | |

### 3.3 Project-Level Work
| Area          | TODO File |
|---------------|-----------|
| Project-wide In-Editor work (DataAssets, Blueprints, custom inspectors, etc.) | [Project-InEditor-TODO.md](Project-InEditor-TODO.md) |
| Project-wide Assets & Content | [Project-Asset-TODO.md](Project-Asset-TODO.md) |

### 3.4 Reference & Legacy
| Document | Description |
|----------|-------------|
| [reference/LegacySpec.md](reference/LegacySpec.md) | Older detailed spec (read only when needed) |

## 4. Quick Start — Working on Any Task

**Always follow this order** (AI agents and humans):

1. Read `Master_Index.md` (this file) — Sections 1–4
2. Read any `_shared/` documents listed as relevant in Section 3.1
3. Open the specific feature spec: `features/[FeatureName].md`
4. Open the relevant TODO file(s) for the work area:
   - Core gameplay/systems → `features/[FeatureName]-TODO.md`
   - In-Editor work (DataAssets, Blueprints, inspectors, etc.) → `features/[FeatureName]-InEditor-TODO.md` (or engine-specific version)
   - Assets & content → `features/[FeatureName]-Asset-TODO.md`
5. Do the work
6. **Update the TODO file(s)** before ending the session (mark completed items, add new ones)

**Golden Rule**: If you find yourself scrolling through a long file, stop and split it.

## 5. TODO Management

Every feature **must** have at least one companion `-TODO.md` file. Most game features will have three.

**File Naming**:
- Core gameplay/systems: `FeatureName-TODO.md`
- In-Editor work: `FeatureName-InEditor-TODO.md` (generic placeholder — see Game Development Extensions below for engine-specific renaming)
- Assets & content: `FeatureName-Asset-TODO.md`

**Purpose**: 
- Visible checklist of what’s done vs. still needed
- Prevents “I think we finished that” drift
- Gives AI agents a clear next-action list

**Cross-Feature Interactions**:
When work in one feature depends on or affects another feature (or a shared component in `_shared/`), add a note in the TODO with a direct link to the other feature’s TODO file. Example:
> Requires changes in `BlockEditor` (see [BlockEditor-TODO.md](../BlockEditor-TODO.md))

This keeps integration requirements visible and prevents silent breakage.

**AI Agents — Dynamic TODO Creation**:
You are **encouraged** to add new TODO items as you work:
- New implementation steps you discover that weren’t in the original plan
- Design clarifications or questions that need user input
- Edge cases, refactoring opportunities, or follow-up tasks

Add them under the appropriate priority section (usually High or Medium). This turns the TODO into a living, evolving task list rather than a static snapshot.

**Recommended Format** (copy from `templates/TODO_Template.md`):

```markdown
# [Feature Name] — TODO

**Last Updated**: YYYY-MM-DD  
**Owner**: [Your Name or "Team"]

## High Priority / Next Up
- [ ] Task description (why it matters)
- [ ] Another task

## Medium Priority
- [ ] ...

## Low Priority / Nice-to-Have
- [ ] ...

## Completed (moved here after [x])
- [x] Task that is done (completed 2026-05-04 by @user)
```

**Workflow**:
- Before starting: Read the TODO, pick the top unchecked item.
- While working: Add new TODO items as you discover them (new steps, clarifications needed, cross-feature dependencies, etc.).
- After finishing any task: Mark it `[x]`, add completion date/note.
- When a section gets long: Move finished items to “Completed” or archive them.
- AI agents: Always end your response by showing the updated TODO section (or at least confirming you updated the file).

## 6. Game Development Extensions (Unreal / Godot / Unity)

For game projects, most features require work across three distinct areas. Each area gets its own focused TODO file so AI agents and humans can stay in the right context:

- `FeatureName-TODO.md` — Core gameplay, systems logic, rules, and simulation
- `FeatureName-InEditor-TODO.md` — Work performed inside the game engine’s editor (creating/setting up DataAssets, wiring Blueprints, custom inspectors, gizmos, editor utilities, menus, editor-only tools, etc.)
- `FeatureName-Asset-TODO.md` — Asset creation, import pipelines, materials, animations, sounds, folder structure, placeholders, and hooking content into the game

Project-level concerns that don’t belong to a single feature use:
- `Project-InEditor-TODO.md`
- `Project-Asset-TODO.md`

**For AI agents**: When creating or referencing the In-Editor TODO file, use the generic name `FeatureName-InEditor-TODO.md` only as a placeholder. Immediately rename the file (and update all links) to the engine-specific version:

- Unreal Engine → `FeatureName-UE-TODO.md`
- Godot → `FeatureName-Godot-TODO.md`
- Unity → `FeatureName-Unity-TODO.md`

This prevents any ambiguity about what “Editor” means and keeps file names crystal clear regardless of the engine being used.

## 7. How to Split a Large Document

When a file starts feeling unwieldy:

1. Identify clean section boundaries.
2. Create a new focused file in the correct folder (`_shared/`, `features/`, etc.).
3. In the original file, replace the section with a short link:
   > **See [NewFile.md](NewFile.md) for full details.**
4. Add the new file to the Document Map in `Master_Index.md`.
5. Create the matching `-TODO.md`, `-InEditor-TODO.md`, and/or `-Asset-TODO.md` files as needed.
6. Update any cross-references in other files.

**Benefits**:
- AI context stays tiny and relevant
- Multiple people/AIs can work on different sections simultaneously
- Search and navigation become trivial

## 8. Status Tracking (Lean Approach)

**Primary mechanism**: Each feature’s `-TODO.md` (and `-InEditor-TODO.md` / `-Asset-TODO.md`) files.

- The TODO lists themselves serve as the living status tracker (High Priority items = In Progress / Planned, Completed section = Done).

**Per-feature status** can also be summarized in a small “Current Status” block at the top of the main feature `.md` file if desired.

---

## How to Bootstrap This in a New (or Existing) Project

1. Create the `docs/` folder structure above.
2. Copy this entire template into `docs/Master_Index.md` and customize.
3. Create `templates/TODO_Template.md` (see below).
4. Pick your first feature → create `FeatureName.md` plus the relevant TODO file(s): `FeatureName-TODO.md`, `FeatureName-InEditor-TODO.md` (or engine-specific), and/or `FeatureName-Asset-TODO.md`.
5. Populate the Document Map.
6. Only add a `STATUS.md` if you later feel you truly need a central dashboard (generally discouraged).

**Pro Tip for Cursor Users**: Add a Cursor Rule that says:

**Modular Documentation Rule (Cursor)**

This project uses a lean modular documentation system. `docs/Master_Index.md` is the single entry point.

**Always follow this order when starting work:**
1. Read `docs/Master_Index.md` first.
2. Follow the Quick Start section exactly.
3. Open the relevant `FeatureName-TODO.md` before making changes.

**While working:**
- Treat the feature's `-TODO.md` as the living task list.
- Add new items as you discover them (new steps, clarifications, cross-feature dependencies, edge cases, refactoring needs).
- Use the "Cross-Feature Dependencies & Integration Notes" section when features interact.

**After changes (mandatory):**
- Update the relevant `-TODO.md` — mark completed items with `[x]` + date.
- Move finished items to Completed when the list gets long.
- Only read other files when they are explicitly linked from Master_Index or the current TODO/spec.

**Clarification Protocol:**
If the user says "review spec", "check for gaps", "ask questions", or "confidence check":
- Re-read the feature spec + TODO
- Identify areas that are vague, missing, or open to interpretation
- Ask targeted clarifying questions instead of assuming
- Only proceed after user confirmation

**Philosophy:** Keep documentation small and accurate. The TODO files are your primary memory across sessions.

---

## Included Supporting Template

See `templates/TODO_Template.md` for the ready-to-copy TODO format.
```