# Orchestrator — Git delivery *(companion to orchestrator.md)*

> **Not a harness subagent.** Parent opens this when resolving/running **`orchestrator.git.mode`**. Main loop: [`orchestrator.md`](orchestrator.md). Build verify: [`../Agent_Build_Verify_Rule.mdc`](../Agent_Build_Verify_Rule.mdc). Todo honesty: [`todo-warden.md`](todo-warden.md).

**Live setting:** `docs/ADT-settings.yaml` → `orchestrator.git.mode` (example: [`../ADT-settings.example.yaml`](../ADT-settings.example.yaml)).

## Modes

| Mode | Commits | Branch | Push | PR / close-out |
|------|---------|--------|------|----------------|
| **`milestone-pr`** | After each verify-pass unit (several TODOs may share one PR) | **New branch per milestone** | Yes | **Per milestone:** draft → build-verify → warden → **squash the whole milestone** → mark ready → **wait CI / Bugbot** → **merge** → default → next branch. A milestone may be **several related TODOs** with **concurrent implementers** when work does not overlap. **Recommend** for overnight drain + forge |
| **`local`** | Same | Current | No | No |
| **`branch-pr`** | Same | One run branch | Yes | Draft mid-run → **end-of-run close-out** (no merge; keeps milestone history) |
| **`branch-pr-squash`** | Same | One run branch | Yes | Same + **squash the whole run** before ready (one PR for human review in the morning; no merge) |
| **`branch-push`** | Same | Run branch | Yes | No PR |
| **`current-push`** | Same | **Current** (often main) | Yes | No PR — **never silent-default** |
| **`none`** | No | — | No | No |

**Why not one giant squash PR for overnight:** a multi-hour drain as a single tip is hard to review, CI/Bugbot fire only at the end, and nothing lands if the last slice fails. **`milestone-pr`** ships each **milestone** as its own PR so checks run on a reviewable diff, auto-fixes apply to that slice, and merged work is on default before the next milestone starts. A milestone is **not** locked to one TODO — group related TODOs and run concurrent implementers when they do not overlap; **squash before mark ready** so tip-only bots see the whole milestone.

**PR modes:**

| Mode | When mark ready | Merge |
|------|-----------------|-------|
| **`milestone-pr`** | After **each** milestone close-out | **Yes** — after green CI (or no CI) + Bugbot pass below |
| **`branch-pr` / `branch-pr-squash`** | **End of run** | **No** |

Override ready/merge only if user said *leave draft* / *keep draft* / *no merge*.

### Cloud Agent path *(remote unattended — does not rewrite settings)*

**Why:** Durable `orchestrator.git.mode` is often **`local`** / **`none`** / **`branch-push`** for IDE work on a laptop. A **Cloud Agent** (Cursor Cloud or similar remote VM whose platform instructions require feature-branch + PR delivery) is the overnight drain path: it needs PRs so CI/Bugbot can see each milestone, a **squash tip per PR** so tip-only bots see the **whole milestone** (not the last fix-up, and not one-TODO-only), and **merge + next branch** so work lands instead of sitting as one giant morning PR.

**Detect Cloud Agent:** session is a remote/unattended cloud run with platform branch+PR obligations — **not** local IDE Composer / desktop agent / user laptop CLI. If unsure → **not** cloud (follow durable mode / ask).

**This-run effective mode** *(before first dispatch; do **not** write `docs/ADT-settings.yaml`)*:

| Durable `orchestrator.git.mode` | Cloud this-run |
|---------------------------------|----------------|
| unset / **`local`** / **`none`** / **`branch-push`** / **`current-push`** / **`branch-pr`** / **`branch-pr-squash`** | **`milestone-pr`** |
| **`milestone-pr`** | **`milestone-pr`** (no change) |

One line: *Git: `milestone-pr` (cloud this-run; durable setting remains `<mode|unset>`)*. Then forge probe + **milestone PR cycle** (below).

**User wins:** explicit this-run order (*use local this run* / *no PR* / *one PR* / *branch-pr-squash this run* / *no merge* / *leave draft*) overrides the cloud default. Still **do not** rewrite ADT-settings unless they asked to change the durable default.

**Not this path:** local IDE orchestration — honor durable mode even if the machine has `gh`. Template sync / non-orchestrate playbooks — unchanged.

### Resolve mode *(before first dispatch)*

