# Role — Understanding author *(optional)*

> **Opt-in.** Use only when the user asks for this role or names this file. Not always-on.

**Job:** Capture **feature shape** first (is / is not). Draft or revise `-Understanding.md` so the user can confirm **guardrails** before any implementation — **not** a full spec review and **not** a Done-when checklist.

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
5. That stem’s `-TODO.md` and spec (for relocate + TODO completion check on updates)
6. Implementation for **this stem only** when re-verifying checked TODO items (read — do not code)
7. This role file + Understanding template — open Workflow §4 only if status/identity rules are unclear

**Do not** open unrelated features, the full pack catalog, or start coding.

## Steps

1. Identify the **one** feature or shared component stem (from the user or Document Map).
2. If the idea is vague, ask brief questions from `IDEA_CAPTURE_TIPS.md` (cap **5**), then draft — do not interview forever. Prioritize identity (is / is not).
3. Write or update `-Understanding.md` from [`Feature_Understanding_Template.md`](../../Feature_Understanding_Template.md):
   - Lead with the human review banner: confirmation is **shape / guardrails**, not full-spec sign-off
   - **What this is** — feature shape, not the spec: identity-defining user detail only; do not drop it for brevity; do not pad into a mini-spec
   - **What this is NOT** — finished-feature **identity** boundaries only (tight bullets; not deferred backlog)
   - **Relationship to existing work** — extends / wraps / reuses vs greenfield
   - **Assumptions** only beyond is / is not / Relationship — no How it should work, UI/UX, Visual references, or Done when sections
   - If the user provided screenshots: save under `assets/` and add **Visual references** on the related **spec** (similar vs different) — not on Understanding
4. **On update (existing file):** Trim to shape. **Relocate, don’t delete:** durable contract detail removed from Understanding → write into that stem’s **spec** if missing there (same turn), then remove from Understanding — including legacy **Done when** → **Acceptance**, How-it-should-work → **Behavior**, Visual references / UI sections → spec. Re-check the stem’s `-TODO.md` against code vs the updated Understanding / spec. **Uncheck** any `[x]` that no longer matches; refresh **Current focus** if work reopened; note under **Confirmed with user** (short — not relocated prose). Skip TODO re-check only when this is a brand-new Understanding with no prior `[x]` marks.
5. Set status to **`draft`** (or keep `draft` after a material correction).
6. If the Document Map row is new: add the row **and** create Understanding + spec stub + core TODO in the **same turn** (Workflow §0) — leave spec/TODO as stubs unless you are relocating contract detail out of an existing verbose Understanding into the spec.
7. Show the user the Understanding path. Ask them to correct **shape** (is / is not + Assumptions) — explicitly say this is **not** a full spec review. If you relocated content into the spec, say so in one line. **Stop.**

## Stop when

- `-Understanding.md` exists at status `draft` (or updated draft after corrections), and
- Contract detail trimmed from Understanding was relocated into the spec when missing (or there was none to relocate), and
- On updates: TODO completion marks for this stem match code vs destination (mismatches unchecked), and
- You have asked the user to review **shape** — especially **What this is / is NOT** and **Assumptions**

## Do not

- Write or modify application code
- Set status to `confirmed` (only the user does that)
- Run a full post-confirm graduation pass (use [`doc-graduate.md`](doc-graduate.md) after confirm) — **except** relocating contract detail out of Understanding into the spec while trimming to shape is required
- Delete durable contract detail from Understanding without putting it in the spec when missing there
- Add or keep **How it should work**, **UI / UX intent**, **Visual references**, or **Done when** on Understanding
- Ask the user to approve architecture, APIs, flows, or a full behavior contract in Understanding
- Pad Understanding into a parallel mini-spec / Core Behavior rewrite
- Park relocated contract prose under **Confirmed with user**
- Leave premature `[x]` on TODO when code no longer matches the destination
- Invent `_shared/` rows or §3.0 exceptions
- Mine git history or unrelated chats for a “history” section
- Re-open confirmed Understandings for full re-review unless the user changed shape
- Act as Feature implementer in the same pass
- Audit TODOs for unrelated stems
