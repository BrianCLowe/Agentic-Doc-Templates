# BlockEditor

**Maturity**: usable
**Related Understanding**: [BlockEditor-Understanding.md](BlockEditor-Understanding.md)
**Related TODO**: [BlockEditor-TODO.md](BlockEditor-TODO.md)

## Overview

Shared block-based editing core — document model, caret, save hooks. Role UIs wrap this.

## Architecture / Contract

- **Owns**: document model, persist hooks, editing commands
- **Does not own**: role chrome, video export, publish HTTP

## Behavior

- Consumers call `openDocument` / `saveDocument`.
- One document model for the studio.

## Acceptance

- [x] RoleEditor can open a document through this API
- [ ] DiffWorkflow can read the same document model

## Decisions

| Date | Decision | Rationale |
|------|----------|-----------|
| 2026-08-01 | One engine | Avoid a second document model |
