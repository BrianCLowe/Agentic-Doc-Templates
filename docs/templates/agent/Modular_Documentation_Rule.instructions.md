---
name: Modular Documentation
description: Read Master_Index first; follow Modular_Docs_Workflow for procedure
applyTo: "**"
---

# Modular Documentation Rule

First, check if `docs/Master_Index.md` exists. If it does not exist, ignore this entire rule and work normally.

This project uses a lean modular documentation system. `docs/Master_Index.md` is the single entry point for **project context and the Document Map**. Full procedure: **`docs/templates/agent/Modular_Docs_Workflow.md`** — open it only when the gates below say so.

**Route by ask** *(open only that playbook — do not scan the pack catalog)*:

| User ask | Open only |
|----------|-----------|
| bootstrap / init modular docs | see **Optional subagents** → else `docs/templates/agent/BOOTSTRAP.md` |
| update / sync doc templates | see **Optional subagents** → else `docs/templates/agent/TEMPLATE_SYNC.md` |
| check for template updates | `docs/templates/agent/TEMPLATE_UPDATE_CHECK.md` |
| install agent rules | `docs/templates/agent/RULE_INSTALL.md` → then only `docs/templates/agent/tools/<key>.md` for each tool |
| draft / revise Understanding, new idea, capture intent, correct What this is / is NOT | see **Optional subagents** → else `docs/templates/agent/roles/understanding-author.md` |
| graduate confirmed Understanding → spec | see **Optional subagents** → else `docs/templates/agent/roles/doc-graduate.md` |
| implement / continue Current focus (Understanding `confirmed`, scope unchanged) | see **Optional subagents** → else session default below |
| feature / shared work (other) | `docs/Master_Index.md` + that feature’s or component’s files |

**Optional subagents** *(parent orchestrates — user need not type `/`; harness-agnostic)*:

When an ask matches a row below, look for a **named agent file** with that filename under **any** of: `.cursor/agents/`, `.grok/agents/`, `.claude/agents/`, `.codex/agents/`.

- If found → **delegate / spawn** that type with a self-contained prompt (feature/component name, paths, user’s ask). On Grok Build: `spawn_subagent` with `subagent_type: <name>` when `.grok/agents/<name>.md` exists. Do **not** treat `.cursor/agents/` as Grok types.
- If missing → follow the **Fallback** playbook/role **in this session** (or spawn a generic child with that playbook path).

| When ask matches | Agent filename | Fallback |
|------------------|----------------|----------|
| draft/revise Understanding, new idea, intent, identity correction | `understanding-author.md` | `docs/templates/agent/roles/understanding-author.md` |
| user confirmed Understanding → update durable spec | `doc-graduate.md` | `docs/templates/agent/roles/doc-graduate.md` |
| implement / continue from Current focus | `feature-implementer.md` | session default below |
| bootstrap / init modular docs | `docs-bootstrap.md` | `docs/templates/agent/BOOTSTRAP.md` |
| update / sync doc templates | `docs-template-sync.md` | `docs/templates/agent/TEMPLATE_SYNC.md` |

**Do not** delegate every message — only when a row above matches. Stay in this session for tiny follow-ups, clarifying questions only, or when the user says to stay here / skip subagents. These must not replace this rule or compete like always-on skill packs. Roles: `docs/templates/agent/roles/README.md`. Tool install paths: `docs/templates/agent/tools/README.md`.

**Session default** *(implement / continue when Understanding is `confirmed` and scope unchanged)*:
1. Read `docs/Master_Index.md` Sections 1–3.
2. Open the active TODO — read **Current focus** first (Workflow §5.1):
   - Shared foundation → `_shared/ComponentName-TODO.md`
   - Feature work → `features/FeatureName-TODO.md`
   - InEditor / Asset TODOs: only when Project Profile **Game extensions** / user indicates game-style work — default is **core TODO only**
3. Read that item’s `-Understanding.md` (context) and spec as linked — do not re-ask for review unless scope changes (Workflow §4).
4. Before integrating a **shared** piece, check its **Maturity** on the spec or Document Map (`draft` | `usable` | `stable`).
5. If the user asks to install tooling: follow **`docs/Tooling.md`** (Workflow §11) — Required (+ skills if listed); Optional only if asked; verify all; ask before admin/large SDKs.
6. If work needs an account, API key, cloud portal registration, or purchase: add/update **`docs/Human-TODO.md`** (Workflow §13) and link from the feature TODO — never store secrets in docs.

**Open `Modular_Docs_Workflow.md` only when:** creating files (§0 Naming), choosing Path A vs Path B, graduating Understanding → spec, or the user asks about procedure. Do **not** re-read the full Workflow every turn.

