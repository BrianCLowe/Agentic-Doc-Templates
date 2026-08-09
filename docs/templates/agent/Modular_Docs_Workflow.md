<!-- pack-version: 2.7.11 -->

> **Agent workflow reference.** Canonical instructions for how to work the modular doc system. Lives in `docs/templates/agent/` with the other agent playbooks — sync from upstream; do **not** copy wholesale into `docs/Master_Index.md`. The live index links here; agent rules summarize and point here for full procedure.

# Modular Documentation — Agent Workflow

**Pack version**: 2.7.11 *(same as `docs/templates/VERSION` / live Master Index **Pack version**)*

**Design intent:** Short user asks → **one** playbook (`BOOTSTRAP`, `TEMPLATE_SYNC`, `TEMPLATE_UPDATE_CHECK`, `RULE_INSTALL` → `tools/<key>.md`, roles, or this file for feature procedure). Do not scan the pack catalog. **Tight scope** = paved path only (not “audit every alternate”). **Timescale** = target architecture when shape is clear ([`Agent_Timescale_Planning_Rule.mdc`](Agent_Timescale_Planning_Rule.mdc)). **Operable done** = user-facing stems need an exercise path / phase / library-only — not domain checklist alone (**§5.3**). **Build green** before “you can test” ([`Agent_Build_Verify_Rule.mdc`](Agent_Build_Verify_Rule.mdc)).

**Docs profile:** `docs/ADT-settings.yaml` → `docs_profile.mode` — **`prevent`** (default if unset) · **`balanced`** · **`ship-first`**. Full rules **§0.1**. Never silent-downgrade a project full of Understandings.

**Optional roles:** [`roles/`](roles/README.md) — never always-on; parent spawns when adapters exist, else playbook in-session. **Orchestrator** = parent only ([`roles/orchestrator.md`](roles/orchestrator.md) + git [`roles/orchestrator-git.md`](roles/orchestrator-git.md)). Single-slice implement → [`roles/feature-implementer.md`](roles/feature-implementer.md).

**Read order (feature / shared work):**

1. `docs/ADT-settings.yaml` → `docs_profile.mode` when present (else **prevent**)
2. [`Master_Index.md`](../../Master_Index.md) — project context + Document Map (Sections 1–3)
3. Active TODO **Current focus** + that item’s Understanding *(if any)* / spec
4. This file — only when creating files, choosing Path A/B, graduating Understanding, or the user asks about procedure

---

## 0.1 Docs profile *(ceremony modes)*

**Live setting:** `docs/ADT-settings.yaml` → `docs_profile.mode` (`prevent` | `balanced` | `ship-first`). Example: [`ADT-settings.example.yaml`](ADT-settings.example.yaml).

| Mode | Default file set on new map row | Coding gate | When to use |
|------|----------------------------------|-------------|-------------|
| **`prevent`** | Spec + **Understanding** (`draft`) + core TODO | **Do not code** while Understanding is `draft` unless user waives | Identity-sensitive products; you prefer prevent wrong builds (pack default) |
| **`balanced`** | Spec + core TODO; **+ Understanding** when identity is ambiguous / multi-surface / split pressure / user asked | Same draft gate **only for stems that have** an Understanding | Mid-size apps; you accept agent judgment on “needs shape file?” |
| **`ship-first`** | Spec + core TODO only (Understanding **not** required) | No Understanding draft gate — implement from TODO + thin spec | Prototypes, clear CRUD, “fix-forward” teams |

**Always required (all modes):** Master Index + Document Map, **spec**, **core TODO**, Human-TODO dual-write rules (§13). Catalog / decisions remain optional per their own sections.

**Unset `docs_profile`:** treat as **`prevent`**. Do **not** invent `ship-first` because files are missing.

**Suggest once** *(bootstrap Step 3p preference batch / first “build from reference” / sync B0.5 if still unset)*:

1. Skim `docs/reference/` (if any) + conversation — do not inventory the whole repo.
2. Recommend a mode with **2–3 short citations** (export path + quote or paraphrase). **Explain each option in plain language** so the user is not guessing labels:
   - **prevent** — “You confirm is/is-not before code” — competing product identities; “not X”; multi-surface / editor / game systems
   - **ship-first** — “Spec+TODO only; no shape gate” — clear CRUD/API; prototype/spike; tiny map
   - **balanced** — “Understanding only when identity is fuzzy (multi-surface, not-X, split, or you say lock shape)” — mid-size / mixed signals
