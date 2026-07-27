<!-- workflow-version: 2.6.6 -->

> **Agent workflow reference.** Canonical instructions for how to work the modular doc system. Lives in `docs/templates/agent/` with the other agent playbooks — sync from upstream; do **not** copy wholesale into `docs/Master_Index.md`. The live index links here; agent rules summarize and point here for full procedure.

# Modular Documentation — Agent Workflow

**Workflow version**: 2.6.6 *(sync with `Master_Index.md` **Workflow version** line when updating)*

**Design intent:** Users give short requests about the docs (“bootstrap”, “draft Understanding for X”, “update the templates”). Route to **one** playbook (`BOOTSTRAP`, `TEMPLATE_SYNC`, `TEMPLATE_UPDATE_CHECK`, `RULE_INSTALL` → `tools/<key>.md`, or this file for feature work) — do not scan the whole pack catalog. **Tight scope:** act on the paved path; do not pre-audit every alternate interpretation before doing the work.

**Optional roles** *(never always-on):* Thin wrappers under [`roles/`](roles/README.md). When harness agents are installed (`.cursor/agents/`, `.grok/agents/`, … via [`tools/`](tools/README.md)), the modular **rule** has the parent **delegate/spawn** on matching asks. Otherwise follow the role `.md` fallback. Roles point back here or to `BOOTSTRAP` / `TEMPLATE_SYNC` — they do not replace this workflow.

**Read order (feature / shared work):**

1. [`Master_Index.md`](../../Master_Index.md) — project context + Document Map (Sections 1–3)
2. Active TODO **Current focus** + that item’s Understanding / spec
3. This file — only when creating files, choosing Path A/B, graduating Understanding, or the user asks about procedure

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

1. Add a row to Master Index §3.1 or §3.2 with the exact paths (**working markdown links** — not “planned” placeholders with nowhere to click).
2. Create those three (or more) **flat files** at those paths **in the same turn** — from [`Feature_Spec_Template.md`](../Feature_Spec_Template.md), [`Feature_Understanding_Template.md`](../Feature_Understanding_Template.md), [`TODO_Template.md`](../TODO_Template.md).
3. All files for one feature live **directly** in `features/` (or `_shared/`), not in a subfolder named after the feature.

**Map without files = incomplete work.** Do not add Document Map rows and defer file creation “until the user picks where to start.” Bootstrap Step 3d and this section require the default file set on disk. Understanding status `draft` means **do not implement code** yet — it does **not** mean skip creating `-Understanding.md`.

**Chat UI (no repo write access):** use [`chat-ui/AGENT.md`](../chat-ui/AGENT.md) — shorter instructions and required save-as output format.

**`docs/reference/`:** Drop zone for **source** materials (design docs, PRDs, chat exports, legacy specs). Not Document Map rows. Read when the user points at a file or asks to convert into modular docs. Optional `docs/reference/visuals/` for inspiration screenshots.

---

## 1. Shared Components — Foundation vs Consumption

**Gate — only create `_shared/` docs when something is actually shared.**

| Put in `_shared/` | Do **not** put in `_shared/` |
|-------------------|------------------------------|
| A **project-owned** piece (code, UI kit, subsystem) that **two or more features** will consume, or that the user named as shared | Engine/framework general knowledge (e.g. “how Unreal works”, UE project-settings overview, generic Godot/Unity primers) |
| Extracted reusable core the user agreed to share | A single feature’s systems dumped into `_shared/` because “nowhere else fit” |
| | Filler Document Map rows so §3.1 is not empty |

**Empty `_shared/` and an empty §3.1 table are normal and preferred** when the project is feature-shaped (many puzzle/game/apps never need shared docs). Prefer `features/` for mode/level/puzzle-specific work. If you must keep engine primers or pasted UE notes, use `docs/reference/` — not fake shared components.

Only when a real shared piece exists: `_shared/` often needs **foundation work first** — code, APIs, or patterns that multiple features will consume later.

**Each substantial shared component** (that passed the gate) gets the **full set of note types** — same as a feature — unless the user explicitly says otherwise for that component:

- `_shared/ComponentName.md` — spec / contract / architecture
- `_shared/ComponentName-Understanding.md` — agent model of user intent (see §4)
- `_shared/ComponentName-TODO.md` — core / systems / foundation tasks
- `_shared/ComponentName-InEditor-TODO.md` — engine editor work *(game extensions / user asked)*
- `_shared/ComponentName-Asset-TODO.md` — assets & content *(game extensions / user asked)*

