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

## Agent timescale planning *(core — always install with modular rule)*

| | |
|--|--|
| **Source** | Rule body from `docs/templates/agent/Agent_Timescale_Planning_Rule.mdc` (strip Cursor frontmatter) |
| **Install to** | `.clinerules/agent-timescale-planning.md` |

## Agent build & verify *(core — always install with modular rule)*

| | |
|--|--|
| **Source** | Rule body from `docs/templates/agent/Agent_Build_Verify_Rule.mdc` (strip Cursor frontmatter) |
| **Install to** | `.clinerules/agent-build-verify.md` |

## Optional — Template update check

If enabled: `.clinerules/template-update-check.md`.

## Optional — Doc roles

No first-class Cline agents folder in this pack. Follow role playbooks in-session. Consider [`agents-md.md`](agents-md.md) for a shared baseline.

## Verify

- `modular-documentation.md`, `agent-timescale-planning.md`, and `agent-build-verify.md` exist under `.clinerules/`
- Visible/toggled in Cline’s Rules panel

## For humans

Conditional rules use YAML `paths:` frontmatter (see Cline docs). Global personal rules live under the OS Documents `Cline/Rules` folder — not used by this pack.
