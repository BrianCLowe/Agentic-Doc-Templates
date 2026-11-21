# Tool install — Continue.dev *(thin)*

> **Status key:** `continue`  
> Open only when installing or refreshing Continue for this project.  
> Docs: [Rules](https://docs.continue.dev/customize/deep-dives/rules)

## Modular rule

| | |
|--|--|
| **Source** | Rule body from `docs/templates/agent/Modular_Documentation_Rule.mdc` + Continue Markdown frontmatter (`name`, `description`, `alwaysApply: true`) |
| **Install to** | `.continue/rules/modular-documentation.md` |
| **Notes** | Rules apply to Agent/Chat/Edit — not autocomplete. Prefer Markdown over legacy YAML. |

## Optional — Template update check

If enabled: same pattern → `.continue/rules/template-update-check.md` from `Template_Update_Check_Rule.mdc` body + frontmatter.

## Optional — Doc roles

No first-class Continue agents folder in this pack. Follow `docs/templates/agent/roles/<role>.md` in-session when asks match.

No skills loader. Route skill asks through the AGENTS.md skills table ([`agents-md.md`](agents-md.md)) or open `docs/templates/agent/skills/<name>/SKILL.md` directly.

## Verify

- `modular-documentation.md` exists under `.continue/rules/`

## For humans

Docs: [Continue rules](https://docs.continue.dev/customize/deep-dives/rules).