**Exceptions:** If the user **explicitly** says a component or feature does not need a particular note type (e.g. "BlockEditor has no asset work"), omit that file and record the exception in Master Index **§3.0** with who said it and when.

**Do not invent exceptions** for rows that *should* exist. Missing files, a thin Document Map, or “we’ll add Understanding later” are **not** reasons to skip Understanding on a real feature/shared row — create the default set. Do **not** invent §3.1 shared rows (or §3.0 excuses) to fill empty space. Do **not** write a §3.0 row that excuses the whole project from Understanding.

**Maturity** *(shared components only)*: Set on the shared **spec** (`draft` | `usable` | `stable`) so consumer features know whether integration is safe. Update when foundation work progresses — see [`Feature_Spec_Template.md`](../Feature_Spec_Template.md).

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
| `-Understanding.md` | **Feature shape / guardrails** — is / is not, Assumptions; user confirms **shape** (not the full contract) | Scoping, planning, corrections |
| `.md` spec (feature or `_shared/`) | **Durable contract** — architecture, API, decisions, stable behavior | After Understanding is `confirmed`; when code and docs must match |

**Workflow:**

1. Agent drafts `-Understanding.md` → user confirms **shape** (`confirmed`) — is / is not + Assumptions. This is **not** a full spec sign-off.
2. Agent **graduates** durable contract content into the spec: overview, architecture/contract, stable behavior, **Acceptance**, **Visual references**, **Decisions**, dependencies, maturity (shared). Synthesize from Understanding **plus** conversation / decisions — do **not** only copy the thin Understanding. Spec may (and should) hold detail that was never in Understanding. A short Understanding is **not** permission to write a short spec.
3. Understanding stays thin: **What this is / is NOT**, **Relationship**, **Assumptions**, and short **Confirmed with user** notes — do not mine past chats or git history for a history section. Do **not** keep How it should work, UI/UX sections, Core Behavior, **Done when**, or Visual references on Understanding after graduation. Spec holds what implementers and future agents should treat as contract truth; **TODO** is the only living work checklist.
4. If implementation diverges, update the spec **or** set Understanding to `superseded` and draft a revision (§4) — do not leave both stale.

See [`Feature_Spec_Template.md`](../Feature_Spec_Template.md) and [`Feature_Understanding_Template.md`](../Feature_Understanding_Template.md).

---

## 3. Quick Start — Working on Any Task

**Minimal implement path** *(Understanding is `confirmed` and scope unchanged — prefer this)*:

1. Read `Master_Index.md` — Sections 1–3
2. Active TODO **Current focus** → that TODO → Understanding (read-only) → spec → code
3. Skip drafting, graduation, and InEditor/Asset TODOs unless status is `draft`, the user changed scope, or Project Profile says game extensions apply

**Full Path A / Path B** when scoping new work, Understanding is missing/`draft`, or graduating to spec:

1. Read `Master_Index.md` — Sections 1–3 (overview, locations, Document Map)
2. Decide: **shared foundation work** (Path A) or **feature work** (Path B) — §1

### Path A — Shared foundation work

Use when building or changing a reusable component, API, or pattern in `_shared/`.

1. Open `_shared/[ComponentName].md`
2. Open `_shared/[ComponentName]-Understanding.md` — **draft or update first** from the conversation; show the user for review (§4). If already `confirmed` and scope unchanged, read only — do not re-draft.
3. Open the relevant shared TODO file(s) (create from [`TODO_Template.md`](../TODO_Template.md) if missing):
   - Core / foundation → `_shared/[ComponentName]-TODO.md`
   - In-Editor work → `_shared/[ComponentName]-InEditor-TODO.md` *(only if Project Profile game extensions apply, or user asked — unless excepted in Master Index §3.0)*
   - Assets & content → `_shared/[ComponentName]-Asset-TODO.md` *(same gate)*
4. Do the work (only after Understanding is `confirmed` or the user explicitly waives review)
5. **Graduate** confirmed content into `_shared/[ComponentName].md` if the spec is still placeholder (§2)
6. **Update the shared TODO file(s)** before ending the session — refresh **Current focus** (§5.1)
7. If consumer features are blocked, ensure their TODOs link here — do not copy foundation tasks into feature TODOs

### Path B — Feature work

1. Open shared docs **only** when linked from this feature’s Understanding, spec, or TODO dependency notes — or the one shared component you are integrating now. Do **not** open every §3.1 “relevant” row.
2. Open `features/[FeatureName].md`
3. Open `features/[FeatureName]-Understanding.md` — **draft or update first** if missing/`draft` or scope changed; if `confirmed` and scope unchanged, read only (§4)
4. Open the relevant feature TODO file(s):
   - Core gameplay/systems → `features/[FeatureName]-TODO.md`
   - In-Editor work → `features/[FeatureName]-InEditor-TODO.md` *(Project Profile game extensions or user asked — §7)*
   - Assets & content → `features/[FeatureName]-Asset-TODO.md` *(same gate)*
