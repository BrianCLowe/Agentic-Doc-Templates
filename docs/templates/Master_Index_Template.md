<!-- template-version: 1.6 -->

> **Template reference.** Do not put project-specific content in this file. Copy to `docs/Master_Index.md` for initial setup, or diff against it when syncing template improvements into the live index. Never edit this template unless the user asks you to.

# [Project Name] — Master Index

**Purpose**: Single entry point for all documentation. Read only the files relevant to the current task.

**Template version**: 1.6 *(update this line in `docs/Master_Index.md` when syncing from `templates/Master_Index_Template.md`)*

## 1. Project Overview

[1–3 short paragraphs describing what the project is, its core architecture, and primary goals. Keep it high-level — details live in feature files.]

### 1.1 Project Profile *(optional — fill once, helps agents and humans)*

| Field | Value |
|-------|--------|
| **Project type** | e.g. game (Unreal) \| web app \| API \| mixed |
| **TODO labels** | Default: Gameplay / InEditor / Asset — or rename in Document Map (e.g. Core / Infra / Content) |
| **Engine / stack** | e.g. UE 5.4, Next.js, … — agent may propose if unknown |
| **Section 7** | Use game extensions (Section 7) \| Skip — use Project Profile labels only |

Rename TODO suffixes in the Document Map when not using game terminology. Section 7 is optional for non-game projects.

## 2. Project Structure & Philosophy

### 2.1 Key Locations

| Path              | Purpose |
|-------------------|---------|
| `docs/`           | All specs, architecture, and tracking |
| `docs/_shared/`   | Reusable components, patterns, and **their foundation TODOs** |
| `docs/_shared/assets/` | Reference **screenshots** for shared components (linked from `-Understanding.md`) |
| `docs/features/`  | Feature-specific specs + TODOs (+ optional sub-indexes) |
| `docs/features/assets/` | Reference **screenshots** for features (linked from `-Understanding.md`) |
| `docs/reference/visuals/` | Optional inspiration screenshots not tied to one feature yet |
| `docs/decisions/` | Optional cross-cutting **Decisions** (project-wide choices — see Section 10) |
| `docs/templates/` | Canonical templates — reference for structure and sync |
| `src/` / `backend/` / `frontend/` | Actual code (reference only) |

### 2.2 Modular Rules

- No file should exceed ~800–1000 lines.
- Shared concepts → `_shared/` — each substantial shared component gets the **same note types as a feature** (spec, Understanding, and focused TODOs — see Sections 2.4 and 5) unless the user **explicitly excepts** specific files for that component
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

**Each substantial shared component** gets the **full set of note types** — same as a feature — unless the user explicitly says otherwise for that component:

- `_shared/ComponentName.md` — spec / contract / architecture
- `_shared/ComponentName-Understanding.md` — agent model of user intent for this shared piece (see Section 5)
- `_shared/ComponentName-TODO.md` — core / systems / foundation tasks
- `_shared/ComponentName-InEditor-TODO.md` — engine editor work *(when applicable)*
- `_shared/ComponentName-Asset-TODO.md` — assets & content *(when applicable)*

**Exceptions:** If the user says a shared component does not need a particular note type (e.g. "BlockEditor has no asset work"), omit that file and record the exception in **Section 3.0**. Do **not** skip Understanding or TODO by default — only when the user explicitly excepts them.

**Maturity** *(shared components only)*: Set on the shared **spec** (`draft` | `usable` | `stable`) so consumer features know whether integration is safe. Update when foundation work progresses — see [`Feature_Spec_Template.md`](templates/Feature_Spec_Template.md).

**Where tasks go** (agents often get this wrong):

| Work type | Put tasks in | Not in |
|-----------|--------------|--------|
| Building or refactoring the shared component itself | `_shared/ComponentName-TODO.md` | A consumer feature's TODO |
| Feature blocked until shared work is done | Consumer feature TODO — **dependency note + link** only | Duplicating foundation tasks in the feature TODO |
| Feature-specific wiring / UI using the shared piece | That feature's TODO | `_shared/ComponentName-TODO.md` |

