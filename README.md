# Agentic Doc Templates

Documentation templates for working with agentic AI coding tools. Copy them into your projects, adapt them to your workflow, and keep a single source of truth here for updates and sharing.

## Core idea

Large documentation sets are split into a lightweight index plus many small, purpose-built files. That keeps agent context windows manageable and makes navigation trivial. Each feature gets a spec, a **Understanding** file (agent model of user intent — scope, UI, what it is *not*), and focused `-TODO.md` task lists.

## Templates

| Template | Description |
|----------|-------------|
| [Master Index Template](docs/templates/Master_Index_Template.md) | Canonical structure for `docs/Master_Index.md` — agent-focused reference |
| [Feature Understanding Template](docs/templates/Feature_Understanding_Template.md) | Agent model of user intent — scope, UI, relationships; review before implementation |
| [Template Sync](docs/templates/TEMPLATE_SYNC.md) | Agent instructions for migrating live docs when templates improve |
| [Rule Install](docs/templates/RULE_INSTALL.md) | Agent instructions for installing the rule — asks user first, supports multiple tools |
| [TODO Template](docs/templates/TODO_Template.md) | Per-feature task lists for agent-driven development |
| [Modular Documentation Rule](docs/templates/Modular_Documentation_Rule.mdc) | Cursor rule — copy to `.cursor/rules/` |
| [Modular Documentation Rule (Copilot)](docs/templates/Modular_Documentation_Rule.instructions.md) | GitHub Copilot instructions — copy to `.github/instructions/` |

## Recommended folder structure

Copy the `docs/templates/` folder into your project (or symlink / submodule this repo). Keep templates pristine — project content lives elsewhere.

```
docs/
├── Master_Index.md            ← Live index (customized from Master_Index_Template.md)
├── rule-install-status.yaml   ← Per-tool rule install decisions (created by agent; optional until first ask)
├── _shared/                   ← Reusable components + foundation TODOs (`Component-TODO.md`)
│   ├── BlockEditor.md
│   ├── BlockEditor-TODO.md
│   └── ...
├── features/                  ← One folder or flat files per feature/module
│   ├── FeatureName.md
│   ├── FeatureName-Understanding.md
│   ├── FeatureName-TODO.md
│   └── ...
├── reference/                 ← Legacy specs, deep-dives, external links
└── templates/                 ← Canonical templates — do not fill with project content
    ├── Master_Index_Template.md
    ├── Feature_Understanding_Template.md
    ├── TEMPLATE_SYNC.md
    ├── RULE_INSTALL.md
    ├── rule-install-status.example.yaml
    ├── TODO_Template.md
    ├── Modular_Documentation_Rule.mdc
    └── Modular_Documentation_Rule.instructions.md
```

### Naming conventions

- Kebab-case for files and folders
- Feature spec: `FeatureName.md`
- Understanding (intent / scope / UI): `FeatureName-Understanding.md`
- TODO files: `FeatureName-TODO.md`, `FeatureName-InEditor-TODO.md`, `FeatureName-Asset-TODO.md`
- Shared components: `docs/_shared/ComponentName.md` + `_shared/ComponentName-TODO.md` for **foundation work** (not in consumer feature TODOs)
- Project-level: `Project-InEditor-TODO.md`, `Project-Asset-TODO.md`
- Game projects: rename In-Editor TODOs to engine-specific names (`FeatureName-UE-TODO.md`, etc.) — see the template Section 6

## Bootstrap a new project

1. Create the `docs/` folder structure above.
2. Copy [`Master_Index_Template.md`](docs/templates/Master_Index_Template.md) → `docs/Master_Index.md`. Replace bracketed placeholders and fill in the Document Map.
3. Copy [`TODO_Template.md`](docs/templates/TODO_Template.md) into `docs/templates/` (if not already there).
4. Copy the full `docs/templates/` folder from this repo so templates stay available for future syncs.
5. **Rule (optional, ask first):** When ready, ask your agent to follow [`RULE_INSTALL.md`](docs/templates/RULE_INSTALL.md). It records your answer per tool in `docs/rule-install-status.yaml` so you are not asked again for tools you installed or declined. See [Using With AI Agents](docs/USING_WITH_AGENTS.md).
6. Create your first feature spec + **Understanding** + TODO file(s) and add rows to the Document Map.
7. Skip a central `STATUS.md` — TODO files are the status tracker.

## Updating when templates improve

Templates are the **schema**; `Master_Index.md` and feature docs are the **instance**.

When this repo (or your copy of `docs/templates/`) gets improvements:

1. Pull or copy the updated template files into your project's `docs/templates/`.
2. Point your agent at [`TEMPLATE_SYNC.md`](docs/templates/TEMPLATE_SYNC.md) and ask it to merge structural changes into your live `docs/Master_Index.md`.
3. The agent should preserve your overview, Document Map, and custom sections while adopting new workflow rules and sections from the template.

Check `<!-- template-version: X.Y -->` in the template against the **Template version** line in your live Master Index to see if you're behind.

## Using with AI agents

The workflow is the same across tools; only the **file location** for rules changes. See **[Using With AI Agents](docs/USING_WITH_AGENTS.md)** for Copilot, Cursor, Claude Code, Continue, Cline, Grok Build, and others.

## License

These templates are released under the [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/) (CC BY 4.0).

You are free to share and adapt the material for any purpose, including commercially, as long as you give appropriate credit. When you reuse or modify these templates, include attribution such as:

> Based on [Agentic Doc Templates](https://github.com/BrianCLowe/Agentic-Doc-Templates) by Brian Lowe, licensed under CC BY 4.0.

See [LICENSE.md](LICENSE.md) for the full license text.
