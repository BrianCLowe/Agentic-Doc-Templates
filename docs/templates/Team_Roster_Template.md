# [Project Name] — Team roster

> Copy to `docs/Team-Roster.md` **only** when this project enabled `team_inbox`. Do not create this live file for a human-only inbox. Never edit this template unless the user asks.

**Last Updated**: [YYYY-MM-DD]  
**Related**: [Human-TODO.md](Human-TODO.md) · [ADT-settings.yaml](ADT-settings.yaml) · [workflow/human-todo.md](templates/agent/workflow/human-todo.md) §13

---

**Who exists** for Human-TODO / human-gated follow-ups. Coding agents **read** this before assigning work. Bots **write their own row**. Empty Active is correct until someone self-IDs.

**Humans:** [`help/SCAFFOLDS.md`](help/SCAFFOLDS.md). Inbox: [`Human-TODO.md`](Human-TODO.md).

**Agents:** Fill-in blanks. Two-stage roster (read vs self-ID / report-only proxy · one initial PR · update when jobs change): [`agent/workflow/human-todo.md`](agent/workflow/human-todo.md).

---

## Active

| role_id | Name | Jobs | Anti-jobs | Follow-ups | Handoff | Roster write |
|---------|------|------|-----------|------------|---------|--------------|
| human | [name or "project owner"] | Sign-off / inbox owner | [— unless defined] | procure · decide · waiting | chat | — |
| [add only by self-ID, user-stated this turn, or report-only proxy] | | | | | | |

**Anti-jobs:** only real “must not” duties. `—` / empty is correct. Do not invent some to look complete.

**Stale row:** when Name, Jobs, Anti-jobs, Follow-ups, or Handoff change → the bot updates **its** row the same turn (report-only asks the proxy). Do not leave yesterday’s job on the roster.

**Roster write:** `self` = this bot updates its own row. `report-only` = another agent or the human adds/updates the row when asked. `—` = human.

---

## Row shape *(not a live bot)*

Do **not** copy this into Active unless that bot exists and is self-IDing / user-named / proxy-requested.

```
| [role_id] | [Name — handle or spawn name] | [Jobs — duties they take] | [Anti-jobs — or —] | [follow-up kinds] | [how a coding agent hands work off] | self or report-only |
```

---

*Keep Active honest — missing bots stay missing. Do not invent a team. One initial PR when standing up a full team — do not open competing roster PRs.*
