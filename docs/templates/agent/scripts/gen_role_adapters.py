#!/usr/bin/env python3
"""Generate cursor/ and grok/ role adapters from adapter-src/.

Source of truth (sibling of this scripts/ folder):
  docs/templates/agent/roles/adapter-src/manifest.json
  docs/templates/agent/roles/adapter-src/bodies/*.md

Usage (from repo / project root):
  python3 docs/templates/agent/scripts/gen_role_adapters.py
  python3 docs/templates/agent/scripts/gen_role_adapters.py --check
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

AGENT_DIR = Path(__file__).resolve().parents[1]  # docs/templates/agent
SRC = AGENT_DIR / "roles" / "adapter-src"
MANIFEST = SRC / "manifest.json"
OUT = {
    "cursor": AGENT_DIR / "roles" / "cursor",
    "grok": AGENT_DIR / "roles" / "grok",
}
CMD = "python3 docs/templates/agent/scripts/gen_role_adapters.py"


def yaml_scalar(value) -> str:
    if isinstance(value, bool):
        return "true" if value else "false"
    return str(value)


def render_description(text: str) -> str:
    """Fold description as YAML >- block (single paragraph)."""
    words = " ".join(text.split())
    lines: list[str] = []
    cur: list[str] = []
    n = 0
    for w in words.split(" "):
        add = len(w) + (1 if cur else 0)
        if cur and n + add > 72:
            lines.append("  " + " ".join(cur))
            cur, n = [w], len(w)
        else:
            cur.append(w)
            n += add
    if cur:
        lines.append("  " + " ".join(cur))
    return "description: >-\n" + "\n".join(lines)


def render_frontmatter(name: str, description: str, extra: dict) -> str:
    parts = ["---", f"name: {name}", render_description(description)]
    preferred = ["prompt_mode", "model", "permission_mode", "agents_md"]
    keys = [k for k in preferred if k in extra] + [
        k for k in extra if k not in preferred
    ]
    for k in keys:
        parts.append(f"{k}: {yaml_scalar(extra[k])}")
    parts.append("---")
    return "\n".join(parts) + "\n"


def render_body(base_body: str, extra_hard_rules: list[str] | None) -> str:
    body = base_body.rstrip() + "\n"
    if not extra_hard_rules:
        return body
    if not body.rstrip().endswith("Hard rules:") and "Hard rules:" not in body:
        raise SystemExit("body missing Hard rules: section")
    extra_block = "\n".join(f"- {r}" for r in extra_hard_rules)
    return body.rstrip() + "\n" + extra_block + "\n"


def generate_one(name: str, entry: dict, harness: str) -> str:
    body_path = SRC / entry["body"]
    base_body = body_path.read_text()
    fm = dict(entry.get(harness) or {})
    extras = None
    if harness == "grok":
        extras = entry.get("grok_extra_hard_rules")
    text = render_frontmatter(name, entry["description"], fm)
    text += "\n" + render_body(base_body, extras)
    return text


def generate_all() -> dict[tuple[str, str], str]:
    manifest = json.loads(MANIFEST.read_text())
    out: dict[tuple[str, str], str] = {}
    for name, entry in manifest["roles"].items():
        for harness in manifest["harnesses"]:
            out[(harness, name)] = generate_one(name, entry, harness)
    return out


def write_all(files: dict[tuple[str, str], str]) -> None:
    for (harness, name), text in files.items():
        path = OUT[harness] / f"{name}.md"
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text)
        try:
            rel = path.relative_to(Path.cwd())
        except ValueError:
            rel = path
        print(f"wrote {rel}")


def check_all(files: dict[tuple[str, str], str]) -> int:
    drift = 0
    for (harness, name), text in files.items():
        path = OUT[harness] / f"{name}.md"
        try:
            rel = path.relative_to(Path.cwd())
        except ValueError:
            rel = path
        if not path.exists():
            print(f"MISSING {rel}")
            drift += 1
            continue
        if path.read_text() != text:
            print(f"DRIFT {rel}")
            drift += 1
    if drift:
        print(f"\n{drift} adapter(s) out of date. Run: {CMD}")
        return 1
    print(f"OK — {len(files)} adapters match adapter-src/")
    return 0


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument(
        "--check",
        action="store_true",
        help="fail if generated adapters differ from files on disk",
    )
    args = ap.parse_args()
    if not MANIFEST.exists():
        print(f"missing {MANIFEST}", file=sys.stderr)
        return 2
    files = generate_all()
    if args.check:
        return check_all(files)
    write_all(files)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
