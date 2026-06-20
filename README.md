# Agentic Doc Templates

> **Documentation templates for agentic AI coding tools.**
> Keep AI agents aligned with your intent across conversations, features, and long-running projects.

[![License: CC BY 4.0](https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)
![Template](https://img.shields.io/badge/Template-Ready-blue)
![Built for](https://img.shields.io/badge/Built%20for-Cursor%20%7C%20Grok%20Build%20%7C%20Claude%20Code-5865F2)

**Quick start:** Click the green **"Use this template"** button at the top of this page to instantly create a new repository with the full `docs/` structure.

---

## Why these templates exist

AI coding agents are powerful but can drift from your original intent over long sessions. These templates give agents a consistent structure: the **agent writes** Understanding and TODO files from your conversation; **you review and correct** them before implementation.

The goal: lightweight documentation that stays in sync with the code and is easy for both people and vision-capable agents to use. No complex instructions needed — point your agent at the templates and it will understand how to use them.

## Quick Start

### Option 1: Use as Template (Recommended)
1. Click **"Use this template"** (green button at the top)
2. Create a new repository in your account
3. Discuss your app idea with your agent or drop in your current docs and ask it to turn it into modular documentation with an appropriate .gitignore
4. Start building.

### Option 2: Copy into existing project
Copy **`docs/templates/`** into your project as **`your-project/docs/templates/`** — one folder, everything included.

Then run the bootstrap with your agent:

> "Bootstrap the modular documentation system using `docs/templates/agent/BOOTSTRAP.md` with the current code and documentation"

See [`docs/templates/help/SETUP.md`](docs/templates/help/SETUP.md) for the human guide.

## What's Included

Everything lives under **`docs/templates/`** — workflow scaffolds, human guides, agent setup, and chat-ui pack. Your live project docs (`Master_Index`, `features/`, `_shared/`) stay separate at `docs/` root.

| Path | Purpose |
|------|---------|
| [Master_Index_Template.md](docs/templates/Master_Index_Template.md) | Lean project index — overview, locations, Document Map |
| [Modular_Docs_Workflow.md](docs/templates/Modular_Docs_Workflow.md) | Full agent procedure (Path A/B, Understanding, TODOs) |
| [Feature_Spec_Template.md](docs/templates/Feature_Spec_Template.md) | Durable spec / contract after Understanding is confirmed |
| [Feature_Understanding_Template.md](docs/templates/Feature_Understanding_Template.md) | Agent drafts its interpretation; you review before coding |
| [TODO_Template.md](docs/templates/TODO_Template.md) | Focused task lists with **Current focus** session handoff |
| [Decision_Template.md](docs/templates/Decision_Template.md) | Optional cross-cutting decision records |
| [chat-ui/](docs/templates/chat-ui/) | **Short instructions for Grok/ChatGPT** — no repo workspace; output files to download |
| [agent/Modular_Documentation_Rule.mdc](docs/templates/agent/Modular_Documentation_Rule.mdc) | Cursor rule template — copy to `.cursor/rules/` |
| [agent/Modular_Documentation_Rule.instructions.md](docs/templates/agent/Modular_Documentation_Rule.instructions.md) | Copilot rule template — copy to `.github/instructions/` |
| [help/](docs/templates/help/) | Human guides — [SETUP](docs/templates/help/SETUP.md), [USAGE](docs/templates/help/USAGE.md), [IDEA_CAPTURE_TIPS](docs/templates/help/IDEA_CAPTURE_TIPS.md), [USING_WITH_AGENTS](docs/templates/help/USING_WITH_AGENTS.md) |
| [agent/](docs/templates/agent/) | Agent setup — [BOOTSTRAP](docs/templates/agent/BOOTSTRAP.md), [RULE_INSTALL](docs/templates/agent/RULE_INSTALL.md), [TEMPLATE_SYNC](docs/templates/agent/TEMPLATE_SYNC.md), rule templates (`.mdc`, `.instructions.md`) |

## Core Philosophy

- **Modular over monolithic** — Small, focused files instead of one giant spec.
- **Understanding before implementation** — The agent drafts `-Understanding.md` first so you can see how it interpreted your request; you review and correct, then implementation starts.
- **Spec after confirm** — Durable architecture and **Decisions** graduate into the spec; Understanding keeps intent and acceptance criteria.
- **Shared maturity** — `draft` / `usable` / `stable` on shared components so features know when integration is safe.
- **Visual references matter** — Screenshots and diagrams stay linked for vision models.
- **Shared components live once** — Common work goes in `_shared/` with the same note types as features unless you explicitly except specific files.
- **Index vs workflow split** — `Master_Index.md` is your project map; `Modular_Docs_Workflow.md` is how agents work the system.
- **One folder to copy** — Setup and usage instructions live inside `docs/templates/` (`help/`, `agent/`) so they do not clutter your project's `docs/` root.

## Recommended folder structure

Flat **sibling files** per feature in `docs/features/` and `docs/_shared/`:

```
docs/
├── Master_Index.md
├── _shared/
│   ├── BlockEditor.md
│   ├── BlockEditor-Understanding.md
│   └── BlockEditor-TODO.md
├── features/
│   ├── MainWorkspace.md
│   ├── MainWorkspace-Understanding.md
│   └── MainWorkspace-TODO.md
└── templates/                   ← copy this entire folder from Agentic Doc Templates
    ├── help/                    ← human guides (not live project docs)
    ├── agent/                   ← bootstrap, rule install, sync
    ├── chat-ui/AGENT.md         ← Grok / ChatGPT (attach this only)
    └── Modular_Docs_Workflow.md ← IDE agents (sync, do not copy into Master_Index)
```

Full path table: [`Modular_Docs_Workflow.md` §0](docs/templates/Modular_Docs_Workflow.md#0-naming--file-layout-read-before-creating-files). **Chat without a repo:** [`chat-ui/README.md`](docs/templates/chat-ui/README.md).

## Common Agent Prompts

- "Create modular docs from our conversation using the templates in `docs/templates/`."
- "Add this idea to the docs — draft Understanding + TODO from what I said, then I'll review."
- "Using https://github.com/BrianCLowe/Agentic-Doc-Templates follow chat-ui/AGENT.md — create modular docs from our conversation with save-as paths for each file."
- "Add shared component [Name] as we discussed to the documentation."
- "Convert this design document into modular docs (without the rule installed reference docs/templates)"
- "Bootstrap the documentation system in this project using `docs/templates/agent/BOOTSTRAP.md`."

Full workflows and more example prompts are in [`docs/templates/help/USAGE.md`](docs/templates/help/USAGE.md).

## Contributing

PRs that improve the templates, add new ones, or refine the workflows are very welcome.

If you're using these successfully with a particular agent/tool, feel free to share your experience in Discussions.

## License

[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) — see [LICENSE.md](LICENSE.md).

When reusing or adapting:

> Based on [Agentic Doc Templates](https://github.com/BrianCLowe/Agentic-Doc-Templates) by Brian Lowe, licensed under CC BY 4.0.
