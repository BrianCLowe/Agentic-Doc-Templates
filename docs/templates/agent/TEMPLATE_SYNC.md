# Template Sync — Agent Instructions

> Use when the user asks to sync, migrate, or **update the doc templates**. Typical ask: *"Update the doc templates from Agentic Doc Templates and sync our live docs."*

**You do both:** (1) **download** the latest pack into the project's `docs/templates/`, then (2) **update live docs** (`Master_Index.md`, Understanding, specs, TODOs) based on what changed — without wiping project content.

**Upstream repo:** `https://github.com/BrianCLowe/Agentic-Doc-Templates`  
**Upstream pack path:** `docs/templates/` (entire folder — scaffolds, workflow, `help/`, `agent/`, `chat-ui/`)

## Goal

1. **Refresh** the project's `docs/templates/` from upstream (agent downloads/replaces those files).
2. **Migrate** live project docs to match new structure — preserve Document Map, overview, and feature content.

## Step 0 — Fetch / replace the template pack *(preferred)*

When the user asks to sync or update templates, **you may download and overwrite** `docs/templates/` from upstream. That folder is the canonical pack — not live project content.

**Preserve (never overwrite from upstream):**

- `docs/Master_Index.md`
- `docs/features/`, `docs/_shared/`, `docs/decisions/`, `docs/reference/`
- `docs/rule-install-status.yaml`
- Installed rule copies outside templates (e.g. `.cursor/rules/`, `AGENTS.md`) — update those separately per [`RULE_INSTALL.md`](RULE_INSTALL.md) if the rule body changed

**Replace:** everything under `docs/templates/` with the upstream tree (same relative paths).

### How to fetch (pick what works in this environment)

| Method | When to use |
|--------|-------------|
| **`gh` / GitHub API / raw URLs** | Agent has network; preferred |
| **`git sparse-checkout` or shallow clone** into a temp dir, then copy `docs/templates/` | Reliable full-tree copy |
| **Download ZIP** of the repo (`…/archive/refs/heads/main.zip`), extract `docs/templates/`, copy over | Works without `gh` |
| **User already refreshed** `docs/templates/` | Skip Step 0; continue from Step 1 |

**Example (PowerShell — ZIP):**

```powershell
$tmp = Join-Path $env:TEMP "agentic-doc-templates-sync"
Remove-Item -Recurse -Force $tmp -ErrorAction SilentlyContinue
New-Item -ItemType Directory -Path $tmp | Out-Null
Invoke-WebRequest -Uri "https://github.com/BrianCLowe/Agentic-Doc-Templates/archive/refs/heads/main.zip" -OutFile "$tmp/main.zip"
Expand-Archive -Path "$tmp/main.zip" -DestinationPath $tmp
$src = Join-Path $tmp "Agentic-Doc-Templates-main\docs\templates"
$dst = "docs/templates"   # project-relative
# Backup optional: Copy-Item $dst "$dst.bak-$(Get-Date -Format yyyyMMdd)" -Recurse
Remove-Item -Recurse -Force $dst -ErrorAction SilentlyContinue
Copy-Item -Recurse $src $dst
```

**Example (bash — sparse clone):**

```bash
tmp=$(mktemp -d)
git clone --depth 1 --filter=blob:none --sparse \
  https://github.com/BrianCLowe/Agentic-Doc-Templates.git "$tmp/repo"
git -C "$tmp/repo" sparse-checkout set docs/templates
rm -rf docs/templates
cp -R "$tmp/repo/docs/templates" docs/templates
```

**Example (single file via raw URL):**

`https://raw.githubusercontent.com/BrianCLowe/Agentic-Doc-Templates/main/docs/templates/Modular_Docs_Workflow.md`

Prefer **whole-tree** replace over one-off files so `help/`, `agent/`, and `chat-ui/` stay in sync.

After fetch: confirm `docs/templates/agent/TEMPLATE_SYNC.md` and version comments in `Master_Index_Template.md` / `Modular_Docs_Workflow.md` match upstream `main`.

**Ask first** only if replacing would destroy local edits the user made *inside* `docs/templates/` (unusual — that folder should stay upstream-clean). If unsure, show a short diff summary of what will be replaced.

## Files involved (after pack is current)

