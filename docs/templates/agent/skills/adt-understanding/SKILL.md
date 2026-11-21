---
name: adt-understanding
description: Draft or revise a feature Understanding, capture intent, and apply the lock gate. Use when the user says draft or revise Understanding, new idea, capture intent, correct What this is / is not, or build live docs from docs/reference/.
---

> **Workflow module — source of truth** for shape vs contract (Understanding + graduation + de-confirm gate). Open from the [workflow index](/docs/templates/agent/Modular_Docs_Workflow.md) when drafting/confirming Understanding, graduating to spec, or deciding additive vs shape change. Rules and roles summarize; **this file wins on conflict**.

# Understanding & graduation

## 2. Understanding → Spec graduation

**Source of truth:** This module (§2 + §4) is the canonical shape-vs-contract procedure. Rules and roles summarize; live scaffolds are fill-in blanks. **This file wins on conflict**. Applies fully under **`prevent`**, and for any stem that **has** an Understanding under other profiles. Under **`build-first`** (no Understanding), grow the **spec** directly as contract home — skip steps 1 and the Understanding half of step 3.

| File | Role | When to update |
|------|------|----------------|
| `-Understanding.md` | **Feature shape / guardrails** — is / is not, Assumptions; user confirms **shape** (not the full contract) | When the profile requires it, or user locks shape / identity is ambiguous |
| `.md` spec (feature or `_shared/`) | **Durable contract** — architecture, API, decisions, stable behavior, Acceptance, Visual references | After shape confirm (if Understanding exists); as you implement under `build-first`; when code and docs must match |

**Workflow *(when Understanding is in play)*:**

1. Agent drafts `-Understanding.md` → user confirms **shape** (`confirmed`) — is / is not + any remaining **real-fork** Assumptions (empty is fine). **Not** a full spec sign-off. Lock obvious defaults; do not invent quizzes (lock gate in §4).
2. Agent **graduates** durable contract into the spec: overview, architecture/contract, Behavior, **Acceptance**, **Visual references**, **Decisions**, dependencies, maturity (shared). Synthesize from Understanding **plus** conversation / decisions - do **not** only copy thin Understanding. A short Understanding is **not** permission to write a short spec. Do **not** omit confirmed Behavior / Acceptance / Visuals to "keep the pack lean" - lean is Understanding shape + no padding, not dropping contract callers need. For Acceptance, prefer a short list of coarse, exercisable outcomes, not a padded checklist. User-facing stems: Acceptance includes >=1 **operable** outcome (something a person can exercise). Name each **category enabler**: one lock in identity, a Dependencies row **Enabler**, and one Acceptance clause that is false on a stub or an unfinished sibling.
3. After graduation, Understanding keeps only shape sections (§4). Spec = contract truth. **In-scope spec surfaces** (kit leftovers on this stem) stay on **this stem’s spec** — a complete overview is **not** permission to omit them, and is **not** a reason to add empty map rows (§0 inventory).
4. If implementation diverges, update the spec **or** set Understanding to `superseded` and revise (§4) — do not leave both stale.

**Workflow *(build-first / no Understanding on stem)*:** Keep a thin-but-real spec; capture lasting preferences on the spec **Decisions** table same turn (§10). Offer *lock shape* (Understanding) when identity fights start.

See [`Feature_Spec_Template.md`](/docs/templates/Feature_Spec_Template.md) and [`Feature_Understanding_Template.md`](/docs/templates/Feature_Understanding_Template.md).

---

## 4. Understanding (Features & Shared)

**Source of truth** with §2 — other pack files summarize; this section wins on conflict. Live `-Understanding.md` files are **fill-in blanks** ([`Feature_Understanding_Template.md`](/docs/templates/Feature_Understanding_Template.md)). Teaching examples live **here**, not in the scaffold. Human review: [`../../help/SCAFFOLDS.md`](/docs/templates/help/SCAFFOLDS.md). **When required:** §0.1 docs profile. **Compaction / thin context:** re-open this module before drafting or editing Understanding — do not reconstruct the gate from memory.

Under **`prevent`**, each **feature** and substantial **shared component** gets a `-Understanding.md` — the agent’s model of **feature shape** (guardrails). **Not** a second durable spec. Under **`balanced`**, create when identity is ambiguous / multi-surface / split pressure / user asked. Under **`build-first`**, only when user asks *lock shape* or the file already exists.

