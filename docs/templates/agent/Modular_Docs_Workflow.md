> **Agent workflow index.** Paved path + router into thin modules under [`workflow/`](workflow/README.md). Sync from upstream; do **not** copy wholesale into `docs/Master_Index.md`. The live index links here; agent rules summarize and point here — then open **one** module when needed.

# Modular Documentation — Agent Workflow

**Pack version:** read [`VERSION`](../VERSION) (`pack-version`). Do not copy the number into this file. Live Master Index is stamped on bootstrap / TEMPLATE_SYNC.

**Design intent:** Short user asks → **one** playbook (`BOOTSTRAP`, `TEMPLATE_SYNC`, `TEMPLATE_UPDATE_CHECK`, `RULE_INSTALL` → `tools/<key>.md`, roles, or this index → **one** workflow module). Do not scan the pack catalog. **Tight scope** = paved path only (not “audit every alternate”). Edge cases live in modules — load them only when the router says so. Live scaffolds are fill-in blanks — teaching lives in [`../help/SCAFFOLDS.md`](../help/SCAFFOLDS.md) and the module you open.

**Compaction / new session / memory loss:** If you cannot recall the paved path, **re-open this index**, then only the matching router module. Do not reconstruct procedure from a live Understanding or spec or from chat memory.

**Docs profile:** `docs/ADT-settings.yaml` → `docs_profile.mode` — which docs to write. **`build-first`** = typed APIs / CRUD. **`prevent`** = editors / games / multi-surface (default if unset). **`balanced`** = mixed. Full rules → [`workflow/profile-standing.md`](workflow/profile-standing.md). Never silent-downgrade a project full of Understandings. Not a coding gate.

**Optional roles:** [`roles/`](roles/README.md) — never always-on; parent spawns when adapters exist, else playbook in-session. **Bootstrap** = parent only ([`BOOTSTRAP.md`](BOOTSTRAP.md)). Documentation roles only: Understanding author, doc graduate, template sync.

---

## Paved path *(default — prefer this)*

Use when the stem is already **ready** under the docs profile and scope is unchanged:

1. **Docs freshness** (cheap): `git status --porcelain` + `git worktree list`. Clean + one worktree → continue. Two or more worktrees → sibling probe in [`workflow/session-freshness.md`](workflow/session-freshness.md) (drift = uncommitted sibling `docs/` or `docs/` **content** differs — not ancestry-only after squash-merge). Dirty **this** tree: one line, continue (do not auto-commit). **New PR / successive spawn:** if an open PR already touches this stem’s spec or Understanding → add there (docs overlap ≠ code overlap)
2. Read `docs/ADT-settings.yaml` → `docs_profile.mode` (else **prevent**); **`standing.instructions` if non-empty**
3. [`Master_Index.md`](../../Master_Index.md) — Sections 1–3 only. Read [`Product-Vision.md`](../../Product-Vision.md) (especially when `confirmed`)
4. That stem’s spec and Understanding *(if any)*. Do the instructed task. A gap those docs already make obvious is part of the instruction. Do **not** create a `*-TODO.md`. There is no Current focus. Do **not** document a fight with a **confirmed** product vision
5. **Stop.** Do **not** open workflow modules unless a row in the router below matches.

**Docs on a new stem:**

| Profile | Files |
|---------|--------|
| **`prevent`** | Spec + Understanding |
| **`balanced`** | Spec; Understanding when identity is ambiguous |
| **`build-first`** | Spec. Draft Product-Vision is not a documentation gate |

