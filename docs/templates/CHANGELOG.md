# Template pack changelog

> **Agents:** After [`agent/TEMPLATE_SYNC_A.md`](agent/TEMPLATE_SYNC_A.md), open [`agent/TEMPLATE_SYNC_B.md`](agent/TEMPLATE_SYNC_B.md). Select catch-up entries from **from** → **to** (B0 Catch-up) — not top-only on version jumps. **Union** Live impact tags; skim Step B lines for one-shots; do not invent a broader audit. **Summarize the union only** — do not name catalog optional tags that were not selected as “skipped.” `auto-all` executes unioned tagged passes on all stems; it is not “run every row in this table.”
>
> **Maintainers:** Every `VERSION` bump must update this file in the same commit (newest entry on top). Keep bullets brief. When editing agent playbooks, write for thorough “off-road” models — explicit scope gates and Do-not lists, not open “as needed” language (see root [`CONTRIBUTING.md`](../../CONTRIBUTING.md)).

**Live impact tags** (use only these — lasting catalog; a tag fires only when a selected catch-up entry lists it):

| Tag | Meaning for Step B |
|-----|--------------------|
| `versions-only` | Bump **Pack version** in live Master Index; stop |
| `master-index` | Adopt structural deltas in live `Master_Index.md` (headings, Key Locations, Document Map columns) |
| `content-templates` | Add *missing* sections/structure from content templates into live Understanding / Spec / TODO / Tooling / Human-TODO — **not** trim/remove (see `optional-live-reshape`) |
| `optional-live-reshape` | Live Understanding → shape trim + relocate into specs (Workflow §4). **`auto` / `auto-all`:** run all Document Map stems. **`choose`:** present + ask once (default yes). Do **not** silent-skip under choose |
| `optional-assumption-cleanout` | Live Understanding lock-gate clean-out (Workflow §4). **`auto` / `auto-all`:** all Document Map Understanding stems. **`choose`:** present + ask once (default yes). Lock obvious defaults; delete invented quizzes; do not treat `docs/reference/` examples as the target unless clearly set as the target; leave only real forks. Do not invent new Assumptions or Understanding on `build-first` |
| `optional-todo-ambition` | Live TODO ambition pass (agent timescale). **`auto` / `auto-all`:** all Document Map `*-TODO.md`. **`choose`:** present + ask once. Do not invent work |
| `optional-todo-operable` | Live TODO operable dual-track (Workflow §5.3). **`auto` / `auto-all`:** all Document Map `*-TODO.md`. **`choose`:** present + ask once. Add exercise-path rows or **library-only** labels; do not invent unrelated backlog |
| `optional-todo-kit-coverage` | Live TODO kit-coverage pass (Workflow §5.4). **`auto` / `auto-all`:** all Document Map `*-TODO.md`. **`choose`:** present + ask once. Add covering TODOs for spec-named in-scope leftovers on **existing** stems (**open or Completed** counts — do not resurrect); one research item if the spec is thin. No new map rows; no vendor-doc fetch in sync |
| `optional-todo-outcomes` | Live TODO outcomes pass (Workflow §5.5). **`auto` / `auto-all`:** all Document Map `*-TODO.md`. **`choose`:** present + ask once. Mirror operable Acceptance into unchecked Outcomes rows; label children; one exercise task when an outcome has no path. Do not check outcomes. Do not mint a task per architecture bullet |
| `optional-todo-completed-cleanout` | Live TODO Completed cleanout. **`auto` / `auto-all`:** all Document Map `*-TODO.md`. **`choose`:** present + ask once. Remove a Completed checkbox that git shows was never an open `[ ]` task and is not an exercise note. Unsure → leave the row |
| `rules` | Refresh installed agent rules/adapters from local pack (**no ask** unless tool has `customized: true`) |
| `optional-upstream-check` | Stamp `upstream:` in `docs/ADT-settings.yaml` / offer enable update-check if unset |
| `process-docs-only` | Pack process/help/agent docs only — no live feature/shared content scan |

---

## 2.9.11

- **Live impact:** `versions-only`, `process-docs-only`, `rules`
- **Summary:** `process-docs-only` does not cancel a skipped `optional-todo-completed-cleanout`. The Step B do-not list names that tag with the other live passes. Work-verifier runs before the claimed TODO item moves to Completed. A fail leaves that item open.
- **Changes:**
  - `VERSION` — 2.9.10 → 2.9.11
  - `agent/TEMPLATE_SYNC_B.md` — do-not guard includes completed-cleanout
  - modular rule twins — After changes: work-verifier, then mark-done
- **Step B:** Bump Master Index **Pack version** to 2.9.11 from local `VERSION`. **`rules`:** refresh installed modular-rule copies so work-verifier runs before the claimed item is marked `[x]` and moved to Completed; on fail the item stays open. No live feature/shared scan. A `process-docs-only` entry in this jump does not cancel `optional-todo-completed-cleanout` from an earlier selected entry.

## 2.9.10

- **Live impact:** `versions-only`, `rules`, `optional-todo-completed-cleanout`
- **Summary:** Completed is not a repair log. A Completed row is a plotted slice or the exercise note that proves an Outcome. An incidental fix stays in git. Sync pass `optional-todo-completed-cleanout` removes a Completed checkbox that was never an open task. A passing exercise note names each observable clause on the stem’s exercise path. A unit-test path does not check the outcome. A code change that alters an observable the outcome names, or a human report that the scenario did not hold, unchecks the outcome and adds one Exercise. Work-verifier compares one claimed TODO item to that unit’s diff. Warden honesty reopens a checked item the code does not implement. Declining doc-roles does not skip either compare.
- **Changes:**
  - `VERSION` — 2.9.9 → 2.9.10
  - `agent/workflow/todos.md` §5.5 — Completed rows, passing note, reopen, code versus the checklist
  - modular rule, `feature-implementer.md`, `todo-warden.md` — do not add a Completed row for an incidental fix; reopen when an observable changes or the scenario did not hold
  - `work-verifier.md`, `orchestrator.md`, `human-todo.md` — one unit’s diff; thin exercise note fails; parent runs the compare when the adapter is absent
  - `TODO_Template.md` — one pointer under Completed
  - `agent/TEMPLATE_SYNC_B.md` — **`optional-todo-completed-cleanout`**
  - `DECISIONS.md` D30, D31
