# Role — Template sync *(optional)*

> **Opt-in.** Use only when the user asks for this role or names this file. Not always-on.

**Job:** Refresh `docs/templates/` from upstream and apply **changelog-scoped** live updates. Thin wrapper around the sync playbooks.

**Canonical procedure:** [`../TEMPLATE_SYNC.md`](../TEMPLATE_SYNC.md) → [`../TEMPLATE_SYNC_A.md`](../TEMPLATE_SYNC_A.md) → (after overwrite) [`../TEMPLATE_SYNC_B.md`](../TEMPLATE_SYNC_B.md) + catch-up [`../../CHANGELOG.md`](../../CHANGELOG.md) entries (union Live impact tags). Settings: [`../ADT-settings.example.yaml`](../ADT-settings.example.yaml) → live `docs/ADT-settings.yaml`.

## When to invoke

- User asks to update / sync doc templates from Agentic Doc Templates
- User says: *Template sync role*, *follow roles/template-sync.md*

## Inputs *(open only these)*

1. [`../TEMPLATE_SYNC.md`](../TEMPLATE_SYNC.md) (entry) then **only** [`../TEMPLATE_SYNC_A.md`](../TEMPLATE_SYNC_A.md) — do **not** open B yet
2. After A finishes: **only** [`../TEMPLATE_SYNC_B.md`](../TEMPLATE_SYNC_B.md) from disk + selected catch-up [`../../CHANGELOG.md`](../../CHANGELOG.md) entries (B0 Catch-up — not top-only on version jumps)
3. `docs/ADT-settings.yaml` (migrate legacy status files per B0.1 if needed; capture `from` before stamp)
4. Live files that Step B / Live impact tags name (usually `Master_Index.md`, versions — not every feature file)
5. On reshape / TODO ambition **execute**: only the Understanding/spec/TODO files for stems in scope

## Steps

1. Open entry [`TEMPLATE_SYNC.md`](../TEMPLATE_SYNC.md) → follow **A** only ([`TEMPLATE_SYNC_A.md`](../TEMPLATE_SYNC_A.md)). **A0 first:** dirty tree → hard stop; do not auto-commit their WIP.
2. When A’s handoff says so: open **local** [`TEMPLATE_SYNC_B.md`](../TEMPLATE_SYNC_B.md) from disk — discard any pre-overwrite sync procedure.
3. Run Step B from B + **unioned** catch-up changelog tags (including B0 settings migrate + sync.mode + B0.3 hygiene commits under `auto` / `auto-all` + **B0.4** cadence when due + **B0.5** docs_profile when unset + **B0.6** orchestrator.git when unset — **always ask git**, even under auto-all).
4. **Rules** when tagged: refresh installed tools via each `tools/<key>.md` — **no ask** unless `customized: true`.
5. **Reshape / TODO ambition** when tagged in the union: if `sync.mode: auto` or `auto-all` → execute all Document Map stems + hygiene commits; if `choose` → explain + ask once; if mode unset → B0.2 ask once then continue. Reshape only applies to stems that **have** Understanding files.
6. Summarize what changed (sync mode, docs_profile if set/asked, catch-up from→to if a jump, what executed, settings migration, git / commits).
7. Run B’s **Present / apply unset options** for missing `optional_rules.*` (`auto-all` enables + installs; `auto`/`choose` ask once).
8. **Stop.**

## Stop when

- A0 cleared (clean tree or explicit waive) and Step A handoff completed and Step B for the **unioned** catch-up tags is done,
- Tagged optional live passes were executed (`auto` / `auto-all`) or presented (`choose`),
- Unset optionals were presented (`auto`/`choose`), auto-enabled (`auto-all`), or already `enabled` / `declined`,
- `docs_profile` was set or left intentionally unset only if B0.5 was not yet due,
- `orchestrator.git.mode` was set or left intentionally unset only if B0.6 was not yet due, and
- You have not scanned live `features/` / `_shared/` unless `content-templates` or an executing reshape/ambition pass required it

## Do not

- Open `TEMPLATE_SYNC_B.md` before Step A finishes (wastes tokens on a playbook that will be replaced)
- Skip A0 dirty-tree hard stop (including under `auto` / `auto-all`)
- Auto-commit pre-sync WIP without an explicit commit ask from the user
- Run Step B from a pre–Step A in-memory playbook
- Invent a broader audit than the unioned catch-up tags + skimmed Step B one-shots
- Read **only the top** changelog entry when jumping versions — union all entries with **from** < version ≤ **to**
- Re-download / restore intentionally deleted `agent/upstream/` attribution files
- Treat `content-templates` as reshape permission — add missing structure only
- Under **`choose`:** silently skip reshape / TODO ambition asks when tagged
- Under **`auto` / `auto-all`:** re-ask for reshape / ambition / rules refresh / B0.3 hygiene commits
- Under **`auto-all`:** leave unset `optional_rules.*` unset, or flip **`declined`** back to enabled
- Ask before refreshing installed rules unless `customized: true`
- Push unless the user explicitly granted push
- On reshape execute: only add template headings and leave obsolete Understanding sections
- On TODO ambition execute: invent work or collapse real human/shared blockers
- Under **`auto` / `choose`:** skip presenting unset optionals (“do not auto-enable” means ask — not silence)
- Bootstrap a new project (use [`bootstrap.md`](bootstrap.md))
- Implement application features