**Additive vs shape (one line):** On a `confirmed` Understanding, a new research angle / extra behavior / edge case that still fits **is / is not** → **spec**, keep `confirmed`. De-confirm / re-draft **only** on a significant shape change — full rule in [`workflow/understanding.md`](workflow/understanding.md#4-understanding-features--shared).

**Same-turn prefs:** Product/UI correction that could be “improved away” → spec **Decisions** ([`workflow/decisions.md`](workflow/decisions.md)). **Override an ADT playbook** (no first-class key) → standing ([`workflow/profile-standing.md`](workflow/profile-standing.md)). How to act in this repo that is **not** a pack playbook → ask once: always-on rule/instruction, or a skill (§0.2). Do not jot that into standing. Do not jot random notes into standing.

---

## Router — open only the matching module

| Situation | Open only |
|-----------|-----------|
| Docs profile unset / suggest / upgrade | [`workflow/profile-standing.md`](workflow/profile-standing.md) (§0.1) |
| Standing / playbook-override LOOKOUT | [`workflow/profile-standing.md`](workflow/profile-standing.md) (§0.2) |
| Session start / dirty sibling worktree / docs may be stale / about to merge live docs / new PR or successive spawn on same-stem docs | [`workflow/session-freshness.md`](workflow/session-freshness.md) (§0.3) |
| Creating files / new Document Map row / split stem / inventory vs new row | [`workflow/naming-layout.md`](workflow/naming-layout.md) (§0) |
| `_shared/` vs feature / foundation task placement | [`workflow/shared-components.md`](workflow/shared-components.md) (§1) |
| Draft / revise Understanding · de-confirm gate · lock gate · assumption clean-out · relocate | [`workflow/understanding.md`](workflow/understanding.md) (§4) |
| Whole-product vision / end-state picture / product vs feature fight | [`workflow/product-vision.md`](workflow/product-vision.md) (§4.5) |
| Graduate confirmed shape → durable spec | [`workflow/understanding.md`](workflow/understanding.md) (§2) |
| Which docs to open for a stem | [`workflow/implement.md`](workflow/implement.md) (§3) |
| Spec Decisions (product/UI) | [`workflow/decisions.md`](workflow/decisions.md) (§10) |
| Install tooling / Project verify handoff | [`workflow/tooling.md`](workflow/tooling.md) (§11) |
| Human inbox dual-write | [`workflow/human-todo.md`](workflow/human-todo.md) (§13) |
| Team inbox · roster (read vs self-ID) | [`workflow/team-roster.md`](workflow/team-roster.md) — only when `team_inbox` is enabled |
| Game extensions · Catalog · sub-index · split large doc · Mermaid | [`workflow/extensions.md`](workflow/extensions.md) (§6–9 · §12) |
| User asks “how does the workflow work?” | This index — then one module if they need depth |

**Do not** open every module. **Do not** re-read this index every turn once you know the paved path. Module list for maintainers: [`workflow/README.md`](workflow/README.md).

**Not this pack:** work checklists, Current focus, implementation roles, git-delivery settings. The harness owns how code is written, verified, and landed.

---

## Compatibility anchors *(deep links → modules)*

Older Master Index / help links land on these headings. Prefer the router table above for new work.

### 0.1 Docs profile *(ceremony modes)*

Full procedure: [`workflow/profile-standing.md`](workflow/profile-standing.md#01-docs-profile-ceremony-modes).

### 0.2 Standing workflow instructions *(user workflow, not pack enums)*

Full procedure: [`workflow/profile-standing.md`](workflow/profile-standing.md#02-standing-workflow-instructions-user-workflow-not-pack-enums).

### 0.3 Session freshness *(docs as source of truth)*

Full procedure: [`workflow/session-freshness.md`](workflow/session-freshness.md). Cheap `git status` + worktree list on the paved path; open-PR check before a new PR / successive spawn. Open the module only when sibling `docs/` drift or docs-overlapping PRs flag.

### 0. Naming & file layout *(read before creating files)*

Full procedure: [`workflow/naming-layout.md`](workflow/naming-layout.md#0-naming--file-layout-read-before-creating-files).

### 1. Shared Components — Foundation vs Consumption

Full procedure: [`workflow/shared-components.md`](workflow/shared-components.md#1-shared-components--foundation-vs-consumption).

### 2. Understanding → Spec graduation

Full procedure: [`workflow/understanding.md`](workflow/understanding.md#2-understanding--spec-graduation).

### 3. Quick Start — Working on Any Task

Paved path is above. Path A/B detail: [`workflow/implement.md`](workflow/implement.md#3-quick-start--working-on-any-task).

### 4. Understanding (Features & Shared)

Full procedure (incl. **de-confirm gate** + **lock gate**): [`workflow/understanding.md`](workflow/understanding.md#4-understanding-features--shared).

### 5. TODO Management *(retired)*

Retired in 2.10.0. The pack does not keep a feature TODO or a Current focus. Do not recreate them. Existing `*-TODO.md` files may stay on disk; do not extend them and do not treat them as the work list. A sync that crosses 2.10.1 offers to delete feature and shared `*-TODO.md` files and says why ([`TEMPLATE_SYNC_B.md`](../TEMPLATE_SYNC_B.md) B0.7). That offer is the step. `auto-all` is not a yes. `Human-TODO.md` stays.

### 7.1 Catalog companions *(list-heavy content)*

See [`workflow/extensions.md`](workflow/extensions.md#71-catalog-companions-list-heavy-content).

### 8. How to Split a Large Document

See [`workflow/extensions.md`](workflow/extensions.md#8-how-to-split-a-large-document).

### 10. Decisions *(lightweight)*

See [`workflow/decisions.md`](workflow/decisions.md#10-decisions-lightweight).

### 11. Tooling *(new machine setup)*

See [`workflow/tooling.md`](workflow/tooling.md#11-tooling-new-machine-setup).

### 4.5 Product vision *(whole-product end-state)*

See [`workflow/product-vision.md`](workflow/product-vision.md#45-product-vision). Create on **all** profiles (lightweight on `balanced` / `build-first`). **`build-first`:** not a gate until *lock product shape*.

### 13. Human TODO *(inbox — needs a human)*

See [`workflow/human-todo.md`](workflow/human-todo.md#13-human-todo-inbox--needs-a-human). Optional `team_inbox` in `ADT-settings.yaml` (omit / unset = human-only). When it is enabled, open [`workflow/team-roster.md`](workflow/team-roster.md) (read vs self-ID).

---

## Instructions for AI Agents

- **Docs freshness** = *are this tree’s docs the ones the user means?* — [`workflow/session-freshness.md`](workflow/session-freshness.md). Run before treating Master Index as current.
- **Master_Index.md** = *what this project is* and *where files live*.
- **Product-Vision.md** = *the whole-product end-state* — [`workflow/product-vision.md`](workflow/product-vision.md). Feature map alone is not identity. **`build-first`:** destination, not a gate.
- **This file** = *how to work* — paved path first; then **one** module from the router.
- **Tooling.md** = *what to install on a new machine* (not package deps) — [`workflow/tooling.md`](workflow/tooling.md).
- **Human-TODO.md** = *what only a human can close* — [`workflow/human-todo.md`](workflow/human-todo.md). Optional `team_inbox` (unset = human-only) → [`workflow/team-roster.md`](workflow/team-roster.md). **Team-Roster.md** = who exists + handoff (create only when enabled; do not invent teammates).
- The installed agent rule ([`Modular_Documentation_Rule.mdc`](Modular_Documentation_Rule.mdc)) is a short checklist — open this index when creating files, Path A/B, graduation, profile/standing questions, or the user asks about procedure; then open only the named module.
