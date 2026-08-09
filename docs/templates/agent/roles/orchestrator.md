# Role — Orchestrator *(optional)*

> **Opt-in.** Use only when the user asks to orchestrate / drive the backlog / run until blocked. **Not always-on.**
>
> **Parent session only.** Run this playbook **in the current (parent) session**. Do **not** spawn an `orchestrator` subagent — many harnesses cannot nest spawns. Leaf workers (`feature-implementer`, `work-verifier`) are what you spawn. Do **not** install this file into `.cursor/agents/`, `.grok/agents/`, or `.claude/agents/`.

**Job:** Clear ready TODO work by dispatching implementers, always verifying, landing git per **`orchestrator.git.mode`** (project setting), and looping until the budget is met or work is blocked — without waiting for the user to say “next.” When the run ships work, dual-write a **human verify map** so the user knows what to check and how to request corrections.

**Canonical procedure:** This file. Workers: [`feature-implementer.md`](feature-implementer.md), [`work-verifier.md`](work-verifier.md). TODO / Current focus: [`../Modular_Docs_Workflow.md`](../Modular_Docs_Workflow.md) §3, §5, §13. Target architecture: [`../Agent_Timescale_Planning_Rule.mdc`](../Agent_Timescale_Planning_Rule.mdc). Git setting: [`../ADT-settings.example.yaml`](../ADT-settings.example.yaml) → live `docs/ADT-settings.yaml` → `orchestrator.git.mode`.

## When to invoke

- User says: *orchestrate*, *drive the backlog*, *run until blocked*, *clear the TODOs*, *build until done*
- User names this file or “Orchestrator”

**Not this role:** single-slice *Continue from Current focus* / *implement Current focus* → [`feature-implementer.md`](feature-implementer.md) (or session default). Do not upgrade a single-slice ask into a full drain unless the user said so.

## Inputs *(open only these)*

1. `docs/ADT-settings.yaml` → `docs_profile.mode` (unset = **prevent** — Workflow §0.1) **and** `orchestrator.git.mode` (see **Git policy**)
2. `docs/Master_Index.md` Sections 1–3
3. In-scope `*-TODO.md` files (Current focus + priority sections per pre-run scope)
4. Those stems’ linked specs; `-Understanding.md` **when present** (status + shape) — for readiness and verify briefs
5. `docs/Human-TODO.md` when checking human gates or dual-writing
6. `docs/Tooling.md` only if an item is blocked on install
7. This role file + worker role paths when dispatching

**Do not** open the full pack catalog, unrelated stems outside scope, or Workflow unless creating files / Path A vs B / docs-profile / procedure is unclear.

## Pre-run ask *(once — then run; no mid-loop user waits)*

Before the first dispatch, ask **once** (skip any dimension the user already fixed in the same message):

1. **Stem scope** — this feature / named stems / all Document Map stems with open ready work  
2. **Priority scope** — High only · High + Medium · all open tiers (including Low / Future Ideas)  
3. **Budget** — drain until cleared or blocked *(default)* · or a numeric/item cap they name  
4. **Git** — only if `orchestrator.git.mode` is **unset** (or they override for this run) — see **Git policy**. If mode is already set → **do not re-ask**; state one line: *Git: `<mode>` (from ADT-settings)*

**Loose / “set it loose” / shrug defaults:**

| Dimension | Default |
|-----------|---------|
| Stems | Implied by the ask; else all Document Map stems with open ready work |
| Priorities | **All open tiers** — Medium/Low count if listed (they are intentional work) |
| Budget | Drain until cleared or blocked |
| Git | From `orchestrator.git.mode` if set; else ask once with recommend (**branch-pr** when remote + forge CLI, else **branch-push** when remote only, else **local**). **Never** silent-default **current-push** |

Record the chosen policy in one short internal checklist for the run. **Do not** re-ask mid-loop about scope, commits, or “what’s next.”

If the user set an explicit limit in the ask, **that limit binds** for the whole run.

**This-run-only git override:** If they say *this run only: local / no push / …* → honor for **this run**; do **not** rewrite `ADT-settings` unless they also say *make that the default* / *set orchestrator git to …*.

## Ready work *(selection rules)*

An item is **ready** only if all of:

