<!-- template-version: 1.3 -->

> **Template reference.** Do not put project-specific content in this file. Copy to `docs/Master_Index.md` for initial setup, or diff against it when syncing template improvements into the live index. Never edit this template unless the user asks you to.

# [Project Name] — Master Index

**Purpose**: Single entry point for all documentation. Read only the files relevant to the current task.

**Template version**: 1.3 *(update this line in `docs/Master_Index.md` when syncing from `templates/Master_Index_Template.md`)*

## 1. Project Overview

[1–3 short paragraphs describing what the project is, its core architecture, and primary goals. Keep it high-level — details live in feature files.]

## 2. Project Structure & Philosophy

### 2.1 Key Locations

| Path              | Purpose |
|-------------------|---------|
| `docs/`           | All specs, architecture, and tracking |
| `docs/_shared/`   | Reusable components, patterns, and **their foundation TODOs** |
| `docs/features/`  | Feature-specific specs + TODOs (+ optional sub-indexes) |
| `docs/features/assets/` | Reference **screenshots** for features (linked from `-Understanding.md`) |
| `docs/reference/visuals/` | Optional inspiration screenshots not tied to one feature yet |
| `docs/templates/` | Canonical templates — reference for structure and sync |
| `src/` / `backend/` / `frontend/` | Actual code (reference only) |

### 2.2 Modular Rules

- No file should exceed ~800–1000 lines.
- Shared concepts → `_shared/` — each substantial shared component gets `ComponentName.md` + `ComponentName-TODO.md` for **foundation work** (see Section 2.4)
- Every major feature gets its own `.md`, a `FeatureName-Understanding.md` (agent model of user intent — see Section 5), plus up to three focused TODO files: `FeatureName-TODO.md` (gameplay/systems), `FeatureName-InEditor-TODO.md` (engine editor work), and `FeatureName-Asset-TODO.md` (assets & content)
- Large docs are split on first sign of bloat (see Section 8)

### 2.3 For Complex Features: Optional Sub-Indexes

When a single feature grows large or has many distinct sub-components, you **may** create a dedicated sub-index:

**File name**: `FeatureName-Index.md` (e.g., `WorldBuilding-Index.md`)

**Purpose**:

- Acts as a mini Master_Index for that feature
- Lists sub-components and links to their `.md` spec and `-TODO.md` files
- Keeps the main feature file from becoming a giant table of contents

**When to create one**:

- Only when the main feature file + its TODO would become hard to navigate
- Left to discretion — most features stay simple (`.md` + `-TODO.md`)

**Document Map entry** — link to the sub-index instead of (or in addition to) the main spec:

| Feature          | Spec / Index                          | Gameplay TODO | InEditor TODO | Asset TODO |
|------------------|---------------------------------------|---------------|---------------|------------|
| World Building   | [features/WorldBuilding-Index.md](...) | [features/WorldBuilding-TODO.md](...) | [features/WorldBuilding-InEditor-TODO.md](...) | [features/WorldBuilding-Asset-TODO.md](...) |

**Example sub-index structure**:

```markdown
# World Building — Index

**Parent Feature**: [WorldBuilding.md](WorldBuilding.md)

## Sub-Components
| Component   | Spec                          | Gameplay TODO                  | InEditor TODO                     | Asset TODO                     |
|-------------|-------------------------------|--------------------------------|-----------------------------------|--------------------------------|
| Characters  | [Characters.md](Characters.md) | [Characters-TODO.md](...)     | [Characters-InEditor-TODO.md](...) | [Characters-Asset-TODO.md](...) |
| Places      | [Places.md](Places.md)         | [Places-TODO.md](...)         | [Places-InEditor-TODO.md](...)     | [Places-Asset-TODO.md](...)     |
```

### 2.4 Shared Components — Foundation vs Consumption

`_shared/` is not only documentation for features to read. Shared pieces often need **foundation work first** — code, APIs, or patterns that multiple features will consume later.

**Each substantial shared component** should have:

- `_shared/ComponentName.md` — spec / contract / architecture
- `_shared/ComponentName-TODO.md` — tasks to **build or change the shared foundation**

**Where tasks go** (agents often get this wrong):

| Work type | Put tasks in | Not in |
|-----------|--------------|--------|
| Building or refactoring the shared component itself | `_shared/ComponentName-TODO.md` | A consumer feature's TODO |
| Feature blocked until shared work is done | Consumer feature TODO — **dependency note + link** only | Duplicating foundation tasks in the feature TODO |
| Feature-specific wiring / UI using the shared piece | That feature's TODO | `_shared/ComponentName-TODO.md` |

