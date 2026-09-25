# Orchestrator — Git delivery *(companion to orchestrator.md)*

> **Not a harness subagent.** Parent opens this when resolving/running **`orchestrator.git.mode`**. Main loop: [`orchestrator.md`](orchestrator.md). Build verify: [`../Agent_Build_Verify_Rule.mdc`](../Agent_Build_Verify_Rule.mdc). Todo honesty: [`todo-warden.md`](todo-warden.md).

**Live setting:** `docs/ADT-settings.yaml` → `orchestrator.git.mode` (example: [`../ADT-settings.example.yaml`](../ADT-settings.example.yaml)). **Worktrees are not a key** — see **Host worktrees** below.

## Modes

| Mode | Commits | Branch | Push | PR / close-out |
|------|---------|--------|------|----------------|
| **`milestone-pr`** | After each verify-pass unit (several TODOs may share one PR) | **New branch per milestone** | Yes | **Per milestone:** draft → build-verify → warden → mark ready → **wait CI / Bugbot** → **merge** → default → next branch. **Do not** squash before ready for Bugbot (it reads the **PR** until ready; commits after ready are tip-only). Squash-before-ready only if standing / a reviewer **only ever reads HEAD**. A milestone may be **several related TODOs** with **concurrent implementers** when work does not overlap. **Recommend** for overnight drain + forge |
| **`local`** | Same | Current | No | No |
| **`branch-pr`** | Same | One run branch | Yes | Draft mid-run → **end-of-run close-out** (no merge; keeps milestone history) |
| **`branch-pr-squash`** | Same | One run branch | Yes | Same + **squash the whole run** before ready (one PR for human review in the morning; no merge) |
| **`branch-push`** | Same | Run branch | Yes | No PR |
| **`current-push`** | Same | **Current** (often main) | Yes | No PR — **never silent-default** |
| **`none`** | No | — | No | No |

**Why not one giant overnight PR:** a multi-hour drain as a single PR is hard to review, CI/Bugbot fire only at the end, and nothing lands if the last slice fails. **`milestone-pr`** ships each **milestone** as its own PR so checks run on a reviewable diff, auto-fixes apply to that slice, and merged work is on default before the next milestone starts. A milestone is **not** locked to one TODO — group related TODOs and run concurrent implementers when they do not overlap. **Bugbot reads the PR until ready** — squash-before-ready is not required. Commits after ready are tip-only. A reviewer that **only ever reads HEAD** → standing *always squash before mark ready* (or use **`branch-pr-squash`**).

**PR modes:**

| Mode | When mark ready | Merge |
|------|-----------------|-------|
| **`milestone-pr`** | After **each** milestone close-out | **Yes** — after green CI (or no CI) + Bugbot pass below |
| **`branch-pr` / `branch-pr-squash`** | **End of run** | **No** |

Override ready/merge only if user said *leave draft* / *keep draft* / *no merge*.

### Cloud Agent path *(remote unattended — does not rewrite settings)*

**Why:** Durable `orchestrator.git.mode` is often **`local`** / **`none`** / **`branch-push`** for IDE work on a laptop. A **Cloud Agent** (Cursor Cloud or similar remote VM whose platform instructions require feature-branch + PR delivery) is the overnight drain path: it needs PRs so CI/Bugbot can see each milestone (Bugbot reads the **PR** until ready — squash-before-ready is not required), and **merge + next branch** so work lands instead of sitting as one giant morning PR.

**Detect Cloud Agent:** session is a remote/unattended cloud run with platform branch+PR obligations — **not** local IDE Composer / desktop agent / user laptop CLI. If unsure → **not** cloud (follow durable mode / ask).

**This-run effective mode** *(before first dispatch; do **not** write `docs/ADT-settings.yaml`)*:

| Durable `orchestrator.git.mode` | Cloud this-run |
|---------------------------------|----------------|
| unset / **`local`** / **`none`** / **`branch-push`** / **`current-push`** / **`branch-pr`** / **`branch-pr-squash`** | **`milestone-pr`** |
| **`milestone-pr`** | **`milestone-pr`** (no change) |

One line: *Git: `milestone-pr` (cloud this-run; durable setting remains `<mode|unset>`)*. Then forge probe + **milestone PR cycle** (below).

