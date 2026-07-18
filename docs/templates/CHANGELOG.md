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

## 2.4

- **Live impact:** `process-docs-only`, `master-index`, `rules`
- **Files:**
  - `CHANGELOG.md` — (new) pack release map for Step B scope
  - `VERSION` — 2.3 → 2.4
  - `Master_Index_Template.md` — Key Locations: CHANGELOG + `docs/reference/` drop zone; At a Glance tight-scope; version markers
  - `Modular_Docs_Workflow.md` — session/Path B/reconciliation scope gates; tight-scope design intent; `docs/reference/` note; **do not invent `_shared/`** when nothing is shared; version markers
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
- **Step B:** Bump Master Index versions to 2.4; adopt Key Locations / At a Glance deltas (CHANGELOG, `reference/`, tight scope, **empty `_shared/` OK**); refresh installed modular rules if user wants (bodies changed); do **not** scan live feature/shared docs; do **not** invent new `_shared/` rows during sync. **`docs/templates/agent/upstream/`** attribution copies (README / LICENSE / CONTRIBUTING) may be **intentionally deleted** by the user (common after Claude/bootstrap cleanup) — do **not** treat that as a broken pack or re-download / restore those files; sync does not require them

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
