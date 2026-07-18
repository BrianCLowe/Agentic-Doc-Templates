# [Project Name] — Human TODO

> Never edit this template unless the user asks you to. Live file: `docs/Human-TODO.md` (copy from this template at bootstrap).

**Last Updated**: [YYYY-MM-DD]  
**Related**: [Master_Index.md](Master_Index.md) · [Tooling.md](Tooling.md) · [Modular_Docs_Workflow.md](agent/Modular_Docs_Workflow.md) §13

---

**Project-level checklist for humans** — things a coding agent **cannot** do: accounts, portals, purchases, API keys, org approvals, cloud resource registration, certificates, store listings, etc.

| | **Human-TODO** | **Tooling.md** | Feature / shared `*-TODO.md` |
|--|----------------|----------------|------------------------------|
| Who acts | **You** (or IT / admin) | Agent on a machine | Agent in the codebase |
| Examples | Azure Bot, Teams app, API keys, domain, App Store | Node, Git, Docker, SDKs | Implement feature X |
| Secrets | **Never** paste keys here — only “create → put in `.env` / vault” | No secrets | No secrets |

**Agent role:** Draft and update rows when work is blocked on procurement. Link from feature TODOs. Do **not** mark items done unless the user said they finished. Do **not** invent purchases or accounts the project does not need.

**Human role:** Work the open items; mark **done** when complete; tell the agent so feature TODOs can unblock.

---

## Open

| Need | Blocks | Owner | Where / how | Status | Notes |
|------|--------|-------|-------------|--------|-------|
| [e.g. Entra app registration + client secret] | [GraphAuth](features/GraphAuth-TODO.md) | You / IT | Entra admin center | open | Secret → `.env` / Key Vault — **not** this file |
| [e.g. Azure Bot + Teams channel] | [TeamsBot](features/TeamsBot-TODO.md) | You | Azure Portal → Bot Service | open | |
| [Add rows as discovered] | | | | open \| waiting \| done | |

**Status values:** `open` · `waiting` (on someone else) · `done`

---

## Done

Move finished rows here (or check them off) so the open list stays short.

| Need | Completed | Notes |
|------|-----------|-------|
| [e.g. Vendor API key created] | YYYY-MM-DD | Stored in local `.env` |

---

## Instructions for AI Agents

- When implementation or Understanding implies an account, key, portal registration, purchase, or org approval → **add a row** here (if missing) and set feature TODO **Blocked by** to this file + the row name.
- Prefer **one project list** — do not duplicate the same procurement item into every feature TODO; **link** instead.
- Never write API keys, passwords, connection strings, or tokens into this file (or any docs file).
- Do not mark **done** from assumptions (“probably already have a key”) — only when the user confirms.
- Distinguish from [`Tooling.md`](Tooling.md): installable CLIs/SDKs go there; human portal/account work goes here.
- On bootstrap: create this file (can start nearly empty). Add rows when the conversation or Document Map implies external dependencies.
- If the user asks “what’s left that I need to do?” — summarize **Open** from this file.

**Instructions for Humans**

- This is your procurement / setup checklist — not for the agent to complete.
- Keep secrets out of git; use `.env.example` for variable *names* only.
- After finishing an item, mark it done and tell the agent which features can proceed.

---

*Part of the Lean Modular Documentation system. Keep Open short — one row per real external need.*
