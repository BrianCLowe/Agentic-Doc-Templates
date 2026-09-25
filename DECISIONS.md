# Agentic Doc Templates — Pack decisions

Maintainer-only record of **why** this pack is the way it is. Whole-repo / “Use this template” installs: bootstrap **Step 1d** **deletes** this file (same gate as `eval/` / `scripts/`). Not in the release zip.

**Why this file exists:** CHANGELOG is archaeology (what shipped). Without a decision log, a later edit can undo a choice and look like a cleanup. Read this before changing pack behavior. If you reverse a row, set it `superseded` and add the replacement — do not delete history.

**Post hoc:** Older rows below were reconstructed from [`docs/templates/CHANGELOG.md`](docs/templates/CHANGELOG.md). When in doubt, the changelog entry in **Since** wins on “what we shipped”; this file wins on “do not silently undo.”

| ID | Decision | Status | Since |
|----|----------|--------|-------|
| D1 | Pack version number lives **only** in `docs/templates/VERSION` | accepted | 2.7.27 |
| D2 | Live scaffolds are fill-in blanks; teaching lives in `help/` + `workflow/` | accepted | 2.7.27 |
| D3 | `build-first` is first-class for typed APIs / CRUD; `prevent` for identity-risky | accepted | 2.7.27 |
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
| D16 | Roles never always-on; orchestrator (and bootstrap) are parent-session only | accepted | 2.7.7 |
| D17 | Assumptions = real forks only; lock obvious defaults; examples are not identity | accepted | 2.7.28 |
| D18 | Sync summaries report the catch-up union only; `auto-all` ≠ every catalog tag | accepted | 2.7.29 |
| D19 | Optional `team_inbox` is opt-in; unset = human-only inbox; do not force a bot org chart | accepted | 2.8.0 |
| D20 | Team roster is two-stage (read vs self-ID); Name / Jobs / Anti-jobs if defined; one initial PR for a full team | accepted | 2.8.1 |
| D21 | Product vision is the whole-product end-state picture; feature map alone is not identity | superseded | 2.9.0 |
| D22 | Named humans self-ID onto the roster with their own slug; generic `human` is leftover bucket, not a teammate | accepted | 2.9.1 |
| D23 | Destination file always; implementation gate only after *lock product shape* + confirm (or prevent’s confirm) | accepted | 2.9.3 |
| D24 | Session-default docs freshness; pack lessons live on the routed path, not only the discovery playbook | accepted | 2.9.4 |
| D25 | Bugbot reads the PR until ready; squash-before-ready is not required (HEAD-only reviewers use standing) | accepted | 2.9.4 |
| D26 | Sibling `docs/` drift is content (`git diff`), not ancestry (`git log` after squash-merge) | accepted | 2.9.5 |
| D27 | Docs profile value `ship-first` is renamed `build-first`; sync rewrites the setting | accepted | 2.9.6 |
| D28 | Slash commands are an opt-in menu for sync and orchestrate only | accepted | 2.9.6 |
| D29 | Repo behavior that is not a pack playbook is asked as a rule or a skill, not filed in standing | accepted | 2.9.6 |
| D30 | Drained child tasks are not capability-done; an Outcomes row stays open until a passing exercise note | accepted | 2.9.9 |

---

## D1 — Version single source

**Decision:** The current pack version number exists only in `docs/templates/VERSION` (`pack-version:`). CHANGELOG records history. Live Master Index is **stamped** from VERSION on bootstrap / TEMPLATE_SYNC. Do not copy the number into scaffolds, workflow comments, README badges, or `ADT-settings.example.yaml`.

**Do not:** Re-introduce `<!-- pack-version: X.Y.Z -->`, a hardcoded **Pack version** on templates, or a README Pack badge (number or `docs/templates/VERSION` stand-in).

## D2 — Skeleton scaffolds, sermons in help / playbooks

