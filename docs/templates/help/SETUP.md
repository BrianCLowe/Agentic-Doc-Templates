# Setting Up Modular Docs in Your Project

Add [Agentic Doc Templates](https://github.com/BrianCLowe/Agentic-Doc-Templates) to a codebase, then let the agent create the live `docs/` layout.

Short asks are enough — *bootstrap modular docs*, *draft Understanding for X*, *update the doc templates*. The agent routes to the matching playbook under `docs/templates/agent/`.

---

## 1. Copy the pack

Copy **`docs/templates/`** into your project as **`your-project/docs/templates/`**.

That one folder includes scaffolds, [`help/`](.), [`agent/`](../agent/), and [`chat-ui/`](../chat-ui/). Live project docs stay at `docs/` root — not inside `templates/`.

You do **not** need this repo’s root `README.md`, `LICENSE.md`, or `CONTRIBUTING.md` in your project. Prefer copy-only so they never land there. If a whole-repo copy left them at the root, bootstrap auto-moves clearly upstream files into `docs/templates/agent/upstream/` (you may delete those copies later; sync does not require them).

| Method | Notes |
|--------|--------|
| **Copy `docs/templates/` only** | Recommended |
| Git submodule | Awkward path; still prefer copying or sparse-checkout of `docs/templates/` |
| Whole-repo clone / “Use this template” into an app | Bootstrap cleans root pack files + deletes Agentic-only `.github/ISSUE_TEMPLATE/` and `.github/workflows/release.yml` |

**Inside the pack:** `help/` (this guide), `agent/` (bootstrap, rules, sync), `chat-ui/` (attach [`AGENT.md`](../chat-ui/AGENT.md) only), plus `VERSION`, `CHANGELOG.md`, and the scaffold templates at the pack root.

---

## 2. Bootstrap

Ask your agent:

> Bootstrap modular docs using `docs/templates/agent/BOOTSTRAP.md`.

That creates `Master_Index.md`, `Tooling.md`, `Human-TODO.md`, `reference/` (for design docs / chat exports), feature/shared folders, and **draft Understanding + stub spec + core TODO for every Document Map row**.

Then you:

1. Correct overview, Document Map, Tooling, and Human-TODO.
2. Review draft `-Understanding.md` files before implementation.
3. Optionally install the modular doc rule — *Follow `docs/templates/agent/RULE_INSTALL.md`* (dispatches to [`../agent/tools/`](../agent/tools/README.md)).
4. Optionally enable **doc roles** (Understanding author, etc.) — bootstrap asks; details: [`../agent/roles/README.md`](../agent/roles/README.md).

**Cursor:** Disable **Compound Engineering** / **Superpowers** if they override the modular rule — [`../agent/tools/cursor.md`](../agent/tools/cursor.md). **Grok Build:** roles go under `.grok/agents/` — [`../agent/tools/grok-build.md`](../agent/tools/grok-build.md).

---

## 3. Folder layout after bootstrap

```
docs/
├── Master_Index.md              ← project map (you maintain)
├── Tooling.md                   ← machine tools (not package deps)
├── Human-TODO.md                ← human inbox (procure, playtest, decide, waiting)
├── rule-install-status.yaml     ← when agent rules are installed
├── upstream-status.yaml         ← optional weekly template update ping
├── reference/                   ← design docs, chat exports, PRDs, legacy specs
│   └── visuals/                 ← optional inspiration screenshots
├── _shared/ + assets/
├── features/ + assets/
├── decisions/                   ← optional
└── templates/                   ← this pack (overwrite on sync; not live content)
    ├── VERSION / CHANGELOG.md
    ├── help/ · agent/ · chat-ui/
    └── … scaffolds + agent/Modular_Docs_Workflow.md
```

Naming and Path A/B: [`../agent/Modular_Docs_Workflow.md`](../agent/Modular_Docs_Workflow.md) §0.

---

## 4. Next

| Goal | Go here |
|------|---------|
| Day-to-day (chat → docs, mid-build ideas, design docs) | [`USAGE.md`](USAGE.md) |
| Optional roles (intent-first Understanding, implement, sync) | [`../agent/roles/README.md`](../agent/roles/README.md) |
| Describing UI / scope (esp. if new to software) | [`IDEA_CAPTURE_TIPS.md`](IDEA_CAPTURE_TIPS.md) |
| Rule / harness install (Cursor, Grok Build, …) | [`../agent/tools/README.md`](../agent/tools/README.md) · human TOC: [`USING_WITH_AGENTS.md`](USING_WITH_AGENTS.md) |
| Brainstorm in Grok/ChatGPT before a repo | [`../chat-ui/README.md`](../chat-ui/README.md) |
| Later: refresh the pack | *Update the doc templates…* — [`TEMPLATE_SYNC.md`](../agent/TEMPLATE_SYNC.md) / [`CHANGELOG.md`](../CHANGELOG.md). If your pack is pre-**1.2** (no sync file), copy `docs/templates/` once first. |
| Version-only ping | *Check for template updates* — [`TEMPLATE_UPDATE_CHECK.md`](../agent/TEMPLATE_UPDATE_CHECK.md) |

After bootstrap, skim `docs/Human-TODO.md` — your inbox for keys, playtests, decisions, and external waiting.

---

## License

[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). Full text: [LICENSE.md on GitHub](https://github.com/BrianCLowe/Agentic-Doc-Templates/blob/main/LICENSE.md) (or under `docs/templates/agent/upstream/` if you kept a copy).

> Based on [Agentic Doc Templates](https://github.com/BrianCLowe/Agentic-Doc-Templates) by Brian Lowe, licensed under CC BY 4.0.
