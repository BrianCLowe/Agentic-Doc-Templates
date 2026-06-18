# Setting Up Modular Docs in Your Project

Human guide for adding [Agentic Doc Templates](https://github.com/BrianCLowe/Agentic-Doc-Templates) to an existing codebase. For agent-driven setup, point your agent at [`BOOTSTRAP.md`](BOOTSTRAP.md).

## Recommended: copy one folder

Copy **`docs/templates/`** from this repo into your project as **`your-project/docs/templates/`**.

You do **not** need the repo root `README.md` or `LICENSE.md` in your project root. Keep attribution via `docs/templates/upstream/` (see below) or a line in your own README.

Also copy [`USING_WITH_AGENTS.md`](USING_WITH_AGENTS.md) — it lives inside `docs/templates/` in current versions.

## Other ways to add templates

| Method | Pros | Notes |
|--------|------|--------|
| **Copy `docs/templates/` only** | Clean project root | Recommended |
| **Git submodule** | Easy upstream updates | Submodule path is often awkward; copy or sparse-checkout `docs/templates/` |
| **Clone whole repo into project** | Simple first copy | Root README/LICENSE collide with yours — use agent [`BOOTSTRAP.md`](BOOTSTRAP.md) to move them to `docs/templates/upstream/` |

## After templates are in place

1. Ask your agent to follow **`BOOTSTRAP.md`** — creates `docs/Master_Index.md`, folders, and relocates upstream root files if needed.
2. Fill in project overview and Document Map in `Master_Index.md`.
3. Add first feature under `docs/features/` (agent drafts spec + Understanding + TODO; you review). Shared components under `docs/_shared/` get the **same note types** unless you explicitly except specific files.
4. Optionally run **`RULE_INSTALL.md`** for your agent tool(s).

**Day-to-day use** (chat → docs, ideas mid-dev, converting design docs): see **[`USAGE.md`](USAGE.md)**.

**Brainstorming in Grok/ChatGPT before you have a repo?** Attach only [`chat-ui/AGENT.md`](chat-ui/AGENT.md) — see [`chat-ui/README.md`](chat-ui/README.md). Copy full templates when you create the project.

**Describing ideas** (UI, flows, scope — especially if you are new to software): see **[`IDEA_CAPTURE_TIPS.md`](IDEA_CAPTURE_TIPS.md)**.

## Folder layout in your project

```
docs/
├── Master_Index.md
├── rule-install-status.yaml     ← created when installing agent rules
├── _shared/
│   └── assets/
├── decisions/                 ← optional cross-cutting decisions
├── features/
│   └── assets/                  ← reference screenshots (linked from Understanding)
├── reference/
│   └── visuals/                 ← optional inspiration before a feature exists
└── templates/
    ├── Master_Index_Template.md
    ├── BOOTSTRAP.md
    ├── SETUP.md                 ← this file
    ├── USAGE.md                 ← how to use templates (chat, ideas, design docs)
    ├── upstream/                ← README + LICENSE moved here if whole repo was copied
    │   ├── README.md
    │   └── LICENSE.md
    └── …
```

## Naming and workflow

See [Recommended folder structure](#recommended-folder-structure) above and [`Modular_Docs_Workflow.md` §0](Modular_Docs_Workflow.md#0-naming--file-layout-read-before-creating-files) for file layout, Understanding workflow, shared foundation TODOs, and template sync.

## License

Templates are [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). Full text: [`upstream/LICENSE.md`](upstream/LICENSE.md) after bootstrap, or [LICENSE.md](https://github.com/BrianCLowe/Agentic-Doc-Templates/blob/main/LICENSE.md) in the GitHub repo.

Attribution example:

> Based on [Agentic Doc Templates](https://github.com/BrianCLowe/Agentic-Doc-Templates) by Brian Lowe, licensed under CC BY 4.0.
