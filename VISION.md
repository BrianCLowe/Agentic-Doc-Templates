# Agentic Doc Templates — Pack vision

> Maintainer file for **this** repo: the ideal whole we are working toward. Not a feature spec, not the changelog, not [`DECISIONS.md`](DECISIONS.md) (that file is “do not silently undo”). Bootstrap **Step 1d deletes** this file from whole-repo user copies. Not in the release zip.

**Status**: confirmed  
**Last Updated**: 2026-09-23  
**Related**: [README.md](README.md) · [DECISIONS.md](DECISIONS.md)

Confirmed 2026-09-23. There is no `docs/reference/` of idea threads — the product was worked out in the templates, decisions, and playbooks over time. This file is the target. Do not treat the current file tree as the target.

---

## What this product is

A **repo-owned docs kit and a set of short playbooks** that any coding agent reads and updates, so the product you meant survives the next chat and the next tool.

It is for someone building software with agents (Cursor, Grok Build, Claude Code, Copilot, OpenClaw, and the next one) who is tired of intent living only in a thread. One small `docs/` map holds what the product is, what each piece is, and what to do next. One short ask routes to one playbook. You still pick the agent. The pack is what that agent is accountable to.

The feel is a **shared notebook with a paved path**: you can open any file and correct it; the agent, after it forgets, re-opens the path instead of inventing a process. The path is only as long as the pack needs to keep intent. It does not recruit you into a bigger process than that.

## What this product is NOT

- NOT a coding-agent runtime, harness, or replacement for Cursor / Claude / Grok / Copilot
- NOT a hosted project tool (Notion, Linear, a ticket system, a memory database)
- NOT one always-on mega-rule that tries to be the whole process, or a dump of every instruction into the session “just in case”
- NOT a single mandatory way of working past what the pack needs in order to function
- NOT a second codebase of ceremony that makes a typed API wait for a shape sermon
- NOT a pile of templates that happen to share a repo, with no single product they are for

## End-state picture

You have an idea, not a process to maintain. You drop the messy threads into the repo (or talk the idea through in the IDE) and say *bootstrap*. Once, the agent asks how this product should be documented — including whether identity is expensive to get wrong — and writes that choice down.

From then on, a sitting looks the same no matter which agent you opened. You say a short thing: draft the shape, continue the current slice, run until blocked, refresh the templates. The agent opens one playbook, reads the one picture of the whole product and the one slice that is next, and does that. It does not rebuild your product from last month’s chat, and it does not “helpfully” start a second product beside the one you confirmed.

Anything the pack can function without stays optional. You turn those pieces on when you want them. When you need the agent to run this pack differently and there is no setting for it, a standing directive records that override. When you tell it how to act in the repo and that is not a pack playbook, it asks whether that should be an always-on rule or a skill it opens when the work comes up. It does not file that in standing. The pack does not quiz you into its own habits. A menu of slash commands is one of those optionals: `/sync` and `/orchestrate` for people who want to pick the ask instead of remembering the sentence. Declining them leaves the short ask as the only path.

The main session stays thin on purpose. Each instruction lives in one place. The agent is guided there when the ask needs it, and does not carry the rest of the pack in memory. When doc roles are installed, heavier moments go to a role so the parent session does not swell to hold them. Without that install, the same work stays in the parent.

When the slice is something a person uses, done means you can run it — not that a library checklist is ticked. When you leave it overnight, related work lands as reviewable changes you can merge in the morning. When this pack itself gets better, one ask refreshes the playbooks and catches your live docs up, and your product’s intent stays yours. That refresh is two steps: first the templates are replaced, then catch-up runs from the instructions that just arrived. Catch-up is not an old procedure sitting in the same file the agent already decided was stale — that is what happened when sync was one file, and the split exists so it does not happen again.

The docs stay small enough to correct in a minute. The playbooks stay the procedure, so a new session does not have to remember how the pack works.

## How the map fits

These are the pieces that already exist in the pack, and the role each one plays in that sitting.

| Stem | Role in the whole |
|------|-------------------|
| Live scaffolds (Master Index, Product vision, Understanding, spec, TODO, Tooling, Human-TODO) | The notebook: fill-in blanks a human can correct. Teaching does not live here. |
| Docs profiles (`prevent` · `build-first` · `balanced`) | The one choice of how hard identity is gated. Build-first is the right path when the contract already is the shape. |
| Optional settings | Pieces the pack can run without. Off until you want them, so one process is not forced on you. Slash commands (`/sync`, `/orchestrate`) are one of these. |
| Standing directives | Your lasting override of a pack playbook when no setting exists. Repo behavior that is not a pack playbook is asked as a rule or a skill. |
| `help/` | How a human uses the notebook. |
| `agent/` workflow modules + installable rules | The paved path, one module at a time. Instructions stay in that one place; the session loads them when the ask needs them. |
| Optional doc roles | If installed, heavier moments leave the parent session. That is a reason to turn them on. Opt-in, never always-on. Bootstrap and the long loop stay in the parent. |
| Template sync A, then B | A replaces the pack. B is the catch-up in the pack you just installed, so those instructions are current and are not discarded as stale. |
| `VERSION` + `CHANGELOG` | How a later pack reaches a project that already has live docs, without a second bootstrap. |
| Root `DECISIONS.md` | Why a pack choice must not be silently undone. Archaeology stays in the changelog. |
| Root `eval/` | Proof the paved path still catches the failures we have already seen. Stays upstream; not part of a user’s app. |

## Assumptions (real forks only)

## Confirmed with user

- 2026-09-23 — Drafted for review from the pack (no reference threads).
- 2026-09-23 — Corrected: do not force a process past what the pack needs (optionals + standing); sync is A then B so catch-up is the new instructions, not a stale single file; token efficiency — one home for each instruction, loaded when needed; roles slim the main session **if installed**.
- 2026-09-23 — Confirmed the whole picture, including build-first, optional `/sync` and `/orchestrate`, and repo behavior that is not a pack playbook asked as a rule or a skill.
