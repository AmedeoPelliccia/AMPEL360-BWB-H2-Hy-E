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
Deepen & Evolve prompts for CGen Docs Waves.

This module contains the prompt templates and composition logic for
AI-assisted document improvement within the AMPEL360 CGen Docs pipeline.

Key ideas:
- CGen proposes, humans dispose: all outputs are *proposals* pending review.
- The AI must NOT change document identity (IDs, ATA numbering, file paths).
- The AI must NOT fabricate certification / regulatory claims.
"""

from __future__ import annotations

import pathlib
from typing import Any, Dict, List

# Main Deepen & Evolve prompt template
DEEPEN_EVOLVE_TEMPLATE = """
You are the CGen Docs Wave assistant for the AMPEL360 BWB H2 Hy-E Q100 programme.

PROJECT CONTEXT
---------------
- Documentation framework: OPT-IN (O-Organization, P-Program, T-Technology,
  I-Infrastructures, N-Neural_Networks_Users_Traceability).
- Numbering: ATA-based structure (ATA_XX-YY-ZZ) with LC pages and GenCCC
  governance for DO-178C / ARINC 653 / CAST-32A / IMA.
- Key principle: "CGen proposes, humans dispose" — all outputs are proposals
  that require human review and approval before merge.

GLOBAL REPOSITORY CONTEXT
-------------------------
{global_context}

DOCUMENT UNDER IMPROVEMENT
--------------------------
Path (relative to repo root): {doc_path}

Current content:
<<<DOC_START
{document_text}
DOC_END>>>

Additional local context (indices, related docs, LC/ATA cross-links):
{doc_context}

OBJECTIVES FOR THIS WAVE ({batch_id})
-------------------------------------
{objectives}

NON-NEGOTIABLE RULES
--------------------
1. Do NOT change:
   - Document IDs (Document ID, revision codes, prefixes/suffixes).
   - ATA numbering, section numbers, or file paths.
   - Existing cross-reference anchors, except to fix obvious typos.
2. Do NOT:
   - Claim certification / approval / acceptance by any authority (EASA, FAA,
     OEM, etc.) beyond what is already present verbatim in the document.
   - Invent performance numbers, safety margins, or legal commitments.
   - Fabricate regulatory references, standards, or document identifiers.
3. You MAY:
   - Improve structure, headings, and section ordering.
   - Clarify ambiguous sentences while preserving technical meaning.
   - Deepen high-level sections with more precise, certification-friendly text.
   - Add non-binding "Future work" or "TBD" notes when gaps are detected.
   - Add internal cross-references between existing documents (ATA, LC, NN,
     GenCCC artefacts) when they are already referenced or clearly implied.

CONCRETE TASKS
--------------
1. Deepen sections that are high-level or contain TBD/TBR markers, proposing
   realistic but non-binding technical content (e.g. rationale, options,
   interfaces) without inventing factual data.
2. Add cross references to relevant ATA chapters, Line Cards (LC-XX),
   Neural Network nodes (NN-XX), or GenCCC artefacts *when already present
   in the local/global context*.
3. Normalize Document Control tables (Owner, Version, Status, AI Assistance,
   etc.) if missing or inconsistent. Do not change the Document ID or path.
4. Clarify open points and outline next steps / actions in a short
   "TODO / Open Points" section where appropriate.
5. Maintain tone and terminology consistent with AMPEL360
   (BWB, H2, Q100, NN-ECS, GenCCC, CGen, etc.).
6. Keep Markdown structure, anchors, and numbering consistent and stable.
7. Mark substantial AI contributions with an embedded `ai_assist` block in
   the Document Control section if new text exceeds 3 sentences in a given
   section.

