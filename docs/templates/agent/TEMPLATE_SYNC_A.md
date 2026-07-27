# Template Sync A — Refresh pack

> **Step A only.** Opened from [`TEMPLATE_SYNC.md`](TEMPLATE_SYNC.md) or the template-sync role. Do **not** open [`TEMPLATE_SYNC_B.md`](TEMPLATE_SYNC_B.md) until this file says to.

## Critical

| Step | What | How |
|------|------|-----|
| **A — Refresh pack** *(this file)* | Replace **entire** `docs/templates/` | ZIP/copy — **full overwrite**, no per-file diffs |
| **B — Update live docs** | Edit live docs per pack changelog | **Only after A** — open [`TEMPLATE_SYNC_B.md`](TEMPLATE_SYNC_B.md) from disk |

**Git is not how you update live docs.** Do **not** `git pull`, `git merge`, `git checkout`, submodule update, or otherwise use the user's project git history to “sync” `Master_Index.md` / `features/` / `_shared/`. Those files are project-owned.

**Upstream is only a download source** for the template pack — not a remote to apply to this repo’s live documentation.

**Upstream repo:** `https://github.com/BrianCLowe/Agentic-Doc-Templates`  
**Upstream pack path:** `docs/templates/` only

---

## Download / replace `docs/templates/` *(full overwrite — no diffs)*

**Always replace the entire folder.** Do **not** inventory, diff, or selectively update files under `docs/templates/`. That wastes tokens. Delete the project's `docs/templates/` (or overwrite it wholesale) and copy the upstream `docs/templates/` tree in one shot.

That folder is the canonical pack — not live project content. Treat this as a dumb replace.

**Never overwrite from the download:**

- `docs/Master_Index.md`
- `docs/features/`, `docs/_shared/`, `docs/decisions/`, `docs/reference/`
- `docs/rule-install-status.yaml`
- `docs/upstream-status.yaml` (weekly check stamp — update versions in Step B)
- Installed rules outside templates (`.cursor/rules/`, `AGENTS.md`, …) — update later via [`RULE_INSTALL.md`](RULE_INSTALL.md) if Step B tags `rules`

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
- Capture Template / Workflow versions *before* overwrite (read `VERSION` in Step B)
- Open [`TEMPLATE_SYNC_B.md`](TEMPLATE_SYNC_B.md) or the top `CHANGELOG.md` Step B before the overwrite finishes
- Add Agentic-Doc-Templates as a git remote of the user project and pull into it
- `git checkout` / `git restore` live docs from any remote
- Treat “sync” as updating the user repo via git

If the user already refreshed `docs/templates/` themselves, skip the download — still continue to the handoff below.

---

## Handoff → Step B *(mandatory)*

Pack on disk is now current. **Stop using this file for procedure.**

1. Open **local** [`TEMPLATE_SYNC_B.md`](TEMPLATE_SYNC_B.md) from disk (the copy just written by the overwrite — not a pre-A memory of any sync playbook).
2. If you entered via `roles/template-sync.md`, you may re-skim that pack role from disk; prefer **B** for the live-doc checklist. Harness adapters under `.cursor/agents/` / `.grok/agents/` may still be stale until B’s `rules` refresh.
3. Do **not** continue from any Step B text you read before the overwrite (including an old monolithic `TEMPLATE_SYNC.md`).

→ Follow [`TEMPLATE_SYNC_B.md`](TEMPLATE_SYNC_B.md) only from here.