3. **Ask once** (bootstrap: inside Step 3p preference batch). Record `docs_profile.mode`, `recorded`, and `source: agent-suggested` or `user`.
4. Re-ask only on explicit *Set docs profile to prevent|balanced|ship-first*.

**Upgrade / downgrade:**

| Change | Behavior |
|--------|----------|
| → **prevent** | Create missing Understandings as `draft` for map rows that lack them; do not wipe specs/TODOs |
| → **balanced** | Keep existing Understandings; stop requiring new ones when identity is clear |
| → **ship-first** | Stop requiring Understanding / confirm; **do not delete** existing `-Understanding.md` files |
| *Lock shape for [Stem]* (any mode) | Draft/update that stem’s Understanding and use the draft gate for **that stem** |

**Orchestrator / implementer readiness** — see [`roles/orchestrator.md`](roles/orchestrator.md) and §3. Work-verifier always checks **spec + TODO**; Understanding only when the file exists or mode is prevent/balanced with a shape file.

---

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
   - **Always:** [`Feature_Spec_Template.md`](../Feature_Spec_Template.md) + [`TODO_Template.md`](../TODO_Template.md)
   - **+ Understanding** ([`Feature_Understanding_Template.md`](../Feature_Understanding_Template.md)): required under **`prevent`**; under **`balanced`** when identity is ambiguous / multi-surface / split / user asked; under **`ship-first`** only if user asked *lock shape* or an Understanding already exists for that stem
   - Add [`Feature_Catalog_Template.md`](../Feature_Catalog_Template.md) only when §7 / list-heavy rules apply
3. All files for one feature live **directly** in `features/` (or `_shared/`), not in a subfolder named after the feature.

**Map without files = incomplete work.** Do not add Document Map rows and defer file creation “until the user picks where to start.” Bootstrap Step 3d and this section require the profile’s default file set on disk. Under **`prevent`**, Understanding status `draft` means **do not implement code** yet — it does **not** mean skip creating `-Understanding.md`.

**`docs/reference/`:** Drop zone for **source** materials. **Recommended habit:** markdown **chat exports** of idea threads (often many files) — they preserve user whys/motives better than polished-only design docs ([`../help/IDEA_CAPTURE_TIPS.md`](../help/IDEA_CAPTURE_TIPS.md)). Also fine: PRDs, legacy specs. Not Document Map rows. Read when the user points at a file or asks to convert / **build or update** live docs from them. Optional `docs/reference/visuals/` for inspiration screenshots. Do **not** send users to a chat-only `AGENT.md` attach flow — that path is paused; export → `reference/` is the supported route.

**One identity per stem:** If conversation or `reference/` material describes **two (or more) finished-feature identities** that do different jobs (different category, product surface, or ownership) — **split**. Add separate Document Map rows + default file sets (§0) in the same turn; move misplaced shape/contract content into the correct stem. Do **not** keep unlike things in one Understanding to avoid creating files or because the user mentioned them together. Prefer asking one clarifying question over silently merging. User correction (“those are two features”) → split immediately — do not wait for them to name paths.

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

**Each substantial shared component** (that passed the gate) gets the **same default file set as a feature** for the active docs profile (§0.1) — unless the user explicitly says otherwise for that component:

- `_shared/ComponentName.md` — spec / contract / architecture **(always)**
- `_shared/ComponentName-Understanding.md` — shape guardrails (§4) — **per profile** (required under `prevent`; situational under `balanced`; optional under `ship-first`)
- `_shared/ComponentName-TODO.md` — core / systems / foundation tasks **(always)**
- `_shared/ComponentName-InEditor-TODO.md` — engine editor work *(game extensions / user asked)*
- `_shared/ComponentName-Asset-TODO.md` — assets & content *(game extensions / user asked)*

**Exceptions:** If the user **explicitly** says a component or feature does not need a particular note type (e.g. "BlockEditor has no asset work"), omit that file and record the exception in Master Index **§3.0** with who said it and when. Project-wide ceremony is **`docs_profile`**, not a §3.0 “no Understanding for the whole project” invention.

**Do not invent exceptions** for rows that *should* exist under the active profile. Under **`prevent`**, missing files or “we’ll add Understanding later” are **not** reasons to skip Understanding — create the default set. Under **`ship-first` / `balanced`**, not creating Understanding when the profile allows is **correct**, not an exception. Do **not** invent §3.1 shared rows (or §3.0 excuses) to fill empty space.

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