**User wins:** explicit this-run order (*use local this run* / *no PR* / *one PR* / *branch-pr-squash this run* / *no merge* / *leave draft*) overrides the cloud default. Still **do not** rewrite ADT-settings unless they asked to change the durable default.

**Not this path:** local IDE orchestration — honor durable mode even if the machine has `gh`. Template sync / non-orchestrate playbooks — unchanged.

Cloud isolation is a **VM + branch**, not a git worktree. Local `/worktree` / `grok -w` / Copilot New Worktree / `claude --worktree` sessions use **Host worktrees** (below) — same “stay, do not checkout default in this tree” spirit.

### Resolve mode *(before first dispatch)*

1. Read `orchestrator.git.mode`.
2. **Cloud Agent?** → apply **Cloud Agent path** above (this-run effective mode); skip steps 3–4 for mode choice; continue at forge probe. Else step 3.
3. **If set** → use it (unless this-run-only override). One line: *Git: `<mode>`*. Probe forge if PR mode (or first run after mode change).
4. **If unset** → **ask once** (recommend):
   - remote + forge CLI → **`milestone-pr`** (overnight: one PR per milestone — may include several related TODOs; concurrent implementers when they do not overlap; wait CI/Bugbot; merge; next branch). Offer **`branch-pr-squash`** for one PR / human merges in the morning; offer **`branch-pr`** to keep milestone history on one PR
   - remote, no CLI → **`milestone-pr`** + install ask, or **`branch-push`**
   - no remote → **`local`** (or **`none`**)
   - **`current-push`** only as explicit solo option
   - **Write-in (not a quiz, not an eighth mode):** same user-facing line as bootstrap 3p **E**. Closest mode + standing for merge commit / rebase-merge / always squash before ready (HEAD-only reviewer) / custom close-out. Do **not** invent a mode
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
| **Host / linked worktree** (below) | **Stay** (`branch_origin: host-worktree`; keep `platform` on Cloud). Do **not** checkout default in this tree. Host/platform tree created **for this run** → continue the effective mode (do not degrade solely because the branch is non-default). Unsure whether this tree is the user’s pre-existing feature → treat as **pre-existing** (degrade `milestone-pr` to `branch-pr-squash` this run; still do not checkout default here) |
| **Docs freshness** | Before trusting Master Index / TODOs or merging: [`../workflow/session-freshness.md`](../workflow/session-freshness.md). Sibling worktree with newer `docs/` → **hard stop** (stay ≠ current) |
| Dirty **unrelated** WIP | **Hard stop** — commit/stash/waive (TEMPLATE_SYNC A0 spirit). **Exception:** this cwd is a **linked/host worktree** and **this tree is clean** — do not hard-stop for dirty files in the **main** checkout. Unrelated dirty **in this tree** still hard-stops |
| `milestone-pr` | **Cloud this-run** already on a non-default branch → **stay**, continue **`milestone-pr`** (record `branch_origin: platform`) — that branch is the platform workspace, not “someone else’s feature.” Non-cloud, non-default **intentional** user feature branch → **stay** and **degrade this run to `branch-pr-squash`** (one PR, **no merge** onto default — do not slice-merge someone else’s feature branch). Else create first `orchestrate/YYYY-MM-DD-<stem-or-scope>` (record `branch_origin: created`) |
| `branch-pr` / `branch-pr-squash` / `branch-push` | Non-default **intentional** feature branch → **stay** (record `branch_origin: pre-existing`). Else create `orchestrate/YYYY-MM-DD-<scope>` (record `branch_origin: created`) |
| `local` / `current-push` | Stay on current branch (`branch_origin: n/a`) |
| `none` | No branch setup |

**Remember for end-of-run:** whether this run **created** branches vs **stayed** on a pre-existing one vs **host-worktree**. That drives **return to default** (below).

### Host worktrees *(isolation — not a setting)*

**Not a key.** Do **not** write `orchestrator.git.worktrees`. Do **not** `git worktree add` / `git worktree remove` / host-delete (`/delete-worktree`, `grok worktree rm`, …) unless the user asked.

**Why:** Cursor, Grok Build, Copilot, and Claude Code already create and clean worktrees. Pack-owned trees fight those managers (Cursor may auto-delete non-manager trees toward a machine cap). OpenClaw / Continue / Cline / `AGENTS.md`-only have **no** manager — that means **serial**, not raw `git worktree add`.

**Detect** *(cheap, before first dispatch)* — any of:

