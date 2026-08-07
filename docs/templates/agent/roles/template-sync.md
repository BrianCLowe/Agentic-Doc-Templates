# Role — Template sync *(optional)*

> **Opt-in.** Use only when the user asks for this role or names this file. Not always-on.

**Job:** Refresh `docs/templates/` from upstream and apply **changelog-scoped** live updates. Thin wrapper around the sync playbooks.

**Canonical procedure:** [`../TEMPLATE_SYNC.md`](../TEMPLATE_SYNC.md) → [`../TEMPLATE_SYNC_A.md`](../TEMPLATE_SYNC_A.md) → (after overwrite) [`../TEMPLATE_SYNC_B.md`](../TEMPLATE_SYNC_B.md) + top [`../../CHANGELOG.md`](../../CHANGELOG.md) entry. Settings: [`../ADT-settings.example.yaml`](../ADT-settings.example.yaml) → live `docs/ADT-settings.yaml`.

## When to invoke

- User asks to update / sync doc templates from Agentic Doc Templates
- User says: *Template sync role*, *follow roles/template-sync.md*

## Inputs *(open only these)*

1. [`../TEMPLATE_SYNC.md`](../TEMPLATE_SYNC.md) (entry) then **only** [`../TEMPLATE_SYNC_A.md`](../TEMPLATE_SYNC_A.md) — do **not** open B yet
2. After A finishes: **only** [`../TEMPLATE_SYNC_B.md`](../TEMPLATE_SYNC_B.md) from disk + **only the top** [`../../CHANGELOG.md`](../../CHANGELOG.md) entry
3. `docs/ADT-settings.yaml` (migrate legacy status files per B0.1 if needed)
4. Live files that Step B / Live impact tags name (usually `Master_Index.md`, versions — not every feature file)
5. On reshape / TODO ambition **execute**: only the Understanding/spec/TODO files for stems in scope

## Steps

1. Open entry [`TEMPLATE_SYNC.md`](../TEMPLATE_SYNC.md) → follow **A** only ([`TEMPLATE_SYNC_A.md`](../TEMPLATE_SYNC_A.md)). Do not read B “for context.”
2. When A’s handoff says so: open **local** [`TEMPLATE_SYNC_B.md`](../TEMPLATE_SYNC_B.md) from disk — discard any pre-overwrite sync procedure.
3. Run Step B from B + top changelog entry’s tags only (including B0 settings migrate + sync.mode).
4. **Rules** when tagged: refresh installed tools via each `tools/<key>.md` — **no ask** unless `customized: true`.
5. **Reshape / TODO ambition** when tagged: if `sync.mode: auto` → execute all Document Map stems; if `choose` → explain + ask once; if mode unset → B0.2 ask once then continue.
6. Summarize what changed (sync mode, what executed, settings migration).
7. Run B’s **Present unset options** for missing `optional_rules.*`.
8. **Stop.**

## Stop when

- Step A handoff completed and Step B for the top changelog entry is done,
- Tagged optional live passes were executed (`auto`) or presented (`choose`),
- Unset optionals were presented (or already `enabled` / `declined`), and
- You have not scanned live `features/` / `_shared/` unless `content-templates` or an executing reshape/ambition pass required it

## Do not

- Open `TEMPLATE_SYNC_B.md` before Step A finishes (wastes tokens on a playbook that will be replaced)
- Run Step B from a pre–Step A in-memory playbook
- Invent a broader audit than the top changelog entry
- Re-download / restore intentionally deleted `agent/upstream/` attribution files
- Treat `content-templates` as reshape permission — add missing structure only
- Under **`choose`:** silently skip reshape / TODO ambition asks when tagged
- Under **`auto`:** re-ask for reshape / ambition / rules refresh
- Ask before refreshing installed rules unless `customized: true`
- On reshape execute: only add template headings and leave obsolete Understanding sections
- On TODO ambition execute: invent work or collapse real human/shared blockers
- Skip presenting unset optionals (“do not auto-enable” means ask — not silence)
- Bootstrap a new project (use [`bootstrap.md`](bootstrap.md))
- Implement application features
