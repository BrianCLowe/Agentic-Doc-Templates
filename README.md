# Agentic Doc Templates

> **Documentation templates for agentic AI coding tools.**
> Keep AI agents aligned with your intent across conversations, features, and long-running projects.

[![License: CC BY 4.0](https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)
![Template](https://img.shields.io/badge/Template-Ready-blue)
![Built for](https://img.shields.io/badge/Built%20for-Cursor%20%7C%20Grok%20Build%20%7C%20Claude%20Code-5865F2)

**Quick start:** Click the green **"Use this template"** button at the top of this page to instantly create a new repository with the full `docs/templates/` structure.

---

## Why these templates exist

AI coding agents are powerful but can drift from your original intent over long sessions. These templates give agents a consistent structure: the **agent writes** Understanding and TODO files from your conversation; **you review and correct** them before implementation — you do not need to author those files yourself.

The goal: lightweight documentation that stays in sync with the code and is easy for both people and vision-capable agents to use.

## Quick Start

### Option 1: Use as Template (Recommended)
1. Click **"Use this template"** (green button at the top)
2. Create a new repository in your account
3. Copy or move `docs/templates/` into your project's `docs/` folder

### Option 2: Copy into existing project
Copy the `docs/templates/` folder into your project as `your-project/docs/templates/`.

Then run the bootstrap with your agent:

> "Bootstrap the modular documentation system using the templates in `docs/templates/BOOTSTRAP.md`"

See [`docs/templates/SETUP.md`](docs/templates/SETUP.md) for the human guide.

## What's Included

| File | Purpose |
|------|---------|
| [Master_Index_Template.md](docs/templates/Master_Index_Template.md) | Core index that ties everything together |
| [Feature_Spec_Template.md](docs/templates/Feature_Spec_Template.md) | Durable spec / contract after Understanding is confirmed |
| [Feature_Understanding_Template.md](docs/templates/Feature_Understanding_Template.md) | Agent drafts its interpretation of your request; you review and correct before coding |
| [TODO_Template.md](docs/templates/TODO_Template.md) | Focused task lists with **Current focus** session handoff |
| [Decision_Template.md](docs/templates/Decision_Template.md) | Optional cross-cutting decision records |
| [BOOTSTRAP.md](docs/templates/BOOTSTRAP.md) | Agent instructions to initialize the system in a new project |
| [SETUP.md](docs/templates/SETUP.md) | Human instructions for adding templates to a project |
| [USAGE.md](docs/templates/USAGE.md) | Workflows for turning conversations, ideas, and design docs into structured documentation |
| [IDEA_CAPTURE_TIPS.md](docs/templates/IDEA_CAPTURE_TIPS.md) | How to describe ideas clearly so agents propose better solutions |
| [TEMPLATE_SYNC.md](docs/templates/TEMPLATE_SYNC.md) | Keep your live docs updated when these templates improve |
| [RULE_INSTALL.md](docs/templates/RULE_INSTALL.md) | Install agent rules for your specific tool |
| [USING_WITH_AGENTS.md](docs/templates/USING_WITH_AGENTS.md) | Guidance for Claude Code, Cursor, Copilot, etc. |
| `.mdc` / `.instructions.md` files | Ready-to-drop agent rule files |

## Core Philosophy

- **Modular over monolithic** — Small, focused files instead of one giant spec.
- **Understanding before implementation** — The agent drafts `-Understanding.md` first so you can see how it interpreted your request; you review and correct, then implementation starts.
- **Spec after confirm** — Durable architecture and **Decisions** graduate into the spec; Understanding keeps intent and acceptance criteria.
- **Shared maturity** — `draft` / `usable` / `stable` on shared components so features know when integration is safe.
- **Visual references matter** — Screenshots and diagrams stay linked for vision models.
- **Shared components live once** — Common work goes in `_shared/` with the same note types as features (Understanding, TODOs, etc.) unless you explicitly except specific files.
- **Easy for both humans and agents** — Clear structure that works in chat and in the IDE.

## Common Agent Prompts

- "Create modular docs from our conversation using the templates in `docs/templates/`."
- "Add this idea to the docs — draft Understanding + TODO from what I said, then I'll review."
- "Using https://github.com/BrianCLowe/Agentic-Doc-Templates please create modular documentation for the app we've been discussing in this chat" Works in chat interfaces like grok.com
- "Add shared component [Name] to `_shared/` — full note set (spec, Understanding, TODOs) unless I say otherwise."
- "Convert this design document into modular docs following Master_Index_Template."
- "Bootstrap the documentation system in this project."

Full workflows and more example prompts are in [`docs/templates/USAGE.md`](docs/templates/USAGE.md).

## Contributing

PRs that improve the templates, add new ones, or refine the workflows are very welcome.

If you're using these successfully with a particular agent/tool, feel free to share your experience in Discussions.

## License

[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) — see [LICENSE.md](LICENSE.md).

When reusing or adapting:

> Based on [Agentic Doc Templates](https://github.com/BrianCLowe/Agentic-Doc-Templates) by Brian Lowe, licensed under CC BY 4.0.