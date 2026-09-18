# How to Use These Templates

Day-to-day workflows after setup. First-time install: [`SETUP.md`](SETUP.md). What each live file is for: [`SCAFFOLDS.md`](SCAFFOLDS.md). Describing ideas in plain language: [`IDEA_CAPTURE_TIPS.md`](IDEA_CAPTURE_TIPS.md).

---

## The loop

Depends on **docs profile** in `docs/ADT-settings.yaml` — a first-class choice ([Workflow §0.1](../agent/workflow/profile-standing.md#01-docs-profile-ceremony-modes)). **`ship-first`** is the right default for typed APIs / CRUD. **`prevent`** is the right default for editors / games / multi-surface (and the fallback if unset):

1. You capture ideas (recommended: chat exports in `docs/reference/`, or a mid-build correction in chat).
2. **`prevent` (default):** agent drafts `Product-Vision.md` (whole-product end-state) **and** `-Understanding.md` (per-feature shape); you confirm both before code. **`ship-first`:** agent drafts thin **spec + TODO** plus a lightweight `Product-Vision.md` (destination, **not a gate**). **`balanced`:** always a lightweight Product-Vision; Understanding when identity is ambiguous; deepen the vision when 2+ stems, the whole is fuzzy, or you *lock product shape*.
3. When Understanding is used: **you confirm shape** — is / is *not* + any remaining **real-fork** Assumptions (empty is fine; not a full-spec review). Under **prevent**, confirm **Product-Vision** as one product (end-state picture), not a feature list. Under **ship-first**, confirm vision only after *lock product shape*. Agents should lock obvious defaults and not treat examples in `docs/reference/` as the target unless you clearly set them as the target.
4. Durable contract lives on the **spec**; work continues from TODOs (**Current focus** for session handoff). Under ship-first, grow the spec as you build; use *lock shape for X* if identity fights start. *Lock product shape* only when the whole product needs a confirm gate. A new session starts with **docs freshness** (`git status` + worktrees) before treating those files as current ([Workflow §0.3](../agent/workflow/session-freshness.md)).

### Recommended practice — chat exports in `reference/`

Work ideas out in chat (Grok.com, ChatGPT, …), **export** threads to markdown, and drop them in **`docs/reference/`** — often many files as you explore different aspects. That raw trail keeps **whys and motives** that polished design docs often lose. Then ask the agent to draft Understandings from those files. Details: [Recommended: export idea chats](IDEA_CAPTURE_TIPS.md#recommended-export-idea-chats-into-docsreference). Optional helper: [AI Exporter](https://saveai.net/) (Markdown + **timestamps** so agents can tell which decisions are newer **across** different conversation exports; not required).

Short asks are enough. Prefer full messy exports over a cleaned summary when you have them.

---

## Pattern 1 — Long chat → documentation *(via export)*

**When:** Brainstorming in Grok, ChatGPT, Claude web, etc.

1. **Export** the thread(s) to markdown (keep the full messy conversation).
2. After the project has `docs/reference/` (bootstrap creates it), drop the exports there.
3. Ask:

> Build or update the live docs from `docs/reference/`.

Do **not** attach a chat-only `AGENT.md` in the web UI for this pack right now — that path is paused; export is the supported route ([`IDEA_CAPTURE_TIPS.md`](IDEA_CAPTURE_TIPS.md#recommended-export-idea-chats-into-docsreference)).

With an IDE already open on the repo, you can also say:

> Using `docs/templates/`, create project documentation from our conversation so far. Do not invent features we did not talk about.

Your job is to correct wrong **identity** assumptions — not to write Understanding from scratch.

---

## Pattern 2 — Idea mid-development

**When:** Already building; a new idea or scope change appears.

> New idea: [brief]. Add it to the docs — draft Understanding + TODO; I'll review.

*(Under **ship-first**, say *spec + TODO* instead of Understanding, or *lock shape* if you want the prevent gate for that stem.)*

> Update `RoleEditor-Understanding.md` — fix What this is NOT: separate UI on the existing editor, not a new editor engine.

Docs stay the living record so the next session does not re-derive from chat alone.

---

## Pattern 3 — `docs/reference/` exports → modular docs *(recommended)*

**Preferred:** drop **chat exports** (markdown dumps from Grok.com / ChatGPT / etc.) into `docs/reference/` as you go — several files is normal. Optionally add a polished design doc too; do not delete the chats that produced it.

**Simple ask** (new or already-started docs):

> Build or update the live docs from `docs/reference/`.

That covers first-time build and later drops of new exports. Point at named files if you only want a subset:

> Build or update live docs from `docs/reference/combat-feel-chat.md` and `docs/reference/inventory-thread.md`.

Agents should split unlike **finished-feature identities** on their own (Workflow / Understanding author) — you should not need to remind them every time. If they still merge two features, correct shape once. Leftover **methods of one kit** should stay as TODOs on the inventory stem (not a stack of empty spec files) — but those TODOs **should exist** so *orchestrate* can drain them. A terse “wrap this public API” is **actionable** (agent diffs docs vs code); vague planned-only extras do **not** get map rows.

Polished PRD-only path still works:

> Read `docs/reference/Original_Design.md`. Convert into modular docs. Keep the original in `reference/`. Prefer also keeping any chat export that led to it.

---

## Pattern 4 — Bootstrap (first time in a repo)

Copy `docs/templates/`, then:

> Bootstrap modular docs using `docs/templates/agent/BOOTSTRAP.md`.

Full copy-vs-whole-repo notes and layout: [`SETUP.md`](SETUP.md). Optional rules: [`RULE_INSTALL.md`](../agent/RULE_INSTALL.md).

---

## Pattern 5 — Update templates from upstream

> Update the doc templates from Agentic Doc Templates and sync our live docs.

Agent overwrites `docs/templates/` ([`TEMPLATE_SYNC_A.md`](../agent/TEMPLATE_SYNC_A.md)), then runs catch-up **from→to** via [`TEMPLATE_SYNC_B.md`](../agent/TEMPLATE_SYNC_B.md) — union Live impact tags across the jump (D18), not the top [`CHANGELOG.md`](../CHANGELOG.md) entry only. The sync summary lists **from→to** and the **unioned** tags that ran. Optional passes that sit in the tag table but were not tagged in this jump are not “skipped instructions.” `auto-all` means execute unioned tagged passes on all stems — not run every catalog row. Procedure and tagged optional passes: [`TEMPLATE_SYNC_B.md`](../agent/TEMPLATE_SYNC_B.md). Entry: [`TEMPLATE_SYNC.md`](../agent/TEMPLATE_SYNC.md) (in the pack since **1.2**; A/B split in **2.6.8**).

**Before 1.2:** If `docs/templates/agent/TEMPLATE_SYNC.md` is missing, copy/replace `docs/templates/` from this repo once (or ask the agent to), then use the sync ask for later updates.

Version check only: *Check for template updates.* — [`TEMPLATE_UPDATE_CHECK.md`](../agent/TEMPLATE_UPDATE_CHECK.md).

---

## Pattern 6 — New machine / tooling

Keep `docs/Tooling.md` accurate. On a new machine:

> Install the project tooling for this machine.

---

## Pattern 7 — Human inbox

Anything only you can close → `docs/Human-TODO.md`: procure, playtest/feel, decide/sign-off, external waiting. Agent **dual-writes** (owner feature TODO + inbox row). You work the Open list; tell the agent in chat when done or with feedback.

> What’s left on the human TODO?

> Checked Score Target — 10k feels a bit short.

> Human TODO: done Tutorial walkthrough.

> Decided Default theme — keep Dev for boot.

> Still waiting on Steam; leave it open.

> Add Azure Bot registration to Human-TODO — we’re blocked.

> I’ll take the Score Target playtest.

> Assign playtest to QA.

> Apply defaults to Open.

> Enable team inbox.

> Add the team — you open the roster PR.

> Put me on the roster as Alex.

> I'm Sam — I take decide and procure.

> You are the QA bot — add yourself to the team roster.

> Add the nightly auditor as report-only.

> Update the QA bot’s jobs — they don’t close playtest.

> What’s on the team roster?

---

## Prompt cheat sheet

| Goal | Say something like |
|------|-------------------|
| Chat → docs | *Build or update the live docs from `docs/reference/`.* *(export threads there first)* |
| New idea | *Add [idea] to the docs — draft Understanding + TODO; I'll review.* *(ship-first: spec + TODO; or *lock shape for X*)* |
| Product vision | *Lock product shape.* / *Draft the end-state picture.* / *What’s the product vision?* |
| Fix misunderstanding | *Update [Feature]-Understanding.md — especially What this is NOT.* |
| UI screenshot | *Save to `docs/features/assets/`, add Visual references on the **spec** (similar vs different).* |
| Vague idea | *Interview me using IDEA_CAPTURE_TIPS.md, then draft [Feature]-Understanding.md.* |
| Chat exports → docs | *Build or update the live docs from `docs/reference/`.* |
| Design doc | *Convert `docs/reference/[file]` to modular docs; keep original (and any chat export) in reference/.* |
| Bootstrap | *Bootstrap modular docs using `docs/templates/agent/BOOTSTRAP.md`.* |
| Install rule | *Follow `docs/templates/agent/RULE_INSTALL.md` for [tool].* |
| Sync pack | *Update the doc templates from Agentic Doc Templates and sync our live docs.* |
| Sync mode | *Set sync to auto.* / *Set sync to auto-all.* / *Set sync to choose.* *(recorded in `docs/ADT-settings.yaml`)* |
| Update-check cadence | *Check for template updates every session.* / *Only check every week.* |
| Optional role — intent | *Draft Understanding for [Feature] from what I said — I’ll review.* (main agent delegates if subagents installed) |
| Optional role — build | *Continue from Current focus.* *(single slice)* |
| Optional role — orchestrate | *Orchestrate — clear ready TODOs until blocked.* *(parent loop; git from `orchestrator.git.mode` — recommend milestone-pr; Cloud Agent this-runs milestone-pr if durable is local-oriented or `branch-pr` / `branch-pr-squash`; per-milestone: several related TODOs + concurrent implementers when they do not overlap **and** the host can isolate → build-verify → warden → squash → ready → wait CI/Bugbot → merge → next branch; already-in-a-host-worktree → stay; Human-TODO verify map)* |
| Optional role — todo warden | *Todo warden — reconcile TODOs vs what shipped.* / *Todo cleanup — move completed items to Completed.* *(docs-only; honesty caps; hygiene moves finished `[x]`; named leftovers get covering TODOs — no vendor-doc fetch)* |
| Set orchestrator git | *Set orchestrator git to milestone-pr* / *branch-pr-squash* / *branch-pr* / *current-push* / *local* |
| Standing playbook override | *Add standing note: always squash before mark ready.* / *From now on, merge each slice after CI.* *(agent should save without being asked twice — only playbook overrides, not random notes)* |
| Optional role — verify | *Verify that unit against Understanding and the spec.* |
| Optional role — graduate | *Understanding confirmed — graduate to the spec.* |
| Force a subagent | `/understanding-author` … *(optional; usually unnecessary)* |
| Tooling | *Install the project tooling for this machine.* |
| Human TODO | *What’s left on the human TODO?* / *Checked [item] — [feedback].* / *I’ll take [item].* / *Assign playtest to QA.* / *Apply defaults to Open.* |
| Team roster | *Enable team inbox.* / *Add the team — you open the roster PR.* / *Put me on the roster as Alex.* / *I'm Sam — I take decide and procure.* / *You are the QA bot.* / *Add [bot] as report-only.* / *Update [bot]’s jobs / anti-jobs.* / *What’s on the team roster?* |

Optional roles (opt-in, never always-on): [`../agent/roles/README.md`](../agent/roles/README.md). Tool install paths: [`USING_WITH_AGENTS.md`](USING_WITH_AGENTS.md).

---

## What good output looks like

| Path | Role |
|------|------|
| `docs/Master_Index.md` | Entry point + Document Map |
| `docs/Product-Vision.md` | Whole-product end-state picture (always created; ship-first = destination until *lock product shape*) |
| `docs/features/FeatureName-Understanding.md` | Shape only — is / is not, Relationship, real-fork Assumptions (not full-spec review) |
| `docs/features/FeatureName.md` | Durable contract after shape confirm |
| `docs/features/FeatureName-TODO.md` | Tasks + **Current focus** |
| `docs/_shared/…` | Only for truly shared project pieces (may be empty) |
| `docs/Tooling.md` / `docs/Human-TODO.md` | Machine tools / human inbox (procure · playtest · decide · waiting) |
| `docs/Team-Roster.md` | Optional team inbox roster (Name / Jobs / Anti-jobs if defined; only when enabled — named humans and bots self-ID; one initial PR; coding agents do not invent) |
| `docs/reference/` | Source materials (not the living map) |
| `docs/templates/` | Upstream pack — not live feature content |

Start with Master Index + one feature; grow as ideas arrive.
