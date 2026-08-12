# Role adapter source

> **Maintainers only.** Cursor and Grok adapters under `../cursor/` and `../grok/` are **generated**. Edit here, then regenerate — do not hand-edit the harness copies.

## Layout

| Path | Role |
|------|------|
| [`manifest.json`](manifest.json) | Role list, descriptions, per-harness frontmatter, optional grok-only hard-rule extras |
| [`bodies/*.md`](bodies/) | Shared adapter body (intro + Hard rules) for both harnesses |

## Regenerate

```bash
python3 scripts/gen_role_adapters.py
python3 scripts/gen_role_adapters.py --check   # CI / pre-commit
```

## Rules

- Hard rules stay short. Full procedure lives in `../<role>.md` and `../../workflow/`.
- De-confirm / additive-vs-shape: **one pointer** to `workflow/understanding.md` §4 — do not restate the gate prose here.
- Never add an `orchestrator` adapter (parent-only).
