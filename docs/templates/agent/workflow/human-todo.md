<!-- pack-version: 2.7.17 -->

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

1. **Dual-write (mandatory):** When Understanding, planning, Current focus, or implementation creates a task only a human can close → in the **same edit** add/update the owner `*-TODO.md` item **and** an **Open** `- [ ]` list item on `Human-TODO.md` (kind + Owner + Blocks). **Never put checkboxes inside markdown tables** — preview cannot toggle those. If it is not on Human-TODO, it does not exist as a human ask — do not bury playtest/feel/sign-off only in feature TODOs or chat.
2. Keep Human-TODO items short; put steps and outcome notes on the owner TODO (`playtest` / `decide`) or under the Human-TODO list item (`procure` / `waiting`).
3. Never store secrets in docs. Instruct: create credential → put in `.env` / vault (names only in `.env.example`).
4. Do not mark items **done** unless the user confirms (chat or explicit checkbox + tell-the-agent). On confirm: update owner TODO (`[x]` + date + feedback notes), move Human-TODO item to **Done** as `- [x]`, refresh affected Current focus.
5. If the user asks what’s left for them → summarize **Open** from `Human-TODO.md` only. If you find human-gated items on feature TODOs missing from the inbox, **repair dual-write** *(one direction)*: add thin Open `- [ ]` items **here** that point at the owner TODO — never the reverse (do not copy this inbox onto feature TODOs “for dual-write”). Then summarize.
6. Create the file at bootstrap (may start empty). Fill as soon as conversation or Document Map implies human-gated work. If Open is still a table, convert to `- [ ]` list items without dropping content.

---
