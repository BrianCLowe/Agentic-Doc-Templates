# [Project Name] — Human TODO

> Never edit this template unless the user asks you to. Live file: `docs/Human-TODO.md` (copy from this template at bootstrap).
>
> **Section order (human-facing doc):** **Open** -> **Done** at the top; how-to for humans then agent notes last. Do not put instructions above the task lists.

**Last Updated**: [YYYY-MM-DD]  
**Related**: [Master_Index.md](Master_Index.md) · [Tooling.md](Tooling.md) · [workflow/human-todo.md](templates/agent/workflow/human-todo.md) §13

---

**Your inbox** — everything waiting on a human. New here? Scroll to [Instructions for Humans](#instructions-for-humans) (and agent notes below that).

---

## Open

Keep this list short — **one `- [ ]` list item per human action** (not a table — table cells are not clickable in preview).

**Owner:** the feature/shared spec or stem name for `decide`; `this file` for `procure` / `waiting`.  
**Kinds:** `procure` - `decide` - `waiting`  

- [ ] **[e.g. Default theme — keep Dev for boot?]** (`decide`)  
  Owner: Theme spec - "Pick boot theme" - Blocks: Theme  
  Notes: Agent: record the pick on the Theme spec Decisions

- [ ] **[e.g. Entra app registration + client secret]** (`procure`)  
  Owner: this file - Blocks: GraphAuth  

- [ ] **[e.g. Steam private beta — App ID]** (`waiting`)  
  Owner: this file · Blocks: Release  
  Notes: Partner portal

- [ ] **[Add items as discovered]** (`kind`)  
  Owner: … · Blocks: …  
  Notes: …

---

## Done

Move finished items here (as `- [x]`) so **Open** stays short.

- [x] **[e.g. Vendor API key created]** (`procure`) - YYYY-MM-DD - Key issued

---

## Instructions for Humans

- This is **your** inbox - everything waiting on you in one place. Skim **Open** at the top when you resume.
- Work an item, then tell the agent in chat (you do not have to edit markdown yourself unless you want to):

  - *Decided Default theme — keep Dev for boot.*
  - *Still waiting on Steam; leave it open.*
  - *What’s left on the human TODO?*

- Optional: check the box in **Open** yourself; still tell the agent so they archive the row.

**Kinds:**

| Kind | Means | Examples |
|------|--------|----------|
| `procure` | Account, key, portal, purchase, org approval | Azure Bot, API key, App Store listing |
| `decide` | Human judgment or sign-off | Theme pick, piece colors, “ship this default” |
| `waiting` | Blocked on someone/something outside the project | Steam Partner App ID, vendor reply |

---

## Instructions for AI Agents

Keep Open -> Done first. Done-only-on-confirm and inbox repair: [`workflow/human-todo.md`](templates/agent/workflow/human-todo.md). Do not reconstruct procedure from this file after compaction.

---

*Keep Open short — one row per real human need.*
