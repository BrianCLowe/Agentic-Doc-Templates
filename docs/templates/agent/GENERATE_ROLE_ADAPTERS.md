<!-- pack-version: 2.7.17 -->

# Generate role adapters — Agent Instructions

> **Maintainers / pack editors.** Use when editing [`roles/adapter-src/`](roles/adapter-src/README.md) or when cursor/grok adapters drift. **No Python required** — write the markdown files directly. Do not invent a local script.

## Goal

Regenerate every harness adapter under `roles/cursor/` and `roles/grok/` from the single source in `roles/adapter-src/`, then stop.

## Inputs *(open only these)*

1. [`roles/adapter-src/manifest.json`](roles/adapter-src/manifest.json) — role list, descriptions, per-harness frontmatter, optional `grok_extra_hard_rules`
2. [`roles/adapter-src/bodies/<role>.md`](roles/adapter-src/bodies/) — shared body (intro + Hard rules) for each role in the manifest
3. Existing `roles/cursor/*.md` and `roles/grok/*.md` only to overwrite

**Do not** open unrelated playbooks or scan the pack catalog.

## Steps

For **each** role name in `manifest.json` → `roles`:

### 1. Cursor adapter → `roles/cursor/<role>.md`

Write the file as:

```markdown
---
name: <role>
description: >-
  <manifest description, soft-wrapped ~72 cols under description: >->
<cursor frontmatter keys from manifest, one per line, e.g. model: inherit>
---

<body file contents verbatim, including trailing newline>
```

Rules:

- `name` is the role key (e.g. `feature-implementer`).
- `description: >-` then indented continuation lines (same style as existing adapters).
- Emit every key in `roles.<role>.cursor` after the description (typical: `model: inherit`). Booleans as `true` / `false`.
- Body = full text of `adapter-src/bodies/<body>` from the manifest `body` field — **no edits**.

### 2. Grok adapter → `roles/grok/<role>.md`

Same as Cursor, but:

- Use `roles.<role>.grok` for frontmatter keys (typical: `prompt_mode`, `model`, `permission_mode`, `agents_md`).
- After the shared body, if `grok_extra_hard_rules` is a non-empty array, append each item as an extra Hard-rules bullet:

```markdown
- <extra rule text>
```

Append them at the end of the existing `Hard rules:` list (do not create a second Hard rules section).

### 3. Coverage

- Write **both** harnesses for every role in the manifest.
- Delete `roles/cursor/<name>.md` or `roles/grok/<name>.md` only if that role was **removed** from the manifest (ask before deleting if unsure).
- **Never** create an `orchestrator` adapter.

## Stop when

- Every manifest role has matching `cursor/` and `grok/` files, and
- Bodies match `adapter-src/bodies/` (plus grok extras when listed), and
- You report which roles were rewritten

## Do not

- Require or invent Python / shell generators for this pack — this playbook **is** the generator
- Hand-edit `cursor/` or `grok/` as the source of truth — edit `adapter-src/` then re-run this playbook
- Restate full Workflow gates in adapter bodies (pointers only)
- Install adapters into `.cursor/agents/` / `.grok/agents/` here — that is [`RULE_INSTALL.md`](RULE_INSTALL.md) / `tools/<key>.md`

## Related

- Source layout: [`roles/adapter-src/README.md`](roles/adapter-src/README.md)
- Optional roles overview: [`roles/README.md`](roles/README.md)
