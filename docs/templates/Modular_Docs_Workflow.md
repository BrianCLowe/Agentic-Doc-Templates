<!-- workflow-version: 2.0 -->

> **Agent workflow reference.** Canonical instructions for how to work the modular doc system. Lives in `docs/templates/` — sync from upstream; do **not** copy wholesale into `docs/Master_Index.md`. The live index links here; agent rules summarize and point here for full procedure.

# Modular Documentation — Agent Workflow

**Workflow version**: 2.0 *(sync with `Master_Index.md` **Workflow version** line when updating)*

**Design intent:** Users give short requests about the docs (“bootstrap”, “draft Understanding for X”, “update the templates”). You read this pack and act — they should not need complex prompts or step-by-step instructions.

**Read order:**

1. [`Master_Index.md`](../Master_Index.md) — project context + Document Map (Sections 1–3)
2. This file — how to work Path A / Path B and manage Understanding, specs, TODOs

---

## 0. Naming & file layout *(read before creating files)*

**Layout:** **Flat sibling files** in `docs/features/` and `docs/_shared/` — one **file set** per feature or shared component. Match the **Document Map** paths in `Master_Index.md` §3.

| Kind | Create this path |
|------|------------------|
| Feature spec | `docs/features/FeatureName.md` |
| Feature Understanding | `docs/features/FeatureName-Understanding.md` |
| Feature TODO | `docs/features/FeatureName-TODO.md` |
| Shared spec | `docs/_shared/ComponentName.md` |
| Shared Understanding | `docs/_shared/ComponentName-Understanding.md` |
| Shared TODO | `docs/_shared/ComponentName-TODO.md` |
| Sub-index *(large feature only)* | `docs/features/FeatureName-Index.md` |
| Screenshots | `docs/features/assets/…` or `docs/_shared/assets/…` |

**Use the same name stem** across the set (`MainWorkspace`, `BlockEditor`, …). Copy spelling from the Document Map when adding to an existing project.

**Case:** Pick one convention per project (PascalCase or kebab-case) in Project Profile (Master Index §1.1) and stay consistent.

**When adding a new feature or shared component:**

1. Add a row to Master Index §3.1 or §3.2 with the exact paths.
2. Create those three (or more) **flat files** at those paths — from [`Feature_Spec_Template.md`](Feature_Spec_Template.md), [`Feature_Understanding_Template.md`](Feature_Understanding_Template.md), [`TODO_Template.md`](TODO_Template.md).
3. All files for one feature live **directly** in `features/` (or `_shared/`), not in a subfolder named after the feature.

**Chat UI (no repo write access):** use [`chat-ui/AGENT.md`](chat-ui/AGENT.md) — shorter instructions and required save-as output format.

---

## 1. Shared Components — Foundation vs Consumption

`_shared/` is not only documentation for features to read. Shared pieces often need **foundation work first** — code, APIs, or patterns that multiple features will consume later.

**Each substantial shared component** gets the **full set of note types** — same as a feature — unless the user explicitly says otherwise for that component:

- `_shared/ComponentName.md` — spec / contract / architecture
- `_shared/ComponentName-Understanding.md` — agent model of user intent (see §4)
- `_shared/ComponentName-TODO.md` — core / systems / foundation tasks
- `_shared/ComponentName-InEditor-TODO.md` — engine editor work *(when applicable)*
- `_shared/ComponentName-Asset-TODO.md` — assets & content *(when applicable)*

**Exceptions:** If the user **explicitly** says a component or feature does not need a particular note type (e.g. "BlockEditor has no asset work"), omit that file and record the exception in Master Index **§3.0** with who said it and when.

**Do not invent exceptions.** Missing files, a thin Document Map, or “we’ll add Understanding later” are **not** exceptions — create the default set (spec + Understanding + core TODO). Do **not** skip Understanding or the core TODO unless the user explicitly excepted them. Do **not** write a §3.0 row that excuses the whole project from Understanding.