**Whole product:** Feature is / is not is **one stem**. The cohesive end-state lives in `docs/Product-Vision.md` — [`product-vision.md`](/docs/templates/agent/workflow/product-vision.md) §4.5. A feature that fights a **confirmed** product vision is a shape fight — do not implement it. Do not paste the product vision into every Understanding.

- Features: `features/FeatureName-Understanding.md`
- Shared: `_shared/ComponentName-Understanding.md`

**Who writes it:** Agent drafts first (`draft`) from conversation, design doc, or interview. User **reviews and corrects shape** — they do not author from scratch and are **not** approving the full contract here.

**Default under prevent:** Same Understanding for shared components as features. **Only skip** when the user **explicitly** excepts it (Master Index §3.0) **or** project `docs_profile` is `build-first` / `balanced` allows skip. Under prevent, missing files or convenience are not exceptions.

**Shape sections only** (keep these; nothing else):

| Section | Put here | Do not put here |
|---------|----------|-----------------|
| **What this is** | Identity-defining user detail: category, metaphors, naming, “feels like,” ownership, product-defining constraints **and surface/architecture identity** (e.g. one continuous surface). Prefer user’s words. Brief feel/layout only if it defines the product. | Flows, module/API diagrams, edge matrices, acceptance lists, How-it-should-work, Core Behavior rewrite, padding/speculation |
| **What this is NOT** | Finished-feature **identity** boundaries (wrong category, wrong product surface/architecture, ownership) | Deferred phases, “not built yet,” backlog, or “NOT the final architecture yet” excuses — those belong on the spec, not as identity |
| **Relationship** | Extends / wraps / reuses vs greenfield | Foundation task lists |
| **Assumptions** | **Real forks only** — two live alternatives with no obvious winner | Invented decisions, obvious defaults, examples-as-picks, full-spec open questions |
| **Confirmed with user** | Short correction notes + date | Relocated contract prose |

Durable contract (Behavior, **Acceptance**, Visual references, architecture) → **spec** (§2).

**Drafting size — What this is**

Length matches the shape detail the user gave — not a telegram summary, and not a parallel feature narrative.

- *Too thin (drops shape):* “A role-specific view of the existing text editor.”
- *Right size (shape):* Same framing **plus** identity they actually gave — e.g. same editing core (not a second engine); one continuous surface vs N separate editors; chrome differs for this workflow; metaphors / “feels like”; product-defining constraints. Not implementation steps, prop tables, happy-path numbered flows, or a full behavior rewrite.
- *Wrong size (mini-spec):* Restating Core Behavior, API/prop tables, scene-break matrices, acceptance checklists, How-it-should-work flows, or every edge case — that belongs in the **spec**.

Product-defining surface / architecture belongs in **What this is** when it decides identity — e.g. “one continuous manuscript surface; seams are visual; notes stay separate storage.” Once confirmed, plan/build that **target** — do not park a fighting interim as the paved path.

**Drafting size — What this is NOT**

Identity boundaries for the **finished** feature. Do **not** list work that is still planned, phased later, or “not implemented yet.”

- *Bad (do not write):* “NOT freeform multi-window Desktop Mode — that is long-term in the spec.” That is deferred work for the same feature, not an identity boundary.
- *Good:* “NOT a freeform multi-window desktop OS — Main Workspace is a document-centric layout (panels / side-by-side), not overlapping OS windows.” *(Only if that is truly never what this feature is meant to be.)*
- *Wrong-engine:* “NOT a second editor engine — same editing core as BlockEditor; this stem is role chrome / a different surface on that core.”

### Lock gate — obvious defaults vs real forks

**Source of truth** for this gate — rules and roles summarize; **this subsection wins on conflict**. Compaction / thin context: re-open this module; do not reconstruct from the scaffold.

Lock obvious category defaults into is / is not and list them in one line on review. Assumptions hold only real forks (no obvious winner). Do not invent a quiz or promote a reference example into identity. If you are unsure whether a choice is a real fork, ask once, clearly.

Agents invent decisions, then either lock the invention as identity or dump it into **Assumptions** so the user has boxes to check. That is the failure. **Empty Assumptions is success** when every default was the obvious best.

