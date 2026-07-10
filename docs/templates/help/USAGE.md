# How to Use These Templates

The templates are not just a folder layout to copy once. They are a **workflow** agents can follow whenever you have ideas, conversations, or existing docs — in the IDE, in chat, or connected to your repo.

Setup first (if you have not already): [`SETUP.md`](SETUP.md) + agent [`../agent/BOOTSTRAP.md`](../agent/BOOTSTRAP.md).

**New to software or describing ideas?** [`IDEA_CAPTURE_TIPS.md`](IDEA_CAPTURE_TIPS.md) — what to think about (UI, flows, scope) so agents build what you mean; you do not need to choose a tech stack yourself.

---

## The basic idea

You give an agent **structure** (`Master_Index_Template.md`, `Feature_Understanding_Template.md`, `TODO_Template.md`, etc.). You describe the idea in chat (or point at a design doc). The **agent drafts** `-Understanding.md` and TODO files so you can see how it interpreted you — then you **review and correct** before implementation. You do not need to write those files yourself.

Same templates, many entry points.

---

## Pattern 1 — Long chat → documentation

**When:** You have been brainstorming in **Grok.com**, ChatGPT, Claude web, or similar — no repo workspace, or you want files to download first.

**What you do:**

1. Attach **`docs/templates/chat-ui/AGENT.md`** only (see [`../chat-ui/README.md`](../chat-ui/README.md)). Optional: `Master_Index_Template.md`, `Feature_Understanding_Template.md`.
2. Ask the agent to output each file with a **Save as:** path — see AGENT.md format.

**Example prompts (chat-only):**

> Follow `AGENT.md`. Turn our conversation into modular docs for [app name]. Each file must start with **Save as:** `docs/...` so I can download them.

> Read `docs/templates/chat-ui/AGENT.md` from Agentic Doc Templates. Draft `-Understanding.md` files first; I'll review before specs and TODOs.

**When you have a repo connector** (Grok → GitHub, Cursor, etc.): connect or upload `docs/templates/`, then use full [`Modular_Docs_Workflow.md`](../Modular_Docs_Workflow.md) or install the agent rule — see [`USING_WITH_AGENTS.md`](USING_WITH_AGENTS.md).

**Example prompts (repo / IDE):**

> Using the templates in `docs/templates/`, create project documentation from our conversation so far.

> Read `docs/templates/Master_Index_Template.md`. Generate `docs/Master_Index.md` and feature docs for [app name]. Do not invent features we did not talk about.

**What you get:** `Master_Index.md`, feature specs, **agent-drafted** Understanding files (scope / UI / what it is *not*) for you to review, TODOs, and `_shared/` entries with the **same note types as features** unless you except specific files.

**Tip:** Ask the agent to **draft Understanding first** and show you the file. That catches “you meant a variant UI, not a new subsystem” before anyone codes. Your job is to correct wrong **identity** assumptions — especially in **What this is NOT** (what the finished feature is not, not a list of unfinished work) — not to write the file from scratch.

---

## Pattern 2 — Idea mid-development → add to docs

**When:** You are already building; a new idea or change comes up in a dev session.

**What you do:** Tell the agent to **update the modular docs**, not only write code.

**Example prompts:**

> New idea: [describe briefly]. Add it to the docs.

> We decided the role editor is a separate UI on the existing text editor, not a new editor. Update `RoleEditor-Understanding.md` — fix "What this is NOT". *(User correction → agent revises the file.)*

**What you get:** Docs stay the living record; the next session (or another tool) reads the same structure instead of re-deriving from chat history.

---

## Pattern 3 — Existing design doc → modular documentation

**When:** You already have a PRD, design doc, Notion export, or long markdown spec.

**What you do:**

1. Put the source doc in the repo (e.g. `docs/reference/Original_Design.md` or a one-off path the agent can read).
2. Ask the agent to **split and map** it into the template structure.

**Example prompts:**

> Read `docs/reference/Original_Design.md`. Convert it into modular documentation per `docs/templates/Master_Index_Template.md`.

> Turn this design doc into modular docs. Keep the original in `reference/`.

**What you get:** Navigable docs sized for agents, with the legacy doc kept for traceability.

---

## Pattern 4 — Greenfield bootstrap in a repo

**When:** New project or an codebase with no modular docs yet.

