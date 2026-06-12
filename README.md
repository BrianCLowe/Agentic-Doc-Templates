# Agentic Doc Templates

Documentation templates for working with agentic AI coding tools — a central place to update and share templates that work well with AI-assisted development.

**GitHub:** [BrianCLowe/Agentic-Doc-Templates](https://github.com/BrianCLowe/Agentic-Doc-Templates)

## Adding to your project

**Recommended:** copy only **`docs/templates/`** into your project as `your-project/docs/templates/`. You do not need this repo's root `README.md` or `LICENSE.md` in your project root.

| Method | What to do |
|--------|------------|
| **Copy templates folder** (best) | Copy `docs/templates/` → your `docs/templates/` |
| **Whole repo copied/cloned** | Ask your agent to follow [`docs/templates/BOOTSTRAP.md`](docs/templates/BOOTSTRAP.md) — it moves upstream README/LICENSE to `docs/templates/upstream/` and creates live docs |
| **Agent bootstrap** | *"Bootstrap modular docs"* + [`BOOTSTRAP.md`](docs/templates/BOOTSTRAP.md) |

Human guide in your project after copy: [`docs/templates/SETUP.md`](docs/templates/SETUP.md).

## How to use (versatile workflows)

Templates are not only for one-time setup. Use them whenever you turn **conversations**, **ideas**, or **design docs** into structured project documentation — in the IDE or in chat (Grok, Claude, etc.), with uploads or a **repo connector**.

**Full guide:** [`docs/templates/USAGE.md`](docs/templates/USAGE.md) — chat → docs, mid-dev ideas, design-doc conversion, bootstrap, template sync, example prompts.

**Describing an idea (especially if you are new to dev):** [`docs/templates/IDEA_CAPTURE_TIPS.md`](docs/templates/IDEA_CAPTURE_TIPS.md) — UI, interactions, flows, and scope in plain language; helps agents propose a stack when you do not know what you need technically.

Quick examples:

- *"Create modular docs from our conversation using the templates in `docs/templates/`."*
- *"Add this idea to the docs — Understanding + TODO + update Master_Index."*
- *"Convert `docs/reference/Design.md` to modular docs per Master_Index_Template."*
- *"Save this screenshot to `docs/features/assets/`, link it in Understanding — similar: X, different: Y."*

> **This repo only:** `README.md` and `LICENSE.md` stay at the **repository root** so GitHub displays them. Consumer projects keep those under `docs/templates/upstream/` instead.

## What's in `docs/templates/`

| File | Purpose |
|------|---------|
| [Master_Index_Template.md](docs/templates/Master_Index_Template.md) | Canonical `docs/Master_Index.md` structure |
| [Feature_Understanding_Template.md](docs/templates/Feature_Understanding_Template.md) | Agent model of user intent before implementation |
| [TODO_Template.md](docs/templates/TODO_Template.md) | Per-feature task lists |
| [BOOTSTRAP.md](docs/templates/BOOTSTRAP.md) | Agent: initialize docs + relocate upstream root files |
| [SETUP.md](docs/templates/SETUP.md) | Human: add templates to a project |
| [USAGE.md](docs/templates/USAGE.md) | Human: workflows — chat → docs, ideas, design-doc conversion |
| [IDEA_CAPTURE_TIPS.md](docs/templates/IDEA_CAPTURE_TIPS.md) | Human: describe your idea — UI, flows, scope; reduces agent drift |
| [TEMPLATE_SYNC.md](docs/templates/TEMPLATE_SYNC.md) | Agent: merge template updates into live docs |
| [RULE_INSTALL.md](docs/templates/RULE_INSTALL.md) | Agent: install rules per tool (asks once) |
| [USING_WITH_AGENTS.md](docs/templates/USING_WITH_AGENTS.md) | Copilot, Cursor, Claude Code, etc. |
| Rule `.mdc` / `.instructions.md` | Drop-in agent rules |

## Core idea

Modular docs: lightweight `Master_Index.md` + small feature files + `-Understanding.md` (scope, UI intent, **visual references**) + `-TODO.md` task lists. Shared foundation work lives in `_shared/Component-TODO.md`, not in consumer feature TODOs. Reference screenshots go in `docs/features/assets/` and stay linked for vision-capable agents across sessions.

## License

[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) — see [LICENSE.md](LICENSE.md).

Attribution when reusing:

> Based on [Agentic Doc Templates](https://github.com/BrianCLowe/Agentic-Doc-Templates) by Brian Lowe, licensed under CC BY 4.0.
