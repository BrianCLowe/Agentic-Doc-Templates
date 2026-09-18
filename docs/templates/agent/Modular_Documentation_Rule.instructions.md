---
name: Modular Documentation
description: Read Master_Index first; follow Modular_Docs_Workflow for procedure
applyTo: "**"
---

# Modular Documentation Rule

First, check if `docs/Master_Index.md` exists. If it does not exist, ignore this entire rule and work normally.

This project uses a lean modular documentation system. `docs/Master_Index.md` is the single entry point for **project context and the Document Map**. Procedure index: **`docs/templates/agent/Modular_Docs_Workflow.md`** (paved path + router) — open it only when the gates below say so, then open **one** named module under `docs/templates/agent/workflow/`. Do **not** edit `docs/templates/` (pack-owned; overwritten on sync — [`docs/templates/README.md`](../README.md)).

**Route by ask** *(open only that playbook — do not scan the pack catalog)*:

| User ask | Open only |
|----------|-----------|
| bootstrap / init modular docs | **parent only** → `docs/templates/agent/BOOTSTRAP.md` (do **not** spawn a bootstrap subagent) |
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
- **Parent-only exception:** matching *orchestrate / drive backlog / …* → follow `docs/templates/agent/roles/orchestrator.md` **in this parent session** only (spawns leaf workers). Matching *bootstrap / init modular docs* → follow `docs/templates/agent/BOOTSTRAP.md` **in this parent session** only. Never install or spawn `orchestrator` or `docs-bootstrap` as harness subagent types — bootstrap **installs** the adapters, so a bootstrap adapter cannot exist until after the job it was meant to do.

| When ask matches | Agent filename | Fallback |
|------------------|----------------|----------|
| draft/revise Understanding, new idea, intent, identity correction, build/update from `docs/reference/` | `understanding-author.md` | `docs/templates/agent/roles/understanding-author.md` |
| user confirmed Understanding → update durable spec | `doc-graduate.md` | `docs/templates/agent/roles/doc-graduate.md` |
| implement / continue from Current focus | `feature-implementer.md` | session default below |
| orchestrate / drive backlog / clear TODOs / until blocked | *(parent only — do not spawn)* | `docs/templates/agent/roles/orchestrator.md` |
| bootstrap / init modular docs | *(parent only — do not spawn)* | `docs/templates/agent/BOOTSTRAP.md` |
| verify completed unit vs Understanding/spec/TODO | `work-verifier.md` | `docs/templates/agent/roles/work-verifier.md` |
| todo warden / reconcile TODOs / TODO honesty / gaps after orchestration / todo cleanup / archive completed | `todo-warden.md` | `docs/templates/agent/roles/todo-warden.md` |
| update / sync doc templates | `docs-template-sync.md` | `docs/templates/agent/TEMPLATE_SYNC.md` |

**Do not** delegate every message — only when a row above matches. Stay in this session for tiny follow-ups, clarifying questions only, or when the user says to stay here / skip subagents. Do **not** turn a single-slice Current focus ask into full orchestration unless the user said orchestrate / drive backlog / clear TODOs. **Successive issues / Grok parent:** do **not** spawn another coding agent + new PR if an open PR already touches this stem’s live docs (`*-TODO.md` / spec / Understanding) — add to that PR (Workflow §0.3). Code in different files does not make a second PR safe. These must not replace this rule or compete like always-on skill packs. Roles: `docs/templates/agent/roles/README.md`. Tool install paths: `docs/templates/agent/tools/README.md`.

**Docs profile** *(read `docs/ADT-settings.yaml` → `docs_profile.mode`; unset = **`prevent`** — Workflow §0.1)*:
| Mode | New map-row files | Coding gate |
|------|-------------------|-------------|
| **`prevent`** | Spec + Understanding (`draft`) + core TODO | No code while Understanding is `draft` (unless waived) |
| **`balanced`** | Spec + TODO; + Understanding when identity ambiguous / multi-surface / split / user asked | Draft gate only if that stem **has** Understanding |
| **`ship-first`** | Spec + core TODO | No Understanding gate; implement from TODO + thin spec. Right default for typed APIs / CRUD. |
If `docs_profile` is unset at bootstrap / first build-from-reference / sync: suggest once from `docs/reference/` (cite 2–3 snippets) → ask → record. Never silent-downgrade a project full of Understandings.

**Standing workflow** *(read `docs/ADT-settings.yaml` → `standing.instructions` when present — Workflow §0.2)*:
- Non-empty bullets = durable **ADT playbook overrides**. Apply after hard safety + this-turn user ask; before pack defaults.
- **LOOKOUT (every turn):** user wants to **override an ADT playbook** going forward (git/ceremony/orchestrate/verify/re-ask) → **same turn** set the first-class ADT-settings key if one fits, else **append** a short bullet under `standing.instructions` and say you saved it. Do not wait for wrap-up. **Do not jot random notes**, prompt-engineering, or other-product API style into standing.
- Product/UI prefs for one stem → spec **Decisions** (§10), not standing. One-off “just this run” → do not write standing. Never invent standing notes.

