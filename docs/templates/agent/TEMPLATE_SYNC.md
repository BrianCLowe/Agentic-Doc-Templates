# Template Sync — Agent Instructions

> Use when the user asks to sync, migrate, or **update the doc templates**. Typical ask: *"Update the doc templates from Agentic Doc Templates and sync our live docs."*

## Critical — two separate steps (do not confuse them)

| Step | What | How |
|------|------|-----|
| **A — Refresh pack** | Replace **entire** `docs/templates/` | ZIP/copy — **full overwrite**, no per-file diffs |
| **B — Update live docs** | Edit live docs per pack changelog | Read `VERSION` + top [`CHANGELOG.md`](../CHANGELOG.md) entry — do **only** what that entry lists |

**Git is not how you update live docs.** Do **not** `git pull`, `git merge`, `git checkout`, submodule update, or otherwise use the user's project git history to “sync” `Master_Index.md` / `features/` / `_shared/`. Those files are project-owned. After Step A, Step B is ordinary file edits guided by the **local** templates and changelog.

**Upstream is only a download source** for the template pack — not a remote to apply to this repo’s live documentation.

**Upstream repo:** `https://github.com/BrianCLowe/Agentic-Doc-Templates`  
**Upstream pack path:** `docs/templates/` only

---

## Step A — Download / replace `docs/templates/` *(full overwrite — no diffs)*

**Always replace the entire folder.** Do **not** inventory, diff, or selectively update files under `docs/templates/`. That wastes tokens. Delete the project's `docs/templates/` (or overwrite it wholesale) and copy the upstream `docs/templates/` tree in one shot.

That folder is the canonical pack — not live project content. Treat Step A as a dumb replace.

**Never overwrite from the download:**

- `docs/Master_Index.md`
- `docs/features/`, `docs/_shared/`, `docs/decisions/`, `docs/reference/`
- `docs/rule-install-status.yaml`
- `docs/upstream-status.yaml` (weekly check stamp — update versions after sync; see below)
- Installed rules outside templates (`.cursor/rules/`, `AGENTS.md`, …) — update later via [`RULE_INSTALL.md`](RULE_INSTALL.md) if needed

**Preferred fetch: ZIP** (no git required in the user project):

```powershell
$tmp = Join-Path $env:TEMP "agentic-doc-templates-sync"
Remove-Item -Recurse -Force $tmp -ErrorAction SilentlyContinue
New-Item -ItemType Directory -Path $tmp | Out-Null
Invoke-WebRequest -Uri "https://github.com/BrianCLowe/Agentic-Doc-Templates/archive/refs/heads/main.zip" -OutFile "$tmp/main.zip"
Expand-Archive -Path "$tmp/main.zip" -DestinationPath $tmp
$src = Join-Path $tmp "Agentic-Doc-Templates-main\docs\templates"
$dst = "docs/templates"   # project-relative
Remove-Item -Recurse -Force $dst -ErrorAction SilentlyContinue
Copy-Item -Recurse $src $dst
```

```bash
tmp=$(mktemp -d)
curl -sL "https://github.com/BrianCLowe/Agentic-Doc-Templates/archive/refs/heads/main.zip" -o "$tmp/main.zip"
unzip -q "$tmp/main.zip" -d "$tmp"
rm -rf docs/templates
cp -R "$tmp/Agentic-Doc-Templates-main/docs/templates" docs/templates
```

**Allowed alternatives** (still **full** folder replace only):

- Clone or sparse-checkout **into a temp directory**, then **copy** the whole `docs/templates/` tree over the project’s `docs/templates/` — never clone over the user project root

**Do not (Step A):**

- Diff old vs new template files and update only what changed
- Fetch individual files with `gh` / raw URLs one-by-one
- Read every file under the existing `docs/templates/` before replacing
- Capture Template / Workflow versions *before* overwrite (read `VERSION` after Step A)
- Add Agentic-Doc-Templates as a git remote of the user project and pull into it
- `git checkout` / `git restore` live docs from any remote
- Treat “sync” as updating the user repo via git

If the user already refreshed `docs/templates/` themselves, skip Step A.

After Step A → go to Step B (start with `VERSION` + `CHANGELOG.md`).

---

## Step B — Update live docs *(changelog-gated)*

Source of truth is **on disk** under `docs/templates/`. Do **not** re-fetch from GitHub for each live file.

### B0 — Scope gate *(do this first — every sync)*

1. Read **local** `docs/templates/VERSION`.
2. Read **only the top entry** of `docs/templates/CHANGELOG.md` (Live impact, Files, Unchanged content templates, Step B).
3. Do **only** the actions implied by that entry’s tags and Step B line.
4. If `CHANGELOG.md` is missing: fall back to comparing **content-template paths only** (`Feature_*_Template.md`, `TODO_Template.md`, `Tooling_Template.md`, `Human_TODO_Template.md`, `Decision_Template.md`) via `git diff` against HEAD or a prior pack copy. Never open all live feature docs “just in case.”

