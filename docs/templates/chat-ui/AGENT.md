# Chat UI — Create modular documentation

> **For agents without repo write access.** Produce markdown files the user can save into their project. Do not invent folder layouts — use **exact paths** below.

## Your job

1. Turn the conversation into modular docs under `docs/`.
2. **Draft `-Understanding.md` first** (status `draft`) — show the user how you interpreted them; they review before specs/TODOs are final.
3. Output **one file per message block** with the full path as a heading so the user can save or download each file.

## Output format *(required)*

Use this pattern for every file:

```markdown
---
**Save as:** `docs/features/MainWorkspace-Understanding.md`
---

# Main Workspace — Understanding

(file content)
```

Separate files with `---` between blocks. Never bury multiple files in one blob without paths.

## Folder layout

```
docs/
├── Master_Index.md
├── _shared/
│   └── ComponentName.md          (+ Understanding, TODO — same folder)
├── features/
│   └── FeatureName.md            (+ Understanding, TODO — same folder)
└── features/assets/              ← screenshots only (optional)
```

**Flat sibling files** in `docs/features/` and `docs/_shared/`. Same **name stem** for each set (e.g. `MainWorkspace` everywhere).

## Files to create per item

| Item | Create these paths |
|------|-------------------|
| **Each feature** | `docs/features/FeatureName.md` |
| | `docs/features/FeatureName-Understanding.md` *(draft first)* |
| | `docs/features/FeatureName-TODO.md` |
| **Each shared component** | `docs/_shared/ComponentName.md` |
| | `docs/_shared/ComponentName-Understanding.md` *(draft first)* |
| | `docs/_shared/ComponentName-TODO.md` |
| **Project entry** | `docs/Master_Index.md` *(overview + Document Map listing every path above)* |
| **Human inbox** *(procure / playtest / decide / waiting)* | `docs/Human-TODO.md` |

Optional later (not required in chat): `-InEditor-TODO.md`, `-Asset-TODO.md`, `docs/Tooling.md`, `docs/decisions/`. Skip unless the user asks or the conversation clearly needs them.

**Shared components** get the same three file types as features unless the user **says** to omit something — record omissions in Master_Index §3.0. Do not invent exceptions.

## Naming

- **FeatureName / ComponentName:** PascalCase or kebab-case — pick one and use it consistently (e.g. `MainWorkspace` or `main-workspace`).
- **Suffixes:** `-Understanding.md`, `-TODO.md` exactly (hyphen before suffix).
- **Spec file:** `docs/features/FeatureName.md` (same folder as Understanding and TODO).

## Master_Index.md *(minimum)*

Include:

1. **Project overview** (1–3 paragraphs from the conversation).
2. **Document Map** — tables linking every file you created:

**Features example:**

| Feature | Spec | Understanding | TODO |
|---------|------|---------------|------|
| Main Workspace | features/MainWorkspace.md | features/MainWorkspace-Understanding.md | features/MainWorkspace-TODO.md |

**Shared example:**

| Component | Spec | Understanding | TODO |
|-----------|------|---------------|------|
| Block Editor | _shared/BlockEditor.md | _shared/BlockEditor-Understanding.md | _shared/BlockEditor-TODO.md |

3. **Template version:** 2.6.3 · **Workflow version:** 2.6.3 *(for later sync with Agentic Doc Templates)*

Use this **minimum** by default. Open [`Master_Index_Template.md`](../Master_Index_Template.md) only if the user asked for the full index section layout.

## Understanding files *(you write first)*

Follow [`Feature_Understanding_Template.md`](../Feature_Understanding_Template.md) when attached. Always include:

- **What this is** / **What this is NOT** — identity of the **finished** feature; NOT is category boundaries, not “not implemented yet”
- **Relationship to existing work** (reuse vs greenfield)
- **Done when** — checkboxes so the user knows when the feature is complete
- **Assumptions** — unchecked until the user confirms

Set status `draft`. Do not treat the user as author — they **review and correct** your draft. After they approve, set **`confirmed`** — then later agents can continue without re-asking for review.

## Spec and TODO

- **Spec** (`FeatureName.md`): durable overview after Understanding is confirmed; can start as a short placeholder in chat sessions.
- **TODO**: initial High Priority items from the conversation; include **Current focus** block at top (one next task). Human-gated items (playtest, decide, procure, waiting) → dual-write owner TODO + `docs/Human-TODO.md` Open row.

## Rules

- Only document what was discussed — do not invent features.
- Reusable pieces used by **multiple** features → `_shared/` with full file set; feature-specific → `features/`. **Skip `_shared/` entirely** if nothing is truly shared — do not invent shared docs or dump engine/framework primers there (use `docs/reference/` if needed).
- When adding a row to Document Map, create all three paths for that row in the same response batch.

## After the user has a repo

They copy `docs/templates/` from [Agentic Doc Templates](https://github.com/BrianCLowe/Agentic-Doc-Templates) and use [`Modular_Docs_Workflow.md`](../agent/Modular_Docs_Workflow.md) + IDE agent rules for ongoing work.
