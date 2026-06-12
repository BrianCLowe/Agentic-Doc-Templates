# How to Use These Templates

The templates are not just a folder layout to copy once. They are a **workflow** agents can follow whenever you have ideas, conversations, or existing docs — in the IDE, in chat, or connected to your repo.

Setup first (if you have not already): [`SETUP.md`](SETUP.md) + agent [`BOOTSTRAP.md`](BOOTSTRAP.md).

**New to software or describing ideas?** [`IDEA_CAPTURE_TIPS.md`](IDEA_CAPTURE_TIPS.md) — what to think about (UI, flows, scope) so agents build what you mean; you do not need to choose a tech stack yourself.

---

## The basic idea

You give an agent **structure** (`Master_Index_Template.md`, `Feature_Understanding_Template.md`, `TODO_Template.md`, etc.). The agent turns **your input** (chat, design doc, half-formed idea) into small linked files under `docs/` instead of one giant doc or nothing at all.

Same templates, many entry points.

---

## Pattern 1 — Long chat → documentation

**When:** You have been brainstorming in Grok, Claude, Cursor, or similar — app ideas, features, architecture — and the conversation is the source of truth.

**What you do:**

1. Make sure the agent can see the templates — upload them, copy into the project, or **connect the repo** (e.g. Grok connectors pointing at [Agentic-Doc-Templates](https://github.com/BrianCLowe/Agentic-Doc-Templates) or your project’s `docs/templates/`).
2. Ask the agent to **turn the conversation into modular docs** that follow the templates.

**Example prompts:**

> Using the Agentic Doc Templates structure, create project documentation from our conversation so far. Follow `Master_Index_Template.md`, add a `-Understanding.md` per feature, and initial `-TODO.md` files. Put shared concepts in `_shared/` where appropriate.

> Read `docs/templates/Master_Index_Template.md` and the other templates in this repo. Generate `docs/Master_Index.md` and feature docs that capture what we discussed about [app name]. Do not invent features we did not talk about.

**What you get:** `Master_Index.md`, feature specs, Understanding files (scope / UI / what it is *not*), TODOs, and `_shared/` entries for reusable pieces — ready to refine in the repo.

**Tip:** Ask for Understanding files explicitly. They catch “you meant a variant UI, not a new subsystem” before anyone codes. Point new collaborators at [`IDEA_CAPTURE_TIPS.md`](IDEA_CAPTURE_TIPS.md) if they are unsure what details to provide.

---

## Pattern 2 — Idea mid-development → add to docs

**When:** You are already building; a new idea or change comes up in a dev session.

**What you do:** Tell the agent to **update the modular docs**, not only write code.

**Example prompts:**

> New idea: [describe briefly]. Add it to the docs — new feature or extend [ExistingFeature]. Update Master_Index Document Map, create Understanding + TODO, link any `_shared/` foundation work.

> We decided the role editor is a separate UI on the existing text editor, not a new editor. Update `RoleEditor-Understanding.md` — fix "What this is NOT" and link to `_shared/BlockEditor.md`.

**What you get:** Docs stay the living record; the next session (or another tool) reads the same structure instead of re-deriving from chat history.

---

## Pattern 3 — Existing design doc → modular documentation

**When:** You already have a PRD, design doc, Notion export, or long markdown spec.

**What you do:**

1. Put the source doc in the repo (e.g. `docs/reference/Original_Design.md` or a one-off path the agent can read).
2. Ask the agent to **split and map** it into the template structure.

**Example prompts:**

> Read `docs/reference/Original_Design.md`. Convert it into modular documentation per `docs/templates/Master_Index_Template.md`. Preserve detail by splitting into feature files; do not leave one huge file. Add Understanding + TODO per feature. Put reusable architecture in `_shared/`.

> Turn this design doc into modular docs. Keep the original in `reference/`; link to it from Master_Index Section 3.4.

**What you get:** Navigable docs sized for agents, with the legacy doc kept for traceability.

---

## Pattern 4 — Greenfield bootstrap in a repo

**When:** New project or an codebase with no modular docs yet.

**What you do:** Copy `docs/templates/`, then agent follows [`BOOTSTRAP.md`](BOOTSTRAP.md). Optionally [`RULE_INSTALL.md`](RULE_INSTALL.md) for Cursor / Copilot / etc.

**Example prompt:**

> Bootstrap modular docs in this project using `docs/templates/BOOTSTRAP.md`.

See [`SETUP.md`](SETUP.md) for copy-only vs whole-repo details.

---

## Pattern 5 — Template updates from upstream

**When:** This template repo improved (new Understanding workflow, `_shared/` TODO rules, etc.).

**What you do:** Refresh files in `docs/templates/`, then agent follows [`TEMPLATE_SYNC.md`](TEMPLATE_SYNC.md).

**Example prompt:**

> Sync our `docs/Master_Index.md` to the latest `Master_Index_Template.md` using TEMPLATE_SYNC.md. Preserve our Document Map and overview.

---

## Works with many agents

| How the agent sees templates | Works for |
|------------------------------|-----------|
| Files in your project `docs/templates/` | Cursor, Copilot, Claude Code, Cline, Continue, etc. |
| Uploaded files in chat | Grok, ChatGPT, Claude web, … |
| **Repo / folder connector** | Grok connectors, GitHub in IDE, clone/submodule |
| This repo URL | Any agent that can fetch or browse the repo |

Tool-specific rule install paths: [`USING_WITH_AGENTS.md`](USING_WITH_AGENTS.md).

---

## Short prompt cheat sheet

| Goal | Say something like |
|------|-------------------|
| Chat → docs | *Create modular docs from our conversation using the templates in `docs/templates/`.* |
| New idea | *Add [idea] to the docs — Understanding + TODO + Master_Index map.* |
| Fix agent misunderstanding | *Update [Feature]-Understanding.md — especially What this is NOT.* |
| UI reference screenshot | *Save to `docs/features/assets/`, add Visual references in Understanding with similar vs different.* |
| Vague idea | *Interview me using IDEA_CAPTURE_TIPS.md, then fill [Feature]-Understanding.md.* |
| Design doc → modular | *Convert `[path]` to modular docs per Master_Index_Template; keep original in reference.* |
| First-time setup | *Bootstrap modular docs using BOOTSTRAP.md.* |
| Install agent rule | *Follow RULE_INSTALL.md for [Cursor / Copilot / …].* |
| Pull template improvements | *Sync Master_Index using TEMPLATE_SYNC.md.* |

---

## What good output looks like

- **`docs/Master_Index.md`** — entry point + Document Map (not a dump of everything).
- **`docs/features/FeatureName-Understanding.md`** — your intent in agent-readable form; you skim and correct.
- **`docs/features/FeatureName-TODO.md`** — next actions (feature work).
- **`docs/_shared/Component-TODO.md`** — foundation work shared by multiple features (not duplicated in feature TODOs).
- **`docs/templates/`** — unchanged canonical copies for future syncs.

You do not need every file on day one. Start with Master_Index + one feature; grow as ideas arrive — from chat, design docs, or the middle of a dev session.