**No-ask proviso:** If the design is already clear (conversation / `docs/reference/` already gives category, is / is not, and the obvious defaults), **zero Assumption asks is correct.** Do not invent a quiz so the user has something to confirm. Shape review may be is / is not only.

| Do | Do not |
|----|--------|
| **Lock the obvious** into **What this is / is NOT** (identity) or a one-line lock on review | Put an obvious best default under **Assumptions** and ask “how should this be handled?” |
| Leave **Assumptions** for **real forks only** | Invent a vendor, jurisdiction, schema, comparison row, or label set the user did not pick — then quiz it |
| Treat chat / `docs/reference/` walkthroughs as **examples**, not the target, unless the user **clearly set them as the target** | Encode a reference example as identity, a vendor pick, a jurisdiction, or a spec constraint |

**Lock the obvious.** A default is obvious when it is the standard for the product category, an already-stated constraint, or the cheaper/simpler path that still hits the target — and the user did not contradict it. Write it into **is / is not**. On shape review, list what you locked in **one line** so they can override. If you are unsure whether it is a real fork, ask once, clearly.

**Category enabler.** An input or a sibling portion the product cannot be exercised truthfully without (prices for a trading product). The user will not think to say it. Write the **existence** into **is / is not** without asking. Which source is a real fork only when two live options have no obvious winner. On the spec: a Dependencies row **Enabler**, and one Acceptance clause that is false when that input is missing.

**Real fork.** Two (or more) live alternatives with **no** obvious winner from the conversation, the category, or the constraints (paid data vs free tables; which third-party API family; journey order when both placements are plausible). Those stay unchecked **Assumptions**. Spec-level open questions still do **not** belong here.

**Examples are not the target** unless the user **clearly set them as the target**. A walkthrough, sample project, named vendor, or place in chat / `docs/reference/` is how they explained the idea — not product identity, not a pick, not a jurisdiction. Keep it out of **is / is not**, the spec, and the fork list. Only lock it if they said this *is* the product, the pick, or the scope.

- *Bad (example → target):* Reference docs walk a timber-frame lot in VA/WV to explain home design. Agent writes a timber-frame / Virginia product, or asks whether that sample is the flagship.
- *Good:* “A home-design app for anywhere in the US first. User location sets jurisdiction.” The timber-frame VA/WV lot stays an example. No named 3D vendor unless they clearly picked one.
- *Bad (invented quiz):* “Energy Star vs other efficiency labels?” when Energy Star is the obvious US residential catalog flag. “Should defaults be user-editable?” when editable is the obvious consumer path.
- *Good (lock):* Energy Star locked in **is / is not**. Defaults are user-editable. Assumptions stay empty unless a real fork remains.
- *Bad (unstated enabler):* A paper-trade stem whose **is** never mentions a price source, because “everyone knows.” The scorer then runs against an unfinished feed and saves “strategies are not completing.”
- *Good (enabler lock):* “Fills use a price source. The scorer does not persist until that source is fully functional.” Paid feed vs free tables stays an Assumption only when both are live and neither wins.
- *Good (real fork):* “Cost tables: free/manual vs paid RSMeans-class.” “Utility tables vs live APIs.” Those have no obvious winner without a budget or integration choice.
- Lock the obvious **full** target. PDF-first as the consumer handoff is a **lock**; IFC stays named on the spec.
- *Do not ask:* “Which jurisdiction should we use?” / “How should Energy Star be handled?” / “Is the reference walkthrough the product?” Those quiz the obvious path or promote an example into a target.

**Clean-out pass.** Existing Understandings (and specs that copied a reference example as a constraint) get the same gate. **Offer** it - all Document Map Understanding stems / named / no; default yes. Sync tag `optional-assumption-cleanout` ([`TEMPLATE_SYNC_B.md`](/docs/templates/agent/TEMPLATE_SYNC_B.md)). Mid-session: if the user is correcting invented decisions or you already see unresolved Assumptions on open stems, offer the same pass. Do **not** silent-scan the whole map without that offer or the tagged sync execute.

On execute (chosen stems that **have** Understanding):