- **Step B:** Bump Master Index **Pack version** to 2.9.10 from local `VERSION`. **`rules`:** refresh installed modular-rule copies so an incidental fix does not get a new Completed row, a passing note names each observable clause, a checked outcome reopens when an observable it names changes or a human says the scenario did not hold, and that audit runs even when the outcome is already `[x]`. An incidental fix that changes an observable is that reopen, not a sentence left on a checked row. A claimed TODO item is compared to that unit’s diff before mark-done. **`optional-todo-completed-cleanout`:** present/execute per `sync.mode` — for each Document Map `*-TODO.md`, under `## Completed` only, remove a `- [x]` row whose title never appears as `- [ ]` in `git log -p` for that file and whose text is an incidental fix (review patch, Bugbot finding, copy, typo). Keep a row that ever existed as an open task. Keep an exercise note. Unsure → leave the row. Do not remove open tasks. Do not check Outcomes. Under **`choose`:** ask once (default all stems). Under **`auto` / `auto-all`:** all Document Map `*-TODO.md`.

## 2.9.9

- **Live impact:** `versions-only`, `rules`, `content-templates`, `optional-todo-outcomes`
- **Summary:** Sticky outcomes. A drained child list is not capability-done. `## Outcomes` stays open until a passing exercise note. A break note does not add a second Exercise. Slices do not check operable Acceptance. The outcome audit checks the parent row and fills the next blank. Doc-roles are optional: declining them, or a one-off change with no orchestrator, still runs that audit in the parent session. The check runs after work-verifier pass when that step exists. An outcome already checked does not get another human-verify playtest. The audit is the only creator of a human-verify playtest, and only after that note. Sync pass `optional-todo-outcomes` retrofits existing stems and withdraws premature look-rows.
- **Changes:**
  - `VERSION` — 2.9.8 → 2.9.9
  - `agent/workflow/todos.md` §5.5 — outcome rows, flat `outcome:` labels, exercise task, who may check
  - `TODO_Template.md` — Outcomes fill-in
  - `agent/roles/feature-implementer.md`, `work-verifier.md`, `doc-graduate.md`, `todo-warden.md`, `orchestrator.md`, `orchestrator-git.md` — slice cannot close an outcome; warden outcome audit; empty list is not stem-drained; warden alone creates human-verify playtests; branch-pr and non-PR close-out commit audit edits on `clean`
  - `agent/TEMPLATE_SYNC_B.md` — **`optional-todo-outcomes`** live pass
  - `agent/workflow/human-todo.md`, modular rule, `help/USAGE.md` — dual-write is `procure` / `decide` / `waiting`; the outcome audit creates the human-verify playtest; declining doc-roles does not skip the audit
  - `DECISIONS.md` D30
- **Step B:** Bump Master Index **Pack version** to 2.9.9 from local `VERSION`. **`content-templates`:** if a live `*-TODO.md` has no `## Outcomes` heading, add that heading from the template (empty fill-in). Do not check outcomes in that step. **`optional-todo-outcomes`:** present/execute per `sync.mode` — for each Document Map stem, mirror each operable Acceptance line into an unchecked Outcomes row (rewrite a non-scenario line from Overview / Behavior; defer when an observable needs a product decision); label open tasks that clearly serve one outcome; uncheck operable Acceptance that is `[x]` with no passing exercise note; add one exercise task only when that outcome has no exercise item yet (none open, none Completed) and no passing note. A Completed break note is not a second Exercise. Do not check outcomes. Do not create a human-verify playtest (the outcome audit is the only creator of that row; this pass does not run it). Withdraw an Open `playtest` whose outcome is still `[ ]` (`not a human look`). Do not diff the repo into a task per architecture bullet. Do not reopen Completed items. Named spec leftovers stay on kit-coverage. Under **`choose`:** ask once (default all stems). Under **`auto` / `auto-all`:** all Document Map `*-TODO.md`. **`rules`:** refresh installed modular-rule copies so an Outcomes row stays open until a passing exercise note. No Understanding reshape.

## 2.9.8

- **Live impact:** `versions-only`, `process-docs-only`, `rules`
- **Files:**
  - `VERSION` — 2.9.7 → 2.9.8
  - `workflow/team-roster.md` *(new)* — team inbox, two-stage roster, and one initial PR. Open only when `team_inbox.enabled`
  - `workflow/human-todo.md` — solo dual-write only. One line: if team inbox is on, open `team-roster.md` for stamp and close
  - Workflow index, scaffolds, roster template, bootstrap — point roster procedure at `team-roster.md`
  - Modular rule — same one-line open
- **Step B:** Bump Master Index **Pack version** to 2.9.8 from local `VERSION`. **`rules`:** refresh installed modular-rule copies so a `team_inbox.enabled` session opens `workflow/team-roster.md`. No live feature/shared scan. Do not create `Team-Roster.md` on a human-only inbox.

## 2.9.7

- **Live impact:** `versions-only`, `process-docs-only`, `rules`, `content-templates`, `master-index`
- **Files:**
  - `VERSION` — 2.9.6 → 2.9.7
  - `Modular_Documentation_Rule.mdc` / `.instructions.md` — one route table (ask, playbook, adapter) names the short asks (*Bootstrap the doc templates*, *Bootstrap modular docs*, *Please update ADT*, *update ADT*, *sync ADT*, *sync the doc templates*, *check for ADT updates*, *drain unblocked TODOs*, reference files). Same playbooks. Profile modes stay in the coding-gate table only. Closing line keeps the scars that are not already in the session checklist. Session default: a `procure` for an API the running app will call also writes **Services this app consumes** on Tooling
  - `Tooling_Template.md` / `workflow/tooling.md` — **Services this app consumes** (service, why, credential name, docs link). Not a Required/Optional row. Install skips it. No secrets
  - `workflow/human-todo.md` — same turn as that `procure` row, add or update the Services row. The Human-TODO item stays the errand
  - `Project_README_Template.md` / `BOOTSTRAP.md` **Step 3r** — if root `README.md` is missing, create the human entry point (what this is, link to Master Index, Tooling, Human-TODO). Do not overwrite a project README. Do not paste the services table or the Document Map
  - `Master_Index_Template.md` — Key Locations row for root `README.md`
- **Step B:** Bump Master Index **Pack version** to 2.9.7 from local `VERSION`. **`rules`:** refresh installed modular-rule copies so the route table is the single one, including those short asks, and session default names the Services row. **`content-templates`:** if live `docs/Tooling.md` has no **Services this app consumes** section, add the empty section from the template. Do not invent services. Do not scan the codebase for APIs. If root `README.md` is missing, copy `Project_README_Template.md` and fill the name from Master Index §1 when that heading is already a real project name. Do not overwrite an existing README. **`master-index`:** Key Locations gains the root `README.md` row when that row is missing. No live feature/shared scan.

## 2.9.6