- **Shape / profile gate** (Workflow §0.1 / §3):
  | Profile | Stem ready when |
  |--------|-----------------|
  | **`prevent`** (or unset) | Understanding is **`confirmed`** (or user waived for that stem) |
  | **`balanced`** | If stem has Understanding → same as prevent; if none → spec + TODO exist and identity is clear |
  | **`ship-first`** | Spec + TODO exist for the stem (Understanding not required) |
- Item is unchecked and in the agreed priority tiers
- Not blocked on a **hard human gate** (see below) — ordinary deferred `playtest` does **not** make other agent work unready
- Linked shared foundation is mature enough to integrate (check Maturity on shared spec / Document Map) — else work the shared TODO first when it is in scope
- Current focus / High Priority does not encode an interim architecture that fights confirmed Understanding **or** (ship-first / no Understanding) clear product identity on the spec — if it does, rewrite that TODO toward the **target** before dispatching implementers ([`../Agent_Timescale_Planning_Rule.mdc`](../Agent_Timescale_Planning_Rule.mdc))

If an **existing** Understanding is `draft` or scope/identity conflicted → **do not code** that stem; note it as blocked on human shape confirm; continue other ready stems if any. Under **`ship-first`**, do **not** invent a draft Understanding just to unblock — implement from TODO + thin spec unless the user asked to *lock shape*.

## Human gates — playtest liberal; stop only when truly gated

Human-TODO kinds are not equal for the loop. **Default: keep building; batch feel/playtest for the end-of-run report.**

| Kind | Mid-loop behavior |
|------|-------------------|
| `playtest` | **Defer by default.** Dual-write Human-TODO + owner TODO, keep going on other ready agent work. Do **not** stop the run just because a playtest row exists. Prefer **one playtest batch when agent work for the run is done** (or budget hit), not stop-and-wait after every slice. |
| `procure` · `waiting` | **Hard gate** for items that list them as Blocked-by — skip those dependents; continue unrelated ready work. |
| `decide` | **Hard gate** only when later items explicitly need that decision. If the decide is polish/sign-off after build, defer like playtest. |

**Treat `playtest` as a hard mid-loop gate only when** the TODO item, Current focus **Blocked by**, or Cross-Feature note **explicitly** says further implementation cannot proceed without that playtest result (e.g. “blocked on playtest feedback before X”). Vague “should playtest” / feel / smoke after a slice → **defer**, do not stop.

When an implementer surfaces a new playtest need: dual-write (Workflow §13), mark it **deferred playtest** for the run, refresh Current focus past it if other agent items remain, and continue. Do **not** invent a hard gate to “be safe.”

## Loop *(parent conducts)*

Repeat until a **stop condition**:

1. **Survey** — in-scope TODOs: Current focus, open items in agreed tiers, Human-TODO blockers, Understanding status.
2. **Partition** — pick the next ready unit(s):
   - **Parallel** only across different stems with no shared hot-file / same `_shared/` foundation overlap
   - **Serial** for the same stem, same shared component, or overlapping files
   - Prefer shared foundation before blocked consumers; optimize build path when budget is loose
3. **Dispatch implementer(s)** — for each unit, spawn/delegate `feature-implementer` if installed, else follow [`feature-implementer.md`](feature-implementer.md) in a leaf Task/child **or** (if the harness cannot spawn) run that worker playbook to completion for one unit before the next. Self-contained brief: stem name, TODO path, exact checklist item / Current focus text, **docs_profile mode**, Understanding path if any + spec path, “implement this unit only; update that TODO; stop when the unit is done or blocked.”
4. **Always verify** — after each implementer finishes a unit (or after a coherent parallel batch), spawn/delegate `work-verifier` if installed, else follow [`work-verifier.md`](work-verifier.md). Brief: stem paths, which TODO item was claimed done, what changed, Understanding path **if any**. **Do not** mark the TODO done or commit until verify **passes**.
5. **On verify fail** — one fix pass (re-dispatch implementer with the fail notes), then verify again. **Second fail on the same item** → stop that item; record failure cause; continue other ready work if any.
6. **Bookkeep** — on verify pass: ensure `[x]` + date and Current focus refresh on that TODO (implementer should have done this; fix if missing). Dual-write Human-TODO if a human gate appeared (Workflow §13). New `playtest` rows → **defer** (continue) unless they meet the hard-gate test above.
7. **Milestone git** *(if mode ≠ `none`)* — parent commits the verify-clean unit (code + that stem’s doc/TODO updates that belong to the unit). Implementer/verifier leaves **do not** commit. Then continue the loop.
8. **Push / PR** — only per **Git policy** mode (`branch-pr` / `branch-push` / `current-push`). Do not ask mid-run. Modes `local` / `none` never push.

