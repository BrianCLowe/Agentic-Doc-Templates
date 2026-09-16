> **Workflow module — source of truth** for shape vs contract (Understanding + graduation + de-confirm gate). Open from the [workflow index](../Modular_Docs_Workflow.md) when drafting/confirming Understanding, graduating to spec, or deciding additive vs shape change. Rules and roles summarize; **this file wins on conflict**.

# Understanding & graduation

## 2. Understanding → Spec graduation

**Source of truth:** This module (§2 + §4) is the canonical shape-vs-contract procedure. Rules and roles summarize; live scaffolds are fill-in blanks. **This file wins on conflict**. Applies fully under **`prevent`**, and for any stem that **has** an Understanding under other profiles. Under **`ship-first`** (no Understanding), grow the **spec** directly as contract home — skip steps 1 and the Understanding half of step 3.

| File | Role | When to update |
|------|------|----------------|
| `-Understanding.md` | **Feature shape / guardrails** — is / is not, Assumptions; user confirms **shape** (not the full contract) | When the profile requires it, or user locks shape / identity is ambiguous |
| `.md` spec (feature or `_shared/`) | **Durable contract** — architecture, API, decisions, stable behavior, Acceptance, Visual references | After shape confirm (if Understanding exists); as you implement under `ship-first`; when code and docs must match |

**Workflow *(when Understanding is in play)*:**

1. Agent drafts `-Understanding.md` → user confirms **shape** (`confirmed`) — is / is not + any remaining **real-fork** Assumptions (empty is fine). **Not** a full spec sign-off. Lock obvious defaults; do not invent quizzes (lock gate in §4).
2. Agent **graduates** durable contract into the spec: overview, architecture/contract, Behavior, **Acceptance**, **Visual references**, **Decisions**, dependencies, maturity (shared). Synthesize from Understanding **plus** conversation / decisions — do **not** only copy thin Understanding. A short Understanding is **not** permission to write a short spec. Do **not** omit confirmed Behavior / Acceptance / Visuals to “keep the pack lean” — lean is Understanding shape + no padding, not dropping contract callers need. Acceptance is usually **3–7** coarse outcomes, not a High Priority twin (§5.3). User-facing stems: Acceptance includes ≥1 **operable** outcome (§5.3).
3. After graduation, Understanding keeps only shape sections (§4). Spec = contract truth; **TODO** = living work checklist. **Same turn:** if Overview/Acceptance are product-shaped and High Priority is domain-only, apply §5.3 bridge (dual-track exercise path, phased note, or **library-only**) — do not leave product Acceptance with silent package TODOs. **In-scope spec surfaces** (kit leftovers on this stem) need covering TODOs on an **existing** stem (§5.4) — a complete spec is **not** permission to omit the backlog “until someone picks it up,” and is **not** a reason to add empty map rows (§0 inventory).
4. If implementation diverges, update the spec **or** set Understanding to `superseded` and revise (§4) — do not leave both stale.

**Workflow *(ship-first / no Understanding on stem)*:** Keep a thin-but-real spec + TODO; capture lasting preferences on the spec **Decisions** table same turn (§10). Offer *lock shape* (Understanding) when identity fights start.

See [`Feature_Spec_Template.md`](../../Feature_Spec_Template.md) and [`Feature_Understanding_Template.md`](../../Feature_Understanding_Template.md).

---

## 4. Understanding (Features & Shared)

**Source of truth** with §2 — other pack files summarize; this section wins on conflict. Live `-Understanding.md` files are **fill-in blanks** ([`Feature_Understanding_Template.md`](../../Feature_Understanding_Template.md)). Teaching examples live **here**, not in the scaffold. Human review: [`../../help/SCAFFOLDS.md`](../../help/SCAFFOLDS.md). **When required:** §0.1 docs profile. **Compaction / thin context:** re-open this module before drafting or editing Understanding — do not reconstruct the gate from memory.

Under **`prevent`**, each **feature** and substantial **shared component** gets a `-Understanding.md` — the agent’s model of **feature shape** (guardrails). **Not** a second durable spec. Under **`balanced`**, create when identity is ambiguous / multi-surface / split pressure / user asked. Under **`ship-first`**, only when user asks *lock shape* or the file already exists.

**Whole product:** Feature is / is not is **one stem**. The cohesive end-state lives in `docs/Product-Vision.md` when that file exists — [`product-vision.md`](product-vision.md) §4.5. A feature that fights a **confirmed** product vision is a shape fight — do not implement it. Do not paste the product vision into every Understanding.

- Features: `features/FeatureName-Understanding.md`
- Shared: `_shared/ComponentName-Understanding.md`

