# Template Sync B — Update live docs

> **Step B only.** Open this file **after** [`TEMPLATE_SYNC_A.md`](TEMPLATE_SYNC_A.md) finishes (or the user already refreshed `docs/templates/`). Do not open this file before the pack overwrite.

Source of truth is **on disk** under `docs/templates/`. Do **not** re-fetch from GitHub for each live file. Do **not** apply this checklist from a playbook you only read before Step A.

---

## B0 — Scope gate *(do this first — every sync)*

1. Confirm Step A completed (or pack was already refreshed) and you opened **this** file from disk after that.
2. Read **local** `docs/templates/VERSION` (`pack-version`). Older dual `template-version` / `workflow-version` lines → treat either as `pack-version`.
3. **Migrate settings** *(if needed)* — see **B0.1** below.
4. Read **only the top entry** of `docs/templates/CHANGELOG.md` (Live impact, Files, Unchanged content templates, Step B).
5. Do **only** the actions implied by that entry’s tags and Step B line.
6. If `CHANGELOG.md` is missing: fall back to comparing **content-template paths only** (`Feature_*_Template.md`, `TODO_Template.md`, `Tooling_Template.md`, `Human_TODO_Template.md`, `Decision_Template.md`) via `git diff` against HEAD or a prior pack copy. Never open all live feature docs “just in case.”

| Live impact tag | Do in Step B |
|-----------------|--------------|
| `versions-only` | Bump **Pack version** in live `Master_Index.md` |
| `master-index` | Adopt structural deltas from `Master_Index_Template.md` into live index (see below) |
| `content-templates` | Add *missing* sections/structure only — **not** trim/remove (reshape is a separate tag) |
| `optional-live-reshape` | Live Understanding shape trim + relocate — **`auto`:** run all stems; **`choose`:** present + ask once |
| `optional-todo-ambition` | Live TODO ambition pass — **`auto`:** run all Document Map TODO stems; **`choose`:** present + ask once |
| `rules` | Refresh installed rules/adapters from local `agent/` (see Rules step — **no ask** unless `customized: true`) |
| `optional-upstream-check` | Stamp `upstream:` in `docs/ADT-settings.yaml` if update-check enabled; offer enable if unset |
| `process-docs-only` | No live feature/shared content scan (versions / Master Index / rules only as other tags say) |

**Default when `content-templates`, `optional-live-reshape`, and `optional-todo-ambition` are absent:** bump versions + Master Index structure if tagged → rules if tagged → summarize → **present unset options** (below). **Do not** open live `features/` or `_shared/` docs.

### B0.1 — Settings file *(migrate once, then use forever)*

**Live:** `docs/ADT-settings.yaml`  
**Example:** [`ADT-settings.example.yaml`](ADT-settings.example.yaml)

1. If `docs/ADT-settings.yaml` **exists** → use it (skip migration).
2. Else if `docs/rule-install-status.yaml` and/or `docs/upstream-status.yaml` exist → **merge** into `docs/ADT-settings.yaml`:
   - Copy `tools` + `optional_rules` from rule-install-status.
   - Map upstream-status → `upstream:` (`local_template_version` / `local_workflow_version` → `local_pack_version`; keep `last_checked`, `update_available`, map `upstream_template_version` → `upstream_pack_version`).
   - If legacy had `check_interval_days` and no `check_mode` → set `check_mode: interval` and keep the days (preserve old weekly throttle).
   - If `sync.mode` missing → leave unset (B0.2 will ask).
   - Write `ADT-settings.yaml`, then **delete** the old status file(s). Note migration in the end summary.
3. Else → create `ADT-settings.yaml` from the example when first recording a tool/optional/sync decision (do not invent installs).

### B0.2 — Sync mode *(ask once if unset)*

Read `sync.mode` from `docs/ADT-settings.yaml`.

| Mode | Behavior |
|------|----------|
| **`auto`** | Apply all changelog-gated live work without mid-sync optionals quiz: versions, master-index, content-templates (missing only), **optional-live-reshape** (all Document Map Understanding stems), **optional-todo-ambition** (all Document Map `*-TODO.md`), rules refresh, upstream stamp. Summarize at end. |
| **`choose`** | Present reshape / TODO ambition (and similar future optional live tags) each sync — ask once per tagged pass. |
| **missing / unset** | **Ask once** before the first optional live pass (or before stopping if none tagged): *Apply recommended live updates automatically on every pack sync (`auto`), or ask about optionals each time (`choose`)?* Record `sync.mode` + `sync.recorded`. Then continue under that mode. Do **not** silent-default. |

Explicit later: *Set sync to auto* / *Set sync to choose*.

### Reference — local template → live file *(only when tagged)*

