# Template Sync B — Update live docs

> **Step B only.** Open this file **after** [`TEMPLATE_SYNC_A.md`](TEMPLATE_SYNC_A.md) finishes (or the user already refreshed `docs/templates/`). Do not open this file before the pack overwrite.

Source of truth is **on disk** under `docs/templates/`. Do **not** re-fetch from GitHub for each live file. Do **not** apply this checklist from a playbook you only read before Step A.

---

## B0 — Scope gate *(do this first — every sync)*

1. Confirm Step A completed (or pack was already refreshed) and you opened **this** file from disk after that.
2. Read **local** `docs/templates/VERSION` (`pack-version` = **to**). Older dual `template-version` / `workflow-version` lines → treat either as `pack-version`.
3. **Migrate settings** *(if needed)* — see **B0.1** below. Then capture **from** *(before any upstream stamp)*:
   - Prefer `docs/ADT-settings.yaml` → `upstream.local_pack_version` (or legacy `local_template_version`)
   - Else live `Master_Index.md` **Pack version** (or legacy Template/Workflow version)
   - Else **from** is unset (first sync)
4. **Select changelog entries** — see **Catch-up** below. Union their **Live impact** tags. Skim each selected entry’s **Step B** line only for one-shots not already covered by tags.
5. Do **only** the actions implied by the **unioned tags** + those skimmed Step B one-shots. Run the gated checklist **once** (do not walk each version as its own sync). Bump **Pack version** once to **to**.
6. If `CHANGELOG.md` is missing: fall back to comparing **content-template paths only** (`Feature_*_Template.md`, `TODO_Template.md`, `Tooling_Template.md`, `Human_TODO_Template.md`, `Decision_Template.md`) via `git diff` against HEAD or a prior pack copy. Never open all live feature docs “just in case.”

### Catch-up *(version jumps)*

Compare semver `X.Y.Z` numerically (major, minor, patch).

| Case | Entries to use |
|------|----------------|
| **from** unset | **Top entry only** (first sync) |
| **from** ≥ **to** | **Top entry only** (same-version re-sync) |
| **from** < **to** | Every `## X.Y.Z` heading where **from** < version ≤ **to**. If that set is empty → top entry only |

**Union tags** from all selected entries. Then:

- Apply the gated checklist **once** for the union (not once per release).
- If the union includes any of `content-templates`, `optional-live-reshape`, `optional-todo-ambition`, `optional-todo-operable`, or `optional-todo-kit-coverage`, run those steps even when newer selected entries also list `process-docs-only` (`process-docs-only` on one release does not cancel live passes from skipped releases).
- Skim Step B lines from selected entries for tips / one-shots not expressed by tags (e.g. Human-TODO tip refresh). Do **not** invent a broader audit than the unioned tags + those lines.
- Do **not** bump Pack version through intermediate numbers — set it once to **to**.

| Live impact tag | Do in Step B |
|-----------------|--------------|
| `versions-only` | Bump **Pack version** in live `Master_Index.md` |
| `master-index` | Adopt structural deltas from `Master_Index_Template.md` into live index (see below) |
| `content-templates` | Add *missing* sections/structure only — **not** trim/remove (reshape is a separate tag) |
| `optional-live-reshape` | Live Understanding shape trim + relocate — **`auto` / `auto-all`:** run all stems; **`choose`:** present + ask once |
| `optional-todo-ambition` | Live TODO ambition pass — **`auto` / `auto-all`:** run all Document Map TODO stems; **`choose`:** present + ask once |
| `optional-todo-operable` | Live TODO operable dual-track pass — **`auto` / `auto-all`:** all Document Map TODO stems; **`choose`:** present + ask once |
| `optional-todo-kit-coverage` | Live TODO kit-coverage pass (Workflow §5.4) — **`auto` / `auto-all`:** all Document Map TODO stems; **`choose`:** present + ask once |
| `rules` | Refresh installed rules/adapters from local `agent/` (see Rules step — **no ask** unless `customized: true`) |
| `optional-upstream-check` | Stamp `upstream:` in `docs/ADT-settings.yaml` if update-check enabled; offer enable if unset |
| `process-docs-only` | No live feature/shared content scan **for that release alone** — still honor live-content tags from other selected catch-up entries |

