#!/usr/bin/env python3
"""Behavioral eval + pack integrity for Agentic Doc Templates.

Usage:
  python3 eval/run_eval.py                          # integrity (CI default)
  python3 eval/run_eval.py prepare <case-id> [--out DIR]
  python3 eval/run_eval.py verify <case-id> --workdir DIR
  python3 eval/run_eval.py list
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EVAL = ROOT / "eval"
CASES = EVAL / "cases"
GEN = ROOT / "scripts" / "gen_role_adapters.py"

# Full de-confirm prose must live only here (pointer-only elsewhere).
DECONFIRM_SOT = ROOT / "docs/templates/agent/workflow/understanding.md"
DECONFIRM_MARKERS = [
    "De-confirm gate (`confirmed` → `draft` / `superseded`)",
    "An **additive** request is **not** a shape change",
]


def load_case(case_id: str) -> dict:
    path = CASES / f"{case_id}.json"
    if not path.exists():
        raise SystemExit(f"unknown case: {case_id} ({path})")
    data = json.loads(path.read_text())
    if data.get("id") != case_id:
        raise SystemExit(f"case id mismatch in {path}")
    return data


def list_cases() -> list[str]:
    return sorted(p.stem for p in CASES.glob("*.json"))


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    h.update(path.read_bytes())
    return h.hexdigest()


def snapshot_tree(root: Path) -> dict[str, str]:
    out: dict[str, str] = {}
    for p in sorted(root.rglob("*")):
        if p.is_file():
            rel = str(p.relative_to(root)).replace("\\", "/")
            out[rel] = sha256_file(p)
    return out


# ----- integrity -----------------------------------------------------------


def check_adapters() -> list[str]:
    errors: list[str] = []
    if not GEN.exists():
        return [f"missing {GEN}"]
    r = subprocess.run(
        [sys.executable, str(GEN), "--check"],
        cwd=ROOT,
        capture_output=True,
        text=True,
    )
    if r.returncode != 0:
        errors.append("adapter drift:\n" + (r.stdout or r.stderr))
    return errors


def check_deconfirm_sot() -> list[str]:
    errors: list[str] = []
    if not DECONFIRM_SOT.exists():
        return [f"missing source of truth {DECONFIRM_SOT.relative_to(ROOT)}"]
    sot = DECONFIRM_SOT.read_text()
    for marker in DECONFIRM_MARKERS:
        if marker not in sot:
            errors.append(
                f"SoT missing marker {marker!r} in {DECONFIRM_SOT.relative_to(ROOT)}"
            )

    # Long gate prose must not be restated outside SoT + changelog/eval docs.
    allow = {
        DECONFIRM_SOT.resolve(),
        (ROOT / "docs/templates/CHANGELOG.md").resolve(),
        (ROOT / "eval/README.md").resolve(),
    }
    # Ignore generated adapter check via bodies pointing short
    needle = "An **additive** request is **not** a shape change"
    for path in (ROOT / "docs/templates").rglob("*.md"):
        if path.resolve() in allow:
            continue
        if path.name == "CHANGELOG.md":
            continue
        text = path.read_text()
        if needle in text:
            errors.append(
                f"de-confirm prose duplicated in {path.relative_to(ROOT)} "
                f"(keep full gate only in workflow/understanding.md)"
            )
    for path in (ROOT / "docs/templates").rglob("*.mdc"):
        text = path.read_text()
        if needle in text:
            errors.append(
                f"de-confirm prose duplicated in {path.relative_to(ROOT)}"
            )
    return errors


def check_case_schema(case: dict) -> list[str]:
    errors: list[str] = []
    for key in ("id", "title", "user", "fixture", "expect"):
        if key not in case:
            errors.append(f"{case.get('id','?')}: missing {key}")
    fixture = EVAL / case.get("fixture", "")
    if case.get("fixture") and not fixture.is_dir():
        errors.append(f"{case['id']}: missing fixture dir {fixture.relative_to(ROOT)}")
    expect = case.get("expect") or {}
    up = expect.get("understanding_path")
    if up and case.get("fixture"):
        if not (fixture / up).exists() and "files_must_not_exist" not in expect:
            # shape/additive fixtures should have the understanding
            if "understanding_status" in expect or "understanding_status_one_of" in expect:
                if not (fixture / up).exists():
                    errors.append(f"{case['id']}: fixture missing {up}")
    return errors


def check_pack_contract(case: dict) -> list[str]:
    errors: list[str] = []
    contract = case.get("pack_contract") or {}
    for item in contract.get("source_must_include") or []:
        path = ROOT / item["file"]
        if not path.exists():
            errors.append(f"{case['id']}: pack_contract missing file {item['file']}")
            continue
        text = path.read_text()
        for pat in item.get("patterns") or []:
            if pat not in text:
                errors.append(
                    f"{case['id']}: {item['file']} missing pattern {pat!r}"
                )
    for item in contract.get("summaries_must_point") or []:
        path = ROOT / item["file"]
        if not path.exists():
            errors.append(f"{case['id']}: summary file missing {item['file']}")
            continue
        text = path.read_text()
        for pat in item.get("must_contain") or []:
            if pat not in text:
                errors.append(
                    f"{case['id']}: {item['file']} should contain {pat!r}"
                )
        for pat in item.get("must_not_contain") or []:
            if pat in text:
                errors.append(
                    f"{case['id']}: {item['file']} still restates {pat!r}"
                )
    return errors


def run_integrity() -> int:
    errors: list[str] = []
    print("== adapters --check ==")
    errors.extend(check_adapters())
    print("== de-confirm source of truth ==")
    errors.extend(check_deconfirm_sot())
    print("== cases ==")
    ids = list_cases()
    if not ids:
        errors.append("no cases in eval/cases/")
    for cid in ids:
        case = load_case(cid)
        errors.extend(check_case_schema(case))
        errors.extend(check_pack_contract(case))
        print(f"  ok schema/contract: {cid}")
    if errors:
        print("\nFAIL")
        for e in errors:
            print(f"  - {e}")
        return 1
    print(f"\nPASS — {len(ids)} cases, adapters clean, de-confirm SoT unique")
    return 0


# ----- prepare / verify ----------------------------------------------------


def prepare(case_id: str, out: Path) -> int:
    case = load_case(case_id)
    fixture = EVAL / case["fixture"]
    if out.exists():
        shutil.rmtree(out)
    out.mkdir(parents=True)
    # copy fixture docs
    shutil.copytree(fixture / "docs", out / "docs")
    # symlink or copy pack templates so agents can open workflow modules
    templates_src = ROOT / "docs/templates"
    dest = out / "docs/templates"
    shutil.copytree(
        templates_src,
        dest,
        ignore=shutil.ignore_patterns("__pycache__", "*.pyc"),
    )
    snap = snapshot_tree(out)
    # Live project docs only — pack templates are reference material for the agent.
    live_snap = {
        k: v
        for k, v in snap.items()
        if k.startswith("docs/") and not k.startswith("docs/templates/")
    }
    meta = {
        "case": case_id,
        "user": case["user"],
        "role": case.get("role"),
        "baseline": live_snap,
    }
    (out / ".eval-meta.json").write_text(json.dumps(meta, indent=2) + "\n")
    brief = out / "EVAL_BRIEF.md"
    brief.write_text(
        f"""# Eval brief — `{case_id}`

