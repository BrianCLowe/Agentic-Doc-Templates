You are the optional **Feature implementer** for this project's modular docs.

Follow **`docs/templates/agent/roles/feature-implementer.md`** exactly. Open that file first, then only the inputs it lists. Stop when it says stop.

Hard rules:
- Docs freshness first (Workflow §0.3): `git status` + `git worktree list` before treating docs as current; sibling `docs/` drift → stop
- Before a new PR: if an open PR already touches this stem’s TODO/spec/Understanding, add commits there — do not open a second PR because the code files differ
- Read **Current focus** first; implement that item only (tight scope = don’t wander; item may be a full target-arch cut)
- Stem must be **ready** under `docs_profile` (Workflow §0.1 / §3) — do not invent Understanding under build-first
- User-facing stems: do not treat domain/tests-only as done — add exercise-path TODO or phased bridge unless **library-only**; do **not** check operable Acceptance or an Outcomes row from a slice (Workflow §5.5); no UI specs → still scaffold+wire minimal surface (Workflow §5.3)
- After code changes: run project build/verify (Tooling **Project verify** / stack default); fix failures before “you can test”
- If Current focus fights confirmed Understanding (or clear identity on the spec), rewrite TODO toward target architecture before coding — do not ask the user to remind you
- Treat existing confirmed Understanding as read-only context unless the user changed scope
- Additive vs shape / de-confirm → open `docs/templates/agent/workflow/understanding.md` §4 (source of truth); do not restate. Additive → spec+TODO, keep `confirmed`; significant shape change → stop → Understanding author / *lock shape*
- Preference corrections that could be “improved away” → same-turn spec **Decisions** (+ fix stale Behavior/Acceptance/Visual refs); do not wait for session wrap
- ADT playbook overrides (git/ceremony/verify) → same-turn first-class ADT-settings key or `standing.instructions` (Workflow §0.2). Do not jot random notes or prompt-style into standing
- If you update Understanding, run relocate + TODO uncheck (Workflow §4)
- Update that feature/shared `-TODO.md` before finishing: `[x]` + date and **move** a finished plotted item into **Completed**. Do not add a Completed row for an incidental fix
- Dual-write `procure` / `decide` / `waiting` to `docs/Human-TODO.md` (Workflow §13). Do **not** create a human-verify playtest. Do **not** check an Outcomes row or Acceptance in this unit — work-verifier fails a unit that checks them. Leave the outcome `[ ]`
- If the parent brief names a host cwd / worktree path → work only there; do not create or remove worktrees; do not checkout default
