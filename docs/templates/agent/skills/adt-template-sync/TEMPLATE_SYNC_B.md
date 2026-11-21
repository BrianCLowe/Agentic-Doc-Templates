# Template Sync B — Update live docs

> **Step B only.** Open this file **after** [`TEMPLATE_SYNC_A.md`](TEMPLATE_SYNC_A.md) finishes (or the user already refreshed `docs/templates/`). Do not open this file before the pack overwrite.

Source of truth is **on disk** under `docs/templates/`. Do **not** re-fetch from upstream for each live file. Do **not** apply this checklist from a playbook you only read before Step A.

---

## B0 — Scope gate *(do this first — every sync)*

1. Confirm Step A completed (or pack was already refreshed) and you opened **this** file from disk after that.
2. Read **local** `docs/templates/VERSION` (`pack-version` = **to**). Older dual `template-version` / `workflow-version` lines → treat either as `pack-version`.
3. **Migrate settings** *(if needed)* — see **B0.1**, then **B0.1b** (profile rename). Then capture **from** *(before any upstream stamp)*:
   - Prefer `docs/ADT-settings.yaml` → `upstream.local_pack_version` (or legacy `local_template_version`)
   - Else live `Master_Index.md` **Pack version** (or legacy Template/Workflow version)
   - Else **from** is unset (first sync)
4. **Select changelog entries** — see **Catch-up** below. Union their **Live impact** tags. Skim each selected entry’s **Step B** line only for one-shots not already covered by tags.
5. Do **only** the actions implied by the **unioned tags** + those skimmed Step B one-shots. Run the gated checklist **once** (do not walk each version as its own sync). Bump **Pack version** once to **to**.
6. If the pack history file is missing: fall back to comparing **content-template paths only** (`Feature_*_Template.md`, `Tooling_Template.md`, `Human_TODO_Template.md`, `Product_Vision_Template.md`, `Decision_Template.md`) against a prior pack copy. Never open all live feature docs "just in case."

### Catch-up *(version jumps)*

Compare semver `X.Y.Z` numerically (major, minor, patch).

| Case | Entries to use |
|------|----------------|
| **from** unset | **Top entry only** (first sync) |
| **from** ≥ **to** | **Top entry only** (same-version re-sync) |
| **from** < **to** | Every `## X.Y.Z` heading where **from** < version ≤ **to**. If that set is empty → top entry only |

**Union tags** from all selected entries. Then:

- If any selected entry is **>= 2.10.0**, drop the non-doc passes from the union **before** the checklist. Leave existing files. They are not the work list. When **from** < 2.10.1 and **to** >= 2.10.1, the offer step is separate. Do not delete those files inside the offer. Those two sync modes are not acceptance of that offer.

- Apply the gated checklist **once** for the union (not once per release).
- If the union includes any of `content-templates`, `optional-live-reshape`, or the assumption-tidy tag, run those steps even when newer selected entries also list `process-docs-only` (`process-docs-only` on one release does not cancel live passes from skipped releases).
- Skim Step B lines from selected entries for tips / one-shots not expressed by tags (e.g. Human-TODO tip refresh). Do **not** invent a broader audit than the unioned tags + those lines.
- Do **not** bump Pack version through intermediate numbers — set it once to **to**.
- The Live impact table below is a **lasting catalog**. A tag fires only when it appears in this union. **Summarize the union only** — do not name catalog optional tags that were not selected as “skipped.”

| Live impact tag | Do in Step B |
|-----------------|--------------|
| `versions-only` | Bump **Pack version** in live `Master_Index.md` |
| `master-index` | Adopt structural deltas from `Master_Index_Template.md` into live index (see below) |
| `content-templates` | Add *missing* sections/structure only — **not** trim/remove (reshape is a separate tag) |
| `optional-live-reshape` | Live Understanding shape trim + relocate — **`auto` / `auto-all`:** run all stems; **`choose`:** present + ask once |
| `optional-assumption-cleanout` | Live Understanding lock-gate clean-out (Workflow §4) — **`auto` / `auto-all`:** all Understanding stems; **`choose`:** present + ask once |
| `rules` | Refresh installed rules/adapters from local `agent/` (see Rules step — **no ask** unless `customized: true`) |
| `optional-upstream-check` | Stamp `upstream:` in `docs/ADT-settings.yaml` if update-check enabled; offer enable if unset |
| `process-docs-only` | No live feature/shared content scan **for that release alone** - still honor live-content tags from other selected catch-up entries. B0.6 may list feature/shared `*-TODO.md` paths when **from** < 2.10.1 (do not open them) |

