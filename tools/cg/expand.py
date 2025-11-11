#!/usr/bin/env python3
"""
CG Expand
Gradually enriches underdeveloped sections.
Respects CG_MODE, CG_MAX_EDITS, CG_SECTION_MIN_WORDS.
"""
from pathlib import Path
import os, re

REPO_ROOT = Path(__file__).resolve().parents[2]
FRAME = REPO_ROOT / "OPT-IN_FRAMEWORK"

MODE = os.getenv("CG_MODE","BALANCED").upper()
MAX_EDITS = int(os.getenv("CG_MAX_EDITS","25"))
MIN_WORDS = int(os.getenv("CG_SECTION_MIN_WORDS","120"))

H2_RE = re.compile(r"^##\s+(.+)$", re.M)

def md_files():
    if FRAME.exists():
        yield from FRAME.rglob("*.md")

def word_count(s: str) -> int:
    return len(re.findall(r"\b\w+\b", s))

def expand(title: str, body: str, full: str) -> str:
    api = os.getenv("OPENAI_API_KEY")
    if not api:
        return body + "\n\n_TODO: Expansion Pending_\n"
    try:
        from openai import OpenAI
        client = OpenAI(api_key=api)
        prompt = f"""Improve this section in mode {MODE}. Avoid invented numbers. Keep ≤ 180 words.

Title: {title}
Current:
{body}

Context:
{full[:1200]}
"""
        resp = client.chat.completions.create(
            model="gpt-4",
            messages=[{"role":"user","content":prompt}],
            temperature=0.3, max_tokens=300
        )
        return resp.choices[0].message.content.strip()
    except:
        return body + "\n\n_TODO: Expansion Pending_\n"

def main():
    edits = 0
    for md in md_files():
        if edits >= MAX_EDITS:
            break
        text = md.read_text(encoding="utf-8", errors="replace")
        orig = text
        matches = list(H2_RE.finditer(text))
        for i, m in enumerate(matches):
            if edits >= MAX_EDITS:
                break
            start = m.end()
            end = matches[i+1].start() if i+1 < len(matches) else len(text)
            body = text[start:end].strip()
            if word_count(body) < MIN_WORDS:
                new_body = expand(m.group(1), body, text)
                text = text[:start] + "\n" + new_body + "\n" + text[end:]
                edits += 1
        if text != orig:
            md.write_text(text, encoding="utf-8")
    print(f"[cg-expand] Expanded sections: {edits} (mode={MODE})")

if __name__ == "__main__":
    main()
