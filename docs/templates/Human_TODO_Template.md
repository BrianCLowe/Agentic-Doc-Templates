# [Project Name] — Human TODO

> Never edit this template unless the user asks you to. Live file: `docs/Human-TODO.md` (copy from this template at bootstrap).

**Last Updated**: [YYYY-MM-DD]  
**Related**: [Master_Index.md](Master_Index.md) · [Tooling.md](Tooling.md) · [Modular_Docs_Workflow.md](agent/Modular_Docs_Workflow.md) §13

---

**One project inbox for everything waiting on a human** — procurement, playtest/feel, decisions/sign-off, and external waiting. Coding agents **cannot** close these from assumptions.

| | **Human-TODO** | **Tooling.md** | Feature / shared `*-TODO.md` |
|--|----------------|----------------|------------------------------|
| Who acts | **You** | Agent on a machine | Agent in the codebase *(except human-gated items)* |
| Role | **Dashboard / index** — short rows + checkboxes | Install CLIs/SDKs | **Owner** of detail & outcome notes for playtest/decide; code tasks |
| Secrets | **Never** paste keys here — only “create → put in `.env` / vault” | No secrets | No secrets |

**Ownership (index + owner):**

| Kind | Human-TODO row | Canonical detail / outcome |
|------|----------------|----------------------------|
| `playtest` · `decide` | Thin pointer + checkbox | Owner feature/shared `*-TODO.md` item |
| `procure` · `waiting` | Row holds how-to / status | This file; features **link here** (do not copy portal steps into every TODO) |

**Kinds:** `procure` · `playtest` · `decide` · `waiting`

| Kind | Means | Examples |
|------|--------|----------|
| `procure` | Account, key, portal, purchase, org approval | Azure Bot, API key, App Store listing |
| `playtest` | Human must run / feel / smoke-test | Score target timing, cascade spam, tutorial walkthrough |
| `decide` | Human judgment or sign-off | Theme pick, piece colors, “ship this default” |
| `waiting` | Blocked on someone/something outside the repo | Steam Partner App ID, vendor reply |

**Agent role:** Dual-write when creating a human-gated task (owner TODO item **and** a row here). Do **not** mark done unless the user said so. Do **not** invent procure/waiting rows the project does not need.

**Human role:** Work **Open**; tell the agent in chat when you finish or have feedback (phrases below). Agent syncs the owner doc and this list.

---

## Open

Keep this list short — one row per real human action. Prefer checkboxes so you can scan quickly.

| Done | Need | Kind | Owner | Blocks | Notes |
|------|------|------|-------|--------|-------|
| - [ ] | [e.g. Score Target feel — is 10k short/right/swingy?] | playtest | [ScoreTarget-TODO.md](features/ScoreTarget-TODO.md) — "Tune win target" | ScoreTarget | Agent: capture feel notes on owner TODO |
| - [ ] | [e.g. Entra app registration + client secret] | procure | this file | [GraphAuth-TODO.md](features/GraphAuth-TODO.md) | Secret → `.env` / Key Vault — **not** this file |
| - [ ] | [e.g. Steam private beta — App ID] | waiting | this file | Release | Partner portal |
| - [ ] | [Add rows as discovered] | | | | |

**Owner column:** link to the feature/shared TODO item title for `playtest` / `decide`; `this file` for `procure` / `waiting`.

---

## Done

Move finished rows here (or leave checked) so **Open** stays short.

| Need | Kind | Completed | Notes |
|------|------|-----------|-------|
| [e.g. Tutorial PIE walkthrough] | playtest | YYYY-MM-DD | Felt fine; no doc change |
| [e.g. Vendor API key created] | procure | YYYY-MM-DD | Stored in local `.env` |

---

## Instructions for AI Agents

- **Dual-write (mandatory):** When Understanding, planning, Current focus, or implementation creates a task only a human can close → in the **same edit**:
  1. Add/update the item on the **owner** `*-TODO.md` (for `playtest` / `decide`: full text + outcome space; for `procure` / `waiting`: a short “Blocked by Human-TODO — [Need]” link).
  2. Add/update a row in **Open** here with Kind, Owner link, and Blocks.
- If it is not on this list, it does **not** exist as a human ask — do not bury playtest/feel/sign-off only in feature TODOs or chat.
- Prefer **one project inbox** — do not duplicate long checklists here; link to the owner item for steps.
- Never write API keys, passwords, connection strings, or tokens into this file (or any docs file).
- Do **not** mark **done** from assumptions (“they probably playtested”) — only when the user confirms in chat or clearly checked the item and told you.
- When the user reports progress or feedback:
  1. Update the **owner** TODO (`[x]` + date; capture feel/decision notes on that item).
  2. Move the Human-TODO row to **Done** (or check it off) and refresh **Last Updated**.
  3. Unblock / refresh Current focus on affected feature TODOs if needed.
- Distinguish from [`Tooling.md`](Tooling.md): installable CLIs/SDKs go there; human portal/account **and** judgment work goes here.
- If the user asks “what’s left that I need to do?” / “what’s on the human TODO?” — summarize **Open** from **this file only**. If you find human-gated items on feature TODOs missing here, **add them** (repair dual-write), then summarize.
- On bootstrap: create this file (can start nearly empty). Add rows as soon as conversation or Document Map implies human-gated work.

---

## Instructions for Humans

- This is **your** inbox — everything waiting on you in one place. Feature TODOs are for the agent; skim **Open** here when you resume.
- Work an item, then tell the agent in chat (you do not have to edit markdown yourself unless you want to):

  - *Checked Score Target — 10k feels short / right / still too swingy.*
  - *Human TODO: done Tutorial walkthrough.*
  - *Decided Default theme — keep Dev for boot.*
  - *Still waiting on Steam; leave it open.*
  - *What’s left on the human TODO?*

- Keep secrets out of git; use `.env.example` for variable *names* only.
- Optional: check the box in **Open** yourself; still tell the agent so they sync the owner TODO and archive the row.

---

*Part of the Lean Modular Documentation system. Keep Open short — one row per real human need.*