**Source of truth:** This section and §4 are the canonical shape-vs-contract procedure. Rules, roles, and template Instruction blocks summarize; **this file wins on conflict**. Applies fully under **`prevent`**, and for any stem that **has** an Understanding under other profiles. Under **`ship-first`** (no Understanding), grow the **spec** directly as contract home — skip steps 1 and the Understanding half of step 3.

| File | Role | When to update |
|------|------|----------------|
| `-Understanding.md` | **Feature shape / guardrails** — is / is not, Assumptions; user confirms **shape** (not the full contract) | When the profile requires it, or user locks shape / identity is ambiguous |
| `.md` spec (feature or `_shared/`) | **Durable contract** — architecture, API, decisions, stable behavior, Acceptance, Visual references | After shape confirm (if Understanding exists); as you implement under `ship-first`; when code and docs must match |

**Workflow *(when Understanding is in play)*:**

1. Agent drafts `-Understanding.md` → user confirms **shape** (`confirmed`) — is / is not + Assumptions. **Not** a full spec sign-off.
2. Agent **graduates** durable contract into the spec: overview, architecture/contract, Behavior, **Acceptance**, **Visual references**, **Decisions**, dependencies, maturity (shared). Synthesize from Understanding **plus** conversation / decisions — do **not** only copy thin Understanding. A short Understanding is **not** permission to write a short spec. User-facing stems: Acceptance includes ≥1 **operable** outcome (§5.3).
3. After graduation, Understanding keeps only shape sections (§4). Spec = contract truth; **TODO** = living work checklist. **Same turn:** if Overview/Acceptance are product-shaped and High Priority is domain-only, apply §5.3 bridge (dual-track exercise path, phased note, or **library-only**) — do not leave product Acceptance with silent package TODOs.
4. If implementation diverges, update the spec **or** set Understanding to `superseded` and revise (§4) — do not leave both stale.

**Workflow *(ship-first / no Understanding on stem)*:** Keep a thin-but-real spec + TODO; capture lasting preferences on the spec **Decisions** table same turn (§10). Offer *lock shape* (Understanding) when identity fights start.

See [`Feature_Spec_Template.md`](../Feature_Spec_Template.md) and [`Feature_Understanding_Template.md`](../Feature_Understanding_Template.md).

---

## 3. Quick Start — Working on Any Task

**Minimal implement path** *(prefer this when ready under §0.1)*:

**Ready when:**

| Profile | Ready to code |
|---------|----------------|
| **`prevent`** | Understanding is `confirmed` (or user waived) and scope unchanged |
| **`balanced`** | If stem has Understanding → same as prevent; if none → thin spec + TODO exist and identity is clear |
| **`ship-first`** | Spec + TODO exist for the stem; no Understanding required |

1. Read `docs_profile` (if set) + `Master_Index.md` — Sections 1–3
2. Active TODO **Current focus** → that TODO → Understanding *(if present — read-only)* → spec → code
3. Skip drafting/graduation unless profile requires shape work, status is `draft` on an existing Understanding, the user changed scope, or Project Profile says game extensions apply
4. **Preference corrections → same turn:** if the user corrected a lasting UI/interaction preference that could be “improved away,” append 1-line **Decisions** row(s) on that stem’s spec and fix contradicting Behavior / Acceptance / Visual refs (§10). Do **not** wait for a session-wrap ask. Update **Current focus** as usual (§5.1) — it is handoff, not the decision log.

**Full Path A / Path B** when scoping new work, Understanding is required and missing/`draft`, or graduating to spec:

1. Read `Master_Index.md` — Sections 1–3 (overview, locations, Document Map)
2. Decide: **shared foundation work** (Path A) or **feature work** (Path B) — §1

### Path A — Shared foundation work

Use when building or changing a reusable component, API, or pattern in `_shared/`.

1. Open `_shared/[ComponentName].md`
2. **Understanding** — under **`prevent`**, or **`balanced`** when identity is unclear / multi-surface: open or draft `_shared/[ComponentName]-Understanding.md` first; show for shape review (§4). If already `confirmed` and scope unchanged, read only. Under **`ship-first`**, skip unless the file exists or user said *lock shape*.
3. Open the relevant shared TODO file(s) (create from [`TODO_Template.md`](../TODO_Template.md) if missing):
   - Core / foundation → `_shared/[ComponentName]-TODO.md`
   - In-Editor work → `_shared/[ComponentName]-InEditor-TODO.md` *(only if Project Profile game extensions apply, or user asked — unless excepted in Master Index §3.0)*
   - Assets & content → `_shared/[ComponentName]-Asset-TODO.md` *(same gate)*