- **Live impact:** `versions-only`, `process-docs-only`, `master-index`, `rules`
- **Files:**
  - `VERSION` — 2.9.5 → 2.9.6
  - Docs profile value **`ship-first` renamed `build-first`** (same mode: spec + TODO, no Understanding gate). Playbooks, scaffolds, help, rules, and the example settings use the new value
  - `TEMPLATE_SYNC_B.md` **B0.1b** — every sync: if `docs_profile.mode` is `ship-first`, rewrite it to `build-first`. Do not re-ask. Do not treat it as unset
  - `workflow/profile-standing.md` — on sight, the same rewrite
  - `BOOTSTRAP.md` Step 3p **C**, `RULE_INSTALL.md`, `TEMPLATE_SYNC_B.md` step 10 — when doc-roles are offered, say why: if installed, heavier moments leave the parent session so it stays slim; without them that work stays in the parent
  - Root `DECISIONS.md` **D27** — do not silently undo
  - `agent/commands/` — optional `/sync` and `/orchestrate` (same playbooks as the short asks). Offered once; decline if they would rather just ask. Cursor, Claude Code, and Copilot install files; other tools record the choice and install nothing
  - Root `DECISIONS.md` **D28** — do not silently undo
  - `workflow/profile-standing.md` §0.2, modular rule LOOKOUT — repo behavior that is **not** an ADT playbook override is **not** standing. Ask once: always-on rule/instruction, or a skill. Do not create either before they answer
  - `workflow/profile-standing.md` **Sync cleanout (2.9.6)** — remove non-pack behavior from `standing.instructions` and ask once: rule, skill, or dropped. Do not silent-create. Playbook overrides stay
  - Root `DECISIONS.md` **D29** — do not silently undo
  - Git menu lives only in `roles/orchestrator-git.md` **Modes**. Bootstrap Step 3p **E** and sync **B0.6** still ask (unset → ask; never silent `current-push`; write-in is not an eighth mode) and present that table — they do not restate the seven modes
  - Docs-profile words live only in `workflow/profile-standing.md` §0.1. Bootstrap Step 3p **A** still asks once before Step 3d and presents that section. The always-on rule keeps the short coding-gate table
  - `eval/run_eval.py` — modular rule `.mdc` and `.instructions.md` bodies must match after frontmatter
- **Step B:** Bump Master Index **Pack version** to 2.9.6 from local `VERSION`. **B0.1b:** rewrite `docs_profile.mode: ship-first` → `build-first` (note it in the summary). **`master-index`:** At a Glance / Key Locations that still say `ship-first` adopt `build-first`. **`rules`:** refresh installed modular-rule copies so the session default names `build-first` and the LOOKOUT line asks rule-or-skill for non-pack repo behavior (standing stays pack playbooks only). **Present unset `slash-commands`** (step 10 / Step 3p **F**): explain `/sync` and `/orchestrate` are a menu; decline if they would rather just ask. If already `enabled`, refresh those command files from `agent/commands/`. **Standing cleanout (2.9.6):** open `standing.instructions` only. Keep ADT playbook overrides. Remove how-to-act bullets that are not pack playbooks, then ask once: always-on rule/instruction, skill, or dropped. Do not create a rule or skill before they answer. Do not silent-create under `auto` / `auto-all`. No live feature/shared scan.

## 2.9.5

- **Live impact:** `versions-only`, `process-docs-only`, `master-index`, `rules`
- **Files:**
  - `VERSION` — 2.9.4 → 2.9.5
  - `workflow/session-freshness.md` — sibling probe: **`git diff --quiet HEAD <other-HEAD> -- docs` is the drift verdict**. `git log HEAD..<other> -- docs` only **names** commits on a real stop. Squash-merge / rebase severs ancestry (GitHub default; `branch-pr-squash`) — graph-only “behind” with identical `docs/` is **not** drift. Pre-merge re-check does not cover the next-session miss the squash **creates**; the content check does
  - `Modular_Documentation_Rule.*` / Workflow index / `Master_Index_Template.md` / `help/USING_WITH_AGENTS.md` — same verdict on the session-default path (was “`docs/` commits this HEAD lacks”)
  - Root `DECISIONS.md` **D26** — do not silently undo
  - Root `eval/` — `session-docs-freshness` covers content-first sibling probe
- **Step B:** Bump Master Index **Pack version** to 2.9.5 from local `VERSION`. **`master-index`:** At a Glance **Docs freshness**: sibling drift = content (`git diff`), not ancestry after squash-merge. **`rules`:** refresh installed modular-rule copies so session default step 0 uses the content verdict — the gate still false-stops after squash-merge if only the pack copy updates. No live feature/shared scan.

## 2.9.4

- **Live impact:** `versions-only`, `process-docs-only`, `master-index`, `rules`
- **Files:**
  - `VERSION` — 2.9.3 → 2.9.4
  - `README.md` *(templates root, new)* — pack-owned; replaced in full on sync; edits vanish; change upstream; project-owned docs live elsewhere
  - `workflow/session-freshness.md` *(new, §0.3)* — session-start `git status` + `git worktree list`; sibling `docs/` drift → hard stop; Stay ≠ current. A0 remains the overwrite gate. **Docs-overlapping PRs:** same-stem TODO/spec on an open PR → add there (docs overlap ≠ code overlap; Grok successive spawn)
  - `Modular_Documentation_Rule.*` — session default step 0 is the cheap check (so it is on the routed path); Shared / Before implementation slimmed to module pointers; bootstrap is **parent only** (no `docs-bootstrap` spawn); successive-issue / Grok parent: do not spawn a second PR that rewrites the same live docs
  - `roles/adapter-src/` — **removed** `docs-bootstrap` (bootstrap installs adapters; the adapter could not exist until after the job). Keep in-session [`roles/bootstrap.md`](agent/roles/bootstrap.md) as a thin parent wrapper
  - Workflow index / implement / todos / Master Index / roles / tools (`grok-build` successive-issues) / help / `TEMPLATE_SYNC_A` / `TEMPLATE_SYNC_B` / `RULE_INSTALL` / `BOOTSTRAP` — route the same lesson; do not leave it only in sync/install playbooks
  - Root `DECISIONS.md` **D24** — do not silently undo; **D6** — standing is the git-mode write-in (not an eighth mode); **D25** — Bugbot reads the PR until ready; squash-before-ready is not required
  - `BOOTSTRAP.md` Step 3p **E**, `TEMPLATE_SYNC_B.md` B0.6, `orchestrator-git.md` / `orchestrator.md`, `profile-standing.md`, `ADT-settings.example.yaml`, `help/USING_WITH_AGENTS.md` — git-mode menu: **write-in (not a quiz, not an eighth mode)** — closest mode + `standing.instructions` for merge commit / rebase-merge / always squash before ready (HEAD-only reviewer) / custom close-out
  - `orchestrator-git.md` / `orchestrator.md` / BOOTSTRAP / B0.6 / roles README / root README — **`milestone-pr` does not squash before ready** for Bugbot (PR review until ready; commits after ready are tip-only). `branch-pr-squash` stays the one-morning-PR option
  - Root `eval/` — `session-docs-freshness` pack contract; `standing-playbook-override-only` covers the git-menu write-in; `milestone-pr-multi-todo` covers D25
