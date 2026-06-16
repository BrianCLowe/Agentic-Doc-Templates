# Bootstrap Modular Docs — Agent Instructions

> Use when the user asks to set up, bootstrap, or initialize modular documentation in their project. Follow this **before** [`RULE_INSTALL.md`](RULE_INSTALL.md) (rules come after doc structure exists).

## Goal

Create the live `docs/` layout (Master_Index, folders, templates in place) without leaving **this repo's** root `README.md` / `LICENSE.md` in the project root when the user copied the whole template repository.

## Step 0 — How templates arrived (pick a path)

| Situation | Action |
|-----------|--------|
| Only `docs/templates/` was copied | Skip Step 1 (relocate). Ensure `docs/templates/` is complete. |
| Whole repo cloned/copied into the project | Do Step 1 after user confirms. |
| Submodule of [Agentic-Doc-Templates](https://github.com/BrianCLowe/Agentic-Doc-Templates) | Prefer symlink or copy `docs/templates/` only; optional Step 1 for root files if submodule is at repo root. |

## Step 1 — Relocate upstream README and LICENSE (ask first)

**Do not move** project-owned root files without confirmation.

1. Check project root for `README.md` and `LICENSE.md`.
2. Detect **upstream template repo files** (safe to relocate):
   - `README.md` first heading is `# Agentic Doc Templates`, or body clearly describes this template pack (not the user's app).
   - `LICENSE.md` contains `Creative Commons Attribution 4.0` and `Brian Lowe` (this pack's license).
3. If **either** file looks like the user's own project docs → **stop**, do not move. Tell them to copy only `docs/templates/` next time (see [`SETUP.md`](SETUP.md)).
4. If upstream files detected → **ask**:

   > These look like the Agentic Doc Templates repo README/LICENSE at your project root. Move them to `docs/templates/upstream/` so your project root stays yours?

5. On **yes**:
   - Create `docs/templates/upstream/` if needed.
   - Move `README.md` → `docs/templates/upstream/README.md`
   - Move `LICENSE.md` → `docs/templates/upstream/LICENSE.md`
   - Do **not** delete — attribution and upstream docs stay in the project.
6. On **no** → leave in place; note in your summary that they may want to remove or merge manually.

If root `README.md` is upstream but user already has a project README they want to keep, offer to move only `LICENSE.md`, or merge upstream readme into `upstream/` without touching their README.

## Step 2 — Create docs layout

Create if missing:

```
docs/
├── Master_Index.md          ← from Master_Index_Template.md (Step 3)
├── rule-install-status.yaml ← only when RULE_INSTALL runs later
├── _shared/
│   └── assets/
├── decisions/                 ← optional cross-cutting decisions
├── features/
│   └── assets/
├── reference/
│   └── visuals/               ← optional; inspiration before a feature exists
└── templates/               ← canonical templates (already present or copy from this folder)
    └── upstream/            ← after Step 1, if applicable
```

Ensure `docs/templates/` contains at least: `Master_Index_Template.md`, `Feature_Spec_Template.md`, `Feature_Understanding_Template.md`, `TODO_Template.md`, `Decision_Template.md`, `IDEA_CAPTURE_TIPS.md`, `TEMPLATE_SYNC.md`, `BOOTSTRAP.md`, `SETUP.md`, `RULE_INSTALL.md`, `USING_WITH_AGENTS.md`, rule templates, `rule-install-status.example.yaml`.

If `docs/USING_WITH_AGENTS.md` exists at `docs/` root (older layout), move it into `docs/templates/` and fix links.

## Step 3 — Create live Master_Index

If `docs/Master_Index.md` does not exist:

1. Copy content from `docs/templates/Master_Index_Template.md`.
2. Replace bracketed placeholders; set **Template version** to match the template.
3. Add at least placeholder rows in Document Map — do not leave Section 3 empty if user named features.

If `Master_Index.md` already exists → do not overwrite; offer [`TEMPLATE_SYNC.md`](TEMPLATE_SYNC.md) instead.

## Step 4 — Tell the user what's next

1. Fill in Section 1 (Project Overview) and Document Map.
2. First feature: agent drafts spec + Understanding + TODO; you review (see [`SETUP.md`](SETUP.md)). Shared components: same full note set under `_shared/` unless the user excepts specific files.
3. Optional: run [`RULE_INSTALL.md`](RULE_INSTALL.md) for agent rules (asks per tool, records in `rule-install-status.yaml`).

## Do not

- Overwrite an existing project `README.md` that is not the upstream template readme.
- Put project feature content into `docs/templates/` (templates stay canonical reference only).
- Skip asking before moving root files.

## Example user prompts

- "Bootstrap modular docs in this project."
- "Set up the Agentic Doc Templates documentation structure."
- "I copied the whole templates repo — clean up and initialize docs."

## Related

- Human setup guide: [`SETUP.md`](SETUP.md)
- **How to use** (chat → docs, ideas, design docs): [`USAGE.md`](USAGE.md)
- Rule install (after bootstrap): [`RULE_INSTALL.md`](RULE_INSTALL.md)
- Template sync (updates): [`TEMPLATE_SYNC.md`](TEMPLATE_SYNC.md)
