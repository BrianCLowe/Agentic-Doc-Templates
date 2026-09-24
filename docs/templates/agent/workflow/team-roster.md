> **Workflow module.** Open only when `docs/ADT-settings.yaml` â `team_inbox.enabled` is true. Unset / `enabled: false` = human-only inbox â do not open this file. Solo dual-write stays in [`human-todo.md`](human-todo.md).

# Team roster

### Team inbox *(optional assignees â do not force)*

**Omit / unset / `enabled: false` = human-only inbox (legacy).** Do **not** invent bot assignees, silent-route Open items, or copy another teamâs bot roster. This is not a mandatory multi-bot org chart. Each project works out who gets what.

When `docs/ADT-settings.yaml` â `team_inbox.enabled: true` (opts into assign-all-at-once):

- Each Open item carries **Assignee:** `<role_id>` Âˇ `unassigned` Âˇ leftover `human` *(only if that id is Active)*. Named humans use **their slug** (`alex`), not a generic dump onto Human-TODO. Role ids are strings the project defines.
- **Assign-all-at-once (bulk path):**
  1. **Stamp-on-dual-write** â stamp Assignee from `kind_defaults` in the same edit **when that `role_id` is Active on the roster** (e.g. all new `playtest` â `qa` after QA self-IDed; `decide` â `alex` after Alex self-IDed). First fill does not wait on a claim or a per-row click. Missing Active row â `unassigned` (do not invent the bot or a human name).
  2. **One-shot backfill** â after the project enables `team_inbox` + roster / `kind_defaults`, agents (or a human) may run *apply defaults to Open* **once**: fill **unassigned** Open rows from `kind_defaults` **only if that `role_id` is Active on the roster**. If the default id is not Active â leave `unassigned`. Do **not** repeatedly re-stamp rows that already have an explicit assignee (claimed / reassigned).
- **`kind_defaults` are the stamp map**, still project-owned â not a pack-required org chart. Stamp only when the `role_id` is **Active** on the team roster (below). Example defaults *some* teams use (not required): `playtest` â `qa`; `procure` / `decide` / secrets â a **named human slug** if they self-IDed, or leftover `human` if that row is Active. Do not invent `qa` / `ux` / other bots or human names to match a default.
- **Claim / reassign is override only** (human or allowed bot) â not the bulk path. A human in chat (*assign playtest to QA* / *Iâll take it*) may always override. A bot may claim only kinds listed in its roleâs `may_claim` (and only when `claim_mode` allows: `open` or `kind_defaults_only`).
- **Bot discovery:** bots watch âmy open rowsâ / one digest ping â **not** one PR per claim.
- Feature `*-TODO.md` human-gated rows may optionally carry the same Assignee line (same stamp / backfill / override rules). **Do not** replace feature TODO ownership of code work.
- Dual-write stays mandatory. Done-only-on-confirm still applies ([`human-todo.md`](human-todo.md) step 4). Prefer: the assignee may mark playtest checked via a chat report. Still **no silent agent close** without that report.
- Never paste secrets or bot credentials into docs.

### Team roster *(two-stage â who exists)*

Live file: **`docs/Team-Roster.md`** (from [`Team_Roster_Template.md`](../../Team_Roster_Template.md)). **Create only when `team_inbox` is enabled.** Unset inbox â do **not** create the file.

`kind_defaults` is the stamp map (kind â `role_id`). The roster is **who that id is** (**Name**), their **Jobs**, **Anti-jobs** *(if defined)*, and **how to hand off** â **named humans and bots**. Human-TODO is the inbox of *work*, not a person. A coding agent cannot discover teammates from pack doc-roles, `.grok/agents/`, or another teamâs settings.

**Row fields:**

| Field | Fill with | Do not |
|-------|-----------|--------|
| **Name** | Display name / handle / spawn name (no secrets) | Invent a teammate or human name |
| **Jobs** | Duties they actually take (plural OK, short) | Copy another teamâs jobs |
| **Anti-jobs** | Real âmust notâ only. `â` / empty if none defined | Invent anti-jobs to look complete |
| **Follow-ups** | Kinds / follow-up types they take | Guess kinds they never claimed |
| **Handoff** | How a coding agent gives them work | Paste credentials |
| **Roster write** | `self` Âˇ `report-only` Âˇ `â` (leftover `human` bucket only) | Dump every person onto `human` |

**Stale row:** if Name, Jobs, Anti-jobs, Follow-ups, or Handoff **change**, the teammate updates **their** row the same turn (report-only asks the proxy). Handoff coding agents do **not** rewrite another teammateâs duties. Do not leave yesterdayâs job on the roster.

