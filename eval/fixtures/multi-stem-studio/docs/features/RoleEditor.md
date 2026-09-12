# RoleEditor

**Related Understanding**: [RoleEditor-Understanding.md](RoleEditor-Understanding.md)
**Related TODO**: [RoleEditor-TODO.md](RoleEditor-TODO.md)

## Overview

Role-specific chrome on the shared BlockEditor engine. Same document, different toolbar / panels.

## Architecture / Contract

- **Owns**: role chrome, focus layout
- **Does not own**: document model, persist pipeline (BlockEditor)

## Behavior

- Opens a manuscript through BlockEditor.
- Chrome differs; the canvas is the shared engine.

## Acceptance

- [ ] User can edit a manuscript in RoleEditor using BlockEditor
- [ ] Save goes through BlockEditor persist hooks

## Decisions

| Date | Decision | Rationale |
|------|----------|-----------|
| 2026-08-01 | Same editing core, not a second engine | Confirmed shape |
