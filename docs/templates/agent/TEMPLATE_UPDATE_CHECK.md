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
| **`always`** *(default / recommended)* | No check interval. Fetch upstream `VERSION` when the rule runs (typically once per session start, or when the user asks). Report if newer. **Do not write settings.** |
| **`interval`** | Fetch only when `last_checked` is older than `check_interval_days` (default **7** if unset under interval mode), or when the user asks. **Write `last_checked` after a fetch** so the next session can skip. Do **not** open a pull request for that write. |
| **missing / unset** | No interval yet. Treat as **`always`** for the fetch this session (**do not write settings**). Sync/bootstrap still runs the cadence ask ([`TEMPLATE_SYNC_B.md`](TEMPLATE_SYNC_B.md) B0.4) until `check_mode_recorded` is set. |

Do **not** invent `check_mode` from legacy `check_interval_days` without asking — leave cadence to B0.4 / bootstrap Step 3p.

## When to run

| Trigger | Action |
|---------|--------|
| User asks to check / sync templates | Run the check now (ignore interval) |
| Rule on + `check_mode: always` | Fetch once this session (or when user asks). Do **not** write settings. Then continue normal work |
| Rule on + `check_mode: interval` + `last_checked` older than `check_interval_days` | Fetch once. Write `last_checked`. Do **not** open a pull request. If the user does not opt to update, include that write in the same commit as this session's other changes |
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

4. Compare upstream pack version to `upstream.local_pack_version` when that key is set (or legacy `local_template_version` if not yet migrated). If it is missing, compare to local `docs/templates/VERSION` (`pack-version`). Do **not** write `local_pack_version` during this check.
5. **Save the result only when there is a check interval.**
   - **No interval** — `check_mode: always`, or `check_mode` missing/unset: do **not** edit `docs/ADT-settings.yaml`. Do **not** set or update `last_checked`, `update_available`, or `upstream_pack_version`. Do **not** commit. Do **not** open a pull request. Report in chat only. The rule runs again next session, so there is nothing to remember on disk.
   - **Interval** — `check_mode: interval`: set `upstream.last_checked` to today (YYYY-MM-DD), clear or set `update_available` / `upstream_pack_version` as appropriate, and write `ADT-settings.yaml` back. That stamp is how the next session knows whether `check_interval_days` has elapsed. Do **not** commit it yet. Do **not** open a pull request for the interval stamp.
6. Tell the user the result briefly:
   - **Newer upstream** → offer [`TEMPLATE_SYNC.md`](TEMPLATE_SYNC.md) (*Update the doc templates from Agentic Doc Templates and sync our live docs.*). Do **not** ZIP-download until they agree (unless they already asked to sync).
   - **Same or older** → say templates look current; do not run TEMPLATE_SYNC.
7. On failed fetch (offline, 404, etc.) → say so once. Under **interval**, still update `last_checked` so you do not thrash every turn. Under **no interval**, do **not** write `last_checked` — once per session already stops a retry every turn; the next session tries again.
8. **Where an interval stamp lands** (skip when nothing was written):
   - User **opts to update** → run TEMPLATE_SYNC. That sync commit carries settings. Do **not** commit the check stamp by itself. Do **not** open a pull request for it.
   - User **does not opt to update** (declines, says later, or upstream is not newer) → do **not** open a pull request. Include the settings edit in the **same commit** as this session's other changes.
   - This session has no other changes → leave the stamp uncommitted. Do **not** open a pull request.

## Do not

- Download the full pack ZIP just to read the version.
- Read the whole `docs/templates/` tree for a version check.
- Under `interval`: re-fetch upstream on every message when `last_checked` is still fresh.
- Under `always`: fetch more than once per session unless the user asks again.
- Under no interval (`always` or unset `check_mode`): edit `docs/ADT-settings.yaml`, set `last_checked` / `update_available` / `upstream_pack_version` / `local_pack_version`, or open a commit or PR to record the check.
- Under `interval`: open a pull request for the check stamp, or commit that stamp by itself. If the user does not opt to update, include it in the same commit as this session's other changes.
- Use git remotes / submodules for this check.
- Overwrite live docs during a check — sync is a separate, user-confirmed step.
- Auto-sync because a newer version exists — only report + offer.

## After a successful TEMPLATE_SYNC

Update `docs/ADT-settings.yaml` → `upstream:`:

- `local_pack_version` from local `docs/templates/VERSION` (installed pack — not a session check log)
- Preserve `check_mode` and `check_interval_days`
- **Interval:** `last_checked` today; `update_available: false` (or remove); remove stale `upstream_pack_version` if present
- **No interval** (`always` or unset): do **not** set `last_checked`, `update_available`, or `upstream_pack_version`. If those keys are already present, **remove** them in this sync stamp (they are check logs; always mode does not use them). That removal rides in the pack/stamp commit — not its own pull request.

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
