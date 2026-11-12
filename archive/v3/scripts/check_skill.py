#!/usr/bin/env python3
"""Static integrity checks for the wanwu-keda skill.

This does not evaluate generated answers. It catches stale routing, missing
reference files, removed theory cards, and re-introduced fixed quotas.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "skills" / "wanwu-keda"
REFS = SKILL / "references"

FORBIDDEN = [
    r"标准\s*[：:]\s*4\s*[～~-]\s*6\s*个模块",
    r"深度\s*[：:]\s*8\s*[～~-]\s*10\s*个模块",
    r"标准\s*\|\s*4\s*[～~-]\s*6",
    r"深度\s*\|\s*8\s*[～~-]\s*10",
    r"3\s*[～~-]\s*6\s*个，(?:每个|都)",
    r"2\s*[～~-]\s*5\s*条",
    r"800\s*[～~-]\s*1800",
    r"2500\s*[～~-]\s*5000",
    r"3500\s*[～~-]\s*4500",
    r"8\s*[～~-]\s*12\s*条",
]


def fail(msg: str) -> None:
    print(f"FAIL: {msg}")


def main() -> int:
    errors: list[str] = []
    if not (SKILL / "SKILL.md").exists():
        errors.append("missing SKILL.md")
    if (REFS / "engines.md").exists():
        errors.append("obsolete references/engines.md still exists")

    routed = set(re.findall(r"references/([a-z-]+\.md)", (SKILL / "SKILL.md").read_text()))
    for name in sorted(routed):
        if not (REFS / name).exists():
            errors.append(f"routed file missing: references/{name}")

    facets = (REFS / "facets.md").read_text()
    cells = re.findall(r"^#### ([A-F]\d{1,2}) ", facets, re.M)
    if len(cells) != 44:
        errors.append(f"facets cells = {len(cells)}, expected 44")
    if len(set(cells)) != len(cells):
        errors.append("duplicate facet ids")

    cards = re.findall(r"^## (T\d{2}) ", (REFS / "theory-cards.md").read_text(), re.M)
    if len(cards) != 24:
        errors.append(f"theory cards = {len(cards)}, expected 24")
    if cards != [f"T{i:02d}" for i in range(1, 25)]:
        errors.append("theory card ids are not sequential T01..T24")

    for path in [SKILL / "SKILL.md", *sorted(REFS.glob("*.md"))]:
        text = path.read_text()
        for pattern in FORBIDDEN:
            if re.search(pattern, text):
                errors.append(f"forbidden fixed quota in {path.relative_to(ROOT)}: {pattern}")

    if errors:
        for e in errors:
            fail(e)
        return 1

    print(f"OK: {len(routed)} routed references, {len(cells)} facets, {len(cards)} theory cards, no fixed quotas")
    return 0


if __name__ == "__main__":
    sys.exit(main())
