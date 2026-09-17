# [Project Name] — Team roster

> Copy to `docs/Team-Roster.md` **only** when this project enabled `team_inbox`. Do not create this live file for a human-only inbox. Never edit this template unless the user asks.

**Last Updated**: [YYYY-MM-DD]  
**Related**: [Human-TODO.md](Human-TODO.md) · [ADT-settings.yaml](ADT-settings.yaml) · [workflow/human-todo.md](templates/agent/workflow/human-todo.md) §13

---

**Who exists** for Human-TODO / human-gated follow-ups. Coding agents **read** this before assigning work. Named humans and bots **write their own row**. Empty Active is correct until someone self-IDs.

**Humans:** put yourself on Active with **your** slug (`alex`, not `human`) so assignments go to you. Human-TODO is the inbox of work, not a person. Optional leftover `human` bucket only if the project wants unsigned human work on that id. Help: [`help/SCAFFOLDS.md`](templates/help/SCAFFOLDS.md). Inbox: [`Human-TODO.md`](Human-TODO.md).

**Agents:** Fill-in blanks. Two-stage roster (read vs self-ID / report-only proxy · one initial PR · update when jobs change): [`agent/workflow/human-todo.md`](templates/agent/workflow/human-todo.md). Bots **write their own row**.

---

## Active

| role_id | Name | Jobs | Anti-jobs | Follow-ups | Handoff | Roster write |
|---------|------|------|-----------|------------|---------|--------------|
| [add only by self-ID, user-stated this turn, or report-only proxy] | | | | | | |

**Anti-jobs:** only real “must not” duties. `—` / empty is correct. Do not invent some to look complete.

**Stale row:** when Name, Jobs, Anti-jobs, Follow-ups, or Handoff change → the teammate updates **their** row the same turn (report-only asks the proxy). Do not leave yesterday’s job on the roster.

**Roster write:** `self` = this teammate (bot or named human) updates their own row. `report-only` = another agent or the human adds/updates the row when asked. `—` = leftover `human` bucket only (not a named person).

---

## Row shape *(not a live bot)*

Do **not** copy this into Active unless that teammate exists and is self-IDing / user-named / proxy-requested.

```
| [role_id — named-human slug or bot id] | [Name] | [Jobs] | [Anti-jobs — or —] | [follow-up kinds] | [handoff] | self or report-only |
```

Named-human example *(not a live person — do not copy as a teammate)*:

```
| [alex] | [Alex] | [Sign-off / decide / procure] | — | decide · procure · waiting | chat | self |
```

---

*Keep Active honest — missing teammates stay missing. Do not invent a team or human names. One initial PR when standing up a full team — do not open competing roster PRs.*
