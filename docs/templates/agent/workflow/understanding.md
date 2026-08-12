<!-- pack-version: 2.7.17 -->

> **Workflow module — source of truth** for shape vs contract (Understanding + graduation + de-confirm gate). Open from the [workflow index](../Modular_Docs_Workflow.md) when drafting/confirming Understanding, graduating to spec, or deciding additive vs shape change. Rules and roles summarize; **this file wins on conflict**.

# Understanding & graduation

## 2. Understanding → Spec graduation

**Source of truth:** This module (§2 + §4) is the canonical shape-vs-contract procedure. Rules, roles, and template Instruction blocks summarize; **this file wins on conflict**. Applies fully under **`prevent`**, and for any stem that **has** an Understanding under other profiles. Under **`ship-first`** (no Understanding), grow the **spec** directly as contract home — skip steps 1 and the Understanding half of step 3.

| File | Role | When to update |
|------|------|----------------|
| `-Understanding.md` | **Feature shape / guardrails** — is / is not, Assumptions; user confirms **shape** (not the full contract) | When the profile requires it, or user locks shape / identity is ambiguous |
| `.md` spec (feature or `_shared/`) | **Durable contract** — architecture, API, decisions, stable behavior, Acceptance, Visual references | After shape confirm (if Understanding exists); as you implement under `ship-first`; when code and docs must match |

**Workflow *(when Understanding is in play)*:**

1. Agent drafts `-Understanding.md` → user confirms **shape** (`confirmed`) — is / is not + Assumptions. **Not** a full spec sign-off.
2. Agent **graduates** durable contract into the spec: overview, architecture/contract, Behavior, **Acceptance**, **Visual references**, **Decisions**, dependencies, maturity (shared). Synthesize from Understanding **plus** conversation / decisions — do **not** only copy thin Understanding. A short Understanding is **not** permission to write a short spec. User-facing stems: Acceptance includes ≥1 **operable** outcome (§5.3).
3. After graduation, Understanding keeps only shape sections (§4). Spec = contract truth; **TODO** = living work checklist. **Same turn:** if Overview/Acceptance are product-shaped and High Priority is domain-only, apply §5.3 bridge (dual-track exercise path, phased note, or **library-only**) — do not leave product Acceptance with silent package TODOs.
4. If implementation diverges, update the spec **or** set Understanding to `superseded` and revise (§4) — do not leave both stale.

**Workflow *(ship-first / no Understanding on stem)*:** Keep a thin-but-real spec + TODO; capture lasting preferences on the spec **Decisions** table same turn (§10). Offer *lock shape* (Understanding) when identity fights start.

See [`Feature_Spec_Template.md`](../../Feature_Spec_Template.md) and [`Feature_Understanding_Template.md`](../../Feature_Understanding_Template.md).

---

## 4. Understanding (Features & Shared)

**Source of truth** with §2 — other pack files summarize; this section wins on conflict. Drafting examples: [`Feature_Understanding_Template.md`](../../Feature_Understanding_Template.md). **When required:** §0.1 docs profile.

Under **`prevent`**, each **feature** and substantial **shared component** gets a `-Understanding.md` — the agent’s model of **feature shape** (guardrails). **Not** a second durable spec. Under **`balanced`**, create when identity is ambiguous / multi-surface / split pressure / user asked. Under **`ship-first`**, only when user asks *lock shape* or the file already exists.

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
| **Assumptions** | Unchecked items needing shape confirmation | Full-spec open questions |
| **Confirmed with user** | Short correction notes + date | Relocated contract prose |

Work queue → **TODO**. Durable contract (Behavior, **Acceptance**, Visual references, architecture) → **spec** (§2).

**Tell the user:** Confirming Understanding = **is / is not** + **Assumptions** (shape). Spec-level detail may be missing on purpose.

**Status**:

