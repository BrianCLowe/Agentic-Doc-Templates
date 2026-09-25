# Contributing to Agentic Doc Templates

Thanks for your interest in contributing! I use these templates daily in my own work, so I'm happy to improve them — but I want to keep the project focused and practical rather than letting it grow in too many directions at once.

## Ways to Contribute

Here are the most helpful ways to contribute:

- **Share how you're using the templates** and what workflows work well for you
- **Suggest improvements** to existing templates (clarity, structure, agent instructions)
- **Propose new templates** that fill a genuine gap
- **Report issues** when something doesn't work well with a specific tool (Cursor, Claude Code, etc.)

## How to Contribute

- **Issues** — Use the issue forms for agent/tool problems, template improvements, docs confusion, or success notes. They keep feedback concrete.
- **Discussions** — Open-ended ideas and “how do I…?” questions are still welcome.
- **Pull Requests** — Welcome for small, focused improvements to existing templates. Please keep changes aligned with the current lightweight, modular style.

**Note for people who copy this repo into an app:** pack-only leftovers belong to *this* template project only — `.github/ISSUE_TEMPLATE/`, `.github/FUNDING.yml`, `.github/workflows/release.yml` / `pack-checks.yml`, `.cursor/environment.json`, `.cursor/skills/pack-release-tag/`, root `eval/`, `scripts/gen_role_adapters.py`, leftover `docs/templates/agent/scripts/*.py`, maintainer `DECISIONS.md`, and maintainer `VISION.md`. If they appear in your app after a whole-repo copy, delete them (bootstrap Steps 1b–1d). Prefer copying only `docs/templates/`.

## What I'm Looking For

I'm more likely to merge contributions that:

- Improve clarity or reduce friction for both humans and agents
- Stay consistent with the current lightweight, modular approach
- Preserve **simplicity** — users should keep saying short action requests (“update the templates”, “draft Understanding for X”); agents route to one playbook
- Solve a real problem I've also run into

I'm more cautious about changes that significantly increase complexity, require long user-facing instruction dumps, or shift the overall direction of the project. I want to avoid ending up maintaining two versions (one public, one private that actually works for me).

**Pack version bumps:** [`docs/templates/VERSION`](docs/templates/VERSION) is the **only** place the pack version number lives. When you change it, update the top entry of [`docs/templates/CHANGELOG.md`](docs/templates/CHANGELOG.md) in the same commit (files touched + Live impact tags + Step B line). Do not copy the number into scaffolds, README badges, workflow comments, or `ADT-settings.example.yaml`.

**Pack decisions:** Lasting pack choices live in root [`DECISIONS.md`](DECISIONS.md) (CHANGELOG is the archaeology — use it to backfill). Supersede a row when reversing it; do not silently undo. The ideal whole we are working toward lives in root [`VISION.md`](VISION.md) — correct that picture; do not treat the current tree as the target. Bootstrap Step 1d **deletes** both files from whole-repo user copies.

**Publishing a GitHub Release:** Push the bump to `main` first, then tag (tag must match `pack-version` in `VERSION`). Tag-only pushes can miss the workflow if `main` does not already have it. Agents follow [`.cursor/skills/pack-release-tag/SKILL.md`](.cursor/skills/pack-release-tag/SKILL.md) — that check is the procedure; do not search the repo for it.

```bash
git push origin main
git tag vX.Y.Z
git push origin vX.Y.Z
```

[`.github/workflows/release.yml`](.github/workflows/release.yml) builds `agentic-doc-templates-X.Y.Z.zip` (pack-only: `docs/templates/`) and publishes the Release with download instructions + that changelog section. If a tag exists but no Release, use **Actions → Release → Run workflow** and enter the tag.

### Writing agent instructions *(for anyone editing this pack — including coding agents)*

Write for **off-road enthusiasts**, not for a careful model that already stays on the paved path.

Thorough agents (and long “thinking” traces) will treat open phrases like “as needed,” “relevant,” “verify,” or “compare” as a license to audit every file and every alternate interpretation before acting. If you mean a short path, **say the short path** — scope gates, ordered steps, explicit **Do not**, and changelog Live impact tags. Do not assume the reader will infer restraint the way you would.

Checklist when changing `docs/templates/agent/` or workflow rules:

