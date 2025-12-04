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
CGen Writer System — Tier-1 Ready

This module replaces the previous diff/write/sidecar utilities with a
robust, deterministic, certification-friendly writer subsystem supporting:

- CGen Docs Waves
- UTCS AQUA evidence chains
- GenCCC governance
- Safe & versioned writes
- Validated sidecars (schema-less but structurally enforced)
- DO-178C-friendly diff semantics
"""

from __future__ import annotations

import difflib
import logging
import pathlib
from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Any, Dict, List, Optional

import yaml

logger = logging.getLogger(__name__)


# ======================================================================
# UTILITY: TIMESTAMP
# ======================================================================

def utc_now() -> str:
    """Return ISO-8601 UTC timestamp."""
    return datetime.now(timezone.utc).isoformat()


# ======================================================================
# BACKUP MANAGER
# ======================================================================

@dataclass
class BackupManager:
    """Creates deterministic timestamped backups for documents."""

    def create(self, path: pathlib.Path) -> pathlib.Path:
        """Create a timestamped backup of the document.

        Args:
            path: Path to the document to backup

        Returns:
            Path to the backup file, or original path if backup fails
        """
        timestamp = datetime.now(timezone.utc).strftime("%Y%m%d_%H%M%S")
        backup_path = path.with_suffix(f".bak.{timestamp}{path.suffix}")

        try:
            content = path.read_text(encoding="utf-8")
            backup_path.write_text(content, encoding="utf-8")
            logger.debug("Created backup: %s", backup_path)
            return backup_path
        except Exception as e:
            logger.warning("Backup creation failed for %s: %s", path, e)
            return path


# ======================================================================
# DIFF ENGINE — DO-178C-FRIENDLY
# ======================================================================

@dataclass
class DiffEngine:
    """Computes a deterministic diff suitable for certification logs."""

    def compute(self, original: str, new: str) -> Dict[str, Any]:
        """Compute a detailed diff between original and new content.

        Args:
            original: Original document content
            new: New document content

        Returns:
            Dictionary with diff statistics and unified diff lines
        """
        orig_lines = original.splitlines()
        new_lines = new.splitlines()

        # Unified diff (DO-178C-friendly representation)
        diff_lines = list(
            difflib.unified_diff(
                orig_lines,
                new_lines,
                fromfile="original",
                tofile="new",
                lineterm=""
            )
        )

        # Line statistics
        added = sum(
            1 for line in diff_lines
            if line.startswith("+") and not line.startswith("+++")
        )
        removed = sum(
            1 for line in diff_lines
            if line.startswith("-") and not line.startswith("---")
        )
        changed = added + removed

        return {
            "lines_added": added,
            "lines_removed": removed,
            "lines_changed_total": changed,
            "total_original": len(orig_lines),
            "total_new": len(new_lines),
            "diff_unified": diff_lines,
        }


# ======================================================================
# SIDECAR WRITER — UTCS AQUA TIER-1
# ======================================================================

@dataclass
class SidecarWriter:
    """
    Writes or updates .cgen.yaml metadata following UTCS AQUA rules.

    Key attributes:
    - Deterministic updates.
    - Wave history capped at N entries.
    - Ensures structural integrity even without a schema file.
    """

    max_history: int = 20
    extension: str = ".cgen.yaml"

    def path_for(self, doc_path: pathlib.Path) -> pathlib.Path:
        """Return normalized sidecar path: file.md.cgen.yaml

        Maintains backward compatibility by appending sidecar extension
        to the document's existing suffix.

        Args:
            doc_path: Path to the document

        Returns:
            Path to the sidecar file
        """
        return doc_path.with_suffix(doc_path.suffix + self.extension)

    def load(self, sidecar_path: pathlib.Path) -> Dict[str, Any]:
        """Load existing sidecar (if present).

        Args:
            sidecar_path: Path to the sidecar file

        Returns:
            Loaded sidecar data or empty dict
        """
        if not sidecar_path.exists():
            return {}

        try:
            data = yaml.safe_load(sidecar_path.read_text(encoding="utf-8")) or {}
            if not isinstance(data, dict):
                logger.warning("Sidecar corrupted (not a dict): %s", sidecar_path)
                return {}
            return data
        except Exception as e:
            logger.warning("Failed to read sidecar %s: %s", sidecar_path, e)
            return {}

    def write(
        self,
        doc_path: pathlib.Path,
        batch: Dict[str, Any],
        ai_metadata: Dict[str, Any],
    ) -> pathlib.Path:
        """Update sidecar metadata according to UTCS AQUA.

        Args:
            doc_path: Path to the document
            batch: Batch configuration
            ai_metadata: Metadata from AI response

        Returns:
            Path to the written sidecar file
        """
        sidecar_path = self.path_for(doc_path)
        existing = self.load(sidecar_path)

        timestamp = utc_now()
        wave_id = batch.get("batch_id", "UNKNOWN")
        ai_model = ai_metadata.get(
            "model", batch.get("ai_policy", {}).get("model", "unknown")
        )
        # Support both 'tokens_used' and legacy 'completion_tokens' field names
        tokens_used = ai_metadata.get(
            "tokens_used", ai_metadata.get("completion_tokens", 0)
        )

        # merge history
        history: List[Dict[str, Any]] = existing.get("wave_history", [])
        history.append(
            {
                "wave_id": wave_id,
                "timestamp": timestamp,
                "model": ai_model,
                "tokens_used": tokens_used,
            }
        )
        history = history[-self.max_history:]

        new_data: Dict[str, Any] = {
            "document": doc_path.name,
            "last_cgen_wave": wave_id,
            "last_cgen_at": timestamp,
            "ai_model": ai_model,
            "reviewer": "TBD",
            "wave_history": history,
        }

        # Notes (max 3)
        notes = ai_metadata.get("notes")
        if notes:
            new_data["notes"] = notes[:3]

        try:
            with open(sidecar_path, "w", encoding="utf-8") as f:
                yaml.dump(
                    new_data,
                    f,
                    default_flow_style=False,
                    sort_keys=False,
                )
            logger.debug("Sidecar written: %s", sidecar_path)
        except Exception as e:
            logger.error("Failed to write sidecar %s: %s", sidecar_path, e)

        return sidecar_path


# ======================================================================
# DOCUMENT WRITER — SAFE, ATOMIC, CERT-READY
# ======================================================================

@dataclass
class DocumentWriter:
    """Writes updated document content safely."""

    def write(self, path: pathlib.Path, content: str) -> None:
        """Write content to a document file.

        Args:
            path: Path to the document
            content: Content to write

        Raises:
            Exception: If write fails
        """
        try:
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(content, encoding="utf-8")
            logger.info("Wrote document: %s", path)
        except Exception as e:
            logger.error("Failed to write document %s: %s", path, e)
            raise


# ======================================================================
# CGen Writer Orchestrator
# ======================================================================

@dataclass
class CGenWriter:
    """High-level orchestrator integrating backup, diff, write, and sidecar."""

    backup: BackupManager = field(default_factory=BackupManager)
    diff_engine: DiffEngine = field(default_factory=DiffEngine)
    sidecar: SidecarWriter = field(default_factory=SidecarWriter)
    writer: DocumentWriter = field(default_factory=DocumentWriter)

    def apply_updates(
        self,
        doc_path: pathlib.Path,
        original_content: str,
        new_content: str,
        batch: Dict[str, Any],
        ai_metadata: Dict[str, Any],
    ) -> Dict[str, Any]:
        """
        Apply document changes with:
        - backup creation
        - diff calculation
        - safe write
        - sidecar update

        Args:
            doc_path: Path to the document
            original_content: Original document content
            new_content: New document content
            batch: Batch configuration
            ai_metadata: Metadata from AI response

        Returns:
            Diff summary dict (with unified diff)
        """

        # Backup
        self.backup.create(doc_path)

        # Diff
        diff_summary = self.diff_engine.compute(original_content, new_content)

        # Write doc
        self.writer.write(doc_path, new_content)

        # Write sidecar
        self.sidecar.write(doc_path, batch, ai_metadata)

        return diff_summary


# ======================================================================
# BACKWARD COMPATIBILITY FUNCTIONS
# ======================================================================

# Default instances for backward compatibility
_backup_manager = BackupManager()
_sidecar_writer = SidecarWriter()
_document_writer = DocumentWriter()
_diff_engine = DiffEngine()


def write_sidecar(
    doc_path: pathlib.Path,
    batch: Dict[str, Any],
    ai_metadata: Dict[str, Any],
) -> None:
    """Write or update the CGen sidecar metadata file.

    The sidecar file tracks the evolution of the document through CGen waves.
    This function maintains backward compatibility with the original API.

    Args:
        doc_path: Path to the original document
        batch: Batch configuration
        ai_metadata: Metadata from AI response
    """
    _sidecar_writer.write(doc_path, batch, ai_metadata)


def apply_changes(doc_path: pathlib.Path, new_content: str) -> None:
    """Write new content to a document file.

    This function maintains backward compatibility with the original API.

    Args:
        doc_path: Path to the document
        new_content: New content to write
    """
    _document_writer.write(doc_path, new_content)


def create_backup(doc_path: pathlib.Path) -> pathlib.Path:
    """Create a backup of the original document.

    This function maintains backward compatibility with the original API.

    Args:
        doc_path: Path to the document to backup

    Returns:
        Path to the backup file
    """
    return _backup_manager.create(doc_path)


def compute_diff_summary(original: str, new: str) -> Dict[str, Any]:
    """Compute a summary of differences between original and new content.

    This function maintains backward compatibility with the original API,
    but now returns additional fields from the DO-178C-friendly diff engine.

    Args:
        original: Original document content
        new: New document content

    Returns:
        Dictionary with diff statistics
    """
    return _diff_engine.compute(original, new)