**Who writes it:** Agent drafts first (`draft`) from conversation, design doc, or interview. User **reviews and corrects shape** — they do not author from scratch and are **not** approving the full contract here.

**Default under prevent:** Same Understanding for shared components as features. **Only skip** when the user **explicitly** excepts it (Master Index §3.0) **or** project `docs_profile` is `ship-first` / `balanced` allows skip. Under prevent, missing files or convenience are not exceptions.

**Shape sections only** (keep these; nothing else):

| Section | Put here | Do not put here |
|---------|----------|-----------------|
| **What this is** | Identity-defining user detail: category, metaphors, naming, “feels like,” ownership, product-defining constraints **and surface/architecture identity** (e.g. one continuous surface). Prefer user’s words. Brief feel/layout only if it defines the product. | Flows, module/API diagrams, edge matrices, acceptance lists, How-it-should-work, Core Behavior rewrite, padding/speculation |
| **What this is NOT** | Finished-feature **identity** boundaries (wrong category, wrong product surface/architecture, ownership) | Deferred phases, “not built yet,” backlog, or “NOT the final architecture yet” excuses — those → TODO / Current focus / spec roadmap |
| **Relationship** | Extends / wraps / reuses vs greenfield | Foundation task lists |
| **Assumptions** | **Real forks only** — two live alternatives with no obvious winner | Invented decisions, obvious defaults, examples-as-picks, full-spec open questions |
| **Confirmed with user** | Short correction notes + date | Relocated contract prose |

Work queue → **TODO**. Durable contract (Behavior, **Acceptance**, Visual references, architecture) → **spec** (§2).

**Drafting size — What this is**

Length matches the shape detail the user gave — not a telegram summary, and not a parallel feature narrative.

- *Too thin (drops shape):* “A role-specific view of the existing text editor.”
- *Right size (shape):* Same framing **plus** identity they actually gave — e.g. same editing core (not a second engine); one continuous surface vs N separate editors; chrome differs for this workflow; metaphors / “feels like”; product-defining constraints. Not implementation steps, prop tables, happy-path numbered flows, or a full behavior rewrite.
- *Wrong size (mini-spec):* Restating Core Behavior, API/prop tables, scene-break matrices, acceptance checklists, How-it-should-work flows, or every edge case — that belongs in the **spec** / **TODO**.

Product-defining surface / architecture belongs in **What this is** when it decides identity — e.g. “one continuous manuscript surface; seams are visual; notes stay separate storage.” Once confirmed, plan/build that **target** — do not park a fighting interim as the paved path.

**Drafting size — What this is NOT**

Identity boundaries for the **finished** feature. Do **not** list work that is still planned, phased later, or “not implemented yet.”

- *Bad (do not write):* “NOT freeform multi-window Desktop Mode — that is long-term in the spec.” That is deferred work for the same feature, not an identity boundary.
- *Good:* “NOT a freeform multi-window desktop OS — Main Workspace is a document-centric layout (panels / side-by-side), not overlapping OS windows.” *(Only if that is truly never what this feature is meant to be.)*
- *Wrong-engine:* “NOT a second editor engine — same editing core as BlockEditor; this stem is role chrome / a different surface on that core.”

### Lock gate — obvious defaults vs real forks

**Source of truth** for this gate — rules and roles summarize; **this subsection wins on conflict**. Compaction / thin context: re-open this module; do not reconstruct from the scaffold.

Agents invent decisions, then either lock the invention as identity or dump it into **Assumptions** so the user has boxes to check. That is the failure. **Empty Assumptions is success** when every default was the obvious best.

**No-ask proviso:** If the design is already clear (conversation / `docs/reference/` already gives category, is / is not, and the obvious defaults), **zero Assumption asks is correct.** Do not invent a quiz so the user has something to confirm. Shape review may be is / is not only.

| Do | Do not |
|----|--------|
| **Lock the obvious** into **What this is / is NOT** (identity) or a one-line lock on review | Put an obvious best default under **Assumptions** and ask “how should this be handled?” |
| Leave **Assumptions** for **real forks only** | Invent a vendor, jurisdiction, schema, comparison row, or label set the user did not pick — then quiz it |
| Treat chat / `docs/reference/` walkthroughs as **examples**, not the target, unless the user **clearly set them as the target** | Encode a reference example as identity, a vendor pick, a jurisdiction, or a spec constraint |
| Ask about a **lesser path** only when a **real non-timescale reason** exists (hard blocker, legal, missing credential, named constraint) | Propose an MVP / half-measure / interim cut “to land 10 minutes faster,” or silently take a lesser path |

