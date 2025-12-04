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
Metadata and logging utilities for CGen Docs Waves.

This module handles wave logging and metadata tracking.
"""

import json
import logging
import pathlib
from datetime import datetime, timezone
from typing import Any, Dict

logger = logging.getLogger(__name__)


def update_wave_log(
    log_dir: pathlib.Path,
    batch_id: str,
    doc_path: pathlib.Path,
    ai_response: Any,
    result: Dict[str, Any],
) -> None:
    """Append an entry to the wave log (JSONL format).

    Args:
        log_dir: Directory for log files
        batch_id: Batch identifier
        doc_path: Path to the processed document
        ai_response: AI response object
        result: Processing result dictionary
    """
    log_dir.mkdir(parents=True, exist_ok=True)
    log_file = log_dir / f"{batch_id}.jsonl"

    log_entry = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "batch_id": batch_id,
        "document": result.get("doc_path", str(doc_path)),
        "model": result.get("model", getattr(ai_response, "model", "unknown")),
        "tokens_used": result.get("tokens_used", getattr(ai_response, "tokens_used", 0)),
        "changed": result.get("changed", False),
        "summary": result.get("summary", getattr(ai_response, "summary", "")),
        "output_path": result.get("output_path"),
    }

    try:
        with open(log_file, "a", encoding="utf-8") as f:
            f.write(json.dumps(log_entry, ensure_ascii=False) + "\n")
        logger.debug("Logged wave entry to: %s", log_file)
    except Exception as e:
        logger.error("Failed to write wave log: %s", e)


def read_wave_log(log_dir: pathlib.Path, batch_id: str) -> list:
    """Read all entries from a wave log.

    Args:
        log_dir: Directory containing log files
        batch_id: Batch identifier

    Returns:
        List of log entry dictionaries
    """
    log_file = log_dir / f"{batch_id}.jsonl"
    entries = []

    if not log_file.exists():
        return entries

    try:
        with open(log_file, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if line:
                    entries.append(json.loads(line))
    except Exception as e:
        logger.error("Failed to read wave log: %s", e)

    return entries


def get_wave_summary(log_dir: pathlib.Path, batch_id: str) -> Dict[str, Any]:
    """Generate a summary of wave processing.

    Args:
        log_dir: Directory containing log files
        batch_id: Batch identifier

    Returns:
        Summary dictionary with statistics
    """
    entries = read_wave_log(log_dir, batch_id)

    if not entries:
        return {"batch_id": batch_id, "total_documents": 0}

    total_docs = len(entries)
    changed_docs = sum(1 for e in entries if e.get("changed", False))
    total_tokens = sum(e.get("tokens_used", 0) for e in entries)

    # Get unique models used
    models = list(set(e.get("model", "unknown") for e in entries))

    # Get time range
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


def generate_wave_report(log_dir: pathlib.Path, batch_id: str) -> str:
    """Generate a markdown report for a wave.

    Args:
        log_dir: Directory containing log files
        batch_id: Batch identifier

    Returns:
        Markdown formatted report
    """
    summary = get_wave_summary(log_dir, batch_id)
    entries = read_wave_log(log_dir, batch_id)

    report_lines = [
        f"# CGen Docs Wave Report: {batch_id}",
        "",
        "## Summary",
        "",
        f"- **Total Documents Processed**: {summary['total_documents']}",
        f"- **Documents Changed**: {summary['documents_changed']}",
        f"- **Documents Unchanged**: {summary['documents_unchanged']}",
        f"- **Total Tokens Used**: {summary['total_tokens_used']:,}",
        f"- **Models Used**: {', '.join(summary['models_used'])}",
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
        summary_text = entry.get("summary", "")[:50]
        if len(entry.get("summary", "")) > 50:
            summary_text += "..."

        report_lines.append(f"| {doc} | {changed} | {tokens} | {summary_text} |")

    report_lines.extend(
        [
            "",
            "---",
            "",
            f"*Report generated: {datetime.now(timezone.utc).isoformat()}*",
        ]
    )

    return "\n".join(report_lines)