| File | Role |
|------|------|
| `docs/templates/Master_Index_Template.md` | Lean index schema (overview + map — **not** full workflow) |
| `docs/templates/Modular_Docs_Workflow.md` | Canonical agent procedure — replace from upstream when workflow version bumps |
| `docs/templates/chat-ui/AGENT.md` | Chat-only instructions — replace when chat pack changes |
| `docs/Master_Index.md` | Live project index (instance) — **merge**, never blind-replace |
| `docs/templates/Feature_Spec_Template.md` | Durable spec / contract after Understanding is confirmed |
| `docs/templates/TODO_Template.md` | Canonical TODO format (+ Current focus handoff) |
| `docs/templates/Decision_Template.md` | Optional cross-cutting decisions in `docs/decisions/` |
| `docs/templates/help/`, `docs/templates/agent/` | Setup and usage guides — refreshed in Step 0 |
| Feature `*-Understanding.md` files | Agent-drafted intent — merge new sections; do not overwrite |
| Feature `*.md` specs | Graduate from Understanding; add Decisions + Maturity (shared) |
| Feature `*-TODO.md` files | Live task lists — update only if template format changed |

Check versions:

- `<!-- template-version: X.Y -->` in `Master_Index_Template.md` → **Template version** in live `Master_Index.md`
- `<!-- workflow-version: X.Y -->` in `Modular_Docs_Workflow.md` → **Workflow version** in live `Master_Index.md`

## Sync workflow (live docs)

1. Complete **Step 0** (or confirm `docs/templates/` is already at upstream).
2. Read `docs/templates/Master_Index_Template.md`, `docs/templates/Modular_Docs_Workflow.md`, and `docs/Master_Index.md`.
3. Compare structure: section headings, Document Map layout, workflow version, naming conventions.
4. **Preserve** all project-specific content in `Master_Index.md`:
   - Section 1 overview text and Project Profile
   - Document Map rows and links (Sections 3.0–3.4)
   - Section 3.0 exception registry rows (**user-requested only** — do not invent rows)
   - Custom sections the project added
5. **Adopt** from `Master_Index_Template.md`:
   - New or revised index sections (Key Locations, At a Glance, Quick Start pointer)
   - Renumbered sections (update internal references)
   - **Do not** merge old workflow sections (4–10) from legacy Master_Index — they now live in `Modular_Docs_Workflow.md`
6. **Adopt** workflow / chat / rules:
   - `Modular_Docs_Workflow.md` and `chat-ui/` should already match upstream after Step 0
   - Update **installed** agent rule copies if the rule body in `docs/templates/agent/` changed materially (especially **§0 Naming** — see [`RULE_INSTALL.md`](RULE_INSTALL.md)); ask before overwriting customized installs
7. Update **Template version** and **Workflow version** lines in `docs/Master_Index.md`.
8. If migrating from pre-1.7 Master_Index: **remove** duplicated workflow sections (old §4 Quick Start through §10 Decisions) from live `Master_Index.md` after confirming content exists in `Modular_Docs_Workflow.md`; replace with lean §4 Quick Start from template.
9. If migrating from pre-1.8 / pre-2.0 layouts: run layout migration per [`BOOTSTRAP.md`](BOOTSTRAP.md) Step 0b — target is a single `docs/templates/` pack with `help/` and `agent/` subfolders (not at `docs/` root).
10. If `Feature_Understanding_Template.md` is new or changed, merge new sections into active `-Understanding.md` files — do not overwrite.
11. If `Feature_Spec_Template.md` is new or changed, merge **Decisions**, **Maturity**, and **Last reconciled** into live specs where placeholders exist.
12. If `TODO_Template.md` changed, add **Current focus** blocks to active TODOs if missing.
13. If Section 3.0 is new, migrate only **user-stated** "excepted" notes into the registry — never invent exceptions.
14. Summarize what changed (pack refresh + live-doc merges) and ask the user to confirm before large structural edits to live docs.

## Do not

- Blindly replace `docs/Master_Index.md` with the template (you will lose the Document Map and overview).
- Copy workflow prose into live `Master_Index.md` (keep it in `Modular_Docs_Workflow.md` only).
- Put project-specific feature content into `docs/templates/`.
- Remove project-only Document Map entries unless the user asks.
- Invent §3.0 exceptions for missing Understanding / TODO files.

## Example user prompts

- "Update the doc templates from Agentic Doc Templates and sync our live docs."
- "Pull the latest Agentic Doc Templates into `docs/templates/` and sync our Master_Index."
- "Sync our docs to https://github.com/BrianCLowe/Agentic-Doc-Templates — download the template pack and migrate."
- "Compare `Master_Index.md` to `Master_Index_Template.md` and apply structural improvements."
- "We updated the templates — migrate our live docs." (pack already refreshed; skip Step 0)
- "Sync workflow to latest Modular_Docs_Workflow.md."