**Default when `content-templates`, `optional-live-reshape`, `optional-todo-ambition`, `optional-todo-operable`, and `optional-todo-kit-coverage` are absent from the union:** bump versions + Master Index structure if tagged → rules if tagged → summarize → **present unset options** (below). **Do not** open live `features/` or `_shared/` docs.

### B0.1 — Settings file *(migrate once, then use forever)*

**Live:** `docs/ADT-settings.yaml`  
**Example:** [`ADT-settings.example.yaml`](ADT-settings.example.yaml)

1. If `docs/ADT-settings.yaml` **exists** → use it (skip migration).
2. Else if `docs/rule-install-status.yaml` and/or `docs/upstream-status.yaml` exist → **merge** into `docs/ADT-settings.yaml`:
   - Copy `tools` + `optional_rules` from rule-install-status.
   - Map upstream-status → `upstream:` (`local_template_version` / `local_workflow_version` → `local_pack_version`; keep `last_checked`, `update_available`, `check_interval_days`, map `upstream_template_version` → `upstream_pack_version`).
   - **Do not** invent `check_mode` or `check_mode_recorded` here — B0.4 asks (legacy weekly days are a hint only).
   - If `sync.mode` missing → leave unset (B0.2 will ask).
   - Write `ADT-settings.yaml`, then **delete** the old status file(s). Note migration in the end summary.
3. Else → create `ADT-settings.yaml` from the example when first recording a tool/optional/sync decision (do not invent installs).

### B0.2 — Sync mode *(ask once if unset)*

Read `sync.mode` from `docs/ADT-settings.yaml`.

| Mode | Behavior |
|------|----------|
| **`auto`** | Apply all changelog-gated live work without mid-sync optionals quiz: versions, master-index, content-templates (missing only), **optional-live-reshape** (all Document Map Understanding stems), **optional-todo-ambition** / **optional-todo-operable** / **optional-todo-kit-coverage** (all Document Map `*-TODO.md` when tagged), rules refresh, upstream stamp. **Also** perform **post-sync hygiene commits** (below) without asking. Still **ask once** for brand-new unset `optional_rules.*`. Summarize at end (include commit subjects). |
| **`auto-all`** | Same as **`auto`**, and also **enable + install** any unset `optional_rules.*` (doc-roles, update-check, future optionals) without asking. Never re-enable **`declined`**. New update-check → `check_mode: always` + record cadence (skip B0.4 ask). Summarize what was auto-enabled. |
| **`choose`** | Present reshape / TODO ambition / TODO operable / TODO kit-coverage (and similar future optional live tags) each sync — ask once per tagged pass. Suggest (do not force) separate commits; commit only if they explicitly ask. |
| **missing / unset** | **Ask once** before the first optional live pass (or before stopping if none tagged): *Recommended live updates automatically (`auto`), everything including new pack optionals (`auto-all`), or ask each sync (`choose`)?* Record `sync.mode` + `sync.recorded`. Then continue under that mode. Do **not** silent-default. |

Explicit later: *Set sync to auto* / *Set sync to auto-all* / *Set sync to choose*.

### B0.3 — Post-sync git hygiene *(after A0 cleared)*

**Pre-sync dirty tree** is handled in [`TEMPLATE_SYNC_A.md`](TEMPLATE_SYNC_A.md) A0 — hard stop; never auto-commit unknown WIP.

**After** pack overwrite + Step B edits, under **`sync.mode: auto`** or **`auto-all`** (git repo only):

