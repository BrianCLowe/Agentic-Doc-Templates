# Template Sync B — Update live docs

> **Step B only.** Open this file **after** [`TEMPLATE_SYNC_A.md`](TEMPLATE_SYNC_A.md) finishes (or the user already refreshed `docs/templates/`). Do not open this file before the pack overwrite.

Source of truth is **on disk** under `docs/templates/`. Do **not** re-fetch from GitHub for each live file. Do **not** apply this checklist from a playbook you only read before Step A.

---

## B0 — Scope gate *(do this first — every sync)*

1. Confirm Step A completed (or pack was already refreshed) and you opened **this** file from disk after that.
2. Read **local** `docs/templates/VERSION`.
3. Read **only the top entry** of `docs/templates/CHANGELOG.md` (Live impact, Files, Unchanged content templates, Step B).
4. Do **only** the actions implied by that entry’s tags and Step B line.
5. If `CHANGELOG.md` is missing: fall back to comparing **content-template paths only** (`Feature_*_Template.md`, `TODO_Template.md`, `Tooling_Template.md`, `Human_TODO_Template.md`, `Decision_Template.md`) via `git diff` against HEAD or a prior pack copy. Never open all live feature docs “just in case.”

| Live impact tag | Do in Step B |
|-----------------|--------------|
| `versions-only` | Bump Template / Workflow version in live `Master_Index.md` |
| `master-index` | Adopt structural deltas from `Master_Index_Template.md` into live index (see below) |
| `content-templates` | Add *missing* sections/structure only — **not** trim/remove (reshape is a separate tag) |
| `optional-live-reshape` | **Present** Understanding shape trim + relocate (below) — **highly recommended**; ask once; never silent-skip; suggest committing pack sync first |
| `rules` | Offer refresh of installed rules from local `agent/` (ask if customized) |
| `optional-upstream-check` | Update `docs/upstream-status.yaml` if present; offer enable if missing |
| `process-docs-only` | No live feature/shared content scan (versions / Master Index / rules only as other tags say) |

**Default when `content-templates` and `optional-live-reshape` are absent:** bump versions + Master Index structure if tagged → summarize → **present unset options** (below). **Do not** open live `features/` or `_shared/` docs.

### Reference — local template → live file *(only when tagged)*

| Local template (read) | Live file (edit carefully) | When |
|-----------------------|----------------------------|------|
| `Master_Index_Template.md` | `docs/Master_Index.md` — never blind-replace | `master-index` or always for version lines |
| `agent/Modular_Docs_Workflow.md` | Already replaced in Step A — do not copy into Master_Index | — |
| `Feature_Understanding_Template.md` | Each `*-Understanding.md` — add *missing* sections only | `content-templates` |
| `Feature_Understanding_Template.md` + Workflow §4 | Each chosen `*-Understanding.md` — **trim** non-shape sections; **relocate** into that stem’s spec; refresh banner/Instructions | `optional-live-reshape` **and** user said yes |
| `Feature_Spec_Template.md` | Each feature/shared `.md` spec — add missing sections only; receive relocated contract on reshape | `content-templates` / reshape yes |
| `TODO_Template.md` | Each `*-TODO.md` — add missing blocks only | `content-templates` |
| `Tooling_Template.md` | `docs/Tooling.md` — create if missing; add sections only | `content-templates` |
| `Human_TODO_Template.md` | `docs/Human-TODO.md` — create if missing; add columns/sections only | `content-templates` |
| `agent/Modular_Documentation_Rule.*` | Installed rule paths — refresh via each `tools/<key>.md` for `status: installed` tools; ask before overwriting custom installs | `rules` |
| `agent/Template_Update_Check_Rule.*` | Optional update-check — same dispatch | `rules` or `optional-upstream-check` |
| `agent/tools/*.md` | Install/sync adapters — open only for tools already `installed` | `rules` |
| `agent/roles/cursor/*.md` / `agent/roles/grok/*.md` | Optional subagents — via tool playbooks (`.cursor/agents/`, `.grok/agents/`, …) | `rules` when `optional_rules.doc-roles` is `enabled` |

Versions:

- `docs/templates/VERSION` (preferred) or `<!-- template-version: X.Y -->` in local `Master_Index_Template.md` → **Template version** in live `Master_Index.md`
- `docs/templates/VERSION` or `<!-- workflow-version: X.Y -->` in local `agent/Modular_Docs_Workflow.md` → **Workflow version** in live `Master_Index.md`

### Gated checklist