**Shared foundation (critical):**
- **Do not invent `_shared/` docs.** Only add §3.1 / `_shared/` when a **project-owned** piece is (or will be) used by **two or more features**, or the user named it as shared. Empty `_shared/` / empty §3.1 is fine. Never park engine/framework primers (e.g. generic Unreal notes) in `_shared/` because nothing else fit — use `features/` or `docs/reference/` (Workflow §1).
- When a real shared component exists: it gets **Understanding by default** (Workflow §1, §4). §3.0 exceptions are **user-requested only** — never invent them because files are missing or to “leave for later.”
- **File layout:** create only paths from Workflow **§0** / Document Map — flat files in `features/` and `_shared/`.
- **Document Map = files on disk.** Adding a §3.1/§3.2 row requires creating Understanding (`draft` OK) + spec stub + core TODO in the same turn. Never leave map-only “planned” rows. Bootstrap Step 3d. **Do not add filler §3.1 rows.**
- Real shared components get the **same note types as features** unless the user explicitly excepted specific files — record those in Master Index **§3.0** (Workflow §1). If Understanding or core TODO is missing for a mapped row and there is no user exception, **create them**.
- Tasks that **build or refactor** a shared component go in `_shared/ComponentName-TODO.md` (and related shared TODOs) — **not** in a consumer feature's TODO.
- Feature TODOs only **link** to shared TODOs when blocked or integrating (dependency note), they do not duplicate foundation tasks.

**Before implementation:**
- **Draft `-Understanding.md` first** when scoping new work — show the user how you interpreted their request; do not expect them to write it. Creating draft Understanding files is required; the `draft` status only blocks **coding**, not writing those files.
- Do not treat a feature as greenfield if Understanding says it extends or reuses existing work.
- Do not start coding while Understanding status is `draft` unless the user explicitly waives review.
- **When Understanding status is `confirmed`**, treat scope as approved — continue from TODO/spec without re-surfacing the Understanding for review.
- When producing a plan, include the Understanding file path so the user can correct scope and UI intent first — **unless** status is already `confirmed` and scope is unchanged.
- If the user's idea is vague, ask brief questions from `docs/templates/help/IDEA_CAPTURE_TIPS.md` (or project copy), then **draft** `-Understanding.md` for their review.
- When the user confirms Understanding, **graduate** durable content to the spec (`Feature_Spec_Template.md`) — Decisions, architecture, shared **Maturity** (Workflow §2).
- Record lasting tradeoffs in the spec **Decisions** table or `docs/decisions/` (Workflow §10).
- When the user provides UI reference screenshots, persist to `docs/features/assets/` or `docs/_shared/assets/` (copy from path when available; if paste-only chat image, ask user to save file or document from vision). Link from `-Understanding.md` **Visual references** with similar vs different.

**While working:**
- **Session start:** Read the active TODO's **Current focus** block first.
- Treat the active TODO as the living task list.
- Add new items as you discover them (new steps, clarifications, cross-feature dependencies, edge cases, refactoring needs).
- Use the "Cross-Feature Dependencies & Integration Notes" section when features interact.

**After changes (mandatory):**
- Update **Current focus** and the relevant `-TODO.md` — mark completed items with `[x]` + date.
- Update `-Understanding.md` / spec **only if this session** changed scope, UI intent, contract, or the user corrected assumptions — especially **What this is NOT** (finished-feature identity, not deferred work).
- Reconcile Understanding vs code **only when** the user reports a mismatch, implementation clearly contradicts Understanding, or this session changes that feature’s behavior — not as a session-start audit (Workflow §4).
- Move finished items to Completed when the list gets long.
- Only read other files when they are explicitly linked from Master_Index or the current TODO/spec.

**Clarification Protocol:**
If the user says "review spec", "check for gaps", "ask questions", or "confidence check" for a **named** feature or Document Map row:
- Re-read **that** feature’s (or shared component’s) spec, Understanding, and TODO only
- Identify the top gaps (cap clarifying questions at **5**)
- Ask targeted clarifying questions instead of assuming
- Only proceed after user confirmation
- Do not re-read unrelated features

**Philosophy:** Keep documentation small and accurate. Prefer short user asks — route to the one matching playbook above. **Tight scope:** do the paved path for the current ask; do not pre-audit alternate interpretations, unrelated files, or “just in case” repo scans before acting. Use Mermaid only when a small diagram beats prose (Workflow §12). TODO **Current focus** + checklists are your primary memory across sessions.
