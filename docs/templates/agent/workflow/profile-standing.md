<!-- pack-version: 2.7.17 -->

> **Workflow module.** Open from the [workflow index](../Modular_Docs_Workflow.md) only when docs profile or standing-instructions procedure is needed. Do not load other modules unless the index routes you there.

# Docs profile & standing instructions

## 0.1 Docs profile *(ceremony modes)*

**Live setting:** `docs/ADT-settings.yaml` → `docs_profile.mode` (`prevent` | `balanced` | `ship-first`). Example: [`ADT-settings.example.yaml`](../ADT-settings.example.yaml).

| Mode | Default file set on new map row | Coding gate | When to use |
|------|----------------------------------|-------------|-------------|
| **`prevent`** | Spec + **Understanding** (`draft`) + core TODO | **Do not code** while Understanding is `draft` unless user waives | Identity-sensitive products; you prefer prevent wrong builds (pack default) |
| **`balanced`** | Spec + core TODO; **+ Understanding** when identity is ambiguous / multi-surface / split pressure / user asked | Same draft gate **only for stems that have** an Understanding | Mid-size apps; you accept agent judgment on “needs shape file?” |
| **`ship-first`** | Spec + core TODO only (Understanding **not** required) | No Understanding draft gate — implement from TODO + thin spec | Prototypes, clear CRUD, “fix-forward” teams |

**Always required (all modes):** Master Index + Document Map, **spec**, **core TODO**, Human-TODO dual-write rules (§13). Catalog / decisions remain optional per their own sections.

**Unset `docs_profile`:** treat as **`prevent`**. Do **not** invent `ship-first` because files are missing.

**Suggest once** *(bootstrap Step 3p preference batch / first “build from reference” / sync B0.5 if still unset)*:

1. Skim `docs/reference/` (if any) + conversation — do not inventory the whole repo.
2. Recommend a mode with **2–3 short citations** (export path + quote or paraphrase). **Explain each option in plain language** so the user is not guessing labels:
   - **prevent** — “You confirm is/is-not before code” — competing product identities; “not X”; multi-surface / editor / game systems
   - **ship-first** — “Spec+TODO only; no shape gate” — clear CRUD/API; prototype/spike; tiny map
   - **balanced** — “Understanding only when identity is fuzzy (multi-surface, not-X, split, or you say lock shape)” — mid-size / mixed signals
3. **Ask once** (bootstrap: inside Step 3p preference batch). Record `docs_profile.mode`, `recorded`, and `source: agent-suggested` or `user`.
4. Re-ask only on explicit *Set docs profile to prevent|balanced|ship-first*.

**Upgrade / downgrade:**

| Change | Behavior |
|--------|----------|
| → **prevent** | Create missing Understandings as `draft` for map rows that lack them; do not wipe specs/TODOs |
| → **balanced** | Keep existing Understandings; stop requiring new ones when identity is clear |
| → **ship-first** | Stop requiring Understanding / confirm; **do not delete** existing `-Understanding.md` files |
| *Lock shape for [Stem]* (any mode) | Draft/update that stem’s Understanding and use the draft gate for **that stem** |

**Orchestrator / implementer readiness** — see [`roles/orchestrator.md`](../roles/orchestrator.md) and §3. Work-verifier always checks **spec + TODO**; Understanding only when the file exists or mode is prevent/balanced with a shape file.

---

## 0.2 Standing workflow instructions *(user workflow, not pack enums)*

**Live setting:** `docs/ADT-settings.yaml` → `standing.instructions` (YAML multi-line string). Example: [`ADT-settings.example.yaml`](../ADT-settings.example.yaml).

**Why:** Pack enums (`docs_profile`, `orchestrator.git.mode`, `sync.mode`, …) cover known forks. Freeform standing notes cover the long tail so user workflow does not die with the chat — e.g. “squash before mark ready” before that was a first-class mode.

| Prefer | Use for |
|--------|---------|
| **First-class ADT-settings key** | When an enum/key already exists — set `docs_profile` / `orchestrator.git.mode` / `sync.mode` / optionals (do **not** only put it in standing) |
| **`standing.instructions`** | Lasting **agent process / pack ceremony / delivery** prefs with no key yet, or finer tweaks enums do not express |
| **Spec Decisions (§10)** | Product/UI/interaction prefs for **one stem** (could be “improved away”) |
| **This-turn only** | One-off overrides the user does **not** want durable — apply now; **do not** write standing |

**Precedence (highest wins):**

1. Hard pack **safety** (dirty-tree hard stop before sync; no silent `current-push`; no force-push / protected-main surprises; no secrets in docs)
2. **This-turn** explicit user instruction
3. **`standing.instructions`** (when non-empty)
4. Structured ADT-settings enums + pack defaults

**Read:** On feature / implement / orchestrate paths, if `standing.instructions` is present and non-empty (ignore comment-only example lines), treat bullets as durable project prefs. Empty / missing = no ceremony — do not invent content.

### LOOKOUT — same-turn capture *(mandatory)*

Be on the lookout every turn. When the user states a **lasting** preference that **opposes pack defaults**, **corrects how the agent just worked**, or says **always / never / from now on / prefer / don’t** about **agent process** (git delivery, PR readiness, ceremony, verify style, “don’t re-ask X”, “always squash…”) → **same turn**:

1. If a **first-class key** fits → update that key in `docs/ADT-settings.yaml` (`recorded` today, `source: user`).
2. Else → **append** one short bullet under `standing.instructions` (create `standing:` if missing). Keep bullets imperative and durable (“When using draft PRs, squash before mark ready”).
3. Tell the user in one line that you saved it (path + paraphrase). Do **not** wait for session wrap or “remember that?”
4. Apply it for the rest of the session (and future sessions via the file).

**Also capture** when they correct pack behavior mid-run without the word “always” if the intent is durable (“I don’t want draft PRs — ready only after squash” → standing or `branch-pr-squash`; “merge each slice after CI” → `milestone-pr`).

**Skip:**

- One-off this-run scope (“just this PR”, “for today only”) unless they also say to keep it
- Product/UI polish for a stem → **Decisions** (§10), not standing
- Pure spacing / ephemeral chat flavor
- Inventing standing notes from “vibes” or agent taste
- Duplicating a preference already encoded in a first-class key (update the key; drop redundant standing bullets if obvious)

**Promotion:** When a standing note becomes a common pack feature, upstream may add an enum; users can set the key and delete the standing bullet. Standing remains the escape hatch.

**Bootstrap:** Do **not** force a freeform quiz. Optional one-liner after Step 3p: *“Any standing workflow notes to save in ADT-settings?”* — skip on no / defaults. Capture-as-you-go is the primary path.

**Explicit later:** *Add standing note: …* / *Clear standing instructions* / edit `docs/ADT-settings.yaml` directly.

---