**Decision:** Live scaffolds (Understanding, spec, TODO, Master Index At a Glance, Catalog, Decision) are fill-in blanks. Teaching lives in `docs/templates/help/` and `docs/templates/agent/workflow/`. Human-TODO keeps inbox kinds / chat phrases (humans do not open playbooks); Tooling keeps tables. After compaction / a new session, agents re-open the [workflow index](docs/templates/agent/Modular_Docs_Workflow.md) then one module — they do not reconstruct procedure from the scaffold. **Sync:** when 2.7.27 is in catch-up, `optional-live-reshape` **strips** copied sermons / long Instructions / inline section essays from live Understanding / spec / TODO **including stems with no Understanding** (keep user fill-in and loud phased-bridge notes; leave a short pointer). `master-index` adopts slimmer At a Glance even if reshape is declined.

**Do not:** Paste playbook essays back into `Feature_Understanding_Template.md`, `Feature_Spec_Template.md`, `TODO_Template.md`, or Master Index §2.2. Do not ship a pack bump that changes the live scaffold without a Step B strip for existing copies.

## D3 — Build-first is first-class

**Decision:** Profile is a product choice, not a concession. **`build-first`** is the right default for typed APIs, CRUD, and clear contracts. **`prevent`** is the right default for editors, games, and multi-surface / identity-risky apps. Unset still means `prevent` so those repos do not lose the gate (D13).

**Do not:** Frame build-first as “if you prefer less ceremony” or “for people in a hurry.”

## D4 — Pack decision log at repo root

**Decision:** Lasting pack choices live in this file. Consumer projects use `docs/decisions/` / spec Decisions tables. Bootstrap deletes this file from user copies.

## D5 — Eval integrity in pack-checks

**Decision:** `python3 eval/run_eval.py` (no model) stays on `.github/workflows/pack-checks.yml`. Cases include **fail-snapshots** a wrong agent output must fail. Grow from integrity; prepare/verify remains the behavioral loop.

**Named fail modes to keep covered:** wrong-engine build; operable-gap marked done; build-first skipping Understanding under **prevent**; inventing Understanding under **build-first**; invented-decision Assumptions / example-as-identity.

## D6 — Standing is not a notes pad

**Decision:** `standing.instructions` holds lasting **ADT playbook overrides** only. Missing / empty is correct. Do not quiz for standing. Do not copy example bullets into live settings. The seven `orchestrator.git.mode` values stay the menu; custom handling (merge commit, rebase-merge, always squash before ready for a HEAD-only reviewer, custom close-out) is a **write-in on that ask**, not an eighth mode.

**Do not:** Add an eighth git mode for merge-commit / rebase-merge / HEAD-only squash. Do not quiz for standing on the git-mode ask — mention the write-in on that menu only.

## D7 — Host worktrees are playbook-only

**Decision:** No `orchestrator.git.worktrees` key. Detect a host worktree and stay. Pack does not `git worktree add`. No host isolation → serial implementers.

## D8 — Milestone ≠ one TODO

**Decision:** `milestone-pr` groups related TODOs and may spawn concurrent implementers when work does not overlap **and** the host can isolate. Squash-before-ready is not part of this cut (D25).

## D9 — Do not migrate a set git mode

**Decision:** Sync / pack recommend must not rewrite `orchestrator.git.mode` once set. Exception: explicit user ask this turn (`source: user`). Cloud Agent may this-run `milestone-pr` without writing the file.

## D10 — Additive vs shape

**Decision:** Full de-confirm gate lives only in `workflow/understanding.md`. Additive work → spec + TODO, keep `confirmed`. De-confirm only on a significant is / is-not / surface / ownership change. Elsewhere: one-line pointers.

## D11 — Operable done

**Decision:** Library/tests `[x]` is not product-done on a user-facing stem. Need an exercise path, a loud phase, or `library-only`. Open operable Acceptance with no covering TODO is incomplete.

## D12 — Finished-kit covering TODOs

**Decision:** In-scope spec leftovers get implementable TODOs on an **existing** stem. Filling those rows is not inventing work. No empty map rows for vague planned-only items. No wait-for-pickup.

## D13 — Unset profile is prevent

**Decision:** Missing `docs_profile.mode` → treat as `prevent`. Do not invent `build-first` because Understanding files are missing.

## D14 — Pack vs consumer tree