1. **Pack / stamp commit** — after versions + rules refresh + settings/upstream stamps (and master-index / content-templates if tagged), if the tree is dirty with sync output → **commit** (no ask). Message like pack sync / version bump — match repo style. **No push** unless they already granted push for this sync.
2. **Reshape commit** — if `optional-live-reshape` ran, commit those live Understanding/spec(/TODO) edits separately when dirty.
3. **TODO ambition commit** — if `optional-todo-ambition` ran, commit those TODO rewrites separately when dirty.
4. **TODO operable commit** — if `optional-todo-operable` ran, commit those dual-track / exercise-path TODO edits separately when dirty (may combine with ambition in one commit if both ran the same stems).
5. **TODO kit-coverage commit** — if `optional-todo-kit-coverage` ran, commit those covering-TODO edits separately when dirty (may combine with other TODO live passes if the same stems).

Invoking sync with `auto` or `auto-all` is an **implicit grant** for these **local** hygiene commits for this run only. It does **not** authorize push or committing unrelated WIP.

Under **`choose`:** recommend the same split commits; ask; never `git commit` unless they explicitly ask.

### B0.4 — Update-check cadence *(ask once if unset)*

If `optional_rules.template-update-check.status` is **`enabled`** and `upstream.check_mode_recorded` is **missing** (or `check_mode` itself is missing):

Under **`sync.mode: auto-all`:** set `check_mode: always` + `check_mode_recorded` today (no ask). Keep existing `interval` + days if already set.

Otherwise **ask once** (do not silent-default; do not skip under `sync.mode: auto`):

> Template update checks are on. Check for a newer pack **every session** (`always` — recommended; negligible token cost), or only every **N days** (`interval`, default 7 if they had a weekly stamp)?

Record:

- `upstream.check_mode`: `always` or `interval`
- `upstream.check_interval_days` when interval (keep prior days if present, else **7**)
- `upstream.check_mode_recorded`: today

If update-check is **declined** or unset → skip B0.4 (step 10 may enable it — under `auto`/`choose` ask cadence in the same turn; under `auto-all` default `always`).

Explicit later: *Check for template updates every session* / *Only check every week*.

### B0.5 — Docs profile *(ask once if unset)*

Read `docs_profile.mode` from `docs/ADT-settings.yaml`.

| State | Behavior |
|-------|----------|
| **`prevent` / `balanced` / `ship-first`** | Keep; no re-ask |
| **missing / unset** | **Ask once** before stopping (do not silent-default to invent ship-first). Runtime already treats unset as **prevent** for coding gates. |

**Ask** (brief; optional 1-line suggest if `docs/reference/` or live Understandings give a signal):

> Docs profile controls Understanding ceremony (Workflow §0.1):
> - **`prevent`** — Understanding + shape confirm before code (current default if unset)
> - **`balanced`** — Understanding only when identity is ambiguous
> - **`ship-first`** — Spec + TODO only; fix-forward
>
> Keep **prevent**, or switch?

Record `docs_profile.mode` + `recorded` (+ `source: user` or `agent-suggested`). Explicit later: *Set docs profile to …*.

Under **`sync.mode: auto-all`:** if unset, set **`prevent`** + `recorded` today (no quiz) — never invent `ship-first` without a user choice.

### B0.6 — Orchestrator git mode *(always ask if unset — including auto-all)*

Read `orchestrator.git.mode` from `docs/ADT-settings.yaml`.

| State | Behavior |
|-------|----------|
| **`local` / `milestone-pr` / `branch-pr` / `branch-pr-squash` / `branch-push` / `current-push` / `none`** | **Keep the exact value; no re-ask.** Do **not** rewrite to `milestone-pr` because it is now recommended. **This-turn exception:** user said *Set orchestrator git to …* / asked to change this setting → record the new mode + `recorded` today + **`source: user`**. That is **user-directed**, not a pack migrate. **Reviewers / Bugbot:** do **not** fail or revert a mode change that stamps `source: user`. |
| **missing / unset** | **Always ask once before stopping** — even under **`sync.mode: auto-all`**. Git strategy is high-impact. **Never** silent-default **`current-push`** or invent a mode without a user answer. |