**Title:** {case['title']}

**Role (if using doc-roles):** `{case.get('role', 'parent')}`

**User message:**

> {case['user']}

## Instructions for the agent under test

1. Treat `{out}` as the project root (modular docs already bootstrapped).
2. Follow installed / pack playbooks as usual (`docs/templates/agent/…`).
3. Apply **only** what the user message requires for this turn.
4. Stop. Do not invent unrelated features.

Then run:

```bash
python3 eval/run_eval.py verify {case_id} --workdir {out}
```
"""
    )
    print(f"Prepared {out}")
    print(f"User message: {case['user']}")
    print(f"Brief: {brief}")
    return 0


def read_status(text: str) -> str | None:
    m = re.search(r"\*\*Status\*\*\s*:\s*`([^`]+)`", text)
    return m.group(1) if m else None


def verify(case_id: str, workdir: Path) -> int:
    case = load_case(case_id)
    meta_path = workdir / ".eval-meta.json"
    if not meta_path.exists():
        print(f"missing {meta_path} — run prepare first")
        return 2
    meta = json.loads(meta_path.read_text())
    baseline: dict[str, str] = meta["baseline"]
    current = {
        k: v
        for k, v in snapshot_tree(workdir).items()
        if k.startswith("docs/") and not k.startswith("docs/templates/")
    }
    expect = case["expect"]
    errors: list[str] = []

    def abspath(rel: str) -> Path:
        return workdir / rel

    for rel in expect.get("files_must_exist") or []:
        if not abspath(rel).exists():
            errors.append(f"missing required file {rel}")

    for rel in expect.get("files_must_not_exist") or []:
        if abspath(rel).exists():
            errors.append(f"file should not exist: {rel}")

    for rel in expect.get("files_must_change") or []:
        if rel not in current:
            errors.append(f"expected change but file missing: {rel}")
        elif rel not in baseline:
            pass  # new file counts as change
        elif current[rel] == baseline[rel]:
            errors.append(f"expected file to change: {rel}")

    for rel in expect.get("files_must_not_change") or []:
        if rel in baseline and rel in current and current[rel] != baseline[rel]:
            errors.append(f"file should not change: {rel}")

    up = expect.get("understanding_path")
    if up and abspath(up).exists():
        text = abspath(up).read_text()
        status = read_status(text)
        if "understanding_status" in expect:
            if status != expect["understanding_status"]:
                errors.append(
                    f"Understanding status {status!r} != "
                    f"{expect['understanding_status']!r}"
                )
        if "understanding_status_one_of" in expect:
            allowed = expect["understanding_status_one_of"]
            if status not in allowed:
                errors.append(
                    f"Understanding status {status!r} not in {allowed}"
                )
        for pat in expect.get("understanding_must_contain") or []:
            if pat not in text:
                errors.append(f"Understanding missing {pat!r}")
        for pat in expect.get("understanding_must_not_contain") or []:
            if pat in text:
                errors.append(f"Understanding must not contain {pat!r}")

    if errors:
        print("VERIFY FAIL")
        for e in errors:
            print(f"  - {e}")
        return 1
    print(f"VERIFY PASS — {case_id}")
    return 0


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    sub = ap.add_subparsers(dest="cmd")

    sub.add_parser("list", help="list case ids")
    p_prep = sub.add_parser("prepare", help="materialize fixture for a case")
    p_prep.add_argument("case_id")
    p_prep.add_argument("--out", type=Path, default=Path("/tmp/adt-eval"))
    p_ver = sub.add_parser("verify", help="check workdir against expect")
    p_ver.add_argument("case_id")
    p_ver.add_argument("--workdir", type=Path, required=True)

    # default integrity when no subcommand
    ap.add_argument(
        "--integrity-only",
        action="store_true",
        help=argparse.SUPPRESS,
    )
    args = ap.parse_args()

    if args.cmd is None:
        return run_integrity()
    if args.cmd == "list":
        for cid in list_cases():
            print(cid)
        return 0
    if args.cmd == "prepare":
        return prepare(args.case_id, args.out)
    if args.cmd == "verify":
        return verify(args.case_id, args.workdir)
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