1. Read `orchestrator.git.mode`.
2. **Cloud Agent?** → apply **Cloud Agent path** above (this-run effective mode); skip steps 3–4 for mode choice; continue at forge probe. Else step 3.
3. **If set** → use it (unless this-run-only override). One line: *Git: `<mode>`*. Probe forge if PR mode (or first run after mode change).
4. **If unset** → **ask once** (recommend):
   - remote + forge CLI → **`milestone-pr`** (overnight: one PR per milestone — may include several related TODOs; concurrent implementers when they do not overlap; squash before ready; wait CI/Bugbot; merge; next branch). Offer **`branch-pr-squash`** for one PR / human merges in the morning; offer **`branch-pr`** to keep milestone history on one PR
   - remote, no CLI → **`milestone-pr`** + install ask, or **`branch-push`**
   - no remote → **`local`** (or **`none`**)
   - **`current-push`** only as explicit solo option
5. Record `mode` + `recorded` (+ `source`) unless *this run only* / cloud this-run override.
6. **Forge tooling probe** (below).
7. Later: *Set orchestrator git to milestone-pr|local|branch-pr|branch-pr-squash|branch-push|current-push|none*.

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

**PR modes** = `milestone-pr` / `branch-pr` / `branch-pr-squash`.

**PR mode + CLI missing/unauthed:** say so; **ask once** — install, skip (push + human PR), or switch mode. Install ≠ login: after install, **ask** before `gh auth login` / equivalent. No silent install/auth; no tokens in docs. Missing CLI is not a hard bootstrap failure. **`milestone-pr` without merge permission** still opens PRs; merge step degrades (below) instead of inventing a bypass.

### Start of run *(after mode resolved)*

| Check | Action |
|-------|--------|
| Not a git repo | Treat as **`none`** this run |
| Dirty **unrelated** WIP | **Hard stop** — commit/stash/waive (TEMPLATE_SYNC A0 spirit) |
| `milestone-pr` | **Cloud this-run** already on a non-default branch → **stay**, continue **`milestone-pr`** (record `branch_origin: platform`) — that branch is the platform workspace, not “someone else’s feature.” Non-cloud, non-default **intentional** user feature branch → **stay** and **degrade this run to `branch-pr-squash`** (one PR, **no merge** onto default — do not slice-merge someone else’s feature branch). Else create first `orchestrate/YYYY-MM-DD-<stem-or-scope>` (record `branch_origin: created`) |
| `branch-pr` / `branch-pr-squash` / `branch-push` | Non-default **intentional** feature branch → **stay** (record `branch_origin: pre-existing`). Else create `orchestrate/YYYY-MM-DD-<scope>` (record `branch_origin: created`) |
| `local` / `current-push` | Stay on current branch (`branch_origin: n/a`) |
| `none` | No branch setup |

**Remember for end-of-run:** whether this run **created** branches vs **stayed** on a pre-existing one. That drives **return to default** (below).

### During the loop

- **Commit** (not `none`): parent, after each work-verifier **pass** — one commit per finished unit (serialize commits if several implementers return together). No secrets; no force-push mid-loop except **`--force-with-lease`** in a squash step.
- **Push** (`milestone-pr`, `branch-pr*`, `branch-push`, `current-push`): after commits (or every few if slow).
- **`milestone-pr`:** stay on this branch while the **named milestone** still has remaining grouped TODOs or in-flight parallel implementers. When that milestone is **complete** → run the **milestone PR cycle** (below) **before** the next milestone. Do **not** start the cycle after the first TODO if more grouped work remains. Waiting on CI is overnight drain — not a stop. **One open PR at a time** (do not open a second milestone PR until this one merged or degraded).
- **`branch-pr` / `branch-pr-squash`:** after first push, open **one draft** PR if missing (scope + “orchestrator run”). Stay draft mid-run. Close-out only at **end of run**.
- No CLI → push + “open PR in browser.”
- **`current-push` rejected:** stop delivery; offer once to fall back to `milestone-pr` (or `branch-pr-squash`) this run — no silent mode switch.

### PR unit + concurrency *(`milestone-pr`)*

A **milestone** is the PR unit. Parent **names** it at partition (stem + short slice title + the TODO list). **Do not** treat “one TODO = one PR” as a hard rule. **Do not** force serial-only implementers.

**Put multiple TODOs on one milestone when any of:**

- Same reviewable cut — same stem, that stem **plus** the shared unblocker for this cut, same Current-focus cluster / one Acceptance line / domain+wire of one operable cut / implementer-split
- Closing after the first item would leave a half-done cut
- Non-overlapping stems the parent **named together** at partition (concurrent this cut — one squash tip)

**Do not put on the same milestone:**

- Unrelated next High/Medium that were **not** named at partition
- “Until the stem is drained” / the rest of the night
- Kitchen-sink / two unrelated diffs you did not name as this cut

**Spawn concurrent implementers when all of:**