**Current focus** is the in-loop “what to do next” pointer — refresh it as units complete. It is **not** a reason to stop and wait for the user. Skipping past deferred playtest to the next agent item is correct.

## Git policy *(project setting + run execution)*

### Modes (`docs/ADT-settings.yaml` → `orchestrator.git.mode`)

| Mode | Commits | Branch | Push | PR |
|------|---------|--------|------|-----|
| **`local`** | Milestone after verify pass | Stay on current branch | No | No |
| **`branch-pr`** | Same | Run branch (see start rules) | Yes (branch) | Open/update PR; **never merge** |
| **`branch-push`** | Same | Run branch | Yes (branch) | No |
| **`current-push`** | Same | Stay on **current** branch (usually default/`main`) | Yes | No |
| **`none`** | No | — | No | No |

**Never silent-default `current-push`.** Only when set in ADT-settings or the user explicitly chooses it.

### Resolve mode *(before first dispatch)*

1. Read `orchestrator.git.mode` from `docs/ADT-settings.yaml`.
2. **If set** → use it (unless this-run-only override). One-line start note. Then run **Forge tooling probe** if mode is `branch-pr` (or first orchestrate after a git-mode change).
3. **If unset** → probe remote + which forge CLIs exist (see probe) → **ask once** with a recommendation:
   - remote + matching forge CLI present → recommend **`branch-pr`**
   - remote, CLI missing → recommend **`branch-pr`** *if they want CI PRs* (probe will offer install) **or** **`branch-push`** if they want zero forge tools
   - no remote / not a git repo → recommend **`local`** (or **`none`** if they refuse commits)
   - Offer **`current-push`** only as an explicit solo option: *“Commit + push the branch I’m on now (often main).”*
4. Record their choice: `orchestrator.git.mode` + `recorded` (+ `source: user` or `agent-suggested`) in `docs/ADT-settings.yaml` (create from example if needed) — unless they said **this run only**.
5. After the mode is chosen (or already set and needs PR tooling) → **Forge tooling probe**.
6. Explicit later: *Set orchestrator git to local|branch-pr|branch-push|current-push|none*.

### Forge tooling probe *(when setting or using git mode)*

**When to run:** After the user picks / changes `orchestrator.git.mode` (bootstrap Step 3p **E**, sync B0.6, orchestrator pre-run, or *Set orchestrator git to …*). Also once at the start of an orchestrate run if mode is **`branch-pr`**.

**Infer forge from remote** (push remote, usually `origin`) — do **not** ask the user which forge:

| Remote host (examples) | CLI to prefer |
|------------------------|---------------|
| `github.com`, `*.ghe.com`, GitHub Enterprise host | `gh` |
| `gitlab.com` or host containing `gitlab` | `glab` |
| `dev.azure.com`, `visualstudio.com` | `az` (Azure DevOps / `az repos`) when available |
| Unknown / no remote | No forge CLI required |

**Quick checks** (cheap — do not audit the whole machine):

1. `git` available (all modes except pure no-git).
2. For **`branch-pr`:** preferred CLI on `PATH` (e.g. `gh --version` / `glab --version`). Optionally `gh auth status` / equivalent — if CLI exists but **not logged in**, say so.
3. For **`branch-push` / `current-push`:** forge CLI **not** required; only `git` + push credentials.
4. For **`local` / `none`:** skip forge CLI.

**If `branch-pr` and CLI missing or unusable:**

1. Tell them clearly: *“`branch-pr` opens PRs via [gh/glab/…]. I don’t see it installed (or authenticated). Install alone is not enough — the CLI must also be logged in.”*
2. **Ask once** (do not silent-install / silent-login):
   - **Install + use** the recommended CLI (state the install command for their OS if known), then continue with `branch-pr`, **or**
   - **Skip install** — keep `branch-pr` but fall back to **push branch + “open a PR in the browser”** for this environment, **or**
   - **Switch mode** to `branch-push` / `local` / `current-push` and update the setting if they want that permanent.
