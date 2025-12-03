#!/usr/bin/env python3
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
Sidebar sync tool for AMPEL360 wiki.

- Scans all .md files in the wiki directory (except _Sidebar.md/_Footer.md).
- Extracts all internal wiki links [[Page_Name]].
- Compares with links already in _Sidebar.md.
- Regenerates an AUTO-GENERATED block with any missing links.

Usage:
    python tools/wiki/sidebar_sync.py [--wiki-dir <path>] [--sidebar <path>]

Configuration:
    By default, the script looks for the wiki at the repository root.
    The sidebar file is expected to be _Sidebar.md in the wiki directory.
"""

import argparse
import logging
import re
import sys
from pathlib import Path
from typing import List, Set

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="[sidebar-sync] %(message)s",
)
logger = logging.getLogger(__name__)

# Markers for the auto-generated block in the sidebar
START_MARKER = "<!-- AUTO-GENERATED-MISSING-LINKS:START -->"
END_MARKER = "<!-- AUTO-GENERATED-MISSING-LINKS:END -->"

# Pattern to match internal wiki links [[Page_Name]]
LINK_PATTERN = re.compile(r"\[\[([^\[\]]+?)\]\]")

# Files to exclude from scanning
EXCLUDE_FILES = frozenset({
    "_Sidebar.md",
    "_Footer.md",
})


def find_markdown_files(base_dir: Path) -> List[Path]:
    """Find all markdown files in the wiki directory.

    Args:
        base_dir: The base directory to search.

    Returns:
        A list of Path objects for all markdown files found.
    """
    md_files: List[Path] = []
    for path in base_dir.rglob("*.md"):
        # Exclude .git, .github, and node_modules directories
        parts = {p.name for p in path.parents}
        if ".git" in parts or ".github" in parts or "node_modules" in parts:
            continue
        if path.name in EXCLUDE_FILES:
            continue
        md_files.append(path)
    return md_files


def extract_links_from_text(text: str) -> Set[str]:
    """Extract all [[...]] links from text.

    Args:
        text: The text content to search.

    Returns:
        A set of link targets found in the text.
    """
    return {m.group(1).strip() for m in LINK_PATTERN.finditer(text)}


def extract_links_from_files(files: List[Path]) -> Set[str]:
    """Extract all internal links from multiple files.

    Args:
        files: List of file paths to scan.

    Returns:
        A set of all unique link targets found across all files.
    """
    links: Set[str] = set()
    for f in files:
        try:
            content = f.read_text(encoding="utf-8")
            links |= extract_links_from_text(content)
        except (OSError, UnicodeDecodeError) as e:
            logger.warning("Could not read %s: %s", f, e)
    return links


def read_sidebar(sidebar_path: Path) -> str:
    """Read the sidebar file content.

    Args:
        sidebar_path: Path to the sidebar file.

    Returns:
        The content of the sidebar file.

    Raises:
        SystemExit: If the sidebar file does not exist.
    """
    if not sidebar_path.exists():
        logger.error("Sidebar file not found: %s", sidebar_path)
        sys.exit(1)
    return sidebar_path.read_text(encoding="utf-8")


def extract_manual_links_from_sidebar(sidebar_text: str) -> Set[str]:
    """Extract links from sidebar excluding the auto-generated block.

    Args:
        sidebar_text: The sidebar content.

    Returns:
        Set of links from the manual (non-auto-generated) parts of sidebar.
    """
    # Remove the auto-generated block before extracting links
    if START_MARKER in sidebar_text and END_MARKER in sidebar_text:
        pre, _, rest = sidebar_text.partition(START_MARKER)
        _, _, post = rest.partition(END_MARKER)
        manual_text = pre + post
    else:
        manual_text = sidebar_text

    return extract_links_from_text(manual_text)


def update_sidebar_content(sidebar_text: str, missing_links: Set[str]) -> str:
    """Update the sidebar with the auto-generated missing links block.

    Args:
        sidebar_text: The current sidebar content.
        missing_links: Set of links that are missing from the sidebar.

    Returns:
        The updated sidebar content with the auto-generated block.
    """
    # Sort links alphabetically for stability
    sorted_links = sorted(missing_links)

    # Build the auto-generated block
    if sorted_links:
        lines = [
            START_MARKER,
            "",
            "## AUTO — Unlinked Wiki Pages",
            "",
            "> This block is auto-generated from internal `[[...]]` links",
            "> that are not yet explicitly referenced in the sidebar.",
            "",
        ]
        for link in sorted_links:
            lines.append(f"- [[{link}]]")
        lines.append("")
        lines.append(END_MARKER)
        lines.append("")
        new_block = "\n".join(lines)
    else:
        # If no missing links, leave a placeholder block
        new_block = "\n".join([
            START_MARKER,
            "",
            "## AUTO — Unlinked Wiki Pages",
            "",
            "> No internal links pending addition to the sidebar.",
            "",
            END_MARKER,
            "",
        ])

    if START_MARKER in sidebar_text and END_MARKER in sidebar_text:
        # Replace existing block
        pre, _, rest = sidebar_text.partition(START_MARKER)
        _, _, post = rest.partition(END_MARKER)
        # Post still contains any content after END_MARKER
        updated = pre.rstrip() + "\n\n" + new_block + post.lstrip("\n")
    else:
        # Append block at the end of sidebar
        sidebar_text = sidebar_text.rstrip() + "\n\n"
        updated = sidebar_text + new_block

    return updated


def main() -> int:
    """Main entry point for sidebar sync."""
    parser = argparse.ArgumentParser(
        description="Sync wiki sidebar with internal links."
    )
    parser.add_argument(
        "--wiki-dir",
        type=Path,
        default=None,
        help="Path to wiki directory. Defaults to repository root.",
    )
    parser.add_argument(
        "--sidebar",
        type=Path,
        default=None,
        help="Path to sidebar file. Defaults to _Sidebar.md in wiki directory.",
    )
    args = parser.parse_args()

    # Determine paths
    repo_root = Path(__file__).resolve().parents[2]
    wiki_dir = args.wiki_dir if args.wiki_dir else repo_root
    sidebar_path = args.sidebar if args.sidebar else wiki_dir / "_Sidebar.md"

    logger.info("Repo root: %s", repo_root)
    logger.info("Wiki dir:  %s", wiki_dir)
    logger.info("Sidebar:   %s", sidebar_path)

    # Find and scan markdown files
    md_files = find_markdown_files(wiki_dir)
    logger.info("Found %d markdown files to scan.", len(md_files))

    all_links = extract_links_from_files(md_files)
    logger.info("Found %d unique internal links [[...]] in wiki pages.", len(all_links))

    # Read current sidebar
    sidebar_text = read_sidebar(sidebar_path)
    sidebar_links = extract_manual_links_from_sidebar(sidebar_text)
    logger.info("Sidebar manually references %d unique internal links.", len(sidebar_links))

    # Calculate missing links
    missing = all_links - sidebar_links
    logger.info("Missing links in sidebar: %d", len(missing))

    # Update sidebar
    updated_sidebar = update_sidebar_content(sidebar_text, missing)

    if updated_sidebar != sidebar_text:
        sidebar_path.write_text(updated_sidebar, encoding="utf-8")
        logger.info("Sidebar updated with AUTO-GENERATED missing links block.")
    else:
        logger.info("Sidebar was already up to date.")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
