> **Workflow module.** Open from the [workflow index](../Modular_Docs_Workflow.md) for Human-TODO dual-write / inbox rules.

# Human TODO

## 13. Human TODO *(inbox — needs a human)*

Live file: **`docs/Human-TODO.md`** (from [`Human_TODO_Template.md`](../../Human_TODO_Template.md)).

**One project inbox for humans** — anything a coding agent must not close from assumptions: procurement, playtest/feel, decisions/sign-off, and external waiting. Format and kinds: see the Human TODO template.

**Section order (human-facing):** **Open** → **Done** at the top (tasks visible immediately); short “scroll for instructions” note above Open; Instructions for Humans then ownership / dual-write / Instructions for AI Agents **below**. Do not put instructions above the task lists.

| Put on Human-TODO | Put elsewhere |
|-------------------|---------------|
| `procure` — portal / account / key / purchase / approval | Installable CLIs/SDKs → [`Tooling.md`](../../../Tooling.md) |
| `playtest` — human must run, feel, or smoke-test | Agent-only code tasks → feature or `_shared/` `*-TODO.md` |
| `decide` — human judgment or sign-off | |
| `waiting` — blocked on someone/something outside the repo | |

**Index + owner (do not “move” tasks):**

| Kind | Canonical detail / outcome | Human-TODO |
|------|----------------------------|------------|
| `playtest` · `decide` | Owner feature/shared `*-TODO.md` item | Thin checkbox row + **Owner** link |
| `procure` · `waiting` | Human-TODO row (how-to / status) | Features **link here** — do not copy full checklists into every TODO |

**Agent behavior:**

1. **Dual-write (mandatory):** When Understanding, planning, Current focus, or implementation creates a task only a human (or an allowed `team_inbox` assignee) can close → in the **same edit** add/update the owner `*-TODO.md` item **and** an **Open** `- [ ]` list item on `Human-TODO.md` (kind + Owner + Blocks). When `team_inbox.enabled`, **stamp Assignee from `kind_defaults`** in that same edit **only if that `role_id` is Active on `docs/Team-Roster.md`** (e.g. `playtest` → `qa` after QA self-IDed). If the kind has no default, or the default id is not Active → `unassigned`. Do **not** invent a roster row to make the stamp work. **Unset / `enabled: false`:** do **not** auto-stamp (legacy human-only). **Never put checkboxes inside markdown tables** — preview cannot toggle those. If it is not on Human-TODO, it does not exist as a human ask — do not bury playtest/feel/sign-off only in feature TODOs or chat.
2. Keep Human-TODO items short; put steps and outcome notes on the owner TODO (`playtest` / `decide`) or under the Human-TODO list item (`procure` / `waiting`).
3. Never store secrets in docs. Instruct: create credential → put in `.env` / vault (names only in `.env.example`).
4. Do not mark items **done** unless there is a confirm report (chat or explicit checkbox + tell-the-agent). **Unset `team_inbox` / `enabled: false`:** only the human’s confirm counts (legacy). **`team_inbox.enabled`:** the assignee’s confirm report counts when settings allow that role to close that kind; default is **bot reports, human or assignee confirms** unless the project opts into `assignee_closes`. Playtest still needs a *Checked…* / human or designated-bot report — **no silent agent close**. On confirm: update owner TODO (`[x]` + date + feedback notes), move Human-TODO item to **Done** as `- [x]`, refresh affected Current focus.
5. If the user asks what’s left for them → summarize **Open** from `Human-TODO.md` only. If you find human-gated items on feature TODOs missing from the inbox, **repair dual-write** *(one direction)*: add thin Open `- [ ]` items **here** that point at the owner TODO — never the reverse (do not copy this inbox onto feature TODOs “for dual-write”). Then summarize.
6. Create the file at bootstrap (may start empty). Fill as soon as conversation or Document Map implies human-gated work. If Open is still a table, convert to `- [ ]` list items without dropping content.

### Team inbox *(optional assignees — do not force)*

**Omit / unset / `enabled: false` = human-only inbox (legacy).** Do **not** invent bot assignees, silent-route Open items, or copy another team’s bot roster. This is not a mandatory multi-bot org chart. Each project works out who gets what.