- `git rev-parse --git-common-dir` differs from `git rev-parse --git-dir` (linked worktree)
- cwd under `~/.cursor/worktrees`, `~/.grok/worktrees`, or `.claude/worktrees`
- Session started via Cursor `/worktree` / Agents Window worktree, `grok -w`, Copilot New Worktree / CLI `/worktree`, or `claude --worktree`
- Cloud Agent workspace → **Cloud Agent path** (VM + branch; not a git worktree)

**Already in one:** stay. One line: *Git: host worktree; staying.* Do **not** nest another tree. Do **not** checkout default **in this tree** (return-to-default is for the **main** checkout only). **Stay ≠ current** — session-start docs staleness is [`../workflow/session-freshness.md`](../workflow/session-freshness.md) (sibling uncommitted `docs/` → hard stop). This file is isolation / delivery only.

**Parallel implementers** require **host isolation** (file-overlap is not enough — two writers still share `HEAD` / index on one checkout):

1. Open **only** [`../tools/<current-tool>.md`](../tools/README.md) → **Host isolation** (current tool = this session; unknown → no manager).
2. Host **can** isolate this spawn **and** items do not share files — **live docs count** (same `*-TODO.md` / spec / Understanding = overlap even if `src/` differs) → spawn concurrent; brief each child with the host cwd/worktree path.
3. Host **cannot** isolate / no manager → **serial** this cut. Do not invent `.adt-worktrees/` or `git worktree add`.
4. Land isolated children onto **this** milestone branch (host apply / merge). **One PR.** Do not open a PR per worktree.

**Do not:** treat a host worktree as a skip of verify / squash / CI; delete a tree you did not create; `/apply-worktree` into a dirty main checkout unless the user asked; nest worktrees.

### During the loop

- **Commit** (not `none`): parent, after each work-verifier **pass** — one commit per finished unit (serialize commits if several implementers return together). No secrets; no force-push mid-loop except **`--force-with-lease`** in a squash step.
- **Push** (`milestone-pr`, `branch-pr*`, `branch-push`, `current-push`): after commits (or every few if slow).
- **`milestone-pr`:** stay on this branch while the **named milestone** still has remaining grouped TODOs or in-flight parallel implementers. When that milestone is **complete** → run the **milestone PR cycle** (below) **before** the next milestone. Do **not** start the cycle after the first TODO if more grouped work remains. Waiting on CI is overnight drain — not a stop. **One open PR at a time** (do not open a second milestone PR until this one merged or degraded).
- **`branch-pr` / `branch-pr-squash`:** after first push, open **one draft** PR if missing (scope + “orchestrator run”). Stay draft mid-run. Close-out only at **end of run**.
- No CLI → push + “open PR in browser.”
- **`current-push` rejected:** stop delivery; offer once to fall back to `milestone-pr` (or `branch-pr-squash`) this run — no silent mode switch.

### PR unit + concurrency *(`milestone-pr`)*

A **milestone** is the PR unit. Parent **names** it at partition (stem + short slice title + the TODO list). **Do not** treat “one TODO = one PR” as a hard rule. **Do not** force serial-only implementers **when the host can isolate**. Host cannot isolate → serial (do not share one checkout across two writers).

**Put multiple TODOs on one milestone when any of:**

- Same reviewable cut — same stem, that stem **plus** the shared unblocker for this cut, same Current-focus cluster / one Acceptance line / domain+wire of one operable cut / implementer-split
- Closing after the first item would leave a half-done cut
- Non-overlapping stems the parent **named together** at partition (concurrent this cut — one squash tip)

**Do not put on the same milestone:**

- Unrelated next High/Medium that were **not** named at partition
- “Until the stem is drained” / the rest of the night
- Kitchen-sink / two unrelated diffs you did not name as this cut

**Spawn concurrent implementers when all of:**

- Items do not share files — **including live docs** (typical: **different stems**, including several stems named on this milestone). Same stem’s TODO/spec = overlap even if code files differ. Before a **new** PR or a Grok successive spawn: if an open PR already touches that stem’s docs → **add to that PR** ([`../workflow/session-freshness.md`](../workflow/session-freshness.md) **Docs-overlapping PRs**)
- **Host isolation** is available (**Host worktrees** above — open that tool’s **Host isolation**; no manager → stop here, run serial)
- Shared foundation consumers need is already done (or is the unit in flight — consumers **wait**)
- Each implementer has its **own** TODO (never two agents on the same Current-focus unit)

