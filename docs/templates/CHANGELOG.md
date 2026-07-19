# Template pack changelog

> **Agents:** After Step A of [`agent/TEMPLATE_SYNC.md`](agent/TEMPLATE_SYNC.md), read **only the top entry** below. Follow its **Live impact** tags and **Step B** line — do not invent a broader audit.
>
> **Maintainers:** Every `VERSION` bump must update this file in the same commit (newest entry on top). Keep bullets brief. When editing agent playbooks, write for thorough “off-road” models — explicit scope gates and Do-not lists, not open “as needed” language (see root [`CONTRIBUTING.md`](../../CONTRIBUTING.md)).

**Live impact tags** (use only these):

| Tag | Meaning for Step B |
|-----|--------------------|
| `versions-only` | Bump Template / Workflow version in live Master Index; stop |
| `master-index` | Adopt structural deltas in live `Master_Index.md` (headings, Key Locations, Document Map columns) |
| `content-templates` | Scan live Understanding / Spec / TODO / Tooling / Human-TODO for *new* sections from those templates |
| `rules` | Offer to refresh installed agent rules from local pack (ask if customized) |
| `optional-upstream-check` | Update or offer `docs/upstream-status.yaml` / update-check rule |
| `process-docs-only` | Pack process/help/agent docs only — no live feature/shared content scan |

---

## 2.6

- **Live impact:** `content-templates`, `master-index`, `rules`, `process-docs-only`
- **Files:**
  - `VERSION` — 2.5 → 2.6
  - `Human_TODO_Template.md` — human **inbox** (not procurement-only): kinds `procure` · `playtest` · `decide` · `waiting`; checkbox Open table; **index + owner** model; human chat phrases; agent dual-write + sync-on-feedback
  - `TODO_Template.md` — Needs-a-human dual-write patterns; humans pointed at `Human-TODO.md` as inbox
  - `agent/Modular_Docs_Workflow.md` — §13 rewritten (inbox, dual-write, repair); version 2.6
  - `agent/Modular_Documentation_Rule.mdc` / `.instructions.md` — dual-write human-gated work; sync Human-TODO on user feedback
  - `agent/roles/feature-implementer.md` — dual-write language
  - `Master_Index_Template.md` — Human-TODO Key Locations / At a Glance / §3.3–3.4; versions 2.6; §13 anchor update
  - `agent/BOOTSTRAP.md`, `help/USAGE.md`, `help/SETUP.md`, `chat-ui/AGENT.md`, `agent/upstream-status.example.yaml`
  - Root `README.md` — pack 2.6; Human-TODO layout blurb
- **Step B:** Bump Master Index versions to 2.6; adopt Human-TODO Key Locations / At a Glance / Document Map wording. Add missing sections/columns from `Human_TODO_Template.md` and `TODO_Template.md` into live `Human-TODO.md` / feature TODOs (**do not** wipe Open/Done content — merge Kind/Owner columns and Instructions). Refresh installed modular rules if user wants (bodies changed). Optionally repair dual-write: human-gated items that exist only on feature TODOs → add thin Open rows on `Human-TODO.md`. Do **not** invent new procure/waiting rows; do **not** mark human items done without user confirmation.

## 2.5