1. Lock obvious defaults that sit as unchecked Assumptions into **is / is not**.
2. Delete Assumption bullets that are invented quizzes, obvious defaults, or reference examples treated as forks.
3. If **is / is not** (or the spec) treated a reference example as the target and it was **not** clearly set as the target → restore category-level identity. **Keep status** — do **not** de-confirm (`confirmed` → `draft`) and do **not** inject a mid-sync shape quiz. Record the correction under **Confirmed with user** and in the sync / review summary.
4. Leave **real forks** unchecked. Empty Assumptions is success. One-line lock list under **Confirmed with user**.
5. Heading → `Assumptions (real forks only)` if it still says “needs user confirmation.”
6. Do **not** invent new Assumptions, new stems, Understanding on `build-first`, or flip status.

**Do not:**

- Fill **Assumptions** so the user has boxes to tick
- Invent Assumption asks because the design already looked clear
- Treat “needs user confirmation” as “quiz every default”
- Treat a reference-doc example as the target unless it was clearly set as the target
- Ask about the obvious path
- Leave a category enabler unstated because the user did not say it
- Invent a later-phase vendor/GIS/API as a shape fork — that is the spec, not Understanding
- De-confirm a `confirmed` Understanding as part of clean-out (sync or role) — keep status; list corrections

**Tell the user:** Confirming Understanding = **is / is not** + any remaining **real-fork** Assumptions (empty Assumptions is fine). Spec-level detail may be missing on purpose. On review, list **locks** in one line so they can override — do not dump those locks as unchecked Assumptions.

**Status**:

| Status | Meaning |
|--------|---------|
| `draft` | Agent wrote/updated; shape not approved. File **must exist** under prevent — `draft` ≠ skip creating Understanding. Draft is not a coding gate |
| `reviewed` | User skimmed; minor edits may remain |
| `confirmed` | User approved **shape** — safe to implement without re-asking Understanding review; **graduate** contract to spec (§2). Not sign-off on every spec detail |
| `superseded` | No longer accurate — revise or reconcile |

**When `confirmed`:** Read for guardrails; proceed from the spec. **Do not** re-surface for review unless shape/scope changes, conflict with code, or status returns to `draft` / `superseded`. Unchecked **Assumptions** after confirm → ask those **real forks** only — do not invent new quizzes.

**De-confirm gate (`confirmed` → `draft` / `superseded`):** Flip status **only** when a **significant shape change** is outlined — the **is / is not** identity, product surface, ownership, or a stated guardrail actually changes (a genuinely new identity → §0 **split**, not a de-confirm). An **additive** request is **not** a shape change: a new research angle, an extra behavior, an edge case, or added detail that still fits the confirmed **is / is not** → record it in the **spec** (Behavior / Acceptance / Decisions) and **keep `confirmed`**. Do **not** revert a confirmed Understanding, rewrite **is / is not**, or re-open shape review just to capture an addition. If genuinely unsure, ask one question — *does this change what the feature is, or just add to it?* — and **default to additive**.

**Reconciliation:** If code diverges from confirmed **shape**, update the spec + **Last reconciled with code**, or set `superseded` and draft a new Understanding. Run **only when** the user reports a mismatch, implementation contradicts Understanding, this session changes that feature's shape/behavior, **or** you are updating that Understanding - **not** as a session-start project-wide audit.

**On Understanding update — relocate** *(same turn, this stem only)*:

1. Trim to shape. Contract content removed from Understanding → **move into that stem’s spec** if missing, then delete from Understanding: legacy **Done when** → **Acceptance**; How-it-should-work / flows → **Behavior**; UI / screenshot tables → **Visual references** / Behavior. Do not discard; do not invent; do not park prose under **Confirmed with user**.

**When to create or update:**

- New feature/change → draft or update Understanding — set **`draft` only if the is / is not or a guardrail changed**; an **additive** item or research angle that fits the confirmed shape → **spec**, keep `confirmed` (de-confirm gate above)
- `docs/reference/` (or chat) → **build or update** live docs; create missing Document Map rows + file sets when material implies new stems. Do **not** treat examples in those files as the target unless clearly set as the target
- User asks to **clean out Assumptions** / lock obvious defaults → **offer** the clean-out pass (lock gate above)
- Plan / “how should we build this” → if `confirmed`, use as guardrails + read spec; if `draft`/missing, draft shape first
- Identity assumption becomes clear → update **What this is NOT** (identity, not backlog)
- Two unlike identities were merged into one stem → **split** (§0 one-identity rule): new row + files; move content; do not leave a frankenstein Understanding
- User corrects you → update immediately (including split/move when they clarify separate features)
- After any update → run relocate for that stem

