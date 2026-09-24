# Behavioral eval harness

> **Maintainers (this upstream repo only).** Tiny golden cases for “agents behave correctly” — the pack’s product value.  
> Outside `docs/templates/` and **not** in the release zip. Whole-repo / “Use this template” installs: bootstrap **Step 1d** deletes root `eval/` from user projects.

## What it checks

| Mode | Command | Needs a model? |
|------|---------|----------------|
| **Pack integrity** (always; this is what pack-checks runs) | `python3 eval/run_eval.py` | No — adapters, de-confirm SoT, VERSION uniqueness, Understanding skeleton, `DECISIONS.md`, case schema, **fail-snapshots must VERIFY FAIL** |
| **Prepare + verify** | `prepare` / `verify` | No for verify; an agent (or human) applies the turn between them |

Golden cases encode failures we have already seen in the field (e.g. additive idea → wrongly de-confirm Understanding).

## Quick start

```bash
# CI / local — no API keys
python3 eval/run_eval.py

# Manual behavioral pass for one case
python3 eval/run_eval.py prepare additive-keeps-confirmed --out /tmp/adt-eval
# …run your agent in /tmp/adt-eval with the printed user message…
python3 eval/run_eval.py verify additive-keeps-confirmed --workdir /tmp/adt-eval
```

## Case format

`eval/cases/<id>.json`:

```json
{
  "id": "additive-keeps-confirmed",
  "title": "…",
  "role": "feature-implementer",
  "user": "Also add CSV export research for this feature.",
  "fixture": "fixtures/additive-keeps-confirmed",
  "expect": {
    "understanding_status": "confirmed",
    "understanding_path": "docs/features/NoteEditor-Understanding.md",
    "files_must_change": [
      "docs/features/NoteEditor.md",
      "docs/features/NoteEditor-TODO.md"
    ],
    "files_must_not_change": [
      "docs/features/NoteEditor-Understanding.md"
    ],
    "understanding_must_not_contain": ["Status**: `draft`"]
  },
  "pack_contract": {
    "source_must_include": [
      {
        "file": "docs/templates/agent/workflow/understanding.md",
        "patterns": ["De-confirm gate", "keep `confirmed`", "additive"]
      }
    ],
    "summaries_must_point": [
      {
        "file": "docs/templates/agent/roles/feature-implementer.md",
        "must_contain": ["workflow/understanding.md"],
        "must_not_contain": ["An **additive** request that fits the confirmed"]
      }
    ]
  }
}
```

## Adding a case

1. Copy a fixture under `fixtures/<id>/` (or grow `fixtures/multi-stem-studio/` when the bug needs a real-looking map).
2. Add `cases/<id>.json` with `expect` + `pack_contract`.
3. For a trap the model must lose: add `fail_snapshot` pointing at a known-bad `fail-snapshots/<id>/docs/` tree. Integrity overlays it after `prepare` and **requires VERIFY FAIL**.
4. Run `python3 eval/run_eval.py` (integrity) and a prepare→agent→verify loop once.

Named fail modes to keep covered: wrong-engine build · operable-gap marked done · prevent skipping Understanding · build-first inventing Understanding · live instruction-footer left in place after sync · invented-decision Assumptions / example-as-identity · sync summary listing catalog optional tags as skipped.

Correctness for this pack ≈ case coverage. Prefer a new golden case over another paragraph of prose when a field bug shows up.
