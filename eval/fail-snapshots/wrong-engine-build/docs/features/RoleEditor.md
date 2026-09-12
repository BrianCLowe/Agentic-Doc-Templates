# RoleEditor

**Related Understanding**: [RoleEditor-Understanding.md](RoleEditor-Understanding.md)
**Related TODO**: [RoleEditor-TODO.md](RoleEditor-TODO.md)

## Overview

Standalone editor with its own document model and save pipeline so we aren't blocked on BlockEditor.

## Architecture / Contract

- **Owns**: second editor engine, own document model, persist pipeline
- **Does not own**: BlockEditor (we forked away)

## Behavior

- Independent document format.
- Own save pipeline.

## Decisions

| Date | Decision | Rationale |
|------|----------|-----------|
| 2026-09-12 | New standalone editor core | User asked to not be blocked |
