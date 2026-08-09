# Template Update Check — Agent Instructions

> Use when the optional Template Update Check rule is installed, or when the user asks to check for template updates. Typical ask: *"Check for Agentic Doc Templates updates."*

## Goal

See whether [Agentic Doc Templates](https://github.com/BrianCLowe/Agentic-Doc-Templates) has a newer pack than this project — **without** downloading the ZIP unless the user wants to sync.

## Settings

**Live:** `docs/ADT-settings.yaml`  
**Example:** [`ADT-settings.example.yaml`](ADT-settings.example.yaml)

This check is enabled only when `optional_rules.template-update-check.status` is `enabled` and an `upstream:` block is present (or can be created on enable).

**Legacy:** If `docs/ADT-settings.yaml` is missing but `docs/upstream-status.yaml` exists → migrate into `ADT-settings.yaml` first ([`TEMPLATE_SYNC_B.md`](TEMPLATE_SYNC_B.md) B0.1), then continue. Do not invent checks against a missing settings file every turn.

### Check mode (`upstream.check_mode`)

| Mode | Behavior |
|------|----------|
| **`always`** *(default / recommended)* | Fetch upstream `VERSION` when the rule runs (typically once per session start, or when the user asks). Report if newer. |
| **`interval`** | Fetch only when `last_checked` is older than `check_interval_days` (default **7** if unset under interval mode), or when the user asks. |
| **missing / unset** | Treat as **`always`** for the fetch this session, but sync/bootstrap should still run the cadence ask ([`TEMPLATE_SYNC_B.md`](TEMPLATE_SYNC_B.md) B0.4) until `check_mode_recorded` is set. |

Do **not** invent `check_mode` from legacy `check_interval_days` without asking — leave cadence to B0.4 / bootstrap Step 3p.

## When to run

| Trigger | Action |
|---------|--------|
| User asks to check / sync templates | Run the check now (ignore interval) |
| Rule on + `check_mode: always` | Fetch once this session (or when user asks), then continue normal work |
| Rule on + `check_mode: interval` + `last_checked` older than `check_interval_days` | Fetch once this session, then continue normal work |
| Rule on + `check_mode: interval` + still within interval | **Stop after reading settings** — do not fetch upstream |

## Cheap check procedure

1. Read **only** `docs/ADT-settings.yaml` (confirm update-check enabled + read `upstream:`).
2. Resolve `check_mode` (default **always** if unset). If `interval` and not due and user did not ask → stop.
3. If due or `always` or requested → fetch **only** the upstream VERSION file (one small request):

   `https://raw.githubusercontent.com/BrianCLowe/Agentic-Doc-Templates/main/docs/templates/VERSION`

   Expected shape:

   ```text
   pack-version: X.Y.Z
   ```

   Legacy dual lines (`template-version` / `workflow-version`) → use `template-version` (or either) as `pack-version`.

4. Compare upstream pack version to `upstream.local_pack_version` (or legacy `local_template_version` if not yet migrated).
5. **Always** set `upstream.last_checked` to today (YYYY-MM-DD), clear or set `update_available` / `upstream_pack_version` as appropriate, and write `ADT-settings.yaml` back.
6. Tell the user the result briefly:
   - **Newer upstream** → offer [`TEMPLATE_SYNC.md`](TEMPLATE_SYNC.md) (*Update the doc templates from Agentic Doc Templates and sync our live docs.*). Do **not** ZIP-download until they agree (unless they already asked to sync).
   - **Same or older** → say templates look current; do not run TEMPLATE_SYNC.
7. On failed fetch (offline, 404, etc.) → say so once; still update `last_checked` so you do not retry every turn under `always` (or thrash under interval); user can ask again later.

## Do not

- Download the full pack ZIP just to read the version.
- Read the whole `docs/templates/` tree for a version check.
- Under `interval`: re-fetch upstream on every message when `last_checked` is still fresh.
- Under `always`: fetch more than once per session unless the user asks again.
- Use git remotes / submodules for this check.
- Overwrite live docs during a check — sync is a separate, user-confirmed step.
- Auto-sync because a newer version exists — only report + offer.

## After a successful TEMPLATE_SYNC

Update `docs/ADT-settings.yaml` → `upstream:`:

- `local_pack_version` from local `docs/templates/VERSION`
- `last_checked` today
- `update_available: false` (or remove)
- Remove stale `upstream_pack_version` if present
- Preserve `check_mode` and `check_interval_days`

Preserve the settings file itself across pack overwrites (`docs/ADT-settings.yaml` is **not** under `docs/templates/`).

## Example user prompts

- "Check for template updates."
- "Is there a newer Agentic Doc Templates pack?"
- "Enable template update checks." *(bootstrap / re-enable — default `check_mode: always`)*
- "Only check for template updates every week." → `check_mode: interval`, `check_interval_days: 7`
- "Check for template updates every session." → `check_mode: always`

## Related

- Full pack refresh: [`TEMPLATE_SYNC.md`](TEMPLATE_SYNC.md)
- Optional rule templates: `Template_Update_Check_Rule.mdc`, `Template_Update_Check_Rule.instructions.md`
