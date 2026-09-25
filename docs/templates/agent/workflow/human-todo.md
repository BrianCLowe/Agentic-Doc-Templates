> **Workflow module.** Open from the [workflow index](../Modular_Docs_Workflow.md) for Human-TODO dual-write / inbox rules.

# Human TODO

## 13. Human TODO *(inbox — needs a human)*

Live file: **`docs/Human-TODO.md`** (from [`Human_TODO_Template.md`](../../Human_TODO_Template.md)).

**One project inbox for humans** — anything a coding agent must not close from assumptions: procurement, playtest/feel, decisions/sign-off, and external waiting. Format and kinds: see the Human TODO template.

**Section order (human-facing):** **Open** → **Done** at the top (tasks visible immediately); short “scroll for instructions” note above Open; Instructions for Humans then ownership / dual-write / Instructions for AI Agents **below**. Do not put instructions above the task lists.

| Put on Human-TODO | Put elsewhere |
|-------------------|---------------|
| `procure` — portal / account / key / purchase / approval | Installable CLIs/SDKs → [`Tooling.md`](../../../Tooling.md) Required / Optional. An API or service the **running app** will call → also **Services this app consumes** on that file (same turn; Workflow §11). The Human-TODO row stays the errand |
| `playtest` — human must run, feel, or smoke-test | Agent-only code tasks → feature or `_shared/` `*-TODO.md` |
| `decide` — human judgment or sign-off | |
| `waiting` — blocked on someone/something outside the repo | |

**Index + owner (do not “move” tasks):**

| Kind | Canonical detail / outcome | Human-TODO |
|------|----------------------------|------------|
| `playtest` · `decide` | Owner feature/shared `*-TODO.md` item | Thin checkbox row + **Owner** link |
| `procure` · `waiting` | Human-TODO row (how-to / status) | Features **link here** — do not copy full checklists into every TODO |

**Agent behavior:**

1. **Dual-write (mandatory)** for `procure` / `decide` / `waiting`: when planning or implementation hits a task only a human can close → in the **same edit** add/update the owner `*-TODO.md` item **and** an **Open** `- [ ]` list item on `Human-TODO.md` (kind + Owner + Blocks). **Human-verify `playtest` is not in this dual-write.** Only the outcome audit creates that row, and only after a passing exercise note (Workflow §5.5). Declining doc-roles does not skip the audit — the parent runs that section in this session. Orchestrator, implementer, graduate, and sync do **not** add a “please look” / human-verify playtest on their own. **Unset / `enabled: false` `team_inbox`:** do **not** auto-stamp (human-only inbox). **`team_inbox.enabled`:** open [`team-roster.md`](team-roster.md) and stamp Assignee there — do not invent a roster row in this file. **Never put checkboxes inside markdown tables** — preview cannot toggle those. If a `procure` / `decide` / `waiting` gate is not on Human-TODO, it does not exist as a human ask.
2. Keep Human-TODO items short; put steps and outcome notes on the owner TODO (`playtest` / `decide`) or under the Human-TODO list item (`procure` / `waiting`).
3. Never store secrets in docs. Instruct: create credential → put in `.env` / vault (names only in `.env.example`). When the `procure` item is an API or service the running app will call, in that **same edit** add or update a **Services this app consumes** row on `docs/Tooling.md` (service, why, credential name, docs link). Create that section from the tooling template if it is missing. Do not put the service in Required / Optional. Do not invent services the project does not call.
4. Do not mark items **done** unless there is a confirm report (chat or explicit checkbox + tell-the-agent). Only the human’s confirm counts. **`team_inbox.enabled`:** who else may close is in [`team-roster.md`](team-roster.md). Playtest still needs a *Checked…* report — **no silent agent close**. On confirm for `procure` / `decide` / `waiting`: update the owner TODO (`[x]` + date + feedback notes), move the Human-TODO item to **Done** as `- [x]`, refresh affected Current focus. On a playtest confirm that the scenario held: leave the outcome `[x]`, move the inbox row to Done with the report. On a playtest confirm that the scenario did not hold: move the inbox row to Done with the report, then run the outcome-audit reopen (Workflow §5.5) — uncheck that outcome and its Acceptance line, one sentence on the outcome, one Exercise. Do not leave the outcome `[x]`.
5. If the user asks what’s left for them → summarize **Open** from `Human-TODO.md` only. If you find `procure` / `decide` / `waiting` items on feature TODOs missing from the inbox, **repair dual-write** *(one direction)*: add thin Open `- [ ]` items **here** that point at the owner TODO — never the reverse (do not copy this inbox onto feature TODOs “for dual-write”). Do **not** repair-add a human-verify `playtest`. Then summarize.
6. Create the file at bootstrap (may start empty). Fill as soon as conversation or Document Map implies human-gated work. If Open is still a table, convert to `- [ ]` list items without dropping content.
