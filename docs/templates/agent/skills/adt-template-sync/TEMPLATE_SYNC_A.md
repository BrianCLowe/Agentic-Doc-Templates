# Template Sync A — Refresh pack

> **Step A only.** Opened from [`TEMPLATE_SYNC.md`](SKILL.md) or the template-sync role. Do **not** open [`TEMPLATE_SYNC_B.md`](TEMPLATE_SYNC_B.md) until this file says to.

## Critical

| Step | What | How |
|------|------|-----|
| **A — Refresh pack** *(this file)* | Replace **entire** `docs/templates/` | ZIP/copy — **full overwrite**, no per-file diffs |
| **B — Update live docs** | Edit live docs per pack changelog | **Only after A** — open [`TEMPLATE_SYNC_B.md`](TEMPLATE_SYNC_B.md) from disk |

**Live docs are updated in Step B.** `Master_Index.md`, `features/`, and `_shared/` are project-owned.

**Upstream is only a download source** for the template pack.

**Upstream:** `https://github.com/BrianCLowe/Agentic-Doc-Templates`  
**Upstream pack path:** `docs/templates/` only

---

## Download / replace `docs/templates/` *(full overwrite — no diffs)*

**Always replace the entire folder.** Do **not** inventory, diff, or selectively update files under `docs/templates/`. Delete the project's `docs/templates/` (or overwrite it wholesale) and copy the upstream `docs/templates/` tree in one shot.

That folder is the canonical pack — not live project content. Treat this as a dumb replace.

**Keep these project-owned paths when copying the download:**

- `docs/Master_Index.md`
- `docs/features/`, `docs/_shared/`, `docs/decisions/`, `docs/reference/`
- `docs/ADT-settings.yaml` (pack prefs — migrate/update in Step B)
- Legacy `docs/rule-install-status.yaml` / `docs/upstream-status.yaml` if still present (migrate in Step B — do not delete in A)
- Installed rules outside templates (`.cursor/rules/`, `AGENTS.md`, …) — update later via [`RULE_INSTALL.md`](/docs/templates/agent/RULE_INSTALL.md) if Step B tags `rules`

**Preferred fetch: ZIP**:

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

**Do not (Step A):**

- Diff old vs new template files and update only what changed
- Fetch individual files one-by-one
- Read every file under the existing `docs/templates/` before replacing
- Capture pack version *before* overwrite (read `VERSION` in Step B)
- Open [`TEMPLATE_SYNC_B.md`](TEMPLATE_SYNC_B.md) or the top `CHANGELOG.md` Step B before the overwrite finishes

If the user already refreshed `docs/templates/`, skip the download. Otherwise, you may copy the full `docs/templates/` from a ZIP or folder the user names. Continue to the handoff below.

---

## Handoff → Step B *(mandatory)*

Pack on disk is now current. **Stop using this file for procedure.**

1. Open **local** [`TEMPLATE_SYNC_B.md`](TEMPLATE_SYNC_B.md) from disk (the copy just written by the overwrite — not a pre-A memory of any sync playbook).
2. If you entered via `roles/template-sync.md`, you may re-skim that pack role from disk; prefer **B** for the live-doc checklist. Harness adapters under `.cursor/agents/` / `.grok/agents/` / `.github/agents/` may still be stale until B’s `rules` refresh.
3. Do **not** continue from any Step B text you read before the overwrite (including an old monolithic `TEMPLATE_SYNC.md`).

→ Follow [`TEMPLATE_SYNC_B.md`](TEMPLATE_SYNC_B.md) only from here.