| Live impact tag | Do in Step B |
|-----------------|--------------|
| `versions-only` | Bump Template / Workflow version in live `Master_Index.md` |
| `master-index` | Adopt structural deltas from `Master_Index_Template.md` into live index (see below) |
| `content-templates` | Add *new* sections to live Understanding / Spec / TODO / Tooling / Human-TODO where missing |
| `rules` | Offer refresh of installed rules from local `agent/` (ask if customized) |
| `optional-upstream-check` | Update `docs/upstream-status.yaml` if present; offer enable if missing |
| `process-docs-only` | No live feature/shared content scan (versions / Master Index / rules only as other tags say) |

**Default when `content-templates` is absent:** bump versions + Master Index structure if tagged → summarize → ask about optional items. **Do not** open live `features/` or `_shared/` docs.

### Reference — local template → live file *(only when tagged)*

| Local template (read) | Live file (edit carefully) | When |
|-----------------------|----------------------------|------|
| `Master_Index_Template.md` | `docs/Master_Index.md` — never blind-replace | `master-index` or always for version lines |
| `agent/Modular_Docs_Workflow.md` | Already replaced in Step A — do not copy into Master_Index | — |
| `Feature_Understanding_Template.md` | Each `*-Understanding.md` — add new sections only | `content-templates` |
| `Feature_Spec_Template.md` | Each feature/shared `.md` spec — add new sections only | `content-templates` |
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
3. **Content templates** *(if `content-templates` only)* — Add missing sections from local templates into live Understanding / Spec / TODO / Tooling / Human-TODO. Do not overwrite project content. Create `Tooling.md` / `Human-TODO.md` from templates when missing and link from Master Index. Ask before large rewrites across many files.
4. **Rules** *(if `rules`)* — For each tool with `tools.*.status: installed` in `docs/rule-install-status.yaml`, open **only** `docs/templates/agent/tools/<key>.md` and refresh that harness (ask first if customized). Do **not** open every tool file. If `optional_rules.doc-roles` is `enabled`, each tool playbook refreshes its agents folder. Remove any stale `.cursor/skills/modular-docs-*` leftovers from older pack drafts (ask first).
5. **Upstream stamp** *(if `optional-upstream-check` or file exists)* — If `docs/upstream-status.yaml` exists: set `local_template_version` / `local_workflow_version` from local `VERSION`, `last_checked` today, clear `update_available` — do **not** delete the file. Refresh optional update-check rules if tagged `rules` / body changed (ask first if customized).
6. **Layout migration** — Run [`BOOTSTRAP.md`](BOOTSTRAP.md) Step 0b **only** if layout markers show older layout (`docs/help/` or `docs/agent/` at docs root, or flat setup files in `templates/`). Skip on a normal modern pack refresh.
7. **Summarize** pack refresh + live-doc updates; ask before large live-doc rewrites.

### Do not (Step B)

- Capture versions before Step A overwrite
- Scan every live Understanding / Spec / TODO unless `content-templates` is listed
- Reconstruct whether a missing section is “new in this version” vs “never adopted” when content templates are unchanged — the changelog already answered
- Treat a missing or empty `docs/templates/agent/upstream/` (deleted README / LICENSE / CONTRIBUTING) as an error or reason to re-download attribution files — users often remove those on purpose after bootstrap
- Open Workflow, help guides, or the whole pack catalog during sync
- Keep pulling from GitHub — work from the **local** `docs/templates/` copy

---

## Do not

- Use **git** to update live docs (`Master_Index`, `features/`, `_shared/`).
- Blindly replace `docs/Master_Index.md` with the template.
- Copy workflow prose into live `Master_Index.md`.
- Put project feature content into `docs/templates/`.
- Remove project-only Document Map entries unless the user asks.
- Invent §3.0 exceptions for missing Understanding / TODO files.
- Diff or cherry-pick inside `docs/templates/` on Step A — **always overwrite the whole folder**.

## Example user prompts

- "Update the doc templates from Agentic Doc Templates and sync our live docs."
- "Download the latest templates into `docs/templates/`, then update Master_Index from the local templates."
- "We already refreshed `docs/templates/` — update our live docs from the local pack." (skip Step A)
- "Apply new template sections to Master_Index; preserve Document Map content."
- "Check for template updates." *(version-only — [`TEMPLATE_UPDATE_CHECK.md`](TEMPLATE_UPDATE_CHECK.md); run this sync only if newer and user agrees)*
