---
name: Modular Documentation
description: Read Master_Index first; follow Modular_Docs_Workflow for procedure
applyTo: "**"
---

# Modular Documentation Rule

First, check if `docs/Master_Index.md` exists. If it does not exist, ignore this entire rule and work normally.

This project uses a lean modular documentation system. `docs/Master_Index.md` is the single entry point for **project context and the Document Map**. Procedure index: **`docs/templates/agent/Modular_Docs_Workflow.md`** (paved path + router) — open it only when the gates below say so, then open **one** named module under `docs/templates/agent/workflow/`.

**Route by ask** *(open only that playbook — do not scan the pack catalog)*:

| User ask | Open only |
|----------|-----------|
| bootstrap / init modular docs | see **Optional subagents** → else `docs/templates/agent/BOOTSTRAP.md` |
| update / sync doc templates | see **Optional subagents** → else `docs/templates/agent/TEMPLATE_SYNC.md` |
| check for template updates | `docs/templates/agent/TEMPLATE_UPDATE_CHECK.md` |
| install agent rules | `docs/templates/agent/RULE_INSTALL.md` → then only `docs/templates/agent/tools/<key>.md` for each tool |
| regenerate role adapters / sync cursor\|grok agents from adapter-src | `docs/templates/agent/GENERATE_ROLE_ADAPTERS.md` |
| draft / revise Understanding, new idea, capture intent, correct What this is / is NOT, build/update live docs from `docs/reference/` | see **Optional subagents** → else `docs/templates/agent/roles/understanding-author.md` |
| graduate confirmed Understanding → spec | see **Optional subagents** → else `docs/templates/agent/roles/doc-graduate.md` |
| implement / continue Current focus (Understanding `confirmed`, scope unchanged) | see **Optional subagents** → else session default below |
| orchestrate / drive backlog / clear TODOs / run until blocked | **parent only** → `docs/templates/agent/roles/orchestrator.md` (do **not** spawn an orchestrator subagent) |
| verify completed unit vs Understanding/spec/TODO | see **Optional subagents** → else `docs/templates/agent/roles/work-verifier.md` |
| todo warden / reconcile TODOs vs implementation / TODO honesty after orchestration / todo cleanup / archive completed TODOs | see **Optional subagents** → else `docs/templates/agent/roles/todo-warden.md` |
| feature / shared work (other) | `docs/Master_Index.md` + that feature’s or component’s files |

**Optional subagents** *(parent orchestrates — user need not type `/`; harness-agnostic)*:

When an ask matches a row below, look for that role under a known agents folder (table filename is `<name>.md`):

- `<name>.md` under `.cursor/agents/`, `.grok/agents/`, `.claude/agents/`, `.codex/agents/`
- `<name>.agent.md` under `.github/agents/` (Copilot CLI / Agents window / Chat custom agents)

- If found → **delegate / spawn** that type with a self-contained prompt (feature/component name, paths, user’s ask). On Grok Build: `spawn_subagent` with `subagent_type: <name>` when `.grok/agents/<name>.md` exists. Do **not** treat `.cursor/agents/` as Grok types. On Copilot: delegate `.github/agents/<name>.agent.md` (CLI `/agent` or inference). Do **not** treat `.cursor/agents/` as Copilot types. User-global `~/.copilot/agents/` is personal — prefer project `.github/agents/`.
- If missing → follow the **Fallback** playbook/role **in this session** (or spawn a generic child with that playbook path).
- **Orchestrator exception:** matching *orchestrate / drive backlog / …* → follow `docs/templates/agent/roles/orchestrator.md` **in this parent session** only. That playbook spawns leaf workers (`feature-implementer`, `work-verifier`, `todo-warden`). Never install or spawn `orchestrator` as a harness subagent type.

| When ask matches | Agent filename | Fallback |
|------------------|----------------|----------|
| draft/revise Understanding, new idea, intent, identity correction, build/update from `docs/reference/` | `understanding-author.md` | `docs/templates/agent/roles/understanding-author.md` |
| user confirmed Understanding → update durable spec | `doc-graduate.md` | `docs/templates/agent/roles/doc-graduate.md` |
| implement / continue from Current focus | `feature-implementer.md` | session default below |
| orchestrate / drive backlog / clear TODOs / until blocked | *(parent only — do not spawn)* | `docs/templates/agent/roles/orchestrator.md` |
| verify completed unit vs Understanding/spec/TODO | `work-verifier.md` | `docs/templates/agent/roles/work-verifier.md` |
| todo warden / reconcile TODOs / TODO honesty / gaps after orchestration / todo cleanup / archive completed | `todo-warden.md` | `docs/templates/agent/roles/todo-warden.md` |
| bootstrap / init modular docs | `docs-bootstrap.md` | `docs/templates/agent/BOOTSTRAP.md` |
| update / sync doc templates | `docs-template-sync.md` | `docs/templates/agent/TEMPLATE_SYNC.md` |

