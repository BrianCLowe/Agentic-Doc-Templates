# Behavioral eval harness

> **Maintainers.** Tiny golden cases for “agents behave correctly” — the pack’s product value.  
> Consumers do **not** need this folder (it is outside `docs/templates/` and not in the release zip).

## What it checks

| Mode | Command | Needs a model? |
|------|---------|----------------|
| **Pack integrity** (always) | `python3 eval/run_eval.py` | No — adapter drift, de-confirm source-of-truth uniqueness, case schema |
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

1. Copy a fixture under `fixtures/<id>/` (minimal Master Index + one stem).
2. Add `cases/<id>.json` with `expect` + `pack_contract`.
3. Run `python3 eval/run_eval.py` (integrity) and a prepare→agent→verify loop once.

Correctness for this pack ≈ case coverage. Prefer a new golden case over another paragraph of prose when a field bug shows up.