When `docs/ADT-settings.yaml` → `team_inbox.enabled: true` (opts into assign-all-at-once):

- Each Open item carries **Assignee:** `<role_id>` · `unassigned` · leftover `human` *(only if that id is Active)*. Named humans use **their slug** (`alex`), not a generic dump onto Human-TODO. Role ids are strings the project defines.
- **Assign-all-at-once (bulk path):**
  1. **Stamp-on-dual-write** — new Open rows get Assignee from `kind_defaults` in the same edit **when that `role_id` is Active on the roster** (e.g. all new `playtest` → `qa` after QA self-IDed; `decide` → `alex` after Alex self-IDed). First fill does not wait on a claim or a per-row click. Missing Active row → `unassigned` (do not invent the bot or a human name).
  2. **One-shot backfill** — after the project enables `team_inbox` + roster / `kind_defaults`, agents (or a human) may run *apply defaults to Open* **once**: fill **unassigned** Open rows from `kind_defaults` **only if that `role_id` is Active on the roster**. If the default id is not Active → leave `unassigned`. Do **not** repeatedly re-stamp rows that already have an explicit assignee (claimed / reassigned).
- **`kind_defaults` are the stamp map**, still project-owned — not a pack-required org chart. Stamp only when the `role_id` is **Active** on the team roster (below). Example defaults *some* teams use (not required): `playtest` → `qa`; `procure` / `decide` / secrets → a **named human slug** if they self-IDed, or leftover `human` if that row is Active. Do not invent `qa` / `ux` / other bots or human names to match a default.
- **Claim / reassign is override only** (human or allowed bot) — not the bulk path. A human in chat (*assign playtest to QA* / *I’ll take it*) may always override. A bot may claim only kinds listed in its role’s `may_claim` (and only when `claim_mode` allows: `open` or `kind_defaults_only`).
- **Bot discovery:** bots watch “my open rows” / one digest ping — **not** one PR per claim.
- Feature `*-TODO.md` human-gated rows may optionally carry the same Assignee line (same stamp / backfill / override rules). **Do not** replace feature TODO ownership of code work.
- Dual-write stays mandatory. Done-only-on-confirm still applies (see step 4). Prefer: the assignee may mark playtest checked via a chat report. Still no silent close without that report.
- Never paste secrets or bot credentials into docs.

### Team roster *(two-stage — who exists)*

Live file: **`docs/Team-Roster.md`** (from [`Team_Roster_Template.md`](../../Team_Roster_Template.md)). **Create only when `team_inbox` is enabled.** Unset inbox → do **not** create the file.

`kind_defaults` is the stamp map (kind → `role_id`). The roster is **who that id is** (**Name**), their **Jobs**, **Anti-jobs** *(if defined)*, and **how to hand off** — **named humans and bots**. Human-TODO is the inbox of *work*, not a person. A coding agent cannot discover teammates from pack doc-roles, `.grok/agents/`, or another team’s settings.

**Row fields:**

| Field | Fill with | Do not |
|-------|-----------|--------|
| **Name** | Display name / handle / spawn name (no secrets) | Invent a teammate or human name |
| **Jobs** | Duties they actually take (plural OK, short) | Copy another team’s jobs |
| **Anti-jobs** | Real “must not” only. `—` / empty if none defined | Invent anti-jobs to look complete |
| **Follow-ups** | Kinds / follow-up types they take | Guess kinds they never claimed |
| **Handoff** | How a coding agent gives them work | Paste credentials |
| **Roster write** | `self` · `report-only` · `—` (leftover `human` bucket only) | Dump every person onto `human` |

**Stale row:** if Name, Jobs, Anti-jobs, Follow-ups, or Handoff **change**, the teammate updates **their** row the same turn (report-only asks the proxy). Handoff coding agents do **not** rewrite another teammate’s duties. Do not leave yesterday’s job on the roster.

**Stage 1 — coding agent on a handoff (read only):**

