# Setting Up Modular Docs in Your Project

Add [Agentic Doc Templates](https://github.com/BrianCLowe/Agentic-Doc-Templates) to a codebase, then let the agent create the live `docs/` layout.

Short asks are enough — *bootstrap modular docs*, *draft Understanding for X*, *update the doc templates*. The agent routes to the matching playbook under `docs/templates/agent/`.

---

## 1. Get the pack

You need **`docs/templates/`** in your project (scaffolds, [`help/`](.), [`agent/`](../agent/)). Live project docs stay at `docs/` root — not inside `templates/`.

| Method | Notes |
|--------|--------|
| **Download release ZIP** | [Releases](https://github.com/BrianCLowe/Agentic-Doc-Templates/releases) → `agentic-doc-templates-X.Y.Z.zip` (not “Source code”) → extract into project root |
| **Copy `docs/templates/` only** | **Recommended** for existing apps — no pack root README/LICENSE/CONTRIBUTING collision |
| **Use this template** | New GitHub repo from the green button |
| **Clone → rename → change remote** | New local app from a full clone; point `origin` at your empty repo |
| Git submodule | Awkward path; still prefer copying or sparse-checkout of `docs/templates/` |

Whole-repo / template installs: bootstrap auto-moves clearly upstream root files into `docs/templates/agent/upstream/` and deletes Agentic-only `.github/ISSUE_TEMPLATE/`, `.github/workflows/release.yml` / `pack-checks.yml`, root `eval/`, root `scripts/gen_role_adapters.py`, and any leftover `docs/templates/agent/scripts/*.py`. Short acquisition table also on the [upstream README — Get started](https://github.com/BrianCLowe/Agentic-Doc-Templates#get-started).

**Inside the pack:** `help/` (this guide), `agent/` (bootstrap, rules, sync), plus `VERSION`, `CHANGELOG.md`, and the scaffold templates at the pack root.

---

## 2. Bootstrap

Ask your agent:

> Bootstrap modular docs using `docs/templates/agent/BOOTSTRAP.md`.

That creates `Master_Index.md`, `Tooling.md`, `Human-TODO.md`, `reference/` (for **chat exports** / design docs), feature/shared folders, records **project preferences in one batch** (docs profile, sync mode, orchestrator git, optional update-check / doc-roles — agent must present and explain each), and the **profile default file set** for every Document Map row named in the bootstrap conversation (always spec + TODO; Understanding when the profile requires it — skip file creation if you named no features yet).

**Recommended habit** *(after bootstrap creates `docs/reference/`):* export idea conversations (Grok.com, ChatGPT, …) to markdown and drop them there — often many threads. Then ask: *Build or update the live docs from `docs/reference/`.* That preserves whys/motives better than a polished design doc alone ([`IDEA_CAPTURE_TIPS.md`](IDEA_CAPTURE_TIPS.md)). Bootstrap alone does not require exports first; building from `reference/` is the follow-up that fills rich Understandings (or thin specs under **ship-first**).

Then you:

1. Drop / add `reference/` exports if you have them, then ask the agent to build or update live docs from that folder.
2. Correct overview, Document Map, Tooling, Human-TODO, and **docs profile** if you want a different ceremony level.
3. Review draft `-Understanding.md` files before implementation when your profile uses them (**prevent** default).
4. Optionally install the modular doc rule — *Follow `docs/templates/agent/RULE_INSTALL.md`* (dispatches to [`../agent/tools/`](../agent/tools/README.md)).
5. Optionally enable **doc roles** (Understanding author, etc.) — bootstrap asks; details: [`../agent/roles/README.md`](../agent/roles/README.md).

**Cursor:** Disable **Compound Engineering** / **Superpowers** if they override the modular rule — [`../agent/tools/cursor.md`](../agent/tools/cursor.md). **Grok Build:** roles go under `.grok/agents/` — [`../agent/tools/grok-build.md`](../agent/tools/grok-build.md).

---

## 3. Folder layout after bootstrap

```
docs/
├── Master_Index.md              ← project map (you maintain)
├── Tooling.md                   ← machine tools (not package deps)
├── Human-TODO.md                ← human inbox (procure, playtest, decide, waiting)
├── ADT-settings.yaml            ← pack prefs (profile, git, standing notes, tools, optionals, sync, upstream)
├── reference/                   ← design docs, chat exports, PRDs, legacy specs
│   └── visuals/                 ← optional inspiration screenshots
├── _shared/ + assets/
├── features/ + assets/
├── decisions/                   ← optional
└── templates/                   ← this pack (overwrite on sync; not live content)
    ├── VERSION / CHANGELOG.md
    ├── help/ · agent/
    └── … scaffolds + agent/Modular_Docs_Workflow.md (index) + agent/workflow/
```

Naming: [`../agent/workflow/naming-layout.md`](../agent/workflow/naming-layout.md) §0. Path A/B: [`../agent/workflow/implement.md`](../agent/workflow/implement.md) §3. Index: [`../agent/Modular_Docs_Workflow.md`](../agent/Modular_Docs_Workflow.md).

---

## 4. Next

| Goal | Go here |
|------|---------|
| Day-to-day (chat → docs, mid-build ideas, design docs) | [`USAGE.md`](USAGE.md) |
| Optional roles (intent-first Understanding, implement, sync) | [`../agent/roles/README.md`](../agent/roles/README.md) |
| Describing UI / scope (esp. if new to software) | [`IDEA_CAPTURE_TIPS.md`](IDEA_CAPTURE_TIPS.md) |
| Rule / harness install (Cursor, Grok Build, …) | [`../agent/tools/README.md`](../agent/tools/README.md) · human TOC: [`USING_WITH_AGENTS.md`](USING_WITH_AGENTS.md) |
| Brainstorm in Grok/ChatGPT before a repo | Export chats → `docs/reference/` — [`IDEA_CAPTURE_TIPS.md`](IDEA_CAPTURE_TIPS.md#recommended-export-idea-chats-into-docsreference) |
| Later: refresh the pack | *Update the doc templates…* — [`TEMPLATE_SYNC.md`](../agent/TEMPLATE_SYNC.md) / [`CHANGELOG.md`](../CHANGELOG.md). If your pack is pre-**1.2** (no sync file), copy `docs/templates/` once first. |
| Version-only ping | *Check for template updates* — [`TEMPLATE_UPDATE_CHECK.md`](../agent/TEMPLATE_UPDATE_CHECK.md) |

After bootstrap, skim `docs/Human-TODO.md` — your inbox for keys, playtests, decisions, and external waiting.

---

## License

[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). Full text: [LICENSE.md on GitHub](https://github.com/BrianCLowe/Agentic-Doc-Templates/blob/main/LICENSE.md) (or under `docs/templates/agent/upstream/` if you kept a copy).

> Based on [Agentic Doc Templates](https://github.com/BrianCLowe/Agentic-Doc-Templates) by Brian Lowe, licensed under CC BY 4.0.
