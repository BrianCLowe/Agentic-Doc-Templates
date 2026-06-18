# Setting Up Modular Docs in Your Project

Human guide for adding [Agentic Doc Templates](https://github.com/BrianCLowe/Agentic-Doc-Templates) to an existing codebase. For agent-driven setup, point your agent at [`../agent/BOOTSTRAP.md`](../agent/BOOTSTRAP.md).

## Recommended: copy three folders

Copy these from this repo into your project (keep the same paths under `docs/`):

| Copy from repo | Into your project |
|----------------|-------------------|
| `docs/help/` | `your-project/docs/help/` |
| `docs/agent/` | `your-project/docs/agent/` |
| `docs/templates/` | `your-project/docs/templates/` |

You do **not** need the repo root `README.md` or `LICENSE.md` in your project root. Keep attribution via `docs/agent/upstream/` (see below) or a line in your own README.

**What's in each folder:**

| Folder | Contents |
|--------|----------|
| `docs/help/` | This file, [`USAGE.md`](USAGE.md), [`IDEA_CAPTURE_TIPS.md`](IDEA_CAPTURE_TIPS.md), [`USING_WITH_AGENTS.md`](USING_WITH_AGENTS.md) |
| `docs/agent/` | [`BOOTSTRAP.md`](../agent/BOOTSTRAP.md), [`RULE_INSTALL.md`](../agent/RULE_INSTALL.md), [`TEMPLATE_SYNC.md`](../agent/TEMPLATE_SYNC.md), `rule-install-status.example.yaml` |
| `docs/templates/` | Workflow + scaffolds (`Master_Index_Template.md`, `Modular_Docs_Workflow.md`, `chat-ui/`, feature templates, rule files to install) |

## Other ways to add templates

| Method | Pros | Notes |
|--------|------|--------|
| **Copy `help/`, `agent/`, `templates/`** | Clean project root | Recommended |
| **Git submodule** | Easy upstream updates | Submodule path is often awkward; copy or sparse-checkout the three folders |
| **Clone whole repo into project** | Simple first copy | Root README/LICENSE collide with yours — use agent [`BOOTSTRAP.md`](../agent/BOOTSTRAP.md) to move them to `docs/agent/upstream/` |

## After templates are in place

1. Ask your agent to follow **`docs/agent/BOOTSTRAP.md`** — creates `docs/Master_Index.md`, folders, and relocates upstream root files if needed.
2. Fill in project overview and Document Map in `Master_Index.md`.
3. Add first feature under `docs/features/` (agent drafts spec + Understanding + TODO; you review). Shared components under `docs/_shared/` get the **same note types** unless you explicitly except specific files.
4. Optionally run **`docs/agent/RULE_INSTALL.md`** for your agent tool(s).

**Day-to-day use** (chat → docs, ideas mid-dev, converting design docs): see **[`USAGE.md`](USAGE.md)**.

**Brainstorming in Grok/ChatGPT before you have a repo?** Attach only [`../templates/chat-ui/AGENT.md`](../templates/chat-ui/AGENT.md) — see [`../templates/chat-ui/README.md`](../templates/chat-ui/README.md). Copy all three folders when you create the project.

**Describing ideas** (UI, flows, scope — especially if you are new to software): see **[`IDEA_CAPTURE_TIPS.md`](IDEA_CAPTURE_TIPS.md)**.

## Folder layout in your project

```
docs/
├── Master_Index.md
├── rule-install-status.yaml     ← created when installing agent rules
├── help/                        ← human guides (this folder)
│   ├── SETUP.md
│   ├── USAGE.md
│   ├── IDEA_CAPTURE_TIPS.md
│   └── USING_WITH_AGENTS.md
├── agent/                       ← agent setup & maintenance
│   ├── BOOTSTRAP.md
│   ├── RULE_INSTALL.md
│   ├── TEMPLATE_SYNC.md
│   ├── rule-install-status.example.yaml
│   └── upstream/                ← README + LICENSE moved here if whole repo was copied
├── _shared/
│   └── assets/
├── decisions/
├── features/
│   └── assets/
├── reference/
│   └── visuals/
└── templates/                   ← workflow + scaffolds only
    ├── Master_Index_Template.md
    ├── Modular_Docs_Workflow.md
    ├── chat-ui/AGENT.md
    ├── Feature_*_Template.md
    └── Modular_Documentation_Rule.*
```

## Naming and workflow

See the repo [README](https://github.com/BrianCLowe/Agentic-Doc-Templates) on GitHub for naming conventions, `Modular_Docs_Workflow.md`, shared foundation TODOs, Understanding files, and template sync.

## License

Templates are [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). Full text: [`../agent/upstream/LICENSE.md`](../agent/upstream/LICENSE.md) after bootstrap, or [LICENSE.md](https://github.com/BrianCLowe/Agentic-Doc-Templates/blob/main/LICENSE.md) in the GitHub repo.

Attribution example:

> Based on [Agentic Doc Templates](https://github.com/BrianCLowe/Agentic-Doc-Templates) by Brian Lowe, licensed under CC BY 4.0.