**Present and explain** the full menu (bootstrap Step 3p **E** wording):

| Mode | One-line |
|------|----------|
| **`milestone-pr`** | **Overnight:** each milestone (several related TODOs OK; concurrent implementers when they do not overlap) → own PR → **squash before ready** → wait CI/Bugbot → **merge** → next branch |
| **`branch-pr-squash`** | One run branch → end: **build-verify → squash whole run → mark ready** (no merge; one morning PR) |
| **`branch-pr`** | Same without squash (keeps milestone history; no merge) |
| **`branch-push`** | Branch → commits → push; no PR |
| **`local`** | Commits only; no push |
| **`current-push`** | Commit + push **whatever branch you are on** (often `main`); solo opt-in only |
| **`none`** | No commits |

Recommend: remote + forge CLI → **`milestone-pr`** (overnight drain: per-milestone PR — several related TODOs + concurrent implementers when they do not overlap; squash before ready; CI/Bugbot; merge; next branch); offer **`branch-pr-squash`** for one PR / human merges in the morning; offer **`branch-pr`** to keep history on one PR; remote, no CLI → still offer **`milestone-pr`** (with install ask) or **`branch-push`**; else **`local`**. Record choice + `recorded` (+ `source`). Explicit later: *Set orchestrator git to …*. **Note (do not re-ask):** a later **Cloud Agent** orchestration this-runs **`milestone-pr`** if durable stays `local` / `none` / `branch-pr-squash` / etc. — see [`roles/orchestrator-git.md`](roles/orchestrator-git.md); sync does not need a second key.

**After the mode is recorded** → **Forge tooling probe** ([`roles/orchestrator-git.md`](roles/orchestrator-git.md)): if **`milestone-pr` / `branch-pr` / `branch-pr-squash`** and CLI missing → ask to install; if not authenticated → **ask to start login** (install alone is not enough). Fall back / switch mode if they decline. Do not silent-install or silent-login.

**Do not** under `auto-all` write `local` (or any mode) and move on without an explicit user pick. If they say “defaults,” treat that as accepting the **stated recommendation** and record it **loudly** in the sync summary: *“Recorded orchestrator.git = X (your default). Other options: …”*. Do **not** stamp `source: user` unless they picked the mode this turn.

### Reference — local template → live file *(only when tagged)*

