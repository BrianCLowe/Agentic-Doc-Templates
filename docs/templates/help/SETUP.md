# Setting Up Modular Docs in Your Project

Human guide for adding [Agentic Doc Templates](https://github.com/BrianCLowe/Agentic-Doc-Templates) to an existing codebase. For agent-driven setup, point your agent at [`../agent/BOOTSTRAP.md`](../agent/BOOTSTRAP.md).

## Recommended: copy one folder

Copy **`docs/templates/`** from this repo into your project as **`your-project/docs/templates/`**.

That single folder includes workflow scaffolds, human guides (`help/`), agent setup (`agent/`), and the chat-ui pack. Your live project docs stay at `docs/` root — `Master_Index.md`, `features/`, `_shared/` — without extra instruction folders beside them.

You do **not** need the repo root `README.md`, `LICENSE.md`, or `CONTRIBUTING.md` in your project root. Keep attribution via `docs/templates/agent/upstream/` (see below) or a line in your own README.

**What's inside `docs/templates/`:**

| Subfolder / file | Contents |
|------------------|----------|
| `help/` | This file, [`USAGE.md`](USAGE.md), [`IDEA_CAPTURE_TIPS.md`](IDEA_CAPTURE_TIPS.md), [`USING_WITH_AGENTS.md`](USING_WITH_AGENTS.md) |
| `agent/` | [`BOOTSTRAP.md`](../agent/BOOTSTRAP.md), [`RULE_INSTALL.md`](../agent/RULE_INSTALL.md), [`TEMPLATE_SYNC.md`](../agent/TEMPLATE_SYNC.md), [`Modular_Documentation_Rule.mdc`](../agent/Modular_Documentation_Rule.mdc), [`Modular_Documentation_Rule.instructions.md`](../agent/Modular_Documentation_Rule.instructions.md), `rule-install-status.example.yaml` |
| `chat-ui/` | Short Grok/ChatGPT instructions — attach [`AGENT.md`](../chat-ui/AGENT.md) only |
| Root of `templates/` | `Master_Index_Template.md`, `Modular_Docs_Workflow.md`, feature templates |

## Other ways to add templates

| Method | Pros | Notes |
|--------|------|--------|
| **Copy `docs/templates/` only** | Clean project `docs/` root | Recommended |
| **Git submodule** | Easy upstream updates | Submodule path is often awkward; copy or sparse-checkout `docs/templates/` |
| **Clone whole repo into project** | Simple first copy | Root README, LICENSE, and CONTRIBUTING collide with yours — use agent [`BOOTSTRAP.md`](../agent/BOOTSTRAP.md) to move them to `docs/templates/agent/upstream/` |

## After templates are in place

1. Ask your agent to follow **`docs/templates/agent/BOOTSTRAP.md`** — creates `docs/Master_Index.md`, folders, and relocates upstream root files if needed.
2. Fill in project overview and Document Map in `Master_Index.md`.
3. Add first feature under `docs/features/` (agent drafts spec + Understanding + TODO; you review). Shared components under `docs/_shared/` get the **same note types** unless you explicitly except specific files.
4. Optionally install the modular doc rule — ask your agent to follow **`docs/templates/agent/RULE_INSTALL.md`**, or install manually (see below).

## Install the agent rule yourself (optional)

If you prefer not to ask an agent to run rule install, copy the rule templates from **`docs/templates/agent/`**:

| Tool | Source (in your project) | Typical install path |
|------|--------------------------|----------------------|
| **Cursor** | [`Modular_Documentation_Rule.mdc`](../agent/Modular_Documentation_Rule.mdc) | `.cursor/rules/modular-documentation.mdc` |
| **GitHub Copilot** | [`Modular_Documentation_Rule.instructions.md`](../agent/Modular_Documentation_Rule.instructions.md) | `.github/instructions/modular-documentation.instructions.md` or `.github/copilot-instructions.md` |
| **Claude Code, Cline, Continue, AGENTS.md** | Rule body from the `.mdc` file (drop Cursor frontmatter) | See [`USING_WITH_AGENTS.md`](USING_WITH_AGENTS.md) or [`RULE_INSTALL.md`](../agent/RULE_INSTALL.md) |

Do not edit the copies under `docs/templates/agent/` — they stay the upstream reference; install **copies** into your tool's config paths.

**Day-to-day use** (chat → docs, ideas mid-dev, converting design docs): see **[`USAGE.md`](USAGE.md)**.

**Updating templates later:** You do not need to re-copy the folder by hand. Ask your agent to update the doc templates — it downloads the latest `docs/templates/` from [Agentic-Doc-Templates](https://github.com/BrianCLowe/Agentic-Doc-Templates) and then updates your live docs (`Master_Index`, Understanding, TODOs) to match. Full procedure: [`../agent/TEMPLATE_SYNC.md`](../agent/TEMPLATE_SYNC.md).

**Brainstorming in Grok/ChatGPT before you have a repo?** Attach only [`../chat-ui/AGENT.md`](../chat-ui/AGENT.md) — see [`../chat-ui/README.md`](../chat-ui/README.md). Copy `docs/templates/` when you create the project.

**Describing ideas** (UI, flows, scope — especially if you are new to software): see **[`IDEA_CAPTURE_TIPS.md`](IDEA_CAPTURE_TIPS.md)**.

## Folder layout in your project

```
docs/
├── Master_Index.md              ← live project docs (you maintain)
├── rule-install-status.yaml     ← created when installing agent rules
├── _shared/
│   └── assets/
├── decisions/
├── features/
│   └── assets/
├── reference/
│   └── visuals/
└── templates/                   ← entire pack from Agentic Doc Templates
    ├── help/                    ← setup, usage, idea capture (this folder)
    ├── agent/                   ← bootstrap, rule install, template sync, rule templates
    │   ├── Modular_Documentation_Rule.mdc
    │   ├── Modular_Documentation_Rule.instructions.md
    │   └── upstream/            ← README, LICENSE, CONTRIBUTING moved here if whole repo was copied
    ├── chat-ui/
    ├── Master_Index_Template.md
    ├── Modular_Docs_Workflow.md
    └── …
```

## Naming and workflow

See the repo [README](https://github.com/BrianCLowe/Agentic-Doc-Templates) on GitHub for naming conventions, `Modular_Docs_Workflow.md`, shared foundation TODOs, Understanding files, and template sync.

## License

Templates are [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). Full text: [`../agent/upstream/LICENSE.md`](../agent/upstream/LICENSE.md) after bootstrap, or [LICENSE.md](https://github.com/BrianCLowe/Agentic-Doc-Templates/blob/main/LICENSE.md) in the GitHub repo.

Attribution example:

> Based on [Agentic Doc Templates](https://github.com/BrianCLowe/Agentic-Doc-Templates) by Brian Lowe, licensed under CC BY 4.0.
