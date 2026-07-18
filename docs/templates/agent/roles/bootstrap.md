# Role — Bootstrap *(optional)*

> **Opt-in.** Use only when the user asks for this role or names this file. Not always-on.

**Job:** First-time modular docs layout for a project. Thin wrapper — do not invent a second bootstrap procedure.

**Canonical procedure:** [`../BOOTSTRAP.md`](../BOOTSTRAP.md) only.

## When to invoke

- User asks to bootstrap / init modular docs
- User says: *Bootstrap role*, *follow roles/bootstrap.md*

## Inputs *(open only these)*

1. [`../BOOTSTRAP.md`](../BOOTSTRAP.md) — follow it end-to-end
2. Files that playbook names (Master Index template, scaffolds, conversation / reference sources it tells you to use)

**Do not** open TEMPLATE_SYNC, the roles catalog beyond this file, or unrelated features.

## Steps

1. Open `docs/templates/agent/BOOTSTRAP.md`.
2. Execute its steps in order, including Step 4b (weekly update checks ask) when you reach it.
3. If the user also wants optional doc roles installed for Cursor, that is **Step 4c** in BOOTSTRAP (or a later RULE_INSTALL ask) — do not enable silently.
4. Stop when BOOTSTRAP’s “Tell the user what's next” is done.

## Stop when

- Live `docs/Master_Index.md` and the layout BOOTSTRAP requires exist, and
- You have reported next steps to the user

## Do not

- Implement application features during bootstrap
- Fill §3.1 `_shared/` with filler rows
- Overwrite a real project README that is not the upstream template readme
- Install always-on competing skill packs
- Run template sync unless the user asked for sync instead of bootstrap