**Do not** delegate every message — only when a row above matches. Stay in this session for tiny follow-ups, clarifying questions only, or when the user says to stay here / skip subagents. Do **not** turn a single-slice Current focus ask into full orchestration unless the user said orchestrate / drive backlog / clear TODOs. These must not replace this rule or compete like always-on skill packs. Roles: `docs/templates/agent/roles/README.md`. Tool install paths: `docs/templates/agent/tools/README.md`.

**Docs profile** *(read `docs/ADT-settings.yaml` → `docs_profile.mode`; unset = **`prevent`** — Workflow §0.1)*:
| Mode | New map-row files | Coding gate |
|------|-------------------|-------------|
| **`prevent`** | Spec + Understanding (`draft`) + core TODO | No code while Understanding is `draft` (unless waived) |
| **`balanced`** | Spec + TODO; + Understanding when identity ambiguous / multi-surface / split / user asked | Draft gate only if that stem **has** Understanding |
| **`ship-first`** | Spec + core TODO | No Understanding gate; implement from TODO + thin spec |
If `docs_profile` is unset at bootstrap / first build-from-reference / sync: suggest once from `docs/reference/` (cite 2–3 snippets) → ask → record. Never silent-downgrade a project full of Understandings.

**Standing workflow** *(read `docs/ADT-settings.yaml` → `standing.instructions` when present — Workflow §0.2)*:
- Non-empty bullets = durable **agent process / pack workflow** prefs. Apply after hard safety + this-turn user ask; before pack defaults.
- **LOOKOUT (every turn):** user states a lasting pref that **opposes pack defaults**, corrects how you just worked, or says always/never/from now on about **process** (git/PR/ceremony/verify/re-ask) → **same turn** set the first-class ADT-settings key if one fits, else **append** a short bullet under `standing.instructions` and say you saved it. Do not wait for wrap-up.
- Product/UI prefs for one stem → spec **Decisions** (§10), not standing. One-off “just this run” → do not write standing. Never invent standing notes.

**Session default** *(implement / continue when ready under docs profile and scope unchanged)*:
1. Read `docs_profile` if present; read non-empty `standing.instructions`; read `docs/Master_Index.md` Sections 1–3.
2. Open the active TODO — read **Current focus** first (Workflow §5.1):
   - Shared foundation → `_shared/ComponentName-TODO.md`
   - Feature work → `features/FeatureName-TODO.md`
   - InEditor / Asset TODOs: only when Project Profile **Game extensions** / user indicates game-style work — default is **core TODO only**
3. Read that item’s `-Understanding.md` **if it exists** (context) and spec as linked — do not re-ask for review unless scope changes (Workflow §4).
4. Before integrating a **shared** piece, check its **Maturity** on the spec or Document Map (`draft` | `usable` | `stable`).
5. If the user asks to install tooling: follow **`docs/Tooling.md`** (Workflow §11) — Required (+ skills if listed); Optional only if asked; verify all; ask before admin/large SDKs.
6. If work needs a **human** (procure, playtest/feel, decide/sign-off, or external waiting): **dual-write** in the same edit — owner `*-TODO.md` item **and** an Open row on **`docs/Human-TODO.md`** (Workflow §13). Never store secrets in docs. Do not bury human asks only in feature TODOs.

**Open `Modular_Docs_Workflow.md` (index) only when:** creating files, choosing Path A vs Path B, graduating Understanding → spec, docs-profile or standing-capture questions, or the user asks about procedure. Then open **only the one module** the index router names (e.g. `workflow/understanding.md` for shape/de-confirm). Do **not** load the whole `workflow/` folder or re-read the index every turn.

**Shared foundation (critical):**
- **Do not invent `_shared/` docs.** Only add §3.1 / `_shared/` when a **project-owned** piece is (or will be) used by **two or more features**, or the user named it as shared. Empty `_shared/` / empty §3.1 is fine. Never park engine/framework primers (e.g. generic Unreal notes) in `_shared/` because nothing else fit — use `features/` or `docs/reference/` (Workflow §1).
- When a real shared component exists: same **profile default file set** as features (Workflow §0.1, §1). §3.0 exceptions are **user-requested only** — never invent them because files are missing or to “leave for later.” Project ceremony is `docs_profile`, not a fake §3.0 “no Understanding project-wide.”
- **File layout:** create only paths from Workflow **§0** / Document Map — flat files in `features/` and `_shared/` (optional `-Catalog.md` for list-heavy stems — Workflow §7.1).
- **Document Map = files on disk.** Adding a §3.1/§3.2 row requires creating the **profile default file set** in the same turn (always spec + core TODO; Understanding per §0.1). A **Catalog** map cell requires `*-Catalog.md` the same turn. Never leave map-only “planned” rows. Bootstrap Step 3d. **Do not add filler §3.1 rows.** Do **not** add map rows for vague planned-only items. Kit leftovers stay as TODOs on the **inventory/owning stem** until that slice is next (Workflow §0 inventory · §5.4) — do not spawn empty stems for every method. A terse wrap-the-public-API goal is **actionable** (expand TODOs from the docs), not a stub.
- Real shared components get the **same note types as features** (for the profile) unless the user explicitly excepted specific files — record those in Master Index **§3.0** (Workflow §1). If core TODO or required Understanding is missing for a mapped row (and no user exception / profile skip), **create them**.
- Tasks that **build or refactor** a shared component go in `_shared/ComponentName-TODO.md` (and related shared TODOs) — **not** in a consumer feature's TODO.
- Feature TODOs only **link** to shared TODOs when blocked or integrating (dependency note), they do not duplicate foundation tasks.

