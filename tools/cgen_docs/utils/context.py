# Copyright 2025 AMPEL360 Project Contributors
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# SPDX-License-Identifier: Apache-2.0

"""
Context loading utilities for CGen Docs Waves.

This module provides functions to load and assemble context information
for AI-assisted document processing, including:

- Global programme context (AMPEL360 / OPT-IN / ATA / GenCCC).
- Local directory context (README, indices, ATA-level READMEs).
- Lightweight ATA metadata inferred from paths.
"""

from __future__ import annotations

import logging
import pathlib
from typing import Any, Dict, List, Optional

logger = logging.getLogger(__name__)

# Maximum characters to include from each context file
MAX_CONTEXT_CHARS = 4000

# Standard context snippets for AMPEL360
AMPEL360_CONTEXT = """
## AMPEL360 BWB H2 Hy-E Q100 Context

### Project Overview
- **Aircraft**: Blended Wing Body (BWB) configuration
- **Propulsion**: Hydrogen (H2) hybrid-electric system
- **Designation**: Q100 (100-passenger class)
- **Framework**: OPT-IN
  - O: Organization
  - P: Program
  - T: Technology (on-board systems)
  - I: Infrastructures (ground, circularity, digital)
  - N: Neural Networks / Users Traceability

### Key Standards and References
- ATA iSpec 2200: Documentation and chapter structure
- DO-178C / DO-330: Software & tool considerations
- ARP4754A / ARP4761: System development & safety
- EASA CS-25: Large aeroplane certification specifications
- EU AI Act: AI system regulation and risk categories

### Digital Governance and Tooling
- **GenCCC**: Generative Configuration, Coverage and Compliance
- **CGen Docs Waves**: Scheduled AI-assisted documentation improvements
- **CAOS**: Computer Aided Operations and Services
- **UTCS AQUA**: Traceability and evidence chain framework
- **DPP**: Digital Product Passport for systems and neural networks

### Terminology (Selected)
- **LC-XX**: Line Card identifier for lifecycle / discipline views
- **NN-XX**: Neural Network node identifier (ATA_95)
- **ATA_XX-YY-ZZ**: Chapter / section-numbering for systems and components
"""


# ---------------------------------------------------------------------------
# Internal helpers
# ---------------------------------------------------------------------------

def _read_truncated(path: pathlib.Path, limit: int) -> Optional[str]:
    """Read a text file and truncate it to a maximum number of characters."""
    try:
        content = path.read_text(encoding="utf-8")
    except Exception as exc:  # noqa: BLE001
        logger.debug("Failed to read context file %s: %s", path, exc)
        return None

    if len(content) > limit:
        return content[:limit] + "\n[...truncated...]"
    return content


# ---------------------------------------------------------------------------
# Global context
# ---------------------------------------------------------------------------

def load_global_context(batch: Dict[str, Any], context_root: pathlib.Path) -> str:
    """Load global context from configured sources.

    Args:
        batch: Batch configuration containing optional `context_sources`.
        context_root: Root directory for additional context documents.

    Returns:
        Assembled global context string (at least AMPEL360 base context).
    """
    context_parts: List[str] = [AMPEL360_CONTEXT]

    context_sources = batch.get("context_sources", [])
    if not context_sources:
        return "\n".join(context_parts)

    for source in context_sources:
        source_path = source.get("path")
        if not source_path:
            logger.debug("Skipping context source without 'path' key: %r", source)
            continue

        # Kept as context_root.parent for compatibility with existing configs.
        path = context_root.parent / source_path
        role = source.get("role", "reference")

        if not path.exists():
            logger.debug("Context source not found: %s", path)
            continue

        content = _read_truncated(path, MAX_CONTEXT_CHARS)
        if content is None:
            continue

        context_parts.append(
            f"\n### Context: {role}\nSource: {source_path}\n\n{content}"
        )
        logger.debug("Loaded context from: %s (role=%s)", path, role)

    return "\n".join(context_parts)


