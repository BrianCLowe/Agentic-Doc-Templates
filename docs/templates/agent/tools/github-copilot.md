# Tool install — GitHub Copilot (VS Code Chat, Agents window, CLI)

> **Status key:** `github-copilot`  
> Open only when installing or refreshing Copilot for this repo.  
> Docs: [Custom instructions](https://code.visualstudio.com/docs/copilot/customization/custom-instructions) · [Custom agents](https://code.visualstudio.com/docs/copilot/customization/custom-agents) · [CLI custom agents](https://docs.github.com/en/copilot/concepts/agents/copilot-cli/about-custom-agents) · [Agents window](https://code.visualstudio.com/docs/copilot/agents/agents-window)

## Modular rule

| | |
|--|--|
| **Source** | `docs/templates/agent/Modular_Documentation_Rule.instructions.md` |
| **Install to** | `.github/instructions/modular-documentation.instructions.md` *(preferred)* **or** append a labeled section to `.github/copilot-instructions.md` |
| **Notes** | Applies to Chat / Agent mode, not inline autocomplete. Ask before overwriting. Enable `.github/instructions` in workspace settings if needed (`chat.instructionsFilesLocations`). |

## Agent timescale planning *(core — always install with modular rule)*

| | |
|--|--|
| **Source** | `docs/templates/agent/Agent_Timescale_Planning_Rule.instructions.md` |
| **Install to** | `.github/instructions/agent-timescale-planning.instructions.md` or labeled section in `copilot-instructions.md` |

## Agent build & verify *(core — always install with modular rule)*

| | |
|--|--|
| **Source** | `docs/templates/agent/Agent_Build_Verify_Rule.instructions.md` |
| **Install to** | `.github/instructions/agent-build-verify.instructions.md` or labeled section in `copilot-instructions.md` |

## Optional — Template update check

Only if `optional_rules.template-update-check.status` is `enabled`.

| | |
|--|--|
| **Source** | `docs/templates/agent/Template_Update_Check_Rule.instructions.md` |
| **Install to** | `.github/instructions/template-update-check.instructions.md` or labeled section in `copilot-instructions.md` |

## Optional — Doc roles

Only if `optional_rules.doc-roles.status` is `enabled`. Copilot custom agents (CLI, Agents window, Chat dropdown): [CLI custom agents](https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/create-custom-agents-for-cli) → `.github/agents/*.agent.md`.

Copilot does **not** load `.cursor/agents/` / `.grok/agents/` as named subagents. Install the Copilot adapters into `.github/agents/` so the Agents window and `copilot` CLI can see them.

| | |
|--|--|
| **Adapter source** | `docs/templates/agent/roles/copilot/*.agent.md` *(generated from [`../roles/adapter-src/`](../roles/adapter-src/README.md) — do not hand-edit; do not copy `roles/cursor/` here)* |
| **Install to** | `.github/agents/` (same filenames, including the `.agent.md` suffix) |
| **Parent delegates** | If `.github/agents/<name>.agent.md` exists → delegate that custom agent with a self-contained prompt (CLI `/agent` or inference; Agents window / Chat dropdown). Else role playbook fallback |
| **Do not** | Install under `.cursor/agents/`; copy Cursor `model: inherit` adapters into `.github/agents/`; use user-global `~/.copilot/agents/` as the pack target |

Files: `understanding-author.agent.md`, `doc-graduate.agent.md`, `feature-implementer.agent.md`, `work-verifier.agent.md`, `todo-warden.agent.md`, `docs-bootstrap.agent.md`, `docs-template-sync.agent.md`.

**Do not** install an `orchestrator` adapter — orchestration runs in the **parent** session via `docs/templates/agent/roles/orchestrator.md` (spawns leaf workers only).

## Verify

- Modular + agent-timescale + agent-build-verify instructions exist under `.github/instructions/` or `copilot-instructions.md`
- Optional: `/init` then confirm modular docs section present
- If doc-roles enabled: seven files under `.github/agents/` (no `orchestrator`; includes `todo-warden.agent.md`)
- Custom agents appear in Chat **Configure Custom Agents** / CLI `/agent` (custom list) / Agents window Customizations

## For humans

Chat view and the Agents window share `.github/agents/` and `.github/instructions/`, but **not** the same chat history (Agents window / CLI are Agent Host sessions). Monorepo: enable `chat.useCustomizationsInParentRepositories` when opening a subfolder. Docs: [VS Code custom instructions](https://code.visualstudio.com/docs/copilot/customization/custom-instructions) · [Agents window](https://code.visualstudio.com/docs/copilot/agents/agents-window).

## Do not

- Expect Copilot to load `.cursor/agents/` as subagents
- Paste role playbook bodies into always-on Copilot instructions
- Skip offering doc-roles because an older pack said Install was None — this tool now has an agents-folder install