**Before implementation:**
- **`prevent`:** **Draft `-Understanding.md` first** when scoping — agent writes; user confirms **shape** only (Workflow §4). `draft` blocks **coding**, not creating the file. Shape-only sections — not a second spec. Capture **product-defining surface/architecture identity** in is / is not when stated (module/API detail → spec). Tell the user confirmation is **is / is not + Assumptions**, not a full spec review.
- **`balanced`:** Draft Understanding when identity is ambiguous / multi-surface / split / user asked; otherwise thin spec + TODO is enough to start.
- **`ship-first`:** No Understanding required; implement from Current focus + thin spec. Offer *lock shape for [Stem]* when identity fights start.
- Do not treat as greenfield if Understanding says it extends/reuses existing work.
- Do not code while an **existing** Understanding is `draft` unless the user waives review (all modes).
- **`confirmed`** → shape approved; continue from TODO/spec without re-asking Understanding review. Plans/TODOs target that shape at agent speed — no user reminder required.
- Plans: under prevent (or when Understanding exists), include Understanding path + “confirm shape, not full spec” — unless already `confirmed` and unchanged. Stepped plans = verify order; exploration spikes stay labeled (Workflow §5.2).
- Vague ideas → brief questions from `docs/templates/help/IDEA_CAPTURE_TIPS.md`, then draft Understanding (**prevent** / when locking shape) or thin spec + TODO (**ship-first** / clear **balanced**).
- **`docs/reference/` → live docs:** when the user drops exports and asks to build/update — create missing Document Map rows + **profile default file sets**; draft/revise Understandings when the profile requires them. If material covers **two unlike identities**, **split** stems (Workflow §0) — do not glue them into one Understanding to stay “tight.” If `docs_profile` unset, suggest + ask once (Workflow §0.1) before bulk create.
- After confirm → **graduate** contract to the spec when Understanding was used (Workflow §2). Under ship-first, grow the spec as you implement. Screenshots → spec **Visual references**. Row registries → optional `-Catalog.md`. Lasting tradeoffs → spec **Decisions** or `docs/decisions/` (Workflow §10) — including implement-time preference corrections (same turn).

**While working:**
- **Session start:** Read the active TODO's **Current focus** block first.
- Treat the active TODO as the living task list; add items as discovered; use Cross-Feature Dependencies when features interact. Rewrite Current focus that fights confirmed Understanding (or clear product identity under ship-first) before coding.
- **Operable (Workflow §5.3):** user-facing stems need exercise path (or library-only / loud phase); no UI specs → still scaffold+wire; open operable Acceptance without covering TODOs = incomplete.
- **Kit coverage (Workflow §5.4):** in-scope spec surfaces need TODO items on an **existing** stem. Writing them is not inventing work. “Picked up” = start the unit, not create the backlog row. Terse + public API docs → expand from the docs; do not interview each facet.

**After changes (mandatory):**
- **Build & verify** on code changes before “you can test” (`docs/Tooling.md` Project verify / stack defaults — `Agent_Build_Verify_Rule`).
- Update **Current focus** + `-TODO.md` (`[x]` + date; **move** finished items into **Completed**). Human-TODO feedback → sync owner + Human-TODO Done (§13); never mark human rows from assumptions.
- Update Understanding/spec **only if this session** changed shape/contract. Preference corrections → same-turn Decisions + fix stale Behavior/Acceptance/Visual (§10). **Pack/process prefs that oppose defaults** → same-turn standing or first-class ADT-settings key (§0.2). Understanding update → relocate + TODO uncheck (§4). No session-start full reconcile.

**Clarification** (*review spec* / *gaps* / *confidence* for a **named** stem): re-read **that** stem only; ≤5 questions; wait for confirm; no unrelated stems.

**Philosophy:** Small accurate docs; short asks → one playbook; tight scope = paved path (not alternate audits). User workflow notes stick via standing (§0.2). Not: human-sprint interim arch when shape is clear · library checklist = product done · ignore open operable Acceptance · finished-kit spec with no covering TODOs · wait-for-pickup instead of drain · let process prefs die with the chat. Mermaid only when it beats prose (§12). TODO Current focus = agent memory; Human-TODO = human inbox.