**Decision:** GitHub Release zip is `docs/templates/` only. Root `eval/`, `scripts/`, this file, pack-checks workflow, issue forms, FUNDING, release.yml, and pack `.cursor/environment.json` are upstream-only and must not stay in a user’s app.

## D15 — Thin workflow index

**Decision:** `Modular_Docs_Workflow.md` is paved path + router. Full procedure lives in one `workflow/` module. Do not re-inflate the monolith.

## D16 — Roles are opt-in; orchestrator stays parent

**Decision:** Doc-role adapters are never always-on. Orchestrate **and bootstrap** run in the parent session only — never install/spawn an `orchestrator` or `docs-bootstrap` subagent type. Bootstrap is what *installs* the adapters.

## D17 — Lock obvious; Assumptions are real forks

**Decision:** Full lock-gate prose lives only in `workflow/understanding.md` §4. Agents lock the obvious best default into **is / is not** without asking. **Assumptions** hold only real forks (no obvious winner). Empty Assumptions is success. If the design is already clear, **zero Assumption asks is correct** — do not invent a quiz. Do **not** treat examples in `docs/reference/` / chat as the target unless the user **clearly set them as the target**. Ask about a **lesser path** only when a **real non-timescale reason** exists (hard blocker, legal, missing credential) — not to offer an MVP / half-measure that lands 10 minutes faster (agent timescale). Offer an **`optional-assumption-cleanout`** pass on existing Understandings. Elsewhere: one-line pointers.

**Do not:** Treat “needs user confirmation” as a license to invent quizzes. Do not promote a reference example into identity or a spec constraint. Do not offer a lesser path to save sprint time.

## D18 — Sync summary is the union, not the catalog

**Decision:** A sync summary reports **from→to**, the **unioned** Live impact tags, and executed / offered / declined **of those tags**. The CHANGELOG / Step B tag table is a lasting capability catalog. A tag fires only when a selected catch-up entry lists it. Do **not** name catalog optional tags that were not in the union as “skipped” — that reads as missed instructions. `auto-all` means: when a tagged pass is in the union, execute it on all Document Map stems without asking. It does **not** mean run every optional pass every sync. Reserve “skipped” for a unioned tagged pass the user declined (`choose`) or a path check that did not apply (B8 modern layout).

**Do not:** Treat the tag table as a per-sync checklist. Do not invent a broader audit than the union to “cover” catalog rows that sit behind the old stamp.

## D19 — Team inbox is optional and non-forcing

**Decision:** `team_inbox` is an optional ADT-settings key for projects that want a human *or* a designated team-bot assignee on Human-TODO (and optionally human-gated feature TODO rows). Omit / unset / `enabled: false` = today’s human-only inbox (**no auto-stamp**). Enabling opts into **assign-all-at-once**: stamp Assignee from `kind_defaults` on dual-write; one-shot *apply defaults to Open* backfill for leftover unassigned rows — **both** only when that `role_id` is Active on the roster (else leave `unassigned`). Do not re-stamp an explicit (claimed / reassigned) assignee. Claim / reassign is **override only**, not the bulk path. Bots discover work via “my open rows” / one digest ping — not one PR per claim. `kind_defaults` are the stamp map, still project-owned — not a mandatory org chart. Do not silent-enable, do not copy Brian’s (or any team’s) bot roster as pack-required defaults, do not auto-close without the assignee’s confirm report.

**Do not:** Treat team routing as the new default. Do not paste secrets or bot credentials into docs. Do not replace feature `*-TODO.md` ownership of code work. Do not require a per-row claim to fill Assignee when `team_inbox` is enabled. Do not backfill an id that is not Active on the roster.

## D20 — Team roster is two-stage (read vs self-ID)

**Decision:** When `team_inbox` is enabled, live **`docs/Team-Roster.md`** (from `Team_Roster_Template.md`) is the project-owned directory of **who exists** (**Name**), their **Jobs**, **Anti-jobs** *(only if defined — empty / `—` is correct)*, and **how to hand off**. `kind_defaults` stay the stamp map — stamp a `role_id` only when that id is **Active** on the roster. **Unset `team_inbox` → do not create the file.** When Name / Jobs / Anti-jobs / Follow-ups / Handoff **change**, the owning teammate updates **their** row the same turn (report-only asks the proxy). Do not leave a stale job on the roster.