| Local template (read) | Live file (edit carefully) | When |
|-----------------------|----------------------------|------|
| `Master_Index_Template.md` | `docs/Master_Index.md` — never blind-replace | `master-index` or always for version lines |
| `agent/Modular_Docs_Workflow.md` + `agent/workflow/` | Already replaced in Step A — do not copy into Master_Index | — |
| `Feature_Understanding_Template.md` | Each `*-Understanding.md` — add *missing* sections only | `content-templates` |
| `Feature_Understanding_Template.md` + `agent/workflow/understanding.md` §4 | Each chosen `*-Understanding.md` — **trim** non-shape sections; **relocate** into that stem’s spec; refresh banner/Instructions | `optional-live-reshape` **and** (`auto` / `auto-all` **or** user said yes) |
| `Feature_Spec_Template.md` | Each feature/shared `.md` spec — add missing sections only; receive relocated contract on reshape | `content-templates` / reshape executing |
| `TODO_Template.md` | Each `*-TODO.md` — add missing blocks only | `content-templates` |
| `TODO_Template.md` + Workflow §5 + `Agent_Timescale_Planning_Rule.mdc` | Chosen `*-TODO.md` (+ Understanding for shape) — streamline High Priority / Current focus | `optional-todo-ambition` **and** (`auto` / `auto-all` **or** user said yes) |
| `TODO_Template.md` + Workflow §5.3 | Chosen `*-TODO.md` (+ Understanding/spec for surface identity) — add exercise-path rows or **library-only** labels | `optional-todo-operable` **and** (`auto` / `auto-all` **or** user said yes) |
| `TODO_Template.md` + Workflow §5.4 | Chosen `*-TODO.md` + matching spec — covering TODOs for spec-named leftovers; one research item if spec is thin | `optional-todo-kit-coverage` **and** (`auto` / `auto-all` **or** user said yes) |
| `Tooling_Template.md` | `docs/Tooling.md` — create if missing; add sections only | `content-templates` |
| `Human_TODO_Template.md` | `docs/Human-TODO.md` — create if missing; add columns/sections only | `content-templates` |
| `agent/Modular_Documentation_Rule.*` | Installed rule paths — refresh via each `tools/<key>.md` for `status: installed` tools | `rules` |
| `agent/Agent_Timescale_Planning_Rule.*` | Core timescale rule — install/refresh with modular rule via each `tools/<key>.md` | `rules` |
| `agent/Agent_Build_Verify_Rule.*` | Core build/verify rule — install/refresh with modular rule via each `tools/<key>.md` | `rules` |
| `agent/Template_Update_Check_Rule.*` | Optional update-check — same dispatch | `rules` or `optional-upstream-check` |
| `agent/tools/*.md` | Install/sync adapters — open only for tools already `installed` | `rules` |
| `agent/roles/cursor/*.md` / `agent/roles/grok/*.md` / `agent/roles/copilot/*.agent.md` | Optional subagents — via tool playbooks | `rules` when `optional_rules.doc-roles` is `enabled` |

Versions:

- `docs/templates/VERSION` → **`pack-version`** → live `Master_Index.md` **Pack version** (and `<!-- pack-version -->` if present)
- Legacy live **Template version** / **Workflow version** lines → **replace** with a single **Pack version** line from `VERSION` (do not keep both systems)

### Gated checklist

1. **Versions** — Set **Pack version** in live `Master_Index.md` from local `VERSION`. Remove obsolete Template/Workflow version lines when present. Update `<!-- pack-version -->` if present (or replace `<!-- template-version -->`).
2. **Master Index** *(if `master-index`)* — Read local `Master_Index_Template.md` + live `Master_Index.md`. Compare **headings / Key Locations / Document Map columns** only — not project prose. **Preserve** overview, Project Profile, Document Map rows (§3.0–3.4), user §3.0 exceptions, custom sections. **Adopt** new index sections, renumbers, Quick Start pointer, Key Locations row for `docs/ADT-settings.yaml` (remove stale `rule-install-status.yaml` / `upstream-status.yaml` rows if present). Update links from `templates/Modular_Docs_Workflow.md` → `templates/agent/Modular_Docs_Workflow.md` if still on the old path. §3.0: record only **user-stated** exceptions.
3. **Content templates** *(if `content-templates`)* — Add **missing** sections/structure from local templates into live Understanding / Spec / TODO / Tooling / Human-TODO. Do **not** remove or reshape existing sections here. Create `Tooling.md` / `Human-TODO.md` from templates when missing and link from Master Index.
4. **Live Understanding reshape** *(if `optional-live-reshape`)* —
   - **`sync.mode: auto` or `auto-all`:** execute for **all Document Map Understanding stems** (no ask). After pack/stamp hygiene commit (B0.3) when applicable; reshape gets its own commit after execute (B0.3).
   - **`sync.mode: choose`:** **Present before stopping** (explain + ask once; **do not** report “skipped by design” without asking). **Highly recommended.**
     1. **Commit hygiene *(suggest)*:** Recommend committing pack sync first so reshape can be a separate commit. Ask; never `git commit` unless they explicitly ask.
     2. **Explain briefly:** Older live Understandings may still hold contract sections. **Yes (recommended)** = trim to shape-only (Workflow §4), relocate overflow into that stem’s spec, refresh banner/Instructions. **No** = leave bodies.
     3. **Ask once — default toward yes:** all Document Map Understanding stems / named / no.
   - **On execute** (`auto` / `auto-all` or yes): for each chosen stem only — open Understanding + matching spec (+ TODO if checking `[x]` per Workflow §4); **relocate, then remove**; do not invent contract detail; stop after chosen stems.