**Stage 1 â coding agent on a handoff (read only):**

1. Open `docs/Team-Roster.md` if it exists. If `team_inbox` is on and the file is missing â create it from the template (named-human / leftover-`human` fill-in **only** if user-stated this turn; Active otherwise empty). **Stop.** Do **not** add bot or invented-name rows.
2. Assign follow-ups / stamp Assignee **only** to **Active** `role_id`s (`human` only if that leftover bucket is Active). Use that rowâs **Handoff**.
3. If the job has no Active row, or `kind_defaults` names a `role_id` that is not Active â write `unassigned`. Do **not** fallback-stamp `human` for human-gated kinds â that locks the row and blocks later *apply defaults to Open* after a bot or named human self-IDs. **Do not invent** a roster entry to match the default.
4. Pack adapters (`understanding-author`, `feature-implementer`, âŚ) are **not** roster bots. Installed harness agents are **not** a license to fill the table.

**Do not (handoff / coding agent):** add a bot because you âknow we need QAâ; invent a human name; copy example / another projectâs rows; backfill Active from `kind_defaults` or `team_inbox.roles`; spawn a bot that is not listed.

**Stage 2 â teammates identify themselves (write own row only):**

You may write the roster **only** when **one** of these is true:

| You may write | When |
|---------------|------|
| **Self-ID** | The user said you are that bot (*you are the QA bot*), or you were spawned as that team `role_id`, **and** `team_inbox` is enabled |
| **Human self-ID** | The human said *put me on the roster as [name]* / *I'm [name] â I take [kinds]* **and** `team_inbox` is enabled. `role_id` = their slug (not `human`). Name = their name |
| **User-stated this turn** | The human named a teammate (*we have a QA grok bot called X* / *add Jordan to the roster*) â add **that** row only |
| **Report-only proxy** | A report-only bot (or the human) asked you to add/update **their** row â add **that** row only |

**Self-ID steps:** create `docs/Team-Roster.md` from the template if missing â add or refresh **your** Active row (`role_id`, Name, Jobs, Anti-jobs if defined else `â`, Follow-ups, Handoff, `Roster write: self`) â match `team_inbox.roles` / `kind_defaults` if those keys already name you â **stop**. Named humans use **their slug**, not `human`. Do **not** add teammates. Do **not** invent jobs, anti-jobs, or names you were not given.

**Report-only bots:** do **not** edit the roster (and do not invent a coding-agent row for yourself). Ask another bot/agent or the human: *add me to Team-Roster as `role_id` âŚ Name âŚ Jobs âŚ Anti-jobs (or â) âŚ follow-ups âŚ handoff âŚ (`report-only`)*. One digest ping is enough. The helper writes **only** the requested row, sets `Roster write: report-only`, and stops.

### One initial PR *(full-team stand-up â no competing roster PRs)*

When **`team_inbox` is first enabled** or a **full team** is added in one go (several teammates named, *add the team*, *stand up the roster*):

1. **One scribe** opens **one** PR that creates `docs/Team-Roster.md` (+ `team_inbox` settings if not already recorded). The scribe is the agent that received *Enable team inbox* / *add the team*, or the first bot asked to stand up the roster â not every bot at once.
2. That PR may include **user-stated** rows from this turn (named humans and bots â Name / Jobs / Anti-jobs if the human defined them). Do not invent the rest of the org chart or human names.
3. **Other bots do not open a second PR** that creates or rebases `Team-Roster.md`. If an open PR already touches the roster or `team_inbox` â add your self-ID on **that** PR if asked, or **wait for merge**, then self-ID. Do not race two âcreate Team-Rosterâ branches.
4. After the file exists on the default branch, later one-bot self-ID / stale-row updates may be their own small PR â still **one file writer at a time**. Check for an open roster PR first.

**Do not:** N bots Ă N PRs for the first roster. Do not treat âI must self-ID nowâ as a license to fork a conflicting Team-Roster branch.

**After a new Active row:** optional one-shot *apply defaults to Open* for leftover `unassigned` rows whose `kind_defaults` now match that **Active** `role_id`. Skip kinds whose default id is still missing from Active. Do not re-stamp explicit assignees.

**Phrases:** *Enable team inbox* (one PR: settings + empty roster; no invented bots or names) Âˇ *Add the team â you open the roster PR* (one scribe) Âˇ *Put me on the roster as Alex* / *I'm Sam â I take decide and procure* (named-human self-ID) Âˇ *You are the QA bot* (bot self-ID; join the open roster PR if one exists) Âˇ *Add the nightly auditor as report-only* (proxy) Âˇ *Update the QA botâs jobs* (stale-row) Âˇ *Whatâs on the team roster?*

---
