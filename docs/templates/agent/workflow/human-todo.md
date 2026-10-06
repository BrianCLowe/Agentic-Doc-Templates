> **Workflow module.** Open from the [workflow index](../Modular_Docs_Workflow.md) for the human inbox.

# Human TODO

## 13. Human TODO *(inbox — needs a human)*

Live file: **`docs/Human-TODO.md`** (from [`Human_TODO_Template.md`](../../Human_TODO_Template.md)).

**One project inbox for humans** — anything a coding agent must not close from assumptions: procurement, playtest/feel, decisions/sign-off, and external waiting. Format and kinds: see the Human TODO template.

**Section order (human-facing):** **Open** → **Done** at the top (tasks visible immediately); short “scroll for instructions” note above Open; Instructions for Humans then ownership / dual-write / Instructions for AI Agents **below**. Do not put instructions above the task lists.

| Put on Human-TODO | Put elsewhere |
|-------------------|---------------|
| `procure` — portal / account / key / purchase / approval | Installable CLIs/SDKs → [`Tooling.md`](../../../Tooling.md) Required / Optional. An API or service the **running app** will call → also **Services this app consumes** on that file (same turn; Workflow §11). The Human-TODO row stays the errand |
| `playtest` — human must run, feel, or smoke-test | Agent-only code is the harness. Do not create a `*-TODO.md` |
| `decide` — human judgment or sign-off | |
| `waiting` — blocked on someone/something outside the repo | |

**The inbox is the only list.** A human errand is an Open row here. Do not also write a feature `*-TODO.md`.

**Agent behavior:**

1. For `procure` / `decide` / `waiting`: add an **Open** `- [ ]` list item on `Human-TODO.md` (kind + Blocks). Do **not** invent a playtest row. **Unset / `enabled: false` `team_inbox`:** do **not** auto-stamp (human-only inbox). **`team_inbox.enabled`:** open [`team-roster.md`](team-roster.md) and stamp Assignee there — do not invent a roster row in this file. Do not invent `Team-Roster.md` bot or human-name rows. **Never put checkboxes inside markdown tables** — preview cannot toggle those. If a `procure` / `decide` / `waiting` gate is not on Human-TODO, it does not exist as a human ask.
2. Keep Human-TODO items short. Put how-to under the list item.
3. Never store secrets in docs. Instruct: create credential → put in `.env` / vault (names only in `.env.example`). When the `procure` item is an API or service the running app will call, in that **same edit** add or update a **Services this app consumes** row on `docs/Tooling.md` (service, why, credential name, docs link). Create that section from the tooling template if it is missing. Do not put the service in Required / Optional. Do not invent services the project does not call.
4. Do not mark items **done** unless there is a confirm report (chat or explicit checkbox + tell-the-agent). Only the human’s confirm counts. **`team_inbox.enabled`:** who else may close is in [`team-roster.md`](team-roster.md). **no silent agent close**. On confirm, move the Human-TODO item to **Done** as `- [x]`.
5. If the user asks what’s left for them → summarize **Open** from `Human-TODO.md` only.
6. Create the file at bootstrap (may start empty). Fill as soon as conversation or Document Map implies human-gated work. If Open is still a table, convert to `- [ ]` list items without dropping content.
