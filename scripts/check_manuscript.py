#!/usr/bin/env python3
"""Validate The Empty Spaces chapter scaffolds, draft status, links and references."""
from pathlib import Path
import json
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
HAN = re.compile(r"[\u4e00-\u9fff]")
NOTES = re.compile(r"^\[\^(\d+)\]:", re.M)
USAGES = re.compile(r"\[\^(\d+)\]")


def main() -> int:
    issues = []
    contents = (BOOK / "CONTENTS.md").read_text(encoding="utf-8")
    metadata = json.loads((ROOT / "book.json").read_text(encoding="utf-8"))
    chapter_meta = {chapter["id"]: chapter for chapter in metadata["chapters"]}
    processed = 0
    drafts = 0
    outlines = 0

    for part, (first, last) in COUNTS.items():
        for n in range(first, last + 1):
            processed += 1
            label = f"chapter-{n:02d}"
            path = BOOK / part / f"{label}.md"
            relative = path.relative_to(ROOT).as_posix()
            m = chapter_meta.get(label)
            if not path.is_file():
                issues.append(f"missing chapter: {relative}")
                continue
            if not m:
                issues.append(f"missing book.json record: {label}")
                continue
            if m.get("file") != relative:
                issues.append(f"book.json path differs: {label}")
            status = m.get("status")
            doc = path.read_text(encoding="utf-8")
            if not re.search(r"^#\s*第(?:\d+|[一二三四五六七八九十百]+)章", doc, re.M):
                issues.append(f"missing chapter title: {relative}")
            if f"{part}/{label}.md" not in contents:
                issues.append(f"missing contents link: {relative}")
            book_title = m.get("title", "").split("：", 1)[-1]
            if book_title and book_title not in doc.splitlines()[0]:
                issues.append(f"chapter title differs from book.json: {relative}")
            if status == "draft":
                drafts += 1
                han_count = len(HAN.findall(doc))
                if han_count < 2500:
                    issues.append(f"draft too short ({han_count} Han chars): {relative}")
                if "待撰写：" in doc or "提纲占位／尚未撰写正文" in doc:
                    issues.append(f"draft still contains placeholder: {relative}")
                if "## 注释与史料" not in doc:
                    issues.append(f"draft has no cited source section: {relative}")
                defined = set(NOTES.findall(doc))
                used = set(USAGES.findall(doc))
                if not defined:
                    issues.append(f"draft has no footnote definitions: {relative}")
                if not used.issubset(defined):
                    issues.append(f"unresolved footnote(s) {sorted(used-defined)}: {relative}")
                if "（完整初稿，待史料审校）" not in contents.split(f"{part}/{label}.md", 1)[1].split("\n", 1)[0]:
                    issues.append(f"contents status differs from draft: {relative}")
            elif status == "outline":
                outlines += 1
                if "核心叙事问题" not in doc or "待撰写" not in doc:
                    issues.append(f"outline scaffold incomplete: {relative}")
                if "（待撰写）" not in contents.split(f"{part}/{label}.md", 1)[1].split("\n", 1)[0]:
                    issues.append(f"contents status differs from outline: {relative}")
            else:
                issues.append(f"unknown chapter status {status}: {relative}")

    if processed != 22:
        issues.append(f"expected 22 chapters, found {processed}")
    if len([c for c in metadata["chapters"] if c["id"].startswith("chapter-")]) != 22:
        issues.append("book.json must contain 22 chapter records")

    prologue = BOOK / "00-prologue" / "prologue.md"
    if not prologue.is_file():
        issues.append("missing prologue")
    else:
        doc = prologue.read_text(encoding="utf-8")
        if len(HAN.findall(doc)) < 2500:
            issues.append("prologue too short")
        if "## 注释与史料" not in doc or "[^1]" not in doc:
            issues.append("prologue lacks referenced notes")
        if "1875" not in doc or "1876" not in doc:
            issues.append("prologue must distinguish gallium discovery from density remeasurement")

    epilogue = BOOK / "06-epilogue" / "epilogue.md"
    epilogue_meta = chapter_meta.get("epilogue")
    if not epilogue.is_file():
        issues.append("missing epilogue")
    elif not epilogue_meta or epilogue_meta.get("status") != "draft":
        issues.append("epilogue must be recorded as full draft in book.json")
    else:
        epi = epilogue.read_text(encoding="utf-8")
        if len(HAN.findall(epi)) < 2500:
            issues.append("epilogue full draft too short")
        if "提纲占位／待撰写" in epi or "## 待办" in epi:
            issues.append("epilogue still contains placeholder text")
        if "## 注释与史料" not in epi:
            issues.append("epilogue lacks cited source section")
        defined = set(NOTES.findall(epi))
        used = set(USAGES.findall(epi))
        if not defined or not used.issubset(defined):
            issues.append("epilogue footnotes are missing or unresolved")
        if "06-epilogue/epilogue.md)（完整初稿，待史料审校）" not in contents:
            issues.append("contents status differs from full epilogue draft")
    for rel in ("research/sources.md", "research/fact-check.md", "research/chronology.md", "editorial/STYLE_GUIDE.md"):
        if not (ROOT / rel).is_file():
            issues.append(f"missing research/editing resource: {rel}")

    for target in re.findall(r"\]\(([^)]+)\)", contents):
        if "://" in target or target.startswith("#"):
            continue
        resolved = (BOOK / target.split("#", 1)[0]).resolve()
        if not resolved.is_file():
            issues.append(f"broken contents link: {target}")

    # Verify the reader-facing README and exact headings, not only the contents index.
    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    for item in metadata["chapters"]:
        rel = item["file"]
        if f"]({rel})" not in readme:
            issues.append(f"missing or malformed README manuscript link: {rel}")
        doc_path = ROOT / rel
        if doc_path.is_file():
            first_line = doc_path.read_text(encoding="utf-8").splitlines()[0]
            if first_line != f"# {item['title']}":
                issues.append(f"heading differs from book.json title: {rel}")

    if issues:
        for item in issues:
            print(f"FAIL: {item}", file=sys.stderr)
        return 1
    print(f"PASS: 22 chapters ({drafts} full drafts, {outlines} placeholders), "
          "prologue and full epilogue draft, footnotes, contents links and book.json")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