**Two stages:** (1) A coding agent that received a **handoff** **reads** the roster and assigns only to Active ids. It must **not** invent bot rows or human names, copy example/other-project rosters, or backfill Active from `kind_defaults` / pack doc-roles / installed harness agents. Empty Active is correct. Missing default → `unassigned` (do not fallback-stamp leftover `human` for human-gated kinds). (2) **Teammates identify themselves** — named humans and bots write or refresh **their own** row only. **Report-only** bots do not edit the roster; they ask another bot/agent or the human to add **one** requested row. A human naming a teammate *this turn* may be written as that one row. That is user fill-in, not invention.

**One initial PR:** standing up `team_inbox` or adding a **full team** is **one scribe / one PR** that creates the roster (plus settings if needed). Other bots do **not** open competing `Team-Roster.md` PRs — join the open roster PR or wait for merge, then self-ID. Later one-bot updates may be their own PR, one writer at a time.

**Do not:** Silent-create `Team-Roster.md` on a human-only inbox. Do not treat pack adapters as roster bots. Do not paste secrets or bot credentials. Do not copy Brian’s (or any team’s) roster into the template as live defaults. Do not invent anti-jobs. Do not race N roster-create PRs.

---

## D21 — Product vision is the whole-product end-state

**Status:** superseded by **D23** (2.9.3). Create-on-`prevent`-only / omit-on-`build-first` is reversed. End-state-picture job stays.

**Decision:** Live **`docs/Product-Vision.md`** (from `Product_Vision_Template.md`) is the cohesive **end-state picture** for the product — what it is / is not as **one** thing, plus how existing Document Map stems fit that whole. Per-feature Understandings and the Document Map stay the inventory of pieces. Master Index §1 stays a short overview. A complete feature map without this file can still be the wrong product.

**Create (2.9.0):** **`prevent`** (and unset → prevent) at bootstrap / first live-docs build / 2.9.0 sync. **`balanced`** when 2+ feature stems or whole-product identity is fuzzy. **`build-first`:** omit unless *lock product shape* / identity fight / file already exists. **Draft source:** peek `docs/reference/` first (idea/identity exports); then fit existing map rows. **Do not** reconstruct the picture from the Document Map / feature Understandings / specs. **Draft does not add a second hard coding gate.** **Confirmed** vision: do not implement a feature that fights it. Lock gate and real-fork Assumptions are Workflow §4 (do not restate). Empty Assumptions is success. Do not invent anti-product quizzes. Do not treat `docs/reference/` examples as the target unless clearly set. End-state picture is **not** a feature checklist or a phased roadmap.

**Do not (2.9.0):** Silent-create on `build-first`. Paste the vision into every Understanding. Turn Master Index into the end-state essay. De-confirm on an additive feature that still fits the picture. Skip `reference/` because the map looks complete.

---

## D22 — Named humans are first-class roster assignees

**Decision:** When `team_inbox` is enabled, human teammates put **themselves** on `docs/Team-Roster.md` with **their own** `role_id` / Name (slug of their name — `alex`, not leftover `human`). Human-TODO stays the inbox of *work*. Assignee is the named person’s slug so follow-ups go to that person. Generic `human` is an **optional leftover bucket** for unsigned human work, and only stamps when that id is Active. Missing Active default → `unassigned` so later *apply defaults to Open* can move the row after a bot or named human self-IDs.

**Do not:** Dump every human onto leftover `human` / treat Human-TODO as the people directory. Do not invent human names. Do not fallback-stamp `human` for human-gated kinds when no Active row matches. Do not silent-enable `team_inbox` so people can “have a roster.”

---

## D23 — Destination file always; gate only after lock + confirm