- **Step B:** Bump Master Index **Pack version** to 2.9.4 from local `VERSION`. **`master-index`:** Key Locations `docs/templates/` row: pack-owned / do not edit / see `templates/README.md`. At a Glance: add **Docs freshness** pointer (Stay ≠ current; same-stem open PR → add there). Quick Start step 1: freshness first. **`rules`:** refresh installed modular-rule copies so session default step 0 is live — the gate does nothing if only the pack copy updates. If doc-roles enabled: refresh **six** adapters; **delete leftover** `docs-bootstrap.md` / `docs-bootstrap.agent.md`. No live feature/shared scan.

## 2.9.3

- **Live impact:** `versions-only`, `process-docs-only`, `content-templates`, `master-index`
- **Files:**
  - `VERSION` — 2.9.2 → 2.9.3
  - `workflow/product-vision.md` — **§4.5:** create destination file on **all** profiles; **`ship-first`** is **not a gate**. *Lock product shape* starts confirm. Draft source unchanged
  - `BOOTSTRAP.md` / `TEMPLATE_SYNC_B.md` / Master Index / help / modular rule — always create lightweight Product-Vision; ship-first does not wait
  - Root `DECISIONS.md` **D23** — supersedes D21 create-omit; end-state-picture job stays
  - Root `eval/` — `product-vision-end-state` must create, must not gate
- **Step B:** Bump Master Index **Pack version** to 2.9.3 from local `VERSION`. **`master-index`:** Key Locations Product-Vision row: all profiles create; `ship-first` is destination-only. **`content-templates`:** if `docs/Product-Vision.md` is missing → create from the template (**all** profiles, including `ship-first`). **Peek `docs/reference/` first** (newest 3–5 idea/identity exports, or user-pointed files) + this-turn conversation; lightweight draft is / is not + end-state picture from **that** (lock obvious; empty Assumptions OK; examples ≠ target unless clearly set). **Then** fill How the map fits from **existing** map rows only. **Do not** build the picture by summarizing the Document Map / feature Understandings / specs. **`ship-first`:** do **not** treat `draft` as a coding gate. *Lock product shape* only starts the confirm gate. Do not invent stems. Do not copy sermons into the live file. Do not skip `reference/` because the map looks complete. No live feature/shared scan beyond that peek + the map-fit table. No `rules` tag — do not refresh installed modular rules from 2.9.3 alone.

## 2.9.2

- **Live impact:** `versions-only`, `process-docs-only`, `content-templates`
- **Files:**
  - `VERSION` — 2.9.1 → 2.9.2
  - `workflow/human-todo.md` — one-shot *apply defaults to Open* fills unassigned rows from `kind_defaults` **only if that `role_id` is Active**; else leave `unassigned` (same gate as stamp-on-dual-write). Do not lock rows onto a missing id
  - `Human_TODO_Template.md` — Claim / backfill legend: Active-roster gate on *apply defaults to Open*
  - `ADT-settings.example.yaml` / `DECISIONS.md` D19 — backfill Active gate
  - Root `eval/` — `team-inbox-optional` covers backfill Active gate
- **Step B:** Bump Master Index **Pack version** to 2.9.2 from local `VERSION`. **`content-templates`:** if live Human-TODO has the *apply defaults to Open* bullet without the Active-roster gate, add **only if that `role_id` is Active on Team-Roster; else leave `unassigned`**. Do **not** run *apply defaults to Open* during this sync unless the user asked and the default ids are Active. Do **not** re-stamp explicit assignees. Do **not** add `team_inbox` from the example. No live feature/shared scan. No `rules` tag — do not refresh installed modular rules from 2.9.2 alone.

## 2.9.1

- **Live impact:** `versions-only`, `process-docs-only`, `content-templates`, `master-index`
- **Files:**
  - `VERSION` — 2.9.0 → 2.9.1
  - `Team_Roster_Template.md` — named humans self-ID with **their slug** (`alex`), not leftover `human`. Human-TODO stays the work inbox. Empty Active until someone self-IDs. Optional leftover `human` bucket only if that id is Active
  - `workflow/human-todo.md` — **Human self-ID** write path; missing Active → `unassigned` (do **not** fallback-stamp `human` for human-gated kinds). Stamp only Active `role_id`s
  - `Human_TODO_Template.md` — Assignee legend: stamp from `kind_defaults` **only if Active on Team-Roster**; else `unassigned`. *Put me on the roster as Alex*
  - `BOOTSTRAP.md` — Step 3p continues to **Step 3v** (was skipping Product-Vision)
  - `ADT-settings.example.yaml` / help / workflow index / Master Index / modular rule — named-human pointers
  - Root `DECISIONS.md` **D22** — do not silently undo
  - Root `eval/` — `team-inbox-optional` covers named-human self-ID + no fallback-stamp
- **Step B:** Bump Master Index **Pack version** to 2.9.1 from local `VERSION`. **`master-index`:** Team-Roster Key Locations / §3.4 blurb may mention named humans (file exists only when `team_inbox` is on). **`content-templates`:** if live `team_inbox.enabled` and `docs/Team-Roster.md` is missing → create from the template (do **not** invent bot or human-name rows; do **not** copy Row shape into Active). If a live roster already has a leftover `human` row, leave it — do not rewrite people onto invented slugs. If live Human-TODO is missing the Active-gate Assignee legend or *Put me on the roster* phrase, add those. If `team_inbox` is unset / `enabled: false` → **do not** create `Team-Roster.md`. Do **not** add `team_inbox` to live settings from the example. No live feature/shared scan. No `rules` tag — do not refresh installed modular rules from 2.9.1 alone.

## 2.9.0