**Example**: Extract a reusable text-editor core into `_shared/BlockEditor.md`. Tasks to create that core → `_shared/BlockEditor-TODO.md`. A role-specific UI that *uses* the core → `RoleEditor-TODO.md` with a note: *Depends on [BlockEditor-TODO.md](BlockEditor-TODO.md) item "Expose shared editing API"* — not the extraction tasks themselves.

Optional: `_shared/_Foundation-TODO.md` for cross-cutting shared work that does not belong to one component file yet.

### 2.5 Understanding → Spec graduation

| File | Role | When to update |
|------|------|----------------|
| `-Understanding.md` | Agent's interpretation; user reviews **before** build | Scoping, planning, corrections |
| `.md` spec (feature or `_shared/`) | **Durable contract** — architecture, API, decisions | After Understanding is `confirmed`; when code and docs must match |

**Workflow:**

1. Agent drafts `-Understanding.md` → user confirms (`confirmed`).
2. Agent **graduates** stable content into the spec: overview, architecture/contract, **Decisions**, dependencies, maturity (shared).
3. Understanding keeps intent, boundaries, acceptance criteria, and correction history; spec holds what implementers and future agents should treat as truth.
4. If implementation diverges, update the spec **or** set Understanding to `superseded` and draft a revision (Section 5) — do not leave both stale.

See [`Feature_Spec_Template.md`](templates/Feature_Spec_Template.md) and [`Feature_Understanding_Template.md`](templates/Feature_Understanding_Template.md).

## 3. Document Map

### 3.0 Note-type exceptions *(registry)*

Record every user exception here so agents do not recreate omitted files.

| Component / Feature | Omitted note types | Recorded |
|---------------------|-------------------|----------|
| *(example)* BlockEditor | InEditor-TODO, Asset-TODO | 2026-06-15 — user |
| [Add rows as needed] | | |

### 3.1 Shared / Core Components

| Component | Maturity | Spec | Understanding | Gameplay TODO | InEditor TODO | Asset TODO |
|-----------|----------|------|---------------|---------------|---------------|------------|
| Core Concept 1 | draft | [_shared/CoreConcept1.md](_shared/CoreConcept1.md) | [_shared/CoreConcept1-Understanding.md](_shared/CoreConcept1-Understanding.md) | [_shared/CoreConcept1-TODO.md](_shared/CoreConcept1-TODO.md) | [_shared/CoreConcept1-InEditor-TODO.md](_shared/CoreConcept1-InEditor-TODO.md) | [_shared/CoreConcept1-Asset-TODO.md](_shared/CoreConcept1-Asset-TODO.md) |
| Core Concept 2 | usable | [_shared/CoreConcept2.md](_shared/CoreConcept2.md) | [_shared/CoreConcept2-Understanding.md](_shared/CoreConcept2-Understanding.md) | [_shared/CoreConcept2-TODO.md](_shared/CoreConcept2-TODO.md) | ... | ... |
| *(optional)* | — | [_shared/_Foundation-TODO.md](_shared/_Foundation-TODO.md) | — | *(this file)* | — | — |

**Maturity** (shared only): `draft` = foundation incomplete · `usable` = features may integrate · `stable` = breaking changes need explicit discussion. Also set on the shared spec file. Omit TODO columns only when recorded in Section 3.0.

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

### 3.4 Reference, Decisions & Legacy

| Document | Description |
|----------|-------------|
| [decisions/](decisions/) | Optional cross-cutting decision files ([`Decision_Template.md`](templates/Decision_Template.md)) |
| [reference/LegacySpec.md](reference/LegacySpec.md) | Older detailed spec (read only when needed) |

## 4. Quick Start — Working on Any Task

**Always follow this order:**

1. Read `Master_Index.md` (this file) — Sections 1–6
2. Decide: **shared foundation work** or **feature work** (Section 2.4)

### Path A — Shared foundation work

Use when building or changing a reusable component, API, or pattern in `_shared/`.