**Decision:** Documenting the destination and gating implementation are **two jobs**. **Always create** a lightweight `docs/Product-Vision.md` (bootstrap / first live-docs / TEMPLATE_SYNC if missing) on **every** profile, including `build-first`. **`prevent`:** status `draft`; user confirms product shape; Understanding confirm still gates that stem. **`balanced`:** always the file; deepen when 2+ stems / fuzzy whole / *lock product shape*; Understanding rules unchanged. **`build-first`:** file is informative and evolving — **not a gate**. Agents read it for destination; they do **not** wait for confirm before spec/TODO work. *Lock product shape* is the only build-first path that starts a confirm gate (identity fight / whole-product fork). After lock + confirm, do not implement a fighting feature. Unset profile still treats as prevent. Draft source unchanged (D21): peek `docs/reference/` first; do not rebuild from the map. Empty Assumptions is success.

**Do not:** Omit the file on `build-first`. Treat `draft` vision as a coding blocker on `build-first`. Invent Understandings under `build-first`. Invent anti-product quizzes. Rebuild the picture from the Document Map. Turn Master Index §1 into the vision essay. Paste the vision into every Understanding. De-confirm on an additive feature that still fits.

---

## D24 — Route the lesson where it is needed

**Decision:** A pack lesson that lives only in the playbook where it was discovered is invisible under “open only the one module the router names.” Two field misses (dirty-tree / worktree stale-docs only in TEMPLATE_SYNC A0 + orchestrator-git; do-not-edit-templates only in RULE_INSTALL + TEMPLATE_SYNC) are the same shape: the knowledge existed, the routing did not.

**Where it must live:**

- **Docs as source of truth** depend on this checkout’s `docs/` being current. Session default (always-loaded rule + paved path) runs a cheap `git status` + `git worktree list` **before** treating Master Index / TODOs as current. Sibling worktree with **newer `docs/` content** (`git diff`) or uncommitted sibling `docs/` → hard stop. Ancestry-only (`git log HEAD..<other> -- docs` after squash-merge) is not drift (D26). Dirty **this** tree is a note, not an implement hard stop (A0 stays the overwrite hard stop). Full procedure: `workflow/session-freshness.md`. Host worktrees “stay” is isolation — stay ≠ current.
- **Pack-owned `docs/templates/`** warning lives at `docs/templates/README.md` (where an agent wanders to “fix a rule”), not only in install/sync playbooks.
- **Bootstrap is parent-only** — same as orchestrator. A `docs-bootstrap` harness adapter is installed *by* bootstrap / rule-install, so it cannot exist for the first (and usual) bootstrap ask. Keep `roles/bootstrap.md` as an in-session wrapper; never generate or install `docs-bootstrap` adapters. Sync B deletes leftovers.
- **Docs-overlapping PRs** — live TODO/spec/Understanding are rewritten every session. Two PRs on the same stem conflict even when `src/` files differ. Session default + Grok parent spawn path: list open PRs; add to the PR that already owns that stem’s docs. Do not leave this only in `tools/grok-build.md` (install-only). Orchestrator “do not share files” includes docs.

**Do not:** File the next field lesson only in the playbook that first hit it. Do not skip session freshness because Current focus “looks recent.” Do not treat already-in-a-worktree as proof the docs are current. Do not omit `rules` on a bump that changes the always-loaded session default (installed copies would not get the gate). Do not re-add a `docs-bootstrap` adapter “for completeness.” Do not spawn a new Grok coding agent + PR per successive complaint on a stem that already has an open PR.

---

## D25 — Bugbot reads the PR until ready

**Decision:** Squash-before-ready is **not** required for Bugbot. Bugbot reviews the **PR** (all commits) until the PR is marked ready. Commits that follow ready are tip-only. `milestone-pr` marks ready on the milestone’s existing commits, waits CI/Bugbot, then squash-merges at the forge. **`branch-pr-squash`** stays the one-morning-PR option. A reviewer that **only ever reads HEAD** (another product, or a standing preference) is a write-in: *always squash before mark ready*.

**Do not:** Restore mandatory squash-before-ready “so tip-only bots see the whole cut.” Do not add an eighth git mode for HEAD-only reviewers. Do not treat forge squash-merge (how the slice lands on default) as the same as rewriting the PR branch before ready.

---

## D26 — Sibling docs drift is content, not ancestry

