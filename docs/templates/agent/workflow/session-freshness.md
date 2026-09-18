> **Workflow module.** Open from the [workflow index](../Modular_Docs_Workflow.md) when session-start **docs freshness** flags a dirty sibling worktree, stale `docs/`, you are about to merge/overwrite live docs, or you would open a **new PR / spawn another coding agent** for a successive issue. Cheap checks live on the **session-default** path — do not open this file when `git status` + one worktree are clean **and** you are not opening a new PR.

# 0.3 Session freshness — docs as source of truth

The pack’s promise is that **live docs are the source of truth across sessions**. That promise holds only when this checkout’s `docs/` is the work the user means — **committed, or the WIP in this tree**, not eight commits behind a sibling worktree.

TEMPLATE_SYNC [A0](../TEMPLATE_SYNC_A.md) already hard-stops a dirty tree before overwrite. This module is the **same lesson on the session-default path**: one `git status` (and a worktree list) before treating Master Index / TODOs as current.

**Not this module:** host isolation / stay-in-this-tree / do-not-`git worktree add` → [`../roles/orchestrator-git.md`](../roles/orchestrator-git.md) **Host worktrees**. Stay ≠ current.

---

## Cheap check *(once per session, before reading docs as current)*

If this project is **not** a git repo → continue (no check).

Run:

```bash
git status --porcelain
git worktree list
```

| State | Action |
|-------|--------|
| Clean + **one** worktree | Continue. Optional one line: *docs freshness: ok*. |
| Dirty **this** tree | One line: *this tree has uncommitted work* (list `docs/` paths if any). Treat on-disk docs as possibly **newer** than `HEAD`. **Continue** — this may be the user’s WIP. Do **not** auto-commit. |
| **Two or more** worktrees (or linked/host worktree) | Do the **sibling probe** below before trusting Master Index / TODOs. |

**Linked/host detect** (same cheap signals as orchestrator-git): `git rev-parse --git-common-dir` differs from `--git-dir`; cwd under `~/.cursor/worktrees`, `~/.grok/worktrees`, or `.claude/worktrees`; session started via `/worktree` / `grok -w` / Copilot New Worktree / `claude --worktree`. Cloud Agent VM + branch is **not** a git worktree — still run `git status`; skip sibling probe unless `git worktree list` shows more than one.

---

## Sibling probe *(only when `git worktree list` has more than one entry)*

For **each other** worktree path:

```bash
git -C <other> status --porcelain -- docs
git log --oneline HEAD..<other-HEAD> -- docs
```

(`<other-HEAD>` = `git -C <other> rev-parse HEAD`.)

| Finding | Action |
|---------|--------|
| Other tree has **uncommitted `docs/`** | **Hard stop.** |
| This `HEAD` **lacks `docs/` commits** the other tree has | **Hard stop.** |
| Neither | Continue. One line: *docs freshness: no sibling docs drift*. |

On **hard stop**:

1. Name the other path, its branch, and what is newer (uncommitted `docs/` and/or commit subjects).
2. Explain: Master Index / TODOs in **this** tree may be stale; implementing or merging from here can **regress** the user’s other tree (the A0 reason — mix or overwrite real work).
3. **Ask** which tree is current. Do **not** auto-commit, stash, merge, rebase, or checkout default in a host worktree.
4. **Stop** until they choose: switch/continue in the current tree · they will commit/merge · explicit waive (warn that you may regress sibling `docs/`).

Re-run the cheap check after they say continue.

---

## Before merge / overwrite that touches live docs

Re-run the cheap check (and sibling probe if multiple worktrees) **again** before merging a branch or replacing `docs/` files. A tree that was clean at session start can still be behind a sibling that received new `docs/` work mid-session.

TEMPLATE_SYNC overwrite still uses **A0** (hard stop on dirty **this** tree) — this module does not replace A0.

---

## Docs-overlapping PRs *(before a new PR or a successive spawn)*

Live docs (`*-TODO.md` **Current focus**, spec Decisions, Understanding, Human-TODO, Master Index) are rewritten every implement session. Two open PRs that touch the **same stem’s docs** conflict when the first merges — even if their **code** files do not overlap. That is the Grok-bot / successive-issue failure: a new coding agent + new PR per complaint, all rewriting the same TODO.

**Cheap check** (when you would open a new PR, spawn another coding agent, or the user filed another issue/complaint in this parent session):

```bash
gh pr list --state open
# or glab / the inferred forge CLI
```

If an open PR already lists this stem’s `*-TODO.md`, spec, or Understanding (or Human-TODO / Master Index you would also edit):

| Who | Action |
|-----|--------|
| This session | **Add commits to that PR.** Checkout its branch (main checkout) or keep working in this host worktree **on that branch**. Do **not** open a second PR. |
| Grok / parent that `spawn_subagent`s coding agents | Do **not** spawn a new agent+branch+PR for this successive issue. Re-brief the in-flight agent or add to its PR. Remember **stem → open PR** for the rest of this parent session. |

**Overlap test is docs, not only code** (docs overlap ≠ code overlap). Different `src/` files + same `features/Foo-TODO.md` = overlap. Same-stem default is **one PR**.

**Not overlap:** different stems, and you will not edit the other PR’s TODO / spec / Understanding / Human-TODO / Master Index.

Project-wide files (Human-TODO, Master Index, Product-Vision): if an open PR already touches them → add there. If none does → keep the edit on **this** PR. Do **not** open a docs-only second PR.

**Not this section:** orchestrator **milestone** sizing (do not dump the whole night into one PR) → [`../roles/orchestrator-git.md`](../roles/orchestrator-git.md). This gate is **do not stack PRs that will rebase-conflict on `docs/`**.

---

## Do not

- Skip the cheap check because Master Index / Current focus “looks recent”
- Treat **already-in-a-worktree → stay** as “this tree’s docs are current”
- Hard-stop ordinary implement solely because **this** tree is dirty (that is A0’s overwrite gate, not this one)
- Hard-stop because the **main** checkout is dirty when **this** linked/host worktree is clean **and** the sibling probe found no `docs/` drift
- Auto-commit / stash / merge to “fix” freshness
- `git worktree add` / remove a host worktree
- Checkout default in a host/linked worktree
- Scan every file under every worktree — porcelain + `git log -- docs` is enough
- Open this module when the cheap freshness check is clean **and** you are not opening a new PR
- Open a second PR because the **code** files differ while the same `*-TODO.md` / spec / Understanding would change
- Spawn a new Grok/coding agent + new PR for a successive complaint on a stem that already has an open PR
- Treat “items do not share code files” as permission to parallelize same-stem **docs**
