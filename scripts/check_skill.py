#!/usr/bin/env python3
"""Static integrity checks for the GPT-authored wanwu-keda v4 skill."""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "skills" / "wanwu-keda"
REFS = SKILL / "references"
EXPECTED = {
    "exploration-method.md",
    "dialogue-patterns.md",
    "reasoning-and-evidence.md",
    "evaluation.md",
}


def main() -> int:
    errors: list[str] = []
    text = (SKILL / "SKILL.md").read_text()
    routed = set(re.findall(r"references/([a-z-]+\.md)", text))

    if routed != EXPECTED:
        errors.append(f"routed refs = {sorted(routed)}, expected {sorted(EXPECTED)}")

    for name in sorted(EXPECTED):
        p = REFS / name
        if not p.exists():
            errors.append(f"missing reference: {name}")
        elif p.stat().st_size == 0:
            errors.append(f"empty reference: {name}")

    old = {"facets.md", "output.md", "traceability.md", "theory-cards.md", "workflow.md", "blindspots.md", "review.md", "explanation.md", "evidence.md"}
    leftovers = sorted(old & {p.name for p in REFS.iterdir() if p.is_file()})
    if leftovers:
        errors.append(f"v3 reference(s) still in current skill: {leftovers}")

    if "## 参考资料加载规则" not in text:
        errors.append("missing reference loading section")

    if errors:
        for e in errors:
            print(f"FAIL: {e}")
        return 1
    print("OK: 4 current references, loading section present, no v3 references in skill")
    return 0


if __name__ == "__main__":
    sys.exit(main())
