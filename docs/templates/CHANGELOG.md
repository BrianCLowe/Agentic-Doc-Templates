# Template pack changelog

> **Agents:** After [`agent/TEMPLATE_SYNC_A.md`](agent/TEMPLATE_SYNC_A.md), open [`agent/TEMPLATE_SYNC_B.md`](agent/TEMPLATE_SYNC_B.md). Select catch-up entries from **from** → **to** (B0 Catch-up) — not top-only on version jumps. **Union** Live impact tags; skim Step B lines for one-shots; do not invent a broader audit.
>
> **Maintainers:** Every `VERSION` bump must update this file in the same commit (newest entry on top). Keep bullets brief. When editing agent playbooks, write for thorough “off-road” models — explicit scope gates and Do-not lists, not open “as needed” language (see root [`CONTRIBUTING.md`](../../CONTRIBUTING.md)).

**Live impact tags** (use only these):

| Tag | Meaning for Step B |
|-----|--------------------|
| `versions-only` | Bump **Pack version** in live Master Index; stop |
| `master-index` | Adopt structural deltas in live `Master_Index.md` (headings, Key Locations, Document Map columns) |
| `content-templates` | Add *missing* sections/structure from content templates into live Understanding / Spec / TODO / Tooling / Human-TODO — **not** trim/remove (see `optional-live-reshape`) |
| `optional-live-reshape` | Live Understanding → shape trim + relocate into specs (Workflow §4). **`auto` / `auto-all`:** run all Document Map stems. **`choose`:** present + ask once (default yes). Do **not** silent-skip under choose |
| `optional-todo-ambition` | Live TODO ambition pass (agent timescale). **`auto` / `auto-all`:** all Document Map `*-TODO.md`. **`choose`:** present + ask once. Do not invent work |
| `optional-todo-operable` | Live TODO operable dual-track (Workflow §5.3). **`auto` / `auto-all`:** all Document Map `*-TODO.md`. **`choose`:** present + ask once. Add exercise-path rows or **library-only** labels; do not invent unrelated backlog |
| `optional-todo-kit-coverage` | Live TODO kit-coverage pass (Workflow §5.4). **`auto` / `auto-all`:** all Document Map `*-TODO.md`. **`choose`:** present + ask once. Add covering TODOs for spec-named in-scope leftovers on **existing** stems (**open or Completed** counts — do not resurrect); one research item if the spec is thin. No new map rows; no vendor-doc fetch in sync |
| `rules` | Refresh installed agent rules/adapters from local pack (**no ask** unless tool has `customized: true`) |
| `optional-upstream-check` | Stamp `upstream:` in `docs/ADT-settings.yaml` / offer enable update-check if unset |
| `process-docs-only` | Pack process/help/agent docs only — no live feature/shared content scan |

---

## 2.7.19

- **Live impact:** `versions-only`, `master-index`, `process-docs-only`, `rules`, `optional-todo-kit-coverage`
- **Files:**
  - `VERSION` — 2.7.18 → 2.7.19
  - `agent/roles/orchestrator-git.md` — new **`milestone-pr`** (recommend): one PR per verified slice → wait CI / Bugbot auto-fixes → **merge** → new branch for the next slice; keep **`branch-pr-squash`** as one-morning-PR / no merge. **Cloud Agent path** this-runs **`milestone-pr`** when durable is `local` / `none` / `branch-push` / `current-push` / `branch-pr` / `branch-pr-squash` / unset (do **not** rewrite ADT-settings; explicit this-run user order wins). Cloud this-run **stays** on the platform workspace branch (no degrade to squash). **Degrade** skips return-to-default / next branch. CI timeout / pending → degrade (do not merge). Comment-only Bugbot fixes re-wait CI
  - `agent/roles/orchestrator.md` — loop runs the milestone PR cycle before the next unit; **serial implementers** under `milestone-pr`; merge grant only for `milestone-pr`; **§5.4 kit coverage** — add covering TODOs on existing stems, do not skip inventory Medium as “not picked up”
  - `agent/workflow/naming-layout.md` — **inventory vs new map rows**; **no map rows for vague planned-only**; terse wrap-the-public-API is **actionable** (not a stub)
  - `agent/workflow/todos.md` — **§5.4** finished-kit spec ⇒ covering TODOs; pickup ≠ backlog; filling in-scope items is not inventing work; **diff vendor docs vs code** without facet-by-facet hand-holding
  - `agent/workflow/understanding.md` §2, `Agent_Timescale_Planning_Rule.mdc` / `.instructions.md`, modular rule, spec/TODO templates, doc-graduate / understanding-author — pointers
  - `agent/roles/todo-warden.md`, `roles/README.md` — per-slice vs end-of-run close-out; named leftovers get covering TODOs (open or Completed); thin wrap-the-API research only if this run claimed kit-complete; no vendor fetch
  - `agent/roles/template-sync.md` + `adapter-src/bodies/docs-template-sync.md` + `todo-warden.md` — honor **`optional-todo-kit-coverage`**; covering includes Completed
  - `agent/roles/cursor/*`, `agent/roles/grok/*` — regenerated adapters
  - `agent/BOOTSTRAP.md` Step 3p **E**, `agent/TEMPLATE_SYNC_B.md` B0.6 — recommend **`milestone-pr`**; menu + cloud note; B adds **`optional-todo-kit-coverage`** live pass (spec-named leftovers → TODOs on this stem; Completed counts; thin wrap-the-API spec → one research TODO; no vendor fetch)
  - `help/USAGE.md` — sync kit-coverage vs warden split
  - `agent/ADT-settings.example.yaml` — example mode **`milestone-pr`**
  - `Master_Index_Template.md`, `help/*`, root `README.md` — recommend + cloud path + inventory/TODO wording
- **Step B:** Bump Master Index **Pack version** to 2.7.19. Adopt At a Glance **orchestrator git** recommend **`milestone-pr`** + Cloud Agent this-run note if missing; adopt **inventory stem** / covering-TODOs wording on At a Glance idea-sources if missing. **Do not** migrate existing live `orchestrator.git.mode` (including `local` / `branch-pr` / `branch-pr-squash`) — cloud overrides are this-run only. **Update and refresh** installed modular + timescale rules from this pack (**no ask** unless `customized: true`). **`optional-todo-kit-coverage`:** present/execute per `sync.mode` — for each Document Map stem, if the **spec already names** in-scope leftover surfaces with no covering TODO (**open or Completed** on **this** stem), add items on that stem (no new map rows; do not resurrect Completed). If Overview claims wrap-the-vendor-API but the spec lists no leftovers, add **one** research TODO (diff vendor docs next session) — do **not** fetch vendor APIs during sync. Under **`choose`:** ask once (default all stems). Under **`auto` / `auto-all`:** all Document Map `*-TODO.md`. Todo-warden does not replace this pass. Orchestrator playbooks are parent-only (no adapter).

## 2.7.18

- **Live impact:** `versions-only`, `master-index`, `process-docs-only`
- **Files:**
  - `VERSION` — 2.7.17 → 2.7.18
  - `agent/roles/orchestrator-git.md` — **Cloud Agent path**: remote Cloud Agents this-run **`branch-pr-squash`** when durable mode is `local` / `none` / `branch-push` / `current-push` / `branch-pr` / unset (do **not** rewrite ADT-settings; explicit this-run user order wins); when unset on local IDE, **recommend `branch-pr-squash`**
  - `agent/roles/orchestrator.md` — pre-run git resolves via Cloud Agent path when applicable
  - `agent/BOOTSTRAP.md` Step 3p **E**, `agent/TEMPLATE_SYNC_B.md` B0.6 — recommend flip + cloud note; menu order leads with squash
  - `agent/ADT-settings.example.yaml` — example mode **`branch-pr-squash`** + cloud this-run comment
  - `Master_Index_Template.md`, `help/*`, root `README.md` — recommend + cloud path wording