**Lock the obvious.** A default is obvious when it is the standard for the product category, an already-stated constraint, or the cheaper/simpler path that still hits the target — and the user did not contradict it. Write it into **is / is not**. Do **not** ask. On shape review, list what you locked in **one line** so they can override.

**Real fork.** Two (or more) live alternatives with **no** obvious winner from the conversation, the category, or the constraints (paid data vs free tables; which third-party API family; journey order when both placements are plausible). Those stay unchecked **Assumptions**. Spec-level open questions still do **not** belong here.

**Examples are not the target** unless the user **clearly set them as the target**. A walkthrough, sample project, named vendor, or place in chat / `docs/reference/` is how they explained the idea — not product identity, not a pick, not a jurisdiction. Do **not** write it into **is / is not** or the spec. Do **not** offer it back as a fork. Only lock it if they said this *is* the product, the pick, or the scope.

- *Bad (example → target):* Reference docs walk a timber-frame lot in VA/WV to explain home design. Agent writes a timber-frame / Virginia product, or asks whether that sample is the flagship.
- *Good:* “A home-design app for anywhere in the US first. User location sets jurisdiction.” The timber-frame VA/WV lot stays an example. No named 3D vendor unless they clearly picked one.
- *Bad (invented quiz):* “Energy Star vs other efficiency labels?” when Energy Star is the obvious US residential catalog flag. “Should defaults be user-editable?” when editable is the obvious consumer path.
- *Good (lock):* Energy Star locked in **is / is not**. Defaults are user-editable. Assumptions stay empty unless a real fork remains.
- *Good (real fork):* “Cost tables: free/manual vs paid RSMeans-class.” “Utility tables vs live APIs.” Those have no obvious winner without a budget or integration choice.
- *Lesser path ≠ faster MVP.* Do **not** offer a thinner cut, interim architecture, or half-measure to save a human sprint or “land something in 10 minutes.” That is agent-timescale ([`Agent_Timescale_Planning_Rule.mdc`](../Agent_Timescale_Planning_Rule.mdc)) — lock the obvious **full** target; stepped bullets are build/verify order, not permission to ship a known-wrong intermediate. PDF-first as the consumer handoff is a **lock**; IFC stays a covering TODO. Do not ask “PDF-only MVP first?”
- *Lesser-path ask (only with a real reason):* A hard external constraint, not speed — e.g. “A claimed-passing energy worksheet needs a licensed stamp we do not have. I locked not-stamp-ready flags. Do you actually want a claimed-passing worksheet (legally worse)?”
- *Do not ask:* “Which jurisdiction should we use?” / “How should Energy Star be handled?” / “Is the reference walkthrough the product?” / “Ship a thinner MVP so we finish faster?” Those quiz the obvious path, promote an example into a target, or apply human-sprint sizing to agent work.

**Clean-out pass:** Existing Understandings (and specs that copied a reference example as a constraint) get the same gate. **Offer** it — all Document Map Understanding stems / named / no; default yes. Sync tag `optional-assumption-cleanout` ([`TEMPLATE_SYNC_B.md`](../TEMPLATE_SYNC_B.md)). Mid-session: if the user is correcting invented decisions or you already see dirty Assumptions on open stems, offer the same pass. Do **not** silent-scan the whole map without that offer or the tagged sync execute.

On execute (chosen stems that **have** Understanding):

1. Lock obvious defaults that sit as unchecked Assumptions into **is / is not**.
2. Delete Assumption bullets that are invented quizzes, obvious defaults, or reference examples treated as forks.
3. If **is / is not** (or the spec) treated a reference example as the target and it was **not** clearly set as the target → restore category-level identity. **Keep status** — do **not** de-confirm (`confirmed` → `draft`) and do **not** inject a mid-sync shape quiz. Record the correction under **Confirmed with user** and in the sync / review summary.
4. Leave **real forks** unchecked. Empty Assumptions is success. One-line lock list under **Confirmed with user**.
5. Heading → `Assumptions (real forks only)` if it still says “needs user confirmation.”
6. Do **not** invent new Assumptions, new stems, Understanding on `ship-first`, lesser-path asks that re-offer a reference example, or flip status.

**Do not:**

- Fill **Assumptions** so the user has boxes to tick
- Invent Assumption asks because the design already looked clear
- Treat “needs user confirmation” as “quiz every default”
- Treat a reference-doc example as the target unless it was clearly set as the target
- Ask about the obvious path
- Silently take a lesser path, or **offer** a lesser path to go faster (no real reason)
- Invent a later-phase vendor/GIS/API as a shape fork — that is TODO / spec, not Understanding
- De-confirm a `confirmed` Understanding as part of clean-out (sync or role) — keep status; list corrections

