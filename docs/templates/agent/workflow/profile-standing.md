> **Workflow module.** Open from the [workflow index](../Modular_Docs_Workflow.md) only when docs profile or standing-instructions procedure is needed. Do not load other modules unless the index routes you there.

# Docs profile & standing instructions

## 0.1 Docs profile *(ceremony modes)*

**Live setting:** `docs/ADT-settings.yaml` → `docs_profile.mode` (`prevent` | `balanced` | `build-first`). Example: [`ADT-settings.example.yaml`](../ADT-settings.example.yaml).

**Legacy value:** `ship-first` is `build-first`. When you read it, rewrite the setting to `build-first` the same turn (sync does this in TEMPLATE_SYNC **B0.1b**). Do not re-ask. Do not treat it as unset.

| Mode | Default file set on new map row | Coding gate | When to use |
|------|----------------------------------|-------------|-------------|
| **`prevent`** | Spec + **Understanding** (`draft`) + core TODO | **Do not code** while Understanding is `draft` unless user waives | **Editors, games, multi-surface / identity-risky products.** Unset → this mode (do not silent-downgrade those repos). |
| **`balanced`** | Spec + core TODO; **+ Understanding** when identity is ambiguous / multi-surface / split pressure / user asked | Same draft gate **only for stems that have** an Understanding | Mid-size / mixed; you accept agent judgment on “needs shape file?” |
| **`build-first`** | Spec + core TODO only (Understanding **not** required) | No Understanding draft gate — implement from TODO + thin spec | **Typed APIs, CRUD, clear contracts.** First-class default for those products — not a concession or “ceremony off.” Also prototypes / fix-forward teams. |

**Always required (all modes):** Master Index + Document Map, **spec**, **core TODO**, Human-TODO dual-write rules (§13). Catalog / decisions remain optional per their own sections.

**Product vision** (`docs/Product-Vision.md` — whole-product end-state): **always create** (all profiles; unset → prevent). **`prevent`** → `draft` + user confirms product shape. **`balanced`** → lightweight; deepen when 2+ stems / fuzzy whole / *lock product shape*. **`build-first`** → lightweight destination; **not a gate** until *lock product shape* + confirm. Confirmed → feature work must not fight it. [`product-vision.md`](product-vision.md) §4.5.

**Unset `docs_profile`:** treat as **`prevent`**. Do **not** invent `build-first` because files are missing.

**Suggest once** *(bootstrap Step 3p preference batch / first “build from reference” / sync B0.5 if still unset)*:

1. Skim `docs/reference/` (if any) + conversation — do not inventory the whole repo.
2. Recommend a mode with **2–3 short citations** (export path + quote or paraphrase). **Explain each option in plain language** so the user is not guessing labels:
   - **prevent** — “You confirm is/is-not before code” — competing product identities; “not X”; **editors, games, multi-surface**
   - **build-first** — “Spec+TODO only; no shape gate” — **typed API / CRUD / clear contract** (the right default there); also prototype/spike; tiny map
   - **balanced** — “Understanding only when identity is fuzzy (multi-surface, not-X, split, or you say lock shape)” — mid-size / mixed signals
3. **Ask once** (bootstrap: inside Step 3p preference batch). Record `docs_profile.mode`, `recorded`, and `source: agent-suggested` or `user`.
4. Re-ask only on explicit *Set docs profile to prevent|balanced|build-first*.

**Upgrade / downgrade:**

| Change | Behavior |
|--------|----------|
| → **prevent** | Create missing Understandings as `draft` for map rows that lack them; do not wipe specs/TODOs |
| → **balanced** | Keep existing Understandings; stop requiring new ones when identity is clear |
| → **build-first** | Stop requiring Understanding / confirm; **do not delete** existing `-Understanding.md` files |
| *Lock shape for [Stem]* (any mode) | Draft/update that stem’s Understanding and use the draft gate for **that stem** |

**Orchestrator / implementer readiness** — see [`roles/orchestrator.md`](../roles/orchestrator.md) and §3. Work-verifier always checks **spec + TODO**; Understanding only when the file exists or mode is prevent/balanced with a shape file.

---

## 0.2 Standing workflow instructions *(user workflow, not pack enums)*

**Live setting:** `docs/ADT-settings.yaml` → `standing.instructions` (YAML multi-line string). Example: [`ADT-settings.example.yaml`](../ADT-settings.example.yaml).

