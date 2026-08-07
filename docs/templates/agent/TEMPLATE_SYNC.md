# Template Sync — Entry

> Use when the user asks to sync, migrate, or **update the doc templates**. Typical ask: *"Update the doc templates from Agentic Doc Templates and sync our live docs."*

**Do not read Step B here** — it lives in a separate file so you do not load live-doc procedure before the pack overwrite.

| Order | Open only | What |
|-------|-----------|------|
| 1 | [`TEMPLATE_SYNC_A.md`](TEMPLATE_SYNC_A.md) | **Preflight** (dirty tree hard gate) → download / replace `docs/templates/` |
| 2 | [`TEMPLATE_SYNC_B.md`](TEMPLATE_SYNC_B.md) | **After** A finishes (or pack already refreshed) — changelog-gated live updates |

**Stop after opening A.** Follow A to the end; A tells you when to open B from disk. Never open B “for context” before A completes.
