<!-- pack-version: 2.7.17 -->

> **Agent workflow index.** Paved path + router into thin modules under [`workflow/`](workflow/README.md). Sync from upstream; do **not** copy wholesale into `docs/Master_Index.md`. The live index links here; agent rules summarize and point here — then open **one** module when needed.

# Modular Documentation — Agent Workflow

**Pack version**: 2.7.17 *(same as `docs/templates/VERSION` / live Master Index **Pack version**)*

**Design intent:** Short user asks → **one** playbook (`BOOTSTRAP`, `TEMPLATE_SYNC`, `TEMPLATE_UPDATE_CHECK`, `RULE_INSTALL` → `tools/<key>.md`, roles, or this index → **one** workflow module). Do not scan the pack catalog. **Tight scope** = paved path only (not “audit every alternate”). Edge cases live in modules — load them only when the router says so.

**Docs profile:** `docs/ADT-settings.yaml` → `docs_profile.mode` — **`prevent`** (default if unset) · **`balanced`** · **`ship-first`**. Full rules → [`workflow/profile-standing.md`](workflow/profile-standing.md). Never silent-downgrade a project full of Understandings.

**Optional roles:** [`roles/`](roles/README.md) — never always-on; parent spawns when adapters exist, else playbook in-session. **Orchestrator** = parent only ([`roles/orchestrator.md`](roles/orchestrator.md) + git [`roles/orchestrator-git.md`](roles/orchestrator-git.md)). Single-slice implement → [`roles/feature-implementer.md`](roles/feature-implementer.md).

---

## Paved path *(default — prefer this)*

Use when the stem is already **ready** under the docs profile and scope is unchanged:

1. Read `docs/ADT-settings.yaml` → `docs_profile.mode` (else **prevent**); `orchestrator.git.mode` when relevant; **`standing.instructions` if non-empty**
2. [`Master_Index.md`](../../Master_Index.md) — Sections 1–3 only
3. Active TODO **Current focus** → that item’s Understanding *(if any — read-only)* → spec → code
4. **Stop.** Do **not** open workflow modules unless a row in the router below matches.

**Ready when:**

| Profile | Ready to code |
|---------|----------------|
| **`prevent`** | Understanding is `confirmed` (or user waived) and scope unchanged |
| **`balanced`** | If stem has Understanding → same as prevent; if none → thin spec + TODO exist and identity is clear |
| **`ship-first`** | Spec + TODO exist for the stem; no Understanding required |

