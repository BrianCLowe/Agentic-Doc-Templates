# Chat UI — Create modular docs (no repo workspace)

Use this folder when the agent **cannot write to a project** — Grok.com, ChatGPT, Claude web, etc. The agent outputs markdown files you **save or download** into your repo later.

## What to attach

| Priority | File | Purpose |
|----------|------|---------|
| **Required** | [`AGENT.md`](AGENT.md) | Short instructions — file paths, naming, output format |
| Optional | [`../Master_Index_Template.md`](../Master_Index_Template.md) | Document Map table shape |
| Optional | [`../Feature_Understanding_Template.md`](../Feature_Understanding_Template.md) | Understanding sections |
| Optional | [`../help/IDEA_CAPTURE_TIPS.md`](../help/IDEA_CAPTURE_TIPS.md) | If the user's idea is still vague |

**Do not** attach the whole `docs/templates/` folder to chat unless the UI handles it well — too many files dilute focus. Start with **AGENT.md** only.

## Example prompt (Grok / ChatGPT)

> Follow `AGENT.md` from Agentic Doc Templates. Turn our conversation into modular documentation for [app name]. Output each file with its full repo path so I can save them under `docs/`. Draft `-Understanding.md` files first — I'll review before you write specs or TODOs.

With repo connector:

> Read `docs/templates/chat-ui/AGENT.md` in [Agentic-Doc-Templates](https://github.com/BrianCLowe/Agentic-Doc-Templates). Create docs from our chat using the paths in AGENT.md.

## After download

1. Create `docs/` in your project and paste files at the paths the agent used.
2. Copy `docs/templates/` from this repo (or bootstrap) for IDE work later.
3. Install the modular doc rule in Cursor/Grok Build when you have a workspace — see [`../agent/RULE_INSTALL.md`](../agent/RULE_INSTALL.md).

Full procedure (Path A/B, graduation, session handoff): [`../Modular_Docs_Workflow.md`](../Modular_Docs_Workflow.md) — for IDE agents, not chat-only sessions.
