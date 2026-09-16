# [Project Name] — Team roster

> Copy to `docs/Team-Roster.md` **only** when this project enabled `team_inbox`. Do not create this live file for a human-only inbox. Never edit this template unless the user asks.

**Last Updated**: [YYYY-MM-DD]  
**Related**: [Human-TODO.md](Human-TODO.md) · [ADT-settings.yaml](ADT-settings.yaml) · [workflow/human-todo.md](templates/agent/workflow/human-todo.md) §13

---

**Who exists** for Human-TODO / human-gated follow-ups. Coding agents **read** this before assigning work. Bots **write their own row**. Empty Active is correct until someone self-IDs.

**Humans:** [`help/SCAFFOLDS.md`](help/SCAFFOLDS.md). Inbox: [`Human-TODO.md`](Human-TODO.md).

**Agents:** Fill-in blanks. Two-stage roster (read vs self-ID / report-only proxy): [`agent/workflow/human-todo.md`](agent/workflow/human-todo.md).

---

## Active

| role_id | Who | Job | Follow-ups | Handoff | Roster write |
|---------|-----|-----|------------|---------|--------------|
| human | [name or "project owner"] | Sign-off / inbox owner | procure · decide · waiting | chat | — |
| [add only by self-ID, user-stated this turn, or report-only proxy] | | | | | |

**Roster write:** `self` = this bot updates its own row. `report-only` = another agent or the human adds/updates the row when asked. `—` = human.

---

## Row shape *(not a live bot)*

Do **not** copy this into Active unless that bot exists and is self-IDing / user-named / proxy-requested.

```
| [role_id] | [handle or spawn name] | [one-line job] | [kinds or follow-up types] | [how a coding agent hands work off] | self or report-only |
```

---

*Keep Active honest — missing bots stay missing. Do not invent a team.*
