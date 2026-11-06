#!/usr/bin/env python3
"""Validate the structural completeness of The Empty Spaces manuscript."""
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
BOOK = ROOT / "manuscript"
COUNTS = {
    "part-01-chaos": (1, 4),
    "part-02-competitors": (5, 9),
    "part-03-discovery": (10, 14),
    "part-04-verification": (15, 18),
    "part-05-legacy": (19, 22),
}

def main() -> int:
    problems = []
    contents = (BOOK / "CONTENTS.md").read_text(encoding="utf-8")
    expected = []
    for part, (first, last) in COUNTS.items():
        for number in range(first, last + 1):
            path = BOOK / part / f"chapter-{number:02d}.md"
            expected.append(path)
            if not path.is_file():
                problems.append(f"missing chapter: {path.relative_to(ROOT)}")
                continue
            content = path.read_text(encoding="utf-8")
            if f"第{number}章" not in content or "核心叙事问题" not in content:
                problems.append(f"bad chapter scaffold: {path.relative_to(ROOT)}")
            if f"{part}/chapter-{number:02d}.md" not in contents:
                problems.append(f"missing contents link: {path.relative_to(ROOT)}")

    if len(expected) != 22:
        problems.append("expected exactly 22 chapter definitions")
    prologue_path = BOOK / "00-prologue" / "prologue.md"
    if not prologue_path.is_file():
        problems.append("missing completed prologue")
    else:
        prologue = prologue_path.read_text(encoding="utf-8")
        chinese_characters = len(re.findall(r"[\u4e00-\u9fff]", prologue))
        if chinese_characters < 2500:
            problems.append(f"prologue too short: {chinese_characters} Han characters")
        if "## 注释与史料" not in prologue:
            problems.append("prologue lacks cited source notes")
        if "[^1]" not in prologue:
            problems.append("prologue lacks inline source references")
        if "1876" not in prologue or "1875" not in prologue:
            problems.append("prologue must distinguish discovery and density remeasurement")

    if not (BOOK / "06-epilogue" / "epilogue.md").is_file():
        problems.append("missing epilogue")
    for relative in [
        "research/sources.md", "research/fact-check.md",
        "research/chronology.md", "editorial/STYLE_GUIDE.md",
    ]:
        if not (ROOT / relative).is_file():
            problems.append(f"missing documentation: {relative}")

    # Only check local markdown links in contents; external sources are not checked here.
    for target in re.findall(r"\]\(([^)]+)\)", contents):
        if "://" in target or target.startswith("#"):
            continue
        resolved = (BOOK / target.split("#", 1)[0]).resolve()
        if not resolved.is_file():
            problems.append(f"broken contents link: {target}")

    if problems:
        for p in problems:
            print("FAIL:", p, file=sys.stderr)
        return 1
    print(f"PASS: 22 chapter scaffolds, complete prologue, epilogue and contents links")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
