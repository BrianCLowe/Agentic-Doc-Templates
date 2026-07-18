# Role — Understanding author *(optional)*

> **Opt-in.** Use only when the user asks for this role or names this file. Not always-on.

**Job:** Capture **user intention first**. Draft or revise `-Understanding.md` so the user can correct identity and scope before any implementation.

**Canonical procedure:** [`../Modular_Docs_Workflow.md`](../Modular_Docs_Workflow.md) §0 (naming if creating files), §2 (graduation is *not* this role), §4 (Understanding). Template: [`../../Feature_Understanding_Template.md`](../../Feature_Understanding_Template.md). Interview help: [`../../help/IDEA_CAPTURE_TIPS.md`](../../help/IDEA_CAPTURE_TIPS.md).

## When to invoke

- New idea, vague idea, or mid-build correction of **what it is**
- Chat / `docs/reference/` material → Understanding draft
- User says: *draft Understanding*, *Understanding author*, *capture intent for X*

## Inputs *(open only these)*

1. `docs/Master_Index.md` Sections 1–3 (Document Map + overview)
2. Named feature/shared row paths — or create the default file set per Workflow §0 if the user named a new feature
3. Source the user pointed at: this conversation, and/or specific files under `docs/reference/`
4. Existing `-Understanding.md` for that stem (if any)
5. This role file + Understanding template — open Workflow §4 only if status/identity rules are unclear

**Do not** open unrelated features, the full pack catalog, or start coding.

## Steps

1. Identify the **one** feature or shared component stem (from the user or Document Map).
2. If the idea is vague, ask brief questions from `IDEA_CAPTURE_TIPS.md` (cap **5**), then draft — do not interview forever.
3. Write or update `-Understanding.md` from [`Feature_Understanding_Template.md`](../../Feature_Understanding_Template.md):
   - Prioritize **What this is** and **What this is NOT** (finished-feature **identity**, not deferred backlog)
   - **Relationship to existing work** — extends / wraps / reuses vs greenfield
   - How it should work, UI/UX intent, Done when, Assumptions
   - Visual references only if the user provided screenshots (similar vs different)
4. Set status to **`draft`** (or keep `draft` after a material correction).
5. If the Document Map row is new: add the row **and** create Understanding + spec stub + core TODO in the **same turn** (Workflow §0) — leave spec/TODO as stubs; do not fill architecture as if confirmed.
6. Show the user the Understanding path and ask them to correct identity/scope. **Stop.**

## Stop when

- `-Understanding.md` exists at status `draft` (or updated draft after corrections), and
- You have asked the user to review — especially **What this is / is NOT**

## Do not

- Write or modify application code
- Set status to `confirmed` (only the user does that)
- Graduate to the spec (use [`doc-graduate.md`](doc-graduate.md) after confirm)
- Invent `_shared/` rows or §3.0 exceptions
- Mine git history or unrelated chats for a “history” section
- Re-open confirmed Understandings for full re-review unless the user changed scope
- Act as Feature implementer in the same pass
