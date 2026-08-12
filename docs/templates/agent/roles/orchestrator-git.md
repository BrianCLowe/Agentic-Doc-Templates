# Orchestrator — Git delivery *(companion to orchestrator.md)*

> **Not a harness subagent.** Parent opens this when resolving/running **`orchestrator.git.mode`**. Main loop: [`orchestrator.md`](orchestrator.md). Build verify: [`../Agent_Build_Verify_Rule.mdc`](../Agent_Build_Verify_Rule.mdc). Todo honesty: [`todo-warden.md`](todo-warden.md).

**Live setting:** `docs/ADT-settings.yaml` → `orchestrator.git.mode` (example: [`../ADT-settings.example.yaml`](../ADT-settings.example.yaml)).

## Modes

| Mode | Commits | Branch | Push | PR / close-out |
|------|---------|--------|------|----------------|
| **`local`** | Milestone after verify pass | Current | No | No |
| **`branch-pr`** | Same | Run branch | Yes | Draft mid-run → **close-out** (no merge; keeps milestone history) |
| **`branch-pr-squash`** | Same | Run branch | Yes | Same + **squash after green verify, before ready** — **recommend** when remote + forge (Bugbot / tip-only / HEAD-only review sees the full run) |
| **`branch-push`** | Same | Run branch | Yes | No PR |
| **`current-push`** | Same | **Current** (often main) | Yes | No PR — **never silent-default** |
| **`none`** | No | — | No | No |

**PR modes:** end-of-run **mark ready** by default (unattended checks). Override only if user said *leave draft* / *keep draft*.

### Cloud Agent path *(remote unattended — does not rewrite settings)*

**Why:** Durable `orchestrator.git.mode` is often **`local`** / **`none`** / **`branch-push`** for IDE work on a laptop. A **Cloud Agent** (Cursor Cloud or similar remote VM whose platform instructions require feature-branch + PR delivery) still needs a PR so CI/Bugbot can see the run. Tip-only bots need a **squash** tip — so the cloud effective mode is **`branch-pr-squash`**.

**Detect Cloud Agent:** session is a remote/unattended cloud run with platform branch+PR obligations — **not** local IDE Composer / desktop agent / user laptop CLI. If unsure → **not** cloud (follow durable mode / ask).

**This-run effective mode** *(before first dispatch; do **not** write `docs/ADT-settings.yaml`)*:

| Durable `orchestrator.git.mode` | Cloud this-run |
|---------------------------------|----------------|
| unset / **`local`** / **`none`** / **`branch-push`** / **`current-push`** / **`branch-pr`** | **`branch-pr-squash`** |
| **`branch-pr-squash`** | **`branch-pr-squash`** (no change) |

One line: *Git: `branch-pr-squash` (cloud this-run; durable setting remains `<mode|unset>`)*. Then forge probe + normal PR close-out (including squash).

**User wins:** explicit this-run order (*use local this run* / *no PR* / *branch-pr only* / *leave draft*) overrides the cloud default. Still **do not** rewrite ADT-settings unless they asked to change the durable default.

**Not this path:** local IDE orchestration — honor durable mode even if the machine has `gh`. Template sync / non-orchestrate playbooks — unchanged.

### Resolve mode *(before first dispatch)*

1. Read `orchestrator.git.mode`.
2. **Cloud Agent?** → apply **Cloud Agent path** above (this-run effective mode); skip steps 3–4 for mode choice; continue at forge probe. Else step 3.
3. **If set** → use it (unless this-run-only override). One line: *Git: `<mode>`*. Probe forge if PR mode (or first run after mode change).
4. **If unset** → **ask once** (recommend):
   - remote + forge CLI → **`branch-pr-squash`** (Bugbot / tip-only bots only see HEAD; squash makes the full run one tip before mark ready). Offer plain **`branch-pr`** if they want to keep milestone commits on the PR
   - remote, no CLI → **`branch-pr-squash`** + install ask, or **`branch-push`**
   - no remote → **`local`** (or **`none`**)
   - **`current-push`** only as explicit solo option
5. Record `mode` + `recorded` (+ `source`) unless *this run only* / cloud this-run override.
6. **Forge tooling probe** (below).
7. Later: *Set orchestrator git to local|branch-pr|branch-pr-squash|branch-push|current-push|none*.

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
| `branch-pr` / `branch-pr-squash` / `branch-push` | Non-default **intentional** feature branch → **stay** (record `branch_origin: pre-existing`). Else create `orchestrate/YYYY-MM-DD-<scope>` (record `branch_origin: created`) |
| `local` / `current-push` | Stay on current branch (`branch_origin: n/a`) |
| `none` | No branch setup |

**Remember for end-of-run:** whether this run **created** the branch vs **stayed** on a pre-existing one. That drives **return to default** (below).

### During the loop

