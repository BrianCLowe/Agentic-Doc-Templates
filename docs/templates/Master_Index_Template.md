<!-- pack-version: 2.7.17 -->

> **Template reference.** Do not put project-specific content in this file. Copy to `docs/Master_Index.md` for initial setup, or diff against it when syncing template improvements into the live index. Never edit this template unless the user asks you to.
>
> **Agent workflow** (paved path + router into thin modules) lives in [`Modular_Docs_Workflow.md`](templates/agent/Modular_Docs_Workflow.md) — do not duplicate it here.

# [Project Name] — Master Index

**Purpose**: Single entry point for **this project's** documentation — overview, locations, and Document Map. Read only the files relevant to the current task.

**Pack version**: 2.7.17 *(from [`templates/VERSION`](templates/VERSION) — update on sync)*

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
| `docs/ADT-settings.yaml` | Pack preferences — **docs profile**, **orchestrator git**, **standing.instructions** (freeform process prefs), sync mode, tools, optionals, upstream stamps ([`ADT-settings.example.yaml`](templates/agent/ADT-settings.example.yaml); Workflow [§0.1](templates/agent/workflow/profile-standing.md#01-docs-profile-ceremony-modes) · [§0.2](templates/agent/workflow/profile-standing.md#02-standing-workflow-instructions-user-workflow-not-pack-enums); [orchestrator Git](templates/agent/roles/orchestrator.md)) |
| `src/` / `backend/` / `frontend/` | Actual code (reference only) |

### 2.2 At a Glance *(policy summary — full rules in Workflow)*

- **Simplicity:** users give short doc actions; agents follow this pack — no complex prompts required.
- **Idea sources:** prefer raw **chat exports** in `docs/reference/` over polished-only design docs — they keep whys/motives for Understanding drafts ([`IDEA_CAPTURE_TIPS.md`](templates/help/IDEA_CAPTURE_TIPS.md)). Ask: *build or update live docs from reference.* Agents keep **one identity per stem** (split unlike features — no user reminder required).
- **Tight scope:** paved path for the current ask only — no “just in case” audits of unrelated files or alternate interpretations before acting.
- **Mermaid:** optional — agent may add a small diagram when it beats prose for structure/flow; do not splash charts everywhere.
- **Tooling:** `docs/Tooling.md` lists machine tools (not package deps); on a new machine, user can ask to install them ([`Tooling_Template.md`](templates/Tooling_Template.md)).
- **Human TODO:** `docs/Human-TODO.md` — one inbox for procure / playtest / decide / waiting; index + owner dual-write ([`Human_TODO_Template.md`](templates/Human_TODO_Template.md); [Workflow §13](templates/agent/workflow/human-todo.md#13-human-todo-inbox--needs-a-human)).
- **Docs profile:** `docs/ADT-settings.yaml` → `docs_profile.mode` — **`prevent`** (default if unset: Understanding + shape confirm), **`balanced`**, or **`ship-first`** (Spec+TODO core). See [Workflow §0.1](templates/agent/workflow/profile-standing.md#01-docs-profile-ceremony-modes).
- **Orchestrator git:** `orchestrator.git.mode` — recommend **`branch-pr-squash`** (Bugbot / tip-only bots), or **`branch-pr`**, **`branch-push`**, **`local`**, **`current-push`** (never silent-default), or **`none`**. Asked if unset even under sync `auto-all`. **Cloud Agent** orchestration this-runs **`branch-pr-squash`** when durable mode is local-oriented (does not rewrite settings). See [orchestrator-git](templates/agent/roles/orchestrator-git.md).
- **File layout:** flat sibling files — always `features/FeatureName.md` + `FeatureName-TODO.md`; **Understanding** per docs profile; optional `FeatureName-Catalog.md` for list-heavy stems (same for `_shared/`) — [Workflow §0](templates/agent/workflow/naming-layout.md#0-naming--file-layout-read-before-creating-files) / [§7.1](templates/agent/workflow/extensions.md#71-catalog-companions-list-heavy-content).
- No file should exceed ~800–1000 lines; split when bloated ([Workflow §8](templates/agent/workflow/extensions.md#8-how-to-split-a-large-document)).
- **Shared** only when something is actually shared across features — empty §3.1 / `_shared/` is fine. Do **not** invent shared rows or park engine/framework primers there ([Workflow §1](templates/agent/workflow/shared-components.md#1-shared-components--foundation-vs-consumption)). Real shared components get the **same note types as features** (for the profile) unless the **user** excepted them — record omissions in **§3.0** only after an explicit user request. Agents must not invent §3.0 or filler §3.1 rows.
- **Understanding** *(when profile requires / user locks shape)*: agent drafts **shape / guardrails** first (`draft`); user confirms is / is not + Assumptions (not a full-spec review); **`confirmed`** = shape approved — agents continue without re-asking ([Workflow §4](templates/agent/workflow/understanding.md#4-understanding-features--shared)).
- **Spec**: durable contract (after shape confirm when Understanding is used; or grown as you build under ship-first) — may hold detail that was never in Understanding ([Workflow §2](templates/agent/workflow/understanding.md#2-understanding--spec-graduation)).
- **Shared maturity** on spec + Document Map: `draft` \| `usable` \| `stable`.

## 3. Document Map

### 3.0 Note-type exceptions *(registry)*

Record **only** omissions the **user explicitly requested**. Agents must **not** invent exceptions to match incomplete docs, save time, or “leave for later.”

| Component / Feature | Omitted note types | Recorded |
|---------------------|-------------------|----------|
| *(example)* BlockEditor | InEditor-TODO, Asset-TODO | 2026-06-15 — **user said** “no asset or in-editor work for BlockEditor” |
| [Add rows only after user excepts] | | |

**Default file set** (create on disk when you add a row — map-only “planned” rows are not allowed): **always** Spec + core TODO; **Understanding** per `docs_profile` ([Workflow §0.1](templates/agent/workflow/profile-standing.md#01-docs-profile-ceremony-modes)). InEditor / Asset TODOs when that work applies. Optional **Catalog** for list-heavy stems ([Workflow §7.1](templates/agent/workflow/extensions.md#71-catalog-companions-list-heavy-content)) — create the file the same turn you add a Catalog map cell. Under **`prevent`**, never omit Understanding unless the user explicitly excepted that item (§3.0). Understanding may be `draft`; that still requires the file when the profile requires it.

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
