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
# SPDX-License-Identifier: Apache-2.0

"""
fill_placeholders.py

CGen placeholder filling automation for AMPEL360 documentation.

This tool automatically detects and fills placeholder content in documentation
files using AI-assisted generation. It supports:
- Legacy placeholders: "[To be completed]"
- New convention: "[CGEN:TODO]", "[CGEN:Scope]", etc.

The tool extracts document context, identifies sections, and generates
appropriate content using OpenAI's API.

Usage:
    python tools/genccc/fill_placeholders.py
    python tools/genccc/fill_placeholders.py --target OPT-IN_FRAMEWORK/I-INFRASTRUCTURES/ATA_03-SUPPORT_INFORMATION_GSE
    python tools/genccc/fill_placeholders.py --dry-run
"""

import argparse
import logging
import os
import re
from datetime import datetime
from pathlib import Path
from typing import Optional, Tuple

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)

# Repository root
SCRIPT_DIR = Path(__file__).resolve().parent
REPO_ROOT = SCRIPT_DIR.parents[1]

# Default target directory
DEFAULT_TARGET = REPO_ROOT / "OPT-IN_FRAMEWORK" / "I-INFRASTRUCTURES" / "ATA_03-SUPPORT_INFORMATION_GSE"

# Placeholder patterns
PLACEHOLDER_PATTERNS = [
    re.compile(r"^\[To be completed\]\s*$"),
    re.compile(r"^\[CGEN:.*\]\s*$"),
]

# Section title pattern (e.g., "2. Scope", "3. Overview")
SECTION_TITLE_RE = re.compile(r"^(#+)\s*(\d+)\.\s+(.*)$")


def is_placeholder(line: str) -> bool:
    """Check if a line is a placeholder that should be filled."""
    return any(p.match(line.strip()) for p in PLACEHOLDER_PATTERNS)


def extract_doc_header(lines: list) -> Tuple[Optional[str], Optional[str]]:
    """
    Extract document ID and title from the first line.
    Expected format: '10-00-02-005-A — LH₂ Properties and Hazards'
    
    Returns:
        (doc_id, doc_title) tuple
    """
    if not lines:
        return None, None

    header = lines[0].strip()
    # Remove leading # marks
    header = header.lstrip('#').strip()
    
    # Match pattern like "10-00-02-005-A — Title"
    m = re.match(r"^([0-9A-Z\-]+)\s+[—–-]\s+(.*)$", header)
    if m:
        return m.group(1), m.group(2)
    
    # Fallback: treat entire header as title
    return None, header


def generate_section_text(
    doc_id: str,
    doc_title: str,
    section_number: str,
    section_title: str,
    existing_context: str
) -> str:
    """
    Generate text for a section using OpenAI API.
    
    Args:
        doc_id: Document identifier (e.g., "10-00-02-005-A")
        doc_title: Document title
        section_number: Section number (e.g., "2")
        section_title: Section title (e.g., "Scope")
        existing_context: Previous content for context
    
    Returns:
        Generated section content
    """
    try:
        from openai import OpenAI
        client = OpenAI()  # Expects OPENAI_API_KEY in environment
    except ImportError:
        logger.error("OpenAI library not installed. Install with: pip install openai")
        return "[ERROR: OpenAI library not available]"
    except Exception as e:
        logger.error(f"Failed to initialize OpenAI client: {e}")
        return f"[ERROR: Failed to initialize OpenAI client - {e}]"

    prompt = f"""You are drafting safety and ground-operations documentation for the AMPEL360 program.

Document ID: {doc_id}
Document Title: {doc_title}

Write the full content for section "{section_number}. {section_title}" of this document.

Audience: safety engineering, ground-operations, and GSE teams.
Style: clear, concise, technical, in English, Markdown-compatible.
Do not write the section heading again, only the body content.
Use proper Markdown formatting (bullet lists, bold, tables as appropriate).

Existing document context (may be partial):
\"\"\"
{existing_context}
\"\"\"

Generate comprehensive, professional content appropriate for aerospace safety documentation.
"""

    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {
                    "role": "system",
                    "content": "You are a technical documentation expert specializing in aerospace safety and ground operations."
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            temperature=0.7,
            max_tokens=2000
        )
        
        text = response.choices[0].message.content or ""
        return text.strip()
    
    except Exception as e:
        logger.error(f"OpenAI API call failed: {e}")
        return f"[ERROR: Failed to generate content - {e}]"


