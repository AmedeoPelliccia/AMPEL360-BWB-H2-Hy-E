#!/usr/bin/env python3
"""
score_relevance.py
Lightweight signal-based related-document scoring.
No embeddings required.

Signals used:
- Matching ATA codes
- Shared directory structure
- Document title keywords
"""
from pathlib import Path
import re
from typing import List, Tuple

ATA_RE = re.compile(r"(ATA[_\-\s]?\d{2}(?:[_\-\s]\d{2})?(?:[_\-\s]\d{2})?)", re.I)

def extract_signals(text: str, rel_path: str) -> set:
    sigs = set(tok.lower() for tok in ATA_RE.findall(text))
    parts = [p.lower() for p in rel_path.split("/")]
    sigs.update(parts)
    return sigs

def jaccard(a: set, b: set) -> float:
    if not a or not b: return 0.0
    return len(a & b) / len(a | b)

def score_pair(src_text: str, src_rel: str, dst_text: str, dst_rel: str) -> float:
    return jaccard(extract_signals(src_text, src_rel), extract_signals(dst_text, dst_rel))

def top_related(src_text: str, src_rel: str, universe: List[Tuple[str,str,str]], k: int = 5):
    scored = []
    for rel, title, full in universe:
        s = score_pair(src_text, src_rel, full, rel)
        if s > 0:
            scored.append((s, rel, title))
    scored.sort(reverse=True, key=lambda x: x[0])
    return scored[:k]
