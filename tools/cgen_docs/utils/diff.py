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
Diff and file writing utilities for CGen Docs Waves.

This module handles writing changes to files and managing sidecar metadata.
"""

import logging
import pathlib
from datetime import datetime, timezone
from typing import Any, Dict

import yaml

logger = logging.getLogger(__name__)


def write_sidecar(
    doc_path: pathlib.Path,
    batch: Dict[str, Any],
    ai_metadata: Dict[str, Any],
) -> None:
    """Write or update the CGen sidecar metadata file.

    The sidecar file tracks the evolution of the document through CGen waves.

    Args:
        doc_path: Path to the original document
        batch: Batch configuration
        ai_metadata: Metadata from AI response
    """
    output_config = batch.get("output", {})
    sidecar_ext = output_config.get("sidecar_extension", ".cgen.yaml")

    sidecar_path = doc_path.with_suffix(doc_path.suffix + sidecar_ext)

    # Load existing sidecar if present
    existing_data: Dict[str, Any] = {}
    if sidecar_path.exists():
        try:
            with open(sidecar_path, "r", encoding="utf-8") as f:
                existing_data = yaml.safe_load(f) or {}
        except Exception as e:
            logger.warning("Failed to read existing sidecar: %s", e)

    # Build new sidecar data
    timestamp = datetime.now(timezone.utc).isoformat()

    sidecar_data = {
        "document": str(doc_path.name),
        "last_cgen_wave": batch["batch_id"],
        "last_cgen_at": timestamp,
        "ai_model": ai_metadata.get("model", batch["ai_policy"].get("model", "unknown")),
        "reviewer": "TBD",
        "wave_history": existing_data.get("wave_history", []),
    }

    # Add to wave history
    wave_entry = {
        "wave_id": batch["batch_id"],
        "timestamp": timestamp,
        "model": sidecar_data["ai_model"],
        "tokens_used": ai_metadata.get("completion_tokens", 0),
    }
    sidecar_data["wave_history"].append(wave_entry)

    # Keep only last 10 entries
    sidecar_data["wave_history"] = sidecar_data["wave_history"][-10:]

    # Notes from AI metadata
    notes = ai_metadata.get("notes", [])
    if notes:
        sidecar_data["notes"] = notes[:3]  # Max 3 notes

    # Write sidecar
    try:
        with open(sidecar_path, "w", encoding="utf-8") as f:
            yaml.dump(sidecar_data, f, default_flow_style=False, sort_keys=False)
        logger.debug("Wrote sidecar: %s", sidecar_path)
    except Exception as e:
        logger.error("Failed to write sidecar %s: %s", sidecar_path, e)


def apply_changes(doc_path: pathlib.Path, new_content: str) -> None:
    """Write new content to a document file.

    Args:
        doc_path: Path to the document
        new_content: New content to write
    """
    try:
        # Create parent directories if needed
        doc_path.parent.mkdir(parents=True, exist_ok=True)

        with open(doc_path, "w", encoding="utf-8") as f:
            f.write(new_content)

        logger.info("Wrote changes to: %s", doc_path)

    except Exception as e:
        logger.error("Failed to write to %s: %s", doc_path, e)
        raise


def create_backup(doc_path: pathlib.Path) -> pathlib.Path:
    """Create a backup of the original document.

    Args:
        doc_path: Path to the document to backup

    Returns:
        Path to the backup file
    """
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_path = doc_path.with_suffix(f".{timestamp}.bak{doc_path.suffix}")

    try:
        content = doc_path.read_text(encoding="utf-8")
        with open(backup_path, "w", encoding="utf-8") as f:
            f.write(content)
        logger.debug("Created backup: %s", backup_path)
        return backup_path
    except Exception as e:
        logger.warning("Failed to create backup: %s", e)
        return doc_path


def compute_diff_summary(original: str, new: str) -> Dict[str, int]:
    """Compute a summary of differences between original and new content.

    Args:
        original: Original document content
        new: New document content

    Returns:
        Dictionary with diff statistics
    """
    orig_lines = original.splitlines()
    new_lines = new.splitlines()

    # Simple line-based diff stats
    orig_set = set(orig_lines)
    new_set = set(new_lines)

    added = len(new_set - orig_set)
    removed = len(orig_set - new_set)
    unchanged = len(orig_set & new_set)

    return {
        "lines_added": added,
        "lines_removed": removed,
        "lines_unchanged": unchanged,
        "total_original": len(orig_lines),
        "total_new": len(new_lines),
    }