5. Do the work (only after Understanding is `confirmed` or the user explicitly waives review)
6. **Graduate** confirmed content into `features/[FeatureName].md` if the spec is still placeholder (§2)
7. **Update the feature TODO file(s)** before ending the session — refresh **Current focus** (§5.1)

If the work is really shared foundation, **stop** — use Path A instead.

**Golden Rule**: If you find yourself scrolling through a long file, stop and split (§8).

---

## 4. Understanding (Features & Shared)

Each **feature** and each substantial **shared component** should have a `-Understanding.md` file — the agent's model of **feature shape** (guardrails): what it is / isn’t, Assumptions, and light intent. It is **not** a second copy of the durable spec.

- Features: `features/FeatureName-Understanding.md`
- Shared: `_shared/ComponentName-Understanding.md`

**Who writes it:** The **agent writes first** (status `draft`) from the conversation, design doc, or interview. The **user reviews and corrects shape** — they do not need to author it from scratch, and they should **not** be asked to approve the full contract here.

**Default:** Agent drafts Understanding for shared components the same way as for features. **Only skip** when the user **explicitly** excepts it (record in Master Index §3.0). Incomplete docs or agent convenience are not exceptions — draft the missing Understanding.

**Purpose**:

- Capture **feature shape** — identity and boundaries for the finished thing — not a snapshot of unfinished work and **not** the full architecture/behavior contract
- Catch misread **identity** early (e.g. "alternate UI for existing editor" vs "brand-new editor")
- Give the user a short artifact to **confirm guardrails** before code is written
- Attach to plans so shape corrections happen at planning time; durable detail **graduates** to the spec (§2)

**Tell the user clearly:** Confirming Understanding = confirming **is / is not** + **Assumptions** (shape). Spec-level detail may be missing here on purpose.

**What this is** (critical — shape, not the spec): Capture identity-defining detail the user stated — category, metaphors, naming, “feels like,” ownership, constraints that decide *what kind of thing* this is. Prefer the user’s words. Brief feel/layout only when it defines the product — not a UI walkthrough. Do **not** drop that shape detail for brevity — and do **not** expand into flows, APIs, edge-case matrices, acceptance checklists, How-it-should-work, or a parallel Core Behavior. Work queue → **TODO**; durable contract + Behavior + **Acceptance** + Visual references → **spec**. Do **not** put **How it should work**, **UI / UX intent**, **Done when**, or **Visual references** sections on Understanding. Do **not** pad, speculate, or invent.

**What this is NOT** (critical — keep tight): List **category / identity** boundaries for the finished feature — wrong product type, wrong architecture, wrong ownership. **Do not** list deferred phases, “not implemented yet,” or long-term goals that still belong to this feature; those go in the TODO, Current focus, or the spec roadmap. Put the user’s shape detail in **What this is**, not in long NOT lists.

**Status**:

| Status | Meaning |
|--------|---------|
| `draft` | Agent wrote or updated; user has not approved **shape** — **do not implement code** unless user waives. The file **must still exist** — `draft` is not a reason to skip creating Understanding |
| `reviewed` | User skimmed; minor edits may remain |
| `confirmed` | User approved **feature shape** (is / is not + Assumptions) — **safe to implement and continue** without re-asking for Understanding review; **graduate** durable contract to spec (§2). Not a sign-off on every spec detail |
| `superseded` | No longer accurate — code or plan changed; draft a revision or reconcile explicitly |

**When status is `confirmed`:** Read the Understanding for **guardrails**, then proceed from the TODO/spec. **Do not** re-surface it for review or ask "does this match your intent?" unless the user changes shape/scope, you discover a conflict with code, or you set status back to `draft` / `superseded`. Unchecked **Assumptions** after `confirmed` means ask about those specific items only — not a full re-review or a full-spec review.

**Reconciliation:** If shipped code diverges from a `confirmed` Understanding’s **shape**, either update the spec to match reality and note **Last reconciled with code** on both files, or set status to `superseded` and draft a new Understanding. Run reconciliation **only when** the user reports a mismatch, implementation clearly contradicts Understanding, this session changes that feature’s shape/behavior, **or you are updating that feature’s Understanding** — **not** as a session-start code-vs-docs audit of the whole repo.

