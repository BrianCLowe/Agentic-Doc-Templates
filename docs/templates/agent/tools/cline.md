# Tool install — Cline *(thin)*

> **Status key:** `cline`  
> Open only when installing or refreshing Cline for this repo.

## Modular rule

| | |
|--|--|
| **Source** | Rule body from `docs/templates/agent/Modular_Documentation_Rule.mdc` (strip Cursor frontmatter; optional Cline `paths` frontmatter) |
| **Install to** | `.clinerules/modular-documentation.md` or `.cline/rules/modular-documentation.md` |

## Optional — Template update check

If enabled: matching path under `.clinerules/` or `.cline/rules/`.

## Optional — Doc roles

No first-class Cline agents folder in this pack. Follow role playbooks in-session. Cline also reads root `AGENTS.md` — consider [`agents-md.md`](agents-md.md).

## Verify

- Rule file exists at the chosen Cline path

## For humans

Docs: [Cline rules](https://docs.cline.bot/customization/cline-rules).