1. Open `docs/Team-Roster.md` if it exists. If `team_inbox` is on and the file is missing → create it from the template (named-human / leftover-`human` fill-in **only** if user-stated this turn; Active otherwise empty). **Stop.** Do **not** add bot or invented-name rows.
2. Assign follow-ups / stamp Assignee **only** to **Active** `role_id`s (`human` only if that leftover bucket is Active). Use that row’s **Handoff**.
3. If the job has no Active row, or `kind_defaults` names a `role_id` that is not Active → write `unassigned`. Do **not** fallback-stamp `human` for human-gated kinds — that locks the row and blocks later *apply defaults to Open* after a bot or named human self-IDs. **Do not invent** a roster entry to match the default.
4. Pack adapters (`understanding-author`, `feature-implementer`, …) are **not** roster bots. Installed harness agents are **not** a license to fill the table.

**Do not (handoff / coding agent):** add a bot because you “know we need QA”; invent a human name; copy example / another project’s rows; backfill Active from `kind_defaults` or `team_inbox.roles`; spawn a bot that is not listed.

**Stage 2 — teammates identify themselves (write own row only):**

You may write the roster **only** when **one** of these is true:

| You may write | When |
|---------------|------|
| **Self-ID** | The user said you are that bot (*you are the QA bot*), or you were spawned as that team `role_id`, **and** `team_inbox` is enabled |
| **Human self-ID** | The human said *put me on the roster as [name]* / *I'm [name] — I take [kinds]* **and** `team_inbox` is enabled. `role_id` = their slug (not `human`). Name = their name |
| **User-stated this turn** | The human named a teammate (*we have a QA grok bot called X* / *add Jordan to the roster*) — add **that** row only |
| **Report-only proxy** | A report-only bot (or the human) asked you to add/update **their** row — add **that** row only |

**Self-ID steps:** create `docs/Team-Roster.md` from the template if missing → add or refresh **your** Active row (`role_id`, Name, Jobs, Anti-jobs if defined else `—`, Follow-ups, Handoff, `Roster write: self`) → match `team_inbox.roles` / `kind_defaults` if those keys already name you → **stop**. Named humans use **their slug**, not `human`. Do **not** add teammates. Do **not** invent jobs, anti-jobs, or names you were not given.

**Report-only bots:** do **not** edit the roster (and do not invent a coding-agent row for yourself). Ask another bot/agent or the human: *add me to Team-Roster as `role_id` … Name … Jobs … Anti-jobs (or —) … follow-ups … handoff … (`report-only`)*. One digest ping is enough. The helper writes **only** the requested row, sets `Roster write: report-only`, and stops.

### One initial PR *(full-team stand-up — no competing roster PRs)*

When **`team_inbox` is first enabled** or a **full team** is added in one go (several teammates named, *add the team*, *stand up the roster*):

1. **One scribe** opens **one** PR that creates `docs/Team-Roster.md` (+ `team_inbox` settings if not already recorded). The scribe is the agent that received *Enable team inbox* / *add the team*, or the first bot asked to stand up the roster — not every bot at once.
2. That PR may include **user-stated** rows from this turn (named humans and bots — Name / Jobs / Anti-jobs if the human defined them). Do not invent the rest of the org chart or human names.
3. **Other bots do not open a second PR** that creates or rebases `Team-Roster.md`. If an open PR already touches the roster or `team_inbox` → add your self-ID on **that** PR if asked, or **wait for merge**, then self-ID. Do not race two “create Team-Roster” branches.
4. After the file exists on the default branch, later one-bot self-ID / stale-row updates may be their own small PR — still **one file writer at a time**. Check for an open roster PR first.

**Do not:** N bots × N PRs for the first roster. Do not treat “I must self-ID now” as a license to fork a conflicting Team-Roster branch.

**After a new Active row:** optional one-shot *apply defaults to Open* for leftover `unassigned` rows whose `kind_defaults` now match that **Active** `role_id`. Skip kinds whose default id is still missing from Active. Do not re-stamp explicit assignees.

**Phrases:** *Enable team inbox* (one PR: settings + empty roster; no invented bots or names) · *Add the team — you open the roster PR* (one scribe) · *Put me on the roster as Alex* / *I'm Sam — I take decide and procure* (named-human self-ID) · *You are the QA bot* (bot self-ID; join the open roster PR if one exists) · *Add the nightly auditor as report-only* (proxy) · *Update the QA bot’s jobs* (stale-row) · *What’s on the team roster?*

---