**On Understanding update — shape trim + relocate:** In the same pass as drafting/revising `-Understanding.md` for a stem, if you remove content that is **contract** (not shape), **move it into that stem’s spec** when missing there, then delete it from Understanding (legacy **Done when** → **Acceptance**; How-it-should-work / flows → **Behavior**; UI sections / screenshot tables → **Visual references** / Behavior as appropriate). Do not discard durable detail. Do not invent. Short **Confirmed with user** notes only — not a dumping ground for relocated prose.

**On Understanding update — TODO:** Also open that stem’s `-TODO.md` and compare checked TODO tasks to the **destination** (updated Understanding + spec) and to implemented code for that stem. **Uncheck** any `[x]` where code no longer matches (partial ship, wrong behavior, or destination changed). Reopen or add TODO items and refresh **Current focus** when work is no longer done. Note corrections under **Confirmed with user**. Do **not** invent completion — leave boxes unchecked when unsure. Optionally align spec **Acceptance** checkboxes the same way — do not recreate a Done when section on Understanding.

**When to create or update** *(agent responsibility unless user edits directly)*:

- User describes a new feature or change → agent drafts or updates Understanding (set `draft` if shape/scope changed materially)
- User asks for a plan, spec review, or "how should we build this" → if Understanding is `confirmed`, use it as guardrails + read the spec; if `draft` or missing, draft or update Understanding first (shape only)
- Agent discovers an **identity** assumption that should be explicit (especially **What this is NOT** — not a backlog of unfinished work)
- User corrects the agent → agent updates Understanding immediately
- After any of the above updates → run the **TODO** check for that stem before stopping

**When planning**: Include the Understanding file (or path) in the plan output and state that user confirmation is for **shape / guardrails**, not the full spec.

See [`Feature_Understanding_Template.md`](../Feature_Understanding_Template.md).

**Acceptance (on the spec):** Usually **3–7** coarse outcomes — not a twin of the TODO checklist. Work breakdown stays in `-TODO.md` only. Do **not** put Done when / Acceptance on `-Understanding.md`.

