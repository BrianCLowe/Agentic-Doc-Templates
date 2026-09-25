# [Project Name] — Human TODO

> Never edit this template unless the user asks you to. Live file: `docs/Human-TODO.md` (copy from this template at bootstrap).
>
> **Section order (human-facing doc):** **Open** → **Done** at the top; how-to for humans then agent dual-write / sync last. Do not put instructions above the task lists.

**Last Updated**: [YYYY-MM-DD]  
**Related**: [Master_Index.md](Master_Index.md) · [Tooling.md](Tooling.md) · [workflow/human-todo.md](templates/agent/workflow/human-todo.md) §13

---

**Your inbox** — everything waiting on a human. New here? Scroll to [Instructions for Humans](#instructions-for-humans) (and agent notes below that).

---

## Open

Keep this list short — **one `- [ ]` list item per human action** (not a table — table cells are not clickable in preview).

**Owner:** link to the feature/shared TODO item title for `playtest` / `decide`; `this file` for `procure` / `waiting`.  
**Kinds:** `procure` · `playtest` · `decide` · `waiting`  
**Assignee** *(optional):* `<role_id>` · `unassigned` · leftover `human` — omit when team inbox is unset. Named humans use their slug (e.g. `alex`), not a generic `human` dump. Leftover `human` only if that id is Active. When `team_inbox` is enabled, new rows **stamp from `kind_defaults` only if that `role_id` is Active on [`Team-Roster.md`](Team-Roster.md)** (e.g. `playtest` → `qa`); else `unassigned`. No per-row click for the first fill.  
**Claim / reassign:** override only (*assign playtest to QA* / *I’ll take it*) — not the bulk path. One-shot *apply defaults to Open* fills leftover unassigned rows after enable **only if that `role_id` is Active on [`Team-Roster.md`](Team-Roster.md)**; else leave `unassigned`.

Enabled-mode row shape *(only when `team_inbox` is on — do not copy Assignee onto default / unset-inbox rows)*:

```
- [ ] **[e.g. Score Target feel]** (`playtest`)
  Owner: … · Blocks: …
  Assignee: qa
```

- [ ] **[e.g. Score Target feel — is 10k short/right/swingy?]** (`playtest`)  
  Owner: [ScoreTarget-TODO.md](features/ScoreTarget-TODO.md) — "Tune win target" · Blocks: ScoreTarget  
  Notes: Agent: capture feel notes on owner TODO

- [ ] **[e.g. Default theme — keep Dev for boot?]** (`decide`)  
  Owner: [Theme-TODO.md](features/Theme-TODO.md) — "Pick boot theme" · Blocks: Theme  
  Notes: Agent: capture the pick on owner TODO

- [ ] **[e.g. Entra app registration + client secret]** (`procure`)  
  Owner: this file · Blocks: [GraphAuth-TODO.md](features/GraphAuth-TODO.md)  
  Notes: Secret → `.env` / Key Vault — **not** this file

- [ ] **[e.g. Steam private beta — App ID]** (`waiting`)  
  Owner: this file · Blocks: Release  
  Notes: Partner portal

- [ ] **[Add items as discovered]** (`kind`)  
  Owner: … · Blocks: …  
  Notes: …

---

## Done

Move finished items here (as `- [x]`) so **Open** stays short.

- [x] **[e.g. Tutorial PIE walkthrough]** (`playtest`) — YYYY-MM-DD — Felt fine; no doc change
- [x] **[e.g. Vendor API key created]** (`procure`) — YYYY-MM-DD — Stored in local `.env`

---

## Instructions for Humans

- This is **your** inbox — everything waiting on you in one place. Feature TODOs are for the agent; skim **Open** at the top when you resume.
- Work an item, then tell the agent in chat (you do not have to edit markdown yourself unless you want to):

  - *Checked Score Target — 10k feels short / right / still too swingy.*
  - *Human TODO: done Tutorial walkthrough.*
  - *Decided Default theme — keep Dev for boot.*
  - *Still waiting on Steam; leave it open.*
  - *I’ll take the Score Target playtest.*
  - *Assign playtest to QA.*
  - *Apply defaults to Open.*
  - *Add the team — you open the roster PR.*
  - *Put me on the roster as Alex.*
  - *I'm Sam — I take decide and procure.*
  - *Update [bot]’s jobs / anti-jobs.*
  - *What’s left on the human TODO?*

- Keep secrets out of git; use `.env.example` for variable *names* only.
- Optional: check the box in **Open** yourself; still tell the agent so they sync the owner TODO and archive the row.
- You can **claim** or **reassign** any Open item (*I’ll take the Score Target playtest.* / *Assign playtest to QA.*). That is an **override** — first fill is stamp-on-create (or one-shot *apply defaults to Open*, Active `role_id` only). Put yourself on the roster with your name if you want assignments to you. You are not forced into a bot team.
- If this project enabled optional team inbox routing, new Open rows stamp Assignee from the project’s kind defaults **when that role is Active on [`Team-Roster.md`](Team-Roster.md)**; else `unassigned`. Named humans put themselves on the roster with **their own name / slug** — this inbox is the work list, not a person. Bots add themselves (Name, Jobs, Anti-jobs if defined). Report-only bots ask someone to add them. Standing up a full team: **one** agent opens the roster PR — do not race competing PRs. A coding agent on a handoff must **not** invent roster bots or human names. Unset settings = this inbox waits on you, same as always; no auto-stamp; no Team-Roster file.

**Kinds:**

| Kind | Means | Examples |
|------|--------|----------|
| `procure` | Account, key, portal, purchase, org approval | Azure Bot, API key, App Store listing |
| `playtest` | Human must run / feel / smoke-test | Score target timing. A human-verify row is added only by todo warden after a passing exercise — not a look at unfinished work |
| `decide` | Human judgment or sign-off | Theme pick, piece colors, “ship this default” |
| `waiting` | Blocked on someone/something outside the repo | Steam Partner App ID, vendor reply |

---

## How this inbox works *(agents)*

| | **Human-TODO** | **Tooling.md** | Feature / shared `*-TODO.md` |
|--|----------------|----------------|------------------------------|
| Who acts | **You** *(or an allowed team bot if this project enabled optional team inbox routing)* | Agent on a machine | Agent in the codebase *(except human-gated items)* |
| Role | **Dashboard / index** — short rows + checkboxes | Install CLIs/SDKs | **Owner** of detail & outcome notes for playtest/decide; code tasks |
| Secrets | **Never** paste keys here — only “create → put in `.env` / vault” | No secrets | No secrets |

**Ownership (index + owner):**

| Kind | Human-TODO row | Canonical detail / outcome |
|------|----------------|----------------------------|
| `playtest` · `decide` | Thin pointer + checkbox | Owner feature/shared `*-TODO.md` item |
| `procure` · `waiting` | Row holds how-to / status | This file; features **link here** (do not copy portal steps into every TODO) |

**Agent role:** Dual-write when creating a human-gated task (owner TODO item **and** a checkbox item here). When `team_inbox` is enabled, stamp Assignee from `kind_defaults` only if that `role_id` is Active on `Team-Roster.md`; else `unassigned` (do not fallback-stamp `human`). Do **not** invent roster bots or human names on a handoff. Do **not** mark done unless the user (or an allowed team-inbox assignee) said so. Do **not** invent procure/waiting items the project does not need.

**Human role:** Work **Open**; tell the agent in chat when you finish or have feedback (phrases above). Agent syncs the owner doc and this list.

---

## Instructions for AI Agents

Keep Open → Done first. Dual-write, done-only-on-confirm, and inbox repair: [`workflow/human-todo.md`](templates/agent/workflow/human-todo.md). Do not reconstruct procedure from this file after compaction.

---

*Keep Open short — one row per real human need.*