**Session default** *(implement / continue when ready under docs profile and scope unchanged)*:
0. **Docs freshness** *(once per session, before treating docs as current)*: if a git repo, run `git status --porcelain` and `git worktree list`. Clean + one worktree → continue. **Sibling worktree** with uncommitted `docs/` or `docs/` commits this HEAD lacks → **stop** — open `docs/templates/agent/workflow/session-freshness.md`. Dirty **this** tree: one line, continue (do not auto-commit). Re-check before merge/overwrite that touches live docs. **Before a new PR or successive spawn:** `gh pr list --state open` (or forge equivalent). Open PR already touches this stem’s TODO/spec/Understanding → **add to that PR**; do not open a second (docs overlap ≠ code overlap — Workflow §0.3).
1. Read `docs_profile` if present; read non-empty `standing.instructions`; read `docs/Master_Index.md` Sections 1–3.
2. Open the active TODO — read **Current focus** first (Workflow §5.1):
   - Shared foundation → `_shared/ComponentName-TODO.md`
   - Feature work → `features/FeatureName-TODO.md`
   - InEditor / Asset TODOs: only when Project Profile **Game extensions** / user indicates game-style work — default is **core TODO only**
3. Read that item’s `-Understanding.md` **if it exists** (context) and spec as linked — do not re-ask for review unless scope changes (Workflow §4).
4. Before integrating a **shared** piece, check its **Maturity** on the spec or Document Map (`draft` | `usable` | `stable`).
5. If the user asks to install tooling: follow **`docs/Tooling.md`** (Workflow §11).
6. If work needs a **human** (procure, playtest/feel, decide/sign-off, or external waiting): **dual-write** — owner `*-TODO.md` **and** an Open row on **`docs/Human-TODO.md`** (Workflow §13). Stamp only Active `role_id`s; do not invent roster rows. Never store secrets in docs.
7. If `docs/Product-Vision.md` is missing at bootstrap / first live-docs / sync → create a lightweight file (all profiles). **Confirmed** vision: do not implement a fighting feature (Workflow §4.5). Under **ship-first**, `draft` is **not a gate**.

**Open `Modular_Docs_Workflow.md` (index) only when:** creating files, choosing Path A vs Path B, graduating Understanding → spec, docs-profile or standing-capture questions, **docs freshness flagged** (sibling drift / stale `docs/` / docs-overlapping PR), the user asks about procedure, **or context is thin** (new session, compaction, memory loss). Then open **only the one module** the index router names. Live scaffolds are fill-in blanks. Do **not** load the whole `workflow/` folder or re-read the index every turn.

**Shared / files / shape** *(full procedure in the named module)*:
- **Do not invent `_shared/`.** Only when a project-owned piece is used by two or more features, or the user named it. Empty §3.1 is fine. Workflow §1 · §0.
- **Document Map = files on disk** the same turn (spec + core TODO; Understanding per §0.1). No map-only planned rows. Kit leftovers stay TODOs on an existing stem (§5.4).
- **`prevent`:** draft Understanding first; `draft` blocks coding. Lock obvious defaults; **Assumptions = real forks only**. Do not treat reference-doc examples as the target unless clearly set as the target. **`balanced`:** Understanding when identity is fuzzy. **`ship-first`:** no Understanding required.
- Do not code while an **existing** Understanding is `draft` unless waived. **`confirmed`** → continue from TODO/spec. Additive vs shape → Workflow §4. Vague ideas → `docs/templates/help/IDEA_CAPTURE_TIPS.md`. `docs/reference/` → live docs: understanding-author.

**While working:** Current focus first; rewrite focus that fights confirmed shape; user-facing stems need an exercise path (§5.3); in-scope spec leftovers need covering TODOs on an existing stem (§5.4).

**After changes (mandatory):**
- **Build & verify** on code changes before “you can test” (`docs/Tooling.md` Project verify — `Agent_Build_Verify_Rule`).
- Update **Current focus** + `-TODO.md` (`[x]` + date; **move** finished items into **Completed**). Human-TODO feedback → sync owner + Human-TODO Done (§13); never mark human rows from assumptions.
- Update Understanding/spec **only if this session** changed shape/contract. Preference corrections → same-turn Decisions + fix stale Behavior/Acceptance/Visual (§10). **ADT playbook overrides** → same-turn standing or first-class ADT-settings key (§0.2). Understanding update → relocate + TODO uncheck (§4). No session-start full reconcile.

**Clarification** (*review spec* / *gaps* / *confidence* for a **named** stem): re-read **that** stem only; ≤5 questions; wait for confirm; no unrelated stems.

**Philosophy:** Small accurate docs; short asks → one playbook; tight scope = paved path (not alternate audits). Pack playbook overrides stick via standing (§0.2) — not a notes pad. Not: human-sprint interim arch when shape is clear · library checklist = product done · ignore open operable Acceptance · finished-kit spec with no covering TODOs · wait-for-pickup instead of drain · let playbook overrides die with the chat · treat uncommitted sibling `docs/` as if this tree were current. TODO Current focus = agent memory; Human-TODO = human inbox.
