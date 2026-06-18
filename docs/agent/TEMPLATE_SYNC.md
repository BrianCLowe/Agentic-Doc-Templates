# Template Sync — Agent Instructions

> Use when the user asks to sync, migrate, or update project documentation to match an improved template. Never edit template files unless the user explicitly requests it.

## Files involved

| File | Role |
|------|------|
| `docs/templates/Master_Index_Template.md` | Lean index schema (overview + map — **not** full workflow) |
| `docs/templates/Modular_Docs_Workflow.md` | Canonical agent procedure — replace from template when workflow version bumps |
| `docs/templates/chat-ui/AGENT.md` | Chat-only instructions (Grok.com, etc.) — replace when chat pack version bumps |
| `docs/Master_Index.md` | Live project index (instance) |
| `docs/templates/Feature_Spec_Template.md` | Durable spec / contract after Understanding is confirmed |
| `docs/templates/TODO_Template.md` | Canonical TODO format (+ Current focus handoff) |
| `docs/templates/Decision_Template.md` | Optional cross-cutting decisions in `docs/decisions/` |
| `docs/help/`, `docs/agent/` | Human guides and agent setup docs — refresh from upstream when those folders change |
| Feature `*-Understanding.md` files | Agent-drafted intent — agent writes first; user reviews |
| Feature `*.md` specs | Graduate from Understanding; add Decisions + Maturity (shared) |
| Feature `*-TODO.md` files | Live task lists — update only if template format changed |

Check versions:

- `<!-- template-version: X.Y -->` in `Master_Index_Template.md` → **Template version** in live `Master_Index.md`
- `<!-- workflow-version: X.Y -->` in `Modular_Docs_Workflow.md` → **Workflow version** in live `Master_Index.md`

## Sync workflow

1. Read `docs/templates/Master_Index_Template.md`, `docs/templates/Modular_Docs_Workflow.md`, and `docs/Master_Index.md`.
2. Compare structure: section headings, Document Map layout, workflow version, naming conventions.
3. **Preserve** all project-specific content in `Master_Index.md`:
   - Section 1 overview text and Project Profile
   - Document Map rows and links (Sections 3.0–3.4)
   - Section 3.0 exception registry rows
   - Custom sections the project added
4. **Adopt** from `Master_Index_Template.md`:
   - New or revised index sections (Key Locations, At a Glance, Quick Start pointer)
   - Renumbered sections (update internal references)
   - **Do not** merge old workflow sections (4–10) from legacy Master_Index — they now live in `Modular_Docs_Workflow.md`
5. **Adopt** from `Modular_Docs_Workflow.md`:
   - Replace `docs/templates/Modular_Docs_Workflow.md` in the project when workflow version is behind (whole file from upstream template)
   - Replace `docs/templates/chat-ui/AGENT.md` when the chat pack version is behind (whole file from upstream)
   - Update agent rule copies if workflow changed materially (especially **§0 Naming** — see [`RULE_INSTALL.md`](RULE_INSTALL.md))
6. Update **Template version** and **Workflow version** lines in `docs/Master_Index.md`.
7. If migrating from pre-1.7 Master_Index: **remove** duplicated workflow sections (old §4 Quick Start through §10 Decisions) from live `Master_Index.md` after confirming content exists in `Modular_Docs_Workflow.md`; replace with lean §4 Quick Start from template.
8. If migrating from pre-1.8 flat `docs/templates/` pack: run layout migration per [`BOOTSTRAP.md`](BOOTSTRAP.md) Step 0b (`help/`, `agent/`, lean `templates/`); refresh `docs/help/` and `docs/agent/` from upstream.
9. If `Feature_Understanding_Template.md` is new or changed, merge new sections into active `-Understanding.md` files — do not overwrite.
10. If `Feature_Spec_Template.md` is new or changed, merge **Decisions**, **Maturity**, and **Last reconciled** into live specs where placeholders exist.
11. If `TODO_Template.md` changed, add **Current focus** blocks to active TODOs if missing.
12. If Section 3.0 is new, migrate scattered "user excepted" notes into the registry.
13. Summarize what changed and ask the user to confirm before large structural edits.

## Do not

- Blindly replace `Master_Index.md` with the template (you will lose the Document Map and overview).
- Copy workflow prose into live `Master_Index.md` (keep it in `Modular_Docs_Workflow.md` only).
- Edit `docs/templates/*` with project-specific content.
- Remove project-only Document Map entries unless the user asks.

## Example user prompts

- "Sync our Master_Index to the latest template."
- "Compare `Master_Index.md` to `Master_Index_Template.md` and apply structural improvements."
- "We updated the templates from Agentic Doc Templates — migrate our docs."
- "Sync workflow to latest Modular_Docs_Workflow.md."
