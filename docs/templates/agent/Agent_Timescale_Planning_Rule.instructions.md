---
name: Agent Timescale Planning
description: Plan and ship at agent speed — target architecture first; no human-sprint interim milestones
applyTo: "**"
---

# Agent Timescale Planning

Coding agents complete multi-concern cuts in one focused session. Do **not** plan like a human sprint (MVP → interim architecture → later rewrite) unless product rules are still unknown. The user should not need to remind you that agent coding speed differs from human sprint sizing — apply this by default.

**When UX / feature shape is already clear** (confirmed Understanding, explicit user contract, or an unambiguous ask):

- Default to the **target architecture** that matches that contract.
- Treat stepped plans as **build/verify order inside one change**, not as permission to ship a known-wrong intermediate.
- Multi-concern work (mapping + chrome + persistence, API + UI + tests, etc.) is a normal single session — not a reason to stage an architecture that fights the UX.
- **Operable product ≠ honest library only.** When the stem is user/operator-facing, landing domain packages + offline tests without a path to exercise the contract (UI, CLI, product API, or documented smoke) is still a human-sized half-product. Prefer one cut that includes wire/surface, dual-track TODOs, or a loud **phased bridge** — not “library done = product done” while Overview/Acceptance still read as a running product. Label true foundation stems **library-only**.
- **No UI specs ≠ defer UI.** Missing mockups/wireframes is not a reason to park the surface for a human design pass. Scaffold a **minimal boring** control plane / CLI / smoke and **wire** domain into it at agent speed; iterate after something runs. Only defer when the user explicitly gates design-first / no UI / library-only.

**Lock shape early (modular docs):** Product-defining surface/architecture identity belongs in Understanding **What this is / is NOT** (or Assumptions) when the project uses Understanding (`docs_profile: prevent` / balanced when ambiguous / *lock shape*) — e.g. one continuous surface vs N editors. Under **ship-first**, put identity constraints on the **spec** (overview / Decisions) until an Understanding exists. Module/API detail stays on the **spec**. Once shape is locked, plans and TODOs must target it.

**Exploration vs shipping:**

- Optional spikes are fine while learning product rules — label them **exploration**, keep them disposable.
- Do **not** promote a spike interim to the paved path once shape is known.
- Spikes are not a required stage before an honest cut when the UX contract already implies the target.

**What is still real** (reason to lock rules, not to ship the wrong shape):

- Wrong product rules lock in fast — lock 3–4 rules when shape is ambiguous, then cut.
- Verification (tests, Docker, clicking the path) still costs wall-clock minutes.

**Examples:**

- Bad: ship N editors + caret bridging as a milestone because “range→note mapping + chrome is too big for one change.”
- Good: one High Priority item = the honest single surface; checklist bullets = verify slices only.
- Bad: “Phase 1 wrong architecture, Phase 2 correct” when the UX already implied the correct one.
- Good: optional labeled spike on a branch; land the target architecture as the default path.
- Bad: “Layer 1 engine + tests done” for a control-plane product with no UI/CLI path and open operable Acceptance.
- Bad: “UI deferred — user didn’t specify screens” while Master Index still implies an operator surface.
- Good: domain cut **plus** exercise-path TODO (or one multi-concern item); scaffold thin desk/CLI and wire it; or **library foundation first · exercise path: …** only when phased on purpose; pure libs marked **library-only**.

**With this pack’s modular docs:** If TODO / Current focus encodes an interim that fights confirmed Understanding, rewrite the TODO toward the target **before** implementing. “Tight scope” means do not wander into unrelated work or repo-wide audits — **not** “ship human-sized half-architectures,” **not** “domain checklist complete = operable product,” and **not** “all TODOs `[x]` while operable Acceptance for the claim stays open” (Workflow §5.3).