**Default when `content-templates`, `optional-live-reshape`, and the assumption-tidy tag are absent from the union:** bump versions + Master Index structure if tagged -> rules if tagged -> summarize -> **present unset options** (below). **Do not** open live `features/` or `_shared/` docs.

### B0.1 — Settings file *(migrate once, then use forever)*

**Live:** `docs/ADT-settings.yaml`  
**Example:** [`ADT-settings.example.yaml`](/docs/templates/agent/ADT-settings.example.yaml)

1. If `docs/ADT-settings.yaml` **exists** → use it (skip migration).
2. Else if `docs/rule-install-status.yaml` and/or `docs/upstream-status.yaml` exist → **merge** into `docs/ADT-settings.yaml`:
   - Copy `tools` + `optional_rules` from rule-install-status.
   - Map upstream-status → `upstream:` (`local_template_version` / `local_workflow_version` → `local_pack_version`; keep `last_checked`, `update_available`, `check_interval_days`, map `upstream_template_version` → `upstream_pack_version`).
   - **Do not** invent `check_mode` or `check_mode_recorded` here - B0.3 asks (legacy weekly days are a hint only).
   - If `sync.mode` missing → leave unset (B0.2 will ask).
   - Write `ADT-settings.yaml`, then **delete** the old status file(s). Note migration in the end summary.
3. Else -> create `ADT-settings.yaml` from the example when first recording a tool/optional/sync decision (do not invent installs). Do **not** copy a `standing:` key from the example - omit it unless the user already stated a playbook override.

### B0.1b — Docs profile rename *(every sync)*

If `docs/ADT-settings.yaml` → `docs_profile.mode` is **`ship-first`**, rewrite that value to **`build-first`**. Same profile (spec; Understanding not required). Do **not** re-ask. Do **not** treat it as unset. Leave `recorded` and `source` as they are. Note the rewrite in the sync summary.

`prevent` and `balanced` stay as written. This is the only settings value this step changes.

### B0.2 — Sync mode *(ask once if unset)*

Read `sync.mode` from `docs/ADT-settings.yaml`.

| Mode | Behavior |
|------|----------|
| **`auto`** | Apply all release-gated live work without mid-sync optionals quiz: versions, master-index, content-templates (missing only), **optional-live-reshape** / assumption tidy (all Document Map Understanding stems when tagged), rules refresh, upstream stamp. Still **ask once** for brand-new unset `optional_rules.*`. Summarize at end. |
| **`auto-all`** | Same as **`auto`**, and also **enable + install** any unset `optional_rules.*` (doc-roles, update-check, future optionals) without asking. Never re-enable **`declined`**. New update-check -> `check_mode: always` + record cadence (skip B0.3 ask). Summarize what was auto-enabled. Does **not** mean run every optional pass in the tag table - only unioned tagged passes, on all Document Map stems, without asking. |
| **`choose`** | Present reshape / assumption tidy (and similar future optional live tags) each sync - ask once per tagged pass. |
| **missing / unset** | **Ask once** before the first optional live pass (or before stopping if none tagged): *Recommended live updates automatically (`auto`), everything including new pack optionals (`auto-all`), or ask each sync (`choose`)?* Record `sync.mode` + `sync.recorded`. Then continue under that mode. Do **not** silent-default. |

Explicit later: *Set sync to auto* / *Set sync to auto-all* / *Set sync to choose*.

### B0.3 - Update-check cadence *(ask once if unset)*

If `optional_rules.template-update-check.status` is **`enabled`** and `upstream.check_mode_recorded` is **missing** (or `check_mode` itself is missing):

Under **`sync.mode: auto-all`:** set `check_mode: always` + `check_mode_recorded` today (no ask). Keep existing `interval` + days if already set.