**Maturity** *(shared components only)*: Set on the shared **spec** (`draft` | `usable` | `stable`) so consumer features know whether integration is safe. Update when foundation work progresses — see [`Feature_Spec_Template.md`](Feature_Spec_Template.md).

**Where tasks go** (agents often get this wrong):

| Work type | Put tasks in | Not in |
|-----------|--------------|--------|
| Building or refactoring the shared component itself | `_shared/ComponentName-TODO.md` | A consumer feature's TODO |
| Feature blocked until shared work is done | Consumer feature TODO — **dependency note + link** only | Duplicating foundation tasks in the feature TODO |
| Feature-specific wiring / UI using the shared piece | That feature's TODO | `_shared/ComponentName-TODO.md` |

**Example**: Extract a reusable text-editor core into `_shared/BlockEditor.md`. Tasks to create that core → `_shared/BlockEditor-TODO.md`. A role-specific UI that *uses* the core → `RoleEditor-TODO.md` with a note: *Depends on [BlockEditor-TODO.md](BlockEditor-TODO.md) item "Expose shared editing API"* — not the extraction tasks themselves.

Optional: `_shared/_Foundation-TODO.md` for cross-cutting shared work that does not belong to one component file yet.

---

## 2. Understanding → Spec graduation

| File | Role | When to update |
|------|------|----------------|
| `-Understanding.md` | Agent's interpretation; user reviews **before** build | Scoping, planning, corrections |
| `.md` spec (feature or `_shared/`) | **Durable contract** — architecture, API, decisions | After Understanding is `confirmed`; when code and docs must match |

**Workflow:**

1. Agent drafts `-Understanding.md` → user confirms (`confirmed`).
2. Agent **graduates** stable content into the spec: overview, architecture/contract, **Decisions**, dependencies, maturity (shared).
3. Understanding keeps intent, boundaries, acceptance criteria, and correction history; spec holds what implementers and future agents should treat as truth.
4. If implementation diverges, update the spec **or** set Understanding to `superseded` and draft a revision (§4) — do not leave both stale.

See [`Feature_Spec_Template.md`](Feature_Spec_Template.md) and [`Feature_Understanding_Template.md`](Feature_Understanding_Template.md).

---

## 3. Quick Start — Working on Any Task

**Always follow this order:**

1. Read `Master_Index.md` — Sections 1–3 (overview, locations, Document Map)
2. Decide: **shared foundation work** (Path A) or **feature work** (Path B) — §1

### Path A — Shared foundation work

Use when building or changing a reusable component, API, or pattern in `_shared/`.

1. Open `_shared/[ComponentName].md`
2. Open `_shared/[ComponentName]-Understanding.md` — **draft or update first** from the conversation; show the user for review (§4)
3. Open the relevant shared TODO file(s) (create from [`TODO_Template.md`](TODO_Template.md) if missing):
   - Core / foundation → `_shared/[ComponentName]-TODO.md`
   - In-Editor work → `_shared/[ComponentName]-InEditor-TODO.md` *(unless excepted in Master Index §3.0)*
   - Assets & content → `_shared/[ComponentName]-Asset-TODO.md` *(unless excepted)*
4. Do the work (only after Understanding is `confirmed` or the user explicitly waives review)
5. **Graduate** confirmed content into `_shared/[ComponentName].md` if the spec is still placeholder (§2)
6. **Update the shared TODO file(s)** before ending the session — refresh **Current focus** (§5.1)
7. If consumer features are blocked, ensure their TODOs link here — do not copy foundation tasks into feature TODOs

### Path B — Feature work

1. Read any `_shared/` documents listed as relevant in Master Index §3.1 (read-only context unless Path A)
2. Open `features/[FeatureName].md`
3. Open `features/[FeatureName]-Understanding.md` — **draft or update first**; show the user for review (§4)
4. Open the relevant feature TODO file(s):
   - Core gameplay/systems → `features/[FeatureName]-TODO.md`
   - In-Editor work → `features/[FeatureName]-InEditor-TODO.md` (or engine-specific version — §7)
   - Assets & content → `features/[FeatureName]-Asset-TODO.md`
