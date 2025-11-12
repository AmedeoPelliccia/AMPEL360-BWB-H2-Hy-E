#!/usr/bin/env python3
"""
CG Scan
Produces audit report of:
- Broken internal links
- Plain ATA reference mentions (not yet hyperlinked)
"""

from pathlib import Path
import re

REPO_ROOT = Path(__file__).resolve().parents[2]
FRAME = REPO_ROOT / "OPT-IN_FRAMEWORK"
REPORT = REPO_ROOT / "cd" / "reports" / "cg_scan_report.md"

LINK_RE = re.compile(r"\[([^\]]+)\]\(([^)]+)\)")
PLAIN_REF_RE = re.compile(r"\b(ATA[_-]?\d{2}(?:[-_]\d{2})?(?:[-_]\d{2})?)\b")

def md_files():
    if FRAME.exists():
        yield from FRAME.rglob("*.md")
    for p in [REPO_ROOT/"README.md"] + list(REPO_ROOT.glob("CAOS_*.md")):
        if p.exists(): yield p

def is_internal(link: str) -> bool:
    return not link.startswith(("http://","https://","#","mailto:"))

def resolve(src: Path, link: str) -> Path:
    return (src.parent / link).resolve() if not link.startswith("/") else (REPO_ROOT / link[1:]).resolve()

def main():
    REPORT.parent.mkdir(parents=True, exist_ok=True)
    lines = ["# CG Scan Report", ""]
    total_files = total_links = broken = plain_refs = 0

    for md in md_files():
        total_files += 1
        text = md.read_text(encoding="utf-8", errors="replace")
        rel = str(md.relative_to(REPO_ROOT))
        issues = []

        for m in LINK_RE.finditer(text):
            target = m.group(2)
            if is_internal(target):
                total_links += 1
                t = resolve(md, target).as_posix().split("#")[0]
                if not Path(t).exists():
                    broken += 1
                    issues.append(f"- 🔗 Broken link: `{target}`")

        for r in sorted(set(PLAIN_REF_RE.findall(text))):
            plain_refs += 1
            issues.append(f"- 📎 Unlinked ATA reference: `{r}`")

        if issues:
            lines.append(f"## {rel}")
            lines.extend(issues)
            lines.append("")

    lines += [
        "---", "",
        "## Summary", "",
        f"- Markdown files scanned: **{total_files}**",
        f"- Internal links found: **{total_links}**",
        f"- Broken links: **{broken}**",
        f"- Plain ATA references: **{plain_refs}**",
        "",
        "To auto-generate missing docs and convert references:",
        "`python tools/cg/generate.py`",
    ]

    REPORT.write_text("\n".join(lines), encoding="utf-8")
    print(f"[cg-scan] Report written to {REPORT}")

if __name__ == "__main__":
    main()
