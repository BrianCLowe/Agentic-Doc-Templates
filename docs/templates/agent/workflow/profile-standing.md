# Docs profile & standing instructions

Follow the `adt-docs-profile` skill: [`docs/templates/agent/skills/adt-docs-profile/SKILL.md`](../skills/adt-docs-profile/SKILL.md). Do not reconstruct the procedure from memory.

| **First-class ADT-settings key** | When an enum/key already exists - set `docs_profile` / `sync.mode` / `team_inbox` / optionals (do **not** only put it in standing). Sync deletes an `orchestrator:` key (TEMPLATE_SYNC B0.5) |
| **Ask: rule or skill** | User told you **how to act in this project**, and it does **not** change an ADT playbook. Do **not** write standing. Ask once (below). |
- **How to act in this project** when it is not an ADT playbook override -> **ask rule or skill** (below). Do **not** file it in standing. Do **not** create the rule or skill before they answer.
### Project behavior that is not pack behavior *(ask once)*

When the user tells you **how to act** in this project - a genuine working guideline - and it does **not** change how an ADT playbook runs:

1. Do **not** append `standing.instructions`. Do **not** invent a project rule or skill in the same breath.
2. **Ask once:** should this be an always-on **rule / instruction** (every turn), or a **skill** (opened when that kind of work comes up)?
3. On **rule** → write it with the installed tool’s rule path ([`../tools/README.md`](../tools/README.md)). On **skill** → write a skill for that tool. On **no** → apply it this turn only if they still want that, and do not store it.
4. One line back: where it went, or that you left it out.

Product/UI for one stem stays on spec **Decisions**. Pack playbook overrides stay on standing or a first-class key. This ask is only the leftover: project behavior that is neither.
| Machine / host tool command that is not pack ceremony | `docs/Tooling.md` (Project verify or notes) |
### Sync cleanout *(2.9.6 one-shot — non-pack behavior leaves standing)*

Run only when the selected changelog catch-up includes **2.9.6**. Skip if `standing.instructions` is missing, empty, or comment-only.

**Open only:** `docs/ADT-settings.yaml` → `standing.instructions`. Do **not** scan the Document Map.

For **each** bullet:

1. **Keep** if it **overrides an ADT playbook** (docs ceremony / sync / re-ask / file-create) and no first-class key fits.
2. **Remove** if it is **how to act in this project** and it does **not** change an ADT playbook. Take it out of standing in this edit so it stops overriding the pack. Hold the text for the ask. Do **not** write a rule or skill yet.
3. Product/UI for a **named** stem, a tool command, or a decision that already has a file → leave those to **Sync relocate (2.7.25)** when that one-shot is also in catch-up. If 2.7.25 is **not** in catch-up, remove them from standing and include them in the same ask (do not invent a spec row during this cleanout).

**Then ask once**, in one message, for every removed bullet:

> These were in standing and they are not pack playbook overrides, so I took them out. For each, should it be an always-on **rule/instruction**, a **skill** opened when that work comes up, or **dropped**?

On **rule** → write it with the installed tool’s rule path ([`../tools/README.md`](../tools/README.md)). On **skill** → write a skill for that tool. On **dropped** → do not store it. Do **not** create either before they answer. If they do not answer, the bullets stay out of standing and the ask stays open.

**Do not:** leave non-pack behavior in standing until they answer. Do not silent-create a rule or skill under `auto` or `auto-all`. Do not rewrite a bullet you kept as a playbook override.
