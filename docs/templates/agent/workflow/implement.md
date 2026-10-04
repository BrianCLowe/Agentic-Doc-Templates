> **Workflow module.** Open from the [workflow index](../Modular_Docs_Workflow.md) when you need which docs to open for a stem. This pack does not run implementation.

# Working on a stem

## 3. Quick Start — Working on Any Task

The harness does the building. This pack keeps the docs those sessions read.

1. **Docs freshness** — `git status --porcelain` + `git worktree list` (Workflow §0.3). Sibling `docs/` drift → **stop**. Dirty **this** tree: note it; continue
2. Read `docs_profile` (if set) + `Master_Index.md` — Sections 1–3. Read `docs/Product-Vision.md`. Under **`prevent`**, the file set includes Understanding. Under **`build-first`**, the spec is enough. That choice is which docs to write. It is not a coding gate
3. Open that stem’s spec and `-Understanding.md` if it exists. Do the instructed task. A gap the confirmed docs already make obvious is part of that instruction. A second product or a checklist of future ideas is not. Do **not** create a `*-TODO.md`. There is no Current focus.
4. If this session changed shape or contract, update the Understanding and/or spec. Otherwise leave them.

### Shared vs feature

- Shared foundation → `_shared/[ComponentName].md` (and Understanding when the profile requires it)
- Feature → `features/[FeatureName].md` (same rule)
- If the work is really shared foundation, document it there — do not copy it into a feature spec

**Golden Rule**: If you find yourself scrolling through a long file, stop and split (§8).
