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

1. **Dual-write (mandatory):** When Understanding, planning, Current focus, or implementation creates a task only a human (or an allowed `team_inbox` assignee) can close → in the **same edit** add/update the owner `*-TODO.md` item **and** an **Open** `- [ ]` list item on `Human-TODO.md` (kind + Owner + Blocks). When `team_inbox.enabled`, also write **Assignee** (`unassigned`, `human`, or a `kind_defaults` hint — do not invent a roster if settings omit `roles`). **Never put checkboxes inside markdown tables** — preview cannot toggle those. If it is not on Human-TODO, it does not exist as a human ask — do not bury playtest/feel/sign-off only in feature TODOs or chat.
2. Keep Human-TODO items short; put steps and outcome notes on the owner TODO (`playtest` / `decide`) or under the Human-TODO list item (`procure` / `waiting`).
3. Never store secrets in docs. Instruct: create credential → put in `.env` / vault (names only in `.env.example`).
4. Do not mark items **done** unless there is a confirm report (chat or explicit checkbox + tell-the-agent). **Unset `team_inbox` / `enabled: false`:** only the human’s confirm counts (legacy). **`team_inbox.enabled`:** the assignee’s confirm report counts when settings allow that role to close that kind; default is **bot reports, human or assignee confirms** unless the project opts into `assignee_closes`. Playtest still needs a *Checked…* / human or designated-bot report — **no silent agent close**. On confirm: update owner TODO (`[x]` + date + feedback notes), move Human-TODO item to **Done** as `- [x]`, refresh affected Current focus.
5. If the user asks what’s left for them → summarize **Open** from `Human-TODO.md` only. If you find human-gated items on feature TODOs missing from the inbox, **repair dual-write** *(one direction)*: add thin Open `- [ ]` items **here** that point at the owner TODO — never the reverse (do not copy this inbox onto feature TODOs “for dual-write”). Then summarize.
6. Create the file at bootstrap (may start empty). Fill as soon as conversation or Document Map implies human-gated work. If Open is still a table, convert to `- [ ]` list items without dropping content.

### Team inbox *(optional assignees — do not force)*

**Omit / unset / `enabled: false` = human-only inbox (legacy).** Do **not** invent bot assignees, silent-route Open items, or copy another team’s bot roster. This is not a mandatory multi-bot org chart. Each project works out who gets what.

When `docs/ADT-settings.yaml` → `team_inbox.enabled: true`:

- Each Open item may carry **Assignee:** `human` | `<role_id>` | `unassigned`. Role ids are strings the project defines.
- **`kind_defaults` are hints**, not a rigid map. First assign may follow them; a human can always override. Example defaults *some* teams use (not required for every adopter): `playtest` → `qa`; placement / YTF feel notes → `ux` (if they have one); `procure` / `decide` / secrets → `human`; code implement → implementer (usually feature `*-TODO.md`, not this inbox); Understanding drain → understanding-author; nightly audit → report-only unless green-lit.
- **Claim / reassign:** a human in chat (*assign playtest to QA* / *I’ll take it*) may always claim or reassign. A bot may claim only kinds listed in its role’s `may_claim` (and only when `claim_mode` allows: `open` or `kind_defaults_only`).
- Feature `*-TODO.md` human-gated rows may optionally carry the same Assignee line. **Do not** replace feature TODO ownership of code work.
- Dual-write stays mandatory. Done-only-on-confirm still applies (see step 4). Prefer: the assignee may mark playtest checked via a chat report. Still no silent close without that report.
- Never paste secrets or bot credentials into docs.

---
