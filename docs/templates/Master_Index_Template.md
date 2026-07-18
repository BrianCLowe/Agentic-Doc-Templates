<!-- template-version: 2.5 -->

> **Template reference.** Do not put project-specific content in this file. Copy to `docs/Master_Index.md` for initial setup, or diff against it when syncing template improvements into the live index. Never edit this template unless the user asks you to.
>
> **Agent workflow** (Path A/B, Understanding, TODO rules) lives in [`Modular_Docs_Workflow.md`](templates/agent/Modular_Docs_Workflow.md) — do not duplicate it here.

# [Project Name] — Master Index

**Purpose**: Single entry point for **this project's** documentation — overview, locations, and Document Map. Read only the files relevant to the current task.

**Template version**: 2.5 *(update when syncing from `templates/Master_Index_Template.md`)*  
**Workflow version**: 2.5 *(must match `templates/agent/Modular_Docs_Workflow.md` — update both on sync)*

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
| `docs/_shared/assets/` | Screenshots for shared components (linked from `-Understanding.md`) |
| `docs/features/`  | Feature-specific specs + TODOs (+ optional sub-indexes) |
| `docs/features/assets/` | Screenshots for features (linked from `-Understanding.md`) |
| `docs/reference/` | Drop zone for design docs, PRDs, chat exports, legacy specs — not the living modular docs ([Workflow](templates/agent/Modular_Docs_Workflow.md)) |
| `docs/reference/visuals/` | Optional inspiration screenshots before a feature exists |
| `docs/Tooling.md` | Machine / workflow tools (not package deps) — install on a new machine ([`Tooling_Template.md`](templates/Tooling_Template.md)) |
| `docs/Human-TODO.md` | Human procurement / external blockers (API keys, cloud bots, accounts) — agent cannot do these ([`Human_TODO_Template.md`](templates/Human_TODO_Template.md)) |
| `docs/decisions/` | Optional cross-cutting decisions ([`Decision_Template.md`](templates/Decision_Template.md)) |
| `docs/templates/` | Upstream template pack — scaffolds, `help/`, `agent/` (incl. [`Modular_Docs_Workflow.md`](templates/agent/Modular_Docs_Workflow.md), optional [`roles/`](templates/agent/roles/README.md), per-tool [`tools/`](templates/agent/tools/README.md)), `chat-ui/`; also [`VERSION`](templates/VERSION) and [`CHANGELOG.md`](templates/CHANGELOG.md) (Step B scope after sync) |
| `docs/upstream-status.yaml` | Optional — weekly template update check stamp ([`TEMPLATE_UPDATE_CHECK.md`](templates/agent/TEMPLATE_UPDATE_CHECK.md)) |
| `src/` / `backend/` / `frontend/` | Actual code (reference only) |

### 2.2 At a Glance *(policy summary — full rules in Workflow)*

