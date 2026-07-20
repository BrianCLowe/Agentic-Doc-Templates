# Tool install — GitHub Copilot (VS Code)

> **Status key:** `github-copilot`  
> Open only when installing or refreshing Copilot for this repo.  
> Docs: [Custom instructions](https://code.visualstudio.com/docs/copilot/customization/custom-instructions)

## Modular rule

| | |
|--|--|
| **Source** | `docs/templates/agent/Modular_Documentation_Rule.instructions.md` |
| **Install to** | `.github/instructions/modular-documentation.instructions.md` *(preferred)* **or** append a labeled section to `.github/copilot-instructions.md` |
| **Notes** | Applies to Chat / Agent mode, not inline autocomplete. Ask before overwriting. Enable `.github/instructions` in workspace settings if needed (`chat.instructionsFilesLocations`). |

## Optional — Template update check

Only if `optional_rules.template-update-check.status` is `enabled`.

| | |
|--|--|
| **Source** | `docs/templates/agent/Template_Update_Check_Rule.instructions.md` |
| **Install to** | `.github/instructions/template-update-check.instructions.md` or labeled section in `copilot-instructions.md` |

## Optional — Doc roles

Copilot does **not** use `.cursor/agents/` / `.grok/agents/` as first-class named subagents in this pack. That does **not** mean there is nothing to offer — still present `optional_rules.doc-roles` when unset (bootstrap Step 4c / TEMPLATE_SYNC present-unset-options).

| | |
|--|--|
| **Install** | **None** for agent adapter files |
| **Runtime** | Parent follows `docs/templates/agent/roles/<role>.md` in-session when the modular rule’s ask matches |
| **On enable** | Record `optional_rules.doc-roles: enabled` so the decision is explicit; playbooks already on disk after pack sync |
| **Also using Cursor / Grok / Claude?** | Install adapters via those tool files when those tools are `installed` |

## Verify

- Instructions file exists under `.github/instructions/` or `copilot-instructions.md`
- Optional: `/init` then confirm modular docs section present

## For humans

Monorepo: enable `chat.useCustomizationsInParentRepositories` when opening a subfolder. Docs: [VS Code custom instructions](https://code.visualstudio.com/docs/copilot/customization/custom-instructions).

## Do not

- Expect Copilot to load `.cursor/agents/` as subagents
- Paste role playbook bodies into always-on Copilot instructions
- Skip offering doc-roles because Install is None — explain in-session playbooks and ask once when unset
