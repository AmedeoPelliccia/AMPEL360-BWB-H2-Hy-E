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
Wave Metadata & Logging Utilities — UTCS/GenCCC Tier-1 Compliant

This module provides:
- Deterministic JSONL logging for each CGen Wave ("E-EVENTLOG").
- Aggregation utilities for batch-wide wave summaries.
- A Markdown generator to produce human-readable reports.

All logs follow UTCS conventions:
- ISO8601 timestamps
- Structured, append-only evidence
- No required schema, but schema-compatible
"""

from __future__ import annotations

import json
import logging
import pathlib
from datetime import datetime, timezone
from typing import Any, Dict, List

logger = logging.getLogger(__name__)


# ======================================================================
# INTERNAL UTILITY
# ======================================================================

def _utc_now() -> str:
    """Return ISO 8601 UTC timestamp."""
    return datetime.now(timezone.utc).isoformat()


# ======================================================================
# WAVE LOGGING (JSONL)
# ======================================================================

def update_wave_log(
    log_dir: pathlib.Path,
    batch_id: str,
    doc_path: pathlib.Path,
    ai_response: Any,
    result: Dict[str, Any],
) -> None:
    """
    Append a UTCS-style log entry (JSONL) representing the processing
    of a single document within a CGen Wave.

    Args:
        log_dir: Directory for log files
        batch_id: Batch identifier (string)
        doc_path: Path to document being processed
        ai_response: AIResponse object
        result: Processing result dict from CGenWriter.apply_updates()
    """
    log_dir.mkdir(parents=True, exist_ok=True)
    log_file = log_dir / f"{batch_id}.jsonl"

    entry = {
        "timestamp": _utc_now(),
        "batch_id": batch_id,
        "document": str(result.get("doc_path", doc_path)),
        "model": result.get("model", getattr(ai_response, "model", "unknown")),
        "tokens_used": result.get("tokens_used", getattr(ai_response, "tokens_used", 0)),
        "changed": bool(result.get("changed", False)),
        "summary": result.get("summary", getattr(ai_response, "summary", "")),
        "output_path": result.get("output_path"),
    }

    try:
        with open(log_file, "a", encoding="utf-8") as f:
            f.write(json.dumps(entry, ensure_ascii=False) + "\n")
        logger.debug("Wave log entry appended: %s", log_file)
    except Exception as e:
        logger.error("Failed to write wave log %s: %s", log_file, e)


# ======================================================================
# READ WAVE LOG (JSONL)
# ======================================================================

def read_wave_log(log_dir: pathlib.Path, batch_id: str) -> List[Dict[str, Any]]:
    """
    Read and parse all line-delimited log entries for a wave.

    Returns empty list if file doesn't exist.
    """
    log_file = log_dir / f"{batch_id}.jsonl"

    if not log_file.exists():
        return []

    entries: List[Dict[str, Any]] = []
    try:
        with open(log_file, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                try:
                    entries.append(json.loads(line))
                except json.JSONDecodeError:
                    logger.warning("Malformed JSON in log file: %s", line)
    except Exception as e:
        logger.error("Failed to read wave log %s: %s", log_file, e)

    return entries


# ======================================================================
# WAVE SUMMARY
# ======================================================================

def get_wave_summary(log_dir: pathlib.Path, batch_id: str) -> Dict[str, Any]:
    """
    Compute a summary of the entries in the wave log.

    Returns:
        {
          "batch_id": ...,
          "total_documents": ...,
          "documents_changed": ...,
          "documents_unchanged": ...,
          "total_tokens_used": ...,
          "models_used": [...],
          "first_processed": ...,
          "last_processed": ...
        }
    """
    entries = read_wave_log(log_dir, batch_id)

    if not entries:
        return {
            "batch_id": batch_id,
            "total_documents": 0,
            "documents_changed": 0,
            "documents_unchanged": 0,
            "total_tokens_used": 0,
            "models_used": [],
            "first_processed": None,
            "last_processed": None,
        }

    total_docs = len(entries)
    changed_docs = sum(1 for e in entries if e.get("changed"))
    total_tokens = sum(e.get("tokens_used", 0) for e in entries)

    # unique models
    models = sorted({e.get("model", "unknown") for e in entries})

    # timestamps
    timestamps = [e.get("timestamp") for e in entries if e.get("timestamp")]
    first_ts = min(timestamps) if timestamps else None
    last_ts = max(timestamps) if timestamps else None

    return {
        "batch_id": batch_id,
        "total_documents": total_docs,
        "documents_changed": changed_docs,
        "documents_unchanged": total_docs - changed_docs,
        "total_tokens_used": total_tokens,
        "models_used": models,
        "first_processed": first_ts,
        "last_processed": last_ts,
    }


# ======================================================================
# MARKDOWN REPORT GENERATOR
# ======================================================================

def generate_wave_report(log_dir: pathlib.Path, batch_id: str) -> str:
    """
    Generate a human-readable Markdown report summarising the Wave.
    """
    summary = get_wave_summary(log_dir, batch_id)
    entries = read_wave_log(log_dir, batch_id)

    lines = [
        f"# CGen Docs Wave Report — {batch_id}",
        "",
        "## Summary",
        "",
        f"- **Total Documents Processed**: {summary['total_documents']}",
        f"- **Documents Changed**: {summary['documents_changed']}",
        f"- **Documents Unchanged**: {summary['documents_unchanged']}",
        f"- **Total Tokens Used**: {summary['total_tokens_used']:,}",
        f"- **Models Used**: {', '.join(summary['models_used']) or 'N/A'}",
        "",
        "## Processing Timeline",
        "",
        f"- **First Processed**: {summary['first_processed'] or 'N/A'}",
        f"- **Last Processed**: {summary['last_processed'] or 'N/A'}",
        "",
        "## Document Details",
        "",
        "| Document | Changed | Tokens | Summary |",
        "|----------|---------|--------|---------|",
    ]

    for entry in entries:
        doc = entry.get("document", "unknown")
        changed = "Yes" if entry.get("changed") else "No"
        tokens = entry.get("tokens_used", 0)

        short_summary = entry.get("summary", "")
        if len(short_summary) > 50:
            short_summary = short_summary[:50] + "…"

        lines.append(f"| {doc} | {changed} | {tokens} | {short_summary} |")

    lines += [
        "",
        "---",
        "",
        f"*Report generated at {datetime.now(timezone.utc).isoformat()}*",
    ]

    return "\n".join(lines)