**Why:** Pack enums (`docs_profile`, `orchestrator.git.mode`, `sync.mode`, …) cover known forks. Standing is the escape hatch when the user wants to **override an ADT playbook** (how *this pack* would otherwise run) and no first-class key exists yet — e.g. always squash before ready for a HEAD-only reviewer, or merge commit / rebase-merge / custom close-out that the seven git modes do not express. It is **not a scratch pad** for random notes. **Git-mode ask** (bootstrap 3p **E** / B0.6 / orchestrator resolve): **Write-in (not a quiz, not an eighth mode)** — mention it **on that menu**. Still do **not** quiz for standing. Do **not** invent an eighth mode.

| Prefer | Use for |
|--------|---------|
| **First-class ADT-settings key** | When an enum/key already exists — set `docs_profile` / `orchestrator.git.mode` / `sync.mode` / `team_inbox` / optionals (do **not** only put it in standing). **Not a key:** `orchestrator.git.worktrees` — host isolation is playbook-only ([`../roles/orchestrator-git.md`](../roles/orchestrator-git.md) **Host worktrees**) |
| **`standing.instructions`** | Lasting **overrides of this pack’s playbooks** (docs ceremony, git delivery, orchestrate / verify / re-ask, file-create) that no key expresses |
| **Spec Decisions (§10)** | Product/UI/interaction prefs for **one stem** (could be “improved away”) |
| **Ask: rule or skill** | User told you **how to act in this repo**, and it does **not** change an ADT playbook. Do **not** write standing. Ask once (below). |
| **This-turn only** | One-off overrides the user does **not** want durable — apply now; **do not** write standing |
| **Do not write** | Session asides, product thoughts, chat flavor |

**Precedence (highest wins):**

1. Hard pack **safety** (dirty-tree hard stop before sync; session-start docs freshness / sibling `docs/` drift — Workflow §0.3; no silent `current-push`; no force-push / protected-main surprises; no secrets in docs)
2. **This-turn** explicit user instruction
3. **`standing.instructions`** (when non-empty)
4. Structured ADT-settings enums + pack defaults

**Read:** On feature / implement / orchestrate paths, if `standing.instructions` is present and non-empty (ignore comment-only example lines), treat bullets as durable **playbook overrides**. Empty / missing = no ceremony — do not invent content.

### LOOKOUT — same-turn capture *(mandatory, playbook overrides only)*

Be on the lookout every turn. Capture **only** when the user is **overriding an ADT playbook** for future sessions — how *this pack* should run git, docs ceremony, orchestrate, verify handoff, re-ask, or file-create. Same turn:

1. If a **first-class key** fits → update that key in `docs/ADT-settings.yaml` (`recorded` today, `source: user`).
2. Else → **append** one short bullet under `standing.instructions` (create `standing:` if missing). Keep bullets imperative and durable. Do **not** create the key just to have a block.
3. Tell the user in one line that you saved it (path + paraphrase). Do **not** wait for session wrap or “remember that?”
4. Apply it for the rest of the session (and future sessions via the file).

**Also capture** when they correct **pack playbook behavior** mid-run without the word “always” if the intent is durable (“I don’t want draft PRs — ready only after squash” → standing or `branch-pr-squash`; “merge each slice after CI” → `milestone-pr`).

**Skip** *(do not write standing)*:

- **Do not jot random notes** — session asides, “remember this,” product thoughts, or a dump of chat flavor
- **How to prompt** another model / API / third-party product (xAI, Grok.com, ChatGPT, …) unless they are changing how an **ADT playbook** in this repo should run
- One-off this-run scope (“just this PR”, “for today only”) unless they also say to keep it
- Product/UI polish for a stem → **Decisions** (§10), not standing
- Correcting how you just worked on **product/code** (unless the correction is “stop following playbook X that way”)
- Pure spacing / ephemeral chat flavor
- Inventing standing notes from “vibes” or agent taste
- Duplicating a preference already encoded in a first-class key (update the key; drop redundant standing bullets if obvious)
- **How to act in this repo** when it is not an ADT playbook override → **ask rule or skill** (below). Do **not** file it in standing. Do **not** create the rule or skill before they answer.

### Repo behavior that is not pack behavior *(ask once)*

When the user tells you **how to act** in this repo — a genuine working guideline — and it does **not** change how an ADT playbook runs:

1. Do **not** append `standing.instructions`. Do **not** invent a project rule or skill in the same breath.
2. **Ask once:** should this be an always-on **rule / instruction** (every turn), or a **skill** (opened when that kind of work comes up)?
3. On **rule** → write it with the installed tool’s rule path ([`../tools/README.md`](../tools/README.md)). On **skill** → write a skill for that tool. On **no** → apply it this turn only if they still want that, and do not store it.
4. One line back: where it went, or that you left it out.

Product/UI for one stem stays on spec **Decisions**. Pack playbook overrides stay on standing or a first-class key. This ask is only the leftover: repo behavior that is neither.