- Items do not share files (typical: **different stems**, including several stems named on this milestone)
- Shared foundation consumers need is already done (or is the unit in flight — consumers **wait**)
- Each implementer has its **own** TODO (never two agents on the same Current-focus unit)

**Do not parallelize:** same files · same Current-focus unit split across two agents · consumer stem blocked on in-flight shared work · a second **PR** (add commits to the open milestone PR instead).

Same-stem default is **serial** (same files). Same-stem parallel only when the items clearly do not share files and are not one focus split.

After the last unit in the milestone: **squash** (tip-only bots / Bugbot must see the **whole milestone**) → mark ready → wait CI/Bugbot → merge. Do **not** stack a second PR on an unmerged first PR.

### End of run *(non-PR)*

- Include human-verify-map doc commit if it dirtied the tree.
- **`branch-push`:** push remaining; report branch name used for the run.
- **`current-push`:** push; report.
- **`local` / `none`:** report commits/dirty; no push.
- **Never merge** in these modes. Force-push only as **force-with-lease** in a squash step.
- Then **return to default branch** (below) when applicable.

### Milestone PR cycle *(`milestone-pr` — strict order, each milestone)*

After the **named milestone** is complete (every grouped TODO verify-pass + committed + pushed; in-flight parallel implementers for this PR have returned). **Do not reorder. Do not start the next milestone’s PR until this cycle merged or degraded.** Do **not** start this cycle after the first TODO if more grouped work remains.

Human-verify-map is **not** part of each cycle — once at true end of run ([`orchestrator.md`](orchestrator.md)). If that map dirties docs after the last code merge → one extra docs-only cycle.

1. **Draft PR** — if missing, open **draft** for **this milestone** (named slice + its TODO list, not “whole orchestration”). Stay draft until step 6. Open the draft after the first push on this branch (mid-milestone is fine); stay draft until squash + ready.
2. **Final push** — remote matches local on this milestone branch.
3. **Build verify** *(gate)* — [`Agent_Build_Verify_Rule.mdc`](../Agent_Build_Verify_Rule.mdc) / Tooling **Project verify**. Fix → re-run until green, or **degrade** (leave **draft**, report).  
   **Do not** warden / squash / mark ready / merge while red.
4. **Todo warden** *(docs-only; after green)* — stems in **this PR**; spawn `todo-warden` or follow [`todo-warden.md`](todo-warden.md). Brief: those stems + claimed-done this milestone; **honesty+hygiene**.  
   - **`gaps-found`:** commit TODOs, push, **leave draft**, **skip squash + ready + merge** (degrade this milestone; optional re-loop **this stem on this branch**).  
   - **`clean`:** continue.  
   - No code in this milestone → skip warden.
5. **Squash** *(after 3 green + 4 clean)* — one commit on **this milestone branch** (not default); subject = this milestone (all TODOs in it); **`--force-with-lease` only**. Unsafe history → skip squash, note, continue. Tip-only bots must see the **whole milestone**, not the last fix-up tip and not a one-TODO fragment.
6. **Mark ready** *(default)* — after 3 green, 4 clean/skipped, 5 done/skipped. Skip if *leave draft*, verify never green, or warden **gaps-found**.
7. **Wait CI** — poll forge checks every **60–120s**. **Stop waiting** at the first of: required checks completed · **45 minutes** with no check still running · budget exhausted.  
   - **Green:** all required checks passed → continue to step 8.  
   - **Red:** apply a fix, local build-verify, push, re-wait. **Fix budget: 2 rounds** after first ready, then **degrade** (leave ready, **do not merge**).  
   - **Incomplete / timeout / budget** (required checks still pending, queued, or never started): **degrade** — do **not** continue to steps 8–9.  
   - **No CI configured:** treat as green for the merge gate after local verify; still do step 8.  
   - Do **not** merge on red, pending, or missing required checks. Do **not** admin-bypass.
8. **Bugbot / tip-only review** — after CI completes (or after ready if no CI), wait up to **10 minutes** (15 if no CI) for comments or auto-pushed commits. None → go to merge.  
   - **Pushed commits** on this branch: `git pull --ff-only`, local build-verify; green → re-wait CI (counts toward the 2-round budget); red → fix or degrade.  
   - **Auto-fix** targeting this branch: **accept** when the diff clearly addresses the reported finding; reject drive-by refactors / unrelated files. Then local verify + re-wait CI.  
   - **Comments only:** apply **clear, in-scope** fixes (one pass); ignore nits / out-of-scope. Do not redesign. If changes were made → commit, push, local build-verify; green → re-wait CI (counts toward the 2-round budget); red → fix or degrade. No changes → go to merge.  
   - Do **not** wait for human reviewers.
