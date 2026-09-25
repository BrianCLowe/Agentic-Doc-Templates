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
5. On reshape / assumption clean-out / TODO ambition / operable / kit-coverage / outcomes / completed cleanout **execute**: Understanding/spec/TODO for stems in scope (spec/TODO-only stems included on the 2.7.27 strip; completed cleanout opens that stem’s `-TODO.md` only)

## Steps

1. Open entry [`TEMPLATE_SYNC.md`](../TEMPLATE_SYNC.md) → follow **A** only ([`TEMPLATE_SYNC_A.md`](../TEMPLATE_SYNC_A.md)). **A0 first:** dirty tree → hard stop; do not auto-commit their WIP.
2. When A’s handoff says so: open **local** [`TEMPLATE_SYNC_B.md`](../TEMPLATE_SYNC_B.md) from disk — discard any pre-overwrite sync procedure.
3. Run Step B from B + **unioned** catch-up changelog tags (including B0 settings migrate + sync.mode + B0.3 hygiene commits under `auto` / `auto-all` + **B0.4** cadence when due + **B0.5** docs_profile when unset + **B0.6** orchestrator.git when unset — **always ask git**, even under auto-all).
4. **Rules** when tagged: refresh installed tools via each `tools/<key>.md` — **no ask** unless `customized: true`.
5. **Reshape / assumption clean-out / TODO ambition / operable / kit-coverage / outcomes / completed cleanout** when tagged in the union: if `sync.mode: auto` or `auto-all` → execute all Document Map stems + hygiene commits; if `choose` → explain + ask once; if mode unset → B0.2 ask once then continue. Shape trim and assumption clean-out (Workflow §4) only apply to stems that **have** Understanding files. **2.7.27 in catch-up:** reshape includes the **instruction-footer strip** on **every** Document Map spec / core TODO (including stems with no Understanding — delete copied sermons and inline section essays; keep fill-in). **`master-index` when tagged** adopts slimmer At a Glance even if reshape is declined. Kit-coverage is spec→TODO on existing stems (Workflow §5.4) — no vendor-doc fetch, no new map rows. Outcomes (Workflow §5.5) mirrors operable Acceptance into unchecked Outcomes rows, labels children, and adds one exercise task when an outcome has no path — do not check outcomes; do **not** create a human-verify playtest (the outcome audit is the only creator of that row); do not mint a task per architecture bullet. Completed cleanout removes a `## Completed` checkbox that `git log -p` never shows as `- [ ]` and whose text is an incidental fix. Keep a row that was ever an open task. Keep an exercise note. Unsure → leave the row. Do not remove open tasks. Do not check Outcomes. Assumption clean-out = lock-gate (obvious defaults; real forks only; reference examples are not the target unless clearly set).
6. Summarize **from the union only**: mode, from→to, unioned tags, executed / offered / declined **of those tags**, settings migration, git / commits. Do **not** name catalog optional tags that were not in the union as skipped. `auto-all` = execute unioned tagged passes on all stems — not “run every tag in the table.”
7. Run B’s **Present / apply unset options** for missing `optional_rules.*` (`auto-all` enables + installs; `auto`/`choose` ask once).
8. **Stop.**

## Stop when

- A0 cleared (clean tree or explicit waive) and Step A handoff completed and Step B for the **unioned** catch-up tags is done,
- Tagged optional live passes were executed (`auto` / `auto-all`) or presented (`choose`),
- Unset optionals were presented (`auto`/`choose`), auto-enabled (`auto-all`), or already `enabled` / `declined`,
- `docs_profile` was set or left intentionally unset only if B0.5 was not yet due,
- `orchestrator.git.mode` was set or left intentionally unset only if B0.6 was not yet due, and
- You have not scanned live `features/` / `_shared/` unless `content-templates` or an executing reshape/assumption-cleanout/ambition/operable/kit-coverage/outcomes/completed-cleanout pass required it

## Do not

- Open `TEMPLATE_SYNC_B.md` before Step A finishes (wastes tokens on a playbook that will be replaced)
- Skip A0 dirty-tree hard stop (including under `auto` / `auto-all`)
- Auto-commit pre-sync WIP without an explicit commit ask from the user
- Run Step B from a pre–Step A in-memory playbook
- Invent a broader audit than the unioned catch-up tags + skimmed Step B one-shots
- Read **only the top** changelog entry when jumping versions — union all entries with **from** < version ≤ **to**
- Re-download / restore intentionally deleted `agent/upstream/` attribution files
- Treat `content-templates` as reshape permission — add missing structure only
- Under **`choose`:** silently skip reshape / assumption clean-out / TODO ambition / operable / kit-coverage / outcomes / completed cleanout asks when tagged
- Under **`auto` / `auto-all`:** re-ask for reshape / assumption clean-out / ambition / operable / kit-coverage / outcomes / completed cleanout / rules refresh / B0.3 hygiene commits
- Under **`auto-all`:** leave unset `optional_rules.*` unset, or flip **`declined`** back to enabled
- Ask before refreshing installed rules unless `customized: true`
- Push unless the user explicitly granted push
- On reshape execute: only add template headings and leave obsolete Understanding sections **or** copied instruction sermons (2.7.27 strip)
- On TODO ambition execute: invent work or collapse real human/shared blockers
- On TODO outcomes execute: check an Outcomes row, or create a human-verify playtest (the outcome audit is the only creator of that row)
- On TODO completed-cleanout execute: remove a plotted slice or an exercise note; remove a row whose title ever appeared as `- [ ]`; remove when unsure; remove open tasks; check Outcomes
- Under **`auto` / `choose`:** skip presenting unset optionals (“do not auto-enable” means ask — not silence)
- Bootstrap a new project (use [`bootstrap.md`](bootstrap.md))
- Implement application features
- Rewrite an already-set `orchestrator.git.mode` unless the user asked this turn (then stamp `source: user`)
- Treat a `source: user` git-mode change as a forbidden pack migrate (reviewers / Bugbot: do not fail it)
- Name optional live tags that were not in the union as “skipped” (they were not this jump’s instructions)
- Treat `auto-all` as license to run every pass in the Live impact tag table
