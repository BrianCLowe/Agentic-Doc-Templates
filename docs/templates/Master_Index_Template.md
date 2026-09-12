> **Template reference.** Do not put project-specific content in this file. Copy to `docs/Master_Index.md` for initial setup, or diff against it when syncing template improvements into the live index. Never edit this template unless the user asks you to.
>
> **Agent workflow** (paved path + router into thin modules) lives in [`Modular_Docs_Workflow.md`](templates/agent/Modular_Docs_Workflow.md) — do not duplicate it here.

# [Project Name] — Master Index

**Purpose**: Single entry point for **this project's** documentation — overview, locations, and Document Map. Read only the files relevant to the current task.

**Pack version**: *(set from [`templates/VERSION`](templates/VERSION) on bootstrap / TEMPLATE_SYNC — do not bump this template)*

## 1. Project Overview

[1–3 short paragraphs describing what the project is, its core architecture, and primary goals. Keep it high-level — details live in feature files.]

### 1.1 Project Profile *(optional — fill once)*

| Field | Value |
|-------|--------|
| **Project type** | e.g. game (Unreal) \| web app \| API \| mixed |
| **TODO labels** | Default: Gameplay / InEditor / Asset — or rename in Document Map (e.g. Core / Infra / Content) |
| **Engine / stack** | e.g. UE 5.4, Next.js, … |
| **Game extensions** | Use Workflow §7 \| Skip — use Project Profile labels only |

Rename TODO suffixes in the Document Map when not using game terminology.

## 2. Key Locations & At a Glance

### 2.1 Key Locations

