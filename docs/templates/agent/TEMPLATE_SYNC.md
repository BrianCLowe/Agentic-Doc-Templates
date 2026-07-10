# Template Sync — Agent Instructions

> Use when the user asks to sync, migrate, or **update the doc templates**. Typical ask: *"Update the doc templates from Agentic Doc Templates and sync our live docs."*

## Critical — two separate steps (do not confuse them)

| Step | What | How |
|------|------|-----|
| **A — Refresh pack** | Replace **only** `docs/templates/` | Download files from GitHub into that folder (ZIP / copy). Network fetch only. |
| **B — Update live docs** | Edit `Master_Index.md`, Understanding, specs, TODOs | Read the **downloaded local copies** in `docs/templates/` and **update live docs as needed**. |

**Git is not how you update live docs.** Do **not** `git pull`, `git merge`, `git checkout`, submodule update, or otherwise use the user's project git history to “sync” `Master_Index.md` / `features/` / `_shared/`. Those files are project-owned. After Step A, Step B is ordinary file edits guided by the **local** templates.

**Upstream is only a download source** for the template pack — not a remote to apply to this repo’s live documentation.

**Upstream repo:** `https://github.com/BrianCLowe/Agentic-Doc-Templates`  
**Upstream pack path:** `docs/templates/` only

---

## Step A — Download / replace `docs/templates/`

Overwrite the project's `docs/templates/` with the upstream tree. That folder is the canonical pack — not live project content.

**Never overwrite from the download:**

- `docs/Master_Index.md`
- `docs/features/`, `docs/_shared/`, `docs/decisions/`, `docs/reference/`
- `docs/rule-install-status.yaml`
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

**Allowed alternatives** (still only to refresh `docs/templates/`):

- Clone or sparse-checkout **into a temp directory**, then **copy** `docs/templates/` into the project — never clone over the user project root
- `gh` / raw URLs for individual files under `docs/templates/`

**Do not:**

- Add Agentic-Doc-Templates as a git remote of the user project and pull into it
- `git checkout` / `git restore` live docs from any remote
- Treat “sync” as updating the user repo via git

If the user already refreshed `docs/templates/` themselves, skip Step A.

After Step A: confirm versions in the **local** `docs/templates/Master_Index_Template.md` and `docs/templates/Modular_Docs_Workflow.md`.

---

## Step B — Update live docs from the downloaded local copies

Source of truth for structure is now **on disk** under `docs/templates/`. Compare those files to the live docs and **update the live docs as needed**. Do not re-fetch from GitHub for each live file.

### Files

| Local template (read) | Live file (edit carefully) |
|-----------------------|----------------------------|
| `docs/templates/Master_Index_Template.md` | `docs/Master_Index.md` — update structure as needed; never blind-replace |
| `docs/templates/Modular_Docs_Workflow.md` | Already replaced in Step A — do not copy into Master_Index |
| `docs/templates/Feature_Understanding_Template.md` | Each `*-Understanding.md` — add new sections where missing |
| `docs/templates/Feature_Spec_Template.md` | Each feature/shared `.md` spec — add new sections where missing |
| `docs/templates/TODO_Template.md` | Each `*-TODO.md` — add missing blocks (e.g. Current focus) |
| `docs/templates/agent/Modular_Documentation_Rule.*` | Installed rule paths — ask before overwriting custom installs |

Versions:

- `<!-- template-version: X.Y -->` in local `Master_Index_Template.md` → **Template version** in live `Master_Index.md`
- `<!-- workflow-version: X.Y -->` in local `Modular_Docs_Workflow.md` → **Workflow version** in live `Master_Index.md`

### Update checklist

1. Read **local** `docs/templates/Master_Index_Template.md`, `Modular_Docs_Workflow.md`, and live `docs/Master_Index.md`.
2. Compare structure: headings, Document Map, versions, naming.
3. **Preserve** in `Master_Index.md`: overview, Project Profile, Document Map rows (§3.0–3.4), user §3.0 exceptions only, custom sections.
4. **Adopt** from the **local** Master_Index template: new index sections, renumbers, Quick Start pointer — not old workflow §4–10 (those live in `Modular_Docs_Workflow.md`).
5. Update installed agent rules from **local** `docs/templates/agent/` if the rule body changed (ask first if customized).
6. Bump **Template version** / **Workflow version** in live `Master_Index.md`.
7. Layout migrations (pre-1.7 / pre-1.8 / pre-2.0): follow [`BOOTSTRAP.md`](BOOTSTRAP.md) Step 0b using the **local** pack layout.
8. Update live Understanding / Spec / TODO files from the local templates as needed — do not overwrite project content.
9. §3.0: record only **user-stated** exceptions — never invent rows.
10. Summarize pack refresh + live-doc updates; ask before large live-doc rewrites.

---

## Do not

- Use **git** to update live docs (`Master_Index`, `features/`, `_shared/`).
- Blindly replace `docs/Master_Index.md` with the template.
- Copy workflow prose into live `Master_Index.md`.
- Put project feature content into `docs/templates/`.
- Remove project-only Document Map entries unless the user asks.
- Invent §3.0 exceptions for missing Understanding / TODO files.
- Keep pulling from GitHub during Step B — work from the **local** `docs/templates/` copy.

## Example user prompts

- "Update the doc templates from Agentic Doc Templates and sync our live docs."
- "Download the latest templates into `docs/templates/`, then update Master_Index from the local templates."
- "We already refreshed `docs/templates/` — update our live docs from the local pack." (skip Step A)
- "Compare `Master_Index.md` to `docs/templates/Master_Index_Template.md` and apply structural improvements."