def process_file(path: Path, dry_run: bool = False) -> bool:
    """
    Process a single file to fill placeholders.
    
    Args:
        path: Path to the file
        dry_run: If True, don't save changes
    
    Returns:
        True if changes were made, False otherwise
    """
    logger.info(f"Processing: {path}")
    
    try:
        original = path.read_text(encoding="utf-8")
    except Exception as e:
        logger.error(f"Failed to read {path}: {e}")
        return False

    lines = original.splitlines()
    
    # Extract document metadata
    doc_id, doc_title = extract_doc_header(lines)
    if not doc_id:
        doc_id = "UNKNOWN"
    if not doc_title:
        doc_title = path.stem

    logger.info(f"  Document: {doc_id} — {doc_title}")

    out_lines = []
    current_section_number = None
    current_section_title = None
    changes_made = False

    for i, line in enumerate(lines):
        # Detect section heading
        m = SECTION_TITLE_RE.match(line)
        if m:
            hash_marks = m.group(1)
            current_section_number = m.group(2)
            current_section_title = m.group(3)
            out_lines.append(line)
            logger.debug(f"  Found section: {current_section_number}. {current_section_title}")
            continue

        # Check for placeholder
        if is_placeholder(line) and current_section_title:
            logger.info(f"  Filling placeholder in section {current_section_number}. {current_section_title}")
            
            # Build context from recent lines
            context_lines = out_lines[-30:] if len(out_lines) > 30 else out_lines
            context_snippet = "\n".join(context_lines)

            # Generate content
            generated = generate_section_text(
                doc_id=doc_id,
                doc_title=doc_title,
                section_number=current_section_number,
                section_title=current_section_title,
                existing_context=context_snippet
            )

            out_lines.append(generated)
            out_lines.append("")  # Add blank line after generated content
            changes_made = True
            # Don't add the placeholder line
        else:
            out_lines.append(line)

    if not changes_made:
        logger.info(f"  No placeholders found in {path}")
        return False

    # Write back if not dry run
    new_text = "\n".join(out_lines)
    if not dry_run:
        try:
            path.write_text(new_text, encoding="utf-8")
            logger.info(f"  ✅ Filled placeholders in {path}")
        except Exception as e:
            logger.error(f"Failed to write {path}: {e}")
            return False
    else:
        logger.info(f"  [DRY RUN] Would update {path}")

    return True


def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(
        description="Fill CGen placeholders in AMPEL360 documentation"
    )
    parser.add_argument(
        "--target",
        type=Path,
        default=DEFAULT_TARGET,
        help="Target directory to process (default: ATA_03)"
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Don't save changes, just report what would be done"
    )
    parser.add_argument(
        "--verbose",
        action="store_true",
        help="Enable verbose logging"
    )
    
    args = parser.parse_args()
    
    if args.verbose:
        logging.getLogger().setLevel(logging.DEBUG)
    
    # Ensure OPENAI_API_KEY is set
    if not os.environ.get("OPENAI_API_KEY"):
        logger.warning("OPENAI_API_KEY not set - placeholder filling may fail")
    
    target_dir = args.target
    if not target_dir.exists():
        logger.error(f"Target directory does not exist: {target_dir}")
        return 1
    
    logger.info(f"Scanning for Markdown files in: {target_dir}")
    
    # Find all markdown files
    md_files = list(target_dir.rglob("*.md"))
    logger.info(f"Found {len(md_files)} Markdown file(s)")
    
    processed_count = 0
    changed_count = 0
    
    for md_file in md_files:
        processed_count += 1
        if process_file(md_file, dry_run=args.dry_run):
            changed_count += 1
    
    logger.info("")
    logger.info("="*60)
    logger.info(f"Summary:")
    logger.info(f"  Files processed: {processed_count}")
    logger.info(f"  Files changed:   {changed_count}")
    if args.dry_run:
        logger.info(f"  Mode: DRY RUN (no files were modified)")
    logger.info("="*60)
    
    return 0


if __name__ == "__main__":
    import sys
    sys.exit(main())
