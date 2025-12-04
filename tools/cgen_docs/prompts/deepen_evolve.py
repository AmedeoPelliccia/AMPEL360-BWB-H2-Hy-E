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
Deepen & Evolve prompts for CGen Docs Waves.

This module contains the prompt templates and composition logic for
AI-assisted document improvement.
"""

import pathlib
from typing import Any, Dict, List

# Main Deepen & Evolve prompt template
DEEPEN_EVOLVE_TEMPLATE = """
You are the CGen Docs Wave assistant for AMPEL360 BWB H2 Hy-E Q100.

Repository context summary:
{global_context}

Document under improvement: {doc_path}
Current content:
<<<DOC_START
{document_text}
DOC_END>>>

Additional local context (indices, related docs):
{doc_context}

Objectives for this wave ({batch_id}):
{objectives}

Instructions:
1. Deepen sections that are high-level or contain TBD/TBR markers.
2. Add cross references to relevant ATA chapters, Line Cards (LC-XX), Neural Network nodes (NN-XX), or GenCCC artifacts.
3. Normalize Document Control tables (Owner, Version, Status, AI Assistance, etc.) if missing or inconsistent.
4. Clarify open points and outline next steps/actions.
5. Maintain tone and terminology consistent with AMPEL360 (BWB, H2, Q100, NN-ECS, etc.).
6. Keep Markdown structure, anchors, numbering.
7. Mark AI contributions with an embedded `ai_assist` block if new text exceeds 3 sentences.

Deliver:
1. Revised Markdown document ready for commit (full document, not diff).
2. Brief change summary (<80 words) at the end between `<!-- CGen Wave Summary -->` and `<!-- /CGen Wave Summary -->` markers.

Important rules:
- Ensure deterministic, certification-friendly wording.
- Do NOT invent data; state "Future work" or "TBD" when information is unavailable.
- Preserve existing Document Control sections; only add/update AI assistance line.
- Use hyperlinks to official sources for standards (EASA, FAA, RTCA, etc.) when referenced.
- Never fabricate regulatory references or document IDs.
"""

# Sidecar metadata prompt template
SIDECAR_TEMPLATE = """
Generate/update a YAML block capturing the latest CGen Docs Wave metadata for {doc_path}.

Existing metadata (if any):
<<<YAML
{existing_sidecar}
YAML_END>>>

Include:
- last_cgen_wave: "{batch_id}"
- last_cgen_at: ISO 8601 UTC timestamp (provided: {run_timestamp})
- ai_model: "{model_name}"
- scope: list of sections touched or created
- reviewer: set to "TBD"
- notes: bullet list (max 3) describing key improvements or pending actions.

Return ONLY valid YAML.
"""


def compose_prompt(
    batch: Dict[str, Any],
    doc_path: pathlib.Path,
    document_text: str,
    global_context: str,
    doc_context: str,
    repo_root: pathlib.Path,
) -> str:
    """Compose the complete prompt for document processing.

    Args:
        batch: Batch configuration dictionary
        doc_path: Path to the document being processed
        document_text: Current content of the document
        global_context: Pre-loaded global context string
        doc_context: Document-specific context string
        repo_root: Repository root path

    Returns:
        Complete prompt string ready for AI processing
    """
    # Format objectives from targets
    objectives = format_objectives(batch.get("targets", []))

    # Truncate document if too long
    max_doc_tokens = batch.get("ai_policy", {}).get("max_tokens_per_doc", 6000)
    max_doc_chars = max_doc_tokens * 4  # Rough estimate

    if len(document_text) > max_doc_chars:
        document_text = (
            document_text[:max_doc_chars]
            + "\n\n[...document truncated due to length...]\n"
        )

    # Truncate context if needed
    max_context_chars = 4000
    if len(global_context) > max_context_chars:
        global_context = (
            global_context[:max_context_chars]
            + "\n[...context truncated...]\n"
        )

    if len(doc_context) > max_context_chars:
        doc_context = (
            doc_context[:max_context_chars]
            + "\n[...local context truncated...]\n"
        )

    # Build the prompt
    rel_path = doc_path.relative_to(repo_root)

    prompt = DEEPEN_EVOLVE_TEMPLATE.format(
        global_context=global_context,
        doc_path=str(rel_path),
        document_text=document_text,
        doc_context=doc_context if doc_context else "(No additional local context available)",
        batch_id=batch.get("batch_id", "UNKNOWN"),
        objectives=objectives,
    )

    return prompt


def format_objectives(targets: List[Dict[str, Any]]) -> str:
    """Format batch targets into a bulleted objectives list.

    Args:
        targets: List of target dictionaries from batch config

    Returns:
        Formatted objectives string
    """
    if not targets:
        return "- Improve documentation quality and completeness"

    lines = []
    for target in sorted(targets, key=lambda t: t.get("priority", 99)):
        target_type = target.get("type", "unknown")
        description = target.get("description", "")

        # Format type for display
        display_type = target_type.replace("_", " ").title()

        if description:
            lines.append(f"- **{display_type}**: {description}")
        else:
            lines.append(f"- {display_type}")

    return "\n".join(lines)


def compose_sidecar_prompt(
    doc_path: pathlib.Path,
    batch_id: str,
    model_name: str,
    run_timestamp: str,
    existing_sidecar: str = "",
) -> str:
    """Compose prompt for sidecar metadata generation.

    Args:
        doc_path: Path to the document
        batch_id: Batch identifier
        model_name: AI model name
        run_timestamp: ISO 8601 timestamp
        existing_sidecar: Existing sidecar content if any

    Returns:
        Prompt for sidecar generation
    """
    return SIDECAR_TEMPLATE.format(
        doc_path=str(doc_path),
        existing_sidecar=existing_sidecar or "(No existing metadata)",
        batch_id=batch_id,
        run_timestamp=run_timestamp,
        model_name=model_name,
    )