- **Step B:** Bump Master Index **Pack version** to 2.7.18. Adopt At a Glance **orchestrator git** recommend **`branch-pr-squash`** + Cloud Agent this-run note if missing. **Do not** migrate existing live `orchestrator.git.mode` (including `local` / `branch-pr`) — cloud overrides are this-run only. No live feature/shared scan. Rules refresh not required (orchestrator is parent playbook only).

## 2.7.17

- **Live impact:** `versions-only`, `rules`, `process-docs-only`
- **Files:**
  - `VERSION` — 2.7.16 → 2.7.17
  - `agent/GENERATE_ROLE_ADAPTERS.md` — **markdown playbook** to regenerate cursor/grok adapters from `roles/adapter-src/` (**no Python** in the pack)
  - Root `scripts/gen_role_adapters.py` — upstream CI helper only (not in the release zip); bootstrap deletes it on whole-repo copies
  - `agent/BOOTSTRAP.md` — **Step 1d**: on whole-repo / “Use this template” installs, delete upstream root `eval/`, root `scripts/gen_role_adapters.py`, leftover `docs/templates/agent/scripts/*.py`, and `.github/workflows/pack-checks.yml`; keep `GENERATE_ROLE_ADAPTERS.md` + `adapter-src/`
  - `help/SETUP.md`, `CONTRIBUTING.md`, `roles/` / adapter-src stamps
- **Step B:** Bump Master Index **Pack version** to 2.7.17. If the project still has root `eval/` / root `scripts/gen_role_adapters.py` / `docs/templates/agent/scripts/*.py` / `.github/workflows/pack-checks.yml` from a whole-repo copy → delete them (bootstrap Step 1d gates). Refresh modular rules only if already installed (**no ask** unless `customized: true`). No live feature/shared content invent.

## 2.7.16

- **Live impact:** `versions-only`, `master-index`, `rules`, `content-templates`, `process-docs-only`
- **Files:**
  - `VERSION` — 2.7.15 → 2.7.16
  - `agent/roles/adapter-src/` — **single source** for cursor/grok adapters (`manifest.json` + `bodies/`); regenerate with `python3 scripts/gen_role_adapters.py`
  - `scripts/gen_role_adapters.py` — generate or `--check` drift (CI)
  - `agent/roles/cursor/*`, `agent/roles/grok/*` — regenerated; do not hand-edit
  - De-confirm / additive-vs-shape — **pointer-only** in roles, adapters, `Feature_Understanding_Template.md`; full gate remains only in `agent/workflow/understanding.md` §4
  - `eval/` — behavioral golden cases + `run_eval.py` (pack integrity always; prepare/verify for agent turns). Not in the release zip
  - `.github/workflows/pack-checks.yml` — adapter `--check` + `eval/run_eval.py` on PR/push
  - `roles/README.md`, `CONTRIBUTING.md`, stamps
- **Step B:** Bump Master Index **Pack version** to 2.7.16. If `optional_rules.doc-roles` **enabled** → refresh **all** role adapters from this pack (generated). Refresh modular rules (**no ask** unless `customized: true`). No live feature/shared content invent.

## 2.7.15