5. Do the work (only after Understanding is `confirmed` or the user explicitly waives review)
6. **Graduate** confirmed content into `features/[FeatureName].md` if the spec is still placeholder (§2)
7. **Update the feature TODO file(s)** before ending the session — refresh **Current focus** (§5.1)

If the work is really shared foundation, **stop** — use Path A instead.

**Golden Rule**: If you find yourself scrolling through a long file, stop and split (§8).

---

## 4. Understanding (Features & Shared)

Each **feature** and each substantial **shared component** should have a `-Understanding.md` file — the agent's model of **what the user wants**: scope, behavior, UI intent, and how the work relates to existing pieces.

- Features: `features/FeatureName-Understanding.md`
- Shared: `_shared/ComponentName-Understanding.md`

**Who writes it:** The **agent writes first** (status `draft`) from the conversation, design doc, or interview. The **user reviews and corrects** — they do not need to author this file from scratch.

**Default:** Agent drafts Understanding for shared components the same way as for features. **Only skip** when the user **explicitly** excepts it (record in Master Index §3.0). Incomplete docs or agent convenience are not exceptions — draft the missing Understanding.

**Purpose**:

- Capture what the feature **is meant to be when complete** (destination), not a snapshot of what is unfinished today
- Catch misread **identity** early (e.g. "alternate UI for existing editor" vs "brand-new editor")
- Give the user a short, readable artifact to **review and correct** before code is written
- Attach to plans and discussions so corrections happen at planning time

**What this is NOT** (critical): List **category / identity** boundaries for the finished feature — wrong product type, wrong architecture, wrong ownership. **Do not** list deferred phases, “not implemented yet,” or long-term goals that still belong to this feature; those go in the TODO, Current focus, or the spec roadmap.

**Status**:

| Status | Meaning |
|--------|---------|
| `draft` | Agent wrote or updated; user has not approved — **do not implement** unless user waives |
| `reviewed` | User skimmed; minor edits may remain |
| `confirmed` | User approved scope — **safe to implement and continue** without asking them to review this Understanding again; **graduate to spec** (§2) |
| `superseded` | No longer accurate — code or plan changed; draft a revision or reconcile explicitly |

**When status is `confirmed`:** Read the Understanding for context, then proceed from the TODO/spec. **Do not** re-surface it for review or ask "does this match your intent?" unless the user changes scope, you discover a conflict with code, or you set status back to `draft` / `superseded`. Unchecked **Assumptions** after `confirmed` means ask about those specific items only — not a full re-review.

**Reconciliation:** If shipped code diverges from a `confirmed` Understanding, either update the spec to match reality and note **Last reconciled with code** on both files, or set status to `superseded` and draft a new Understanding. Do not treat stale `confirmed` as current without checking.

**When to create or update** *(agent responsibility unless user edits directly)*:

- User describes a new feature or change → agent drafts or updates Understanding (set `draft` if scope changed materially)
- User asks for a plan, spec review, or "how should we build this" → if Understanding is `confirmed`, use it; if `draft` or missing, draft or update first
- Agent discovers an **identity** assumption that should be explicit (especially **What this is NOT** — not a backlog of unfinished work)
- User corrects the agent → agent updates Understanding immediately

**When planning**: Include the Understanding file (or path) in the plan output so the user can correct it before implementation starts.

See [`Feature_Understanding_Template.md`](Feature_Understanding_Template.md).

**Acceptance criteria:** The agent drafts **Done when** checkboxes in Understanding so the user can confirm completeness without reading every TODO.