**Promotion:** When a standing note becomes a common pack feature, upstream may add an enum; users can set the key and delete the standing bullet. Standing remains the escape hatch for playbook overrides.

**Bootstrap:** Do **not** quiz for standing. Skip unless they already stated a playbook override this conversation. Capture-as-you-go is the only path. Missing `standing:` is correct.

**Explicit later:** *Add standing note: …* / *Clear standing instructions* / edit `docs/ADT-settings.yaml` directly. *Add standing note* still means a **playbook override** — do not file prompt-engineering or other-product API style just because they said “remember.”

### Sync relocate *(2.7.25 one-shot — misplaced standing → live docs)*

Run only when the selected changelog catch-up includes **2.7.25** (TEMPLATE_SYNC_B Step B one-shot). Skip if `standing.instructions` is missing, empty, or comment-only examples.

**Open only:** `docs/ADT-settings.yaml` → `standing.instructions`, then **only** the one destination file a misplaced bullet names (below). Do **not** scan the Document Map or live feature/shared folder.

For **each** standing bullet:

1. **Keep** if it **overrides an ADT playbook** (git / ceremony / orchestrate / verify / re-ask / file-create) and no first-class key fits.
2. **Promote** if a first-class key fits **and that key is unset or already matches** → **unset:** set that key (`recorded` today, `source: user`) and **delete** the standing bullet. **Already matches:** **delete** the standing bullet (do **not** restamp). If the key is already set to a **different** value → **keep** the standing bullet; do **not** overwrite `docs_profile` / `orchestrator.git.mode` / `sync.mode` or stamp `source: user` (B0.6: that stamp blocks revert; user is not speaking this turn).
3. **Move then delete** anything else — do not leave a copy in standing:

| Misplaced bullet | Destination *(create the section/row if missing; do not invent a stem)* |
|------------------|------------------------------------------------------------------------|
| Product/UI / interaction for a **named** Document Map stem | That stem’s spec **Decisions** (1-line row). Fix stale Behavior / Acceptance / Visual in the **same edit** if they still state the old contract |
| How to prompt / call a **named** product API that is a map stem | That stem’s spec **Decisions** (or **Behavior** if that section already holds the call contract) |
| Machine / host tool command that is not pack ceremony | `docs/Tooling.md` (Project verify or notes) |
| Cross-cutting product choice and `docs/decisions/` already exists for it | That decision file (do **not** create a new ADR for a prompt-style aside) |

4. **No named home** (bullet names nothing on the Document Map / Tooling / an existing decision) → if this catch-up also includes **2.9.6**, leave **how to act in this repo** bullets for **Sync cleanout (2.9.6)** below. Do **not** drop those here. Any other no-home bullet → **delete from standing** and list the dropped text in the sync summary. Do **not** invent a map row, Understanding, spec, or `docs/decisions/` file.
5. Tell the user one line per relocated or dropped bullet (old paraphrase → new path, or “dropped, no home”).

**Do not:** invent standing; rewrite playbook-override bullets that already belong; open every spec “just in case”; treat `process-docs-only` as a ban on this one-shot (it bans a live scan, not the named destination).

### Sync cleanout *(2.9.6 one-shot — non-pack behavior leaves standing)*

Run only when the selected changelog catch-up includes **2.9.6**. Skip if `standing.instructions` is missing, empty, or comment-only.

**Open only:** `docs/ADT-settings.yaml` → `standing.instructions`. Do **not** scan the Document Map.

For **each** bullet:

1. **Keep** if it **overrides an ADT playbook** (git / ceremony / orchestrate / verify / re-ask / file-create) and no first-class key fits.
2. **Remove** if it is **how to act in this repo** and it does **not** change an ADT playbook. Take it out of standing in this edit so it stops overriding the pack. Hold the text for the ask. Do **not** write a rule or skill yet.
3. Product/UI for a **named** stem, a tool command, or a decision that already has a file → leave those to **Sync relocate (2.7.25)** when that one-shot is also in catch-up. If 2.7.25 is **not** in catch-up, remove them from standing and include them in the same ask (do not invent a spec row during this cleanout).

**Then ask once**, in one message, for every removed bullet:

> These were in standing and they are not pack playbook overrides, so I took them out. For each, should it be an always-on **rule/instruction**, a **skill** opened when that work comes up, or **dropped**?

On **rule** → write it with the installed tool’s rule path ([`../tools/README.md`](../tools/README.md)). On **skill** → write a skill for that tool. On **dropped** → do not store it. Do **not** create either before they answer. If they do not answer, the bullets stay out of standing and the ask stays open.

**Do not:** leave non-pack behavior in standing until they answer. Do not silent-create a rule or skill under `auto` or `auto-all`. Do not rewrite a bullet you kept as a playbook override.

---