OUTPUT FORMAT
-------------
Deliver:
1. The **full revised Markdown document**, ready for commit (not a diff).
   - Preserve any YAML-like front-matter / document-control blocks at the top.
   - You may only *update* fields such as description, status text, or
     AI-assistance details, never the identifiers.
   - Do NOT wrap the whole answer in Markdown code fences (```).
2. A brief change summary (<80 words) at the end of the document, placed
   between the markers:

   <!-- CGen Wave Summary -->
   (summary text here)
   <!-- /CGen Wave Summary -->

IMPORTANT RULES
---------------
- Ensure precise, deterministic, certification-friendly wording.
- If required information is unknown or not given, clearly state
  "Future work" or "TBD" instead of inventing details.
- Preserve existing Document Control sections; only add/update the AI
  assistance line as needed.
- When referencing standards (EASA, FAA, RTCA, EUROCAE, etc.), use generic
  wording unless a specific reference is already present; never fabricate
  standard IDs or issue numbers.
"""

# Sidecar metadata prompt template
SIDECAR_TEMPLATE = """
Generate or update a YAML block capturing the latest CGen Docs Wave metadata
for the document at path: {doc_path}.

Existing metadata (if any):
<<<YAML
{existing_sidecar}
YAML_END>>>

Requirements:
- Produce ONLY valid YAML (no comments, no surrounding fences).
- Overwrite or create fields as needed.

Include at least:
- last_cgen_wave: "{batch_id}"
- last_cgen_at: ISO 8601 UTC timestamp (provided: {run_timestamp})
- ai_model: "{model_name}"
- scope: list of sections touched or created (short, human-readable labels)
- reviewer: set to "TBD"
- notes: bullet list (max 3) describing key improvements or pending actions.

The YAML should be suitable for storing in a sidecar file committed to the repo.
"""


def _truncate(text: str, max_chars: int, suffix: str) -> str:
    """Truncate a string to max_chars, appending suffix if truncated."""
    if len(text) <= max_chars:
        return text
    return text[:max_chars] + suffix


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
        batch: Batch configuration dictionary.
        doc_path: Path to the document being processed.
        document_text: Current content of the document.
        global_context: Pre-loaded global context string for the batch.
        doc_context: Document-specific context string (indices, neighbours).
        repo_root: Repository root path.

    Returns:
        Complete prompt string ready for AI processing.
    """
    # Format objectives from targets
    objectives = format_objectives(batch.get("targets", []))

    # Rough character limit derived from max_tokens_per_doc policy.
    max_doc_tokens = batch.get("ai_policy", {}).get("max_tokens_per_doc", 6000)
    max_doc_chars = max_doc_tokens * 4  # Rough token→char estimate

    document_text = _truncate(
        document_text,
        max_doc_chars,
        "\n\n[...document truncated due to length...]\n",
    )

    # Truncate contexts to avoid runaway prompts
    max_context_chars = batch.get("ai_policy", {}).get(
        "max_context_chars", 4000
    )

    global_context = _truncate(
        global_context,
        max_context_chars,
        "\n[...global context truncated...]\n",
    )

    doc_context = _truncate(
        doc_context,
        max_context_chars,
        "\n[...local context truncated...]\n",
    ) or "(No additional local context available)"

    # Build the prompt
    rel_path = doc_path.relative_to(repo_root)

    prompt = DEEPEN_EVOLVE_TEMPLATE.format(
        global_context=global_context,
        doc_path=str(rel_path),
        document_text=document_text,
        doc_context=doc_context,
        batch_id=batch.get("batch_id", "UNKNOWN"),
        objectives=objectives,
    )

    return prompt


def format_objectives(targets: List[Dict[str, Any]]) -> str:
    """Format batch targets into a bulleted objectives list.

    Args:
        targets: List of target dictionaries from batch config.

    Returns:
        Formatted objectives string.
    """
    if not targets:
        return "- Improve documentation quality, depth, and internal consistency."

    lines: List[str] = []
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
        doc_path: Path to the document.
        batch_id: Batch identifier.
        model_name: AI model name.
        run_timestamp: ISO 8601 timestamp.
        existing_sidecar: Existing sidecar content, if any.

    Returns:
        Prompt string for sidecar generation.
    """
    return SIDECAR_TEMPLATE.format(
        doc_path=str(doc_path),
        existing_sidecar=existing_sidecar or "(No existing metadata)",
        batch_id=batch_id,
        run_timestamp=run_timestamp,
        model_name=model_name,
    )