**Additive vs shape (one line):** On a `confirmed` Understanding, a new research angle / extra behavior / edge case that still fits **is / is not** → **spec + TODO**, keep `confirmed`. De-confirm / re-draft **only** on a significant shape change — full rule in [`workflow/understanding.md`](workflow/understanding.md#4-understanding-features--shared).

**Same-turn prefs:** Product/UI correction that could be “improved away” → spec **Decisions** ([`workflow/decisions.md`](workflow/decisions.md)). Pack/process always-never → standing or first-class key ([`workflow/profile-standing.md`](workflow/profile-standing.md)).

---

## Router — open only the matching module

| Situation | Open only |
|-----------|-----------|
| Docs profile unset / suggest / upgrade | [`workflow/profile-standing.md`](workflow/profile-standing.md) (§0.1) |
| Standing / process prefs / LOOKOUT capture | [`workflow/profile-standing.md`](workflow/profile-standing.md) (§0.2) |
| Creating files / new Document Map row / split stem | [`workflow/naming-layout.md`](workflow/naming-layout.md) (§0) |
| `_shared/` vs feature / foundation task placement | [`workflow/shared-components.md`](workflow/shared-components.md) (§1) |
| Draft / revise Understanding · de-confirm gate · relocate | [`workflow/understanding.md`](workflow/understanding.md) (§4) |
| Graduate confirmed shape → durable spec | [`workflow/understanding.md`](workflow/understanding.md) (§2) |
| Path A vs Path B unclear · readiness table detail | [`workflow/implement.md`](workflow/implement.md) (§3) |
| TODO layout · Current focus · operable done · exploration | [`workflow/todos.md`](workflow/todos.md) (§5) |
| Spec Decisions (product/UI) | [`workflow/decisions.md`](workflow/decisions.md) (§10) |
| Install tooling / Project verify handoff | [`workflow/tooling.md`](workflow/tooling.md) (§11) |
| Human inbox dual-write | [`workflow/human-todo.md`](workflow/human-todo.md) (§13) |
| Game extensions · Catalog · sub-index · split large doc · Mermaid | [`workflow/extensions.md`](workflow/extensions.md) (§6–9 · §12) |
| User asks “how does the workflow work?” | This index — then one module if they need depth |

**Do not** open every module. **Do not** re-read this index every turn once you know the paved path. Module list for maintainers: [`workflow/README.md`](workflow/README.md).

**Timescale / build green:** target architecture when shape is clear ([`Agent_Timescale_Planning_Rule.mdc`](Agent_Timescale_Planning_Rule.mdc)). Build green before “you can test” ([`Agent_Build_Verify_Rule.mdc`](Agent_Build_Verify_Rule.mdc)). Operable done detail → [`workflow/todos.md`](workflow/todos.md) §5.3.

---

## Compatibility anchors *(deep links → modules)*

Older Master Index / help links land on these headings. Prefer the router table above for new work.

### 0.1 Docs profile *(ceremony modes)*

Full procedure: [`workflow/profile-standing.md`](workflow/profile-standing.md#01-docs-profile-ceremony-modes).

### 0.2 Standing workflow instructions *(user workflow, not pack enums)*

Full procedure: [`workflow/profile-standing.md`](workflow/profile-standing.md#02-standing-workflow-instructions-user-workflow-not-pack-enums).

### 0. Naming & file layout *(read before creating files)*

Full procedure: [`workflow/naming-layout.md`](workflow/naming-layout.md#0-naming--file-layout-read-before-creating-files).

### 1. Shared Components — Foundation vs Consumption

Full procedure: [`workflow/shared-components.md`](workflow/shared-components.md#1-shared-components--foundation-vs-consumption).

### 2. Understanding → Spec graduation

Full procedure: [`workflow/understanding.md`](workflow/understanding.md#2-understanding--spec-graduation).

### 3. Quick Start — Working on Any Task

Paved path is above. Path A/B detail: [`workflow/implement.md`](workflow/implement.md#3-quick-start--working-on-any-task).

### 4. Understanding (Features & Shared)

Full procedure (incl. **de-confirm gate**): [`workflow/understanding.md`](workflow/understanding.md#4-understanding-features--shared).

### 5. TODO Management

Full procedure: [`workflow/todos.md`](workflow/todos.md#5-todo-management). Current focus §5.1 · exploration §5.2 · operable §5.3 live in that file.

### 5.1 Session handoff — Current focus

See [`workflow/todos.md`](workflow/todos.md#51-session-handoff--current-focus).

### 7.1 Catalog companions *(list-heavy content)*

See [`workflow/extensions.md`](workflow/extensions.md#71-catalog-companions-list-heavy-content).

### 8. How to Split a Large Document

See [`workflow/extensions.md`](workflow/extensions.md#8-how-to-split-a-large-document).

### 10. Decisions *(lightweight)*

See [`workflow/decisions.md`](workflow/decisions.md#10-decisions-lightweight).

### 11. Tooling *(new machine setup)*

See [`workflow/tooling.md`](workflow/tooling.md#11-tooling-new-machine-setup).

### 13. Human TODO *(inbox — needs a human)*

See [`workflow/human-todo.md`](workflow/human-todo.md#13-human-todo-inbox--needs-a-human).

---

## Instructions for AI Agents

- **Master_Index.md** = *what this project is* and *where files live*.
- **This file** = *how to work* — paved path first; then **one** module from the router.
- **Tooling.md** = *what to install on a new machine* (not package deps) — [`workflow/tooling.md`](workflow/tooling.md).
- **Human-TODO.md** = *what only a human can close* — [`workflow/human-todo.md`](workflow/human-todo.md).
- The installed agent rule ([`Modular_Documentation_Rule.mdc`](Modular_Documentation_Rule.mdc)) is a short checklist — open this index when creating files, Path A/B, graduation, profile/standing questions, or the user asks about procedure; then open only the named module.
