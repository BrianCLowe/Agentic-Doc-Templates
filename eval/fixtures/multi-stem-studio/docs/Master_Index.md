# Studio — Master Index

**Pack version**: eval

## 1. Project Overview

A manuscript studio: one shared editing engine, a role-specific surface, a diff workflow, video export, and a small publish API. Identity-risky product — docs profile is **prevent**.

## 3. Document Map

### 3.1 Shared / Core Components

| Component | Maturity | Spec | Understanding | TODO |
|-----------|----------|------|---------------|------|
| BlockEditor | usable | [_shared/BlockEditor.md](_shared/BlockEditor.md) | [_shared/BlockEditor-Understanding.md](_shared/BlockEditor-Understanding.md) | [_shared/BlockEditor-TODO.md](_shared/BlockEditor-TODO.md) |

### 3.2 Features

| Feature | Spec | Understanding | TODO |
|---------|------|---------------|------|
| RoleEditor | [RoleEditor.md](features/RoleEditor.md) | [RoleEditor-Understanding.md](features/RoleEditor-Understanding.md) | [RoleEditor-TODO.md](features/RoleEditor-TODO.md) |
| DiffWorkflow | [DiffWorkflow.md](features/DiffWorkflow.md) | [DiffWorkflow-Understanding.md](features/DiffWorkflow-Understanding.md) | [DiffWorkflow-TODO.md](features/DiffWorkflow-TODO.md) |
| VideoGeneration | [VideoGeneration.md](features/VideoGeneration.md) | [VideoGeneration-Understanding.md](features/VideoGeneration-Understanding.md) | [VideoGeneration-TODO.md](features/VideoGeneration-TODO.md) |
| PublishApi | [PublishApi.md](features/PublishApi.md) | [PublishApi-Understanding.md](features/PublishApi-Understanding.md) | [PublishApi-TODO.md](features/PublishApi-TODO.md) |

### 3.4 Decisions

| Document | Description |
|----------|-------------|
| [decisions/2026-08-01-one-editor-engine.md](decisions/2026-08-01-one-editor-engine.md) | One editing engine — RoleEditor is chrome on BlockEditor |
