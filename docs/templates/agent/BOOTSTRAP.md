# Bootstrap Modular Docs — Agent Instructions

> Use when the user asks to set up, bootstrap, or initialize modular documentation in their project. Follow this **before** [`RULE_INSTALL.md`](RULE_INSTALL.md) (rules come after doc structure exists).

## Goal

Create the live `docs/` layout (Master_Index, feature folders, template pack in place) without leaving **this repo's** root `README.md`, `LICENSE.md`, or `CONTRIBUTING.md` in the project root when the user copied the whole template repository.

## Step 0 — How templates arrived (pick a path)

| Situation | Action |
|-----------|--------|
| `docs/templates/` copied (full pack with `help/`, `agent/`, scaffolds) | Skip Step 1 (relocate) unless whole repo. Verify subfolders are complete. |
| `docs/help/` and/or `docs/agent/` at `docs/` root (older layout) | Run **Step 0b — migrate layout**, then continue. |
| Flat files only in `docs/templates/` (oldest layout) | Run **Step 0b — migrate layout**, then continue. |
| Whole repo cloned/copied into the project | Do Step 1 after user confirms. |
| Submodule of [Agentic-Doc-Templates](https://github.com/BrianCLowe/Agentic-Doc-Templates) | Prefer copy of `docs/templates/`; optional Step 1 for root files if submodule is at repo root. |

## Step 0b — Migrate older layouts (if needed)

Reorganize without losing content. Target: **everything meta** lives under `docs/templates/`; live project docs stay at `docs/` root only.

| From (old) | To (current) |
|------------|--------------|
| `docs/help/` (entire folder at docs root) | `docs/templates/help/` |
| `docs/agent/` (entire folder at docs root) | `docs/templates/agent/` |
| `docs/templates/SETUP.md`, `USAGE.md`, `IDEA_CAPTURE_TIPS.md`, `USING_WITH_AGENTS.md` (flat in templates) | `docs/templates/help/` |
| `docs/templates/BOOTSTRAP.md`, `RULE_INSTALL.md`, `TEMPLATE_SYNC.md`, `rule-install-status.example.yaml` (flat in templates) | `docs/templates/agent/` |
| `docs/templates/upstream/` | `docs/templates/agent/upstream/` |
| `docs/templates/Modular_Documentation_Rule.mdc`, `Modular_Documentation_Rule.instructions.md` (flat in templates) | `docs/templates/agent/` |
| `docs/USING_WITH_AGENTS.md` (at `docs/` root) | `docs/templates/help/USING_WITH_AGENTS.md` |

Fix internal links after moving. **Keep at `docs/templates/` root:** `Master_Index_Template.md`, `Modular_Docs_Workflow.md`, `chat-ui/`, `Feature_*_Template.md`, `TODO_Template.md`, `Decision_Template.md`. **Keep in `docs/templates/agent/`:** rule templates (`.mdc`, `.instructions.md`), bootstrap, rule install, template sync.

## Step 1 — Relocate upstream README, LICENSE, and CONTRIBUTING (ask first)

**Do not move** project-owned root files without confirmation.

1. Check project root for `README.md`, `LICENSE.md`, and `CONTRIBUTING.md`.
2. Detect **upstream template repo files** (safe to relocate):
   - `README.md` first heading is `# Agentic Doc Templates`, or body clearly describes this template pack (not the user's app).
   - `LICENSE.md` contains `Creative Commons Attribution 4.0` and `Brian Lowe` (this pack's license).
   - `CONTRIBUTING.md` first heading is `# Contributing to Agentic Doc Templates`, or body clearly describes contributing to this template repo (not the user's project).
3. If **any** detected file looks like the user's own project docs → **stop** moving that file. Tell them to copy only `docs/templates/` next time (see [`../help/SETUP.md`](../help/SETUP.md)).
4. If upstream files detected → **ask**:

   > These look like Agentic Doc Templates repo files at your project root (README, LICENSE, and/or CONTRIBUTING). Move them to `docs/templates/agent/upstream/` so your project root stays yours?

5. On **yes**:
   - Create `docs/templates/agent/upstream/` if needed.
   - Move `README.md` → `docs/templates/agent/upstream/README.md` *(when detected as upstream)*
   - Move `LICENSE.md` → `docs/templates/agent/upstream/LICENSE.md` *(when detected as upstream)*
   - Move `CONTRIBUTING.md` → `docs/templates/agent/upstream/CONTRIBUTING.md` *(when detected as upstream)*
   - Do **not** delete — attribution and upstream docs stay in the project.
6. On **no** → leave in place; note in your summary that they may want to remove or merge manually.

If root `README.md` is upstream but user already has a project README they want to keep, offer to move only `LICENSE.md` and/or `CONTRIBUTING.md`, or merge upstream readme into `upstream/` without touching their README.

## Step 1b — Remove upstream GitHub issue templates (user projects)

**This pack’s** `.github/ISSUE_TEMPLATE/` is for feedback on [Agentic-Doc-Templates](https://github.com/BrianCLowe/Agentic-Doc-Templates) only. It must **not** stay in a user’s app repo.

When the whole template repo was cloned/copied into a project (or “Use this template” left `.github/ISSUE_TEMPLATE/` behind):

1. If `.github/ISSUE_TEMPLATE/` exists **and** contains Agentic Doc Templates forms (e.g. `agent-tool-problem.yml`, `template-improvement.yml`, `docs-confusion.yml`, `feedback.yml`, or bodies that mention Agentic Doc Templates / modular docs templates) → **delete that directory** (and remove `.github/` if it is empty afterward).
2. If `.github/ISSUE_TEMPLATE/` looks like the **user’s own** issue forms → **do not delete**.
3. Prefer copying only `docs/templates/` next time so `.github/` never lands in the project.

Also delete root-level Agentic-only GitHub noise if present from a whole-repo copy and clearly not the user’s: e.g. leftover `ISSUE_TEMPLATE` paths under `.github/` that match the upstream pack. Do **not** delete the user’s `.github/workflows/`, Copilot instructions, or other project GitHub config.

## Step 2 — Create docs layout

Create if missing:

```
docs/
├── Master_Index.md          ← from Master_Index_Template.md (Step 3)
├── Tooling.md               ← from Tooling_Template.md (Step 3b — machine tools)
├── Human-TODO.md            ← from Human_TODO_Template.md (Step 3d — human procurement)
├── rule-install-status.yaml ← only when RULE_INSTALL runs later
├── _shared/
│   └── assets/
├── decisions/
├── features/
│   └── assets/
├── reference/
│   └── visuals/
└── templates/               ← full template pack (not live project content)
    ├── help/
    ├── agent/
    ├── chat-ui/
    └── … scaffolds + workflow
```

Ensure **`docs/templates/`** contains at least:

- **Root:** `Master_Index_Template.md`, `Modular_Docs_Workflow.md`, `chat-ui/AGENT.md`, `Feature_Spec_Template.md`, `Feature_Understanding_Template.md`, `TODO_Template.md`, `Decision_Template.md`, `Tooling_Template.md`, `Human_TODO_Template.md`
- **`help/`:** `SETUP.md`, `USAGE.md`, `IDEA_CAPTURE_TIPS.md`, `USING_WITH_AGENTS.md`
- **`agent/`:** `BOOTSTRAP.md`, `RULE_INSTALL.md`, `TEMPLATE_SYNC.md`, `Modular_Documentation_Rule.mdc`, `Modular_Documentation_Rule.instructions.md`, `rule-install-status.example.yaml`

Run Step 0b if any setup files are still at `docs/` root or flat in `docs/templates/`.

## Step 3 — Create live Master_Index

If `docs/Master_Index.md` does not exist:

1. Copy content from `docs/templates/Master_Index_Template.md`.
2. Replace bracketed placeholders; set **Template version** and **Workflow version** to match the templates.
3. Fill Document Map (§3) from the conversation, README, or known scope — do not leave Section 3 empty if the user named features or shared components.

If `Master_Index.md` already exists → do not overwrite; offer [`TEMPLATE_SYNC.md`](TEMPLATE_SYNC.md) instead.

## Step 3b — Create live Tooling.md

If `docs/Tooling.md` does not exist:

1. Copy from `docs/templates/Tooling_Template.md`.
2. Fill **Required** (and optional) tools from Project Profile, README, and known stack — mark guesses for the user to confirm.
3. Ensure Master Index Key Locations / §3.4 link to `Tooling.md`.

If it already exists → do not overwrite; offer to update rows when the stack changes.

## Step 3c — Create live Human-TODO.md

If `docs/Human-TODO.md` does not exist:

1. Copy from `docs/templates/Human_TODO_Template.md`.
2. Add rows for any accounts, API keys, portal registrations, or purchases implied by the conversation / Document Map (e.g. Azure Bot, Teams app, Graph credentials). Leave empty Open table if none yet.
3. Ensure Master Index §3.3 / §3.4 link to `Human-TODO.md`.

If it already exists → add newly discovered procurement needs; do not wipe user-completed rows.

## Step 3d — Create files for every Document Map row *(mandatory)*

**A Document Map row is not documentation.** If you put a feature or shared component in §3.1 / §3.2, you **must** create the default file set in the same session (see [`Modular_Docs_Workflow.md`](../Modular_Docs_Workflow.md) §0):

| Always create | Status / notes |
|---------------|----------------|
| `*-Understanding.md` | status `draft` — agent interpretation for user review |
| `*.md` spec | stub/placeholder OK until Understanding is `confirmed` |
| `*-TODO.md` | core TODO; add InEditor/Asset TODOs when Project Profile / game extensions apply |

**Do not:**

- Leave map-only “planned” rows with broken or missing links “until the user picks one”
- Treat the Understanding `draft` gate as a reason to **skip creating** Understanding files — `draft` blocks **coding**, not **writing docs**
- Create nine fully graduated specs before the user confirms — stubs + draft Understandings are correct

**When many features were named** (e.g. 5+):

1. Create the default file set for **every** map row (Understanding as `draft`, thin spec stub, core TODO).
2. Tell the user which Understandings to review first (suggest Path A foundation or the feature they care about most).
3. Optionally ask once: “Review all draft Understandings, or start with [X]?” — do **not** wait for that ask before creating the files.

If the user named **no** features yet, skip Step 3d and say so in Step 4.

## Step 4 — Tell the user what's next

1. Confirm or correct Section 1 (Project Overview), Document Map, `docs/Tooling.md`, and `docs/Human-TODO.md`.
2. Point at the **draft** `-Understanding.md` files created in Step 3d — user reviews / corrects before implementation.
3. Point at **Open** items on `Human-TODO.md` — things only the human can procure before those features unblock.
4. After they confirm an Understanding, graduate durable content into the spec and continue from TODOs ([`../help/SETUP.md`](../help/SETUP.md)).
5. Optional: run [`RULE_INSTALL.md`](RULE_INSTALL.md) for agent rules (asks per tool, records in `rule-install-status.yaml`).

## Do not

- Overwrite an existing project `README.md` that is not the upstream template readme.
- Put project feature content into `docs/templates/` (templates stay canonical reference only).
- Create `docs/help/` or `docs/agent/` at docs root — those belong inside `docs/templates/`.
- Leave Agentic Doc Templates `.github/ISSUE_TEMPLATE/` in a user project — delete it (Step 1b).
- Skip asking before moving root files.
- Finish bootstrap with a filled Document Map but **no** feature/shared files on disk.
- Put human procurement items only in feature TODOs — use `docs/Human-TODO.md` and link from features.

## Example user prompts

- "Bootstrap modular docs in this project."
- "Set up the Agentic Doc Templates documentation structure."
- "I copied the whole templates repo — clean up and initialize docs."

## Related

- Human setup guide: [`../help/SETUP.md`](../help/SETUP.md)
- **How to use** (chat → docs, ideas, design docs): [`../help/USAGE.md`](../help/USAGE.md)
- Rule install (after bootstrap): [`RULE_INSTALL.md`](RULE_INSTALL.md)
- Template sync (updates): [`TEMPLATE_SYNC.md`](TEMPLATE_SYNC.md)
