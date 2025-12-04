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

# SPDX-License-Identifier: Apache-2.0

"""
Context loading utilities for CGen Docs Waves.

This module provides functions to load and assemble context information
for AI-assisted document processing.
"""

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
- **Framework**: OPT-IN (Organization, Program, Technology, Infrastructure, Neural Networks)

### Key Standards
- ATA iSpec 2200: Documentation structure
- DO-178C: Software considerations in airborne systems
- EASA CS-25: Large aeroplane certification specifications
- EU AI Act: AI system regulation

### Terminology
- **LC-XX**: Line Card (lifecycle phase identifier)
- **NN-XX**: Neural Network node
- **GenCCC**: Generative Configuration, Coverage, and Compliance
- **CAOS**: Continuous Airworthiness Orchestration System
- **DPP**: Digital Product Passport
"""


def load_global_context(
    batch: Dict[str, Any], context_root: pathlib.Path
) -> str:
    """Load global context from configured sources.

    Args:
        batch: Batch configuration containing context_sources
        context_root: Root directory for context loading

    Returns:
        Assembled global context string
    """
    context_parts = [AMPEL360_CONTEXT]

    context_sources = batch.get("context_sources", [])
    for source in context_sources:
        path = context_root.parent / source["path"]
        role = source.get("role", "reference")

        if path.exists():
            try:
                content = path.read_text(encoding="utf-8")
                # Truncate if too long
                if len(content) > MAX_CONTEXT_CHARS:
                    content = content[:MAX_CONTEXT_CHARS] + "\n[...truncated...]"

                context_parts.append(
                    f"\n### Context: {role}\nSource: {source['path']}\n\n{content}"
                )
                logger.debug("Loaded context from: %s", path)
            except Exception as e:
                logger.warning("Failed to load context from %s: %s", path, e)
        else:
            logger.debug("Context source not found: %s", path)

    return "\n".join(context_parts)


def load_context_snippets(
    doc_path: pathlib.Path, repo_root: pathlib.Path
) -> str:
    """Load context snippets relevant to a specific document.

    This function finds and loads related documents such as:
    - Parent README files
    - Sibling index files
    - Related ATA chapter documents

    Args:
        doc_path: Path to the document being processed
        repo_root: Repository root path

    Returns:
        Assembled context snippets string
    """
    snippets: List[str] = []

    # Look for parent README
    parent_readme = doc_path.parent / "README.md"
    if parent_readme.exists() and parent_readme != doc_path:
        try:
            content = parent_readme.read_text(encoding="utf-8")
            if len(content) > MAX_CONTEXT_CHARS // 2:
                content = content[: MAX_CONTEXT_CHARS // 2] + "\n[...truncated...]"
            snippets.append(f"### Parent README\n{content}")
        except Exception as e:
            logger.debug("Failed to read parent README: %s", e)

    # Look for index file
    index_file = doc_path.parent / "00_INDEX.md"
    if index_file.exists():
        try:
            content = index_file.read_text(encoding="utf-8")
            if len(content) > MAX_CONTEXT_CHARS // 2:
                content = content[: MAX_CONTEXT_CHARS // 2] + "\n[...truncated...]"
            snippets.append(f"### Directory Index\n{content}")
        except Exception as e:
            logger.debug("Failed to read index file: %s", e)

    # Look for grandparent README (ATA chapter level)
    grandparent_readme = doc_path.parent.parent / "README.md"
    if grandparent_readme.exists():
        try:
            content = grandparent_readme.read_text(encoding="utf-8")
            if len(content) > MAX_CONTEXT_CHARS // 4:
                content = content[: MAX_CONTEXT_CHARS // 4] + "\n[...truncated...]"
            snippets.append(f"### ATA Chapter README\n{content}")
        except Exception as e:
            logger.debug("Failed to read grandparent README: %s", e)

    # Extract ATA chapter info from path
    ata_info = extract_ata_info(doc_path, repo_root)
    if ata_info:
        snippets.append(f"### ATA Reference\n{ata_info}")

    return "\n\n".join(snippets) if snippets else ""


def extract_ata_info(doc_path: pathlib.Path, repo_root: pathlib.Path) -> Optional[str]:
    """Extract ATA chapter information from document path.

    Args:
        doc_path: Path to the document
        repo_root: Repository root path

    Returns:
        ATA chapter information string, or None
    """
    rel_path = doc_path.relative_to(repo_root)
    path_parts = rel_path.parts

    # Look for ATA chapter pattern (e.g., ATA_21-ECS, ATA_53-FUSELAGE)
    for part in path_parts:
        if part.startswith("ATA_"):
            # Extract chapter number
            try:
                chapter_part = part.split("-")[0].replace("ATA_", "")
                chapter_num = int(chapter_part)
                chapter_name = part.split("-", 1)[1] if "-" in part else ""
                return f"ATA Chapter {chapter_num}: {chapter_name.replace('_', ' ')}"
            except (ValueError, IndexError):
                pass

    return None


def get_related_documents(
    doc_path: pathlib.Path, repo_root: pathlib.Path, max_docs: int = 5
) -> List[pathlib.Path]:
    """Find related documents in the same directory or ATA chapter.

    Args:
        doc_path: Path to the current document
        repo_root: Repository root path
        max_docs: Maximum number of related documents to return

    Returns:
        List of paths to related documents
    """
    related: List[pathlib.Path] = []

    # Sibling documents
    parent = doc_path.parent
    for sibling in parent.glob("*.md"):
        if sibling != doc_path and sibling.name not in ("README.md", "00_INDEX.md"):
            related.append(sibling)
            if len(related) >= max_docs:
                break

    return related[:max_docs]
