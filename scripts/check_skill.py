#!/usr/bin/env python3
"""Static integrity checks for the wanwu-kewen skill."""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "skills" / "wanwu-kewen" / "SKILL.md"


def main() -> int:
    errors: list[str] = []
    if not SKILL.exists():
        errors.append("missing skills/wanwu-kewen/SKILL.md")
    else:
        text = SKILL.read_text()
        if not text.startswith("---\n"):
            errors.append("SKILL.md must start with YAML frontmatter")
        match = re.search(r"^name:\s*(\S+)\s*$", text, re.M)
        if not match or match.group(1) != "wanwu-kewen":
            errors.append("frontmatter name must be wanwu-kewen")
        if "description:" not in text:
            errors.append("frontmatter description missing")
        for old in ("wanwu-keda", "references/", "archive/v3"):
            if old in text:
                errors.append(f"stale v3 reference in SKILL.md: {old}")

    old_dir = ROOT / "skills" / "wanwu-keda"
    if old_dir.exists():
        errors.append("old skills/wanwu-keda directory still exists")

    if errors:
        for e in errors:
            print(f"FAIL: {e}")
        return 1
    print("OK: wanwu-kewen SKILL.md present, frontmatter valid, no old skill directory")
    return 0


if __name__ == "__main__":
    sys.exit(main())