4. Do the work when **ready** under the table above (not blocked on a draft Understanding that exists)
5. **Graduate** confirmed shape into the shared spec if Understanding was used and the spec is still placeholder (§2); under ship-first grow the spec as you go
6. **Update the shared TODO file(s)** before ending the session — refresh **Current focus** (§5.1)
7. If consumer features are blocked, ensure their TODOs link here — do not copy foundation tasks into feature TODOs

### Path B — Feature work

1. Open shared docs **only** when linked from this feature’s Understanding, spec, or TODO dependency notes — or the one shared component you are integrating now. Do **not** open every §3.1 “relevant” row.
2. Open `features/[FeatureName].md`
3. **Understanding** — same profile rules as Path A step 2 for `features/[FeatureName]-Understanding.md`
4. Open the relevant feature TODO file(s):
   - Core gameplay/systems → `features/[FeatureName]-TODO.md`
   - In-Editor work → `features/[FeatureName]-InEditor-TODO.md` *(Project Profile game extensions or user asked — §7)*
   - Assets & content → `features/[FeatureName]-Asset-TODO.md` *(same gate)*
5. Do the work when **ready** under the table above
6. **Graduate** or grow the feature spec per §2
7. **Update the feature TODO file(s)** before ending the session — refresh **Current focus** (§5.1)

If the work is really shared foundation, **stop** — use Path A instead.

**Golden Rule**: If you find yourself scrolling through a long file, stop and split (§8).

---

## 4. Understanding (Features & Shared)

**Source of truth** with §2 — other pack files summarize; this section wins on conflict. Drafting examples: [`Feature_Understanding_Template.md`](../Feature_Understanding_Template.md). **When required:** §0.1 docs profile.

Under **`prevent`**, each **feature** and substantial **shared component** gets a `-Understanding.md` — the agent’s model of **feature shape** (guardrails). **Not** a second durable spec. Under **`balanced`**, create when identity is ambiguous / multi-surface / split pressure / user asked. Under **`ship-first`**, only when user asks *lock shape* or the file already exists.

- Features: `features/FeatureName-Understanding.md`
- Shared: `_shared/ComponentName-Understanding.md`

**Who writes it:** Agent drafts first (`draft`) from conversation, design doc, or interview. User **reviews and corrects shape** — they do not author from scratch and are **not** approving the full contract here.

**Default under prevent:** Same Understanding for shared components as features. **Only skip** when the user **explicitly** excepts it (Master Index §3.0) **or** project `docs_profile` is `ship-first` / `balanced` allows skip. Under prevent, missing files or convenience are not exceptions.

**Shape sections only** (keep these; nothing else):

| Section | Put here | Do not put here |
|---------|----------|-----------------|
| **What this is** | Identity-defining user detail: category, metaphors, naming, “feels like,” ownership, product-defining constraints **and surface/architecture identity** (e.g. one continuous surface). Prefer user’s words. Brief feel/layout only if it defines the product. | Flows, module/API diagrams, edge matrices, acceptance lists, How-it-should-work, Core Behavior rewrite, padding/speculation |
| **What this is NOT** | Finished-feature **identity** boundaries (wrong category, wrong product surface/architecture, ownership) | Deferred phases, “not built yet,” backlog, or “NOT the final architecture yet” excuses — those → TODO / Current focus / spec roadmap |
| **Relationship** | Extends / wraps / reuses vs greenfield | Foundation task lists |
| **Assumptions** | Unchecked items needing shape confirmation | Full-spec open questions |
| **Confirmed with user** | Short correction notes + date | Relocated contract prose |

Work queue → **TODO**. Durable contract (Behavior, **Acceptance**, Visual references, architecture) → **spec** (§2).

**Tell the user:** Confirming Understanding = **is / is not** + **Assumptions** (shape). Spec-level detail may be missing on purpose.

**Status**:

| Status | Meaning |
|--------|---------|
| `draft` | Agent wrote/updated; shape not approved — **do not implement code** unless user waives. File **must exist** — `draft` ≠ skip creating Understanding |
| `reviewed` | User skimmed; minor edits may remain |
| `confirmed` | User approved **shape** — safe to implement without re-asking Understanding review; **graduate** contract to spec (§2). Not sign-off on every spec detail |
| `superseded` | No longer accurate — revise or reconcile |