**Do not parallelize:** host cannot isolate · same files · **same stem docs** (TODO/spec/Understanding) · same Current-focus unit split across two agents · consumer stem blocked on in-flight shared work · a second **PR** that would rewrite the same live docs (add commits to the open PR instead — successive Grok/issue agents included) · pack-created worktrees.

Same-stem default is **serial** (same files, including docs). Same-stem parallel only when the items clearly do not share **code or docs** and are not one focus split.

After the last unit in the milestone: mark ready → wait CI/Bugbot → merge. **Do not** squash before ready for Bugbot (it reads the PR until ready). Do **not** stack a second PR on an unmerged first PR.

### End of run *(non-PR)*

- Include a warden Human-TODO commit if that step dirtied the tree. Do **not** add a separate human-verify map.
- **`branch-push`:** push remaining; report branch name used for the run.
- **`current-push`:** push; report.
- **`local` / `none`:** report commits/dirty; no push.
- **Never merge** in these modes. Force-push only as **force-with-lease** in a squash step.
- Then **return to default branch** (below) when applicable.

### Milestone PR cycle *(`milestone-pr` — strict order, each milestone)*

After the **named milestone** is complete (every grouped TODO verify-pass + committed + pushed; in-flight parallel implementers for this PR have returned). **Do not reorder. Do not start the next milestone’s PR until this cycle merged or degraded.** Do **not** start this cycle after the first TODO if more grouped work remains.

The orchestrator does **not** write a human-verify map. Todo warden creates that playtest inside the warden step when an outcome passes, and that edit commits with the warden docs. No extra end-of-run look-list cycle.

1. **Draft PR** — if missing, open **draft** for **this milestone** (named slice + its TODO list, not “whole orchestration”). Stay draft until step 6. Open the draft after the first push on this branch (mid-milestone is fine); stay draft until ready.
2. **Final push** — remote matches local on this milestone branch.
3. **Build verify** *(gate)* — [`Agent_Build_Verify_Rule.mdc`](../Agent_Build_Verify_Rule.mdc) / Tooling **Project verify**. Fix → re-run until green, or **degrade** (leave **draft**, report).  
   **Do not** warden / squash / mark ready / merge while red.
4. **Todo warden** *(docs-only; after green)* — stems in **this PR**; spawn `todo-warden` when that adapter is installed, otherwise follow [`todo-warden.md`](todo-warden.md) in this session. Doc-roles declined does not skip the outcome audit. Brief: those stems + claimed-done this milestone (including any feature / stem / outcome-done claim); **honesty+hygiene** and **outcome audit** (Workflow §5.5).  
   - **`gaps-found`:** commit TODOs and any Acceptance / Human-TODO edits from this warden, push, **leave draft**, **skip ready + merge** (degrade this milestone; optional re-loop **this stem on this branch**).  
   - **`clean`:** continue. **`Outcomes open` does not block ready** and is not stem-drained. Commit any outcome-audit TODO / Acceptance / Human-TODO edits, push, continue. Do **not** report the feature or stem done while an outcome is `[ ]`. The next unit is the exercise task when none exists, or the cited-break follow-up — not a second Exercise.  
   - No code in this milestone → skip warden.
5. **Squash** *(skip by default)* — only if standing / this-turn ask / a reviewer **only ever reads HEAD**. Then one commit on **this milestone branch** (not default); subject = this milestone; **`--force-with-lease` only**. Unsafe history → skip squash, note, continue. **Bugbot reads the PR until ready** — squash-before-ready is not required. Commits after ready are tip-only (keep those fixes as the review unit; do not squash the whole milestone so HEAD equals the cut).
6. **Mark ready** *(default)* — after 3 green, 4 clean/skipped, 5 done/skipped. Skip if *leave draft*, verify never green, or warden **gaps-found**.
7. **Wait CI** — poll forge checks every **60–120s**. **Stop waiting** at the first of: required checks completed · **45 minutes** with no check still running · budget exhausted.  
   - **Green:** all required checks passed → continue to step 8.  
   - **Red:** apply a fix, local build-verify, push, re-wait. **Fix budget: 2 rounds** after first ready, then **degrade** (leave ready, **do not merge**).  
   - **Incomplete / timeout / budget** (required checks still pending, queued, or never started): **degrade** — do **not** continue to steps 8–9.  
   - **No CI configured:** treat as green for the merge gate after local verify; still do step 8.  
   - Do **not** merge on red, pending, or missing required checks. Do **not** admin-bypass.