| Local template (read) | Live file (edit carefully) | When |
|-----------------------|----------------------------|------|
| `Master_Index_Template.md` | `docs/Master_Index.md` — never blind-replace | `master-index` or always for version lines |
| `agent/Modular_Docs_Workflow.md` | Already replaced in Step A — do not copy into Master_Index | — |
| `Feature_Understanding_Template.md` | Each `*-Understanding.md` — add *missing* sections only | `content-templates` |
| `Feature_Understanding_Template.md` + Workflow §4 | Each chosen `*-Understanding.md` — **trim** non-shape sections; **relocate** into that stem’s spec; refresh banner/Instructions | `optional-live-reshape` **and** (auto **or** user said yes) |
| `Feature_Spec_Template.md` | Each feature/shared `.md` spec — add missing sections only; receive relocated contract on reshape | `content-templates` / reshape executing |
| `TODO_Template.md` | Each `*-TODO.md` — add missing blocks only | `content-templates` |
| `TODO_Template.md` + Workflow §5 + `Agent_Timescale_Planning_Rule.mdc` | Chosen `*-TODO.md` (+ Understanding for shape) — streamline High Priority / Current focus | `optional-todo-ambition` **and** (auto **or** user said yes) |
| `Tooling_Template.md` | `docs/Tooling.md` — create if missing; add sections only | `content-templates` |
| `Human_TODO_Template.md` | `docs/Human-TODO.md` — create if missing; add columns/sections only | `content-templates` |
| `agent/Modular_Documentation_Rule.*` | Installed rule paths — refresh via each `tools/<key>.md` for `status: installed` tools | `rules` |
| `agent/Agent_Timescale_Planning_Rule.*` | Core timescale rule — install/refresh with modular rule via each `tools/<key>.md` | `rules` |
| `agent/Template_Update_Check_Rule.*` | Optional update-check — same dispatch | `rules` or `optional-upstream-check` |
| `agent/tools/*.md` | Install/sync adapters — open only for tools already `installed` | `rules` |
| `agent/roles/cursor/*.md` / `agent/roles/grok/*.md` | Optional subagents — via tool playbooks | `rules` when `optional_rules.doc-roles` is `enabled` |

Versions:

- `docs/templates/VERSION` → **`pack-version`** → live `Master_Index.md` **Pack version** (and `<!-- pack-version -->` if present)
- Legacy live **Template version** / **Workflow version** lines → **replace** with a single **Pack version** line from `VERSION` (do not keep both systems)

### Gated checklist

1. **Versions** — Set **Pack version** in live `Master_Index.md` from local `VERSION`. Remove obsolete Template/Workflow version lines when present. Update `<!-- pack-version -->` if present (or replace `<!-- template-version -->`).
2. **Master Index** *(if `master-index`)* — Read local `Master_Index_Template.md` + live `Master_Index.md`. Compare **headings / Key Locations / Document Map columns** only — not project prose. **Preserve** overview, Project Profile, Document Map rows (§3.0–3.4), user §3.0 exceptions, custom sections. **Adopt** new index sections, renumbers, Quick Start pointer, Key Locations row for `docs/ADT-settings.yaml` (remove stale `rule-install-status.yaml` / `upstream-status.yaml` rows if present). Update links from `templates/Modular_Docs_Workflow.md` → `templates/agent/Modular_Docs_Workflow.md` if still on the old path. §3.0: record only **user-stated** exceptions.
3. **Content templates** *(if `content-templates`)* — Add **missing** sections/structure from local templates into live Understanding / Spec / TODO / Tooling / Human-TODO. Do **not** remove or reshape existing sections here. Create `Tooling.md` / `Human-TODO.md` from templates when missing and link from Master Index.
4. **Live Understanding reshape** *(if `optional-live-reshape`)* —
   - **`sync.mode: auto`:** execute for **all Document Map Understanding stems** (no ask). Skip commit-hygiene mid-sync asks; note in summary that a separate commit for reshape is optional for the user later.
   - **`sync.mode: choose`:** **Present before stopping** (explain + ask once; **do not** report “skipped by design” without asking). **Highly recommended.**
     1. **Commit hygiene *(suggest, do not auto-commit)*:** After pack refresh + version/rules/status stamps, **recommend** committing pack sync first so reshape can be a separate commit. Ask; never `git commit` unless they explicitly ask.
     2. **Explain briefly:** Older live Understandings may still hold contract sections. **Yes (recommended)** = trim to shape-only (Workflow §4), relocate overflow into that stem’s spec, refresh banner/Instructions. **No** = leave bodies.
     3. **Ask once — default toward yes:** all Document Map Understanding stems / named / no.
   - **On execute** (auto or yes): for each chosen stem only — open Understanding + matching spec (+ TODO if checking `[x]` per Workflow §4); **relocate, then remove**; do not invent contract detail; stop after chosen stems.