**When `confirmed`:** Read for guardrails; proceed from TODO/spec. **Do not** re-surface for review unless shape/scope changes, conflict with code, or status returns to `draft` / `superseded`. Unchecked **Assumptions** after confirm → ask those items only.

**Reconciliation:** If code diverges from confirmed **shape**, update the spec + **Last reconciled with code**, or set `superseded` and draft a new Understanding. Run **only when** the user reports a mismatch, implementation contradicts Understanding, this session changes that feature’s shape/behavior, **or** you are updating that Understanding — **not** as a session-start repo-wide audit.

**On Understanding update — relocate + TODO** *(same turn, this stem only)*:

1. Trim to shape. Contract content removed from Understanding → **move into that stem’s spec** if missing, then delete from Understanding: legacy **Done when** → **Acceptance**; How-it-should-work / flows → **Behavior**; UI / screenshot tables → **Visual references** / Behavior. Do not discard; do not invent; do not park prose under **Confirmed with user**.
2. Open that stem’s `-TODO.md`; compare `[x]` items to destination (Understanding + spec) and code. **Uncheck** mismatches; reopen items / refresh **Current focus** when work reopened. Optionally align spec **Acceptance** the same way — never recreate Done when on Understanding.

**When to create or update:**

- New feature/change → draft or update Understanding (`draft` if shape changed)
- `docs/reference/` (or chat) → **build or update** live docs; create missing Document Map rows + file sets when material implies new stems
- Plan / “how should we build this” → if `confirmed`, use as guardrails + read spec; if `draft`/missing, draft shape first
- Identity assumption becomes clear → update **What this is NOT** (identity, not backlog)
- Two unlike identities were merged into one stem → **split** (§0 one-identity rule): new row + files; move content; do not leave a frankenstein Understanding
- User corrects you → update immediately (including split/move when they clarify separate features)
- After any update → run relocate + TODO check for that stem

**When planning:** Include the Understanding path; state confirmation is for **shape / guardrails**, not the full spec. Once shape implies a product surface/architecture, **lock it in is / is not** (or Assumptions) and default TODOs/plans to that **target** (agent timescale — not MVP → interim → rewrite). Stepped bullets = build/verify order inside one cut. Do not ask the user to remind you.