| Path              | Purpose |
|-------------------|---------|
| `docs/`           | All specs, architecture, and tracking |
| `docs/_shared/`   | Reusable **project** components used by multiple features (may be empty — do not invent filler) |
| `docs/_shared/assets/` | Screenshots for shared components (linked from the shared **spec** **Visual references**) |
| `docs/features/`  | Feature-specific specs + TODOs (+ optional sub-indexes) |
| `docs/features/assets/` | Screenshots for features (linked from the feature **spec** **Visual references**) |
| `docs/reference/` | **Recommended:** chat exports (md) of idea threads — also design docs / PRDs / legacy specs. Not living modular docs ([Workflow](templates/agent/Modular_Docs_Workflow.md); tips: [`help/IDEA_CAPTURE_TIPS.md`](templates/help/IDEA_CAPTURE_TIPS.md)) |
| `docs/reference/visuals/` | Optional inspiration screenshots before a feature exists |
| `docs/Tooling.md` | Machine / workflow tools (not package deps) — install on a new machine ([`Tooling_Template.md`](templates/Tooling_Template.md)) |
| `docs/Human-TODO.md` | Human inbox — procure, playtest, decide, waiting (agent cannot close from assumptions) ([`Human_TODO_Template.md`](templates/Human_TODO_Template.md)) |
| `docs/decisions/` | Optional cross-cutting decisions ([`Decision_Template.md`](templates/Decision_Template.md)) |
| `docs/templates/` | Upstream template pack — scaffolds, `help/`, `agent/` (incl. [`Modular_Docs_Workflow.md`](templates/agent/Modular_Docs_Workflow.md) index + [`workflow/`](templates/agent/workflow/README.md) modules, optional [`roles/`](templates/agent/roles/README.md), per-tool [`tools/`](templates/agent/tools/README.md)); also [`VERSION`](templates/VERSION) and [`CHANGELOG.md`](templates/CHANGELOG.md) (Step B scope after sync) |
| `docs/ADT-settings.yaml` | Pack preferences — **docs profile**, **orchestrator git**, **standing.instructions** (playbook overrides, not a notes pad), sync mode, tools, optionals, upstream stamps ([`ADT-settings.example.yaml`](templates/agent/ADT-settings.example.yaml); Workflow [§0.1](templates/agent/workflow/profile-standing.md#01-docs-profile-ceremony-modes) · [§0.2](templates/agent/workflow/profile-standing.md#02-standing-workflow-instructions-user-workflow-not-pack-enums); [orchestrator Git](templates/agent/roles/orchestrator.md)) |
| `src/` / `backend/` / `frontend/` | Actual code (reference only) |

### 2.2 At a Glance *(pointers — full rules in the workflow)*

| Topic | Where the rule lives |
|-------|----------------------|
| **Docs profile** | `docs/ADT-settings.yaml` → `docs_profile.mode`. **`prevent`** = editors / games / multi-surface (default if unset). **`ship-first`** = typed APIs / CRUD. **`balanced`** = mixed. [§0.1](templates/agent/workflow/profile-standing.md#01-docs-profile-ceremony-modes) |
| **Orchestrator git** | `orchestrator.git.mode` — ask if unset. Host worktrees: already-in-a-worktree → stay; pack does not `git worktree add`. [orchestrator-git](templates/agent/roles/orchestrator-git.md) |
| **File layout / kit leftovers** | Flat sibling files; no map-only planned rows; leftovers stay as TODOs on an existing stem. [§0](templates/agent/workflow/naming-layout.md#0-naming--file-layout-read-before-creating-files) · [§5.4](templates/agent/workflow/todos.md#54-finished-kit-contract--covering-todos-not-wait-for-pickup) |
| **Understanding / Spec** | Shape vs contract. [§4](templates/agent/workflow/understanding.md#4-understanding-features--shared) · [§2](templates/agent/workflow/understanding.md#2-understanding--spec-graduation) |
| **Shared** | Only when actually shared. Same note types as features unless the user excepted them in §3.0. [§1](templates/agent/workflow/shared-components.md#1-shared-components--foundation-vs-consumption) |
| **Human inbox / Tooling** | [`Human-TODO.md`](Human-TODO.md) · [`Tooling.md`](Tooling.md) |
| **Size / split** | Split when a file is bloated. [§8](templates/agent/workflow/extensions.md#8-how-to-split-a-large-document) |

Do **not** paste playbook procedure into this table. Compaction: re-open the [workflow index](templates/agent/Modular_Docs_Workflow.md), then one module.

## 3. Document Map

### 3.0 Note-type exceptions *(registry)*

Record **only** omissions the **user explicitly requested**. Agents must **not** invent exceptions to match incomplete docs, save time, or “leave for later.”

| Component / Feature | Omitted note types | Recorded |
|---------------------|-------------------|----------|
| *(example)* BlockEditor | InEditor-TODO, Asset-TODO | 2026-06-15 — **user said** “no asset or in-editor work for BlockEditor” |
| [Add rows only after user excepts] | | |

**Default file set** when adding a row (same turn, on disk — no map-only “planned” rows): Spec + core TODO; **Understanding** per `docs_profile`; InEditor / Asset / Catalog when that work applies. [§0](templates/agent/workflow/naming-layout.md#0-naming--file-layout-read-before-creating-files) · [§0.1](templates/agent/workflow/profile-standing.md#01-docs-profile-ceremony-modes).

### 3.1 Shared / Core Components

Leave this table **empty** (or with a single “*(none yet)*” note) unless a piece is truly shared across features. Do not invent rows or park engine/framework overviews here.

| Component | Maturity | Spec | Understanding | Catalog | Gameplay TODO | InEditor TODO | Asset TODO |
|-----------|----------|------|---------------|---------|---------------|---------------|------------|
| *(example — only if actually shared)* BlockEditor | draft | [_shared/BlockEditor.md](_shared/BlockEditor.md) | [_shared/BlockEditor-Understanding.md](_shared/BlockEditor-Understanding.md) | — | [_shared/BlockEditor-TODO.md](_shared/BlockEditor-TODO.md) | … | … |
| *(optional)* | — | [_shared/_Foundation-TODO.md](_shared/_Foundation-TODO.md) | — | — | *(this file)* | — | — |

**Maturity** (shared only): `draft` · `usable` · `stable`. Omit TODO columns only when recorded in §3.0. Use **Catalog** when a shared piece has a row registry; otherwise `—`.

### 3.2 Features & Modules

| Feature          | Spec / Index                                      | Understanding | Catalog | Gameplay TODO | InEditor TODO | Asset TODO |
|------------------|---------------------------------------------------|---------------|---------|---------------|---------------|------------|
| Main Workspace   | [features/MainWorkspace.md](features/MainWorkspace.md) | [features/MainWorkspace-Understanding.md](features/MainWorkspace-Understanding.md) | — | [features/MainWorkspace-TODO.md](features/MainWorkspace-TODO.md) | [features/MainWorkspace-InEditor-TODO.md](features/MainWorkspace-InEditor-TODO.md) | [features/MainWorkspace-Asset-TODO.md](features/MainWorkspace-Asset-TODO.md) |
| Diff Workflow    | [features/DiffWorkflow.md](features/DiffWorkflow.md)     | [features/DiffWorkflow-Understanding.md](features/DiffWorkflow-Understanding.md) | — | [features/DiffWorkflow-TODO.md](features/DiffWorkflow-TODO.md) | [features/DiffWorkflow-InEditor-TODO.md](features/DiffWorkflow-InEditor-TODO.md) | [features/DiffWorkflow-Asset-TODO.md](features/DiffWorkflow-Asset-TODO.md) |
| World Building   | [features/WorldBuilding-Index.md](...) *(sub-index)* | [features/WorldBuilding-Understanding.md](...) | — | [features/WorldBuilding-TODO.md](...) | [features/WorldBuilding-InEditor-TODO.md](...) | [features/WorldBuilding-Asset-TODO.md](...) |
| [Add more rows as needed] | | | | | | |

### 3.3 Project-Level Work

| Area          | TODO File |
|---------------|-----------|
| **Human inbox** (procure, playtest, decide, waiting) | [Human-TODO.md](Human-TODO.md) |
| Project-wide In-Editor work (DataAssets, Blueprints, custom inspectors, etc.) | [Project-InEditor-TODO.md](Project-InEditor-TODO.md) |
| Project-wide Assets & Content | [Project-Asset-TODO.md](Project-Asset-TODO.md) |

### 3.4 Reference, Decisions, Tooling & Legacy

| Document | Description |
|----------|-------------|
| [Human-TODO.md](Human-TODO.md) | Human inbox — agent dual-writes rows; you complete / give feedback in chat ([`Human_TODO_Template.md`](templates/Human_TODO_Template.md)) |
| [Tooling.md](Tooling.md) | Machine / workflow tools — install on a new machine ([`Tooling_Template.md`](templates/Tooling_Template.md)) |
| [decisions/](decisions/) | Optional cross-cutting decision files ([`Decision_Template.md`](templates/Decision_Template.md)) |
| [reference/LegacySpec.md](reference/LegacySpec.md) | Older detailed spec (read only when needed) |

## 4. Quick Start

1. Read this file — find the feature or shared component in **§3 Document Map**.
2. Follow **[`templates/agent/Modular_Docs_Workflow.md`](templates/agent/Modular_Docs_Workflow.md)** (paved path) — Path A/B detail in [`workflow/implement.md`](templates/agent/workflow/implement.md) when needed.
3. End the session by updating the active TODO **Current focus** ([Workflow §5.1](templates/agent/workflow/todos.md#51-session-handoff--current-focus)).

**Agents:** The installed modular documentation rule is a short checklist; procedure is the workflow **index** then **one** module under `templates/agent/workflow/`.
