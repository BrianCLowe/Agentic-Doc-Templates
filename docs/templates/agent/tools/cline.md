# Tool install — Cline *(thin)*

> **Status key:** `cline`  
> Open only when installing or refreshing Cline for this repo.  
> Docs: [Rules](https://docs.cline.bot/customization/cline-rules)

## Modular rule

| | |
|--|--|
| **Source** | Rule body from `docs/templates/agent/Modular_Documentation_Rule.mdc` (strip Cursor frontmatter; optional `paths` frontmatter for conditional rules) |
| **Install to** | `.clinerules/modular-documentation.md` *(primary — current Cline docs)* |
| **Notes** | Cline also auto-detects `AGENTS.md` and some other tools’ rule files. Prefer `.clinerules/` for pack-owned installs. |

## Retired rules *(delete on refresh)*

The pack no longer ships timescale or build-verify rules. **Delete** `.clinerules/agent-timescale-planning.md` and `.clinerules/agent-build-verify.md` if present.

## Optional — Template update check

If enabled: `.clinerules/template-update-check.md`.

## Optional — Doc roles

No first-class Cline agents folder in this pack. Follow role playbooks in-session. Consider [`agents-md.md`](agents-md.md) for a shared baseline.

## Optional — Slash commands

No command folder. On enable, record `optional_rules.slash-commands` and do not invent files. The short asks stay the path.

## Verify

- `modular-documentation.md` exists under `.clinerules/`
- Timescale and build-verify rules are **absent**
- Visible/toggled in Cline’s Rules panel

## For humans

Conditional rules use YAML `paths:` frontmatter (see Cline docs). Global personal rules live under the OS Documents `Cline/Rules` folder — not used by this pack.
