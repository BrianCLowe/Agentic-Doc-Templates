# How to Use These Templates

Day-to-day workflows after setup. First-time install: [`SETUP.md`](SETUP.md). Describing ideas in plain language: [`IDEA_CAPTURE_TIPS.md`](IDEA_CAPTURE_TIPS.md).

---

## The loop

1. You describe the idea (chat, `docs/reference/` design doc, or a mid-build correction).
2. The **agent drafts** `-Understanding.md` — **feature shape / guardrails**, not a full spec.
3. **You confirm shape** — especially what it is / is *not* and **Assumptions**. Spec-level detail may be missing on purpose.
4. After confirm, durable contract lands in the **spec**; work continues from TODOs (**Current focus** for session handoff).

Short asks are enough. Prefer the **full messy chat** over a polished summary when you have it — export or paste the whole thread; save lasting copies under `docs/reference/`. Details: [Bring the whole conversation](IDEA_CAPTURE_TIPS.md#bring-the-whole-conversation).

---

## Pattern 1 — Long chat → documentation

**When:** Brainstorming in Grok, ChatGPT, Claude web, etc. — no repo, or files to download first.

1. Attach **`docs/templates/chat-ui/AGENT.md`** only ([`chat-ui/README.md`](../chat-ui/README.md)).
2. Ask for **Save as:** paths per file; draft `-Understanding.md` first.

> Follow `AGENT.md`. Turn our conversation into modular docs for [app name]. Each file must start with **Save as:** `docs/...`.

With a repo/IDE: put `docs/templates/` in the project (or connect the repo), then:

> Using `docs/templates/`, create project documentation from our conversation so far. Do not invent features we did not talk about.

Your job is to correct wrong **identity** assumptions — not to write Understanding from scratch. When moving into the IDE, bring the **entire** brainstorm thread (see tip above).

---

## Pattern 2 — Idea mid-development

**When:** Already building; a new idea or scope change appears.

> New idea: [brief]. Add it to the docs — draft Understanding + TODO; I'll review.

> Update `RoleEditor-Understanding.md` — fix What this is NOT: separate UI on the existing editor, not a new editor engine.

Docs stay the living record so the next session does not re-derive from chat alone.

---

## Pattern 3 — Design doc / PRD → modular docs

Drop sources into **`docs/reference/`** (and the chat that produced them, if you still have it). Then:

> Read `docs/reference/Original_Design.md`. Convert into modular docs per `Master_Index_Template.md`. Keep the original in `reference/`.

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
| Chat → docs | *Create modular docs from our conversation using `docs/templates/`.* |
| New idea | *Add [idea] to the docs — draft Understanding + TODO; I'll review.* |
| Fix misunderstanding | *Update [Feature]-Understanding.md — especially What this is NOT.* |
| UI screenshot | *Save to `docs/features/assets/`, add Visual references on the **spec** (similar vs different).* |
| Vague idea | *Interview me using IDEA_CAPTURE_TIPS.md, then draft [Feature]-Understanding.md.* |
| Design doc | *Convert `docs/reference/[file]` to modular docs; keep original in reference/.* |
| Bootstrap | *Bootstrap modular docs using `docs/templates/agent/BOOTSTRAP.md`.* |
| Install rule | *Follow `docs/templates/agent/RULE_INSTALL.md` for [tool].* |
| Sync pack | *Update the doc templates from Agentic Doc Templates and sync our live docs.* |
| Sync mode | *Set sync to auto.* / *Set sync to choose.* *(recorded in `docs/ADT-settings.yaml`)* |
| Update-check cadence | *Check for template updates every session.* / *Only check every week.* |
| Optional role — intent | *Draft Understanding for [Feature] from what I said — I’ll review.* (main agent delegates if subagents installed) |
| Optional role — build | *Continue from Current focus.* *(single slice)* |
| Optional role — orchestrate | *Orchestrate — clear ready TODOs until blocked.* *(parent loop; ask scope/git once, then run)* |
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
