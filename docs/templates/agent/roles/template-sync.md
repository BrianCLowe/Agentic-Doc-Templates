# Role — Template sync *(optional)*

> **Opt-in.** Use only when the user asks for this role or names this file. Not always-on.

**Job:** Refresh `docs/templates/` from upstream and apply **changelog-scoped** live updates. Thin wrapper around the sync playbook.

**Canonical procedure:** [`../TEMPLATE_SYNC.md`](../TEMPLATE_SYNC.md) + top entry of [`../../CHANGELOG.md`](../../CHANGELOG.md).

## When to invoke

- User asks to update / sync doc templates from Agentic Doc Templates
- User says: *Template sync role*, *follow roles/template-sync.md*

## Inputs *(open only these)*

1. [`../TEMPLATE_SYNC.md`](../TEMPLATE_SYNC.md)
2. After Step A: **only the top** [`../../CHANGELOG.md`](../../CHANGELOG.md) entry
3. Live files that Step B / Live impact tags name (usually `Master_Index.md`, versions — not every feature file)

## Steps

1. Follow TEMPLATE_SYNC Step A (overwrite pack), then Step B from the top changelog entry’s tags only.
2. If `optional_rules.doc-roles` is `enabled` and changelog tags `rules`, for each `tools.*.status: installed` tool open `docs/templates/agent/tools/<key>.md` only and refresh that harness’s agents folder — ask if customized.
3. Summarize what changed. **Stop.**

## Stop when

- Step B for the top changelog entry is done (or user declined optional refreshes), and
- You have not scanned live `features/` / `_shared/` unless a Live impact tag required it

## Do not

- Invent a broader audit than the top changelog entry
- Re-download / restore intentionally deleted `agent/upstream/` attribution files
- Rewrite live Understanding/spec/TODO content “to match new templates” unless tagged `content-templates`
- Bootstrap a new project (use [`bootstrap.md`](bootstrap.md))
- Implement application features
