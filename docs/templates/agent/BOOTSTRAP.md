# Bootstrap Modular Docs — Agent Instructions

> Use when the user asks to set up, bootstrap, or initialize modular documentation in their project. Follow this **before** [`RULE_INSTALL.md`](RULE_INSTALL.md) (rules come after doc structure exists).

## Goal

Create the live `docs/` layout (Master_Index, feature folders, template pack in place) without leaving **this repo's** root `README.md`, `LICENSE.md`, or `CONTRIBUTING.md` in the project root when the user copied the whole template repository.

## Step 0 — How templates arrived (pick a path)

| Situation | Action |
|-----------|--------|
| `docs/templates/` copied (full pack with `help/`, `agent/`, scaffolds) | Skip Step 1 (relocate) unless whole repo. **Spot-check** pack (below) — do not walk the whole tree. |
| `docs/help/` and/or `docs/agent/` at `docs/` root (older layout) | Run **Step 0b — migrate layout**, then continue. |
| Flat files only in `docs/templates/` (oldest layout) | Run **Step 0b — migrate layout**, then continue. |
| Whole repo cloned/copied into the project | Do Step 1 (auto-move clearly upstream root files; ask only if ambiguous). |
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

Fix internal links after moving. **Keep at `docs/templates/` root:** `VERSION`, `CHANGELOG.md`, `Master_Index_Template.md`, `Modular_Docs_Workflow.md`, `chat-ui/`, `Feature_*_Template.md`, `TODO_Template.md`, `Decision_Template.md`. **Keep in `docs/templates/agent/`:** rule templates (`.mdc`, `.instructions.md`), bootstrap, rule install, template sync.

## Step 1 — Relocate upstream README, LICENSE, and CONTRIBUTING *(auto-move when clearly this pack)*

1. Check project root for `README.md`, `LICENSE.md`, and `CONTRIBUTING.md`.
2. Per file, decide **clearly upstream** vs **project-owned** vs **ambiguous**:

   **Clearly upstream — move immediately, do not ask** (any strong marker is enough):

   | File | Clear upstream markers |
   |------|------------------------|
   | `README.md` | Heading `# Agentic Doc Templates`, or body names **Agentic Doc Templates** / **Agentic-Doc-Templates** as *this* pack (not merely linking to it) |
   | `LICENSE.md` | **Creative Commons Attribution 4.0** plus **Brian Lowe** / **BrianCLowe** |
   | `CONTRIBUTING.md` | Heading `# Contributing to Agentic Doc Templates`, or body is about contributing to this template pack |

   Also treat as clearly upstream if the file repeatedly names **Brian Lowe**, **BrianCLowe**, or **Agentic Doc Templates** as the author/product of *these* root docs (not the user’s app).

   **Project-owned — do not move:** File describes the user’s app/product with no pack markers above.

   **Ambiguous — ask once** (only this case): Markers conflict or you cannot tell. Do not re-ask every session.

3. For each **clearly upstream** file:
   - Create `docs/templates/agent/upstream/` if needed.
   - Move → `docs/templates/agent/upstream/README.md` (or `LICENSE.md` / `CONTRIBUTING.md`).
   - Do **not** delete — attribution stays in the project.
   - Mention the move briefly in the bootstrap summary — **no confirmation prompt**.

4. Leave project-owned files alone. Suggest copying only `docs/templates/` next time (see [`../help/SETUP.md`](../help/SETUP.md)).

Do **not** overwrite a project-owned root `README.md`. If an upstream README is already under `agent/upstream/`, leave the user’s root README alone.

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
├── upstream-status.yaml     ← only when weekly template update checks are enabled (Step 4b)
├── _shared/
│   └── assets/
├── decisions/
├── features/
│   └── assets/
├── reference/               ← design docs, chat exports, PRDs, legacy specs (not living modular docs)
│   ├── README.md            ← short “what goes here” (create if missing — see below)
│   └── visuals/             ← optional inspiration screenshots
└── templates/               ← full template pack (not live project content)
    ├── help/
    ├── agent/
    ├── chat-ui/
    └── … scaffolds + workflow
```

If `docs/reference/README.md` is missing, create it with:

```markdown
# Reference materials

Drop **source** materials here — design docs, PRDs, Notion/export dumps, full chat transcripts, legacy specs.

Living modular docs stay in `features/`, `_shared/`, and `Master_Index.md`. Agents read files here when you point at them (or when converting to modular docs); they do not treat this folder as the Document Map.

