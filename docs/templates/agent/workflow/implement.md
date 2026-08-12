<!-- pack-version: 2.7.17 -->

> **Workflow module.** Open from the [workflow index](../Modular_Docs_Workflow.md) when Path A vs Path B is unclear, or you need the ready-to-code table. Prefer the index **paved path** when already ready.

# Working paths (implement)

## 3. Quick Start — Working on Any Task

**Minimal implement path** *(prefer this when ready under §0.1)*:

**Ready when:**

| Profile | Ready to code |
|---------|----------------|
| **`prevent`** | Understanding is `confirmed` (or user waived) and scope unchanged |
| **`balanced`** | If stem has Understanding → same as prevent; if none → thin spec + TODO exist and identity is clear |
| **`ship-first`** | Spec + TODO exist for the stem; no Understanding required |

1. Read `docs_profile` (if set) + `Master_Index.md` — Sections 1–3
2. Active TODO **Current focus** → that TODO → Understanding *(if present — read-only)* → spec → code
3. Skip drafting/graduation unless profile requires shape work, status is `draft` on an existing Understanding, the user changed scope, or Project Profile says game extensions apply
4. **Preference corrections → same turn:** if the user corrected a lasting UI/interaction preference that could be “improved away,” append 1-line **Decisions** row(s) on that stem’s spec and fix contradicting Behavior / Acceptance / Visual refs (§10). Do **not** wait for a session-wrap ask. Update **Current focus** as usual (§5.1) — it is handoff, not the decision log.

**Full Path A / Path B** when scoping new work, Understanding is required and missing/`draft`, or graduating to spec:

1. Read `Master_Index.md` — Sections 1–3 (overview, locations, Document Map)
2. Decide: **shared foundation work** (Path A) or **feature work** (Path B) — §1

### Path A — Shared foundation work

Use when building or changing a reusable component, API, or pattern in `_shared/`.

1. Open `_shared/[ComponentName].md`
2. **Understanding** — under **`prevent`**, or **`balanced`** when identity is unclear / multi-surface: open or draft `_shared/[ComponentName]-Understanding.md` first; show for shape review (§4). If already `confirmed` and scope unchanged, read only. Under **`ship-first`**, skip unless the file exists or user said *lock shape*.
3. Open the relevant shared TODO file(s) (create from [`TODO_Template.md`](../../TODO_Template.md) if missing):
   - Core / foundation → `_shared/[ComponentName]-TODO.md`
   - In-Editor work → `_shared/[ComponentName]-InEditor-TODO.md` *(only if Project Profile game extensions apply, or user asked — unless excepted in Master Index §3.0)*
   - Assets & content → `_shared/[ComponentName]-Asset-TODO.md` *(same gate)*
4. Do the work when **ready** under the table above (not blocked on a draft Understanding that exists)
5. **Graduate** confirmed shape into the shared spec if Understanding was used and the spec is still placeholder (§2); under ship-first grow the spec as you go
6. **Update the shared TODO file(s)** before ending the session — refresh **Current focus** (§5.1)
7. If consumer features are blocked, ensure their TODOs link here — do not copy foundation tasks into feature TODOs

### Path B — Feature work

1. Open shared docs **only** when linked from this feature’s Understanding, spec, or TODO dependency notes — or the one shared component you are integrating now. Do **not** open every §3.1 “relevant” row.
2. Open `features/[FeatureName].md`
3. **Understanding** — same profile rules as Path A step 2 for `features/[FeatureName]-Understanding.md`
4. Open the relevant feature TODO file(s):
   - Core gameplay/systems → `features/[FeatureName]-TODO.md`
   - In-Editor work → `features/[FeatureName]-InEditor-TODO.md` *(Project Profile game extensions or user asked — §7)*
   - Assets & content → `features/[FeatureName]-Asset-TODO.md` *(same gate)*
5. Do the work when **ready** under the table above
6. **Graduate** or grow the feature spec per §2
7. **Update the feature TODO file(s)** before ending the session — refresh **Current focus** (§5.1)

If the work is really shared foundation, **stop** — use Path A instead.

**Golden Rule**: If you find yourself scrolling through a long file, stop and split (§8).

---