8. **Bugbot** — after CI completes (or after ready if no CI), wait up to **10 minutes** (15 if no CI) for comments or auto-pushed commits. None → go to merge. Bugbot already had the **PR** (all commits) at ready; further commits here are tip-only.  
   - **Pushed commits** on this branch: `git pull --ff-only`, local build-verify; green → re-wait CI (counts toward the 2-round budget); red → fix or degrade.  
   - **Auto-fix** targeting this branch: **accept** when the diff clearly addresses the reported finding; reject drive-by refactors / unrelated files. Then local verify + re-wait CI.  
   - **Comments only:** apply **clear, in-scope** fixes (one pass); ignore nits / out-of-scope. Do not redesign. If changes were made → commit, push, local build-verify; green → re-wait CI (counts toward the 2-round budget); red → fix or degrade. No changes → go to merge.  
   - Do **not** wait for human reviewers.
9. **Merge** — squash-merge via the inferred CLI (**no** failing-check bypass). Forge delete-on-merge is OK.  
   - **Denied** (permissions, required human review, read-only CLI, protection): **degrade** — do not retry with bypass, do not stack a second PR.  
10. **Return to default** *(successful merge only — skip on degrade)* — follow **Return to default branch** below. **Main checkout:** `git checkout` default; `git pull --ff-only` if clean and tracking exists. Pull/rebase fight → **stop git cycling**, report, stay put. **Host / linked worktree:** do **not** `git checkout` default (Git refuses when the main checkout already has it).  
11. **Next branch or stop** *(successful merge only — skip on degrade)* — ready work + budget remain → create `orchestrate/YYYY-MM-DD-<stem-or-scope>` from default (append `-2`, `-3` if the name exists); continue the loop. **Main checkout:** create from the checked-out default. **Host / linked worktree:** `git fetch` (if a remote exists) then `git checkout --no-track -b` that name from `origin/<default>` — do **not** checkout default first (`-b` from a remote-tracking ref **tracks that ref** unless `--no-track`). First push of the new branch: `git push -u origin HEAD` (or the new name) so upstream is the **milestone** branch, not default. Else (true end): **main checkout** stays on default; **host / linked worktree** stays put (do not checkout default).

**Degrade** *(any step above)*: leave the PR as-is (draft or ready); do **not** merge; **skip steps 10–11**. Same stem’s next item → **stay on this unmerged branch** (more commits on the **same** PR). Other **independent** stems → new branch from **default** (they do not need this PR). **Host / linked worktree:** `git checkout --no-track -b` from `origin/<default>` — do **not** checkout default first; first push `-u` to the **new** name. Report the block.

**Order why:** each overnight milestone is reviewable, checked, and on default before the next milestone starts — so a late failure does not roll back earlier work. Grouping related TODOs + concurrent implementers is how a milestone stays agent-speed. Bugbot reads the PR until ready; squash-before-ready is not required.

### PR close-out *(branch-pr / branch-pr-squash — strict order)*

After agent work done. **Do not reorder. Do not merge.** Do **not** add a human-verify map before or after warden.

1. **Final push** — remote matches local.
2. **Build verify** *(gate)* — [`Agent_Build_Verify_Rule.mdc`](../Agent_Build_Verify_Rule.mdc) / Tooling **Project verify**. Fix → re-run until green, or stop (leave **draft**, report block).  
   **Do not** warden / squash / mark ready while red. If stopping here with a clean tree → still **return to default** (step 6), then report.