5. **Live TODO ambition** *(if `optional-todo-ambition`)* —
   - **`sync.mode: auto` or `auto-all`:** execute for **all Document Map `*-TODO.md` stems** (no ask); commit per B0.3 after.
   - **`sync.mode: choose`:** present + ask once (default all stems / named / no); suggest separate commit; commit only if they ask.
   - **On execute:** for each stem — open TODO + Understanding; merge interim-architecture staging into target-architecture High Priority; keep real blockers; refresh Current focus; do **not** invent **out-of-kit** work. Covering TODOs for in-scope spec surfaces is Workflow §5.4 (not inventing).
5b. **Live TODO operable** *(if `optional-todo-operable`)* —
   - **`sync.mode: auto` or `auto-all`:** execute for **all Document Map `*-TODO.md` stems** (no ask); commit per B0.3 after.
   - **`sync.mode: choose`:** present + ask once (default all stems / named / no); explain Workflow §5.3 dual-track; suggest separate commit; commit only if they ask.
   - **On execute:** for each stem — open TODO + Understanding/spec (Overview, Acceptance, surface identity) + Master Index product surface if needed. If user/operator-facing and High Priority has **no** exercise path (UI / CLI / product API / documented smoke) → **add** surface/wire/smoke items (**scaffold + wire** minimal boring surface when UI was never specified) **or** a loud phased bridge (`library foundation first · exercise path: …`) only when domain-before-surface is intentional; refresh Current focus when the next work should be the path. If open **operable Acceptance** has no open TODO that addresses those lines → add matching work items (or phase). If pure foundation → one **library-only** note (TODO or Current focus). Do **not** invent “await UI design” for blank canvas, invent unrelated backlog, rewrite domain items, force UI onto library stems, or dual-maintain every Acceptance line as a TODO twin.
5c. **Live TODO kit coverage** *(if `optional-todo-kit-coverage`)* —
   - **`sync.mode: auto` or `auto-all`:** execute for **all Document Map `*-TODO.md` stems** (no ask); commit per B0.3 after.
   - **`sync.mode: choose`:** present + ask once (default all stems / named / no); explain Workflow §5.4 (spec-named leftovers get TODOs on **existing** stems; terse wrap-the-API is not a stub; no new map rows); suggest separate commit; commit only if they ask.
   - **On execute:** for each stem — open that spec + **this stem’s** `-TODO.md` only (no vendor-doc fetch; do **not** open other stems). **Covering** = an open **or Completed** `[x]` item on **this** TODO that addresses the leftover (do not resurrect shipped methods). If the spec **already names** in-scope leftover surfaces (Behavior / Architecture leftover list) with **no** covering item on this TODO → **add** Medium items on **this** stem (High only if Current focus is empty and this is the next winner). If Overview/identity claims wrap-the-vendor-API (or equivalent) but the spec lists **no** leftover surfaces and this TODO has **no** open or Completed research item → add **one** Medium item: *Diff vendor API docs vs this kit; add covering TODOs (Workflow §5.4)* — next-session research, not this sync. Do **not** create Document Map rows; do **not** invent playground/UI/out-of-kit APIs; do **not** split stems; do **not** implement code.
