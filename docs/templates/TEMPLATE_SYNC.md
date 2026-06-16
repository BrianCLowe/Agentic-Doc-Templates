# Template Sync — Agent Instructions

> Use when the user asks to sync, migrate, or update project documentation to match an improved template. Never edit template files unless the user explicitly requests it.

## Files involved

| File | Role |
|------|------|
| `docs/templates/Master_Index_Template.md` | Canonical structure (schema) |
| `docs/Master_Index.md` | Live project index (instance) |
| `docs/templates/Feature_Spec_Template.md` | Durable spec / contract after Understanding is confirmed |
| `docs/templates/TODO_Template.md` | Canonical TODO format (+ Current focus handoff) |
| `docs/templates/Decision_Template.md` | Optional cross-cutting decisions in `docs/decisions/` |
| Feature `*-Understanding.md` files | Agent-drafted intent — agent writes first; user reviews |
| Feature `*.md` specs | Graduate from Understanding; add Decisions + Maturity (shared) |
| Feature `*-TODO.md` files | Live task lists — update only if template format changed |

Check `<!-- template-version: X.Y -->` at the top of `Master_Index_Template.md` and the **Template version** line in live `Master_Index.md` to see if the project is behind.

## Sync workflow

1. Read `docs/templates/Master_Index_Template.md` and `docs/Master_Index.md`.
2. Compare structure: section headings, new/removed sections, workflow rules, naming conventions.
3. **Preserve** all project-specific content:
   - Section 1 overview text
   - Document Map rows and links (Sections 3.0–3.4)
   - Custom sections the project added
   - Any project-specific paths or conventions documented in the live file
4. **Adopt** from the template:
   - New or revised sections
   - Updated modular rules and quick-start order
   - Improved agent workflow instructions
   - Renumbered sections (update internal references)
5. Update the **Template version** line in `docs/Master_Index.md` to match the template.
6. If `Feature_Understanding_Template.md` is new or changed, merge new sections into active `-Understanding.md` files (features and shared) — do not overwrite. Add **Done when** and reconciliation fields if missing.
7. If `Feature_Spec_Template.md` is new or changed, merge **Decisions**, **Maturity**, and **Last reconciled** sections into live specs where placeholders exist.
8. If `TODO_Template.md` changed, add **Current focus** blocks to active TODOs if missing — do not rewrite task content.
9. If Section 3.0 (exceptions registry) is new, migrate any scattered "user excepted" notes into the registry.
10. Summarize what changed and ask the user to confirm before large structural edits.

## Do not

- Blindly replace `Master_Index.md` with the template (you will lose the Document Map and overview).
- Edit `docs/templates/*` with project-specific content.
- Remove project-only Document Map entries or custom sections unless the user asks.

## Example user prompts

- "Sync our Master_Index to the latest template."
- "Compare `Master_Index.md` to `Master_Index_Template.md` and apply structural improvements."
- "We updated the templates from Agentic Doc Templates — migrate our docs."
