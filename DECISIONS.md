# Agentic Doc Templates — Pack decisions

Maintainer-only record of **why** this pack is the way it is. Whole-repo / “Use this template” installs: bootstrap **Step 1d** **deletes** this file (same gate as `eval/` / `scripts/`). Not in the release zip.

**Why this file exists:** CHANGELOG is archaeology (what shipped). Without a decision log, a later edit can undo a choice and look like a cleanup. Read this before changing pack behavior. If you reverse a row, set it `superseded` and add the replacement — do not delete history.

**Post hoc:** Older rows below were reconstructed from [`docs/templates/CHANGELOG.md`](docs/templates/CHANGELOG.md). When in doubt, the changelog entry in **Since** wins on “what we shipped”; this file wins on “do not silently undo.”

| ID | Decision | Status | Since |
|----|----------|--------|-------|
| D1 | Pack version number lives **only** in `docs/templates/VERSION` | accepted | 2.7.27 |
| D2 | Live scaffolds are fill-in blanks; teaching lives in `help/` + `workflow/` | accepted | 2.7.27 |
| D3 | `ship-first` is first-class for typed APIs / CRUD; `prevent` for identity-risky | accepted | 2.7.27 |
| D4 | This root `DECISIONS.md` is the pack’s own decision log | accepted | 2.7.27 |
| D5 | Integrity eval (incl. fail-snapshots) stays in pack-checks | accepted | 2.7.27 |
| D6 | Standing is playbook overrides only; omit the key when empty | accepted | 2.7.25 |
| D7 | Host worktrees are not a settings key; pack does not create trees | accepted | 2.7.24 |
| D8 | `milestone-pr` is a multi-TODO cut, not one-TODO serial PRs | accepted | 2.7.21 |
| D9 | Do not migrate an already-set `orchestrator.git.mode` | accepted | 2.7.20 |
| D10 | Additive request ≠ shape change; de-confirm SoT is `workflow/understanding.md` | accepted | 2.7.14 |
| D11 | User-facing “done” needs an exercise path (operable) | accepted | 2.7.8 |
| D12 | Kit leftovers stay as covering TODOs on an existing stem | accepted | 2.7.19 |
| D13 | Unset `docs_profile` → `prevent` (no silent downgrade) | accepted | 2.7.7 |
| D14 | Release zip is pack-only `docs/templates/`; maintainer dirs stay upstream | accepted | 2.7.17 |
| D15 | Workflow is an index + one module; not a monolith | accepted | 2.7.15 |
| D16 | Roles never always-on; orchestrator is parent-session only | accepted | 2.7.7 |

---

## D1 — Version single source

**Decision:** The current pack version number exists only in `docs/templates/VERSION` (`pack-version:`). CHANGELOG records history. Live Master Index is **stamped** from VERSION on bootstrap / TEMPLATE_SYNC. Do not copy the number into scaffolds, workflow comments, README badges, or `ADT-settings.example.yaml`.

**Do not:** Re-introduce `<!-- pack-version: X.Y.Z -->` or a hardcoded **Pack version** on templates.

## D2 — Skeleton scaffolds, sermons in help / playbooks

**Decision:** Live scaffolds (Understanding, spec, TODO, Master Index At a Glance, Catalog, Decision) are fill-in blanks. Teaching lives in `docs/templates/help/` and `docs/templates/agent/workflow/`. Human-TODO keeps inbox kinds / chat phrases (humans do not open playbooks); Tooling keeps tables. After compaction / a new session, agents re-open the [workflow index](docs/templates/agent/Modular_Docs_Workflow.md) then one module — they do not reconstruct procedure from the scaffold. **Sync:** when 2.7.27 is in catch-up, `optional-live-reshape` **strips** copied sermons / long Instructions / inline section essays from live Understanding / spec / TODO **including stems with no Understanding** (keep user fill-in and loud phased-bridge notes; leave a short pointer). `master-index` adopts slimmer At a Glance even if reshape is declined.