1. Open `_shared/[ComponentName].md`
2. Open `_shared/[ComponentName]-Understanding.md` — **draft or update first** from the conversation when discussing, planning, or scoping; show the user for review (same rules as features — Section 5)
3. Open the relevant shared TODO file(s) (create from `templates/TODO_Template.md` if missing):
   - Core / foundation → `_shared/[ComponentName]-TODO.md`
   - In-Editor work → `_shared/[ComponentName]-InEditor-TODO.md` *(unless user excepted)*
   - Assets & content → `_shared/[ComponentName]-Asset-TODO.md` *(unless user excepted)*
4. Do the work (only after Understanding is `confirmed` or the user explicitly waives review)
5. **Graduate** confirmed content into `_shared/[ComponentName].md` if the spec is still placeholder (Section 2.5)
6. **Update the shared TODO file(s)** before ending the session — refresh **Current focus** (Section 6)
7. If consumer features are blocked, ensure their TODOs link here — do not copy foundation tasks into feature TODOs

### Path B — Feature work

1. Read any `_shared/` documents listed as relevant in Section 3.1 (read-only context unless Path A)
2. Open `features/[FeatureName].md`
3. Open `features/[FeatureName]-Understanding.md` — **draft or update first** from the conversation when discussing, planning, or scoping; show the user for review
4. Open the relevant feature TODO file(s):
   - Core gameplay/systems → `features/[FeatureName]-TODO.md`
   - In-Editor work → `features/[FeatureName]-InEditor-TODO.md` (or engine-specific version)
   - Assets & content → `features/[FeatureName]-Asset-TODO.md`
5. Do the work (only after Understanding is `confirmed` or the user explicitly waives review)
6. **Graduate** confirmed content into `features/[FeatureName].md` if the spec is still placeholder (Section 2.5)
7. **Update the feature TODO file(s)** before ending the session — refresh **Current focus** (Section 6)

If the work is really shared foundation, **stop** — use Path A instead.

**Golden Rule**: If you find yourself scrolling through a long file, stop and split it.

## 5. Understanding (Features & Shared)

Each **feature** and each substantial **shared component** should have a `-Understanding.md` file — the agent's model of **what the user wants**: scope, behavior, UI intent, and how the work relates to existing pieces.

- Features: `features/FeatureName-Understanding.md`
- Shared: `_shared/ComponentName-Understanding.md`

**Who writes it:** The **agent writes first** (status `draft`) from the conversation, design doc, or interview. The **user reviews and corrects** — they do not need to author this file from scratch. The point is to show the user how the agent interpreted the request *before* anyone codes.

**Default:** Agent drafts Understanding for shared components the same way as for features. **Only skip** when the user explicitly excepts it for that component.

**Purpose**:

- Catch misread scope early (e.g. "alternate UI for existing editor" vs "brand-new editor")
- Give the user a short, readable artifact to **review and correct** before code is written — not a form for them to fill out
- Attach to plans and discussions so corrections happen at planning time

**Status**:

| Status | Meaning |
|--------|---------|
| `draft` | Agent wrote or updated; user has not approved — **do not implement** unless user waives |
| `reviewed` | User skimmed; minor edits may remain |
| `confirmed` | User approved — OK to implement per this understanding; **graduate to spec** (Section 2.5) |
| `superseded` | No longer accurate — code or plan changed; agent should draft a new revision or reconcile explicitly |

**Reconciliation:** If shipped code diverges from a `confirmed` Understanding, either update the spec to match reality and note **Last reconciled with code** on both files, or set status to `superseded` and draft a new Understanding. Do not treat stale `confirmed` as current without checking.

**When to create or update** *(agent responsibility unless user edits directly)*:

- User describes a new feature or change → agent drafts or updates Understanding
- User asks for a plan, spec review, or "how should we build this" → agent drafts Understanding first, then plan
- Agent discovers a scope assumption that should be explicit (especially **What this is NOT**)
- User corrects the agent → agent updates Understanding immediately (especially **What this is NOT**)

**When planning**: Include the Understanding file (or path) in the plan output so the user can correct it before implementation starts.

See `templates/Feature_Understanding_Template.md`.

**Acceptance criteria:** The agent drafts **Done when** checkboxes in Understanding so the user can confirm completeness without reading every TODO. See template.