**Example**: Extract a reusable text-editor core into `_shared/BlockEditor.md`. Tasks to create that core → `_shared/BlockEditor-TODO.md`. A role-specific UI that *uses* the core → `RoleEditor-TODO.md` with a note: *Depends on [BlockEditor-TODO.md](BlockEditor-TODO.md) item "Expose shared editing API"* — not the extraction tasks themselves.

Optional: `_shared/_Foundation-TODO.md` for cross-cutting shared work that does not belong to one component file yet.

## 3. Document Map

### 3.1 Shared / Core Components

| Document | TODO | Description |
|----------|------|-------------|
| [_shared/CoreConcept1.md](_shared/CoreConcept1.md) | [_shared/CoreConcept1-TODO.md](_shared/CoreConcept1-TODO.md) | Foundation work for this shared piece |
| [_shared/CoreConcept2.md](_shared/CoreConcept2.md) | [_shared/CoreConcept2-TODO.md](_shared/CoreConcept2-TODO.md) | ... |
| [_shared/_Foundation-TODO.md](_shared/_Foundation-TODO.md) | *(this file)* | Optional umbrella for shared work not tied to one spec |

### 3.2 Features & Modules

| Feature          | Spec / Index                                      | Understanding | Gameplay TODO | InEditor TODO | Asset TODO |
|------------------|---------------------------------------------------|---------------|---------------|---------------|------------|
| Main Workspace   | [features/MainWorkspace.md](features/MainWorkspace.md) | [features/MainWorkspace-Understanding.md](features/MainWorkspace-Understanding.md) | [features/MainWorkspace-TODO.md](features/MainWorkspace-TODO.md) | [features/MainWorkspace-InEditor-TODO.md](features/MainWorkspace-InEditor-TODO.md) | [features/MainWorkspace-Asset-TODO.md](features/MainWorkspace-Asset-TODO.md) |
| Diff Workflow    | [features/DiffWorkflow.md](features/DiffWorkflow.md)     | [features/DiffWorkflow-Understanding.md](features/DiffWorkflow-Understanding.md) | [features/DiffWorkflow-TODO.md](features/DiffWorkflow-TODO.md) | [features/DiffWorkflow-InEditor-TODO.md](features/DiffWorkflow-InEditor-TODO.md) | [features/DiffWorkflow-Asset-TODO.md](features/DiffWorkflow-Asset-TODO.md) |
| World Building   | [features/WorldBuilding-Index.md](...) *(sub-index)* | [features/WorldBuilding-Understanding.md](...) | [features/WorldBuilding-TODO.md](...) | [features/WorldBuilding-InEditor-TODO.md](...) | [features/WorldBuilding-Asset-TODO.md](...) |
| [Add more rows as needed] | | | | | |

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

**Always follow this order:**

1. Read `Master_Index.md` (this file) — Sections 1–6
2. Decide: **shared foundation work** or **feature work** (Section 2.4)

### Path A — Shared foundation work

Use when building or changing a reusable component, API, or pattern in `_shared/`.

1. Open `_shared/[ComponentName].md`
2. Open `_shared/[ComponentName]-TODO.md` (create from `templates/TODO_Template.md` if missing)
3. Do the work; update **`_shared/[ComponentName]-TODO.md`**
4. If consumer features are blocked, ensure their TODOs link here — do not copy foundation tasks into feature TODOs

### Path B — Feature work

1. Read any `_shared/` documents listed as relevant in Section 3.1 (read-only context unless Path A)
2. Open `features/[FeatureName].md`
3. Open `features/[FeatureName]-Understanding.md` — create or update when discussing, planning, or scoping
4. Open the relevant feature TODO file(s):
   - Core gameplay/systems → `features/[FeatureName]-TODO.md`
   - In-Editor work → `features/[FeatureName]-InEditor-TODO.md` (or engine-specific version)
   - Assets & content → `features/[FeatureName]-Asset-TODO.md`
5. Do the work (only after Understanding is `confirmed` or the user explicitly waives review)
6. **Update the feature TODO file(s)** before ending the session

If the work is really shared foundation, **stop** — use Path A instead.

**Golden Rule**: If you find yourself scrolling through a long file, stop and split it.

## 5. Feature Understanding

Each feature should have `FeatureName-Understanding.md` — the agent's model of **what the user wants**: scope, behavior, UI intent, and how the feature relates to existing work.

**Purpose**:

- Catch misread scope early (e.g. "alternate UI for existing editor" vs "brand-new editor")
- Give the user a short, readable artifact to correct before code is written
- Attach to plans and discussions so corrections happen at planning time

**Status**:

| Status | Meaning |
|--------|---------|
| `draft` | Agent wrote or updated; user has not approved — **do not implement** unless user waives |
| `reviewed` | User skimmed; minor edits may remain |
| `confirmed` | User approved — OK to implement per this understanding |

**When to create or update**:

- User describes a new feature or change
- User asks for a plan, spec review, or "how should we build this"
- Agent discovers a scope assumption that should be explicit (especially **What this is NOT**)

**When planning**: Include the Understanding file (or path) in the plan output so the user can correct it before implementation starts.

See `templates/Feature_Understanding_Template.md`.

**Visual references (screenshots):** If the user provides screenshots of similar sites or apps, save under `docs/features/assets/` (or `docs/reference/visuals/` if not feature-specific). Link from `-Understanding.md` with **similar vs different** notes so vision-capable agents can reuse them in later sessions. See [`IDEA_CAPTURE_TIPS.md`](templates/IDEA_CAPTURE_TIPS.md#visual-references-screenshots).

## 6. TODO Management

Every feature **must** have at least one companion `-TODO.md` file. Most game features will have three.

Every substantial `_shared/` component **must** have its own `-TODO.md` for foundation work (Section 2.4).

**File naming**:

- Core gameplay/systems: `FeatureName-TODO.md`
- In-Editor work: `FeatureName-InEditor-TODO.md` (rename to engine-specific — see Section 7)
- Assets & content: `FeatureName-Asset-TODO.md`
- Shared foundation: `_shared/ComponentName-TODO.md`

**Shared vs feature — cross-links**:

When a feature depends on shared foundation work, the feature TODO gets a **dependency note**, not a duplicate of the foundation tasks:

> Blocked until shared editor API exists (see [_shared/BlockEditor-TODO.md](../_shared/BlockEditor-TODO.md) — "Expose shared editing API")

When implementing the shared piece itself, tasks stay in `_shared/ComponentName-TODO.md` even if a feature motivated the work.

**Cross-feature interactions**: When work depends on or affects another feature, add a note in the TODO with a direct link. Example:

> Requires `DiffWorkflow` integration (see [DiffWorkflow-TODO.md](DiffWorkflow-TODO.md))

**Dynamic TODO creation**: Add new items as you work — implementation steps, clarifications for the user, edge cases, refactoring, follow-ups. Use High or Medium priority. See `templates/TODO_Template.md` for format.

**Workflow**:

- Before starting: Read the TODO, pick the top unchecked item.
- While working: Add new items as you discover them.
- After finishing a task: Mark `[x]`, add completion date/note.
- When a section gets long: Move finished items to Completed or archive them.
- End each session by updating the TODO file (show the updated section or confirm the file was updated).

## 7. Game Development Extensions (Unreal / Godot / Unity)

Most game features use three TODO areas:

- `FeatureName-TODO.md` — Core gameplay, systems logic, rules, simulation
- `FeatureName-InEditor-TODO.md` — Engine editor work (DataAssets, Blueprints, inspectors, editor tools, etc.)
- `FeatureName-Asset-TODO.md` — Assets, import pipelines, materials, animations, hooking content into the game

Project-level: `Project-InEditor-TODO.md`, `Project-Asset-TODO.md`

When creating In-Editor TODO files, rename immediately to the engine-specific version and update all links:

- Unreal Engine → `FeatureName-UE-TODO.md`
- Godot → `FeatureName-Godot-TODO.md`
- Unity → `FeatureName-Unity-TODO.md`

## 8. How to Split a Large Document

When a file starts feeling unwieldy:

1. Identify clean section boundaries.
2. Create a new focused file in the correct folder (`_shared/`, `features/`, etc.).
3. In the original file, replace the section with a short link:
   > **See [NewFile.md](NewFile.md) for full details.**
4. Add the new file to the Document Map in `Master_Index.md`.
5. Create matching files as needed: feature `-Understanding.md` / `-TODO.md`; shared `_shared/Component-TODO.md`
6. Update cross-references in other files.

## 9. Status Tracking (Lean Approach)

**Primary mechanism**: Each feature's `-TODO.md` (and `-InEditor-TODO.md` / `-Asset-TODO.md`) files.

- High Priority = in progress / planned
- Completed section = done

Optional: add a small "Current Status" block at the top of the main feature `.md` file.

Do not add a central `STATUS.md` unless the project truly needs a dashboard.
