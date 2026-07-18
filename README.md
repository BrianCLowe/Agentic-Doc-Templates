# Agentic Doc Templates

> **Documentation templates for agentic AI coding tools.**  
> Keep agents aligned with your intent across conversations, features, and long-running projects.

[![License: CC BY 4.0](https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)
![Pack](https://img.shields.io/badge/Pack-2.4-blue)
![Built for](https://img.shields.io/badge/Built%20for-Cursor%20%7C%20Copilot%20%7C%20Claude%20Code%20%7C%20Grok-5865F2)

---

## How it works

AI coding agents drift when intent lives only in chat. This pack gives them a small, consistent `docs/` layout:

1. You describe the idea (chat, design doc, or mid-build correction).
2. The **agent drafts** `-Understanding.md` — how it interpreted you.
3. **You review and correct** (especially identity: what it is / is *not*).
4. After you confirm, work continues from TODOs and specs; session handoff uses **Current focus**.

Short asks are enough: *bootstrap*, *draft Understanding for X*, *update the doc templates*. The agent routes to the matching playbook inside `docs/templates/`.

---

## Get started

### Existing project *(recommended)*

Copy **`docs/templates/`** into your repo as **`your-project/docs/templates/`**, then ask your agent:

> Bootstrap modular docs using `docs/templates/agent/BOOTSTRAP.md`.

Human guide: [`docs/templates/help/SETUP.md`](docs/templates/help/SETUP.md).

### New repository from this template

1. Click **Use this template** (green button).
2. Ask your agent to bootstrap (it will create the live `docs/` layout and auto-move this pack’s root README/LICENSE/CONTRIBUTING into `docs/templates/agent/upstream/` when those files are clearly from Agentic Doc Templates).
3. Discuss the app (or drop design docs / chat exports into `docs/reference/`) and review draft Understandings before coding.

Prefer **copy `docs/templates/` only** into an existing app so this repo’s root files never collide with yours.

### Chat UI first *(no repo yet)*

Attach only [`docs/templates/chat-ui/AGENT.md`](docs/templates/chat-ui/AGENT.md). Save the exported files into your project later; keep the full brainstorm thread (ideally under `docs/reference/`). See [`docs/templates/chat-ui/README.md`](docs/templates/chat-ui/README.md).

### Cursor plugin note

**Compound Engineering** and **Superpowers** often override the modular-docs Cursor rule. Disable them (or their always-on skills) for this workspace if you rely on this pack. Details: [`USING_WITH_AGENTS.md`](docs/templates/help/USING_WITH_AGENTS.md#cursor).

---

## Stay current

Once your project has the sync playbook (`docs/templates/agent/TEMPLATE_SYNC.md`, added in pack **1.2**), you do not need to copy files by hand when this repo improves. Ask:

> Update the doc templates from Agentic Doc Templates and sync our live docs.

The agent overwrites the pack (ZIP/copy), then follows [`docs/templates/CHANGELOG.md`](docs/templates/CHANGELOG.md) for what to change in live docs — usually versions and Master Index, not a rewrite of every feature file.

**One-time catch-up:** If your `docs/templates/` is from **before 1.2** (no `agent/TEMPLATE_SYNC.md`), copy or replace that folder from this repo once — or tell the agent to — so the sync instructions exist locally. After that, the ask above is enough.

Version-only ping (optional weekly rule): *Check for template updates.* — [`TEMPLATE_UPDATE_CHECK.md`](docs/templates/agent/TEMPLATE_UPDATE_CHECK.md).

---

## What’s in the pack

Everything ships under **`docs/templates/`**. Live project docs stay at `docs/` root.

| Area | Role |
|------|------|
| **Scaffolds** | Master Index, Understanding, Spec, TODO, Tooling, Human-TODO, Decision templates + [`Modular_Docs_Workflow.md`](docs/templates/Modular_Docs_Workflow.md) |
| **[`help/`](docs/templates/help/)** | Human guides — [SETUP](docs/templates/help/SETUP.md), [USAGE](docs/templates/help/USAGE.md), [IDEA_CAPTURE_TIPS](docs/templates/help/IDEA_CAPTURE_TIPS.md), [USING_WITH_AGENTS](docs/templates/help/USING_WITH_AGENTS.md) |
| **[`agent/`](docs/templates/agent/)** | Bootstrap, rule install, template sync, update check, Cursor/Copilot rule templates |
| **[`chat-ui/`](docs/templates/chat-ui/)** | Short instructions for Grok/ChatGPT (no workspace) |
| **[`VERSION`](docs/templates/VERSION)** / **[`CHANGELOG.md`](docs/templates/CHANGELOG.md)** | Cheap upstream compare + sync scope after a pack refresh |

---

## Live docs layout

After bootstrap, a typical project looks like:

```
docs/
├── Master_Index.md              ← project map (you maintain)
├── Tooling.md                   ← machine tools (not package deps)
├── Human-TODO.md                ← keys, portals, accounts (human only)
├── reference/                   ← design docs, chat exports, PRDs, legacy specs
│   └── visuals/                 ← optional inspiration screenshots
├── _shared/                     ← reusable components (same note types as features)
│   └── ComponentName.md (+ Understanding, TODO)
├── features/
│   └── FeatureName.md (+ Understanding, TODO)
├── decisions/                   ← optional cross-cutting decisions
└── templates/                   ← this pack (overwrite on sync; not live content)
```

Flat sibling files per feature/shared component. Naming: [`Modular_Docs_Workflow.md` §0](docs/templates/Modular_Docs_Workflow.md#0-naming--file-layout-read-before-creating-files).

---

## Ideas that guide the pack

- **Simplicity** — Short user asks; agents follow one playbook.
- **Understanding before code** — Agent drafts; you confirm identity and scope.
- **Modular map** — Small files + Document Map; not one giant spec.
- **Tight scope** — Paved path for the current ask; no “just in case” audits.
- **One folder to copy** — `docs/templates/` holds setup, workflow, and rules so your `docs/` root stays yours.

Deeper day-to-day patterns: [`docs/templates/help/USAGE.md`](docs/templates/help/USAGE.md).

---

## Example prompts

- *Bootstrap modular docs using `docs/templates/agent/BOOTSTRAP.md`.*
- *Draft Understanding for [feature] from what I said — I’ll review.*
- *Update the doc templates from Agentic Doc Templates and sync our live docs.*
- *Check for template updates.*
- *Follow `chat-ui/AGENT.md` — turn our conversation into modular docs with Save-as paths.*

More: [`USAGE.md`](docs/templates/help/USAGE.md).

---

## Contributing

PRs that improve the templates or workflows are welcome. Prefer focused changes; when bumping [`VERSION`](docs/templates/VERSION), update [`CHANGELOG.md`](docs/templates/CHANGELOG.md) in the same commit.

**Feedback:** [Open an issue](https://github.com/BrianCLowe/Agentic-Doc-Templates/issues/new/choose). Discussions for open-ended questions. See [`CONTRIBUTING.md`](CONTRIBUTING.md).

---

## License

[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) — see [LICENSE.md](LICENSE.md).

When reusing or adapting:

> Based on [Agentic Doc Templates](https://github.com/BrianCLowe/Agentic-Doc-Templates) by Brian Lowe, licensed under CC BY 4.0.