**Visual references (screenshots):** Save under `docs/features/assets/`, `docs/_shared/assets/`, or `docs/reference/visuals/`. Link from the **spec** (`FeatureName.md` / `_shared/ComponentName.md`) **Visual references** with **similar vs different** notes — not from `-Understanding.md`. See [`../help/IDEA_CAPTURE_TIPS.md`](../help/IDEA_CAPTURE_TIPS.md#visual-references-screenshots).

---

## 5. TODO Management

Every feature **must** have at least one companion `-TODO.md` file (core). InEditor / Asset TODOs only when Project Profile game extensions apply or the user asks — most non-game features need the core TODO only.

Every substantial `_shared/` component gets the **same TODO file set as a feature** (§1) unless the user explicitly excepted specific files (Master Index §3.0).

**File naming**:

- Core gameplay/systems: `FeatureName-TODO.md` or `_shared/ComponentName-TODO.md`
- In-Editor work: `FeatureName-InEditor-TODO.md` or `_shared/ComponentName-InEditor-TODO.md` (rename per §7)
- Assets & content: `FeatureName-Asset-TODO.md` or `_shared/ComponentName-Asset-TODO.md`

**Shared vs feature — cross-links**:

When a feature depends on shared foundation work, the feature TODO gets a **dependency note**, not a duplicate of the foundation tasks:

> Blocked until shared editor API exists (see [_shared/BlockEditor-TODO.md](../_shared/BlockEditor-TODO.md) — "Expose shared editing API")

**Cross-feature interactions**: Add a note in the TODO with a direct link when work depends on or affects another feature.

**Dynamic TODO creation**: Add new items as you work. See [`TODO_Template.md`](../TODO_Template.md) for format.

**Workflow**:

- **Session start:** Read the active TODO's **Current focus** block first (§5.1) — then High Priority.
- While working: Add new items as you discover them.
- After finishing a task: Mark `[x]`, add completion date/note.
- When a section gets long: Move finished items to Completed or archive (`-todo-complete.md`).
- **Session end:** Update **Current focus** for the next session.

### 5.1 Session handoff — Current focus

Each active `-TODO.md` should keep a short **Current focus** block at the top (see [`TODO_Template.md`](../TODO_Template.md)):

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
| **Decisions** section in feature or shared **spec** | Choices local to that piece ([`Feature_Spec_Template.md`](../Feature_Spec_Template.md)) |
| `docs/decisions/YYYY-MM-DD-short-title.md` | Cross-cutting choices ([`Decision_Template.md`](../Decision_Template.md)) |

When the user confirms a tradeoff during Understanding review, the agent adds a row to the spec **Decisions** table. Link standalone decision files from Master Index §3.4.

---

## 11. Tooling *(new machine setup)*

Live file: **`docs/Tooling.md`** (from [`Tooling_Template.md`](../Tooling_Template.md)).

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

## 12. Mermaid diagrams *(optional, agent judgment)*

Use Mermaid in **specs** or Master Index overview when a **small** diagram explains structure or flow better than prose — e.g. happy-path flow, feature ↔ `_shared/` ownership, module boundaries. Do **not** put flowcharts on `-Understanding.md` (shape only).

| Do | Do not |
|----|--------|
| One focused chart when it clarifies | Diagrams in every file by default |
| Prefer Mermaid for structure/flow | Replace UI screenshots with Mermaid |
| Leave it out when bullets are enough | Decorative or huge multi-subgraph charts |

**Agent decides.** Users should not need to ask for Mermaid. Do not splash charts everywhere just because the format is available.

---

## 13. Human TODO *(inbox — needs a human)*

Live file: **`docs/Human-TODO.md`** (from [`Human_TODO_Template.md`](../Human_TODO_Template.md)).

**One project inbox for humans** — anything a coding agent must not close from assumptions: procurement, playtest/feel, decisions/sign-off, and external waiting. Format and kinds: see the Human TODO template.

**Section order (human-facing):** **Open** → **Done** at the top (tasks visible immediately); short “scroll for instructions” note above Open; Instructions for Humans then ownership / dual-write / Instructions for AI Agents **below**. Do not put instructions above the task lists.

| Put on Human-TODO | Put elsewhere |
|-------------------|---------------|
| `procure` — portal / account / key / purchase / approval | Installable CLIs/SDKs → [`Tooling.md`](../../Tooling.md) |
| `playtest` — human must run, feel, or smoke-test | Agent-only code tasks → feature or `_shared/` `*-TODO.md` |
| `decide` — human judgment or sign-off | |
| `waiting` — blocked on someone/something outside the repo | |

**Index + owner (do not “move” tasks):**

| Kind | Canonical detail / outcome | Human-TODO |
|------|----------------------------|------------|
| `playtest` · `decide` | Owner feature/shared `*-TODO.md` item | Thin checkbox row + **Owner** link |
| `procure` · `waiting` | Human-TODO row (how-to / status) | Features **link here** — do not copy full checklists into every TODO |

**Agent behavior:**

1. **Dual-write (mandatory):** When Understanding, planning, Current focus, or implementation creates a task only a human can close → in the **same edit** add/update the owner `*-TODO.md` item **and** an **Open** `- [ ]` list item on `Human-TODO.md` (kind + Owner + Blocks). **Never put checkboxes inside markdown tables** — preview cannot toggle those. If it is not on Human-TODO, it does not exist as a human ask — do not bury playtest/feel/sign-off only in feature TODOs or chat.
2. Keep Human-TODO items short; put steps and outcome notes on the owner TODO (`playtest` / `decide`) or under the Human-TODO list item (`procure` / `waiting`).
3. Never store secrets in docs. Instruct: create credential → put in `.env` / vault (names only in `.env.example`).
4. Do not mark items **done** unless the user confirms (chat or explicit checkbox + tell-the-agent). On confirm: update owner TODO (`[x]` + date + feedback notes), move Human-TODO item to **Done** as `- [x]`, refresh affected Current focus.
5. If the user asks what’s left for them → summarize **Open** from `Human-TODO.md` only. If you find human-gated items on feature TODOs missing from the inbox, **repair dual-write** *(one direction)*: add thin Open `- [ ]` items **here** that point at the owner TODO — never the reverse (do not copy this inbox onto feature TODOs “for dual-write”). Then summarize.
6. Create the file at bootstrap (may start empty). Fill as soon as conversation or Document Map implies human-gated work. If Open is still a table, convert to `- [ ]` list items without dropping content.

---

## Instructions for AI Agents

- **Master_Index.md** = *what this project is* and *where files live*.
- **This file** = *how to work* the system. Follow Path A or B (§3) on every task.
- **Tooling.md** = *what to install on a new machine* (not package deps).
- **Human-TODO.md** = *what only a human can close* (procure, playtest, decide, waiting) — §13; dual-write with owner TODOs.
- **Mermaid** = optional (§12) — use when clearer than prose; never required.
- The installed agent rule ([`Modular_Documentation_Rule.mdc`](Modular_Documentation_Rule.mdc)) is a short checklist — read this file when doing non-trivial doc or implementation work.