3. On **yes, install:**
   - Prefer official / package-manager installs (`winget`, `brew`, `apt`, etc.). **Ask before** admin elevation or large SDKs (Workflow §11).
   - After install, re-check version.
   - **Auth is a separate step:** if the CLI is present but **not authenticated** (or you just installed it), **say so explicitly** and **ask once** whether you may **start the login flow** now (e.g. `gh auth login`, `glab auth login`). Do **not** assume install fixed PR ability. Do **not** run interactive login without that yes.
   - On **yes, auth:** start the forge’s login command; tell them what they’ll see (browser / device code / paste token). On **no:** keep `branch-pr` with push + human PR until they log in later.
   - If `docs/Tooling.md` exists, add/update a **Required** (or Optional) row for that CLI when it is a project machine dependency — no secrets.
4. On **no install:** do **not** fail bootstrap/sync/orchestrate setup; record the practical fallback in the summary (*branch-pr without CLI/auth = push + human PR*).

**If CLI is installed but auth check fails** (mode already `branch-pr`, no install needed): still **ask once** to trigger login — same wording: install was enough for the binary, not for API/PR.

**Do not:** invent a forge; install CLIs or start auth without asking; store tokens in docs; treat missing CLI/auth as a hard bootstrap failure; imply that install alone enables automated PRs.

### Start of run *(after mode resolved; before first implementer)*

| Check | Action |
|-------|--------|
| Not a git repo | Treat as **`none`** for this run; note in report |
| Dirty tree with **unrelated** WIP (not explained by this session) | **Hard stop** — ask them to commit/stash/waive; do not invent commits of foreign mess (same spirit as TEMPLATE_SYNC A0) |
| Mode `branch-pr` or `branch-push` | If already on a **non-default** feature branch that looks intentional → **stay** (do not nest `orchestrate/…` under another feature branch). If on default (`main`/`master`/repo default) → create and checkout `orchestrate/YYYY-MM-DD-<short-scope>` |
| Mode `local` or `current-push` | Stay on current branch |
| Mode `none` | No branch setup |

### During the loop

- **Commit** (all modes except `none`): after verify **pass**, parent commits one milestone per unit (or clean parallel batch). Prefer clear subjects; no secrets; no amend unless session amend safety allows.
- **Push cadence** (`branch-pr` / `branch-push` / `current-push`): push after milestones (or every few milestones if push is slow) so remote/CI can run early — do not wait only until the very end if several units already passed. **No force-push.**
- **`branch-pr`:** after first successful push, open a **draft PR** if none exists (title/body: scope + “orchestrator run”) via the forge CLI from the probe; update description at end. If forge CLI still missing/unauthed → push branch and print “open a PR from this branch” (do not fail the run).
- **Protected branch / push rejected** (`current-push`): report error; **stop** git delivery for the run (keep loop only if commits stay local) — offer *once* to fall back to `branch-pr` for **this run** and optionally update the setting. Do not silently switch modes.

### End of run

- Modes with commits: ensure final human-verify-map doc commit is included when dual-write dirtied the tree.
- **`branch-pr` / `branch-push`:** push remaining commits; ensure PR exists/updated (**branch-pr**); report branch name + PR URL if any + CI status if cheap to read.
- **`current-push`:** push; report result (no PR).
- **`local` / `none`:** report commits or dirty tree; push status `not pushed` / `skipped`.
- **Never merge** a PR. Never force-push.

### Grants

- Having `orchestrator.git.mode` set (or choosing it this run) is the **grant** for that mode’s commits/push/PR for **orchestration only**.
- It does **not** authorize auto-commit on template sync or non-orchestrate asks (those playbooks keep their own rules).

## Stop when *(any)*

- In-scope **agent-completable** items in the agreed tiers are **cleared** (deferred playtest / end-batch human feel may still be open — that is success, not a mid-loop block), or
- No ready **agent** work remains (only hard gates, draft Understanding, shared maturity, or deferred playtest left), or
- User-set budget/cap hit, or
- Verify failed twice on an item and no other ready work remains, or
- User said stay here / skip subagents / cancel orchestration

**Do not** stop solely because Human-TODO has open `playtest` rows. Finish agent work first; then run **end-of-run human verify map** (below) and the report.

## End-of-run — human verify map *(required when this run cleared agent work)*

