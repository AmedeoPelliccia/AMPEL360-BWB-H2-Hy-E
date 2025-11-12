#!/usr/bin/env python3
"""
CG Generate
- Converts ATA references into hyperlinks
- Creates missing target documents
- Uses AI contextual generation if OPENAI_API_KEY is provided
"""
from pathlib import Path
import os, re, datetime

REPO_ROOT = Path(__file__).resolve().parents[2]
FRAME = REPO_ROOT / "OPT-IN_FRAMEWORK"

LINK_RE = re.compile(r"\[([^\]]+)\]\(([^)]+)\)")
PLAIN_REF_RE = re.compile(r"\b(ATA[_-]?\d{2}(?:[-_]\d{2})?(?:[-_]\d{2})?)\b")

def md_files():
    if FRAME.exists():
        yield from FRAME.rglob("*.md")
    for p in [REPO_ROOT/"README.md"] + list(REPO_ROOT.glob("CAOS_*.md")):
        if p.exists(): yield p

def guess_target(token: str):
    norm = token.replace("_","-")
    matches = list(REPO_ROOT.rglob(f"*{norm}*.md"))
    return matches[0] if matches else None

def create_doc(path: Path, context: str):
    path.parent.mkdir(parents=True, exist_ok=True)
    if path.exists(): return False

    # Ensure path is within REPO_ROOT
    try:
        rel_path = path.relative_to(REPO_ROOT)
    except ValueError:
        # Path is outside REPO_ROOT, skip
        return False

    title = path.stem.replace("_"," ").replace("-"," ").title()
    timestamp = datetime.datetime.now().isoformat()
    placeholder = f"""# {title}
## Overview
Placeholder generated automatically. Path: `{rel_path}`

## Purpose
To be completed based on system role and ATA allocation.

## Document Control
Generated: {timestamp}
Status: Draft
Source: CG Generate
"""
    api = os.getenv("OPENAI_API_KEY")
    if api:
        try:
            from openai import OpenAI
            client = OpenAI(api_key=api)
            prompt = f"Generate a concise initial technical document for: {title}\nContext:\n{context[:1500]}"
            resp = client.chat.completions.create(
                model="gpt-4",
                messages=[{"role":"user","content":prompt}],
                temperature=0.2, max_tokens=900
            )
            placeholder = resp.choices[0].message.content or placeholder
        except Exception as e:
            print(f"[cg-generate] AI fallback for {title}: {e}")
            # Add note to document when AI generation fails
            placeholder = f"""# {title}
## Overview
Placeholder generated automatically. Path: `{rel_path}`

## Purpose
To be completed based on system role and ATA allocation.

## Document Control
Generated: {timestamp}
Status: Draft
Source: CG Generate (AI-enhanced generation attempted but failed)
Note: Template-based content used due to AI generation error

"""

    path.write_text(placeholder, encoding="utf-8")
    return True

def main():
    edits = 0
    for md in md_files():
        text = md.read_text(encoding="utf-8", errors="replace")
        original = text

        # Convert ATA references to hyperlinks
        # Use regex substitution with negative lookbehind to avoid replacing already-linked references
        for r in sorted(set(PLAIN_REF_RE.findall(text)), key=len, reverse=True):
            tgt = guess_target(r)
            if tgt:
                rel = os.path.relpath(tgt, md.parent)
                # Avoid replacing references that are already inside markdown links
                pattern = rf'(?<!\[)(?<!\]\(){re.escape(r)}(?!\]\()'
                text = re.sub(pattern, f"[{r}]({rel})", text)

        # Create documents for missing linked targets
        for m in LINK_RE.finditer(text):
            target = m.group(2).split("#")[0]
            if target.startswith(("http","mailto","#")):
                continue
            tgt_path = (md.parent / target).resolve()
            # Only create documents within REPO_ROOT
            try:
                tgt_path.relative_to(REPO_ROOT)
                if not tgt_path.exists():
                    create_doc(tgt_path, text)
            except ValueError:
                # Path is outside REPO_ROOT, skip
                pass

        if text != original:
            md.write_text(text, encoding="utf-8")
            edits += 1

    print(f"[cg-generate] Documents modified: {edits}")

if __name__ == "__main__":
    main()
