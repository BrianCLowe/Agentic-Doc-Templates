# Bootstrap Modular Docs — Agent Instructions

> Use when the user asks to set up, bootstrap, or initialize modular documentation in their project. Follow this **before** [`RULE_INSTALL.md`](RULE_INSTALL.md) (rules come after doc structure exists).

## Goal

Create the live `docs/` layout (Master_Index, feature folders, template pack in place) without leaving **this repo's** root `README.md`, `LICENSE.md`, or `CONTRIBUTING.md` in the project root when the user copied the whole template repository.

## Step 0 — How templates arrived (pick a path)

| Situation | Action |
|-----------|--------|
| `docs/templates/` copied (full pack with `help/`, `agent/`, scaffolds) | Skip Step 1 (relocate) unless whole repo. **Spot-check** pack (below) — do not walk the whole tree. |
| `docs/help/` and/or `docs/agent/` at `docs/` root (older layout) | Run **Step 0b — migrate layout**, then continue. |
| Flat files only in `docs/templates/` (oldest layout) | Run **Step 0b — migrate layout**, then continue. |
| Whole repo cloned/copied into the project | Do Step 1 (auto-move clearly upstream root files; ask only if ambiguous). |
| Submodule of [Agentic-Doc-Templates](https://github.com/BrianCLowe/Agentic-Doc-Templates) | Prefer copy of `docs/templates/`; optional Step 1 for root files if submodule is at repo root. |

## Step 0b — Migrate older layouts (if needed)

Reorganize without losing content. Target: **everything meta** lives under `docs/templates/`; live project docs stay at `docs/` root only.

| From (old) | To (current) |
|------------|--------------|
| `docs/help/` (entire folder at docs root) | `docs/templates/help/` |
| `docs/agent/` (entire folder at docs root) | `docs/templates/agent/` |
| `docs/templates/SETUP.md`, `USAGE.md`, `IDEA_CAPTURE_TIPS.md`, `USING_WITH_AGENTS.md` (flat in templates) | `docs/templates/help/` |
| `docs/templates/BOOTSTRAP.md`, `RULE_INSTALL.md`, `TEMPLATE_SYNC.md`, `rule-install-status.example.yaml` / `ADT-settings.example.yaml` (flat in templates) | `docs/templates/agent/` |
| `docs/templates/Modular_Docs_Workflow.md` (at templates root) | `docs/templates/agent/Modular_Docs_Workflow.md` |
| `docs/templates/upstream/` | `docs/templates/agent/upstream/` |
| `docs/templates/Modular_Documentation_Rule.mdc`, `Modular_Documentation_Rule.instructions.md` (flat in templates) | `docs/templates/agent/` |
| `docs/USING_WITH_AGENTS.md` (at `docs/` root) | `docs/templates/help/USING_WITH_AGENTS.md` |

Fix internal links after moving (including Master Index links to the workflow). **Keep at `docs/templates/` root:** `VERSION`, `CHANGELOG.md`, `Master_Index_Template.md`, `Feature_*_Template.md`, `TODO_Template.md`, `Decision_Template.md`, Tooling/Human_TODO templates. **Keep in `docs/templates/agent/`:** `Modular_Docs_Workflow.md` (index), `workflow/` modules, `roles/` (incl. `adapter-src/`), `GENERATE_ROLE_ADAPTERS.md`, rule templates (`.mdc`, `.instructions.md`), bootstrap, rule install, template sync. (`chat-ui/` may exist as a paused stub — not a live path.)

## Step 1 — Relocate upstream README, LICENSE, and CONTRIBUTING *(auto-move when clearly this pack)*

1. Check project root for `README.md`, `LICENSE.md`, and `CONTRIBUTING.md`.
2. Per file, decide **clearly upstream** vs **project-owned** vs **ambiguous**:

   **Clearly upstream — move immediately, do not ask** (any strong marker is enough):

   | File | Clear upstream markers |
   |------|------------------------|
   | `README.md` | Heading `# Agentic Doc Templates`, or body names **Agentic Doc Templates** / **Agentic-Doc-Templates** as *this* pack (not merely linking to it) |
   | `LICENSE.md` | **Creative Commons Attribution 4.0** plus **Brian Lowe** / **BrianCLowe** |
   | `CONTRIBUTING.md` | Heading `# Contributing to Agentic Doc Templates`, or body is about contributing to this template pack |

   Also treat as clearly upstream if the file repeatedly names **Brian Lowe**, **BrianCLowe**, or **Agentic Doc Templates** as the author/product of *these* root docs (not the user’s app).

   **Project-owned — do not move:** File describes the user’s app/product with no pack markers above.

   **Ambiguous — ask once** (only this case): Markers conflict or you cannot tell. Do not re-ask every session.

3. For each **clearly upstream** file:
   - Create `docs/templates/agent/upstream/` if needed.
   - Move → `docs/templates/agent/upstream/README.md` (or `LICENSE.md` / `CONTRIBUTING.md`).
   - Do **not** delete — attribution stays in the project.
   - Mention the move briefly in the bootstrap summary — **no confirmation prompt**.

4. Leave project-owned files alone. Suggest copying only `docs/templates/` next time (see [`../help/SETUP.md`](../help/SETUP.md)).

Do **not** overwrite a project-owned root `README.md`. If an upstream README is already under `agent/upstream/`, leave the user’s root README alone.

## Step 1b — Remove upstream GitHub config (user projects)

**This pack’s** `.github/` files are for [Agentic-Doc-Templates](https://github.com/BrianCLowe/Agentic-Doc-Templates) only (issue forms + Release workflow). They must **not** stay in a user’s app repo.

When the whole template repo was cloned/copied into a project (or “Use this template” left `.github/` behind):

1. If `.github/ISSUE_TEMPLATE/` exists **and** contains Agentic Doc Templates forms (e.g. `agent-tool-problem.yml`, `template-improvement.yml`, `docs-confusion.yml`, `feedback.yml`, or bodies that mention Agentic Doc Templates / modular docs templates) → **delete that directory**.
2. If `.github/ISSUE_TEMPLATE/` looks like the **user’s own** issue forms → **do not delete**.
3. If `.github/workflows/release.yml` exists **and** is the upstream pack Release workflow (e.g. workflow `name: Release`, builds `agentic-doc-templates-*.zip`, or comments/body mention Agentic Doc Templates pack releases) → **delete that file**. Remove `.github/workflows/` if it is empty afterward.
4. Pack-checks workflow cleanup is **Step 1d** (same whole-repo gate).
5. Do **not** delete the user’s other workflows, Copilot instructions, or other project GitHub config.
6. Remove `.github/` if it is empty afterward.
7. Prefer copying only `docs/templates/` next time so `.github/` never lands in the project.

## Step 1c — Remove upstream Cloud Agent config (user projects)

**This pack's** `.cursor/environment.json` configures the Cloud Agent dev environment for [Agentic-Doc-Templates](https://github.com/BrianCLowe/Agentic-Doc-Templates) itself — it only verifies the pack's release-build toolchain (`git`, `zip`, `awk`) and installs no app dependencies. It is **not** meant for a user's app and must **not** stay in their repo.

When the whole template repo was cloned/copied into a project (or “Use this template” left `.cursor/` behind):

1. If `.cursor/environment.json` exists **and** is the upstream pack config (e.g. `"name": "Agentic Doc Templates"`, or its `install` only checks the release-build toolchain / mentions Agentic Doc Templates and installs no real app dependencies) → **delete that file**.
2. If `.cursor/environment.json` looks like the **user's own** environment (installs their app's dependencies, references their stack, starts their services) → **do not delete**.
3. Do **not** delete the user's other `.cursor/` config (rules, MCP config, etc.). Remove `.cursor/` only if it is empty afterward.
4. Prefer copying only `docs/templates/` next time so `.cursor/` never lands in the project.

## Step 1d — Remove upstream maintainer tooling (user projects)

**This pack's** root `eval/`, root `scripts/` (CI helper), and any leftover `docs/templates/agent/scripts/*.py` are for maintaining [Agentic-Doc-Templates](https://github.com/BrianCLowe/Agentic-Doc-Templates) itself. They must **not** stay in a user’s app repo. Adapter regeneration for pack editors is the markdown playbook [`GENERATE_ROLE_ADAPTERS.md`](GENERATE_ROLE_ADAPTERS.md) — **no Python**.

When the whole template repo was cloned/copied into a project (or “Use this template” left these behind):

1. If project-root **`eval/`** exists **and** is this pack’s harness (e.g. `eval/run_eval.py`, `eval/cases/additive-keeps-confirmed.json`, or `eval/README.md` names Agentic Doc Templates / modular-docs behavioral eval) → **delete the entire `eval/` directory**.
2. If project-root **`scripts/gen_role_adapters.py`** exists (upstream CI helper) → **delete that file**. Remove root `scripts/` if it is empty afterward.
3. If **`docs/templates/agent/scripts/`** exists with pack Python helpers (e.g. `gen_role_adapters.py`) from an older pack zip → **delete that directory** (the playbook replaced it).
4. If `.github/workflows/pack-checks.yml` exists **and** is this pack’s integrity workflow (e.g. workflow `name: Pack checks`, runs `gen_role_adapters.py --check` and/or `eval/run_eval.py`) → **delete that file**. Remove `.github/workflows/` / `.github/` if empty afterward (same care as Step 1b — do not delete the user’s other workflows).
5. Do **not** delete `docs/templates/agent/roles/adapter-src/` or [`GENERATE_ROLE_ADAPTERS.md`](GENERATE_ROLE_ADAPTERS.md) — those are pack files.
6. Do **not** delete a user’s own `eval/` or `scripts/` that are clearly for their app (different README / no Agentic Doc Templates markers).
7. Prefer copying only `docs/templates/` next time so maintainer folders never land in the project.

## Step 2 — Create docs layout

Create if missing:

```
docs/
├── Master_Index.md          ← from Master_Index_Template.md (Step 3)
├── Tooling.md               ← from Tooling_Template.md (Step 3b — machine tools)
├── Human-TODO.md            ← from Human_TODO_Template.md (Step 3c — human inbox)
├── ADT-settings.yaml        ← pack prefs (tools, optionals, sync mode, upstream) when first recorded
├── _shared/
│   └── assets/
├── decisions/
├── features/
│   └── assets/
├── reference/               ← design docs, chat exports, PRDs, legacy specs (not living modular docs)
│   ├── README.md            ← short “what goes here” (create if missing — see below)
│   └── visuals/             ← optional inspiration screenshots
└── templates/               ← full template pack (not live project content)
    ├── help/
    ├── agent/
    └── … scaffolds + workflow
```

If `docs/reference/README.md` is missing, create it with:

```markdown
# Reference materials

**Recommended:** export idea chats (Grok.com, ChatGPT, Claude web, …) to markdown and drop them here — often several threads as you work out different aspects of an app or game. Raw conversations keep your whys, rejects, and motives; polished design docs often lose those.

Then ask: *Build or update the live docs from `docs/reference/`.* Agents draft or revise Understandings (and Document Map rows) and should split unlike identities on their own.

Also fine here: design docs, PRDs, Notion/export dumps, legacy specs. When you have both a chat export and a cleaned write-up, keep **both**.

Living modular docs stay in `features/`, `_shared/`, and `Master_Index.md`. Agents read files here when you point at them (or when converting to modular docs); they do not treat this folder as the Document Map.

Optional: `visuals/` for inspiration screenshots before a feature folder exists.
```

**Pack spot-check** (enough to proceed — do not inventory every file):

- `VERSION`, `CHANGELOG.md`, `agent/Modular_Docs_Workflow.md`, `agent/BOOTSTRAP.md`, `help/SETUP.md`

If any of those are missing, expand the inventory below and run Step 0b if layout looks old. Otherwise continue.

**Full inventory** *(only if spot-check fails):*

- **Root:** `VERSION`, `CHANGELOG.md`, `Master_Index_Template.md`, `Feature_Spec_Template.md`, `Feature_Understanding_Template.md`, `TODO_Template.md`, `Decision_Template.md`, `Tooling_Template.md`, `Human_TODO_Template.md`
- **`help/`:** `SETUP.md`, `USAGE.md`, `IDEA_CAPTURE_TIPS.md`, `USING_WITH_AGENTS.md`
- **`agent/`:** `Modular_Docs_Workflow.md`, `workflow/` (modules), `roles/` (+ `adapter-src/`), `GENERATE_ROLE_ADAPTERS.md`, `BOOTSTRAP.md`, `RULE_INSTALL.md`, `TEMPLATE_SYNC.md`, `TEMPLATE_SYNC_A.md`, `TEMPLATE_SYNC_B.md`, `TEMPLATE_UPDATE_CHECK.md`, `Modular_Documentation_Rule.mdc`, `Modular_Documentation_Rule.instructions.md`, `Agent_Timescale_Planning_Rule.mdc`, `Agent_Timescale_Planning_Rule.instructions.md`, `Agent_Build_Verify_Rule.mdc`, `Agent_Build_Verify_Rule.instructions.md`, `Template_Update_Check_Rule.mdc`, `Template_Update_Check_Rule.instructions.md`, `ADT-settings.example.yaml`

Run Step 0b if any setup files are still at `docs/` root or flat in `docs/templates/`.

## Step 3 — Create live Master_Index

If `docs/Master_Index.md` does not exist:

1. Copy content from `docs/templates/Master_Index_Template.md`.
2. Replace bracketed placeholders; set **Pack version** from local `docs/templates/VERSION`.
3. Fill Document Map (§3) from **this conversation and Project Profile** — do not leave §3.2 empty if the user named **features**. Leave **§3.1 Shared empty** unless the user named a truly shared, project-owned piece used by multiple features — do **not** invent `_shared/` rows or dump engine/framework overview (e.g. generic Unreal notes) there. Open README only if overview/map are empty. Do **not** invent features from a codebase scan.

If `Master_Index.md` already exists → do not overwrite; offer [`TEMPLATE_SYNC.md`](TEMPLATE_SYNC.md) instead.

## Step 3b — Create live Tooling.md

If `docs/Tooling.md` does not exist:

1. Copy from `docs/templates/Tooling_Template.md`.
2. Fill **Required** (and optional) tools from Project Profile and this conversation — mark guesses for the user to confirm. Open README only if the stack is unknown.
3. Ensure Master Index Key Locations / §3.4 link to `Tooling.md`.

If it already exists → do not overwrite; offer to update rows when the stack changes.

## Step 3c — Create live Human-TODO.md

If `docs/Human-TODO.md` does not exist:

1. Copy from `docs/templates/Human_TODO_Template.md`.
2. Add Open rows for any human-gated needs implied by the conversation / Document Map — `procure` (keys/portals), `playtest`, `decide`, or `waiting`. Leave empty Open table if none yet.
3. Ensure Master Index §3.3 / §3.4 link to `Human-TODO.md`.

If it already exists → add newly discovered human-gated needs (procure / playtest / decide / waiting); do not wipe user-completed rows.

## Step 3p — Project preferences *(one batch ask — before Step 3d)*

**Mandatory:** Present **and explain** every still-unset preference below in **one** user-facing message. Do **not** drip-feed separate quizzes across later steps for the same keys. Skip only keys already set in `docs/ADT-settings.yaml`. Create/update that file from [`ADT-settings.example.yaml`](ADT-settings.example.yaml) when recording.

**You must include** (when unset):

| # | Preference | Key | Why it matters |
|---|------------|-----|----------------|
| A | **Docs profile** (ceremony) | `docs_profile.mode` | Controls whether Understanding + shape-confirm block code. **Required before Step 3d** file create. |
| B | **Template update checks** | `optional_rules.template-update-check` | Optional upstream VERSION ping |
| C | **Doc roles** | `optional_rules.doc-roles` | Optional subagent adapters (orchestrator stays parent-only) |
| D | **Pack sync mode** | `sync.mode` | How TEMPLATE_SYNC handles live optionals |
| E | **Orchestrator git** | `orchestrator.git.mode` | How long unattended runs land in git — **important**; never silent-default |

### How to present *(agent requirements)*

1. Skim conversation + `docs/reference/` if present (do not inventory the whole repo) for docs-profile + git recommendations only.
2. Lead with: *“I need a few project preferences once — all in this message. Pick each or say ‘defaults’ / accept suggestions.”*
3. For **each** unset row: short plain-language **what it does**, the **options**, and your **suggestion** (with 1–3 citations for docs profile when reference exists).
4. Wait for answers (or “use your suggestions”) → record all chosen keys + `recorded` today + `source` where applicable → continue to Step 3d.
5. If they only answer some rows, re-ask **only** the missing ones before 3d (docs profile is blocking for 3d).

### A — Docs profile *(options to explain)*

| Mode | Tell the user |
|------|----------------|
| **`prevent`** *(suggested default if unclear)* | Agent drafts `-Understanding.md` first; **you confirm shape** (is / is not) before code. Best when wrong product identity is expensive. |
| **`balanced`** | Spec + TODO always; Understanding **only when** product identity is fuzzy (competing surfaces, “not X”, multi-feature mush, or you ask to lock shape). You are choosing “judgment call,” not “no docs.” |
| **`ship-first`** | Spec + TODO only; no shape-confirm gate. Faster; fix-forward via verify + Human-TODO. *Lock shape for X* anytime. |

Suggest with citations when possible (prevent / balanced / ship-first signals — Workflow §0.1).

### B — Template update checks

Explain: optional rule pings upstream `VERSION` only; then they can TEMPLATE_SYNC. Default cadence **`always`** (per session) or **`interval`**. Options: **enable** (always or interval) / **decline**.

### C — Doc roles

Explain: optional Understanding author, implementer, work verifier, etc. as harness adapters; short asks still work without install; orchestrator is never a subagent. Options: **enable** / **decline**.

### D — Pack sync mode

| Mode | Tell the user |
|------|----------------|
| **`auto`** | Recommended live updates + hygiene commits without mid-sync quizzes; still asks for brand-new pack optionals |
| **`auto-all`** | Same + enable/install unset pack optionals (never re-enable declined). **Still asks orchestrator git** (see E / B0.6) |
| **`choose`** | Ask about live optionals each sync |

### E — Orchestrator git *(always explain fully when unset)*

| Mode | Tell the user |
|------|----------------|
| **`milestone-pr`** *(suggest if remote + forge CLI)* | **Overnight drain:** each verified slice → own branch → draft PR → build-verify → squash that slice → mark ready → **wait CI / accept Bugbot auto-fixes** → **merge** → new branch for the next slice. Reviewable diffs; work lands before morning. |
| **`branch-pr-squash`** | One run branch → milestone commits → draft PR mid-run → end: **build-verify → squash the whole run to one commit → mark ready** (no merge). Use when you want **one morning PR** to review yourself. |
| **`branch-pr`** | Same without squash — keeps milestone history on the PR. Unattended CI after the run. No merge. |
| **`branch-push`** *(suggest if remote, no forge CLI)* | Same without PR |
| **`local`** *(suggest if no remote)* | Milestone commits only; nothing leaves the machine |
| **`current-push`** | Commit + **push the branch you are on now** (often `main`). Solo / you own the remote. **Never** applied without you picking it. |
| **`none`** | No commits during orchestration |

**Cloud Agents:** if they later orchestrate in Cursor Cloud (or similar) while this key stays `local` / `none` / `branch-pr-squash` / etc., the agent uses **`milestone-pr` for that run only** and does **not** rewrite this setting — see [`roles/orchestrator-git.md`](roles/orchestrator-git.md) **Cloud Agent path**.

**Never** silent-default **`current-push`**. Git strategy is high-impact — if they shrug, restate the suggestion and get an explicit pick (or “use suggestion”).

**After they pick a git mode** → run **Forge tooling probe** ([`roles/orchestrator-git.md`](roles/orchestrator-git.md)): infer forge from remote; if **`milestone-pr` / `branch-pr` / `branch-pr-squash`** and CLI missing → **ask to install**; if CLI present but not logged in (or just installed) → **ask to start auth** (install ≠ ready for PRs). Fall back to push + human PR / switch mode if they decline. Do not silent-install or silent-login.

### Optional — standing workflow notes *(not a mandatory quiz row)*

After recording A–E, **one optional line** is enough: *“Any standing workflow notes to save in `docs/ADT-settings.yaml` (agent process prefs the enums don’t cover)?”* Skip on no / defaults / silence. Do **not** invent bullets. Primary path is **lookout capture** later (Workflow §0.2): when they state always/never prefs that oppose pack defaults, append `standing.instructions` same turn.

Explicit later (any preference): *Set docs profile to …* / *Set sync to …* / *Set orchestrator git to …* / *Add standing note: …* / enable-decline optionals.

## Step 3d — Create files for every Document Map row *(mandatory)*

**A Document Map row is not documentation.** If you put a feature or shared component in §3.1 / §3.2, you **must** create the **profile default file set** in the same session (Workflow §0 / §0.1). Read `docs_profile.mode` (unset → **prevent**).

| File | `prevent` | `balanced` | `ship-first` |
|------|-----------|------------|--------------|
| `*.md` spec | always (stub OK) | always | always |
| `*-TODO.md` | always | always | always |
| `*-Understanding.md` | always (`draft`) | when identity ambiguous / multi-surface / split / user asked; else optional | only if user asked *lock shape* |

Add InEditor/Asset TODOs when Project Profile / game extensions apply.

**Do not:**

- Leave map-only “planned” rows with broken or missing links “until the user picks one”
- Under **`prevent`**: treat the Understanding `draft` gate as a reason to **skip creating** Understanding files — `draft` blocks **coding**, not **writing docs**
- Under **`ship-first`**: invent Understanding files “just in case”
- Create nine fully graduated specs before the user confirms — stubs (+ draft Understandings when required) are correct

**When many features were named** (e.g. 5+):

1. Create the profile default file set for **every** map row.
2. If Understandings were created: tell the user which to review first (Path A foundation or the feature they care about most).
3. Optionally ask once: “Review all draft Understandings, or start with [X]?” — do **not** wait for that ask before creating the files.

If the user named **no** features yet, skip Step 3d and say so in Step 4.

## Step 4 — Tell the user what's next

1. Confirm or correct Section 1 (Project Overview), Document Map, `docs/Tooling.md`, and `docs/Human-TODO.md`. Confirm **preferences** recorded in Step 3p (docs profile, sync, git, optionals).
2. If draft `-Understanding.md` files exist — user reviews / corrects **shape** before implementation (**prevent** / those stems). Under **ship-first**, point at specs + TODOs instead.
3. Point at **Open** items on `Human-TODO.md` — things only the human can close (procure, playtest, decide, waiting).
4. After they confirm an Understanding (when used), graduate durable content into the spec and continue from TODOs ([`../help/SETUP.md`](../help/SETUP.md)). Under ship-first, continue from TODOs and grow the spec as you build.
5. **Preference catch-up:** if any Step 3p key is still unset, re-present **only** the missing rows (same explanations as 3p) before finishing — do not invent defaults for **orchestrator git** or **current-push**.
6. Optional: run [`RULE_INSTALL.md`](RULE_INSTALL.md) for agent rules (asks per tool, records in `docs/ADT-settings.yaml`). If doc-roles or update-check were **enabled** in 3p, RULE_INSTALL also installs those optional artifacts.

### Preference detail (reference — already covered in Step 3p)

| Topic | On enable / choose |
|-------|--------------------|
| Template update-check **yes** | Set `optional_rules.template-update-check` enabled; `upstream:` + `local_pack_version`; `check_mode` always or interval + `check_mode_recorded` |
| Doc roles **yes** | `optional_rules.doc-roles` enabled; install adapters via each `tools/<key>.md` on RULE_INSTALL |
| Update-check / roles **no** | Record `declined` |
| Explicit later | *Enable template update checks* / *Enable optional doc roles* / *Set sync to …* / *Set docs profile to …* / *Set orchestrator git to …* |

## Do not

- Overwrite an existing project `README.md` that is not the upstream template readme.
- Put project feature content into `docs/templates/` (templates stay canonical reference only).
- Create `docs/help/` or `docs/agent/` at docs root — those belong inside `docs/templates/`.
- Leave Agentic Doc Templates `.github/ISSUE_TEMPLATE/`, `.github/workflows/release.yml`, or `.github/workflows/pack-checks.yml` in a user project — delete them (Step 1b / 1d).
- Leave the pack's own `.cursor/environment.json` (Cloud Agent env config) in a user project on a whole-repo copy — delete it (Step 1c); keep the user's own env/rules.
- Leave upstream root **`eval/`**, root **`scripts/gen_role_adapters.py`**, or leftover **`docs/templates/agent/scripts/*.py`** in a user project on a whole-repo copy — delete them (Step 1d); keep [`GENERATE_ROLE_ADAPTERS.md`](GENERATE_ROLE_ADAPTERS.md).
- Ask before moving root files that are **clearly** upstream (Agentic Doc Templates / Brian Lowe / BrianCLowe markers) — just move them.
- Finish bootstrap with a filled Document Map but **no** feature/shared files on disk.
- Put human-gated items only in feature TODOs — dual-write `docs/Human-TODO.md` + owner TODO (Workflow §13).
- Drip-feed preference quizzes (4b/4c/4d/4e-style) when Step 3p already covers them — **one batch**.
- Silent-default `sync.mode` or **`orchestrator.git.mode: current-push`** without the user picking them.
- Skip Step 3p (or stay silent about unset prefs) because the user did not ask — present and explain; record decisions.
- Keep writing `docs/rule-install-status.yaml` / `docs/upstream-status.yaml` on new projects — use `docs/ADT-settings.yaml` only.

## Example user prompts

- "Bootstrap modular docs in this project."
- "Set up the Agentic Doc Templates documentation structure."
- "I copied the whole templates repo — clean up and initialize docs."

## Related

- Human setup guide: [`../help/SETUP.md`](../help/SETUP.md)
- **How to use** (chat → docs, ideas, design docs): [`../help/USAGE.md`](../help/USAGE.md)
- Rule install (after bootstrap): [`RULE_INSTALL.md`](RULE_INSTALL.md)
- Template sync (updates): [`TEMPLATE_SYNC.md`](TEMPLATE_SYNC.md)
- Cheap update ping: [`TEMPLATE_UPDATE_CHECK.md`](TEMPLATE_UPDATE_CHECK.md)
