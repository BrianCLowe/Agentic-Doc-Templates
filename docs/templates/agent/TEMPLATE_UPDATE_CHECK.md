# Template Update Check — Agent Instructions

> Use when the optional Template Update Check rule is installed, or when the user asks to check for template updates. Typical ask: *"Check for Agentic Doc Templates updates."*

## Goal

See whether [Agentic Doc Templates](https://github.com/BrianCLowe/Agentic-Doc-Templates) has a newer pack than this project — **without** downloading the ZIP unless the user wants to sync.

## Status file

**Live:** `docs/upstream-status.yaml`  
**Example:** [`upstream-status.example.yaml`](upstream-status.example.yaml)

If the live file is missing, this check is not enabled — tell the user and offer to create it (bootstrap / re-enable). Do not invent checks against a missing file every turn.

## When to run

| Trigger | Action |
|---------|--------|
| User asks to check / sync templates | Run the check now (ignore interval) |
| Optional rule + `last_checked` older than `check_interval_days` (default 7) | Run once this session, then continue normal work |
| Optional rule + still within interval | **Stop after reading the status file** — do not fetch upstream |

“Weekly” means **next session after the interval**, not a background cron.

## Cheap check procedure

1. Read **only** `docs/upstream-status.yaml`.
2. If not due and user did not ask → stop.
3. If due or requested → fetch **only** the upstream VERSION file (one small request):

   `https://raw.githubusercontent.com/BrianCLowe/Agentic-Doc-Templates/main/docs/templates/VERSION`

   Expected shape:

   ```text
   template-version: X.Y
   workflow-version: X.Y
   ```

4. Compare upstream `template-version` to `local_template_version` in the status file.
5. **Always** set `last_checked` to today (YYYY-MM-DD), clear or set `update_available` / `upstream_template_version` as appropriate, and write the status file back.
6. Tell the user the result briefly:
   - **Newer upstream** → offer [`TEMPLATE_SYNC.md`](TEMPLATE_SYNC.md) (*Update the doc templates from Agentic Doc Templates and sync our live docs.*). Do **not** ZIP-download until they agree (unless they already asked to sync).
   - **Same or older** → say templates look current; do not run TEMPLATE_SYNC.
7. On failed fetch (offline, 404, etc.) → say so once; still update `last_checked` so you do not retry every turn; user can ask again later.

## Do not

- Download the full pack ZIP just to read the version.
- Read the whole `docs/templates/` tree for a version check.
- Re-fetch upstream on every message when `last_checked` is still fresh.
- Use git remotes / submodules for this check.
- Overwrite live docs during a check — sync is a separate, user-confirmed step.

## After a successful TEMPLATE_SYNC

Update `docs/upstream-status.yaml`:

- `local_template_version` / `local_workflow_version` from local `docs/templates/VERSION`
- `last_checked` today
- `update_available: false` (or remove)
- Remove stale `upstream_template_version` if present

Preserve `check_interval_days` and the file itself across pack overwrites (`docs/upstream-status.yaml` is **not** under `docs/templates/`).

## Example user prompts

- "Check for template updates."
- "Is there a newer Agentic Doc Templates pack?"
- "Check for template updates every week." *(enable / re-install optional rule — see [`BOOTSTRAP.md`](BOOTSTRAP.md) / [`RULE_INSTALL.md`](RULE_INSTALL.md))*

## Related

- Full pack refresh: [`TEMPLATE_SYNC.md`](TEMPLATE_SYNC.md)
- Optional rule templates: `Template_Update_Check_Rule.mdc`, `Template_Update_Check_Rule.instructions.md`