- **Simplicity:** users give short doc actions; agents follow this pack — no complex prompts required.
- **Tight scope:** paved path for the current ask only — no “just in case” audits of unrelated files or alternate interpretations before acting.
- **Mermaid:** optional — agent may add a small diagram when it beats prose for structure/flow; do not splash charts everywhere.
- **Tooling:** `docs/Tooling.md` lists machine tools (not package deps); on a new machine, user can ask to install them ([`Tooling_Template.md`](templates/Tooling_Template.md)).
- **Human TODO:** `docs/Human-TODO.md` — accounts, keys, portal registrations the agent cannot complete ([`Human_TODO_Template.md`](templates/Human_TODO_Template.md); [Workflow §13](templates/agent/Modular_Docs_Workflow.md#13-human-todo-procurement--external-blockers)).
- **File layout:** flat sibling files — `features/FeatureName.md`, `FeatureName-Understanding.md`, `FeatureName-TODO.md` (same for `_shared/`) — see [Workflow §0](templates/agent/Modular_Docs_Workflow.md#0-naming--file-layout-read-before-creating-files).
- No file should exceed ~800–1000 lines; split when bloated ([Workflow §8](templates/agent/Modular_Docs_Workflow.md#8-how-to-split-a-large-document)).
- **Shared** only when something is actually shared across features — empty §3.1 / `_shared/` is fine. Do **not** invent shared rows or park engine/framework primers there ([Workflow §1](templates/agent/Modular_Docs_Workflow.md#1-shared-components--foundation-vs-consumption)). Real shared components get the **same note types as features** unless the **user** excepted them — record omissions in **§3.0** only after an explicit user request. Agents must not invent §3.0 or filler §3.1 rows.
- **Understanding**: agent drafts first (`draft`); user reviews before build; **`confirmed`** = approved — agents continue without re-asking ([Workflow §4](templates/agent/Modular_Docs_Workflow.md#4-understanding-features--shared)).
- **Spec**: durable contract after Understanding is `confirmed` ([Workflow §2](templates/agent/Modular_Docs_Workflow.md#2-understanding--spec-graduation)).
- **Shared maturity** on spec + Document Map: `draft` \| `usable` \| `stable`.

## 3. Document Map

### 3.0 Note-type exceptions *(registry)*

Record **only** omissions the **user explicitly requested**. Agents must **not** invent exceptions to match incomplete docs, save time, or “leave for later.”

| Component / Feature | Omitted note types | Recorded |
|---------------------|-------------------|----------|
| *(example)* BlockEditor | InEditor-TODO, Asset-TODO | 2026-06-15 — **user said** “no asset or in-editor work for BlockEditor” |
| [Add rows only after user excepts] | | |

**Default file set** (create on disk when you add a row — map-only “planned” rows are not allowed): Spec + Understanding + core TODO. InEditor / Asset TODOs when that work applies. **Never omit Understanding or the core TODO** unless the user explicitly excepted them for that item. Understanding may be `draft`; that still requires the file to exist.

### 3.1 Shared / Core Components

Leave this table **empty** (or with a single “*(none yet)*” note) unless a piece is truly shared across features. Do not invent rows or park engine/framework overviews here.

| Component | Maturity | Spec | Understanding | Gameplay TODO | InEditor TODO | Asset TODO |
|-----------|----------|------|---------------|---------------|---------------|------------|
| *(example — only if actually shared)* BlockEditor | draft | [_shared/BlockEditor.md](_shared/BlockEditor.md) | [_shared/BlockEditor-Understanding.md](_shared/BlockEditor-Understanding.md) | [_shared/BlockEditor-TODO.md](_shared/BlockEditor-TODO.md) | … | … |
| *(optional)* | — | [_shared/_Foundation-TODO.md](_shared/_Foundation-TODO.md) | — | *(this file)* | — | — |

**Maturity** (shared only): `draft` · `usable` · `stable`. Omit TODO columns only when recorded in §3.0.

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
| **Human / procurement** (API keys, Azure/Teams bots, accounts, purchases) | [Human-TODO.md](Human-TODO.md) |
| Project-wide In-Editor work (DataAssets, Blueprints, custom inspectors, etc.) | [Project-InEditor-TODO.md](Project-InEditor-TODO.md) |
| Project-wide Assets & Content | [Project-Asset-TODO.md](Project-Asset-TODO.md) |

### 3.4 Reference, Decisions, Tooling & Legacy

| Document | Description |
|----------|-------------|
| [Human-TODO.md](Human-TODO.md) | Human procurement checklist — agent drafts rows; you complete ([`Human_TODO_Template.md`](templates/Human_TODO_Template.md)) |
| [Tooling.md](Tooling.md) | Machine / workflow tools — install on a new machine ([`Tooling_Template.md`](templates/Tooling_Template.md)) |
| [decisions/](decisions/) | Optional cross-cutting decision files ([`Decision_Template.md`](templates/Decision_Template.md)) |
| [reference/LegacySpec.md](reference/LegacySpec.md) | Older detailed spec (read only when needed) |

## 4. Quick Start

1. Read this file — find the feature or shared component in **§3 Document Map**.
2. Follow **[`templates/agent/Modular_Docs_Workflow.md`](templates/agent/Modular_Docs_Workflow.md)** — Path A (`_shared/` foundation) or Path B (feature work).
3. End the session by updating the active TODO **Current focus** ([Workflow §5.1](templates/agent/Modular_Docs_Workflow.md#51-session-handoff--current-focus)).

**Agents:** The installed modular documentation rule is a short checklist; full procedure is in `Modular_Docs_Workflow.md`.