**Visual references (screenshots):** Save under `docs/features/assets/`, `docs/_shared/assets/`, or `docs/reference/visuals/`. Link from `-Understanding.md` with **similar vs different** notes. See [`../help/IDEA_CAPTURE_TIPS.md`](../help/IDEA_CAPTURE_TIPS.md#visual-references-screenshots).

---

## 5. TODO Management

Every feature **must** have at least one companion `-TODO.md` file. Most game features will have three.

Every substantial `_shared/` component gets the **same TODO file set as a feature** (§1) unless the user explicitly excepted specific files (Master Index §3.0).

**File naming**:

- Core gameplay/systems: `FeatureName-TODO.md` or `_shared/ComponentName-TODO.md`
- In-Editor work: `FeatureName-InEditor-TODO.md` or `_shared/ComponentName-InEditor-TODO.md` (rename per §7)
- Assets & content: `FeatureName-Asset-TODO.md` or `_shared/ComponentName-Asset-TODO.md`

**Shared vs feature — cross-links**:

When a feature depends on shared foundation work, the feature TODO gets a **dependency note**, not a duplicate of the foundation tasks:

> Blocked until shared editor API exists (see [_shared/BlockEditor-TODO.md](../_shared/BlockEditor-TODO.md) — "Expose shared editing API")

**Cross-feature interactions**: Add a note in the TODO with a direct link when work depends on or affects another feature.

**Dynamic TODO creation**: Add new items as you work. See [`TODO_Template.md`](TODO_Template.md) for format.

**Workflow**:

- **Session start:** Read the active TODO's **Current focus** block first (§5.1) — then High Priority.
- While working: Add new items as you discover them.
- After finishing a task: Mark `[x]`, add completion date/note.
- When a section gets long: Move finished items to Completed or archive (`-todo-complete.md`).
- **Session end:** Update **Current focus** for the next session.

### 5.1 Session handoff — Current focus

Each active `-TODO.md` should keep a short **Current focus** block at the top (see [`TODO_Template.md`](TODO_Template.md)):

- One active task (or "blocked by …")
- Blockers with links
- Optional: last session date / agent tool

This gives the next agent (or a different tool) a 5-second orientation without re-reading everything.

---

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

## 10. Decisions *(lightweight)*

Record **why** something was chosen — not every task, only choices with lasting impact.

| Where | Use for |
|-------|---------|
| **Decisions** section in feature or shared **spec** | Choices local to that piece ([`Feature_Spec_Template.md`](Feature_Spec_Template.md)) |
| `docs/decisions/YYYY-MM-DD-short-title.md` | Cross-cutting choices ([`Decision_Template.md`](Decision_Template.md)) |

When the user confirms a tradeoff during Understanding review, the agent adds a row to the spec **Decisions** table. Link standalone decision files from Master Index §3.4.

---

## 11. Tooling *(new machine setup)*

Live file: **`docs/Tooling.md`** (from [`Tooling_Template.md`](Tooling_Template.md)).

Lists **machine / workflow tools** (CLIs, SDKs, runtimes, engines, profile-installed agent skills) — **not** package-manager dependencies.

When the user asks to install tooling / set up this machine / get the project working on a new PC:

1. Read `docs/Tooling.md`.
2. Install **Required** for the current OS (prefer user-level / non-interactive package managers).
3. Refresh PATH or use a new shell if needed; run every **Verify** command.
4. Install **Agent skills** rows if that section exists; new session may be required for skills to load.
5. Run **After tools are installed** (env files, package restore, start commands).
6. Report pass/fail. Install **Optional** only if asked (or “everything”). Ask before admin / large SDK installs.

Do not invent tools; update the file when the stack changes. No secrets in `Tooling.md`.

---

## Instructions for AI Agents

- **Master_Index.md** = *what this project is* and *where files live*.
- **This file** = *how to work* the system. Follow Path A or B (§3) on every task.
- **Tooling.md** = *what to install on a new machine* (not package deps).
- The installed agent rule ([`agent/Modular_Documentation_Rule.mdc`](agent/Modular_Documentation_Rule.mdc)) is a short checklist — read this file when doing non-trivial doc or implementation work.