- **Live impact:** `versions-only`, `process-docs-only`, `content-templates`, `master-index`
- **Files:**
  - `VERSION` — 2.8.1 → 2.9.0
  - `Product_Vision_Template.md` — **(new)** live `docs/Product-Vision.md`: whole-product is / is not + **end-state picture** + how the map fits. Not a feature checklist. Not a second spec
  - `workflow/product-vision.md` — **§4.5:** create under **prevent** (bootstrap / first live-docs / sync); **balanced** when 2+ stems or fuzzy whole; **do not** silent-create on **ship-first**. **Draft source:** peek `docs/reference/` first — do **not** rebuild the picture from the feature map. Draft does not add a second coding gate; **confirmed** vision: do not implement a fighting feature. Lock gate stays Workflow §4
  - `Master_Index_Template.md` / bootstrap / sync / help / paved path / understanding + implement pointers
  - Root `DECISIONS.md` **D21** — do not silently undo
  - Root `eval/` — `product-vision-end-state` pack contract + scaffold skeleton
- **Step B:** Bump Master Index **Pack version** to 2.9.0 from local `VERSION`. **`master-index`:** add Key Locations / §3.4 / At a Glance row for Product-Vision. **`content-templates`:** if `docs_profile` is **`prevent`** (or unset) and `docs/Product-Vision.md` is missing → create from the template. **Peek `docs/reference/` first** (newest 3–5 idea/identity exports, or user-pointed files) + this-turn conversation; draft is / is not + end-state picture from **that** (lock obvious; empty Assumptions OK; examples ≠ target unless clearly set). **Then** fill How the map fits from **existing** map rows only. **Do not** build the picture by summarizing the Document Map / feature Understandings / specs. **`balanced`:** create only if 2+ feature stems or whole-product identity is already fuzzy (same peek). **`ship-first`:** **do not** create *(superseded by 2.9.3 always-create)*. Do not invent stems. Do not copy sermons into the live file. Do not skip `reference/` because the map looks complete. No live feature/shared scan beyond that peek + the map-fit table. No `rules` tag — do not refresh installed modular rules from 2.9.0 alone.

## 2.8.1

- **Live impact:** `versions-only`, `process-docs-only`, `content-templates`, `master-index`
- **Files:**
  - `VERSION` — 2.8.0 → 2.8.1
  - `Team_Roster_Template.md` — **(new)** live `docs/Team-Roster.md` scaffold (create **only** when `team_inbox` is enabled). Columns: **Name**, **Jobs**, **Anti-jobs** *(if defined)*, Follow-ups, Handoff, Roster write. Empty Active + optional `human` fill-in is correct. Row-shape example is **not** a live bot. Update the row when jobs change
  - `workflow/human-todo.md` — **two-stage roster:** coding agent on a handoff **reads** only (do not invent rows; stamp `kind_defaults` only if that `role_id` is Active); bots **self-ID** their own row (Name / Jobs / Anti-jobs if defined); report-only bots ask another agent or the human to add them. **One initial PR** when standing up a full team — do not open competing roster PRs. Stale-row: update same turn when duties change
  - `Human_TODO_Template.md` / `ADT-settings.example.yaml` / workflow index / help / bootstrap / `TEMPLATE_SYNC_B.md` — pointers; do not silent-create the live roster on a human-only inbox
  - `Master_Index_Template.md` — optional Key Locations / §3.4 row for Team-Roster
  - Root `DECISIONS.md` **D20** — do not silently undo
  - Root `eval/` — `team-inbox-optional` contract covers the roster split
- **Step B:** Bump Master Index **Pack version** to 2.8.1 from local `VERSION`. **`master-index`:** add the optional Team-Roster Key Locations / §3.4 row (file exists only when `team_inbox` is on). **`content-templates`:** if live `team_inbox.enabled` and `docs/Team-Roster.md` is missing → create from the template (**human** fill-in only; do **not** invent bot rows; do **not** copy Row shape into Active). If `team_inbox` is unset / `enabled: false` → **do not** create `Team-Roster.md`. Do **not** add `team_inbox` to live settings from the example. No live feature/shared scan. No `rules` tag — do not refresh installed modular rules from 2.8.1 alone.

## 2.8.0

- **Live impact:** `versions-only`, `process-docs-only`, `content-templates`
- **Files:**
  - `VERSION` — 2.7.29 → 2.8.0
  - `agent/ADT-settings.example.yaml` — optional **`team_inbox`** (omit / unset / `enabled: false` = human-only inbox; **no auto-stamp**). Enabling opts into **assign-all-at-once**: stamp Assignee from `kind_defaults` on dual-write; one-shot *apply defaults to Open* backfill. Suggested kind→role defaults are the stamp map, not a mandatory bot org chart. Do not force a project into another team’s workflow
  - `workflow/human-todo.md` — team assignees / **claim / reassign** as **override only**; stamp-on-dual-write + one-shot backfill are the bulk path; bot discovery = “my open rows” / one digest ping (not one PR per claim). Dual-write + done-only-on-confirm still apply (assignee chat report may check playtest; no silent close)
  - `Human_TODO_Template.md` — optional **Assignee** / **Claim** lines; first fill stamps from kind defaults when enabled; claim/reassign is override only; not forced into a bot team
  - `Modular_Docs_Workflow.md` — one-line `team_inbox` pointer on §13
  - `roles/todo-warden.md` — do not mark Human-TODO done without a confirm; allowed assignee bots count only when `team_inbox.enabled`
  - `TEMPLATE_SYNC_B.md` B0.1 — do not copy `team_inbox` from the example unless the user already enabled team routing
  - Root `DECISIONS.md` **D19** — do not silently undo
  - Root `eval/` — `team-inbox-optional` pack contract
- **Step B:** Bump Master Index **Pack version** to 2.8.0 from local `VERSION`. **Do not** add `team_inbox` to live `ADT-settings.yaml` from the example (omit / unset stays human-only — **no silent force** into team routing; **no auto-stamp**). If live `team_inbox.enabled` + `kind_defaults` already exist, agents may run *apply defaults to Open* **once** (fill unassigned only **if that `role_id` is Active on Team-Roster**; else leave `unassigned`; do not re-stamp explicit assignees). If `content-templates`: add missing optional Assignee / Claim *shape* and the human claim/reassign / *apply defaults to Open* bullets on live Human-TODO (leave `unassigned` unless live settings are enabled, this is that one-shot backfill, **and** the default `role_id` is Active; do **not** invent role ids or enable routing). No live feature/shared scan. No optional live pass unless its tag is in this jump’s union (this entry adds none beyond content-templates). No `rules` tag on this entry — do not refresh installed modular rules from 2.8.0 alone.

## 2.7.29