- **Live impact:** `process-docs-only`, `master-index`, `rules`
- **Files:**
  - `VERSION` — 2.4 → 2.5
  - `agent/roles/` — **(new)** optional playbook roles: Understanding author, Doc graduate, Feature implementer, Bootstrap, Template sync + `README.md`; never always-on
  - `agent/roles/cursor/*.md` — Cursor **subagent** adapters → `.cursor/agents/` ([subagents docs](https://cursor.com/docs/subagents)); gated “Use when …”; not Agent Skills
  - `agent/roles/grok/*.md` — **(new)** Grok Build subagent adapters → `.grok/agents/`
  - `agent/roles/README.md` — harness adapter table (Cursor vs Grok vs Claude)
  - `agent/tools/` — **(new)** per-tool install/sync playbooks (`cursor`, `grok-build`, `claude-code`, `github-copilot`, `agents-md`, `openclaw`, thin `continue`/`cline`) + `README.md`; Claude `AGENTS.md` caveat; Grok `.grok/agents/` = CLI-documented + verify via `grok inspect` / playbook fallback
  - `agent/RULE_INSTALL.md` — router: ask/status yaml → open only `tools/<key>.md`; `optional_rules.doc-roles`
  - `agent/BOOTSTRAP.md` — Step 4c doc roles; installs via tool playbooks
  - `agent/TEMPLATE_SYNC.md` — rules refresh dispatches per installed tool; doc-roles via harness folders
  - `agent/rule-install-status.example.yaml` — `grok-build` + `doc-roles` path examples
  - `agent/Modular_Docs_Workflow.md` — optional roles + tools/ pointer; version 2.5
  - `agent/Modular_Documentation_Rule.mdc` / `.instructions.md` — parent orchestrates delegation/spawn (`.cursor/agents/`, `.grok/agents/`, …); `/` optional; fallbacks if agents missing
  - `Master_Index_Template.md` — Key Locations notes for `agent/roles/` + `agent/tools/`; versions 2.5
  - `help/USING_WITH_AGENTS.md` — slimmed human TOC → `tools/*.md`
  - `help/USAGE.md`, `help/SETUP.md` — roles / tools usage
  - `chat-ui/AGENT.md`, `agent/upstream-status.example.yaml` — version markers 2.5
  - Root `README.md` — pack 2.5; roles + tools in inventory
- **Unchanged content templates:** Feature_Understanding, Feature_Spec, TODO, Tooling, Human_TODO, Decision
- **Step B:** Bump Master Index versions to 2.5; adopt Key Locations deltas (`agent/roles/`, `agent/tools/`). For each `tools.*.status: installed`, open that `tools/<key>.md` only and refresh (ask if customized). If `optional_rules.doc-roles` is `enabled`, refresh harness agents folders (`.cursor/agents/` from `roles/cursor/`, `.grok/agents/` from `roles/grok/`, …). Remove any stale `.cursor/skills/modular-docs-*` leftovers. Do **not** open every tool file; do **not** scan live feature/shared docs; do **not** auto-enable doc roles if previously declined or unset.

## 2.4

- **Live impact:** `process-docs-only`, `master-index`, `rules`
- **Files:**
  - `CHANGELOG.md` — (new) pack release map for Step B scope
  - `VERSION` — 2.3 → 2.4
  - `Master_Index_Template.md` — Key Locations: CHANGELOG + `docs/reference/` drop zone; At a Glance tight-scope; version markers
  - `agent/Modular_Docs_Workflow.md` — **moved from pack root** into `agent/` (agent playbook, not a content template); session/Path B/reconciliation scope gates; tight-scope; `reference/`; no invented `_shared/`; version markers
  - `agent/TEMPLATE_SYNC.md` — changelog-first Step B + Do-not list; do not restore deleted `agent/upstream/` attribution files
  - `agent/upstream/README.md` — empty/deleted upstream copies are OK; sync must not re-fetch them
  - `agent/Modular_Documentation_Rule.mdc` — session default, route-by-ask, after-changes gates; tight-scope philosophy; no invented `_shared/`
  - `agent/Modular_Documentation_Rule.instructions.md` — same as `.mdc` body
  - `agent/BOOTSTRAP.md` — pack spot-check; map fill from conversation; auto-move clearly upstream README/LICENSE/CONTRIBUTING (no ask); create `docs/reference/README.md`; leave §3.1 empty unless truly shared
  - `agent/RULE_INSTALL.md` — bounded install-path checks
  - `agent/upstream-status.example.yaml` — example versions 2.4
  - `chat-ui/AGENT.md` — Master Index template only when asked; version markers
  - `help/SETUP.md` — tightened install flow (copy → bootstrap → layout → next links); less post-setup bullet pile
  - `help/USAGE.md` — deduped tips; patterns kept; bootstrap/sync shortened to point at SETUP/CHANGELOG
  - `help/USING_WITH_AGENTS.md` — sync wording (inventory links unchanged in role)
  - `help/IDEA_CAPTURE_TIPS.md`, `chat-ui/README.md` — full chat history tip; save under `docs/reference/`
  - Root `README.md` — rewritten landing page (how it works → get started → stay current; less inventory dump); Stay current caveat for packs before TEMPLATE_SYNC (pre-1.2)
  - Root `CONTRIBUTING.md` — changelog maintenance; maintainer note: write agent instructions for off-road / thorough models
- **Unchanged content templates:** Feature_Understanding, Feature_Spec, TODO, Tooling, Human_TODO, Decision
- **Step B:** Bump Master Index versions to 2.4; adopt Key Locations / At a Glance deltas (CHANGELOG, `reference/`, tight scope, **empty `_shared/` OK**); **retarget workflow links** to `docs/templates/agent/Modular_Docs_Workflow.md` (file moved out of pack root); if a stale copy remains at `docs/templates/Modular_Docs_Workflow.md`, remove it after the pack overwrite (Step A should already replace the whole folder). Refresh installed modular rules if user wants (bodies changed); do **not** scan live feature/shared docs; do **not** invent new `_shared/` rows during sync. **`docs/templates/agent/upstream/`** attribution copies may be **intentionally deleted** — do **not** re-download / restore them

## 2.3

- **Live impact:** `master-index`, `optional-upstream-check`, `process-docs-only`
- **Files:**
  - `VERSION` — 2.2 → 2.3
  - `Master_Index_Template.md` — VERSION in templates row; optional `upstream-status.yaml` Key Locations row
  - `Modular_Docs_Workflow.md` — process/version alignment
  - `agent/TEMPLATE_SYNC.md`, `agent/TEMPLATE_UPDATE_CHECK.md` — upstream check + sync stamp
  - `agent/Template_Update_Check_Rule.*`, `agent/upstream-status.example.yaml`, `agent/RULE_INSTALL.md`
  - `help/SETUP.md`, `help/USAGE.md`, `help/USING_WITH_AGENTS.md`, `chat-ui/AGENT.md`
- **Unchanged content templates:** Feature_Understanding, Feature_Spec, TODO, Tooling, Human_TODO, Decision
- **Step B:** Bump Master Index versions; adopt Master Index Key Locations deltas; link optional upstream check — do **not** scan live feature/shared docs
