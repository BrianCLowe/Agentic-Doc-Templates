# Role — Template sync *(optional)*

> **Opt-in.** Use only when the user asks for this role or names this file. Not always-on.

**Job:** Refresh `docs/templates/` from upstream and apply **changelog-scoped** live updates. Thin wrapper around the sync playbooks.

**Canonical procedure:** [`../TEMPLATE_SYNC.md`](../TEMPLATE_SYNC.md) → [`../TEMPLATE_SYNC_A.md`](../TEMPLATE_SYNC_A.md) → (after overwrite) [`../TEMPLATE_SYNC_B.md`](../TEMPLATE_SYNC_B.md) + top [`../../CHANGELOG.md`](../../CHANGELOG.md) entry.

## When to invoke

- User asks to update / sync doc templates from Agentic Doc Templates
- User says: *Template sync role*, *follow roles/template-sync.md*

## Inputs *(open only these)*

1. [`../TEMPLATE_SYNC.md`](../TEMPLATE_SYNC.md) (entry) then **only** [`../TEMPLATE_SYNC_A.md`](../TEMPLATE_SYNC_A.md) — do **not** open B yet
2. After A finishes: **only** [`../TEMPLATE_SYNC_B.md`](../TEMPLATE_SYNC_B.md) from disk + **only the top** [`../../CHANGELOG.md`](../../CHANGELOG.md) entry
3. Live files that Step B / Live impact tags name (usually `Master_Index.md`, versions — not every feature file)
4. On accepted `optional-live-reshape`: only the Understanding + spec (+ TODO if needed) for stems the user chose
5. On accepted `optional-todo-ambition`: only the `*-TODO.md` (+ Understanding) for stems the user chose

## Steps

1. Open entry [`TEMPLATE_SYNC.md`](../TEMPLATE_SYNC.md) → follow **A** only ([`TEMPLATE_SYNC_A.md`](../TEMPLATE_SYNC_A.md)). Do not read B “for context.”
2. When A’s handoff says so: open **local** [`TEMPLATE_SYNC_B.md`](../TEMPLATE_SYNC_B.md) from disk — discard any pre-overwrite sync procedure.
3. Run Step B from B + top changelog entry’s tags only.
4. If `optional_rules.doc-roles` is `enabled` and changelog tags `rules`, for each `tools.*.status: installed` tool open `docs/templates/agent/tools/<key>.md` only and refresh that harness’s agents folder — ask if customized.
5. If tagged `optional-live-reshape`: run B’s **Live Understanding reshape** — **highly recommended**; explain drift risk + ask once (default: all stems / named / no). Suggest committing the pack sync first so reshape is a separate commit (ask — do **not** auto-commit). Do **not** silent-skip. On yes: trim + relocate per Workflow §4 — **not** add-sections-only.
6. If tagged `optional-todo-ambition`: run B’s **Live TODO ambition** — explain + ask once (default: all Document Map TODO stems / named / no). Suggest committing pack sync first (ask — do **not** auto-commit). Do **not** silent-skip. On yes: streamline High Priority / Current focus toward target architecture; preserve real blockers; do not invent work.
7. Summarize what changed (include reshape / TODO ambition offered + accepted/declined + whether a separate commit was suggested).
8. Run B’s **Present unset options** — explain + ask once for any missing `optional_rules.*`. Do **not** stay silent because status is unset or because an installed tool has no adapter install.
9. **Stop.**

## Stop when

- Step A handoff completed and Step B for the top changelog entry is done,
- `optional-live-reshape` was presented (and executed or declined) when tagged,
- `optional-todo-ambition` was presented (and executed or declined) when tagged,
- Unset optionals were presented (or already `enabled` / `declined`), and
- You have not scanned live `features/` / `_shared/` unless `content-templates` or (`optional-live-reshape` and user said yes) or (`optional-todo-ambition` and user said yes)

## Do not

- Open `TEMPLATE_SYNC_B.md` before Step A finishes (wastes tokens on a playbook that will be replaced)
- Run Step B from a pre–Step A in-memory playbook
- Invent a broader audit than the top changelog entry
- Re-download / restore intentionally deleted `agent/upstream/` attribution files
- Treat `content-templates` as reshape permission — add missing structure only
- Auto-rewrite or silently skip live Understanding bodies when `optional-live-reshape` is tagged — **ask**
- Auto-rewrite or silently skip live TODOs when `optional-todo-ambition` is tagged — **ask**
- On reshape yes: only add template headings and leave obsolete Understanding sections
- On TODO ambition yes: invent work or collapse real human/shared blockers
- Skip presenting unset optionals (“do not auto-enable” means ask — not silence)
- Bootstrap a new project (use [`bootstrap.md`](bootstrap.md))
- Implement application features