- **Live impact:** `versions-only`, `process-docs-only`, `rules`
- **Files:**
  - `VERSION` — 2.7.28 → 2.7.29
  - `agent/TEMPLATE_SYNC_B.md` — **Summarize** reports **from→to** + **unioned** tags + executed / offered / declined **from that union only**. Do **not** name catalog optional tags that were not in the union as “skipped.” `auto-all` = execute unioned tagged passes on all stems, not every row in the tag table. “Skipped” is reserved for a unioned tagged pass the user declined (`choose`) or a path check that did not apply (B8 modern layout)
  - `roles/template-sync.md` + adapter-src / cursor|grok|copilot adapters — same summarize rule
  - `help/USAGE.md` — sync summary lists the union, not the full catalog
  - Root `DECISIONS.md` **D18** — do not silently undo
  - Root `eval/` — `sync-summary-union-only` pack contract
- **Step B:** Bump Master Index **Pack version** to 2.7.29 from local `VERSION`. Refresh installed modular rules (**no ask** unless `customized: true`). If `optional_rules.doc-roles` is **enabled** → refresh **docs-template-sync** adapters. No live feature/shared scan. No optional live pass unless its tag is in this jump’s union (this entry adds none).

## 2.7.28

- **Live impact:** `versions-only`, `process-docs-only`, `rules`, `optional-assumption-cleanout`
- **Files:**
  - `VERSION` — 2.7.27 → 2.7.28
  - `CHANGELOG.md` — new Live impact tag `optional-assumption-cleanout`
  - `agent/workflow/understanding.md` §4 — **lock gate** (source of truth): lock obvious defaults in is / is not; **Assumptions = real forks only** (empty is success); **no-ask proviso** (design already clear → zero Assumption asks is correct); do **not** treat examples in `docs/reference/` / chat as the target unless clearly set as the target; lesser-path ask only with a **real non-timescale reason** (not an MVP / half-measure to finish faster). **Clean-out pass** procedure lives here
  - `Feature_Understanding_Template.md` — heading `Assumptions (real forks only)`; one optional bullet
  - `roles/understanding-author.md` + adapter-src / cursor|grok|copilot adapters — pointer: lock obvious; offer clean-out; reference examples are not the target unless clearly set
  - `roles/template-sync.md` + adapter-src / cursor|grok|copilot adapters + `TEMPLATE_SYNC_B.md` — honor **`optional-assumption-cleanout`**
  - `help/SCAFFOLDS.md`, `IDEA_CAPTURE_TIPS.md`, `USAGE.md` — empty Assumptions is correct; reference examples ≠ target unless clearly set
  - Modular rules + timescale rule + workflow index — one-line pointers (do not restate the gate)
  - Root `DECISIONS.md` **D17** — do not silently undo
  - Root `eval/` — `lock-obvious-assumptions` pack contract + fail-snapshot of an invented-decision Understanding
- **Step B:** Bump Master Index **Pack version** to 2.7.28 from local `VERSION`. Refresh installed modular rules (**no ask** unless `customized: true`). If `optional_rules.doc-roles` is **enabled** → refresh **understanding-author** + **docs-template-sync** adapters. **`optional-assumption-cleanout`:** present/execute per `sync.mode`. **`auto` / `auto-all`:** all Document Map Understanding stems. **`choose`:** present + ask once (default yes). Execute = Workflow §4 clean-out (lock obvious; delete invented quizzes; un-target reference examples that were not clearly set as the target; leave real forks). **Keep status** — do **not** de-confirm or inject a mid-sync shape quiz. Do **not** invent new Assumptions. Do **not** invent Understanding on `ship-first`. Do **not** rewrite user fill-in that is already category-correct.

## 2.7.27

