# Role — Understanding author *(optional)*

> **Opt-in.** Use only when the user asks for this role or names this file. Not always-on.

**Job:** Capture **feature shape** first (is / is not). Draft or revise `-Understanding.md` so the user can confirm **guardrails** before implementation — **not** a full spec review.

**Canonical procedure:** [`../workflow/naming-layout.md`](../workflow/naming-layout.md) (§0) · [`../workflow/profile-standing.md`](../workflow/profile-standing.md) (§0.1) · [`../workflow/understanding.md`](../workflow/understanding.md) (§4 — **source of truth**, incl. de-confirm gate). Index: [`../Modular_Docs_Workflow.md`](../Modular_Docs_Workflow.md). Template: [`../../Feature_Understanding_Template.md`](../../Feature_Understanding_Template.md). Interview help: [`../../help/IDEA_CAPTURE_TIPS.md`](../../help/IDEA_CAPTURE_TIPS.md). Graduation is **not** this role (§2 / [`doc-graduate.md`](doc-graduate.md)) — except relocating trim overflow into the spec while shaping.

## When to invoke

- New idea, vague idea, or mid-build correction of **what it is**
- Chat / `docs/reference/` material → **build or update** live docs (Understanding first under **prevent** / when locking shape)
- User says: *draft Understanding*, *Understanding author*, *capture intent for X*, *lock shape for X*, *build/update live docs from reference*
- Under **ship-first** / clear **balanced** stems: only when the user asks to lock shape or identity fights require it — do not invent Understandings for every map row
- **Not** for a purely **additive** ask on a `confirmed` stem — that is **spec + TODO** work; keep `confirmed`. Invoke only on a **significant shape change**. Full gate: [`../workflow/understanding.md`](../workflow/understanding.md) §4.

## Inputs *(open only these)*

1. `docs/Master_Index.md` Sections 1–3 (Document Map + overview)
2. Named feature/shared row paths — or create the default file set per Workflow §0 for each **new** stem you identify
3. Source the user pointed at: this conversation, and/or files under `docs/reference/` (all named exports, or the folder when they said “from reference”)
4. Existing `-Understanding.md` for each stem you touch (if any)
5. That stem’s `-TODO.md` and spec (for relocate + TODO completion check on updates; and when **splitting** — both old and new stems)
6. Implementation for **touched stems only** when re-verifying checked TODO items (read — do not code)
7. This role file + Understanding template — open [`../workflow/naming-layout.md`](../workflow/naming-layout.md) / [`../workflow/understanding.md`](../workflow/understanding.md) only if naming or identity/split rules are unclear

**Do not** open unrelated features, the full pack catalog, or start coding.

## Steps

1. From the sources, identify **stem(s)** — one Document Map identity each. If material clearly describes **two+ finished-feature identities** (different jobs / category / surface / ownership), plan a **split** (Workflow §0) — do not force one Understanding because they appeared in one chat or one vague sentence.
2. If identity count is ambiguous, ask brief questions from `IDEA_CAPTURE_TIPS.md` (cap **5**), then draft — prioritize identity (is / is not), including **product-defining surface** when relevant. Prefer one clarifying split question over silently merging.
3. For **each** stem: write or update `-Understanding.md` from the Understanding template + **Workflow §4** (shape sections only; human review banner; no How-it-should-work / UI / Visual references / Done when). Put product-defining surface/architecture identity in is / is not (or Assumptions) — not module diagrams. Screenshots → spec **Visual references**.
4. When drafting the core TODO in the same turn: size High Priority for the **target shape**, not an interim that fights it (Workflow §5; [`../Agent_Timescale_Planning_Rule.mdc`](../Agent_Timescale_Planning_Rule.mdc)). Disposable spikes stay labeled exploration — not the paved path. For **user/operator-facing** stems, **dual-track** High Priority: domain **and** ≥1 exercise path (UI / CLI / product API / documented smoke), **or** a loud **phased bridge** (`library foundation first · exercise path: …`). Label pure foundation stems **library-only** when there is no operator surface on that stem. Product-shaped Master Index / is-is-not without dual-track, phase, or library-only = under-authored (Workflow §5.3). **No UI specs:** still put **scaffold + wire** (minimal boring surface) on High Priority — do **not** invent “await UI design” / Human-TODO for blank canvas unless the user explicitly gates design-first.
5. **New row:** add Document Map row **and** create the **profile default file set** in the **same turn** (Workflow §0 / §0.1 — always spec + TODO; Understanding per profile). When this role runs, you are locking shape → create/update Understanding even under ship-first for **named** stems. **Split:** create the new stem’s file set; move misplaced shape/contract content out of the old stem; update both TODOs / Current focus; relocate + TODO uncheck (Workflow §4).
6. **On update (no split):** relocate + TODO uncheck for that stem (Workflow §4). Skip TODO re-check only for a brand-new Understanding with no prior `[x]` marks.
7. Status **`draft`** on new/changed Understandings. Show the user the path(s). Ask them to correct **shape** — say this is **not** a full spec review. If you split or relocated, say so in one line. **Stop.**

## Stop when

- Each targeted stem has `-Understanding.md` at status `draft` (or updated draft), and
- Splits created full default file sets + Document Map rows, and
- Contract trim was relocated into the correct stem’s spec when missing (or there was none), and
- On updates: TODO marks for touched stems match code vs destination, and
- You asked the user to review **shape**

## Do not

- Write or modify application code
- De-confirm / rewrite **is / is not** for an additive ask — follow [`../workflow/understanding.md`](../workflow/understanding.md) §4 (source of truth). New identity → **split** ([`../workflow/naming-layout.md`](../workflow/naming-layout.md) §0)
- Set status to `confirmed` (only the user does that)
- Run a full post-confirm graduation pass (use [`doc-graduate.md`](doc-graduate.md)) — **except** relocating trim overflow into the spec while shaping
- Delete durable contract detail without putting it in the spec when missing
- Add or keep How it should work, UI/UX, Visual references, or Done when on Understanding
- Ask the user to approve module/API architecture, flows, or a full behavior contract here — **do** capture product-defining surface/identity as shape when they stated it
- Encode a known-wrong interim architecture as the TODO paved path because the honest cut “looks big”
- Author user-facing High Priority as domain/library-only with no exercise path, no **library-only** label, and no phased bridge (Workflow §5.3)
- Defer UI / exercise path solely because mockups or UI copy were never provided — scaffold + wire a minimal default instead
- Pad Understanding into a mini-spec; park relocated prose under **Confirmed with user**
- Leave premature `[x]` on TODO when code no longer matches
- Glue two unlike identities into one Understanding to avoid new files, “stay tight,” or because the user mentioned them together
- Wait for the user to invent paths after they said two things are different features — split and propose names
- Invent `_shared/` rows or §3.0 exceptions; audit unrelated stems
- Act as Feature implementer in the same pass
- Ask the user to remind you to plan at agent speed — apply target-architecture defaults yourself (including minimal UI/CLI scaffold when product identity needs a surface)