**Visual references (screenshots):** If the user provides screenshots of similar sites or apps, save under `docs/features/assets/`, `docs/_shared/assets/`, or `docs/reference/visuals/` as appropriate. Link from `-Understanding.md` with **similar vs different** notes so vision-capable agents can reuse them in later sessions. See [`IDEA_CAPTURE_TIPS.md`](templates/IDEA_CAPTURE_TIPS.md#visual-references-screenshots).

## 6. TODO Management

Every feature **must** have at least one companion `-TODO.md` file. Most game features will have three.

Every substantial `_shared/` component gets the **same TODO file set as a feature** (Section 2.4) unless the user explicitly excepts specific files.

**File naming**:

- Core gameplay/systems: `FeatureName-TODO.md` or `_shared/ComponentName-TODO.md`
- In-Editor work: `FeatureName-InEditor-TODO.md` or `_shared/ComponentName-InEditor-TODO.md` (rename to engine-specific — see Section 7)
- Assets & content: `FeatureName-Asset-TODO.md` or `_shared/ComponentName-Asset-TODO.md`
- Understanding: `FeatureName-Understanding.md` or `_shared/ComponentName-Understanding.md`

**Shared vs feature — cross-links**:

When a feature depends on shared foundation work, the feature TODO gets a **dependency note**, not a duplicate of the foundation tasks:

> Blocked until shared editor API exists (see [_shared/BlockEditor-TODO.md](../_shared/BlockEditor-TODO.md) — "Expose shared editing API")

When implementing the shared piece itself, tasks stay in `_shared/ComponentName-TODO.md` even if a feature motivated the work.

**Cross-feature interactions**: When work depends on or affects another feature, add a note in the TODO with a direct link. Example:

> Requires `DiffWorkflow` integration (see [DiffWorkflow-TODO.md](DiffWorkflow-TODO.md))

**Dynamic TODO creation**: Add new items as you work — implementation steps, clarifications for the user, edge cases, refactoring, follow-ups. Use High or Medium priority. See `templates/TODO_Template.md` for format.

**Workflow**:

- **Session start:** Read the active TODO's **Current focus** block first (Section 6) — then High Priority.
- Before starting: Pick the top unchecked item (or continue Current focus).
- While working: Add new items as you discover them.
- After finishing a task: Mark `[x]`, add completion date/note.
- When a section gets long: Move finished items to Completed or archive them (`-todo-complete.md`).
- **Session end:** Update **Current focus** for the next session; update the TODO file (show the updated section or confirm the file was updated).

### 6.1 Session handoff — Current focus

Each active `-TODO.md` should keep a short **Current focus** block at the top (see [`TODO_Template.md`](templates/TODO_Template.md)):

- One active task (or "blocked by …")
- Blockers with links
- Optional: last session date / agent tool

This gives the next agent (or a different tool) a 5-second orientation without re-reading everything.

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
5. Create matching files as needed: full note set for features and shared components (spec from [`Feature_Spec_Template.md`](templates/Feature_Spec_Template.md), `-Understanding.md`, `-TODO.md`, and InEditor/Asset TODOs when applicable) unless recorded in Section 3.0
6. Update cross-references in other files.

## 9. Status Tracking (Lean Approach)

**Primary mechanism**: Each feature's and shared component's `-TODO.md` (and `-InEditor-TODO.md` / `-Asset-TODO.md`) files.

- High Priority = in progress / planned
- Completed section = done

Optional: add a small "Current Status" block at the top of the main feature `.md` file.

Do not add a central `STATUS.md` unless the project truly needs a dashboard.

## 10. Decisions *(lightweight)*

Record **why** something was chosen — not every task, only choices with lasting impact.

| Where | Use for |
|-------|---------|
| **Decisions** section in feature or shared **spec** | Choices local to that piece (see [`Feature_Spec_Template.md`](templates/Feature_Spec_Template.md)) |
| `docs/decisions/YYYY-MM-DD-short-title.md` | Cross-cutting or project-wide choices (optional) |

When the user confirms a tradeoff during Understanding review, the agent adds a row to the spec **Decisions** table (and graduates it from Understanding if noted there). Link from Master_Index Section 3.4 if you add standalone decision files.
