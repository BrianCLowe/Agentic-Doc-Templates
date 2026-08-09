# Orchestrator — Git delivery *(companion to orchestrator.md)*

> **Not a harness subagent.** Parent opens this when resolving/running **`orchestrator.git.mode`**. Main loop: [`orchestrator.md`](orchestrator.md). Build verify: [`../Agent_Build_Verify_Rule.mdc`](../Agent_Build_Verify_Rule.mdc). Todo honesty: [`todo-warden.md`](todo-warden.md).

**Live setting:** `docs/ADT-settings.yaml` → `orchestrator.git.mode` (example: [`../ADT-settings.example.yaml`](../ADT-settings.example.yaml)).

## Modes

| Mode | Commits | Branch | Push | PR / close-out |
|------|---------|--------|------|----------------|
| **`local`** | Milestone after verify pass | Current | No | No |
| **`branch-pr`** | Same | Run branch | Yes | Draft mid-run → **close-out** (no merge) |
| **`branch-pr-squash`** | Same | Run branch | Yes | Same + **squash after green verify, before ready** (tip-only bots / HEAD-only review) |
| **`branch-push`** | Same | Run branch | Yes | No PR |
| **`current-push`** | Same | **Current** (often main) | Yes | No PR — **never silent-default** |
| **`none`** | No | — | No | No |

**PR modes:** end-of-run **mark ready** by default (unattended checks). Override only if user said *leave draft* / *keep draft*.

### Resolve mode *(before first dispatch)*

1. Read `orchestrator.git.mode`.
2. **If set** → use it (unless this-run-only override). One line: *Git: `<mode>`*. Probe forge if PR mode (or first run after mode change).
3. **If unset** → **ask once** (recommend):
   - remote + forge CLI → **`branch-pr`** (offer **`branch-pr-squash`** for tip-only bots)
   - remote, no CLI → **`branch-pr`** + install ask, or **`branch-push`**
   - no remote → **`local`** (or **`none`**)
   - **`current-push`** only as explicit solo option
4. Record `mode` + `recorded` (+ `source`) unless *this run only*.
5. **Forge tooling probe** (below).
6. Later: *Set orchestrator git to local|branch-pr|branch-pr-squash|branch-push|current-push|none*.

### Forge tooling probe

**When:** mode pick/change (bootstrap 3p **E**, sync B0.6, orchestrate start for PR modes).

**Infer CLI from remote** (do not ask which forge):

| Remote | CLI |
|--------|-----|
| github.com / GHE | `gh` |
| gitlab | `glab` |
| Azure DevOps | `az` when available |
| Unknown / none | no forge CLI |

**Checks (cheap):** `git`; for PR modes — CLI on PATH + auth status if easy.

**PR mode + CLI missing/unauthed:** say so; **ask once** — install, skip (push + human PR), or switch mode. Install ≠ login: after install, **ask** before `gh auth login` / equivalent. No silent install/auth; no tokens in docs. Missing CLI is not a hard bootstrap failure.

### Start of run *(after mode resolved)*

| Check | Action |
|-------|--------|
| Not a git repo | Treat as **`none`** this run |
| Dirty **unrelated** WIP | **Hard stop** — commit/stash/waive (TEMPLATE_SYNC A0 spirit) |
| `branch-pr` / `branch-pr-squash` / `branch-push` | Non-default intentional branch → **stay**; else create `orchestrate/YYYY-MM-DD-<scope>` |
| `local` / `current-push` | Stay on current branch |
| `none` | No branch setup |

### During the loop

- **Commit** (not `none`): parent, after work-verifier **pass** — one milestone per unit/batch. No secrets; no force-push mid-loop.
- **Push** (`branch-pr*`, `branch-push`, `current-push`): after milestones (or every few if slow).
- **PR modes:** after first push, open **draft** PR if missing (scope + “orchestrator run”). Stay draft mid-run. No CLI → push + “open PR in browser.”
- **`current-push` rejected:** stop delivery; offer once to fall back to `branch-pr` this run — no silent mode switch.

### End of run *(non-PR)*

- Include human-verify-map doc commit if it dirtied the tree.
- **`branch-push`:** push remaining; report branch.
- **`current-push`:** push; report.
- **`local` / `none`:** report commits/dirty; no push.
- **Never merge.** Force-push only as **force-with-lease** in squash step below.

### PR close-out *(branch-pr / branch-pr-squash — strict order)*

After agent work done (+ human-verify-map committed if needed). **Do not reorder.**

1. **Final push** — remote matches local.
2. **Build verify** *(gate)* — [`Agent_Build_Verify_Rule.mdc`](../Agent_Build_Verify_Rule.mdc) / Tooling **Project verify**. Fix → re-run until green, or stop (leave **draft**, report block).  
   **Do not** warden / squash / mark ready while red.
3. **Todo warden** *(docs-only; after green)* — if this run cleared implementer units: spawn `todo-warden` or follow [`todo-warden.md`](todo-warden.md). Brief: in-scope stems + claimed-done list.  
   - **`gaps-found`:** commit TODOs, push, **leave draft**, **skip squash + ready**, report; optional re-loop if budget.  
   - **`clean`:** continue.  
   - No code units this run → skip warden.
4. **Squash** *(`branch-pr-squash` only; after 2 green + 3 clean)* — one commit on **run branch** (not default); subject = run scope; **`--force-with-lease` only**. Unsafe history → skip squash, note, continue.
5. **Mark ready** *(default)* — after 2 green, 3 clean/skipped, 4 done/skipped. Skip if *leave draft*, verify never green, or warden **gaps-found**.
6. **Report** — branch, PR URL, draft/ready, squash?, verify, warden, CI if cheap.

**Order why:** green build → honest backlog → optional single HEAD → invite checks.

### Non-PR + warden

After loop (+ human verify map): if implementer units shipped → run **todo-warden** once. **gaps-found** → commit TODOs when mode allows commits; do not claim stem/Layer drained.

### Grants / do not

- Mode (or this-run override) grants **only** that mode’s commit/push/PR for **orchestration**.
- Not a grant for template sync or other playbooks.
- **Do not:** merge PRs; bare `--force`; silent-default `current-push`; invent forge; store tokens.