3. **Todo warden** *(docs-only; after green)* — if this run cleared implementer units: spawn `todo-warden` when that adapter is installed, otherwise follow [`todo-warden.md`](todo-warden.md) in this session. Doc-roles declined does not skip the outcome audit. Brief: in-scope stems + claimed-done list; mode **honesty+hygiene** (reopen/add gaps **and** move parked `[x]` into Completed) and **outcome audit** (Workflow §5.5).  
   - **`gaps-found`:** commit TODOs (and any Acceptance / Human-TODO edits from this warden), push, **leave draft**, **skip squash + ready**; then **return to default** (run branch remains on remote). Optional re-loop if budget — if re-looping, **stay** on run branch until that loop’s close-out.  
   - **`clean`:** continue. **`Outcomes open` does not block ready.** If warden edited TODOs, Acceptance, or Human-TODO (exercise row, outcome check, premature-playtest withdraw), **commit those docs and push** before squash / ready. Do not return to default and leave them dirty. Do **not** report the feature or stem done while an outcome is `[ ]`.  
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
| This run **created** the branch (`branch_origin: created` or `platform`) **and** cwd is the **main** checkout | **Default:** `git checkout` repo default (`main` / `master` / `git symbolic-ref refs/remotes/origin/HEAD` / forge default). Optional cheap `git pull --ff-only` on default if clean and tracking exists — do not merge/rebase fights. **`milestone-pr`:** do this after **each successful merge** (step 9), then step 11 may create the next branch. On degrade, **skip** return-to-default. |
| cwd is a **linked / host worktree** (`branch_origin: host-worktree` or `platform` on Cloud) | **Do not** checkout default **in this tree**. **`milestone-pr` after successful merge + more work:** skip the step 10 checkout; step 11 creates the next branch **in this tree** from `origin/<default>` (`git fetch` + `git checkout --no-track -b` — never checkout default; first push `-u` to the **new** name, not default). True end / non-PR close-out: leave as-is. One line: *session is a host worktree; left it as-is* (or *next branch from origin/default*). |
| This run **stayed** on a pre-existing intentional feature branch | **Do not** auto-checkout default (user may still be building that feature). One line in report: *stayed on `<branch>` (pre-existing)*. |
| User said *stay on this branch* / *this run only stay here* | Skip return. |
| Working tree **dirty** with uncommitted work | **Do not** checkout away — report dirty + stay; ask commit/stash if needed. |
| `local` / `current-push` / `none` / never left default | Skip (already on default or no branch hop). |
| `branch-push` with **created** branch | Same as created: return to default after final push (+ warden if any). |

**When:** after that branch’s delivery is done (milestone cycle **successful merge**, or branch-pr close-out 1–5, including gaps-found push). **Never** checkout default *before* final push / squash / mark-ready / merge on the run branch. **Never** checkout default on **`milestone-pr` degrade** (stay on the unmerged slice).

**Do not:** mass-delete branches (forge delete-on-merge is OK); merge PRs **except** `milestone-pr` step 9; force-checkout over dirty files.

### Non-PR + warden

After the loop: if implementer units shipped → run the outcome audit once (spawn `todo-warden` when that adapter is installed; otherwise follow [`todo-warden.md`](todo-warden.md) here). **gaps-found** → commit TODOs and any Acceptance / Human-TODO edits from this audit when mode allows commits; do not claim stem/Layer drained. **`clean` with warden file edits** (outcome audit, Acceptance checkbox, Human-TODO playtest or withdraw) → commit those docs too when mode allows commits, before return-to-default. A dirty tree of audit edits is not “clean enough to checkout away.” Then **return to default** when `branch_origin: created` **and** cwd is the **main** checkout (host / linked worktree → skip; see table).

### Grants / do not

- Mode (or this-run / **Cloud Agent** override) grants **only** that effective mode’s commit/push/PR/**merge** for **orchestration**.
- **`milestone-pr` merge grant** is only step 9 after green local verify + warden clean/skipped + (**required CI green** or no CI configured) + Bugbot pass (or no comments). **Not** a grant after CI timeout / pending checks / Bugbot comments that still need a push. Never a grant to bypass protection or merge other playbooks’ PRs.
- Not a grant for template sync or other playbooks.
- **Do not:** merge PRs in `branch-pr` / `branch-pr-squash` / non-PR modes; bare `--force`; silent-default `current-push`; invent forge; store tokens; rewrite durable `orchestrator.git.mode` because of a Cloud Agent this-run (**explicit** *Set orchestrator git to …* / `source: user` **is** a durable rewrite — reviewers / Bugbot must not fail it); leave HEAD on an orchestrator-created branch after a **finished** run without returning to default **unless** cwd is a host/linked worktree; stack PRs; treat one TODO as one PR; force serial-only implementers under `milestone-pr` **when the host can isolate**; spawn concurrent writers on a **shared** checkout; `git worktree add` / write `orchestrator.git.worktrees`; squash before ready **for Bugbot** (it reads the PR until ready); accumulate a whole overnight drain into one PR under `milestone-pr`.