**What you do:** Copy `docs/templates/`, then agent follows [`../agent/BOOTSTRAP.md`](../agent/BOOTSTRAP.md). Optionally [`../agent/RULE_INSTALL.md`](../agent/RULE_INSTALL.md) for Cursor / Copilot / etc.

**Example prompt:**

> Bootstrap modular docs in this project using `docs/templates/agent/BOOTSTRAP.md`.

See [`SETUP.md`](SETUP.md) for copy-only vs whole-repo details.

---

## Pattern 5 — Template updates from upstream

**When:** This template repo improved (new Understanding rules, layout, workflow, etc.).

**What you do:** Just ask the agent — no manual download required. Point it at [`../agent/TEMPLATE_SYNC.md`](../agent/TEMPLATE_SYNC.md). The agent will:

1. **Download** the latest `docs/templates/` pack from [Agentic-Doc-Templates](https://github.com/BrianCLowe/Agentic-Doc-Templates) and replace your project's template folder.
2. **Update live docs** based on what changed — merge new Master_Index structure, Understanding / spec / TODO template sections, version lines — without wiping your Document Map or feature content.

**Example prompts:**

> Update the doc templates from Agentic Doc Templates and sync our live docs.

> Pull the latest templates from https://github.com/BrianCLowe/Agentic-Doc-Templates into `docs/templates/` and sync our Master_Index.

> The modular doc templates have been updated — download the pack and match our documentation to the updates.

---

## Works with many agents

| How the agent sees templates | Works for |
|------------------------------|-----------|
| `docs/templates/` in your project | Cursor, Copilot, Claude Code, Cline, Continue, etc. |
| Uploaded files in chat | Grok, ChatGPT, Claude web, … |
| **Repo / folder connector** | Grok connectors, GitHub in IDE, clone/submodule |
| This repo URL | Any agent that can fetch or browse the repo |

Tool-specific rule install paths: [`USING_WITH_AGENTS.md`](USING_WITH_AGENTS.md).

---

## Short prompt cheat sheet

| Goal | Say something like |
|------|-------------------|
| Chat → docs | *Create modular docs from our conversation using the templates in `docs/templates/`.* |
| New idea | *Add [idea] to the docs — draft Understanding + TODO; I'll review.* |
| Fix agent misunderstanding | *Update [Feature]-Understanding.md from my correction — especially What this is NOT.* |
| UI reference screenshot | *Save to `docs/features/assets/`, add Visual references in Understanding with similar vs different.* |
| Vague idea | *Interview me using IDEA_CAPTURE_TIPS.md, then **draft** [Feature]-Understanding.md for my review.* |
| Design doc → modular | *Convert `[path]` to modular docs per Master_Index_Template; keep original in reference.* |
| First-time setup | *Bootstrap modular docs using `docs/templates/agent/BOOTSTRAP.md`.* |
| Install agent rule | *Follow `docs/templates/agent/RULE_INSTALL.md` for [Cursor / Copilot / …].* |
| Pull template improvements | *Update the doc templates from Agentic Doc Templates and sync our live docs.* |

---

## What good output looks like

- **`docs/Master_Index.md`** — entry point + Document Map (not a dump of everything).
- **`docs/features/FeatureName-Understanding.md`** — agent's draft of how it interpreted your request; you skim, correct, confirm.
- **`docs/features/FeatureName.md`** — durable spec after confirm (Decisions, architecture).
- **`docs/features/FeatureName-TODO.md`** — next actions + **Current focus** for session handoff.
- **`docs/_shared/Component.md`** — shared spec with **Maturity** (`draft` | `usable` | `stable`)
- **`docs/_shared/Component-Understanding.md`** — same review loop as feature Understanding
- **`docs/_shared/Component-TODO.md`** — foundation work (not duplicated in feature TODOs)
- **`docs/_shared/Component-InEditor-TODO.md`** / **`Component-Asset-TODO.md`** — when applicable; record omissions in Master_Index Section 3.0
- **`docs/decisions/`** — optional cross-cutting decision files
- **`docs/templates/`** — upstream template pack (workflow, scaffolds, `help/`, `agent/`, `chat-ui/`) — not live project content

You do not need every file on day one. Start with Master_Index + one feature; grow as ideas arrive — from chat, design docs, or the middle of a dev session.