1. **Versions** — Bump **Template version** / **Workflow version** (and `<!-- template-version -->` if present) in live `Master_Index.md` from local `VERSION`.
2. **Master Index** *(if `master-index`)* — Read local `Master_Index_Template.md` + live `Master_Index.md`. Compare **headings / Key Locations / Document Map columns** only — not project prose. **Preserve** overview, Project Profile, Document Map rows (§3.0–3.4), user §3.0 exceptions, custom sections. **Adopt** new index sections, renumbers, Quick Start pointer. Update links from `templates/Modular_Docs_Workflow.md` → `templates/agent/Modular_Docs_Workflow.md` if still on the old path. §3.0: record only **user-stated** exceptions.
3. **Content templates** *(if `content-templates`)* — Add **missing** sections/structure from local templates into live Understanding / Spec / TODO / Tooling / Human-TODO. Do **not** remove or reshape existing sections here. Create `Tooling.md` / `Human-TODO.md` from templates when missing and link from Master Index.
4. **Live Understanding reshape** *(if `optional-live-reshape`)* — **Present before stopping** (explain + ask once; **do not** report “skipped by design” without asking). **Highly recommended** — stale Understanding bodies drift from Workflow §4 and waste sessions (wrong re-reviews, mini-specs, missed relocate).
   1. **Commit hygiene *(suggest, do not auto-commit)*:** After pack refresh + version/rules/status stamps, **recommend** the user commit the pack sync first so reshape of live Understanding/spec files can land in a **separate** follow-up commit. Ask if they want to commit now, reshape first then commit both, or proceed without committing. Never `git commit` unless they explicitly ask.
   2. **Explain briefly:** Older live Understandings may still hold contract sections (How-it-should-work, UI/UX, Visual references, Done when, long Behavior). Leaving them invites inefficiency and real agent mistakes. **Yes (recommended)** = for each chosen stem, trim Understanding to shape-only (Workflow §4), **move** overflow into that stem’s spec if missing, then **delete** it from Understanding; refresh human review banner + Instructions from the Understanding template. **No** = leave bodies alone (new drafts still use shape-only; drift remains until a later pass).
   3. **Ask once — default toward yes:** Prefer offering **all Document Map Understanding stems** as the recommended choice; also allow named stems only / no (or later). Phrase so declining is explicit, not the quiet default.
   4. On **no/later:** do not open live feature/shared bodies for reshape; note the decline **and** that reshape remains recommended when they next touch those stems.
   5. On **yes:** for each chosen stem only:
      - Open that stem’s `-Understanding.md` + matching spec (+ `-TODO.md` if checking `[x]` marks per Workflow §4).
      - **Relocate, then remove** — do not only add headings. Non-shape sections and contract prose leave Understanding after they land on the spec (Done when → Acceptance; flows → Behavior; screenshots → Visual references).
      - Do not invent contract detail. Do not pad the spec empty if there was nothing to relocate.
      - Stop after chosen stems — no repo-wide audit beyond the user’s scope.
5. **Rules** *(if `rules`)* — For each tool with `tools.*.status: installed` in `docs/rule-install-status.yaml`, open **only** `docs/templates/agent/tools/<key>.md` and refresh that harness (ask first if customized). Do **not** open every tool file. If `optional_rules.doc-roles` is `enabled`, each tool playbook refreshes its agents folder. Remove any stale `.cursor/skills/modular-docs-*` leftovers from older pack drafts (ask first).
6. **Upstream stamp** *(if `optional-upstream-check` or file exists)* — If `docs/upstream-status.yaml` exists: set `local_template_version` / `local_workflow_version` from local `VERSION`, `last_checked` today, clear `update_available` — do **not** delete the file. Refresh optional update-check rules if tagged `rules` / body changed (ask first if customized).
7. **Layout migration** — Run [`BOOTSTRAP.md`](BOOTSTRAP.md) Step 0b **only** if layout markers show older layout (`docs/help/` or `docs/agent/` at docs root, or flat setup files in `templates/`). Skip on a normal modern pack refresh.
8. **Summarize** pack refresh + live-doc updates + whether reshape was offered and accepted/declined.
9. **Present unset options** *(every sync — before stopping)* — Users cannot ask for what they were never told exists. Read `docs/rule-install-status.yaml` if present. For each known pack optional (`optional_rules.template-update-check`, `optional_rules.doc-roles`, plus any **new** optional named in the top changelog entry / Step B):
   - **`declined`** → do not re-ask; a one-line “still off” note is enough.
   - **`enabled`** → already handled by refresh steps above; no re-pitch.
   - **missing / unset** → **briefly explain** what it is, what “yes” installs for *this* project’s `tools.*.status: installed` tools (including “no adapter files — playbooks used in-session” when that tool’s `tools/<key>.md` says Install: None), then **ask once** (yes / no / later). On yes/no, record `enabled` or `declined`. Do **not** enable silently. Do **not** treat unset as silent no. Do **not** skip the ask because an installed tool has no harness adapters (e.g. Copilot + doc-roles).

### Do not (Step B)

- Open or follow this file before Step A / pack refresh completes
- Run Step B from a pre–Step A in-memory copy of any sync playbook
- Capture versions before Step A overwrite
- Scan every live Understanding / Spec / TODO unless `content-templates` or (`optional-live-reshape` **and** user said yes)
- Treat `content-templates` as permission to trim/remove Understanding sections — that requires `optional-live-reshape` + user yes
- Treat “do not auto-rewrite” / “skipped by design” as permission to **omit the reshape ask** when `optional-live-reshape` is tagged
- On reshape yes: add template headings only and leave obsolete Understanding sections in place
- Reconstruct whether a missing section is “new in this version” vs “never adopted” when content templates are unchanged — the changelog already answered
- Treat a missing or empty `docs/templates/agent/upstream/` (deleted README / LICENSE / CONTRIBUTING) as an error or reason to re-download attribution files — users often remove those on purpose after bootstrap
- Open Workflow, help guides, or the whole pack catalog during sync (open Workflow §4 only while executing an accepted reshape)
- Keep pulling from GitHub — work from the **local** `docs/templates/` copy
- Skip presenting unset optionals because “do not auto-enable” — that means ask, not stay silent
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
- "Download the latest templates into `docs/templates/`, then update Master_Index from the local templates."
- "We already refreshed `docs/templates/` — update our live docs from the local pack." *(skip A download; open this file)*
- "Apply new template sections to Master_Index; preserve Document Map content."
- "Check for template updates." *(version-only — [`TEMPLATE_UPDATE_CHECK.md`](TEMPLATE_UPDATE_CHECK.md); run sync A→B only if newer and user agrees)*