5. **Live TODO ambition** *(if `optional-todo-ambition`)* —
   - **`sync.mode: auto`:** execute for **all Document Map `*-TODO.md` stems** (no ask).
   - **`sync.mode: choose`:** present + ask once (default all stems / named / no); commit-hygiene suggest only in choose mode.
   - **On execute:** for each stem — open TODO + Understanding; merge interim-architecture staging into target-architecture High Priority; keep real blockers; refresh Current focus; do **not** invent work.
6. **Rules** *(if `rules`)* — For each tool with `tools.*.status: installed` in `docs/ADT-settings.yaml`, open **only** `docs/templates/agent/tools/<key>.md` and refresh that harness.
   - **Default:** refresh pack-managed modular + timescale rules (and enabled optionals) **without asking** — installed means pack-owned.
   - **Ask before overwrite only if** that tool entry has `customized: true` (or an explicit note that pack rule bodies were hand-edited).
   - If `optional_rules.doc-roles` is `enabled`, refresh that tool’s agents folder (six adapters; **no** `orchestrator` adapter).
   - Remove any stale `.cursor/skills/modular-docs-*` leftovers from older pack drafts (ask first only if deleting user-looking paths outside known leftovers).
7. **Upstream stamp** *(if `optional-upstream-check` or update-check enabled)* — If `optional_rules.template-update-check.status` is `enabled`: ensure `upstream:` exists; set `local_pack_version` from local `VERSION`, `last_checked` today, clear `update_available` / stale `upstream_pack_version`. Do **not** delete `ADT-settings.yaml`. Refresh optional update-check rules if tagged `rules` / body changed (same customized rule as above).
8. **Layout migration** — Run [`BOOTSTRAP.md`](BOOTSTRAP.md) Step 0b **only** if layout markers show older layout (`docs/help/` or `docs/agent/` at docs root, or flat setup files in `templates/`). Skip on a normal modern pack refresh.
9. **Summarize** pack refresh + live-doc updates + sync mode used + reshape / TODO ambition executed or (choose) offered/declined + settings migration if any.
10. **Present unset options** *(every sync — before stopping)* — Users cannot ask for what they were never told exists. Read `docs/ADT-settings.yaml`. For each known pack optional (`optional_rules.template-update-check`, `optional_rules.doc-roles`, plus any **new** optional named in the top changelog entry / Step B):
   - **`declined`** → do not re-ask; a one-line “still off” note is enough.
   - **`enabled`** → already handled by refresh steps above; no re-pitch.
   - **missing / unset** → **briefly explain** + **ask once** (yes / no / later). On yes/no, record `enabled` or `declined`. Do **not** enable silently. Do **not** treat unset as silent no.
   - Under **`sync.mode: auto`:** still ask for **brand-new unset optionals** the user has never decided (do not silent-enable new product features). Changelog-tagged **live passes** (reshape, ambition, …) are already covered by auto — those are not “new optionals.”
11. If `sync.mode` still unset after the above → run **B0.2** before stopping.

### Do not (Step B)

- Open or follow this file before Step A / pack refresh completes
- Run Step B from a pre–Step A in-memory copy of any sync playbook
- Capture versions before Step A overwrite
- Scan every live Understanding / Spec / TODO unless `content-templates` or (`optional-live-reshape` and executing) or (`optional-todo-ambition` and executing)
- Treat `content-templates` as permission to trim/remove Understanding sections — that requires `optional-live-reshape` + execute
- Under **`choose`:** omit the reshape / TODO ambition ask when those tags are present
- Under **`auto`:** re-ask for reshape / ambition / rules refresh when tags say to run them
- Ask before refreshing installed rules unless `customized: true`
- On reshape execute: add template headings only and leave obsolete Understanding sections in place
- On TODO ambition execute: invent work, expand scope, or collapse real human/shared blockers
- Keep writing `docs/rule-install-status.yaml` or `docs/upstream-status.yaml` after migration
- Reconstruct whether a missing section is “new in this version” vs “never adopted” when content templates are unchanged — the changelog already answered
- Treat a missing or empty `docs/templates/agent/upstream/` as an error or reason to re-download attribution files
- Open Workflow, help guides, or the whole pack catalog during sync (open Workflow §4 only while executing reshape; Workflow §5 / timescale rule only while executing TODO ambition)
- Keep pulling from GitHub — work from the **local** `docs/templates/` copy
- Skip presenting unset `optional_rules.*` because “do not auto-enable” — that means ask, not stay silent
- Equate “no install artifacts for this harness” with “nothing to offer the user”

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
- "Set sync to auto." / "Set sync to choose."
