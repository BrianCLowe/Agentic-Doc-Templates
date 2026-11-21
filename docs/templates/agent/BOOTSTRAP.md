# Bootstrap Modular Docs — Agent Instructions

Follow the `adt-bootstrap` skill: [`docs/templates/agent/skills/adt-bootstrap/SKILL.md`](skills/adt-bootstrap/SKILL.md). Do not reconstruct the procedure from memory.

Fix internal links after moving (including Master Index links to the workflow). **Keep at `docs/templates/` root:** `VERSION`, `CHANGELOG.md`, `Master_Index_Template.md`, `Feature_*_Template.md`, `Decision_Template.md`, Tooling/Human_TODO/Product_Vision templates. **Keep in `docs/templates/agent/`:** `Modular_Docs_Workflow.md` (index), `workflow/` modules, `roles/` (incl. `adapter-src/`), `GENERATE_ROLE_ADAPTERS.md`, rule templates (`.mdc`, `.instructions.md`), bootstrap, rule install, template sync. (`chat-ui/` may exist as a paused stub - not a live path.)
- **Root:** `README.md` (pack-owned warning), `VERSION`, `CHANGELOG.md`, `Master_Index_Template.md`, `Feature_Spec_Template.md`, `Feature_Understanding_Template.md`, `Decision_Template.md`, `Tooling_Template.md`, `Human_TODO_Template.md`, `Product_Vision_Template.md`
2. Add Open rows for any human-gated needs implied by the conversation / Document Map - `procure` (keys/portals), `decide`, or `waiting`. If none yet, leave the Open **list** empty (not a table - Workflow Section 13).
If it already exists -> add newly discovered human-gated needs (procure / decide / waiting); do not wipe user-completed rows.
**Mandatory:** Present **and explain** every still-unset preference below in **one** user-facing message. Do **not** drip-feed separate quizzes across later steps for the same keys. Skip only keys already set in `docs/ADT-settings.yaml`. Create/update that file from [`ADT-settings.example.yaml`](ADT-settings.example.yaml) when recording. Do **not** copy a `standing:` key from the example - omit it unless they already stated a playbook override.
Do not create `*-TODO.md`.