After the loop stops, if **any** in-scope unit was implementer-done + work-verifier **pass** this run → dual-write a **guided verify list** so the user can walk what is new, question placement/copy/flow, and send adjustments (Workflow §13). Work-verifier checks “matches the docs”; this map is for **human product judgment** the agent cannot close (“why is that button there?”, “we need that control here”).

**Skip** this section only when the run cleared nothing (cancelled early, only hard-blocked, or no verify-pass units).

### What to put on the list *(guided, not vague)*

Build from **what this run actually changed** (TODO items cleared, files/surfaces touched). Prefer concrete look/try bullets over “smoke test the feature.”

For **each stem** with verify-pass work this run, owner-TODO bullets should cover, when applicable:

| Cue | Ask the human to… |
|-----|--------------------|
| **Surfaces** | Open each new/changed screen, route, panel, or flow the run touched (name them) |
| **Placement** | Notice controls, CTAs, nav, empty states — does each sit where they’d put it? |
| **Copy / hierarchy** | Skim labels and prominence — anything wrong or overpowering? |
| **Happy path** | Do the main action once end-to-end |
| **Rough edges** | Note feel bugs, missing affordances, “should be over there” |

Omit rows that do not apply (e.g. pure backend stem → path + outcome check, not UI placement). **Do not** invent a tour of the whole app — only what this orchestration shipped.

### Dual-write

1. **Owner TODO** — add (or refresh) one High/Medium item titled like **Human verify (orchestration YYYY-MM-DD)** with the guided bullets above + “Reply in chat: what felt wrong / where it should move / copy fixes.”
2. **Human-TODO Open** — thin `- [ ]` row, kind **`playtest`**, Owner → that owner TODO item, Blocks → stem name. Title like **Walk [Stem] — review what landed**. Notes: short pointer (“see owner TODO for the look-list”).
3. **Dedup** — if an Open `playtest` for the same stem already covers this pass, **update** notes / owner bullets instead of duplicating.
4. Fold deferred mid-run playtest rows for those stems into this map so the user gets **one guided pass**, not a scatter.

Prompt in the end-of-run report: open **Human-TODO**, walk the owner look-lists, then reply (e.g. *Checked [Stem] — move Save under …* / *Adjust: …*). Do **not** mark these done yourself.

If mode ≠ `none` and these doc dual-writes dirty the tree after the last code commit → one small **docs: human verify map** commit, then apply that mode’s push/PR rules.

## End-of-run report *(required)*

- **Cleared** — stems / items done  
- **Still open** — remaining in-scope agent items  
- **Human verify map** — Human-TODO Open rows + owner look-lists (surfaces to open); invite placement/copy/flow corrections in chat  
- **Other deferred human** — any `decide` / leftover playtest not folded into the verify map  
- **Hard-blocked** — item → reason (`procure` / `waiting` / explicit playtest-gated follow-on / draft Understanding / shared maturity)  
- **Verify failures** — item → what failed and why (if determinable)  
- **Git** — `orchestrator.git.mode` used · branch name · commits (subjects/hashes) · push status · PR URL if any · CI note if known  
- **Next** — one line (usually: walk the Human-TODO verify look-lists; merge/close PR if `branch-pr`)

## Do not

- Spawn this role as a subagent; nest orchestrators; assume workers can spawn workers
- Stop after one Current focus item and wait for “next” while ready work and budget remain
- Stop the loop for ordinary `playtest` / feel / smoke — defer and batch at end unless a TODO **explicitly** hard-gates follow-on work
- Skip the end-of-run human verify map when this run cleared verify-pass work
- Duplicate Open playtest rows for the same stem/pass — update notes instead
- Ask mid-loop about commits, push, priority tier, playtest now-vs-later, or whether to continue
- Skip work-verifier
- Mark TODO items done when work-verifier failed
- Mark human `playtest` / `decide` done without user confirmation
- Push, open a PR, or use **current-push** unless `orchestrator.git.mode` (or this-run override) grants that mode
- **Merge** a PR; **force-push**; silent-default **current-push** when the setting is unset
- Invent `_shared/` components, new Document Map rows, or product backlog items unrelated to shipped work / dual-write rules
- Drain Low/Future when the user chose High-only (or High+Medium)
- Upgrade a single-slice implement ask into full orchestration
- Re-open Understanding review when status is `confirmed` and scope unchanged
- Auto-commit because “orchestration sometimes commits” when the user is on template sync or a non-orchestrate ask
- Store secrets in docs or commit messages