- **Live impact:** `versions-only`, `master-index`, `rules`, `content-templates`, `process-docs-only`
- **Files:**
  - `VERSION` — 2.7.14 → 2.7.15
  - `agent/Modular_Docs_Workflow.md` — **index + paved path + router** (no longer a 600-line monolith). Agents load the short path first; open **one** module when needed
  - `agent/workflow/` — new modules: `profile-standing`, `naming-layout`, `shared-components`, `understanding` (source of truth for shape/graduation/**de-confirm gate**), `implement`, `todos`, `decisions`, `tooling`, `human-todo`, `extensions` + `README.md`
  - Index keeps **compatibility anchors** so older Master Index / help deep links still resolve, then point into modules
  - Roles (`understanding-author`, `feature-implementer`, `doc-graduate`, `work-verifier`, `todo-warden`) + modular rules + content/help templates — point at specific modules, not the whole workflow
  - `Master_Index_Template.md`, `BOOTSTRAP.md`, root README stamp
- **Step B:** Bump Master Index **Pack version** to 2.7.15. Adopt Key Locations wording for workflow index + `workflow/` if missing. Refresh installed modular rules (**no ask** unless `customized: true`). If `optional_rules.doc-roles` **enabled** → refresh role adapters that point at Workflow. No live feature/shared content invent (structural playbook split only).

## 2.7.14

- **Live impact:** `versions-only`, `rules`, `content-templates`, `process-docs-only`
- **Files:**
  - `VERSION` — 2.7.13 → 2.7.14
  - `agent/BOOTSTRAP.md` — new **Step 1c**: on whole-repo copies, delete the pack's own `.cursor/environment.json` (Cloud Agent env config that only verifies the release-build toolchain) so it does not pollute user project repos; keep the user's own `.cursor/` config. Do-not list updated.
  - `agent/Modular_Docs_Workflow.md` §4 — new **de-confirm gate**: a `confirmed` Understanding flips to `draft` / `superseded` **only** on a significant shape change (is / is not / guardrail / product surface); an **additive** request (new research angle / extra detail that fits the shape) → **spec + TODO**, keep `confirmed`. Routing bullet clarified.
  - `agent/roles/understanding-author.md` + cursor|grok adapters — do not de-confirm / re-draft for additive asks; invoke only on a significant shape change
  - `agent/roles/feature-implementer.md` + cursor|grok adapters — additive request that fits confirmed is / is not is **not** a scope change: add to spec + TODO, keep `confirmed`, continue; only shape change stops
  - `Feature_Understanding_Template.md` — AI-instructions de-confirm gate note
- **Step B:** Bump Master Index **Pack version** to 2.7.14. If `optional_rules.doc-roles` **enabled** → refresh **understanding-author** + **feature-implementer** adapters. Refresh modular rules (**no ask** unless `customized: true`). No live feature/shared content invent (de-confirm gate is guidance for future edits, not a live-doc reshape).

## 2.7.13

- **Live impact:** `versions-only`, `rules`, `content-templates`, `process-docs-only`
- **Files:**
  - `VERSION` — 2.7.12 → 2.7.13
  - `agent/roles/todo-warden.md` + cursor|grok adapters — **hygiene/cleanup**: move true `[x]` from High/Medium/Low into **Completed** (uncapped); honesty+hygiene default; *todo cleanup* = hygiene-only; hygiene never forces `gaps-found`; no auto `-todo-complete.md`
  - `agent/roles/orchestrator-git.md` — close-out warden brief includes hygiene
  - `agent/roles/feature-implementer.md` + adapters — finish → move items to Completed
  - `agent/Modular_Docs_Workflow.md` §5, modular rules — mark done **and move** to Completed
  - `TODO_Template.md` — heading is plain **`## Completed`** (dropped Archive / `-todo-complete.md` parenthetical)
  - `roles/README.md`, `help/USAGE.md`, stamps
- **Step B:** Bump Master Index **Pack version** to 2.7.13. If `optional_rules.doc-roles` **enabled** → refresh **todo-warden** (+ feature-implementer) adapters. Refresh modular rules (**no ask** unless `customized: true`). Do **not** auto-run warden on all live TODOs. No live feature/shared content invent.

## 2.7.12

- **Live impact:** `versions-only`, `master-index`, `rules`, `process-docs-only`
- **Files:**
  - `VERSION` — 2.7.11 → 2.7.12
  - `agent/ADT-settings.example.yaml` — **`standing.instructions`** freeform durable process prefs (survives sync)
  - `agent/Modular_Docs_Workflow.md` — **§0.2** standing instructions: precedence, **LOOKOUT** same-turn capture when user opposes pack defaults, Decisions cross-ref
  - `agent/Modular_Documentation_Rule.mdc` / `.instructions.md` — always-on standing read + lookout; after-changes capture
  - `agent/BOOTSTRAP.md` — optional post-3p standing line (not a mandatory quiz)
  - `agent/roles/orchestrator.md`, `feature-implementer.md` — read standing; capture process prefs mid-run
  - `Master_Index_Template.md`, `help/USING_WITH_AGENTS.md`, `help/USAGE.md`, root README — stamps / expectations
- **Step B:** Bump Master Index **Pack version** to 2.7.12. Adopt Key Locations wording for `standing.instructions` if present. Refresh installed modular rules (**no ask** unless `customized: true`). Do **not** invent standing content on consumer projects. No live feature/shared content scan.

## 2.7.11

- **Live impact:** `versions-only`, `process-docs-only`
- **Files:**
  - `VERSION` — 2.7.10 → 2.7.11
  - `agent/roles/orchestrator-git.md` — **return to default branch** after run when this orchestration **created** `orchestrate/…` (not pre-existing feature branches); report final HEAD; skip if dirty / user said stay
  - `agent/roles/orchestrator.md`, `roles/README.md` — end report includes current branch after return
  - stamps: Master Index / Workflow / ADT-settings example / root README
- **Step B:** Bump Master Index **Pack version** to 2.7.11. No live feature/shared scan. Rules refresh not required (orchestrator playbooks only).

## 2.7.10

- **Live impact:** `versions-only`, `rules`, `process-docs-only`
- **Files:**
  - `VERSION` — 2.7.9 → 2.7.10
  - `agent/roles/todo-warden.md` + cursor|grok adapters — **docs-only** honesty pass: reopen overclaims, ≤5 cited gap TODOs, ≤10 reopens; no code; no invention
  - `agent/roles/orchestrator-git.md` — **extracted** git modes, forge probe, PR close-out (build-verify → warden → squash → ready); `orchestrator.md` slimmed to loop + gates + human verify map
  - `agent/Modular_Docs_Workflow.md` — tighter design intent + **§5.3** (table form; same guardrails)
  - `agent/Modular_Documentation_Rule.*` — shorter operable/after-changes/philosophy; still points at Workflow/rules
  - `agent/roles/orchestrator.md` — close-out via git companion; **gaps-found** keeps PR draft
  - `roles/README.md`, `tools/cursor|grok|claude-code.md`, `BOOTSTRAP` / `TEMPLATE_SYNC_B` forge pointers, `help/USAGE.md`, stamps
- **Step B:** Bump Master Index **Pack version** to 2.7.10. If `optional_rules.doc-roles` **enabled** → refresh adapters including new **`todo-warden`**. Refresh modular rules (**no ask** unless `customized: true`). No live feature/shared content scan.

## 2.7.9

- **Live impact:** `versions-only`, `master-index`, `process-docs-only`
- **Files:**
  - `VERSION` — 2.7.8 → 2.7.9
  - `agent/roles/orchestrator.md` — **`branch-pr-squash`**; PR close-out **strict order**: final push → **build verify** → squash (squash mode only) → **mark ready** (default); draft mid-run; force-with-lease only for squash
  - `agent/ADT-settings.example.yaml`, `BOOTSTRAP.md` Step 3p **E**, `TEMPLATE_SYNC_B.md` **B0.6**, `Master_Index_Template.md` — new mode + close-out wording
  - stamps: Workflow / ADT-settings example / root README
- **Step B:** Bump Master Index **Pack version** to 2.7.9. Adopt At a Glance **orchestrator git** wording (`branch-pr-squash`, build-verify then ready). Existing `branch-pr` users keep mode (behavior now includes ready-at-end + pre-ready build verify — no mode migration). Do **not** invent `branch-pr-squash` without user choice. No live feature/shared scan. Rules refresh not required (orchestrator is parent playbook only).

## 2.7.8

- **Live impact:** `versions-only`, `rules`, `content-templates`, `optional-todo-operable`, `process-docs-only`
- **Files:**
  - `VERSION` — 2.7.7 → 2.7.8
  - `agent/Modular_Docs_Workflow.md` — **§5.3 Operable done**: exercise path vs library-only; **layer desync**; **phased bridge**; **Acceptance bridge**; **No UI specs ≠ defer** (scaffold + wire minimal boring surface); §11 Project verify handoff pointer
  - `agent/Agent_Build_Verify_Rule.mdc` + `.instructions.md` — **core** always-on: discover project verify (Tooling → scripts → Docker → engine → CI); run → fix → re-run before “you can test”
  - `Tooling_Template.md` — **Project verify (agent handoff)** table (apps, compose, UE, etc.)
  - `agent/tools/*` — install/refresh build-verify with modular + timescale
  - `TODO_Template.md`, `Feature_Spec_Template.md` — dual-track / phase note; Acceptance bridge guidance
  - `agent/roles/feature-implementer.md`, `work-verifier.md`, `understanding-author.md`, `doc-graduate.md`, `orchestrator.md` + cursor|grok adapters — operable gap, scaffold+wire, build-verify before handoff, Acceptance update, graduate TODO bridge, survey rewrite
  - `agent/Agent_Timescale_Planning_Rule.*`, `Modular_Documentation_Rule.*` — operable ≠ library-only; no-UI-specs default; post-change build-verify
  - `agent/TEMPLATE_SYNC_B.md` — **`optional-todo-operable`** live pass + rules refresh includes build-verify
  - stamps: Master Index template / Workflow / ADT-settings example / root README
- **Step B:** Bump Master Index **Pack version** to 2.7.8. **content-templates:** add *missing* TODO/spec/**Tooling Project verify** structure only. **`optional-todo-operable`:** present/execute per `sync.mode` — for user-facing stems missing exercise path, add UI/CLI/smoke TODO rows (**scaffold + wire** if UI never specified) **or** phased bridge only when intentional; if open operable Acceptance has no covering TODO, add work (or phase); label pure foundation **library-only**; do not invent “await UI design” or unrelated work or twin every Acceptance line. Under **`choose`:** ask once (default all stems). Under **`auto` / `auto-all`:** all Document Map `*-TODO.md`. **Update and refresh** installed modular + timescale + **build-verify** rules **and** doc-role adapters (**no ask** unless `customized: true`). Fill live `Tooling.md` Project verify when empty and stack is known. No Understanding reshape.

## 2.7.7

- **Live impact:** `versions-only`, `master-index`, `rules`, `process-docs-only`
- **Files:**
  - `VERSION` — 2.7.6 → 2.7.7
  - `agent/ADT-settings.example.yaml` — **`docs_profile.mode`**: `prevent` \| `balanced` \| `ship-first`; **`orchestrator.git.mode`**: `local` \| `branch-pr` \| `branch-push` \| `current-push` \| `none`
  - `agent/Modular_Docs_Workflow.md` — **§0.1 Docs profile** (plain-language options); §0/§1/§2/§3/§4 branch on profile; Spec+TODO core
  - `agent/Modular_Documentation_Rule.*` — docs_profile table + ready gates
  - `agent/BOOTSTRAP.md` — **Step 3p one-batch** project preferences (profile, update-check, doc-roles, sync, orchestrator git); 3d uses profile
  - `agent/TEMPLATE_SYNC_B.md` — **B0.5** docs_profile; **B0.6** orchestrator git **always ask if unset** (including `auto-all`; never invent `current-push` / silent-write)
  - `agent/roles/orchestrator.md` — Git policy; **forge tooling probe** (infer CLI from remote; ask to install if missing; **ask to start auth** if not logged in — install ≠ PR-ready); readiness by docs_profile
  - `agent/roles/work-verifier.md` + Grok adapter — plan-mode: prefer read tools if shell blocked
  - `agent/roles/*`, cursor|grok adapters — profile + git wiring; Grok work-verifier `permission_mode: plan`
  - `agent/tools/grok-build.md` — subagents on by default; Claude vs Cursor compat
  - `agent/Agent_Timescale_Planning_Rule.*` — identity on Understanding or spec under ship-first
  - `Master_Index_Template.md`, `help/*`, root README — prevent default + ship-first + batch prefs + orchestrator git
  - stamps: Master Index / Workflow / ADT-settings example / root README
- **Step B:** Bump Master Index **Pack version** to 2.7.7. Adopt At a Glance / Key Locations **docs profile** + **orchestrator git** wording. If `docs_profile.mode` unset → **B0.5** (`auto-all` → `prevent`). If `orchestrator.git.mode` unset → **B0.6 always ask** (even under `auto-all`). **Update and refresh** installed modular + timescale rules **and** doc-role adapters from this pack (**no ask** unless `customized: true`); if Grok doc-roles enabled include `work-verifier` (`permission_mode: plan` + read-tool fallback). Do **not** delete existing Understandings. No live feature/shared content scan beyond rules/index stamps.

## 2.7.6

- **Live impact:** `versions-only`, `master-index`, `rules`, `content-templates`, `optional-live-reshape`, `optional-todo-ambition`
- **Files:**
  - `VERSION` — 2.7.5 → 2.7.6
  - `agent/TEMPLATE_SYNC_B.md` — **Catch-up:** on version jumps, union Live impact tags from all `##` entries with **from** < version ≤ **to** (not top-only); `process-docs-only` on a newer entry does not cancel live passes from skipped releases; bump Pack version once to **to**. **`sync.mode: auto-all`** — same as `auto` plus enable + install unset `optional_rules.*` (never re-enable `declined`; new update-check defaults `check_mode: always`)
  - `agent/ADT-settings.example.yaml`, `BOOTSTRAP.md` Step 4d, `RULE_INSTALL.md`, `TEMPLATE_SYNC_A.md`, help USAGE / USING_WITH_AGENTS — `auto-all` documented
  - `agent/roles/template-sync.md` + cursor/grok adapters — catch-up union + `auto-all`
  - `help/IDEA_CAPTURE_TIPS.md`, `help/USAGE.md` — AI Exporter tip: timestamps so agents can order which decisions are newer across different conversation exports
  - root `README.md`, `help/SETUP.md`, `help/USAGE.md`, `help/USING_WITH_AGENTS.md`, Workflow, tools — **pause chat-ui attach-AGENT.md path**; recommend export → `docs/reference/` instead; remove `chat-ui/AGENT.md`
  - `chat-ui/README.md` — stub pointing at export habit (former AGENT.md instructions removed until fixed)
  - root `README.md`, `help/SETUP.md` — Get started: acquisition methods (download / copy / template / clone-rename-remote) then bootstrap → build from reference → sync; not “download then sync” as first install
  - `CHANGELOG.md` — agent header catch-up language; this entry
  - stamps: Master Index / Workflow / ADT-settings example / root README
- **Step B:** Bump Master Index **Pack version** to 2.7.6. Refresh installed modular rules / template-sync adapters (sync catch-up playbook; include timescale if missing). **Missed-pass recovery** *(projects that jumped while sync was top-entry-only may lack expected shapes):* (1) `master-index` — adopt missing Key Locations / Document Map columns / At a Glance deltas (Catalog column, `ADT-settings.yaml` row, chat-export tip, etc.). (2) `content-templates` — add *missing* Understanding / Spec / TODO / Tooling / Human-TODO structure only (not trim). (3) **`optional-live-reshape`:** Workflow §4 shape — present/execute per `sync.mode` (same as 2.6.8); decline if already reshaped. (4) **`optional-todo-ambition`:** present/execute per `sync.mode` (same as 2.7.1); decline if already done. Under **`choose`:** ask once per optional pass. Under **`auto` / `auto-all`:** run all Document Map stems for tagged passes (mostly idempotent). If `sync.mode` unset → offer `auto` / `auto-all` / `choose` (B0.2). Under **`auto-all`:** also enable + install any unset pack optionals. Do not invent work beyond these tags.

## 2.7.5

- **Live impact:** `versions-only`, `process-docs-only`
- **Files:**
  - `VERSION` — 2.7.4 → 2.7.5
  - `agent/roles/orchestrator.md` — end-of-run **guided look-list** (surfaces / placement / copy / happy path) dual-written as Human-TODO `playtest` + owner bullets; product judgment vs work-verifier; dedup
  - `agent/roles/README.md` — orchestrator stop line updated
  - `help/USAGE.md` — orchestrate ask notes end-of-run verify map
  - `Human_TODO_Template.md` — `playtest` tip for post-orchestration look-list
  - stamps: Master Index / Workflow / chat-ui / ADT-settings example / root README
- **Step B:** Bump Master Index **Pack version** to 2.7.5. Refresh Human-TODO template tip if live file still carries the kinds table from pack. No live feature/shared content scan. No rules refresh required (orchestrator is parent playbook only).

## 2.7.4

- **Live impact:** `versions-only`, `rules`, `process-docs-only`
- **Files:**
  - `VERSION` — 2.7.3 → 2.7.4
  - `agent/TEMPLATE_SYNC_A.md` — **A0 preflight:** dirty working tree → hard stop; ask user to commit **their** WIP (no auto-commit); explicit waive required to proceed dirty
  - `agent/TEMPLATE_SYNC_B.md` — **`sync.mode: auto`** includes post-sync hygiene commits; **B0.4** ask once for update-check cadence (`always` vs `interval`) when `check_mode_recorded` missing; no silent interval migrate
  - `agent/TEMPLATE_SYNC.md`, `roles/template-sync.md` + cursor/grok adapters, `BOOTSTRAP.md` Step 4b/4d, `ADT-settings.example.yaml`, `TEMPLATE_UPDATE_CHECK.md`, `RULE_INSTALL.md` — same policy
- **Step B:** Bump Master Index **Pack version** to 2.7.4. If update-check is enabled and `upstream.check_mode_recorded` is missing → ask cadence once (B0.4). Refresh installed modular rules / template-sync adapters if the user wants. No live feature/shared content scan.

## 2.7.3

- **Live impact:** `versions-only`, `master-index`, `rules`, `process-docs-only`
- **Files:**
  - `VERSION` — 2.7.2 → 2.7.3
  - `help/IDEA_CAPTURE_TIPS.md`, `help/USAGE.md`, `help/SETUP.md` — **recommended practice:** export idea chats to markdown in `docs/reference/`; simple ask *build or update live docs from reference* (split is agent duty, not in the ask); optional [AI Exporter](https://saveai.net/) tip
  - `agent/BOOTSTRAP.md` — richer `docs/reference/README.md` scaffold text
  - `agent/Modular_Docs_Workflow.md` §0/§4 — one identity per stem; split/move when unlike features were merged; reference → build/update
  - `agent/roles/understanding-author.md` + cursor/grok adapters; modular rule — build/update from reference; do not glue unlike identities
  - `Master_Index_Template.md`, `chat-ui/README.md`, root `README.md` — recommendation surfaced
- **Step B:** Bump Master Index **Pack version** to 2.7.3. Adopt Key Locations / At a Glance wording for chat-export recommendation if missing. Refresh installed modular rules if the user wants (routing + split guidance). No live feature/shared content scan.

## 2.7.2

- **Live impact:** `versions-only`, `master-index`, `rules`, `process-docs-only`
- **Files:**
  - `VERSION` — 2.7.1 → 2.7.2; **single `pack-version`** (drops dual template/workflow fields)
  - `agent/ADT-settings.example.yaml` — **new** unified live settings (`sync.mode`, tools, optional_rules, upstream); replaces `rule-install-status.example.yaml` + `upstream-status.example.yaml` (removed); upstream **`check_mode: always`** default (interval optional)
  - `agent/TEMPLATE_SYNC_B.md` — migrate legacy status files → `docs/ADT-settings.yaml`; **`sync.mode: auto|choose`**; auto runs reshape/ambition when tagged; rules refresh without ask unless `customized: true`; Pack version stamp; legacy weekly → `check_mode: interval`
  - `agent/BOOTSTRAP.md` — Steps 4b/4c write ADT-settings; **Step 4d** sync mode ask; 4b offers always vs interval; layout tree uses `ADT-settings.yaml`
  - `agent/RULE_INSTALL.md`, `TEMPLATE_UPDATE_CHECK.md`, `Template_Update_Check_Rule.*`, `TEMPLATE_SYNC_A.md`, `tools/*` — ADT-settings paths; pack-version compare; always-check default
  - `agent/roles/orchestrator.md` — **new** parent-only backlog loop (verify always; milestone commits; playtest liberal / batch at end)
  - `agent/roles/work-verifier.md` + `roles/cursor|grok/work-verifier.md` — **new** leaf verify role
  - `agent/roles/template-sync.md` + cursor/grok adapters — sync.mode + no-ask rules refresh
  - `agent/roles/README.md` — orchestrator + work-verifier; never install orchestrator adapter
  - `agent/Modular_Documentation_Rule.mdc` / `.instructions.md` — orchestrate / verify routes
  - `agent/Modular_Docs_Workflow.md`, `Master_Index_Template.md`, `chat-ui/AGENT.md`, `help/*`, root `README.md` — Pack version + ADT-settings Key Locations
- **Step B:** Migrate `rule-install-status.yaml` / `upstream-status.yaml` → `docs/ADT-settings.yaml` if needed (B0.1). If `sync.mode` unset → ask once (B0.2 / bootstrap 4d). Set live Master Index **Pack version** to 2.7.2 (replace Template/Workflow version lines). Adopt Key Locations row for `ADT-settings.yaml`. Refresh installed rules/adapters **without asking** (unless `customized: true`); if doc-roles enabled include `work-verifier` (six adapters; no `orchestrator`). No live feature/shared content scan unless other tags appear in a future top entry.

## 2.7.1

- **Live impact:** `versions-only`, `rules`, `content-templates`, `optional-todo-ambition`, `process-docs-only`
- **Files:**
  - `VERSION` — 2.7.0 → 2.7.1
  - `agent/Agent_Timescale_Planning_Rule.mdc` / `.instructions.md` — **new** core always-on rule: target architecture at agent speed; lock shape early; exploration vs shipping; user should not need to remind
  - `agent/tools/*` — install timescale rule with modular rule (all harnesses)
  - `agent/Modular_Docs_Workflow.md` — §4 surface-in-shape; §5 High Priority + **§5.2 Exploration vs shipping**; version 2.7.1
  - `agent/Modular_Documentation_Rule.mdc` / `.instructions.md` — Philosophy + Before implementation: shape surface, agent-speed plans, rewrite fighting focus
  - `Feature_Understanding_Template.md`, `Feature_Spec_Template.md`, `TODO_Template.md`, `help/IDEA_CAPTURE_TIPS.md` — product-defining surface in shape; module/API on spec; exploration labeling
  - `agent/roles/understanding-author.md` + `feature-implementer.md` + cursor/grok adapters — target shape / no user reminder
  - `agent/TEMPLATE_SYNC_B.md`, `agent/roles/template-sync.md` + cursor/grok adapters — Live impact tag `optional-todo-ambition`
  - `CHANGELOG.md` — tag table + this entry
  - `help/USING_WITH_AGENTS.md`, `Master_Index_Template.md`, `agent/upstream-status.example.yaml`, `chat-ui/AGENT.md`, root `README.md` — stamps / notes
- **Step B:** Bump Master Index versions to 2.7.1. Refresh installed rules (modular **and** new `agent-timescale-planning`) if the user wants. `content-templates`: add any *missing* Understanding/TODO/spec structure only (do not treat as reshape). **`optional-todo-ambition` (required ask — optional pass):** Explain that High Priority / Current focus may still stage human-sprint n-step interim architectures that fight confirmed shape. **Offer** a live TODO ambition pass (default choice: all Document Map `*-TODO.md` stems; or named stems / no). **Yes** = open chosen TODOs (+ Understanding for shape); merge interim staging into target-architecture High Priority; keep genuine verify slices / human/shared blockers; refresh Current focus; do **not** invent work. **No/later** = leave bodies; new TODOs still follow agent-timescale instructions. Do **not** silent-skip the ask. Suggest committing pack sync (+ rules) first so TODO rewrites can be a separate commit (ask — do not auto-commit).

## 2.7.0

- **Live impact:** `versions-only`, `master-index`, `content-templates`, `rules`, `process-docs-only`
- **Files:**
  - `VERSION` — 2.6.9 → 2.7.0
  - `Feature_Catalog_Template.md` — **new** optional sibling for list-heavy stems (readiness column)
  - `agent/Modular_Docs_Workflow.md` — §0 Catalog paths; **§7.1 Catalog companions**; version 2.7.0
  - `Feature_Spec_Template.md` — optional Catalog pointer section; do not dump registries into Behavior
  - `Master_Index_Template.md` — Document Map **Catalog** column; file-layout At a Glance note
  - `agent/Modular_Documentation_Rule.mdc` / `.instructions.md` — Catalog on map = file same turn; no row dumps in Understanding
  - `agent/upstream-status.example.yaml`, `chat-ui/AGENT.md`, root `README.md` — version stamps
- **Step B:** Bump Master Index versions to 2.7.0. Adopt Catalog column on Document Map where useful (use `—` when no catalog). Refresh installed modular rules if the user wants. Do **not** invent Catalogs for every stem — only list-heavy / game registry pressure (Workflow §7.1). New `Feature_Catalog_Template.md` available for scaffolds.

## 2.6.9

- **Live impact:** `versions-only`, `rules`, `process-docs-only`
- **Files:**
  - `VERSION` — 2.6.8 → 2.6.9
  - `agent/Modular_Docs_Workflow.md` — §3 minimal path + §10: same-turn **Decisions** capture for implement/polish preference corrections; threshold + skip rules; version 2.6.9
  - `agent/Modular_Documentation_Rule.mdc` / `.instructions.md` — After changes: preference corrections → Decisions (+ stale Behavior/Acceptance/Visual) same turn; no session-wrap dependency
  - `agent/roles/feature-implementer.md` + `roles/cursor|grok/feature-implementer.md` — preference corrections are contract; Do-not defer to bedtime wrap
  - `Feature_Spec_Template.md`, `Decision_Template.md`, `TODO_Template.md` — Decisions vs Current focus guidance
  - `help/IDEA_CAPTURE_TIPS.md`, `help/USING_WITH_AGENTS.md` — same-turn capture note
  - `Master_Index_Template.md`, `agent/upstream-status.example.yaml`, `chat-ui/AGENT.md`, root `README.md` — version stamps
- **Step B:** Bump Master Index versions to 2.6.9. Refresh installed modular rules if the user wants (bodies changed). Do **not** auto-backfill Decisions rows for past polish sessions. Spec/TODO instruction tweaks apply going forward and when that stem is next edited.

## 2.6.8

- **Live impact:** `versions-only`, `rules`, `content-templates`, `optional-live-reshape`, `process-docs-only`
- **Files:**
  - `VERSION` — 2.6.7 → 2.6.8
  - `CHANGELOG.md` — new Live impact tag `optional-live-reshape` (highly recommended; suggest separate commit); `content-templates` clarified (add missing only)
  - `agent/TEMPLATE_SYNC.md` — thin entry (A then B); **`TEMPLATE_SYNC_A.md`** / **`TEMPLATE_SYNC_B.md`** split so Step B is not loaded before pack overwrite
  - `agent/roles/template-sync.md`, `roles/cursor|grok/docs-template-sync.md` — A-then-B; reshape ask; commit-pack-first suggestion
  - `Master_Index_Template.md`, `agent/upstream-status.example.yaml`, `chat-ui/AGENT.md`, root `README.md` — version stamps
- **Step B:** After pack refresh, open local **`agent/TEMPLATE_SYNC_B.md`** from disk (not a pre-overwrite sync playbook). Bump Master Index versions to 2.6.8. Refresh installed modular rules if the user wants. `content-templates`: add any *missing* structure only (do not treat as reshape). **`optional-live-reshape` (required ask — highly recommended):** Explain that leaving pre-shape Understanding sections (How-it-should-work, Done when, UI/Visuals, long contract prose) drifts from the workflow and causes agent inefficiency / wrong reviews. **Recommend yes** (default: all Document Map stems; or named stems / no). **Yes** = trim + **relocate** into that stem’s spec (Workflow §4) — not add headings only. Do **not** silent-skip or bury as “skipped by design.” **Commit hygiene:** after pack refresh + version/rules stamps, **suggest** the user commit that sync first (ask them — do not auto-commit) so live Understanding/spec reshape can be a **separate** follow-up commit. On **no/later**: do not rewrite bodies; note the drift risk briefly. On **yes**: for each chosen stem, remove non-shape sections after relocate; refresh banner + Instructions from the Understanding template; spec anti-compression for relocated content. Do not invent contract detail.

## 2.6.7

- **Live impact:** `versions-only`, `rules`, `content-templates`, `process-docs-only`
- **Files:**
  - `VERSION` — 2.6.6 → 2.6.7
  - `agent/Modular_Docs_Workflow.md` — §2 / §4 as **source of truth** for shape vs contract; tightened overlapping prose; version 2.6.7
  - `agent/Modular_Documentation_Rule.mdc` / `.instructions.md` — Understanding essays compressed to gates + §2/§4 pointers
  - `Feature_Understanding_Template.md` — short **Instructions for AI Agents** checklist (section examples kept)
  - `Feature_Spec_Template.md` — shorter agent Instructions; point to Workflow §2
  - `agent/roles/understanding-author.md`, `doc-graduate.md`, `feature-implementer.md` + cursor/grok adapters — pointer trim
  - `TODO_Template.md`, `Decision_Template.md`, `Tooling_Template.md` — light consistency polish
  - `chat-ui/AGENT.md` — shape-confirm job blurb; version stamps
  - `Master_Index_Template.md`, `agent/upstream-status.example.yaml`, root `README.md` — version stamps
- **Step B:** Bump Master Index versions to 2.6.7. Refresh installed modular rules if the user wants (bodies changed). Do **not** auto-rewrite live Understanding / Spec / TODO bodies during sync — instruction-block changes apply to new drafts and when that stem is next edited. *(Superseded presentation: 2.6.8 adds `optional-live-reshape` — sync to 2.6.8+ and present the reshape ask.)*

## 2.6.6

- **Live impact:** `versions-only`, `rules`, `content-templates`, `process-docs-only`
- **Files:**
  - `VERSION` — 2.6.5 → 2.6.6
  - `Feature_Understanding_Template.md` — Understanding = **shape only**: What this is / is NOT, Relationship, Assumptions, Confirmed; **How it should work / UI/UX / Visual references / Done when removed**; relocate-don’t-delete into spec when trimming
  - `Feature_Spec_Template.md` — **Contract home** banner + Behavior anti-compression; **Acceptance** + **Visual references** + Behavior hold flows/UI; graduate synthesizes conversation/decisions, not Understanding-only copy
  - `agent/Modular_Docs_Workflow.md` — §2 / §4 shape-vs-spec + graduation anti-compression; version 2.6.6
  - `agent/Modular_Documentation_Rule.mdc` / `.instructions.md` — same shape / guardrails messaging
  - `agent/roles/understanding-author.md`, `roles/cursor|grok/understanding-author.md` — ask user to confirm shape, not full spec
  - `agent/roles/doc-graduate.md`, `agent/roles/feature-implementer.md` — thin Understanding; graduate must not under-fill spec
  - `help/IDEA_CAPTURE_TIPS.md`, `help/USAGE.md`, `chat-ui/AGENT.md` — human-facing shape confirmation
  - `Master_Index_Template.md`, `agent/upstream-status.example.yaml`, root `README.md` — version stamps
- **Step B:** Bump Master Index versions to 2.6.6. Do **not** auto-rewrite live Understanding or Spec bodies during sync. New drafts / Understanding-author / Doc-graduate revisions use shape-only Understanding (is / is not / Relationship / Assumptions); when revising a live Understanding, add/keep the human review banner and trim only if the user asks or that stem is being updated — **relocate** trimmed contract detail (How-it-should-work → Behavior; Visual references; Done when → Acceptance) into that stem’s spec if missing (do not delete). When graduating or updating a live spec, apply anti-compression only for that stem. Do **not** auto-audit every live TODO during sync. Refresh installed modular rules if the user wants (bodies changed). Update Key Locations asset blurbs to “linked from the **spec**” if adopting Master Index deltas.

## 2.6.5

- **Live impact:** `versions-only`, `rules`, `process-docs-only`
- **Files:**
  - `VERSION` — 2.6.4 → 2.6.5
  - `Feature_Understanding_Template.md` — **What this is**: completeness over compression (keep user-stated details; do not pad); NOT stays tight; on Understanding updates re-check **Done when** + TODO and **uncheck** code/spec mismatches
  - `agent/Modular_Docs_Workflow.md` — §4 same What this is rule + Done when/TODO uncheck-on-update; version 2.6.5
  - `agent/Modular_Documentation_Rule.mdc` / `.instructions.md` — same Understanding update / Done when rules
  - `agent/roles/understanding-author.md`, `roles/cursor|grok/understanding-author.md` — completeness over compression; Done when/TODO re-check on update
  - `agent/roles/feature-implementer.md`, `roles/cursor|grok/feature-implementer.md` — if updating Understanding, run the same Done when/TODO check
  - `help/IDEA_CAPTURE_TIPS.md`, `chat-ui/AGENT.md` — mapping / chat-UI guidance
  - `Master_Index_Template.md`, `agent/upstream-status.example.yaml`, root `README.md` — version stamps
- **Step B:** Bump Master Index versions to 2.6.5. Do **not** auto-rewrite live Understanding **What this is** sections during sync. New drafts and Understanding-author revisions use completeness-over-compression; expand a thin section only when the user asks (or when user-stated detail is missing). Do **not** auto-audit every live Done when/TODO during sync — that check runs when an Understanding is updated. Refresh installed modular rules if the user wants (bodies changed).

## 2.6.4

- **Live impact:** `content-templates`, `versions-only`, `process-docs-only`
- **Files:**
  - `VERSION` — 2.6.3 → 2.6.4
  - `Human_TODO_Template.md` — **human-facing order:** Open → Done at top (with scroll-for-instructions note); Instructions for Humans then agent dual-write / Instructions for AI Agents below
  - `agent/Modular_Docs_Workflow.md` — §13 notes Human-TODO section order; version 2.6.4
  - `Master_Index_Template.md`, `chat-ui/AGENT.md`, `agent/upstream-status.example.yaml`, root `README.md` — version stamps
- **Step B:** Bump Master Index versions to 2.6.4. Reorder live `Human-TODO.md` to match the template (Open/Done first; instructions below) — preserve all Open/Done items; move sections only. Do **not** invent or close items.

## 2.6.3

- **Live impact:** `versions-only`, `process-docs-only`
- **Files:**
  - `VERSION` — 2.6.2 → 2.6.3
  - `CHANGELOG.md` — 2.6 Step B dual-write wording clarified; 2.5 Step B “unset ≠ silence” fix
  - `agent/Modular_Docs_Workflow.md` — §13 repair: owner TODO → Human-TODO only; no reverse
  - `Human_TODO_Template.md` — same one-direction repair note
  - `agent/TEMPLATE_SYNC.md` — **Present unset options** every sync (explain + ask; unset ≠ silent no)
  - `agent/roles/template-sync.md` — same present-unset step
  - `agent/RULE_INSTALL.md` — ask doc-roles when missing for any tool (incl. Copilot); unset status row
  - `agent/tools/github-copilot.md`, `agent/tools/openclaw.md` — still offer doc-roles when Install is None
  - `agent/roles/README.md` — “no adapters” ≠ “nothing to offer”
  - `agent/BOOTSTRAP.md` — do not skip Steps 4b/4c by silence
  - `Master_Index_Template.md`, `chat-ui/AGENT.md`, `agent/upstream-status.example.yaml`, root `README.md` — version stamps
- **Step B:** Bump Master Index versions to 2.6.3. Dual-write reminder *(no new scan required)*: **optional** repair is inbox gaps only — human-gated items already on feature/shared `*-TODO.md` with no Open row on `Human-TODO.md` → add thin Open `- [ ]` on `Human-TODO.md`. Do **not** reverse-repair (Human-TODO → feature TODOs / “Needs a human” pointers “for dual-write”). Do **not** invent or close human items. **Present unset options:** if `optional_rules.doc-roles` (or `template-update-check`) is missing, briefly explain and ask once — do **not** auto-enable; do **not** stay silent because unset or because Copilot has no agents-folder install. Record `enabled` or `declined` on answer.

## 2.6.2

- **Live impact:** `versions-only`, `process-docs-only`
- **Files:**
  - `VERSION` — 2.6.1 → 2.6.2
  - `agent/BOOTSTRAP.md` — Step 1b also deletes upstream `.github/workflows/release.yml` after whole-repo clone / “Use this template”
  - `help/SETUP.md` — notes Release workflow cleanup with issue templates
- **Step B:** Bump Master Index versions to 2.6.2. If the project still has Agentic’s `.github/workflows/release.yml` from a whole-repo copy, delete it (and empty `.github/` folders). Do **not** delete the user’s other workflows.

## 2.6.1

- **Live impact:** `content-templates`, `versions-only`, `process-docs-only`
- **Files:**
  - `VERSION` — 2.6 → 2.6.1
  - `Human_TODO_Template.md` — **Open/Done use `- [ ]` list items**, not table cells (preview cannot toggle checkboxes in tables)
  - `agent/Modular_Docs_Workflow.md` — §13: no table checkboxes; convert legacy table Open lists
- **Step B:** Bump Master Index versions to 2.6.1. Convert live `Human-TODO.md` **Open** (and Done if tabular) from table rows to `- [ ]` / `- [x]` list items — preserve Need, Kind, Owner, Blocks, Notes content. Do **not** invent or close items.

## 2.6

- **Live impact:** `content-templates`, `master-index`, `rules`, `process-docs-only`
- **Files:**
  - `VERSION` — 2.5 → 2.6
  - `Human_TODO_Template.md` — human **inbox** (not procurement-only): kinds `procure` · `playtest` · `decide` · `waiting`; checkbox Open list; **index + owner** model; human chat phrases; agent dual-write + sync-on-feedback
  - `TODO_Template.md` — Needs-a-human dual-write patterns; humans pointed at `Human-TODO.md` as inbox
  - `agent/Modular_Docs_Workflow.md` — §13 rewritten (inbox, dual-write, repair); version 2.6
  - `agent/Modular_Documentation_Rule.mdc` / `.instructions.md` — dual-write human-gated work; sync Human-TODO on user feedback
  - `agent/roles/feature-implementer.md` — dual-write language
  - `Master_Index_Template.md` — Human-TODO Key Locations / At a Glance / §3.3–3.4; versions 2.6; §13 anchor update
  - `agent/BOOTSTRAP.md`, `help/USAGE.md`, `help/SETUP.md`, `chat-ui/AGENT.md`, `agent/upstream-status.example.yaml`
  - Root `README.md` — pack 2.6; Human-TODO layout blurb
- **Step B:** Bump Master Index versions to 2.6; adopt Human-TODO Key Locations / At a Glance / Document Map wording. **Required** (`content-templates`): merge missing sections/columns from `Human_TODO_Template.md` → live `Human-TODO.md`, and from `TODO_Template.md` → live `*-TODO.md` (e.g. **Needs a human** heading + Instructions) — **do not** wipe Open/Done; merge structure only. Refresh installed modular rules if user wants (bodies changed). **Optional dual-write repair** *(inbox gaps only — one direction)*: when a human-gated item (`procure` / `playtest` / `decide` / `waiting`) already exists on a feature/shared `*-TODO.md` but has **no** matching Open item on `Human-TODO.md`, add a thin Open `- [ ]` on `Human-TODO.md` that points at that owner TODO. Do **not** invent new human items; do **not** mark items done without user confirmation. Do **not** reverse-repair (copy Human-TODO → feature TODOs, or add “Needs a human” pointers onto feature TODOs “for dual-write”) — that is **not** this optional step. Do **not** skip the required structure merge by calling it dual-write repair.

## 2.5

- **Live impact:** `process-docs-only`, `master-index`, `rules`
- **Files:**
  - `VERSION` — 2.4 → 2.5
  - `agent/roles/` — **(new)** optional playbook roles: Understanding author, Doc graduate, Feature implementer, Bootstrap, Template sync + `README.md`; never always-on
  - `agent/roles/cursor/*.md` — Cursor **subagent** adapters → `.cursor/agents/` ([subagents docs](https://cursor.com/docs/subagents)); gated “Use when …”; not Agent Skills
  - `agent/roles/grok/*.md` — **(new)** Grok Build subagent adapters → `.grok/agents/`
  - `agent/roles/README.md` — harness adapter table (Cursor vs Grok vs Claude)
  - `agent/tools/` — **(new)** per-tool install/sync playbooks (`cursor`, `grok-build`, `claude-code`, `github-copilot`, `agents-md`, `openclaw`, thin `continue`/`cline`) + `README.md`; Claude `AGENTS.md` caveat; Grok `.grok/agents/` = CLI-documented + verify via `grok inspect` / playbook fallback
  - `agent/RULE_INSTALL.md` — router: ask/status yaml → open only `tools/<key>.md`; `optional_rules.doc-roles`
  - `agent/BOOTSTRAP.md` — Step 4c doc roles; installs via tool playbooks
  - `agent/TEMPLATE_SYNC.md` — rules refresh dispatches per installed tool; doc-roles via harness folders
  - `agent/rule-install-status.example.yaml` — `grok-build` + `doc-roles` path examples
  - `agent/Modular_Docs_Workflow.md` — optional roles + tools/ pointer; version 2.5
  - `agent/Modular_Documentation_Rule.mdc` / `.instructions.md` — parent orchestrates delegation/spawn (`.cursor/agents/`, `.grok/agents/`, …); `/` optional; fallbacks if agents missing
  - `Master_Index_Template.md` — Key Locations notes for `agent/roles/` + `agent/tools/`; versions 2.5
  - `help/USING_WITH_AGENTS.md` — slimmed human TOC → `tools/*.md`
  - `help/USAGE.md`, `help/SETUP.md` — roles / tools usage
  - `chat-ui/AGENT.md`, `agent/upstream-status.example.yaml` — version markers 2.5
  - Root `README.md` — pack 2.5; roles + tools in inventory
- **Unchanged content templates:** Feature_Understanding, Feature_Spec, TODO, Tooling, Human_TODO, Decision
- **Step B:** Bump Master Index versions to 2.5; adopt Key Locations deltas (`agent/roles/`, `agent/tools/`). For each `tools.*.status: installed`, open that `tools/<key>.md` only and refresh (ask if customized). If `optional_rules.doc-roles` is `enabled`, refresh harness agents folders (`.cursor/agents/` from `roles/cursor/`, `.grok/agents/` from `roles/grok/`, …). Remove any stale `.cursor/skills/modular-docs-*` leftovers. Do **not** open every tool file; do **not** scan live feature/shared docs; do **not** auto-enable doc roles. If `doc-roles` is **declined**, leave it. If **missing/unset**, briefly explain (playbooks + optional harness adapters) and **ask once**, then record `enabled` or `declined` — do **not** stay silent because unset or because the installed tool has no agents-folder install.

## 2.4

- **Live impact:** `process-docs-only`, `master-index`, `rules`
- **Files:**
  - `CHANGELOG.md` — (new) pack release map for Step B scope
  - `VERSION` — 2.3 → 2.4
  - `Master_Index_Template.md` — Key Locations: CHANGELOG + `docs/reference/` drop zone; At a Glance tight-scope; version markers
  - `agent/Modular_Docs_Workflow.md` — **moved from pack root** into `agent/` (agent playbook, not a content template); session/Path B/reconciliation scope gates; tight-scope; `reference/`; no invented `_shared/`; version markers
  - `agent/TEMPLATE_SYNC.md` — changelog-first Step B + Do-not list; do not restore deleted `agent/upstream/` attribution files
  - `agent/upstream/README.md` — empty/deleted upstream copies are OK; sync must not re-fetch them
  - `agent/Modular_Documentation_Rule.mdc` — session default, route-by-ask, after-changes gates; tight-scope philosophy; no invented `_shared/`
  - `agent/Modular_Documentation_Rule.instructions.md` — same as `.mdc` body
  - `agent/BOOTSTRAP.md` — pack spot-check; map fill from conversation; auto-move clearly upstream README/LICENSE/CONTRIBUTING (no ask); create `docs/reference/README.md`; leave §3.1 empty unless truly shared
  - `agent/RULE_INSTALL.md` — bounded install-path checks
  - `agent/upstream-status.example.yaml` — example versions 2.4
  - `chat-ui/AGENT.md` — Master Index template only when asked; version markers
  - `help/SETUP.md` — tightened install flow (copy → bootstrap → layout → next links); less post-setup bullet pile
  - `help/USAGE.md` — deduped tips; patterns kept; bootstrap/sync shortened to point at SETUP/CHANGELOG
  - `help/USING_WITH_AGENTS.md` — sync wording (inventory links unchanged in role)
  - `help/IDEA_CAPTURE_TIPS.md`, `chat-ui/README.md` — full chat history tip; save under `docs/reference/`
  - Root `README.md` — rewritten landing page (how it works → get started → stay current; less inventory dump); Stay current caveat for packs before TEMPLATE_SYNC (pre-1.2)
  - Root `CONTRIBUTING.md` — changelog maintenance; maintainer note: write agent instructions for off-road / thorough models
- **Unchanged content templates:** Feature_Understanding, Feature_Spec, TODO, Tooling, Human_TODO, Decision
- **Step B:** Bump Master Index versions to 2.4; adopt Key Locations / At a Glance deltas (CHANGELOG, `reference/`, tight scope, **empty `_shared/` OK**); **retarget workflow links** to `docs/templates/agent/Modular_Docs_Workflow.md` (file moved out of pack root); if a stale copy remains at `docs/templates/Modular_Docs_Workflow.md`, remove it after the pack overwrite (Step A should already replace the whole folder). Refresh installed modular rules if user wants (bodies changed); do **not** scan live feature/shared docs; do **not** invent new `_shared/` rows during sync. **`docs/templates/agent/upstream/`** attribution copies may be **intentionally deleted** — do **not** re-download / restore them

## 2.3

- **Live impact:** `master-index`, `optional-upstream-check`, `process-docs-only`
- **Files:**
  - `VERSION` — 2.2 → 2.3
  - `Master_Index_Template.md` — VERSION in templates row; optional `upstream-status.yaml` Key Locations row
  - `Modular_Docs_Workflow.md` — process/version alignment
  - `agent/TEMPLATE_SYNC.md`, `agent/TEMPLATE_UPDATE_CHECK.md` — upstream check + sync stamp
  - `agent/Template_Update_Check_Rule.*`, `agent/upstream-status.example.yaml`, `agent/RULE_INSTALL.md`
  - `help/SETUP.md`, `help/USAGE.md`, `help/USING_WITH_AGENTS.md`, `chat-ui/AGENT.md`
- **Unchanged content templates:** Feature_Understanding, Feature_Spec, TODO, Tooling, Human_TODO, Decision
- **Step B:** Bump Master Index versions; adopt Master Index Key Locations deltas; link optional upstream check — do **not** scan live feature/shared docs
