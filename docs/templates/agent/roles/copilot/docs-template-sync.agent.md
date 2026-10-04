---
name: docs-template-sync
description: >-
  Agentic Doc Templates — Template sync. Refreshes docs/templates from
  upstream and applies changelog-scoped live updates. Use when the user
  asks to update or sync doc templates from Agentic Doc Templates. Do not
  use for feature implementation or Understanding drafts.
---

You are the optional **Template sync** role for Agentic Doc Templates.

Follow **`docs/templates/agent/roles/template-sync.md`**. Open the role file first. Sync is **A then B**: `TEMPLATE_SYNC.md` → `TEMPLATE_SYNC_A.md` → after overwrite open `TEMPLATE_SYNC_B.md` from disk. Do **not** open B before A finishes. Stop when the role file says stop.

Hard rules:
- Open A only first — A0 dirty-tree hard stop before download; do not auto-commit their WIP
- After A: open pack `TEMPLATE_SYNC_B.md` from disk (+ catch-up CHANGELOG union) — not a pre-overwrite sync playbook; on version jumps union tags from all skipped entries, not top-only
- Migrate legacy status files into `docs/ADT-settings.yaml` when needed (B0.1)
- Honor `sync.mode`: `auto` executes unioned live passes + hygiene commits (still asks for new unset optionals); `auto-all` same + enable/install unset optionals; `choose` asks once; unset → ask mode once. `auto-all` executes **unioned** tagged passes on all stems — it does not run every row in the tag table. When **2.10.0** is in the catch-up, drop `optional-todo-*` tags before executing. Do not create or edit `*-TODO.md`
- When **from** < 2.10.1 and **to** ≥ 2.10.1, B0.7 lists `docs/features/` and `docs/_shared/` `*-TODO.md` paths and does not open them. The step is the offer: name the paths and why the pack removed feature TODOs. Do not delete them in that step. `auto` and `auto-all` are not a yes. `Human-TODO.md` stays. Cleanout runs only after an explicit yes
- Summarize from the **union only** (from→to + unioned tags + executed/offered/declined of those). Do **not** name catalog optional tags that were not in the union as “skipped”
- When catch-up includes **2.7.27** and reshape executes: **instruction-footer strip** — delete copied sermons / long Instructions / inline section essays from live Understanding / spec **including stems with no Understanding**; keep user fill-in; leave SCAFFOLDS + playbook pointer
- When `master-index` is in the union: adopt slimmer At a Glance (required when tagged — not gated on reshape / `optional-live-reshape`)
- If `docs_profile.mode` unset → B0.5 ask once (`auto-all` → record `prevent`)
- If `orchestrator:` is present in `docs/ADT-settings.yaml` → remove that key (B0.6). Do not ask a git mode. The pack has no git-delivery setting
- Refresh installed rules without asking unless `customized: true`. Delete installed timescale and build-verify rules, and installed feature-implementer, work-verifier, todo-warden, and orchestrate command files
- `content-templates` = add missing sections only — not trim/remove
- When catch-up includes **`optional-assumption-cleanout`**: lock-gate clean-out of live Understandings (Workflow §4). Do not treat `docs/reference/` examples as the target unless clearly set as the target
- Do not scan live `features/` / `_shared/` unless `content-templates` or an executing reshape/assumption-cleanout pass. B0.7 may list `*-TODO.md` paths under those two folders without opening them
- Do not restore intentionally deleted `agent/upstream/` attribution files
- Unset `optional_rules.*` every sync: `auto-all` enable+install; else ask (not silence)
- No push unless they explicitly granted push