- **Commit** (not `none`): parent, after work-verifier **pass** — one milestone per unit/batch. No secrets; no force-push mid-loop.
- **Push** (`branch-pr*`, `branch-push`, `current-push`): after milestones (or every few if slow).
- **PR modes:** after first push, open **draft** PR if missing (scope + “orchestrator run”). Stay draft mid-run. No CLI → push + “open PR in browser.”
- **`current-push` rejected:** stop delivery; offer once to fall back to `branch-pr-squash` (or `branch-pr`) this run — no silent mode switch.

### End of run *(non-PR)*

- Include human-verify-map doc commit if it dirtied the tree.
- **`branch-push`:** push remaining; report branch name used for the run.
- **`current-push`:** push; report.
- **`local` / `none`:** report commits/dirty; no push.
- **Never merge.** Force-push only as **force-with-lease** in squash step below.
- Then **return to default branch** (below) when applicable.

### PR close-out *(branch-pr / branch-pr-squash — strict order)*

After agent work done (+ human-verify-map committed if needed). **Do not reorder.**

1. **Final push** — remote matches local.
2. **Build verify** *(gate)* — [`Agent_Build_Verify_Rule.mdc`](../Agent_Build_Verify_Rule.mdc) / Tooling **Project verify**. Fix → re-run until green, or stop (leave **draft**, report block).  
   **Do not** warden / squash / mark ready while red. If stopping here with a clean tree → still **return to default** (step 6), then report.
3. **Todo warden** *(docs-only; after green)* — if this run cleared implementer units: spawn `todo-warden` or follow [`todo-warden.md`](todo-warden.md). Brief: in-scope stems + claimed-done list; mode **honesty+hygiene** (reopen/add gaps **and** move parked `[x]` into Completed).  
   - **`gaps-found`:** commit TODOs, push, **leave draft**, **skip squash + ready**; then **return to default** (run branch remains on remote). Optional re-loop if budget — if re-looping, **stay** on run branch until that loop’s close-out.  
   - **`clean`:** continue.  
   - No code units this run → skip warden.
4. **Squash** *(`branch-pr-squash` only; after 2 green + 3 clean)* — one commit on **run branch** (not default); subject = run scope; **`--force-with-lease` only**. Unsafe history → skip squash, note, continue.
5. **Mark ready** *(default)* — after 2 green, 3 clean/skipped, 4 done/skipped. Skip if *leave draft*, verify never green, or warden **gaps-found**.
6. **Return to default branch** — see below (after this run’s work on the run branch is finished).
7. **Report** — run branch, PR URL, draft/ready, squash?, verify, warden, CI if cheap, **current HEAD** (e.g. *now on `main`; was `orchestrate/…`*).

**Order why:** green build → honest backlog → optional single HEAD → invite checks → leave the machine on the default branch so the next ask is not on a closed/merged/stale PR tip.

### Return to default branch *(end of run — default when this run created the branch)*

**Purpose:** After orchestration, local HEAD should not stay on a disposable `orchestrate/…` (or equivalent) so the next ask (template sync, casual fix) does not land on a closed/merged PR branch.

| Case | Action |
|------|--------|
| This run **created** the run branch (`branch_origin: created`) | **Default:** `git checkout` repo default (`main` / `master` / `git symbolic-ref refs/remotes/origin/HEAD` / forge default). Optional cheap `git pull --ff-only` on default if clean and tracking exists — do not merge/rebase fights. |
| This run **stayed** on a pre-existing intentional feature branch | **Do not** auto-checkout default (user may still be building that feature). One line in report: *stayed on `<branch>` (pre-existing)*. |
| User said *stay on this branch* / *this run only stay here* | Skip return. |
| Working tree **dirty** with uncommitted work | **Do not** checkout away — report dirty + stay; ask commit/stash if needed. |
| `local` / `current-push` / `none` / never left default | Skip (already on default or no branch hop). |
| `branch-push` with **created** branch | Same as created: return to default after final push (+ warden if any). |

**When:** **Last** git step after this run’s delivery for the branch is done (final push, close-out steps 1–5 as applicable, including gaps-found push). **Never** checkout default *before* final push / squash / mark-ready on the run branch.

**Do not:** delete the run branch locally/remotely unless the user asked; merge the PR; force-checkout over dirty files.

### Non-PR + warden

After loop (+ human verify map): if implementer units shipped → run **todo-warden** once. **gaps-found** → commit TODOs when mode allows commits; do not claim stem/Layer drained. Then **return to default** when `branch_origin: created`.

### Grants / do not

- Mode (or this-run / **Cloud Agent** override) grants **only** that effective mode’s commit/push/PR for **orchestration**.
- Not a grant for template sync or other playbooks.
- **Do not:** merge PRs; bare `--force`; silent-default `current-push`; invent forge; store tokens; rewrite durable `orchestrator.git.mode` because of a Cloud Agent this-run; leave HEAD on an orchestrator-created branch after a finished run without reporting it.