6. **Rules** *(if `rules`)* — For each tool with `tools.*.status: installed` in `docs/ADT-settings.yaml`, open **only** `docs/templates/agent/tools/<key>.md` and refresh that harness.
   - **Default:** refresh pack-managed modular + timescale + **build-verify** rules (and enabled optionals) **without asking** — installed means pack-owned.
   - **Ask before overwrite only if** that tool entry has `customized: true` (or an explicit note that pack rule bodies were hand-edited).
   - If `optional_rules.doc-roles` is `enabled`, refresh that tool’s agents folder (seven adapters including `todo-warden`; **no** `orchestrator` adapter).
   - Remove any stale `.cursor/skills/modular-docs-*` leftovers from older pack drafts (ask first only if deleting user-looking paths outside known leftovers).
7. **Upstream stamp** *(if `optional-upstream-check` or update-check enabled)* — If `optional_rules.template-update-check.status` is `enabled`: ensure `upstream:` exists; set `local_pack_version` from local `VERSION`, `last_checked` today, clear `update_available` / stale `upstream_pack_version`. Do **not** delete `ADT-settings.yaml`. Refresh optional update-check rules if tagged `rules` / body changed (same customized rule as above).
8. **Layout migration** — Run [`BOOTSTRAP.md`](BOOTSTRAP.md) Step 0b **only** if layout markers show older layout (`docs/help/` or `docs/agent/` at docs root, or flat setup files in `templates/`). Skip on a normal modern pack refresh.
9. **Summarize** pack refresh + live-doc updates + sync mode used + catch-up **from→to** (or top-entry-only) + reshape / TODO ambition / TODO operable / TODO kit-coverage executed or (choose) offered/declined + settings migration if any + **git** (A0 preflight outcome; hygiene commits made or skipped; push status — default not pushed).
10. **Present / apply unset options** *(every sync — before stopping)* — Users cannot ask for what they were never told exists. Read `docs/ADT-settings.yaml`. For each known pack optional (`optional_rules.template-update-check`, `optional_rules.doc-roles`, plus any **new** optional named in selected catch-up entries / Step B):
   - **`declined`** → do not re-ask or re-enable; a one-line “still off” note is enough.
   - **`enabled`** → already handled by refresh steps above; no re-pitch of the feature — but if update-check is enabled and cadence was never recorded, **B0.4** still applies.
   - **missing / unset** under **`sync.mode: auto-all`:** **enable + install** without asking (record `enabled` + `recorded` today). For `template-update-check`: ensure `upstream:`, set `local_pack_version`, `check_mode: always`, `check_mode_recorded` today. For `doc-roles` (and any optional with install artifacts): run each installed tool’s `tools/<key>.md` optional section. Note auto-enabled items in the summary. Never treat this as license to flip **`declined`** → enabled.
   - **missing / unset** under **`auto`** or **`choose`:** **briefly explain** + **ask once** (yes / no / later). On **yes** for `template-update-check`, also run **B0.4** cadence ask in the same turn before stopping. On yes/no, record `enabled` or `declined`. Do **not** enable silently. Do **not** treat unset as silent no.
   - Under **`sync.mode: auto`:** changelog-tagged **live passes** (reshape, ambition, …) are already covered by auto — those are not “new optionals.” Cadence (B0.4) is still asked when due.
11. If `sync.mode` still unset after the above → run **B0.2** before stopping.
12. If update-check is enabled and `check_mode_recorded` still missing → run **B0.4** before stopping (`auto-all` defaults `always` there).
13. If `docs_profile.mode` still unset → run **B0.5** before stopping (`auto-all` defaults `prevent` there).
14. If `orchestrator.git.mode` still unset → run **B0.6** before stopping (**always ask**, including under `auto-all` — never invent `current-push` or silent-write `local`).

### Do not (Step B)