**Tell the user:** Confirming Understanding = **is / is not** + any remaining **real-fork** Assumptions (empty Assumptions is fine). Spec-level detail may be missing on purpose. On review, list **locks** in one line so they can override — do not dump those locks as unchecked Assumptions.

**Status**:

| Status | Meaning |
|--------|---------|
| `draft` | Agent wrote/updated; shape not approved — **do not implement code** unless user waives. File **must exist** — `draft` ≠ skip creating Understanding |
| `reviewed` | User skimmed; minor edits may remain |
| `confirmed` | User approved **shape** — safe to implement without re-asking Understanding review; **graduate** contract to spec (§2). Not sign-off on every spec detail |
| `superseded` | No longer accurate — revise or reconcile |

**When `confirmed`:** Read for guardrails; proceed from TODO/spec. **Do not** re-surface for review unless shape/scope changes, conflict with code, or status returns to `draft` / `superseded`. Unchecked **Assumptions** after confirm → ask those **real forks** only — do not invent new quizzes.

**De-confirm gate (`confirmed` → `draft` / `superseded`):** Flip status **only** when a **significant shape change** is outlined — the **is / is not** identity, product surface, ownership, or a stated guardrail actually changes (a genuinely new identity → §0 **split**, not a de-confirm). An **additive** request is **not** a shape change: a new research angle, an extra behavior, an edge case, or added detail that still fits the confirmed **is / is not** → record it in the **spec** (Behavior / Acceptance / Decisions) and/or a **TODO** item and **keep `confirmed`**. Do **not** revert a confirmed Understanding, rewrite **is / is not**, or re-open shape review just to capture an addition. If genuinely unsure, ask one question — *does this change what the feature is, or just add to it?* — and **default to additive**.

**Reconciliation:** If code diverges from confirmed **shape**, update the spec + **Last reconciled with code**, or set `superseded` and draft a new Understanding. Run **only when** the user reports a mismatch, implementation contradicts Understanding, this session changes that feature’s shape/behavior, **or** you are updating that Understanding — **not** as a session-start repo-wide audit.

**On Understanding update — relocate + TODO** *(same turn, this stem only)*:

1. Trim to shape. Contract content removed from Understanding → **move into that stem’s spec** if missing, then delete from Understanding: legacy **Done when** → **Acceptance**; How-it-should-work / flows → **Behavior**; UI / screenshot tables → **Visual references** / Behavior. Do not discard; do not invent; do not park prose under **Confirmed with user**.
2. Open that stem’s `-TODO.md`; compare `[x]` items to destination (Understanding + spec) and code. **Uncheck** mismatches; reopen items / refresh **Current focus** when work reopened. Optionally align spec **Acceptance** the same way — never recreate Done when on Understanding.

**When to create or update:**

- New feature/change → draft or update Understanding — set **`draft` only if the is / is not or a guardrail changed**; an **additive** item or research angle that fits the confirmed shape → **spec + TODO**, keep `confirmed` (de-confirm gate above)
- `docs/reference/` (or chat) → **build or update** live docs; create missing Document Map rows + file sets when material implies new stems. Do **not** treat examples in those files as the target unless clearly set as the target
- User asks to **clean out Assumptions** / lock obvious defaults → **offer** the clean-out pass (lock gate above)
- Plan / “how should we build this” → if `confirmed`, use as guardrails + read spec; if `draft`/missing, draft shape first
- Identity assumption becomes clear → update **What this is NOT** (identity, not backlog)
- Two unlike identities were merged into one stem → **split** (§0 one-identity rule): new row + files; move content; do not leave a frankenstein Understanding
- User corrects you → update immediately (including split/move when they clarify separate features)
- After any update → run relocate + TODO check for that stem

**When planning:** Include the Understanding path; state confirmation is for **shape / guardrails**, not the full spec. Once shape implies a product surface/architecture, **lock it in is / is not** and default TODOs/plans to that **target** (agent timescale — not MVP → interim → rewrite). Obvious defaults lock the same way (lock gate above). **Assumptions** only for real forks. Stepped bullets = build/verify order inside one cut. Do not ask the user to remind you.

**Acceptance** lives on the **spec** (usually 3–7 coarse outcomes) — not on Understanding. **Visual references:** save under `docs/features/assets/`, `docs/_shared/assets/`, or `docs/reference/visuals/`; link from the **spec** with similar vs different — not from `-Understanding.md`. See [`../help/IDEA_CAPTURE_TIPS.md`](../../help/IDEA_CAPTURE_TIPS.md#visual-references-screenshots).

---
