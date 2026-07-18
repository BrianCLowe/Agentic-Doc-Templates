# Tool install playbooks

> **Machine-oriented.** Bootstrap / [`../RULE_INSTALL.md`](../RULE_INSTALL.md) / template sync open **only** the tool files for tools in `docs/rule-install-status.yaml` (or the one tool the user just named). Do not open every file here.

Each file is an **install/sync adapter**: where the modular rule goes, optional update-check path, optional doc-roles format, conflicts, verify. It does **not** restate Understanding / TODO / Workflow procedure.

## Index *(status key → file)*

| Status key | File | Ships |
|------------|------|-------|
| `cursor` | [`cursor.md`](cursor.md) | yes |
| `grok-build` | [`grok-build.md`](grok-build.md) | yes |
| `claude-code` | [`claude-code.md`](claude-code.md) | yes |
| `github-copilot` | [`github-copilot.md`](github-copilot.md) | yes |
| `agents-md` | [`agents-md.md`](agents-md.md) | yes |
| `continue` | [`continue.md`](continue.md) | thin |
| `cline` | [`cline.md`](cline.md) | thin |

Human overview (TOC): [`../../help/USING_WITH_AGENTS.md`](../../help/USING_WITH_AGENTS.md).

Shared sources (do not duplicate into tool files):

- Modular rule bodies: [`../Modular_Documentation_Rule.mdc`](../Modular_Documentation_Rule.mdc), [`../Modular_Documentation_Rule.instructions.md`](../Modular_Documentation_Rule.instructions.md)
- Role playbooks: [`../roles/`](../roles/README.md)
- Role adapters: [`../roles/cursor/`](../roles/cursor/), [`../roles/grok/`](../roles/grok/)

## Dispatcher rules

1. Read `docs/rule-install-status.yaml`.
2. For each tool to install or refresh → open **`tools/<key>.md` only** → execute that file → stop.
3. Never scan the pack catalog for “other tools that might help.”