- Open or follow this file before Step A / pack refresh completes
- Run Step B from a pre–Step A in-memory copy of any sync playbook
- Capture versions before Step A overwrite
- Scan every live Understanding / Spec / TODO unless `content-templates` or (`optional-live-reshape` and executing) or (`optional-todo-ambition` and executing) or (`optional-todo-operable` and executing) or (`optional-todo-kit-coverage` and executing)
- Treat `content-templates` as permission to trim/remove Understanding sections — that requires `optional-live-reshape` + execute
- Under **`choose`:** omit the reshape / TODO ambition / TODO operable / TODO kit-coverage ask when those tags are present
- Under **`auto` / `auto-all`:** re-ask for reshape / ambition / operable / kit-coverage / rules refresh when tags say to run them
- Under **`auto` / `auto-all`:** skip B0.3 hygiene commits when sync produced a dirty tree (unless not a git repo)
- Auto-commit **pre-sync** WIP (A0) or push without an explicit grant
- Ask before refreshing installed rules unless `customized: true`
- On reshape execute: add template headings only and leave obsolete Understanding sections in place
- On TODO ambition execute: invent work, expand scope, or collapse real human/shared blockers
- On TODO operable execute: invent unrelated backlog, force UI onto **library-only** stems, or rewrite domain items beyond adding exercise-path / library-only labels
- On TODO kit-coverage execute: fetch vendor APIs, create new map rows, split stems, invent playground/out-of-kit surfaces, implement code, or re-open leftovers that already have **Completed** covering items
- Keep writing `docs/rule-install-status.yaml` or `docs/upstream-status.yaml` after migration
- Reconstruct whether a missing section is “new in this version” vs “never adopted” when content templates are unchanged — the changelog already answered
- Treat a missing or empty `docs/templates/agent/upstream/` as an error or reason to re-download attribution files
- Open Workflow, help guides, or the whole pack catalog during sync (open Workflow §4 only while executing reshape; Workflow §5 / timescale rule only while executing TODO ambition, TODO operable, or TODO kit-coverage)
- Keep pulling from GitHub — work from the **local** `docs/templates/` copy
- Under **`auto` / `choose`:** skip presenting unset `optional_rules.*` because “do not auto-enable” — that means ask, not stay silent
- Under **`auto-all`:** leave unset `optional_rules.*` unset — enable + install them (except **`declined`**)
- Silent-set `check_mode` from legacy `check_interval_days` without B0.4 (except **`auto-all`** defaulting `always` when cadence is missing)
- Skip B0.4 when update-check is enabled but `check_mode_recorded` is missing under `auto` / `choose` (under `auto-all`, default `always`)
- Equate “no install artifacts for this harness” with “nothing to offer the user”
- Under **`auto-all`:** flip **`declined`** optionals back to enabled
- Read **only the top** changelog entry when **from** < **to** and intermediate `##` entries exist — **union** those entries (Catch-up above)
- Let a newer entry’s `process-docs-only` cancel `content-templates` / reshape / ambition / operable / kit-coverage tags from skipped releases in the same jump
- Walk each catch-up version as its own full sync or bump Pack version through intermediate numbers
- Rewrite an already-set `orchestrator.git.mode` because the pack now recommends `milestone-pr`, because At a Glance wording changed, or because a Cloud Agent this-runs `milestone-pr`
- Fail, revert, or treat as a forbidden migrate a durable `orchestrator.git.mode` change that stamps **`source: user`** (or the user asked to change that setting on this PR) — that is user-directed

---

## Do not

- Use **git** to update live docs (`Master_Index`, `features/`, `_shared/`).
- Blindly replace `docs/Master_Index.md` with the template.
- Copy workflow prose into live `Master_Index.md`.
- Put project feature content into `docs/templates/`.
- Remove project-only Document Map entries unless the user asks.
- Invent §3.0 exceptions for missing Understanding / TODO files.
- Diff or cherry-pick inside `docs/templates/` on Step A — **always overwrite the whole folder** (see [`TEMPLATE_SYNC_A.md`](TEMPLATE_SYNC_A.md)).

## Example user prompts

- "Update the doc templates from Agentic Doc Templates and sync our live docs."
- "We already refreshed `docs/templates/` — update our live docs from the local pack." *(skip A download; open this file)*
- "Set sync to auto." / "Set sync to auto-all." / "Set sync to choose."