# ---------------------------------------------------------------------------
# Local / document-level context
# ---------------------------------------------------------------------------

def load_context_snippets(doc_path: pathlib.Path, repo_root: pathlib.Path) -> str:
    """Load context snippets relevant to a specific document.

    This function finds and loads related documents such as:
    - Parent README files.
    - Sibling index files.
    - Grandparent (ATA chapter) README.
    - Lightweight ATA chapter information derived from the path.

    Args:
        doc_path: Path to the document being processed.
        repo_root: Repository root path.

    Returns:
        Assembled context snippets string (may be empty).
    """
    snippets: List[str] = []

    # Parent README
    parent_readme = doc_path.parent / "README.md"
    if parent_readme.exists() and parent_readme != doc_path:
        content = _read_truncated(parent_readme, MAX_CONTEXT_CHARS // 2)
        if content:
            snippets.append(f"### Parent README\n{content}")

    # Directory index (00_INDEX.md)
    index_file = doc_path.parent / "00_INDEX.md"
    if index_file.exists():
        content = _read_truncated(index_file, MAX_CONTEXT_CHARS // 2)
        if content:
            snippets.append(f"### Directory Index\n{content}")

    # Grandparent README (often ATA chapter or LC-level)
    grandparent_readme = doc_path.parent.parent / "README.md"
    if grandparent_readme.exists():
        content = _read_truncated(grandparent_readme, MAX_CONTEXT_CHARS // 4)
        if content:
            snippets.append(f"### ATA/LC Level README\n{content}")

    # ATA info inferred from path
    ata_info = extract_ata_info(doc_path, repo_root)
    if ata_info:
        snippets.append(f"### ATA Reference\n{ata_info}")

    return "\n\n".join(snippets) if snippets else ""


# ---------------------------------------------------------------------------
# ATA extraction
# ---------------------------------------------------------------------------

def extract_ata_info(doc_path: pathlib.Path, repo_root: pathlib.Path) -> Optional[str]:
    """Extract ATA chapter information from a document path.

    Args:
        doc_path: Path to the document.
        repo_root: Repository root path.

    Returns:
        ATA chapter information string, or None if not identifiable.
    """
    rel_path = doc_path.relative_to(repo_root)
    path_parts = rel_path.parts

    # Look for ATA chapter pattern (e.g., ATA_21-ECS, ATA_53-FUSELAGE)
    for part in path_parts:
        if not part.startswith("ATA_"):
            continue

        try:
            base = part.split("-", 1)
            chapter_part = base[0].replace("ATA_", "")
            chapter_num = int(chapter_part)
            chapter_name = base[1] if len(base) > 1 else ""
            chapter_name_clean = chapter_name.replace("_", " ").strip()
            label = f"ATA Chapter {chapter_num}"
            if chapter_name_clean:
                label += f": {chapter_name_clean}"
            return label
        except (ValueError, IndexError):
            # Not a valid ATA pattern; continue scanning other parts
            continue

    return None


# ---------------------------------------------------------------------------
# Related documents
# ---------------------------------------------------------------------------

def get_related_documents(
    doc_path: pathlib.Path,
    repo_root: pathlib.Path,
    max_docs: int = 5,
) -> List[pathlib.Path]:
    """Find related documents in the same directory or ATA chapter.

    Currently implemented as:
    - Sibling Markdown documents in the same directory,
      excluding the current document and standard index files.

    Args:
        doc_path: Path to the current document.
        repo_root: Repository root path (currently unused, kept for future use).
        max_docs: Maximum number of related documents to return.

    Returns:
        List of paths to related documents (possibly empty).
    """
    related: List[pathlib.Path] = []

    parent = doc_path.parent
    # Deterministic ordering for reproducibility
    for sibling in sorted(parent.glob("*.md")):
        if sibling == doc_path:
            continue
        if sibling.name in ("README.md", "00_INDEX.md"):
            continue

        related.append(sibling)
        if len(related) >= max_docs:
            break

    return related[:max_docs]

