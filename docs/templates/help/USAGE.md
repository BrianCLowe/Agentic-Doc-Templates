# How to Use These Templates

Day-to-day workflows after setup. First-time install: [`SETUP.md`](SETUP.md). Describing ideas in plain language: [`IDEA_CAPTURE_TIPS.md`](IDEA_CAPTURE_TIPS.md).

---

## The loop

Depends on **docs profile** in `docs/ADT-settings.yaml` (`prevent` default if unset — [Workflow §0.1](../agent/workflow/profile-standing.md#01-docs-profile-ceremony-modes)):

1. You capture ideas (recommended: chat exports in `docs/reference/`, or a mid-build correction in chat).
2. **`prevent` (default):** agent drafts `-Understanding.md` (shape / guardrails). **`ship-first`:** agent drafts thin **spec + TODO** only. **`balanced`:** Understanding when identity is ambiguous.
3. When Understanding is used: **you confirm shape** — is / is *not* + **Assumptions** (not a full-spec review).
4. Durable contract lives on the **spec**; work continues from TODOs (**Current focus** for session handoff). Under ship-first, grow the spec as you build; use *lock shape for X* if identity fights start.

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

Agents should split unlike identities on their own (Workflow / Understanding author) — you should not need to remind them every time. If they still merge two features, correct shape once.

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

Agent overwrites `docs/templates/` ([`TEMPLATE_SYNC_A.md`](../agent/TEMPLATE_SYNC_A.md)), then follows the top [`CHANGELOG.md`](../CHANGELOG.md) entry via [`TEMPLATE_SYNC_B.md`](../agent/TEMPLATE_SYNC_B.md) (usually versions + Master Index — not every feature file). Entry: [`TEMPLATE_SYNC.md`](../agent/TEMPLATE_SYNC.md) (in the pack since **1.2**; A/B split in **2.6.8**).

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

> Still waiting on Steam; leave it open.

> Add Azure Bot registration to Human-TODO — we’re blocked.

---

## Prompt cheat sheet

| Goal | Say something like |
|------|-------------------|
| Chat → docs | *Build or update the live docs from `docs/reference/`.* *(export threads there first)* |
| New idea | *Add [idea] to the docs — draft Understanding + TODO; I'll review.* *(ship-first: spec + TODO; or *lock shape for X*)* |
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
| Optional role — orchestrate | *Orchestrate — clear ready TODOs until blocked.* *(parent loop; git from `orchestrator.git.mode` — recommend branch-pr-squash; Cloud Agent this-runs squash-PR if durable is local-oriented; close-out: build-verify → todo-warden → squash? → mark ready; Human-TODO verify map)* |
| Optional role — todo warden | *Todo warden — reconcile TODOs vs what shipped.* / *Todo cleanup — move completed items to Completed.* *(docs-only; honesty caps; hygiene moves finished `[x]`)* |
| Set orchestrator git | *Set orchestrator git to branch-pr-squash* / *branch-pr* / *current-push* / *local* |
| Standing workflow note | *Add standing note: always squash before mark ready.* / *From now on, don’t open draft PRs until verify is green.* *(agent should save without being asked twice)* |
| Optional role — verify | *Verify that unit against Understanding and the spec.* |
| Optional role — graduate | *Understanding confirmed — graduate to the spec.* |
| Force a subagent | `/understanding-author` … *(optional; usually unnecessary)* |
| Tooling | *Install the project tooling for this machine.* |
| Human TODO | *What’s left on the human TODO?* / *Checked [item] — [feedback].* |

Optional roles (opt-in, never always-on): [`../agent/roles/README.md`](../agent/roles/README.md). Tool install paths: [`USING_WITH_AGENTS.md`](USING_WITH_AGENTS.md).

---

## What good output looks like

| Path | Role |
|------|------|
| `docs/Master_Index.md` | Entry point + Document Map |
| `docs/features/FeatureName-Understanding.md` | Shape only — is / is not, Relationship, Assumptions (not full-spec review) |
| `docs/features/FeatureName.md` | Durable contract after shape confirm |
| `docs/features/FeatureName-TODO.md` | Tasks + **Current focus** |
| `docs/_shared/…` | Only for truly shared project pieces (may be empty) |
| `docs/Tooling.md` / `docs/Human-TODO.md` | Machine tools / human inbox (procure · playtest · decide · waiting) |
| `docs/reference/` | Source materials (not the living map) |
| `docs/templates/` | Upstream pack — not live feature content |

Start with Master Index + one feature; grow as ideas arrive.