**Acceptance** lives on the **spec** (usually 3–7 coarse outcomes) — not on Understanding. **Visual references:** save under `docs/features/assets/`, `docs/_shared/assets/`, or `docs/reference/visuals/`; link from the **spec** with similar vs different — not from `-Understanding.md`. See [`../help/IDEA_CAPTURE_TIPS.md`](../help/IDEA_CAPTURE_TIPS.md#visual-references-screenshots).

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

- **High Priority sizing:** Prefer one item (or a tight cluster) that lands the **confirmed target architecture**. Sub-bullets / Medium Priority = verify slices or follow-ups — not “ship the wrong architecture first.” If Current focus fights confirmed Understanding, rewrite the TODO before coding ([`Agent_Timescale_Planning_Rule.mdc`](Agent_Timescale_Planning_Rule.mdc)).
- **Operable done / dual track:** See §5.3 — user-facing stems need domain **and** exercise-path rows; library-only stems must say so.
- **Exploration vs shipping:** See §5.2.
- **Session start:** Read the active TODO's **Current focus** block first (§5.1) — then High Priority.
- While working: Add new items as you discover them (including exercise-path rows when domain work reveals a missing run path — §5.3).
- After finishing a task: Mark `[x]`, add completion date/note.
- When a section gets long: Move finished items to Completed or archive (`-todo-complete.md`).
- **Session end:** Update **Current focus** for the next session.

### 5.1 Session handoff — Current focus

Each active `-TODO.md` should keep a short **Current focus** block at the top (see [`TODO_Template.md`](../TODO_Template.md)):

- One active task (or "blocked by …")
- Blockers with links
- Optional: last session date / agent tool

This gives the next agent (or a different tool) a 5-second orientation without re-reading everything.

### 5.2 Exploration vs shipping

When product shape is still unknown, a short **spike** (branch, throwaway prototype, learning pass) is fine. Label it clearly in Current focus / High Priority as **exploration** — not the destination architecture.

**Rules:**

- Spikes teach product rules; they are **optional**, not a required stage before the honest cut.
- Once Understanding (or the user) locks shape, the **paved path** is the target architecture. Do **not** promote the spike’s interim (e.g. caret bridging, dual systems) into High Priority milestones.
- After shape is clear: either land the target cut, or keep a named spike item explicitly disposable — never “Phase 1 wrong arch → Phase 2 correct” as the default plan when UX already implied the correct one.
- Lock 3–4 product rules when shape is ambiguous, then cut — do not use ambiguity as cover for shipping a known-wrong interim once rules are known.

### 5.3 Operable done — exercise path *(not library-by-default)*

**Failure mode:** Product-shaped Index / Understanding / Overview / Acceptance + domain-only TODOs/Architecture → agents clear packages and call the stem done. **Allowed only with an explicit bridge.**

**User/operator-facing milestone “done” requires:**

1. Domain work for that cut, **and**  
2. An **exercise path** (UI · CLI · product API · documented smoke) matching how the product is used, **and**  
3. Operable **Acceptance** for that claim closed **or** still covered by open TODOs  

| Bridge | When | How |
|--------|------|-----|
| **Dual-track TODOs** | Default for user-facing stems | High Priority = domain **and** surface/wire/smoke |
| **`library-only`** | Pure package / no operator surface on **this** stem | Label TODO/focus once; consumers own wire |
| **Phased** | Domain before surface **on purpose** | Loud: `library foundation first · exercise path: <named path>` — not silent package-only High Priority |
| **Scaffold + wire** | Product needs a surface but **no UI specs** | Minimal boring UI/CLI/smoke on High Priority / same cut — **not** Human-TODO “await design” unless user gated design-first / no UI / library-only |

**Do not:** invent a phase only because mockups are missing; treat blank canvas as a hard decide; twin every High Priority row onto Acceptance.

**Acceptance:** not a second checklist. Open **operable** lines = remaining work. When a TODO meets a line → update Acceptance same turn. “All TODOs `[x]`” + open operable Acceptance + no covering work = **incomplete** (stem drained / Layer done claims fail).

**Implement / verify / orchestrate:** add missing exercise-path TODOs when discovered; domain-only clearance without path/phase/library-only is not stem-done. Work-verifier **fails** claimed feature/Layer done that is domain-only without bridge, or that leaves matching operable Acceptance open with no TODO.

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

### 7.1 Catalog companions *(list-heavy content)*

**When:** Project Profile is game-style **or** a stem’s durable content is a growing **registry of rows** (units, fuels, tech goals, recipes, deployables, orbitals, loot tables) that would bloat the spec’s Behavior section.

**Create:** sibling `FeatureName-Catalog.md` (or `_shared/ComponentName-Catalog.md`) from [`Feature_Catalog_Template.md`](../Feature_Catalog_Template.md). Link it from the Document Map (**Catalog** column) and from a short **Catalog** pointer on the spec.

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

## 10. Decisions *(lightweight)*

Record **why** something was chosen — not every task, only choices with lasting impact. **Capture in the same turn as the choice** — do not rely on the user asking to wrap up the session.

| Where | Use for |
|-------|---------|
| **Decisions** section in feature or shared **spec** | Choices local to that piece ([`Feature_Spec_Template.md`](../Feature_Spec_Template.md)) |
| `docs/decisions/YYYY-MM-DD-short-title.md` | Cross-cutting choices ([`Decision_Template.md`](../Decision_Template.md)) |

**When to record:**

1. **Understanding review** — user confirms a tradeoff → add row(s) when graduating / updating the spec (§2).
2. **Implement / polish** *(confirmed stem)* — user corrects a **preference that could be “improved away”** (e.g. always-on vs proximity chrome, confirm-before-delete, hide type while writing, empty lines aren’t chunks) → **same turn** append 1-line row(s) to that stem’s **Decisions** table. If Behavior / Acceptance / Visual references still state the old contract, fix those sentences in the **same edit**.

**Skip:** pure spacing / pixel tweaks unless the user says “remember this.” Do **not** create `docs/decisions/` ADRs for feature-local polish. Do **not** dump choices into **Current focus** (handoff only — an optional one-line pointer to Decisions is fine).

**Pattern:** `date | choice | why (short)`. Prefer several rows on one polish burst over separate ADR files.

Link standalone decision files from Master Index §3.4.

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

**Project verify (handoff):** Fill **`docs/Tooling.md` → Project verify (agent handoff)** with this repo’s real build/typecheck/container/engine commands when known. After code changes, agents follow [`Agent_Build_Verify_Rule.mdc`](Agent_Build_Verify_Rule.mdc) (core install with modular rules): run those commands (or proportional stack defaults), **fix failures**, and only then tell the user they can test. Build green ≠ operable product (see §5.3); both apply when both apply.

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
