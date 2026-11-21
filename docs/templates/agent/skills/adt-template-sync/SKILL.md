---
name: adt-template-sync
description: Refresh the ADT pack and catch live docs up. Use when the user says update or sync the doc templates, update the doc templates, update ADT, or sync ADT.
---


> Use when the user asks to sync, migrate, or **update the doc templates**. Typical ask: *"Update the doc templates from Agentic Doc Templates and sync our live docs."*

**Do not read Step B here** — it lives in a separate file so you do not load live-doc procedure before the pack overwrite.

| Order | Open only | What |
|-------|-----------|------|
| 1 | [`TEMPLATE_SYNC_A.md`](TEMPLATE_SYNC_A.md) | Download / replace `docs/templates/` |
| 2 | [`TEMPLATE_SYNC_B.md`](TEMPLATE_SYNC_B.md) | **After** A finishes (or pack already refreshed) — changelog-gated live updates |

**Stop after opening A.** Follow A to the end; A tells you when to open B from disk. Never open B “for context” before A completes.
## Sync checklist


> **Opt-in.** Use only when the user asks for this role or names this file. Not always-on.

**Job:** Refresh `docs/templates/` from upstream and apply **changelog-scoped** live updates. Thin wrapper around the sync playbooks.

**Canonical procedure:** [`../TEMPLATE_SYNC.md`](SKILL.md) → [`../TEMPLATE_SYNC_A.md`](TEMPLATE_SYNC_A.md) → (after overwrite) [`../TEMPLATE_SYNC_B.md`](TEMPLATE_SYNC_B.md) + catch-up [`../../CHANGELOG.md`](/docs/templates/CHANGELOG.md) entries (union Live impact tags). Settings: [`../ADT-settings.example.yaml`](/docs/templates/agent/ADT-settings.example.yaml) → live `docs/ADT-settings.yaml`.

## When to invoke

- User asks to update / sync doc templates from Agentic Doc Templates
- User says: *Template sync role*, *follow roles/template-sync.md*

## Inputs

1. [`../TEMPLATE_SYNC.md`](SKILL.md) (entry) then **only** [`../TEMPLATE_SYNC_A.md`](TEMPLATE_SYNC_A.md) — do **not** open B yet
2. After A finishes: **only** [`../TEMPLATE_SYNC_B.md`](TEMPLATE_SYNC_B.md) from disk + selected catch-up [`../../CHANGELOG.md`](/docs/templates/CHANGELOG.md) entries (B0 Catch-up — not top-only on version jumps)
3. `docs/ADT-settings.yaml` (migrate legacy status files per B0.1 if needed; capture `from` before stamp)
4. Live files that Step B / Live impact tags name (usually `Master_Index.md`, versions — not every feature file)
5. On reshape / assumption tidy **execute**: Understanding and spec for stems in scope.

## Steps

1. Open entry [`TEMPLATE_SYNC.md`](SKILL.md) -> follow **A** only ([`TEMPLATE_SYNC_A.md`](TEMPLATE_SYNC_A.md)).
2. When A’s handoff says so: open **local** [`TEMPLATE_SYNC_B.md`](TEMPLATE_SYNC_B.md) from disk — discard any pre-overwrite sync procedure.
3. Run Step B from B + **unioned** catch-up release tags (including B0 settings migrate + sync.mode + **B0.3** cadence when due + **B0.4** docs_profile when unset).
4. **Rules** when tagged: refresh installed tools via each `tools/<key>.md` - **no ask** unless `customized: true`.
5. **Reshape / assumption clean-out** when tagged in the union: if `sync.mode: auto` or `auto-all` -> execute all Document Map stems; if `choose` -> explain + ask once; if mode unset -> B0.2 ask once then continue. Shape trim and assumption clean-out (Workflow Section 4) only apply to stems that **have** Understanding files. **2.7.27 in catch-up:** reshape includes the **instruction-footer strip** on **every** Document Map spec (including stems with no Understanding - delete copied sermons and inline section essays; keep fill-in). **`master-index` when tagged** adopts slimmer At a Glance even if reshape is declined. Assumption clean-out = lock-gate (obvious defaults; real forks only; reference examples are not the target unless clearly set). Kit leftovers stay on the existing spec. Do not create map rows for them.
6. Summarize **from the union only**: mode, from->to, unioned tags, executed / offered / declined **of those tags**, settings migration. Do **not** name catalog optional tags that were not in the union as skipped. `auto-all` = execute unioned tagged passes on all stems - not "run every tag in the table." If B0.6 applied, the same end message includes the offer (paths + why). That offer is not a union tag and not an executed pass.
7. Run B’s **Present / apply unset options** for missing `optional_rules.*` (`auto-all` enables + installs; `auto`/`choose` ask once).
8. **Stop.**

## Stop when

- Step A handoff completed and Step B for the **unioned** catch-up tags is done,
- Tagged optional live passes were executed (`auto` / `auto-all`) or presented (`choose`),
- Unset optionals were presented (`auto`/`choose`), auto-enabled (`auto-all`), or already `enabled` / `declined`,
- `docs_profile` was set or left intentionally unset only if B0.4 was not yet due,
- `docs/ADT-settings.yaml` has no `orchestrator:` key after B0.5, and
- You have not scanned live `features/` / `_shared/` unless `content-templates` or an executing reshape/assumption-cleanout pass required it, or B0.6 listed `*-TODO.md` paths without opening them, and you did not create or edit `*-TODO.md` when the catch-up includes >= 2.10.0, and you did not delete them unless the user had already said yes to B0.6

## Do not

- Open `TEMPLATE_SYNC_B.md` before Step A finishes
- Run Step B from a pre–Step A in-memory playbook
- Invent a broader audit than the unioned catch-up tags + skimmed Step B one-shots
- Read **only the top** changelog entry when jumping versions — union all entries with **from** < version ≤ **to**
- Re-download / restore intentionally deleted `agent/upstream/` attribution files
- Treat `content-templates` as reshape permission — add missing structure only
- Under **`choose`:** silently skip reshape / assumption tidy asks when tagged
- Under **`auto` / `auto-all`:** re-ask for reshape / assumption tidy / rules refresh
- Under **`auto-all`:** leave unset `optional_rules.*` unset, or flip **`declined`** back to enabled
- Ask before refreshing installed rules unless `customized: true`
- On reshape execute: only add template headings and leave obsolete Understanding sections **or** copied instruction sermons (2.7.27 strip)
- Under **`auto` / `choose`:** skip presenting unset optionals (“do not auto-enable” means ask — not silence)
- Bootstrap a new project (use [`bootstrap.md`](/docs/templates/agent/roles/bootstrap.md))
- Implement application features
- Create or extend `*-TODO.md` when the catch-up includes ≥ 2.10.0
- Treat `sync.mode: auto` or `sync.mode: auto-all` as a yes to the B0.6 offer, or delete leftover feature `*-TODO.md` files in the offer step. `docs/Human-TODO.md` is not part of that offer
- Name optional live tags that were not in the union as “skipped” (they were not this jump’s instructions)
- Treat `auto-all` as license to run every pass in the Live impact tag table
