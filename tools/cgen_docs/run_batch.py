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
CGen Docs Waves runner.

This script executes documentation improvement waves for AMPEL360 BWB H2 Hy-E.
It reads batch configurations, processes documents through AI-assisted deepening,
and maintains evolution metadata.

Usage:
    python tools/cgen_docs/run_batch.py --batch-id BATCH_ONBOARD_A
    python tools/cgen_docs/run_batch.py --batch-id BATCH_ONBOARD_A --dry-run
"""

import argparse
import json
import logging
import pathlib
import sys
from datetime import datetime, timezone
from typing import Any, Dict, List, Optional

import yaml

# Add parent directory to path for imports
sys.path.insert(0, str(pathlib.Path(__file__).parent))

from utils.context import load_context_snippets, load_global_context
from utils.ai import run_deepen_evolve_prompt, AIResponse
from utils.diff import write_sidecar, apply_changes
from utils.metadata import update_wave_log
from prompts.deepen_evolve import compose_prompt

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)
logger = logging.getLogger("cgen_docs")

# Minimum content length threshold for comprehensive documents (characters)
# Documents below this length are considered "short" and not comprehensive
MIN_COMPREHENSIVE_LENGTH = 800

# Threshold for automatic comprehensive protection (used in Check 4)
# Documents above this length with good content are automatically protected
COMPREHENSIVE_PROTECTION_LENGTH = 1500

# Status values that indicate validated/approved documentation
PROTECTED_STATUS_VALUES = [
    "APPROVED",
    "VALIDATED",
    "RELEASED",
    "FINAL",
    "ACCEPTED"
]


def is_document_protected(doc_text: str, doc_path: pathlib.Path) -> tuple[bool, str]:
    """
    Check if a document should be protected from AI overwriting.
    
    A document is protected if:
    1. It has a protected status in Document Control (APPROVED, VALIDATED, etc.) - HIGHEST PRIORITY
    2. It has substantial content (>800 chars minimum to be considered)
    3. It is comprehensive (>1500 chars, >15 content lines, <3 placeholders)
    4. It has minimal placeholders relative to sections (<30%)
    
    Args:
        doc_text: Full text of the document
        doc_path: Path to the document
    
    Returns:
        Tuple of (is_protected, reason)
    """
    lines = doc_text.splitlines()
    
    # Check 1: Protected status in Document Control (HIGHEST PRIORITY)
    # Documents with approved/validated status should ALWAYS be protected
    doc_lower = doc_text.lower()
    if "## document control" in doc_lower:
        # Check for status field
        for line in lines:
            line_lower = line.lower()
            if "status" in line_lower or "**status:**" in line_lower:
                # Check if status indicates protected/validated content
                for status in PROTECTED_STATUS_VALUES:
                    if status.lower() in line_lower:
                        return True, f"document has protected status: {status}"
    
    # Check 2: Substantial content length
    if len(doc_text) < MIN_COMPREHENSIVE_LENGTH:
        return False, "document is short (not comprehensive yet)"
    
    # Check 3: Count sections with real content vs placeholders
    section_count = 0
    placeholder_count = 0
    content_lines = 0
    
    for line in lines:
        stripped = line.strip()
        
        # Count sections (## headers)
        if stripped.startswith("##") and not stripped.startswith("###"):
            section_count += 1
        
        # Count placeholders
        if any(p in stripped.lower() for p in ["[to be completed]", "[cgen:", "[tbd]", "[tbr]"]):
            placeholder_count += 1
        
        # Count substantive content lines (longer lines with actual content)
        # Include bullet points as they are real content
        if len(stripped) > 40 and not stripped.startswith("#"):
            content_lines += 1
    
    # If document has many placeholders relative to sections, it's not comprehensive
    if section_count > 0 and placeholder_count >= section_count * 0.3:
        return False, f"document has {placeholder_count} placeholders in {section_count} sections"
    
    # If document lacks substantive content, it's not comprehensive
    if content_lines < 8:
        return False, "document lacks substantive content"
    
    # Check 4: If document is comprehensive (long with good content), protect it
    if len(doc_text) > COMPREHENSIVE_PROTECTION_LENGTH and content_lines > 15 and placeholder_count < 3:
        return True, "document is comprehensive with minimal placeholders"
    
    return False, "document can be improved by CGen"


def load_batch(batch_id: str, batches_dir: pathlib.Path) -> Dict[str, Any]:
    """Load batch configuration from YAML file.

    Args:
        batch_id: The batch identifier (e.g., BATCH_ONBOARD_A)
        batches_dir: Path to the batches directory

    Returns:
        Dictionary containing batch configuration

    Raises:
        FileNotFoundError: If batch file doesn't exist
        yaml.YAMLError: If YAML parsing fails
    """
    batch_file = batches_dir / f"{batch_id}.yaml"
    if not batch_file.exists():
        raise FileNotFoundError(f"Batch file not found: {batch_file}")

    logger.info("Loading batch configuration: %s", batch_file)
    with open(batch_file, "r", encoding="utf-8") as f:
        data = yaml.safe_load(f)

    # Validate required fields
    required_fields = ["batch_id", "scope", "targets", "ai_policy"]
    for field in required_fields:
        if field not in data:
            raise ValueError(f"Missing required field '{field}' in batch config")

    return data


def collect_documents(
    scope: List[Dict[str, Any]], repo_root: pathlib.Path
) -> List[pathlib.Path]:
    """Collect all documents matching the batch scope.

    Args:
        scope: List of scope entries from batch config
        repo_root: Root directory of the repository

    Returns:
        Sorted list of document paths
    """
    docs: List[pathlib.Path] = []

    for entry in scope:
        root = repo_root / entry["path"]
        if not root.exists():
            logger.warning("Scope path does not exist: %s", root)
            continue

        patterns = entry.get("patterns", ["**/*.md"])
        excludes = entry.get("exclude", [])

        for pattern in patterns:
            for file in root.glob(pattern):
                # Check exclusions
                excluded = False
                for ex in excludes:
                    if file.match(ex):
                        excluded = True
                        break

                if not excluded and file.is_file():
                    docs.append(file)

    unique_docs = sorted(set(docs))
    logger.info("Collected %d documents from scope", len(unique_docs))
    return unique_docs


def process_document(
    doc_path: pathlib.Path,
    batch: Dict[str, Any],
    global_context: str,
    repo_root: pathlib.Path,
    dry_run: bool = False,
) -> Optional[Dict[str, Any]]:
    """Process a single document through the CGen Docs Wave.

    Args:
        doc_path: Path to the document
        batch: Batch configuration
        global_context: Pre-loaded global context string
        repo_root: Repository root path
        dry_run: If True, don't write changes

    Returns:
        Dictionary with processing results, or None if skipped
    """
    logger.info("Processing: %s", doc_path.relative_to(repo_root))

    try:
        original_text = doc_path.read_text(encoding="utf-8")
    except Exception as e:
        logger.error("Failed to read %s: %s", doc_path, e)
        return None

    # Check if document is protected from overwriting
    is_protected, reason = is_document_protected(original_text, doc_path)
    if is_protected:
        logger.info("⚠️  SKIPPING protected document: %s", doc_path.relative_to(repo_root))
        logger.info("    Reason: %s", reason)
        return {
            "doc_path": str(doc_path.relative_to(repo_root)),
            "batch_id": batch["batch_id"],
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "skipped": True,
            "skip_reason": reason,
            "changed": False,
        }

    # Load document-specific context
    doc_context = load_context_snippets(doc_path, repo_root)

    # Compose the AI prompt
    prompt = compose_prompt(
        batch=batch,
        doc_path=doc_path,
        document_text=original_text,
        global_context=global_context,
        doc_context=doc_context,
        repo_root=repo_root,
    )

    # Run AI processing
    ai_response = run_deepen_evolve_prompt(prompt, batch["ai_policy"], dry_run=dry_run)

    if ai_response is None:
        logger.warning("AI processing returned no response for %s", doc_path)
        return None

    result = {
        "doc_path": str(doc_path.relative_to(repo_root)),
        "batch_id": batch["batch_id"],
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "model": ai_response.model,
        "tokens_used": ai_response.tokens_used,
        "changed": False,
        "summary": ai_response.summary,
    }

    if dry_run:
        logger.info("[DRY-RUN] Would process: %s", doc_path)
        return result

    # Apply post-processing rules
    new_text = apply_postrules(original_text, ai_response, doc_path)

    # Check for changes
    if new_text != original_text:
        result["changed"] = True
        
        # Quality check: prevent massive content reduction
        orig_len = len(original_text)
        new_len = len(new_text)
        reduction_ratio = (orig_len - new_len) / orig_len if orig_len > 0 else 0
        
        # If AI output is significantly shorter, it might be replacing good content with placeholders
        if reduction_ratio > 0.3:  # More than 30% reduction
            logger.warning("⚠️  AI output is significantly shorter than original")
            logger.warning("    Original: %d chars, New: %d chars (%.1f%% reduction)", 
                          orig_len, new_len, reduction_ratio * 100)
            logger.warning("    Forcing draft_sidecar mode to preserve original")
            write_mode = "draft_sidecar"
        else:
            write_mode = batch["ai_policy"].get("write_mode", "inplace")

        # Write sidecar metadata
        output_config = batch.get("output", {})
        if output_config.get("update_sidecars", True):
            write_sidecar(doc_path, batch, ai_response.metadata)

        # Apply changes based on write mode
        if write_mode == "draft_sidecar":
            draft_suffix = batch["ai_policy"].get("draft_suffix", "_CGEN_DRAFT")
            draft_path = doc_path.with_suffix(f"{draft_suffix}.md")
            apply_changes(draft_path, new_text)
            result["output_path"] = str(draft_path.relative_to(repo_root))
            logger.info("Draft saved to: %s (original preserved)", draft_path.relative_to(repo_root))
        else:
            apply_changes(doc_path, new_text)
            result["output_path"] = str(doc_path.relative_to(repo_root))

        # Update wave log
        if output_config.get("log_to_jsonl", True):
            log_path = repo_root / output_config.get("log_path", "cd/cgen_docs/logs")
            update_wave_log(log_path, batch["batch_id"], doc_path, ai_response, result)

        logger.info("Changes applied to: %s", doc_path)
    else:
        logger.info("No changes detected for: %s", doc_path)

    return result


def apply_postrules(
    original_text: str, ai_response: AIResponse, doc_path: pathlib.Path
) -> str:
    """Apply post-processing rules to AI output.

    Args:
        original_text: Original document text
        ai_response: AI response containing new text
        doc_path: Path to the document

    Returns:
        Processed text ready for writing
    """
    new_text = ai_response.content

    # Preserve original line endings
    if "\r\n" in original_text and "\r\n" not in new_text:
        new_text = new_text.replace("\n", "\r\n")

    # Ensure trailing newline
    if not new_text.endswith("\n"):
        new_text += "\n"

    # Validate Document Control section exists
    if "## Document Control" not in new_text:
        logger.warning("Document Control section missing in output for %s", doc_path)

    return new_text


def main() -> int:
    """Main entry point for CGen Docs Waves runner."""
    parser = argparse.ArgumentParser(
        description="CGen Docs Waves - AI-assisted documentation improvement"
    )
    parser.add_argument(
        "--batch-id",
        required=True,
        help="Batch identifier (e.g., BATCH_ONBOARD_A)",
    )
    parser.add_argument(
        "--batches-dir",
        default="cd/cgen_docs/batches",
        help="Path to batches directory",
    )
    parser.add_argument(
        "--context-root",
        default="OPT-IN_FRAMEWORK",
        help="Root directory for context loading",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Don't write changes, just show what would be done",
    )
    parser.add_argument(
        "--verbose",
        "-v",
        action="store_true",
        help="Enable verbose logging",
    )
    args = parser.parse_args()

    if args.verbose:
        logging.getLogger().setLevel(logging.DEBUG)

    # Determine repository root
    repo_root = pathlib.Path.cwd()
    batches_dir = repo_root / args.batches_dir

    try:
        # Load batch configuration
        batch = load_batch(args.batch_id, batches_dir)
        logger.info("Loaded batch: %s - %s", batch["batch_id"], batch.get("name", ""))

        # Collect documents
        docs = collect_documents(batch["scope"], repo_root)
        if not docs:
            logger.warning("No documents found in batch scope")
            return 0

        # Load global context
        context_root = repo_root / args.context_root
        global_context = load_global_context(batch, context_root)

        # Process each document
        results = []
        for doc in docs:
            result = process_document(
                doc_path=doc,
                batch=batch,
                global_context=global_context,
                repo_root=repo_root,
                dry_run=args.dry_run,
            )
            if result:
                results.append(result)

        # Summary
        changed = sum(1 for r in results if r.get("changed", False))
        skipped = sum(1 for r in results if r.get("skipped", False))
        processed = len(results) - skipped
        
        logger.info("")
        logger.info("="*60)
        logger.info("Wave complete:")
        logger.info("  Total documents: %d", len(results))
        logger.info("  Protected/skipped: %d", skipped)
        logger.info("  Processed: %d", processed)
        logger.info("  Changed: %d", changed)
        logger.info("="*60)

        return 0

    except FileNotFoundError as e:
        logger.error("File not found: %s", e)
        return 1
    except ValueError as e:
        logger.error("Configuration error: %s", e)
        return 1
    except Exception as e:
        logger.exception("Unexpected error: %s", e)
        return 1


if __name__ == "__main__":
    sys.exit(main())