| Status | Meaning |
|--------|---------|
| `draft` | Agent wrote/updated; shape not approved — **do not implement code** unless user waives. File **must exist** — `draft` ≠ skip creating Understanding |
| `reviewed` | User skimmed; minor edits may remain |
| `confirmed` | User approved **shape** — safe to implement without re-asking Understanding review; **graduate** contract to spec (§2). Not sign-off on every spec detail |
| `superseded` | No longer accurate — revise or reconcile |

**When `confirmed`:** Read for guardrails; proceed from TODO/spec. **Do not** re-surface for review unless shape/scope changes, conflict with code, or status returns to `draft` / `superseded`. Unchecked **Assumptions** after confirm → ask those items only.

**De-confirm gate (`confirmed` → `draft` / `superseded`):** Flip status **only** when a **significant shape change** is outlined — the **is / is not** identity, product surface, ownership, or a stated guardrail actually changes (a genuinely new identity → §0 **split**, not a de-confirm). An **additive** request is **not** a shape change: a new research angle, an extra behavior, an edge case, or added detail that still fits the confirmed **is / is not** → record it in the **spec** (Behavior / Acceptance / Decisions) and/or a **TODO** item and **keep `confirmed`**. Do **not** revert a confirmed Understanding, rewrite **is / is not**, or re-open shape review just to capture an addition. If genuinely unsure, ask one question — *does this change what the feature is, or just add to it?* — and **default to additive**.

**Reconciliation:** If code diverges from confirmed **shape**, update the spec + **Last reconciled with code**, or set `superseded` and draft a new Understanding. Run **only when** the user reports a mismatch, implementation contradicts Understanding, this session changes that feature’s shape/behavior, **or** you are updating that Understanding — **not** as a session-start repo-wide audit.

**On Understanding update — relocate + TODO** *(same turn, this stem only)*:

1. Trim to shape. Contract content removed from Understanding → **move into that stem’s spec** if missing, then delete from Understanding: legacy **Done when** → **Acceptance**; How-it-should-work / flows → **Behavior**; UI / screenshot tables → **Visual references** / Behavior. Do not discard; do not invent; do not park prose under **Confirmed with user**.
2. Open that stem’s `-TODO.md`; compare `[x]` items to destination (Understanding + spec) and code. **Uncheck** mismatches; reopen items / refresh **Current focus** when work reopened. Optionally align spec **Acceptance** the same way — never recreate Done when on Understanding.

**When to create or update:**

- New feature/change → draft or update Understanding — set **`draft` only if the is / is not or a guardrail changed**; an **additive** item or research angle that fits the confirmed shape → **spec + TODO**, keep `confirmed` (de-confirm gate above)
- `docs/reference/` (or chat) → **build or update** live docs; create missing Document Map rows + file sets when material implies new stems
- Plan / “how should we build this” → if `confirmed`, use as guardrails + read spec; if `draft`/missing, draft shape first
- Identity assumption becomes clear → update **What this is NOT** (identity, not backlog)
- Two unlike identities were merged into one stem → **split** (§0 one-identity rule): new row + files; move content; do not leave a frankenstein Understanding
- User corrects you → update immediately (including split/move when they clarify separate features)
- After any update → run relocate + TODO check for that stem

**When planning:** Include the Understanding path; state confirmation is for **shape / guardrails**, not the full spec. Once shape implies a product surface/architecture, **lock it in is / is not** (or Assumptions) and default TODOs/plans to that **target** (agent timescale — not MVP → interim → rewrite). Stepped bullets = build/verify order inside one cut. Do not ask the user to remind you.

**Acceptance** lives on the **spec** (usually 3–7 coarse outcomes) — not on Understanding. **Visual references:** save under `docs/features/assets/`, `docs/_shared/assets/`, or `docs/reference/visuals/`; link from the **spec** with similar vs different — not from `-Understanding.md`. See [`../help/IDEA_CAPTURE_TIPS.md`](../../help/IDEA_CAPTURE_TIPS.md#visual-references-screenshots).

---