- **Live impact:** `versions-only`, `master-index`, `content-templates`, `optional-live-reshape`, `process-docs-only`, `rules`
- **Files:**
  - `VERSION` — 2.7.26 → 2.7.27
  - Root `DECISIONS.md` — **(new)** pack decision log (CHANGELOG is archaeology; this file is “do not silently undo”). Bootstrap Step 1d **deletes** it on whole-repo copies. Not in the release zip
  - `VERSION` is the **only** pack-version number — dropped `<!-- pack-version -->` comments, hardcoded **Pack version** on templates / workflow index, README badge number, and example `local_pack_version`
  - `Feature_Understanding_Template.md` — fill-in blanks; teaching examples stay in `workflow/understanding.md`. New `help/SCAFFOLDS.md`. Compaction: re-open the workflow index then one module
  - `Feature_Spec_Template.md`, `TODO_Template.md`, `Master_Index_Template.md` §2.2, `Decision_Template.md`, `Feature_Catalog_Template.md` — same: fill-in + pointers. Human-TODO keeps inbox kinds / chat phrases; Tooling keeps tables; only the **agent** dual-write / install essays moved to playbooks
  - `agent/TEMPLATE_SYNC_B.md` — **2.7.27 instruction-footer strip** (this version’s reshape): delete copied sermons / long Instructions / inline section essays from live Understanding / spec / TODO **including stems with no Understanding**; keep user fill-in and loud phased-bridge notes; leave a short help/playbook pointer. `master-index` adopts slimmer At a Glance even if reshape is declined
  - Root `README.md` — **ship-first is first-class** (typed APIs / CRUD); `prevent` for editors / games / multi-surface. Public example: [xAIkit](https://github.com/BrianCLowe/xAIkit)
  - `workflow/profile-standing.md`, `BOOTSTRAP.md`, `ADT-settings.example.yaml`, `help/USAGE.md`, Master Index At a Glance, modular rules — same profile framing
  - Root `eval/` — fail-snapshots a wrong tree must fail (wrong-engine build, operable-gap marked done, prevent skipping Understanding, ship-first inventing Understanding, live instruction-footer left in place); `fixtures/multi-stem-studio/`; integrity grows (VERSION uniqueness, scaffold skeletons, `read_status` accepts unfilled Status enum, `DECISIONS.md`). Still what pack-checks runs
- **Step B:** Bump Master Index **Pack version** to 2.7.27 from local `VERSION` (do not copy a number into the template). If At a Glance **docs profile** still frames ship-first as a concession / “if you prefer,” adopt first-class wording (`ship-first` = typed APIs / CRUD; `prevent` = editors / games / multi-surface; unset → prevent). Refresh installed modular rules (**no ask** unless `customized: true`). **Do not** add root `DECISIONS.md` to consumer repos. If a whole-repo copy left pack `DECISIONS.md` at the project root → delete it (bootstrap Step 1d). **`master-index`:** If live At a Glance is still a policy dump (Simplicity / Idea sources / full git-mode list / Understanding essay), replace with the template’s short pointer table (keep first-class `ship-first` / `prevent` + host-worktrees one-liner). Required when tagged — **even if reshape is declined**. **`optional-live-reshape` (2.7.27 instruction-footer strip):** present/execute per `sync.mode`. **`auto` / `auto-all`:** all Document Map stems that have spec / core TODO (**including stems with no Understanding**). **`choose`:** present + ask once (default yes). On execute → [`TEMPLATE_SYNC_B.md`](agent/TEMPLATE_SYNC_B.md) **2.7.27 Instruction-footer strip**: delete pack sermons, inline section essays, and long Instructions footers; keep What this is / contract / TODOs / loud phased-bridge notes; add the short SCAFFOLDS + playbook pointer if missing. Also run usual §4 relocate if How-it-should-work / Done when still sit on Understanding. Do **not** rewrite user fill-in. Do **not** invent stems or Understanding on `ship-first`.

## 2.7.26

- **Live impact:** `versions-only`, `process-docs-only`
- **Files:**
  - `VERSION` — 2.7.25 → 2.7.26
  - `agent/ADT-settings.example.yaml` — **omit** the `standing:` key. Comments: missing / empty is the correct default; do not invent; do not copy an empty block “to have something.” Dropped the sample bullets (they restated first-class git modes / Tooling and read as “write your own”)
  - `agent/BOOTSTRAP.md` — do not copy `standing:` from the example; **do not quiz** “any standing notes?” after 3p
  - `agent/TEMPLATE_SYNC_B.md` B0.1 — same omit-when-creating
  - `agent/workflow/profile-standing.md` — no standing quiz; do not create the key just to have a block
  - `help/USING_WITH_AGENTS.md` — bootstrap does not quiz for standing
- **Step B:** Bump Master Index **Pack version** to 2.7.26. **Do not** add `standing:` to live `ADT-settings.yaml` from the example. If live `standing.instructions` is **only** the old pack comment examples (“Examples only — delete and write your own” / squash-before-ready / milestone-pr restatement / docker-compose verify) → **delete** the `standing:` key (leave real user bullets). Do **not** invent standing. No live feature/shared scan. No second 2.7.25 relocate unless that one-shot is still in catch-up.

## 2.7.25

- **Live impact:** `versions-only`, `master-index`, `process-docs-only`, `rules`
- **Files:**
  - `VERSION` — 2.7.24 → 2.7.25
  - `agent/workflow/profile-standing.md` — **§0.2 LOOKOUT** is **playbook overrides only**: user wants to **override an ADT playbook** (git/ceremony/orchestrate/verify/re-ask). **Not a scratch pad** — do not jot random notes, how to prompt another model/API, or other-product style. Dropped “corrects how you just worked” as a capture trigger. **Sync relocate** one-shot: strip misplaced standing bullets into the relevant live doc
  - `agent/TEMPLATE_SYNC_B.md` — standing-relocate one-shot may open §0.2 + the **one** named destination (not a live scan)
  - `agent/ADT-settings.example.yaml` — same scope on the `standing:` comment
  - `agent/Modular_Documentation_Rule.mdc` / `.instructions.md` — always-on lookout + after-changes + philosophy: playbook overrides, not a notes pad
  - `agent/Modular_Docs_Workflow.md`, `BOOTSTRAP.md`, `roles/orchestrator.md`, `roles/feature-implementer.md` + adapter-src + regenerated adapters — same
  - `workflow/decisions.md`, `Master_Index_Template.md`, `help/*`, root `README.md` — standing = playbook override, not freeform process notes
- **Step B:** Bump Master Index **Pack version** to 2.7.25. If Key Locations still calls `standing.instructions` “freeform process prefs” without playbook-override scope, adopt the template wording. Refresh installed modular rules (**no ask** unless `customized: true`). If `optional_rules.doc-roles` is **enabled** → refresh `feature-implementer` adapters from this pack. **Standing relocate (this version only):** open `docs/ADT-settings.yaml` → `standing.instructions` only (skip if empty/missing/comment-only). **Keep** bullets that **override an ADT playbook** (or promote to a first-class key and drop — **only** when that key is unset or already matches; do **not** overwrite a different set `docs_profile` / `orchestrator.git.mode` / `sync.mode` or stamp `source: user` on that overwrite). **Move then delete** the rest into the relevant live doc — do not leave a copy in standing. Procedure: Workflow [§0.2 Sync relocate](agent/workflow/profile-standing.md#02-standing-workflow-instructions-user-workflow-not-pack-enums). **Do not** invent standing content, a new map row, or a live feature/shared scan. Open only the one destination named by a misplaced bullet.

## 2.7.24

- **Live impact:** `versions-only`, `master-index`, `process-docs-only`, `rules`
- **Files:**
  - `VERSION` — 2.7.23 → 2.7.24
  - `agent/roles/orchestrator-git.md` — **Host worktrees** (not a settings key): detect linked/host worktree and **stay**; do not checkout default in that tree; dirty-WIP hard-stop is **this tree** only; concurrent implementers require **host isolation** (else serial); pack does **not** `git worktree add`. **`milestone-pr` cycle 10–11:** main checkout still returns to default; host worktree skips that checkout and starts the next branch with `git checkout --no-track -b` from `origin/<default>` (plain `-b` from `origin/<default>` would track default; first push `-u` to the new name)
  - `agent/roles/orchestrator.md` — parallel only when host can isolate; brief child cwd; do not return-to-default inside a host worktree
  - `agent/tools/*.md` — **Host isolation** per harness (Cursor / Grok / Copilot / Claude can isolate; OpenClaw / Continue / Cline / `AGENTS.md` → serial)
  - `agent/roles/feature-implementer.md` + `work-verifier.md` + `adapter-src` + regenerated cursor/grok/copilot adapters — honor briefed host cwd; do not create/remove worktrees
  - `agent/BOOTSTRAP.md` Step 3p **E**, `agent/TEMPLATE_SYNC_B.md` B0.6, `agent/ADT-settings.example.yaml`, `agent/workflow/profile-standing.md`, `Master_Index_Template.md`, `help/*`, `roles/README.md`, `workflow/todos.md`, root `README.md` — host-worktree wording; no new quiz; do not invent a worktrees key
- **Step B:** Bump Master Index **Pack version** to 2.7.24. If At a Glance **orchestrator git** lacks the **host worktrees** note (already-in-a-worktree → stay; pack does not create trees; concurrent needs host isolation), adopt it. **Do not** add `orchestrator.git.worktrees`. **Do not** migrate an already-set `orchestrator.git.mode`. If `optional_rules.doc-roles` is **enabled** → refresh `feature-implementer` + `work-verifier` adapters from this pack (**no ask** unless `customized: true`). No live feature/shared scan.

## 2.7.23

- **Live impact:** `versions-only`, `process-docs-only`, `rules`
- **Files:**
  - `VERSION` — 2.7.22 → 2.7.23
  - `agent/roles/adapter-src/manifest.json` — add `copilot` harness
  - `agent/roles/copilot/*.agent.md` — **(new)** Copilot CLI / Agents window / Chat adapters (`name` + `description` only; no `model: inherit`)
  - `agent/GENERATE_ROLE_ADAPTERS.md`, `roles/adapter-src/README.md` — generate `roles/copilot/<role>.agent.md`
  - Root `scripts/gen_role_adapters.py` — `.agent.md` extension for copilot
  - `agent/tools/github-copilot.md` — doc-roles install → `.github/agents/` (was Install None)
  - `agent/Modular_Documentation_Rule.mdc` / `.instructions.md` — look up `<name>.agent.md` under `.github/agents/`; do not treat `.cursor/agents/` as Copilot types
  - `agent/roles/README.md`, `agent/tools/README.md`, `agent/RULE_INSTALL.md`, `agent/TEMPLATE_SYNC_A.md` / `_B.md`, `agent/ADT-settings.example.yaml`, `agent/tools/agents-md.md` / `openclaw.md` / `cursor.md` / `grok-build.md`, `help/USING_WITH_AGENTS.md`, `help/SETUP.md` — Copilot path + Chat vs Agents window session note
- **Step B:** Bump Master Index **Pack version** to 2.7.23. **Update and refresh** installed modular + timescale + build-verify rules from this pack (**no ask** unless `customized: true`). If `optional_rules.doc-roles` is **enabled** and `tools.github-copilot.status: installed` → install/refresh seven `.github/agents/*.agent.md` from `roles/copilot/` (this version adds that folder — older packs had no Copilot agents-folder install). Do **not** copy `roles/cursor/` into `.github/agents/`. If doc-roles is **declined**, leave it. If **missing/unset**, ask once (do **not** stay silent). OpenClaw/Continue/Cline still have no adapters. No live feature/shared scan.

## 2.7.22

- **Live impact:** `versions-only`, `process-docs-only`
- **Files:**
  - `VERSION` — 2.7.21 → 2.7.22
  - `agent/BOOTSTRAP.md` Step 1b — delete upstream `.github/FUNDING.yml` (`github: BrianCLowe`) on whole-repo / “Use this template” copies; do **not** wipe all of `.github/` or the user’s own funding file
  - `help/SETUP.md`, root `CONTRIBUTING.md` — same list
- **Step B:** Bump Master Index **Pack version** to 2.7.22. If a whole-repo copy left `.github/FUNDING.yml` with `github: BrianCLowe` / Agentic Doc Templates comments → **delete that file**. Do **not** delete the user’s own funding file. No live feature/shared scan. Rules refresh not required.

## 2.7.21

- **Live impact:** `versions-only`, `master-index`, `process-docs-only`
- **Files:**
  - `VERSION` — 2.7.20 → 2.7.21
  - `agent/roles/orchestrator-git.md` — **`milestone-pr` miss:** a milestone is **not** one TODO / one implementer. Group related TODOs on one PR; spawn **concurrent implementers** when work does not overlap; **squash the whole milestone before mark ready** so tip-only bots see the cut. Still one open PR at a time; still do not dump the whole night into one PR
  - `agent/roles/orchestrator.md` — partition names the milestone; parallel implementers when items do not share files; PR cycle runs when the **named milestone** is complete, not after the first unit
  - `agent/BOOTSTRAP.md` Step 3p **E**, `agent/TEMPLATE_SYNC_B.md` B0.6, `agent/ADT-settings.example.yaml`, `agent/workflow/todos.md`, `roles/README.md`, `Master_Index_Template.md`, `help/*`, root `README.md` — same wording
- **Step B:** Bump Master Index **Pack version** to 2.7.21. If At a Glance **orchestrator git** still reads as one-TODO / serial-only per-slice PRs, adopt **per-milestone** (several related TODOs + concurrent implementers when they do not overlap; squash before ready). **Do not** migrate an already-set `orchestrator.git.mode`. No live feature/shared scan. Rules refresh not required (orchestrator is parent playbook only).

## 2.7.20

- **Live impact:** `versions-only`, `process-docs-only`
- **Files:**
  - `VERSION` — 2.7.19 → 2.7.20
  - `agent/TEMPLATE_SYNC_B.md` B0.6 — already-set git mode stays; **user ask this turn** may rewrite + `source: user`. That is **not** a pack migrate
  - `agent/ADT-settings.example.yaml` — **Reviewers / Bugbot:** do not fail a durable `orchestrator.git.mode` change when `source: user`
  - `agent/roles/orchestrator-git.md`, `roles/template-sync.md` + adapter — same exception
- **Step B:** Bump Master Index **Pack version** to 2.7.20. **Do not** migrate an already-set `orchestrator.git.mode` just because the pack now recommends `milestone-pr` (cloud this-run still does not write the file). **Exception — reviewers / Bugbot:** if this PR changes `orchestrator.git.mode` **and** stamps `source: user` (or the user said *Set orchestrator git to …* / asked to change that setting on this PR), that is **user-directed**. Do **not** fail, revert, or treat it as a forbidden sync migrate. If live `ADT-settings.yaml` lacks that reviewer note next to `orchestrator.git`, add the comment from the example (do **not** change the mode). No live feature/shared scan. Rules refresh not required.

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
- **Step B:** Bump Master Index **Pack version** to 2.7.19. Adopt At a Glance **orchestrator git** recommend **`milestone-pr`** + Cloud Agent this-run note if missing; adopt **inventory stem** / covering-TODOs wording on At a Glance idea-sources if missing. **Do not** migrate existing live `orchestrator.git.mode` (including `local` / `branch-pr` / `branch-pr-squash`) — cloud overrides are this-run only. **Exception:** an explicit user *Set orchestrator git to …* / setting change this PR with `source: user` is **user-directed** — reviewers / Bugbot must **not** fail or revert it. **Update and refresh** installed modular + timescale rules from this pack (**no ask** unless `customized: true`). **`optional-todo-kit-coverage`:** present/execute per `sync.mode` — for each Document Map stem, if the **spec already names** in-scope leftover surfaces with no covering TODO (**open or Completed** on **this** stem), add items on that stem (no new map rows; do not resurrect Completed). If Overview claims wrap-the-vendor-API but the spec lists no leftovers, add **one** research TODO (diff vendor docs next session) — do **not** fetch vendor APIs during sync. Under **`choose`:** ask once (default all stems). Under **`auto` / `auto-all`:** all Document Map `*-TODO.md`. Todo-warden does not replace this pass. Orchestrator playbooks are parent-only (no adapter).

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
