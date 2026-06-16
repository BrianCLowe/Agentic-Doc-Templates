# Template Sync — Agent Instructions

> Use when the user asks to sync, migrate, or update project documentation to match an improved template. Never edit template files unless the user explicitly requests it.

## Files involved

| File | Role |
|------|------|
| `docs/templates/Master_Index_Template.md` | Canonical structure (schema) |
| `docs/Master_Index.md` | Live project index (instance) |
| `docs/templates/TODO_Template.md` | Canonical TODO format |
| Feature `*-Understanding.md` files | Agent-drafted intent docs — agent writes first when scoping; user reviews and corrects |
| Feature `*-TODO.md` files | Live task lists — update only if template format changed |

Check `<!-- template-version: X.Y -->` at the top of `Master_Index_Template.md` and the **Template version** line in live `Master_Index.md` to see if the project is behind.

## Sync workflow

1. Read `docs/templates/Master_Index_Template.md` and `docs/Master_Index.md`.
2. Compare structure: section headings, new/removed sections, workflow rules, naming conventions.
3. **Preserve** all project-specific content:
   - Section 1 overview text
   - Document Map rows and links (Sections 3.1–3.4)
   - Custom sections the project added
   - Any project-specific paths or conventions documented in the live file
4. **Adopt** from the template:
   - New or revised sections
   - Updated modular rules and quick-start order
   - Improved agent workflow instructions
   - Renumbered sections (update internal references)
5. Update the **Template version** line in `docs/Master_Index.md` to match the template.
6. If `Feature_Understanding_Template.md` is new or changed, ensure active features **and shared components** have agent-drafted `-Understanding.md` files — do not overwrite existing content; merge new sections only. Skip only where the user previously excepted Understanding for a specific shared component.
7. If `TODO_Template.md` changed, update existing feature TODO files only where format differs — do not rewrite task content.
8. Summarize what changed and ask the user to confirm before large structural edits.

## Do not

- Blindly replace `Master_Index.md` with the template (you will lose the Document Map and overview).
- Edit `docs/templates/*` with project-specific content.
- Remove project-only Document Map entries or custom sections unless the user asks.

## Example user prompts

- "Sync our Master_Index to the latest template."
- "Compare `Master_Index.md` to `Master_Index_Template.md` and apply structural improvements."
- "We updated the templates from Agentic Doc Templates — migrate our docs."