**Do not:** Paste playbook essays back into `Feature_Understanding_Template.md`, `Feature_Spec_Template.md`, `TODO_Template.md`, or Master Index §2.2. Do not ship a pack bump that changes the live scaffold without a Step B strip for existing copies.

## D3 — Ship-first is first-class

**Decision:** Profile is a product choice, not a concession. **`ship-first`** is the right default for typed APIs, CRUD, and clear contracts. **`prevent`** is the right default for editors, games, and multi-surface / identity-risky apps. Unset still means `prevent` so those repos do not lose the gate (D13).

**Do not:** Frame ship-first as “if you prefer less ceremony” or “for people in a hurry.”

## D4 — Pack decision log at repo root

**Decision:** Lasting pack choices live in this file. Consumer projects use `docs/decisions/` / spec Decisions tables. Bootstrap deletes this file from user copies.

## D5 — Eval integrity in pack-checks

**Decision:** `python3 eval/run_eval.py` (no model) stays on `.github/workflows/pack-checks.yml`. Cases include **fail-snapshots** a wrong agent output must fail. Grow from integrity; prepare/verify remains the behavioral loop.

**Named fail modes to keep covered:** wrong-engine build; operable-gap marked done; ship-first skipping Understanding under **prevent**; inventing Understanding under **ship-first**.

## D6 — Standing is not a notes pad

**Decision:** `standing.instructions` holds lasting **ADT playbook overrides** only. Missing / empty is correct. Do not quiz for standing. Do not copy example bullets into live settings.

## D7 — Host worktrees are playbook-only

**Decision:** No `orchestrator.git.worktrees` key. Detect a host worktree and stay. Pack does not `git worktree add`. No host isolation → serial implementers.

## D8 — Milestone ≠ one TODO

**Decision:** `milestone-pr` groups related TODOs, may spawn concurrent implementers when work does not overlap **and** the host can isolate, then squashes the whole milestone before ready.

## D9 — Do not migrate a set git mode

**Decision:** Sync / pack recommend must not rewrite `orchestrator.git.mode` once set. Exception: explicit user ask this turn (`source: user`). Cloud Agent may this-run `milestone-pr` without writing the file.

## D10 — Additive vs shape

**Decision:** Full de-confirm gate lives only in `workflow/understanding.md`. Additive work → spec + TODO, keep `confirmed`. De-confirm only on a significant is / is-not / surface / ownership change. Elsewhere: one-line pointers.

## D11 — Operable done

**Decision:** Library/tests `[x]` is not product-done on a user-facing stem. Need an exercise path, a loud phase, or `library-only`. Open operable Acceptance with no covering TODO is incomplete.

## D12 — Finished-kit covering TODOs

**Decision:** In-scope spec leftovers get implementable TODOs on an **existing** stem. Filling those rows is not inventing work. No empty map rows for vague planned-only items. No wait-for-pickup.

## D13 — Unset profile is prevent

**Decision:** Missing `docs_profile.mode` → treat as `prevent`. Do not invent `ship-first` because Understanding files are missing.

## D14 — Pack vs consumer tree

**Decision:** GitHub Release zip is `docs/templates/` only. Root `eval/`, `scripts/`, this file, pack-checks workflow, issue forms, FUNDING, release.yml, and pack `.cursor/environment.json` are upstream-only and must not stay in a user’s app.

## D15 — Thin workflow index

**Decision:** `Modular_Docs_Workflow.md` is paved path + router. Full procedure lives in one `workflow/` module. Do not re-inflate the monolith.

## D16 — Roles are opt-in; orchestrator stays parent

**Decision:** Doc-role adapters are never always-on. Orchestrate runs in the parent session only — never install/spawn an `orchestrator` subagent type.

---

## Public example

[xAIkit](https://github.com/BrianCLowe/xAIkit) used this pack on a typed API (a natural **ship-first** fit).