Otherwise **ask once** (do not silent-default; do not skip under `sync.mode: auto`):

> Template update checks are on. Check for a newer pack **every session** (`always` — recommended; negligible token cost), or only every **N days** (`interval`, default 7 if they had a weekly stamp)?

Record:

- `upstream.check_mode`: `always` or `interval`
- `upstream.check_interval_days` when interval (keep prior days if present, else **7**)
- `upstream.check_mode_recorded`: today

If update-check is **declined** or unset -> skip B0.3 (step 10 may enable it - under `auto`/`choose` ask cadence in the same turn; under `auto-all` default `always`).

Explicit later: *Check for template updates every session* / *Only check every week*.

### B0.4 - Docs profile *(ask once if unset)*

Read `docs_profile.mode` from `docs/ADT-settings.yaml`.

| State | Behavior |
|-------|----------|
| **`prevent` / `balanced` / `build-first`** | Keep; no re-ask |
| **missing / unset** | **Ask once** before stopping (do not silent-default to invent build-first). Unset means **prevent** for which docs to write. |

**Ask** (brief; optional 1-line suggest if `docs/reference/` or live Understandings give a signal):

**Present and explain** the menu by opening [`workflow/profile-standing.md`](/docs/templates/agent/workflow/profile-standing.md#01-docs-profile-ceremony-modes) §0.1 (source of truth) and using that table. Do **not** restate the three modes here.

Record `docs_profile.mode` + `recorded` (+ `source: user` or `agent-suggested`). Explicit later: *Set docs profile to …*.

Under **`sync.mode: auto-all`:** if unset, set **`prevent`** + `recorded` today (no quiz) — never invent `build-first` without a user choice.

### B0.5 - Remove orchestrator key *(2.10.0)*

If `docs/ADT-settings.yaml` contains an `orchestrator:` key, **remove that key**.

**Write-in (not a quiz, not an eighth mode):** standing stays playbook overrides only. Do not quiz for standing on this sync. Do not invent a settings enum for a docs or sync override.

### B0.6 - Offer leftover feature TODOs *(when crossing 2.10.1)*

**When this step runs:** **from** < 2.10.1 and **to** ≥ 2.10.1.

**When it does not run:** **from** ≥ 2.10.1, including a same-version re-sync. Do not offer again.

This step is the same under `auto`, `auto-all`, `choose`, and an unset mode. The mode does not answer it. It is not a Live impact tag. Do not execute it because `auto-all` executes unioned passes.

**List (do not open):** files named `*-TODO.md` directly in `docs/features/` and `docs/_shared/`. If a subdirectory of those two folders contains a `*-TODO.md`, include that path. Do not look anywhere else. Do not list `docs/Human-TODO.md`. Do not open the files. Do not read their boxes. If the list is empty, skip this step.

**The step is the offer.** If this turn’s user message already says to clean them out or to delete the leftover feature TODOs, that is the yes: do **Cleanout** below and do not also ask. `sync.mode` is not that message.

Otherwise send one message that names every path in the list and says why:

> These files are leftover feature TODOs: [paths]. The pack removed feature TODOs. It writes documentation and syncs itself. It does not keep a feature checklist or a Current focus. The harness owns the code. An agent that opens one of these files still sees the old boxes and can treat that list as the work. The pack will not add to them. Clean them out?

Sending that message finishes this step. The cleanout is not this step. Continue the rest of Step B. Do not delete, edit, or move the files in this step.

Send the offer in its own sentences. Do not attach it to the sync-mode question. A choice of `auto-all` does not answer the offer.

**Not a yes:** `sync.mode: auto` and `sync.mode: auto-all` do not answer the offer. A missing reply, silence, or “finish the sync” does not. Do not delete the files because the mode is `auto-all`.

#### Cleanout

Run only after an explicit yes to **this** offer. A bare yes answers this offer only when the previous assistant message was the offer. “Clean them out” or “delete the leftover feature TODOs” answers it whenever the user says that. A yes to the sync-mode question does not. `auto` and `auto-all` do not.

A later session that only has that yes opens this section and does the cleanout. It does not start a template sync.

1. Delete each path from the list. No other file.
2. In `docs/Master_Index.md`, delete link text that points at a deleted file. Keep the stem’s row and its other cells.
3. In that stem’s spec, `-Understanding.md`, and Catalog file, delete a line that only links the deleted TODO (`Related TODO`). Leave every other line. Skip a file that is not there.
4. Leave `docs/Human-TODO.md` in place.
5. Stop. Do not create a replacement list. Do not open other docs.

### Reference — local template → live file *(only when tagged)*

| Local template (read) | Live file (edit carefully) | When |
|-----------------------|----------------------------|------|
| `Master_Index_Template.md` | `docs/Master_Index.md` — never blind-replace | `master-index` or always for version lines |
| `agent/Modular_Docs_Workflow.md` + `agent/workflow/` | Already replaced in Step A — do not copy into Master_Index | — |
| `Feature_Understanding_Template.md` | Each `*-Understanding.md` — add *missing* sections only | `content-templates` |
| `Feature_Understanding_Template.md` + `agent/workflow/understanding.md` §4 | Each chosen `*-Understanding.md` — **trim** non-shape sections; **relocate** into that stem’s spec; **2.7.27:** strip instruction sermons (below) | `optional-live-reshape` **and** (`auto` / `auto-all` **or** user said yes) |
| `agent/workflow/understanding.md` §4 lock gate | Each chosen `*-Understanding.md` — lock obvious defaults; delete invented quizzes; un-target reference examples not clearly set as the target | `optional-assumption-cleanout` **and** (`auto` / `auto-all` **or** user said yes) |
| `Feature_Spec_Template.md` | Each feature/shared `.md` spec — add missing sections only; receive relocated contract on reshape | `content-templates` / reshape executing |
| `Tooling_Template.md` | `docs/Tooling.md` — create if missing; add sections only | `content-templates` |
| `Human_TODO_Template.md` | `docs/Human-TODO.md` — create if missing; add columns/sections only | `content-templates` |
| `Product_Vision_Template.md` | `docs/Product-Vision.md` — create if missing (**all** profiles). Lightweight draft; **peek `docs/reference/` first**; do **not** rebuild from the map. **`build-first`:** not a gate | `content-templates` |
| `agent/Modular_Documentation_Rule.*` | Installed rule paths — refresh via each `tools/<key>.md` for `status: installed` tools | `rules` |
| *(retired 2.10.0)* timescale + build-verify rules | **Delete** installed copies via each `tools/<key>.md`. The pack no longer ships them | `rules` |
| `agent/Template_Update_Check_Rule.*` | Optional update-check — same dispatch | `rules` or `optional-upstream-check` |
| `agent/tools/*.md` | Install/sync adapters — open only for tools already `installed` | `rules` |
| `agent/roles/cursor/*.md` / `agent/roles/grok/*.md` / `agent/roles/copilot/*.agent.md` | Optional subagents — via tool playbooks | `rules` when `optional_rules.doc-roles` is `enabled` |

Versions:

- `docs/templates/VERSION` → **`pack-version`** → live `Master_Index.md` **Pack version** (and `<!-- pack-version -->` if present)
- Legacy live **Template version** / **Workflow version** lines → **replace** with a single **Pack version** line from `VERSION` (do not keep both systems)

### Gated checklist

1. **Versions** — Set **Pack version** in live `Master_Index.md` from local `VERSION`. Remove obsolete Template/Workflow version lines when present. Update `<!-- pack-version -->` if present (or replace `<!-- template-version -->`).
2. **Master Index** *(if `master-index`)* - Required when tagged - not gated on reshape / `optional-live-reshape`. Read local `Master_Index_Template.md` + live `Master_Index.md`. Compare **headings / Key Locations / Document Map columns / At a Glance** only - not project prose. **Preserve** overview, Project Profile, Document Map rows (Section 3.0-3.4), user Section 3.0 exceptions, custom sections. **Adopt** new index sections, renumbers, Quick Start pointer, Key Locations row for `docs/ADT-settings.yaml` (remove stale `rule-install-status.yaml` / `upstream-status.yaml` rows if present). If Section 2.2 At a Glance is still a policy dump (Simplicity / Idea sources / Understanding essay), replace it with the template's short pointer table (keep the first-class docs profile). Adopt the Key Locations `docs/templates/` "pack-owned; do not edit" wording when missing. Update links from `templates/Modular_Docs_Workflow.md` -> `templates/agent/Modular_Docs_Workflow.md` if still on the old path. Section 3.0: record only **user-stated** exceptions.
3. **Content templates** *(if `content-templates`)* - Add **missing** sections/structure from local templates into live Understanding / Spec / Tooling / Human-TODO / the whole-product picture. Do **not** remove or reshape existing sections here. Create `Tooling.md` / `Human-TODO.md` from templates when missing and link from Master Index. Create the whole-product picture file from its template if missing (every profile). List `docs/reference/` before drafting (prefer the newest idea/identity sources, or user-pointed files; skip vendor and API dumps unless they define the product). Draft is / is not plus the whole-product picture from those sources and this-turn conversation (lock obvious; examples are not the target unless clearly set; lightweight). **Then** fill How the map fits from existing map rows only. Do **not** draft that picture from the Document Map, feature Understandings, or specs. Do **not** skip `docs/reference/` because the map looks complete. On the profile that ships from a spec: create the picture file if missing; do not wait for confirm before coding.
4. **Live Understanding reshape** *(if `optional-live-reshape`)* —
   - **`sync.mode: auto` or `auto-all`:** execute for **all Document Map Understanding stems** (no ask).
   - **`sync.mode: choose`:** **Present before stopping** (explain + ask once; **do not** report “skipped by design” without asking). **Highly recommended.**
     1. **Explain briefly:** Older live Understandings may still hold contract sections **and** copied pack sermons / long Instructions footers. Spec / TODO sermons also sit on stems with **no** Understanding (`build-first` / excepted / balanced skip). **Yes (recommended)** = trim Understanding to shape (Workflow Section 4), relocate overflow into that stem's spec, **and** run the **2.7.27 instruction-footer strip** (below) on **every** Document Map spec / core TODO (Understanding too when present). **No** = leave bodies.
     2. **Ask once - default toward yes:** all Document Map stems (reshape Understanding where present; strip spec/TODO on every stem, even without Understanding) / named / no.
   - **On execute** (`auto` / `auto-all` or yes): **(a)** If 2.7.27 is in catch-up → run **Instruction-footer strip** first on **every** chosen stem that has a spec and/or core TODO — **including stems with no Understanding**. **(b)** For chosen stems that **have** Understanding: if How-it-should-work / Done when / other non-shape sections remain → **relocate, then remove** (Workflow §4). Do not invent contract detail; do not invent Understanding on `build-first` stems; stop after chosen stems.

4b. **Live Assumption clean-out** *(if `optional-assumption-cleanout`)* —
   - **`sync.mode: auto` or `auto-all`:** execute for **all Document Map Understanding stems** (no ask).
   - **`sync.mode: choose`:** **Present before stopping** (explain + ask once; **do not** report “skipped by design” without asking). **Recommended.**
     1. **Explain briefly:** Older live Understandings may hold invented Assumption quizzes, obvious defaults left unchecked, or `docs/reference/` / chat **examples treated as the target**. **Yes (recommended)** = lock-gate clean-out (Workflow Section 4): lock obvious defaults into is / is not; delete invented quizzes; un-target reference examples that were **not** clearly set as the target; leave only real forks (empty Assumptions is success). **No** = leave bodies.
     2. **Ask once - default toward yes:** all Document Map Understanding stems / named / no.
   - **On execute** (`auto` / `auto-all` or yes): for each chosen stem that **has** `-Understanding.md`, follow Workflow §4 **Clean-out pass**. Open that Understanding (and that stem’s spec only if a reference example was copied there as a constraint). **Keep status** — do **not** de-confirm `confirmed` → `draft`; do **not** inject a mid-sync shape quiz. List identity corrections in the sync summary. Do **not** invent new Assumptions; do **not** invent Understanding on `build-first`; do **not** silent-scan stems the user did not choose; stop after chosen stems.

### 2.7.27 Instruction-footer strip *(optional-live-reshape one-shot)*

Run only when selected catch-up includes **2.7.27** and reshape is executing. Open Document Map spec + core TODO for **every** stem in scope (Understanding too when it exists). **Do not skip a stem because Understanding is absent.** Not Human-TODO, not Tooling, not `docs/decisions/`.

**Goal:** Live files are fill-in blanks. Pack sermons and long instruction footers copied from older templates go away. User content stays. Teaching lives in [`help/SCAFFOLDS.md`](/docs/templates/help/SCAFFOLDS.md) + the matching workflow module.

**Understanding** — delete these if present (they are pack teaching, **not** contract — do **not** relocate into the spec):

- Size / is-not examples: `*Too thin`, `*Right size`, `*Wrong size`, `*Bad example`, `*Good example`, “Feature shape, not the spec”
- The essay “This file is the agent’s model of **feature shape**…” / “The agent writes this file first”
- `## Instructions for AI Agents` / `**Instructions for Humans**` / `**Instructions for AI Agents**` blocks that restate the playbook

**Keep:** Status, dates, Related links, **What this is** / **is NOT**, Relationship, Assumptions, Confirmed with user, and any user-written bullets in those sections.

**Then** if the file has no short pointer to `help/SCAFFOLDS.md` and `workflow/understanding.md`, add the two-line human/agent banner from current [`Feature_Understanding_Template.md`](/docs/templates/Feature_Understanding_Template.md) (do not paste the old sermon).

**Spec** — delete these pack phrases if present (they are teaching — **not** contract; do **not** relocate):

- Section sermons: `Contract completeness here`, `Lives here, not in Understanding`, `Lives here (the contract)`, `Bridge to TODOs`, `Acceptance must be **operable**`, `Do not thin Architecture`, `Graduation / anti-compression`
- `## Instructions for AI Agents` / `**Instructions for Humans**` footers that restate Workflow

**Keep:** Overview, Architecture, Behavior *user content*, Acceptance *checkbox items*, Decisions *rows*, Visual *table rows*, Dependencies, Current status.

**Then** if the spec has no short pointer to `help/SCAFFOLDS.md` and `workflow/understanding.md`, add the two-line human/agent banner from current [`Feature_Spec_Template.md`](/docs/templates/Feature_Spec_Template.md).





**Master Index** is **not** this strip — adopt slimmer At a Glance under the `master-index` tag (step 2). That tag is **required when present**, even if reshape is declined.

**Do not:** rewrite What this is / user Behavior / Acceptance items; invent stems; strip Human-TODO human kinds / chat phrases or Tooling tables (those stay human-facing); treat `content-templates` as this strip (that tag only **adds** missing sections).
6. **Rules** *(if `rules`)* — For each tool with `tools.*.status: installed` in `docs/ADT-settings.yaml`, open **only** `docs/templates/agent/tools/<key>.md` and refresh that harness.
   - **Default:** refresh the pack-managed modular rule (and enabled optionals) **without asking** — installed means pack-owned. **Delete** installed timescale and build-verify rules. The pack no longer ships them.
   - Refresh the pack skills for each installed tool via its `tools/<key>.md` Skills section.
   - **Ask before overwrite only if** that tool entry has `customized: true` (or an explicit note that pack rule bodies were hand-edited).
   - If `optional_rules.doc-roles` is `enabled`, refresh that tool’s agents folder (**three** adapters: understanding-author, doc-graduate, docs-template-sync; **no** `docs-bootstrap` adapter). **Delete leftover** installed `docs-bootstrap`, `feature-implementer`, `work-verifier`, `todo-warden`, and `orchestrator` adapter files.
   - Remove any stale `.cursor/skills/modular-docs-*` leftovers from older pack drafts (ask first only if deleting user-looking paths outside known leftovers).
7. **Upstream stamp** *(if `optional-upstream-check` or update-check enabled)* - If `optional_rules.template-update-check.status` is `enabled`: ensure `upstream:` exists; set `local_pack_version` from local `VERSION`. **`check_mode: interval`:** set `last_checked` today; clear `update_available` / stale `upstream_pack_version`. **No interval** (`always` or unset): do **not** set `last_checked`, `update_available`, or `upstream_pack_version`. If those keys are present, **remove** them (check logs; the next session fetches again). Do **not** delete `ADT-settings.yaml`. Refresh optional update-check rules if tagged `rules` / body changed (same customized rule as above).
8. **Layout migration** — Run [`BOOTSTRAP.md`](/docs/templates/agent/BOOTSTRAP.md) Step 0b **only** if layout markers show older layout (`docs/help/` or `docs/agent/` at docs root, or flat setup files in `templates/`). Skip on a normal modern pack refresh.
9. **Summarize from the union only:**
   - sync mode used
   - catch-up **from→to** (or top-entry-only) + the **unioned** Live impact tags (+ skimmed Step B one-shots)
   - of those **unioned** optional live passes: executed / offered / declined (`choose`)
   - settings migration if any
   - any `orchestrator:` key removed

   **Do not** name optional tags that were **not** in the union as “skipped.” They were not this jump’s instructions — listing them sounds like missed work. The tag table is a lasting catalog; a tag fires only when selected changelog entries tag it.

   **“Skipped”** is reserved for: a **unioned** tagged pass that was in scope but not executed (`choose`: user declined); or a path check that did not apply (B8 modern layout — no old `docs/help/` / `docs/agent/` leftovers).

   If B0.6 applied, the same end message includes the offer (paths + why). That offer is not a union tag. Do not report it as executed. The files are still on disk unless they had already said yes.

   `auto-all` does **not** mean “run every optional pass every sync.” It means: when a tagged pass is **in the union**, execute it on all Document Map stems without asking.
10. **Present / apply unset options** *(every sync - before stopping)* - Users cannot ask for what they were never told exists. Read `docs/ADT-settings.yaml`. For each known pack optional (`optional_rules.template-update-check`, `optional_rules.doc-roles`, plus any **new** optional named in selected catch-up entries / Step B):
   - **`declined`** → do not re-ask or re-enable; a one-line “still off” note is enough.
   - **`enabled`** -> already handled by refresh steps above; no re-pitch of the feature - but if update-check is enabled and cadence was never recorded, **B0.3** still applies.
   - **missing / unset** under **`sync.mode: auto-all`:** **enable + install** without asking (record `enabled` + `recorded` today). For `template-update-check`: ensure `upstream:`, set `local_pack_version`, `check_mode: always`, `check_mode_recorded` today. For `doc-roles` (and any optional with install artifacts): run each installed tool’s `tools/<key>.md` optional section. Note auto-enabled items in the summary. Never treat this as license to flip **`declined`** → enabled.
   - **missing / unset** under **`auto`** or **`choose`:** **briefly explain** + **ask once** (yes / no / later). For **`doc-roles`**, include why: if installed, heavier doc moments leave the parent session so it stays slim; without them that work stays in the parent (bootstrap Step 3p **C**). On **yes** for `template-update-check`, also run **B0.3** cadence ask in the same turn before stopping. On yes/no, record `enabled` or `declined`. Do **not** enable silently. Do **not** treat unset as silent no.
   - Under **`sync.mode: auto`:** changelog-tagged **live passes** (reshape, ambition, ...) are already covered by auto - those are not "new optionals." Cadence (B0.3) is still asked when due.
11. If `sync.mode` still unset after the above → run **B0.2** before stopping.
12. If update-check is enabled and `check_mode_recorded` still missing -> run **B0.3** before stopping (`auto-all` defaults `always` there).
13. If `docs_profile.mode` still unset -> run **B0.4** before stopping (`auto-all` defaults `prevent` there).
14. If `docs/ADT-settings.yaml` still contains an `orchestrator:` key -> run **B0.5** and **remove that key**.
15. If **from** < 2.10.1 and **to** >= 2.10.1 -> run **B0.6**. The step is the offer. Do not delete feature `*-TODO.md` files in this step unless this turn's user message already accepted that offer. `auto` and `auto-all` are not a yes. If **from** >= 2.10.1, do not run B0.6.

### Do not (Step B)

- Open or follow this file before Step A / pack refresh completes
- Run Step B from a pre–Step A in-memory copy of any sync playbook
- Capture versions before Step A overwrite
- Scan every live Understanding / Spec unless `content-templates` or (`optional-live-reshape` and executing) or (the assumption-tidy tag and executing) or the **2.7.25 standing relocate** one-shot (then only the **one** destination a misplaced standing bullet names - Workflow Section 0.2 standing relocate) or the **2.9.6 standing cleanout** one-shot (then only `standing.instructions` - Workflow Section 0.2 standing cleanout) or the **2.7.27 footer pass** (then every in-scope stem's spec, and Understanding when present).
- Treat `content-templates` as permission to trim/remove Understanding sections — that requires `optional-live-reshape` + execute
- Under **`choose`:** omit the reshape / assumption tidy ask when those tags are present
- Under **`auto` / `auto-all`:** re-ask for reshape / assumption tidy / rules refresh when tags say to run them
- Ask before refreshing installed rules unless `customized: true`
- On reshape execute: add template headings only and leave obsolete Understanding sections **or** copied instruction sermons in place
- On 2.7.27 instruction-footer strip: relocate sermons into the spec; delete user What this is / Assumptions; skip spec/TODO-only stems; skip spec/TODO footers or inline section sermons when those files still have the long playbook restatement; delete a loud phased-bridge note; leave a dumped At a Glance when `master-index` is tagged
- Keep writing `docs/rule-install-status.yaml` or `docs/upstream-status.yaml` after migration
- Reconstruct whether a missing section is “new in this version” vs “never adopted” when content templates are unchanged — the changelog already answered
- Treat a missing or empty `docs/templates/agent/upstream/` as an error or reason to re-download attribution files
- Open Workflow, help guides, or the whole pack catalog during sync (open Workflow Section 4 only while executing reshape or assumption tidy; Workflow Section 0.2 standing relocate only when the 2.7.25 standing-relocate one-shot is in catch-up; Workflow Section 0.2 standing cleanout only when the 2.9.6 standing-cleanout one-shot is in catch-up)
- On assumption clean-out execute: invent new Assumption quizzes; treat a `docs/reference/` example as the target unless it was clearly set as the target; invent Understanding on `build-first`; rewrite user fill-in that is already category-correct; **de-confirm** a `confirmed` Understanding or inject a mid-sync shape quiz
- Re-fetch from upstream for each live file - work from the **local** `docs/templates/` copy
- Under **`auto` / `choose`:** skip presenting unset `optional_rules.*` because “do not auto-enable” — that means ask, not stay silent
- Under **`auto-all`:** leave unset `optional_rules.*` unset — enable + install them (except **`declined`**)
- Under no interval (`always` or unset `check_mode`): write `last_checked`, `update_available`, or `upstream_pack_version` on the upstream stamp - remove those keys if present
- Silent-set `check_mode` from legacy `check_interval_days` without B0.3 (except **`auto-all`** defaulting `always` when cadence is missing)
- Skip B0.3 when update-check is enabled but `check_mode_recorded` is missing under `auto` / `choose` (under `auto-all`, default `always`)
- Equate “no install artifacts for this harness” with “nothing to offer the user”
- Under **`auto-all`:** flip **`declined`** optionals back to enabled
- Read **only the top** changelog entry when **from** < **to** and intermediate `##` entries exist — **union** those entries (Catch-up above)
- Let a newer entry's `process-docs-only` cancel `content-templates` / reshape / assumption-tidy tags from skipped releases in the same jump
- Name catalog optional tags that were **not** in the union as “skipped” (they were not this jump’s instructions)
- Treat `auto-all` as license to run every pass in the Live impact tag table
- Walk each catch-up version as its own full sync or bump Pack version through intermediate numbers
- Treat `sync.mode: auto` or `sync.mode: auto-all` as a yes to the B0.6 offer. Delete or edit leftover feature `*-TODO.md` files in the offer step. Include `docs/Human-TODO.md` in that offer. Turn B0.6 into a Live impact tag. Offer again when **from** >= 2.10.1

---

## Do not

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