Optional: `visuals/` for inspiration screenshots before a feature folder exists.
```

**Pack spot-check** (enough to proceed — do not inventory every file):

- `VERSION`, `CHANGELOG.md`, `Modular_Docs_Workflow.md`, `agent/BOOTSTRAP.md`, `help/SETUP.md`

If any of those are missing, expand the inventory below and run Step 0b if layout looks old. Otherwise continue.

**Full inventory** *(only if spot-check fails):*

- **Root:** `VERSION`, `CHANGELOG.md`, `Master_Index_Template.md`, `Modular_Docs_Workflow.md`, `chat-ui/AGENT.md`, `Feature_Spec_Template.md`, `Feature_Understanding_Template.md`, `TODO_Template.md`, `Decision_Template.md`, `Tooling_Template.md`, `Human_TODO_Template.md`
- **`help/`:** `SETUP.md`, `USAGE.md`, `IDEA_CAPTURE_TIPS.md`, `USING_WITH_AGENTS.md`
- **`agent/`:** `BOOTSTRAP.md`, `RULE_INSTALL.md`, `TEMPLATE_SYNC.md`, `TEMPLATE_UPDATE_CHECK.md`, `Modular_Documentation_Rule.mdc`, `Modular_Documentation_Rule.instructions.md`, `Template_Update_Check_Rule.mdc`, `Template_Update_Check_Rule.instructions.md`, `rule-install-status.example.yaml`, `upstream-status.example.yaml`

Run Step 0b if any setup files are still at `docs/` root or flat in `docs/templates/`.

## Step 3 — Create live Master_Index

If `docs/Master_Index.md` does not exist:

1. Copy content from `docs/templates/Master_Index_Template.md`.
2. Replace bracketed placeholders; set **Template version** and **Workflow version** to match the templates.
3. Fill Document Map (§3) from **this conversation and Project Profile** — do not leave Section 3 empty if the user named features or shared components. Open README only if overview/map are empty. Do **not** invent features from a codebase scan.

If `Master_Index.md` already exists → do not overwrite; offer [`TEMPLATE_SYNC.md`](TEMPLATE_SYNC.md) instead.

## Step 3b — Create live Tooling.md

If `docs/Tooling.md` does not exist:

1. Copy from `docs/templates/Tooling_Template.md`.
2. Fill **Required** (and optional) tools from Project Profile and this conversation — mark guesses for the user to confirm. Open README only if the stack is unknown.
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
5. Run **Step 4b** (weekly template update checks) before finishing.
6. Optional: run [`RULE_INSTALL.md`](RULE_INSTALL.md) for agent rules (asks per tool, records in `rule-install-status.yaml`). If Step 4b was **yes**, RULE_INSTALL also installs the optional update-check rule.

## Step 4b — Weekly template update checks (ask first)

Projects that copied or templated this pack do **not** share the upstream git remote. Offer an **optional** agent rule that pings upstream about once a week (or whenever the user asks).

**Ask** (do not enable silently):

> Want the agent to check weekly for Agentic Doc Templates updates?
>
> How it works: a tiny `docs/upstream-status.yaml` stores `last_checked` and your local template version. When a week has passed (or you ask), the agent fetches only the upstream `VERSION` file and tells you if a newer pack exists — then you can sync with TEMPLATE_SYNC.
>
> Token cost is negligible (tens of tokens to read the status file; a small network fetch only when due). Decline if you prefer to ask manually: *"Update the doc templates from Agentic Doc Templates and sync our live docs."*

### On **yes**

1. Create `docs/upstream-status.yaml` from [`upstream-status.example.yaml`](upstream-status.example.yaml).
2. Set `last_checked` to today, and `local_template_version` / `local_workflow_version` from local `docs/templates/VERSION` (or the markers in `Master_Index_Template.md` / `Modular_Docs_Workflow.md` if `VERSION` is missing).
3. Record in `docs/rule-install-status.yaml` under `optional_rules.template-update-check` with `status: enabled` and `recorded` (create the file if needed — see [`rule-install-status.example.yaml`](rule-install-status.example.yaml)).
4. Install the optional rule when installing tool rules — follow [`RULE_INSTALL.md`](RULE_INSTALL.md) **Optional rules**. If the user skips RULE_INSTALL for now, note that checks need the optional rule installed for their tool(s).

### On **no**

1. Do **not** create `docs/upstream-status.yaml`.
2. Record `optional_rules.template-update-check` with `status: declined` and `recorded` in `docs/rule-install-status.yaml` so future sessions do not re-ask unless the user requests it.
3. Mention they can still sync anytime via [`TEMPLATE_SYNC.md`](TEMPLATE_SYNC.md) or enable checks later (*"Check for template updates every week"*).

### Explicit overrides later

- "Check for template updates every week" / "Enable template update checks" → treat as **yes** even if previously declined.
- "Stop checking for template updates" → remove or leave `docs/upstream-status.yaml`; set optional rule status to `declined`; remove installed `template-update-check` rule files if present (ask before deleting).

## Do not

- Overwrite an existing project `README.md` that is not the upstream template readme.
- Put project feature content into `docs/templates/` (templates stay canonical reference only).
- Create `docs/help/` or `docs/agent/` at docs root — those belong inside `docs/templates/`.
- Leave Agentic Doc Templates `.github/ISSUE_TEMPLATE/` in a user project — delete it (Step 1b).
- Ask before moving root files that are **clearly** upstream (Agentic Doc Templates / Brian Lowe / BrianCLowe markers) — just move them.
- Finish bootstrap with a filled Document Map but **no** feature/shared files on disk.
- Put human procurement items only in feature TODOs — use `docs/Human-TODO.md` and link from features.
- Enable weekly template update checks without asking (Step 4b).

## Example user prompts

- "Bootstrap modular docs in this project."
- "Set up the Agentic Doc Templates documentation structure."
- "I copied the whole templates repo — clean up and initialize docs."

## Related

- Human setup guide: [`../help/SETUP.md`](../help/SETUP.md)
- **How to use** (chat → docs, ideas, design docs): [`../help/USAGE.md`](../help/USAGE.md)
- Rule install (after bootstrap): [`RULE_INSTALL.md`](RULE_INSTALL.md)
- Template sync (updates): [`TEMPLATE_SYNC.md`](TEMPLATE_SYNC.md)
- Cheap update ping: [`TEMPLATE_UPDATE_CHECK.md`](TEMPLATE_UPDATE_CHECK.md)