- Prefer “do X, then stop” over “update as needed”
- Name which files to open; name which not to open
- Put the common case first (minimal path); park rare migrations behind a clear trigger
- Keep [`Modular_Docs_Workflow.md`](docs/templates/agent/Modular_Docs_Workflow.md) as a short **index** (paved path + router); put full procedure in one [`workflow/`](docs/templates/agent/workflow/README.md) module — do not re-inflate the monolith
- Edit harness adapters only under [`adapter-src/`](docs/templates/agent/roles/adapter-src/README.md), then follow [`GENERATE_ROLE_ADAPTERS.md`](docs/templates/agent/GENERATE_ROLE_ADAPTERS.md) (markdown playbook — **no Python** in the pack). Upstream CI may run root `scripts/gen_role_adapters.py --check`
- De-confirm / additive-vs-shape and lock-gate / real-fork Assumptions: full prose only in [`workflow/understanding.md`](docs/templates/agent/workflow/understanding.md); elsewhere **one-line pointers**
- Prefer a new root [`eval/`](eval/README.md) golden case (upstream repo only — not in the release zip) over more prose when fixing a field behavior bug; `python3 eval/run_eval.py` must stay green on this repo
- If Step B / sync behavior changes, update [`CHANGELOG.md`](docs/templates/CHANGELOG.md) so consumers do not reverse-engineer the pack

If you're unsure whether something fits, just start a Discussion first — I'm happy to talk about it.

## Attribution

All contributions are accepted under the same [CC BY 4.0](LICENSE.md) license as the rest of the project.

Thanks again for helping make these templates better. I genuinely appreciate it.

---

## If you use this repo inside your project

**Recommended:** Copy only **`docs/templates/`** into your project. You do not need this repo's root files — your project keeps its own README and docs layout.

**If you cloned or copied the whole repository** into your project (or used "Use this template" and then merged into an existing app), these root files belong to the **template pack**, not your app:

| Root file | What bootstrap does |
|-----------|---------------------|
| `README.md` | Relocate → `docs/templates/agent/upstream/README.md` |
| `LICENSE.md` | Relocate → `docs/templates/agent/upstream/LICENSE.md` |
| `CONTRIBUTING.md` | Relocate → `docs/templates/agent/upstream/CONTRIBUTING.md` |
| `DECISIONS.md` | **Delete** (pack-maintainer log — Step 1d) |
| `VISION.md` | **Delete** (pack-maintainer vision — Step 1d) |
| `.github/ISSUE_TEMPLATE/` | **Delete** if pack forms (Step 1b) |
| `.github/FUNDING.yml` | **Delete** if this pack’s (Step 1b) |
| `.github/workflows/release.yml` | **Delete** if pack Release workflow (Step 1b) |
| `.github/workflows/pack-checks.yml` | **Delete** if pack integrity workflow (Step 1d) |
| `.cursor/environment.json` | **Delete** if pack Cloud Agent env (Step 1c) |
| `.cursor/skills/pack-release-tag/` | **Delete** when `name:` is `pack-release-tag` (Step 1c). Leave the user’s other skills |
| root `eval/` | **Delete** if pack harness (Step 1d) |
| `scripts/gen_role_adapters.py` | **Delete** (upstream CI helper — Step 1d) |
| leftover `docs/templates/agent/scripts/*.py` | **Delete** (Step 1d) |

That keeps your project root for **your** README and metadata. Attribution and upstream license text stay in `upstream/` inside the template pack.

**Agent bootstrap:** Point your agent at [`docs/templates/agent/BOOTSTRAP.md`](docs/templates/agent/BOOTSTRAP.md) — Step 1 auto-moves clearly upstream root files (Agentic Doc Templates / Brian Lowe markers) to `docs/templates/agent/upstream/` without asking; asks only if ambiguous.

**Manual move:** Create `docs/templates/agent/upstream/` if needed, move the three files above, then write your own project `README.md` at the repo root.

Do **not** put `CONTRIBUTING.md`, `LICENSE.md`, or the template pack README at `docs/` root — only under `docs/templates/agent/upstream/` when you need them for attribution.

If a whole-repo copy left **`.github/ISSUE_TEMPLATE/`**, **`.github/FUNDING.yml`**, **`.github/workflows/release.yml`** / **`pack-checks.yml`**, pack **`.cursor/environment.json`**, **`.cursor/skills/pack-release-tag/`**, root **`eval/`**, **`scripts/gen_role_adapters.py`**, leftover **`docs/templates/agent/scripts/*.py`**, maintainer **`DECISIONS.md`**, or maintainer **`VISION.md`** in your app, delete them — those are for Agentic Doc Templates upstream, not for your product. Bootstrap Steps 1b–1d remove them automatically.