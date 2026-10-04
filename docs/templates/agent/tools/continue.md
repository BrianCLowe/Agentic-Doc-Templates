# Tool install — Continue.dev *(thin)*

> **Status key:** `continue`  
> Open only when installing or refreshing Continue for this repo.  
> Docs: [Rules](https://docs.continue.dev/customize/deep-dives/rules)

## Modular rule

| | |
|--|--|
| **Source** | Rule body from `docs/templates/agent/Modular_Documentation_Rule.mdc` + Continue Markdown frontmatter (`name`, `description`, `alwaysApply: true`) |
| **Install to** | `.continue/rules/modular-documentation.md` |
| **Notes** | Rules apply to Agent/Chat/Edit — not autocomplete. Prefer Markdown over legacy YAML. |

## Retired rules *(delete on refresh)*

The pack no longer ships timescale or build-verify rules. **Delete** `.continue/rules/agent-timescale-planning.md` and `.continue/rules/agent-build-verify.md` if present.

## Optional — Template update check

If enabled: same pattern → `.continue/rules/template-update-check.md` from `Template_Update_Check_Rule.mdc` body + frontmatter.

## Optional — Doc roles

No first-class Continue agents folder in this pack. Follow `docs/templates/agent/roles/<role>.md` in-session when asks match.

## Optional — Slash commands

No command folder. On enable, record `optional_rules.slash-commands` and do not invent files. The short asks stay the path.

## Verify

- `modular-documentation.md` exists under `.continue/rules/`
- Timescale and build-verify rules are **absent**

## For humans

Docs: [Continue rules](https://docs.continue.dev/customize/deep-dives/rules).