**Decision:** The session-freshness sibling probe hard-stops on **uncommitted sibling `docs/`** or **`git diff --quiet HEAD <other-HEAD> -- docs` failing**. `git log HEAD..<other-HEAD> -- docs` only **names** commits in a real stop message. Squash-merge (GitHub default; `branch-pr-squash`; standing squash-before-ready) severs ancestry: the worktree is “behind” on the graph and **identical** on `docs/` content. That is not drift. A pre-merge re-check does not catch the state the squash **creates**; the content verdict does.

**Do not:** Verdict sibling drift from `git log HEAD..<other> -- docs` alone. Do not restore “this HEAD lacks `docs/` commits the other tree has” as a hard stop.

---

## D27 — Profile value `ship-first` is renamed `build-first`

**Decision:** The docs-profile mode for typed APIs / CRUD / clear contracts is **`build-first`**. The behavior is unchanged from D3 (spec + TODO, no Understanding gate, not a concession). The old settings value **`ship-first`** is a legacy spelling of the same mode. TEMPLATE_SYNC **B0.1b** (every sync) and Workflow §0.1 (on sight) rewrite `docs_profile.mode` from `ship-first` to `build-first`. Do not re-ask. Do not treat the old value as unset. This is a rename, not a migrate of a chosen profile (D9 still forbids rewriting a set `orchestrator.git.mode`).

**Do not:** Leave live settings on `ship-first`. Do not invent a second mode. Do not frame `build-first` as ceremony-off or for people in a hurry (D3).

---

## D28 — Slash commands are opt-in

**Decision:** `optional_rules.slash-commands` is an optional menu for two asks: `/sync` and `/orchestrate`. They point at the same playbooks as the short asks. Missing / unset means ask once (bootstrap Step 3p **F**, sync step 10, rule install). **Decline** is correct when the user would rather just ask. Do not silent-enable except under `sync.mode: auto-all` (same as other unset optionals). Do not add more commands. Cursor, Claude Code, and Copilot get the files. Other tools record the choice and install nothing.

**Do not:** Make slash commands the paved path. Do not install them when the key is missing or declined. Do not paste playbook bodies into the command files.

---

## D29 — Repo behavior that is not pack behavior

**Decision:** `standing.instructions` stays ADT playbook overrides only (D6). When the user tells the agent **how to act in this repo** and that guideline does **not** change an ADT playbook, the agent **asks once**: an always-on **rule / instruction**, or a **skill** opened when that kind of work comes up. It does not write standing. It does not create the rule or skill before the answer. Product/UI for one stem stays on spec Decisions. **Sync cleanout (2.9.6):** when that version is in catch-up, remove non-pack behavior from standing and ask once per removed bullet: rule, skill, or dropped. Do not leave it in standing until they answer. Do not silent-create under `auto` or `auto-all`.

**Do not:** File repo working guidelines in standing. Do not silent-create a rule or skill. Do not treat “make a rule” as the only home — always-on is the rule, loaded-when-needed is the skill.

---

## D30 — Sticky outcomes

**Decision:** D11 still requires an exercise path on a user-facing stem. D30 adds the sticky row. Each operable Acceptance line has an unchecked `## Outcomes` row. Child tasks stay flat and carry `outcome: <slug>`. Completing the children does not check the outcome or that Acceptance line. Only the outcome audit may check them, and only when a Completed exercise item cites a path, a date, and an observation that the scenario held. A Completed break note does not spawn a second Exercise in that same pass; it spawns cited follow-ups. An empty High/Medium/Low list while an outcome is open is not stem-drained. The sync pass `optional-todo-outcomes` retrofits existing stems; it does not invent the remaining path from a code diff. Todo warden is the only role that creates a human-verify playtest, and only after that passing note.

**Do not:** Nest children under a parent checkbox. Do not let a slice check operable Acceptance. Do not treat warden `clean` plus an open outcome as feature done. Do not let the orchestrator or implementer write a human-verify playtest. Do not ask the human to look at an outcome that is still open.

---

## Public example

[xAIkit](https://github.com/BrianCLowe/xAIkit) used this pack on a typed API (a natural **build-first** fit).