**When planning:** Include the Understanding path; state confirmation is for **shape / guardrails**, not the full spec. Once shape implies a product surface/architecture, **lock it in is / is not** and default the spec to that **target**. Obvious defaults lock the same way (lock gate above). **Assumptions** only for real forks. Do not ask the user to remind you.

**Acceptance** lives on the **spec** (a short list of coarse, exercisable outcomes, not a padded checklist) - not on Understanding. **Visual references:** save under `docs/features/assets/`, `docs/_shared/assets/`, or `docs/reference/visuals/`; link from the **spec** with similar vs different - not from `-Understanding.md`. See [`../../help/IDEA_CAPTURE_TIPS.md`](/docs/templates/help/IDEA_CAPTURE_TIPS.md#visual-references-screenshots).

---
## Understanding author checklist


> **Opt-in.** Use only when the user asks for this role or names this file. Not always-on.

**Job:** Capture **feature shape** first (is / is not). Draft or revise `-Understanding.md` so the user can confirm **guardrails** before implementation — **not** a full spec review.

**Canonical procedure:** [`../workflow/naming-layout.md`](/docs/templates/agent/workflow/naming-layout.md) (§0) · [`../workflow/profile-standing.md`](/docs/templates/agent/workflow/profile-standing.md) (§0.1) · [`../workflow/understanding.md`](/docs/templates/agent/workflow/understanding.md) (§4 — **source of truth**, incl. de-confirm gate). Index: [`../Modular_Docs_Workflow.md`](/docs/templates/agent/Modular_Docs_Workflow.md). Template: [`../../Feature_Understanding_Template.md`](/docs/templates/Feature_Understanding_Template.md). Interview help: [`../../help/IDEA_CAPTURE_TIPS.md`](/docs/templates/help/IDEA_CAPTURE_TIPS.md). Graduation is **not** this role (§2 / [`doc-graduate.md`](/docs/templates/agent/roles/doc-graduate.md)) — except relocating trim overflow into the spec while shaping.

## When to invoke

- New idea, vague idea, or mid-build correction of **what it is**
- Chat / `docs/reference/` material → **build or update** live docs (Understanding first under **prevent** / when locking shape)
- User says: *draft Understanding*, *Understanding author*, *capture intent for X*, *lock shape for X*, *lock product shape*, *draft the product vision / end-state picture*, *build/update live docs from reference*, *clean out Assumptions*, *lock obvious assumptions*
- Under **build-first** / clear **balanced** stems: only when the user asks to lock shape or identity fights require it — do not invent Understandings for every map row
- **Not** for a purely **additive** ask on a `confirmed` stem — update the **spec**; keep `confirmed`. Invoke only on a **significant shape change**. Full gate: [`../workflow/understanding.md`](/docs/templates/agent/workflow/understanding.md) §4.

## Inputs

1. `docs/Master_Index.md` Sections 1-3 (Document Map + overview). `docs/Product-Vision.md` if it exists - if missing, draft a lightweight file to start (Workflow Section 4.5); deepen when identity is fuzzy, there are multiple stems, or the user asks to *lock product shape*. Under **build-first**, do not wait for confirm. Document only the product the docs confirm.
2. Named feature/shared row paths — or create the default file set per Workflow §0 for each **new** stem you identify
3. Source the user pointed at: this conversation, and/or files under `docs/reference/` (all named exports, or the folder when they said “from reference”)
4. Existing `-Understanding.md` for each stem you touch (if any)
5. That stem’s spec (relocate overflow on updates; when **splitting** — both old and new stems)
6. This role file + Understanding template — open [`../workflow/naming-layout.md`](/docs/templates/agent/workflow/naming-layout.md) / [`../workflow/understanding.md`](/docs/templates/agent/workflow/understanding.md) only if naming or identity/split rules are unclear

**Do not** open unrelated features, the full pack catalog, or start coding.

## Steps

1. From the sources, identify **stem(s)** — one Document Map identity each. If material clearly describes **two+ finished-feature identities** (different jobs / category / surface / ownership), plan a **split** (Workflow §0) — do not force one Understanding because they appeared in one chat or one vague sentence.
2. If identity count is ambiguous, ask brief questions from `IDEA_CAPTURE_TIPS.md` (cap **5**), then draft — prioritize identity (is / is not), including **product-defining surface** when relevant. Prefer one clarifying split question over silently merging. **Skip the facet interview** when the goal is terse but actionable (wrap a documented public API / match the upstream SDK) — record those in-scope surfaces on this stem’s **spec**. Do not add map rows for vague planned-only extras (Workflow §0 inventory). Do **not** interview obvious defaults (Workflow §4 lock gate).
3. For **each** stem: write or update `-Understanding.md` from the Understanding template + **Workflow §4** (shape sections only; human review banner; no How-it-should-work / UI / Visual references / Done when). Put product-defining surface/architecture identity **and obvious defaults** in is / is not — not module diagrams. **Assumptions = real forks only** (empty is success). Name a category input the product cannot be true without in is / is not, even when the user did not say it (Workflow §4). Do **not** treat examples in `docs/reference/` / chat as the target unless clearly set as the target. Screenshots → spec **Visual references**. Full lock gate: [`../workflow/understanding.md`](/docs/templates/agent/workflow/understanding.md) §4. If the user asked to clean Assumptions, or you already see invented quizzes on open stems, **offer** the clean-out pass (all / named / no; default yes) — execute Workflow §4 Clean-out (**keep status**; do not de-confirm). Do not silent-scan the map.
4. **New row:** add Document Map row **and** create the **profile default file set** in the **same turn** (Workflow §0 / §0.1 — spec; Understanding per profile). When this role runs, you are locking shape → create/update Understanding even under build-first for **named** stems. **Split:** create the new stem’s file set; move misplaced shape/contract content out of the old stem; relocate overflow into the spec (Workflow §4).
5. **On update (no split):** relocate overflow into the spec for that stem (Workflow §4).
6. Status **`draft`** on **new** Understandings and on updates that change **is / is not** or a guardrail because the user changed shape. After a §4 clean-out → **keep status** (do **not** de-confirm). Show the user the path(s). Ask them to correct **shape** when status is `draft` — say this is **not** a full spec review. List **locks** in one line; leave only real forks in Assumptions. If the design was already clear, **zero Assumption asks is correct** — do not invent a quiz. If you split or relocated, say so in one line. **Stop.**

## Stop when

- Each targeted stem has `-Understanding.md` at status `draft` (new / user shape change) **or** kept prior status after a §4 clean-out, and
- Splits created full default file sets + Document Map rows, and
- Contract trim was relocated into the correct stem’s spec when missing (or there was none), and
- You asked the user to review **shape** when status is `draft`, listed locks, and left only real forks in Assumptions

## Do not

- Write or modify application code
- De-confirm / rewrite **is / is not** for an additive ask, or de-confirm after clean-out — follow [`../workflow/understanding.md`](/docs/templates/agent/workflow/understanding.md) §4 (source of truth). New identity → **split** ([`../workflow/naming-layout.md`](/docs/templates/agent/workflow/naming-layout.md) §0)
- Set status to `confirmed` (only the user does that)
- Run a full post-confirm graduation pass (use [`doc-graduate.md`](/docs/templates/agent/roles/doc-graduate.md)) — **except** relocating trim overflow into the spec while shaping
- Delete durable contract detail without putting it in the spec when missing
- Add or keep How it should work, UI/UX, Visual references, or Done when on Understanding
- Ask the user to approve module/API architecture, flows, or a full behavior contract here — **do** capture product-defining surface/identity as shape when they stated it
- Encode a known-wrong interim architecture in **is / is not**
- Pad Understanding into a mini-spec; park relocated prose under **Confirmed with user**
- Invent Assumption checkboxes or treat a reference-doc example as the target unless it was clearly set as the target (Workflow §4 lock gate)
- Invent Assumption asks when the design is already clear (zero asks is correct)
- Leave a category input unstated because the user did not say it (Workflow §4)
- Ask how to handle an obvious best default
- Glue two unlike identities into one Understanding to avoid new files, “stay tight,” or because the user mentioned them together
- Wait for the user to invent paths after they said two things are different features — split and propose names
- Invent `_shared/` rows or §3.0 exceptions; audit unrelated stems
