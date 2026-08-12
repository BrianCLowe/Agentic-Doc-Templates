<!-- pack-version: 2.7.17 -->

> **Workflow module.** Open from the [workflow index](../Modular_Docs_Workflow.md) for same-turn Decisions capture (product/UI prefs). Pack/process prefs → [profile-standing](profile-standing.md) §0.2.

# Decisions

## 10. Decisions *(lightweight)*

Record **why** something was chosen — not every task, only choices with lasting impact. **Capture in the same turn as the choice** — do not rely on the user asking to wrap up the session.

| Where | Use for |
|-------|---------|
| **Decisions** section in feature or shared **spec** | Choices local to that piece ([`Feature_Spec_Template.md`](../../Feature_Spec_Template.md)) |
| `docs/decisions/YYYY-MM-DD-short-title.md` | Cross-cutting choices ([`Decision_Template.md`](../../Decision_Template.md)) |
| **`standing.instructions`** in `docs/ADT-settings.yaml` | Lasting **agent process / pack workflow** prefs (not product UI) — see **§0.2** |

**When to record:**

1. **Understanding review** — user confirms a tradeoff → add row(s) when graduating / updating the spec (§2).
2. **Implement / polish** *(confirmed stem)* — user corrects a **preference that could be “improved away”** (e.g. always-on vs proximity chrome, confirm-before-delete, hide type while writing, empty lines aren’t chunks) → **same turn** append 1-line row(s) to that stem’s **Decisions** table. If Behavior / Acceptance / Visual references still state the old contract, fix those sentences in the **same edit**.
3. **Pack / agent process** — user opposes pack defaults or states always/never workflow prefs → **standing** or first-class ADT-settings key (**§0.2**), not Decisions.

**Skip:** pure spacing / pixel tweaks unless the user says “remember this.” Do **not** create `docs/decisions/` ADRs for feature-local polish. Do **not** dump choices into **Current focus** (handoff only — an optional one-line pointer to Decisions is fine). Do **not** put product UI prefs only in standing.

**Pattern:** `date | choice | why (short)`. Prefer several rows on one polish burst over separate ADR files.

Link standalone decision files from Master Index §3.4.

---