9. **Merge** — squash-merge via the inferred CLI (**no** failing-check bypass). Forge delete-on-merge is OK.  
   - **Denied** (permissions, required human review, read-only CLI, protection): **degrade** — do not retry with bypass, do not stack a second PR.  
10. **Return to default** *(successful merge only — skip on degrade)* — `git checkout` default; `git pull --ff-only` if clean and tracking exists. Pull/rebase fight → **stop git cycling**, report, stay put.  
11. **Next branch or stop** *(successful merge only — skip on degrade)* — ready work + budget remain → create `orchestrate/YYYY-MM-DD-<stem-or-scope>` from default (append `-2`, `-3` if the name exists); continue the loop. Else stay on default (true end).

**Degrade** *(any step above)*: leave the PR as-is (draft or ready); do **not** merge; **skip steps 10–11**. Same stem’s next item → **stay on this unmerged branch** (more commits on the **same** PR). Other **independent** stems → new branch from **default** (they do not need this PR). Report the block.

**Order why:** each overnight milestone is reviewable, checked, and on default before the next milestone starts — so a late failure does not roll back earlier work, and Bugbot never sees only the last fix-up commit. Grouping related TODOs + concurrent implementers is how a milestone stays agent-speed; squash-before-ready is how tip-only checks still see the whole cut.

### PR close-out *(branch-pr / branch-pr-squash — strict order)*

After agent work done (+ human-verify-map committed if needed). **Do not reorder. Do not merge.**

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

### Return to default branch *(after a created-branch delivery)*

**Purpose:** Local HEAD should not stay on a disposable `orchestrate/…` so the next ask (template sync, casual fix, **next milestone**) does not land on a closed/merged/stale PR tip.

| Case | Action |
|------|--------|
| This run **created** the branch (`branch_origin: created` or `platform`) | **Default:** `git checkout` repo default (`main` / `master` / `git symbolic-ref refs/remotes/origin/HEAD` / forge default). Optional cheap `git pull --ff-only` on default if clean and tracking exists — do not merge/rebase fights. **`milestone-pr`:** do this after **each successful merge** (step 9), then step 11 may create the next branch. On degrade, **skip** return-to-default. |
| This run **stayed** on a pre-existing intentional feature branch | **Do not** auto-checkout default (user may still be building that feature). One line in report: *stayed on `<branch>` (pre-existing)*. |
| User said *stay on this branch* / *this run only stay here* | Skip return. |
| Working tree **dirty** with uncommitted work | **Do not** checkout away — report dirty + stay; ask commit/stash if needed. |
| `local` / `current-push` / `none` / never left default | Skip (already on default or no branch hop). |
| `branch-push` with **created** branch | Same as created: return to default after final push (+ warden if any). |

**When:** after that branch’s delivery is done (milestone cycle **successful merge**, or branch-pr close-out 1–5, including gaps-found push). **Never** checkout default *before* final push / squash / mark-ready / merge on the run branch. **Never** checkout default on **`milestone-pr` degrade** (stay on the unmerged slice).

**Do not:** mass-delete branches (forge delete-on-merge is OK); merge PRs **except** `milestone-pr` step 9; force-checkout over dirty files.

### Non-PR + warden

After loop (+ human verify map): if implementer units shipped → run **todo-warden** once. **gaps-found** → commit TODOs when mode allows commits; do not claim stem/Layer drained. Then **return to default** when `branch_origin: created`.

### Grants / do not

- Mode (or this-run / **Cloud Agent** override) grants **only** that effective mode’s commit/push/PR/**merge** for **orchestration**.
- **`milestone-pr` merge grant** is only step 9 after green local verify + warden clean/skipped + (**required CI green** or no CI configured) + Bugbot pass (or no comments). **Not** a grant after CI timeout / pending checks / Bugbot comments that still need a push. Never a grant to bypass protection or merge other playbooks’ PRs.
- Not a grant for template sync or other playbooks.
- **Do not:** merge PRs in `branch-pr` / `branch-pr-squash` / non-PR modes; bare `--force`; silent-default `current-push`; invent forge; store tokens; rewrite durable `orchestrator.git.mode` because of a Cloud Agent this-run (**explicit** *Set orchestrator git to …* / `source: user` **is** a durable rewrite — reviewers / Bugbot must not fail it); leave HEAD on an orchestrator-created branch after a **finished** run without returning to default; stack PRs; treat one TODO as one PR; force serial-only implementers under `milestone-pr`; skip squash before ready (tip-only bots would see only the last tip); accumulate a whole overnight drain into one PR under `milestone-pr`.
