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
AI integration utilities for CGen Docs Waves.

This module provides the interface to AI models for document processing,
including request construction, retries, safety controls, and response parsing.

Governance principles:
- CGen proposes, humans dispose.
- All AI outputs must undergo human review before merge.
- No AI call may modify document identity (IDs, ATA numbers, file paths).
"""

from __future__ import annotations

import logging
import os
import time
from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Any, Dict, Optional

logger = logging.getLogger(__name__)

# Environment variables for API configuration
OPENAI_API_KEY_VAR = "OPENAI_API_KEY"
GITHUB_COPILOT_API_VAR = "GITHUB_TOKEN"


# ---------------------------------------------------------------------------
# Response container
# ---------------------------------------------------------------------------

@dataclass
class AIResponse:
    """Structured container for AI model response data."""

    content: str
    summary: str = ""
    model: str = ""
    tokens_used: int = 0
    finish_reason: str = ""
    metadata: Dict[str, Any] = field(default_factory=dict)


# ---------------------------------------------------------------------------
# API Client Resolution
# ---------------------------------------------------------------------------

def get_api_client():
    """
    Return an OpenAI API client if available.

    The lookup is deliberately simple to allow mocking or future extensions.
    """
    openai_key = os.environ.get(OPENAI_API_KEY_VAR)
    if not openai_key:
        logger.warning("AI integration disabled (missing %s)", OPENAI_API_KEY_VAR)
        return None

    try:
        import openai
        return openai.OpenAI(api_key=openai_key)
    except ImportError:
        logger.warning("OpenAI Python package not installed.")
        return None


# ---------------------------------------------------------------------------
# Core execution entry point
# ---------------------------------------------------------------------------

def run_deepen_evolve_prompt(
    prompt: str,
    ai_policy: Dict[str, Any],
    dry_run: bool = False,
    max_retries: int = 3,
    original_content: Optional[str] = None,
) -> Optional[AIResponse]:
    """
    Execute the deepen/evolve prompt against an AI model with retry handling.

    Args:
        prompt: The prompt to send to the AI model.
        ai_policy: The AI policy controlling model selection and limits.
        dry_run: If True, bypasses the actual API and returns a mock response.
        max_retries: Maximum number of retry attempts.
        original_content: Original document content to preserve when AI is unavailable
            or in dry-run mode. If provided, this content will be returned unchanged
            instead of a placeholder, maintaining document integrity.

    Returns:
        AIResponse or None if all attempts fail.
    """

    if dry_run:
        return _mock_response(prompt, ai_policy, original_content)

    client = get_api_client()
    if client is None:
        logger.warning("No API client available; falling back to mock response.")
        return _mock_response(prompt, ai_policy, original_content)

    model = ai_policy.get("model", "gpt-4o")
    fallback_model = ai_policy.get("fallback_model", "gpt-4o-mini")
    max_tokens = ai_policy.get("max_output_tokens", 8000)
    temperature = ai_policy.get("temperature", 0.15)

    for attempt in range(max_retries):
        current_model = model if attempt == 0 else fallback_model

        try:
            logger.info("Calling AI model: %s (attempt %d)", current_model, attempt + 1)

            response = client.chat.completions.create(
                model=current_model,
                messages=[
                    {
                        "role": "system",
                        "content": (
                            "You are the CGen Docs Wave assistant for AMPEL360. "
                            "Improve documentation only, maintaining structure, "
                            "conservatism, and certification-aligned language. "
                            "Do NOT create or modify document IDs or ATA numbering."
                        ),
                    },
                    {"role": "user", "content": prompt},
                ],
                max_tokens=max_tokens,
                temperature=temperature,
            )

            choice = response.choices[0]
            content = choice.message.content or ""
            summary = _extract_summary(content)

            return AIResponse(
                content=content,
                summary=summary,
                model=current_model,
                tokens_used=response.usage.total_tokens if response.usage else 0,
                finish_reason=choice.finish_reason or "",
                metadata={
                    "prompt_tokens": response.usage.prompt_tokens if response.usage else 0,
                    "completion_tokens": response.usage.completion_tokens if response.usage else 0,
                    "timestamp": datetime.now(timezone.utc).isoformat(),
                    "model": current_model,
                },
            )

        except Exception as e:
            logger.warning(
                "AI model call failed for model %s (attempt %d/%d): %s",
                current_model, attempt + 1, max_retries, e,
            )

            if attempt < max_retries - 1:
                backoff = (attempt + 1) * 2
                logger.info("Retrying in %d seconds...", backoff)
                time.sleep(backoff)
            else:
                logger.error("All retry attempts exhausted.")
                return None

    return None


# ---------------------------------------------------------------------------
# Summary extraction
# ---------------------------------------------------------------------------

def _extract_summary(content: str) -> str:
    """
    Extract the CGen Wave Summary section from an AI-generated document.
    Returns the summary text or "".
    """
    markers = [
        ("<!-- CGen Wave Summary -->", "<!-- /CGen Wave Summary -->"),
        ("<!-- CGen Wave Summary", "-->"),
    ]

    for start_marker, end_marker in markers:
        try:
            if start_marker in content:
                start_idx = content.index(start_marker) + len(start_marker)
                end_idx = content.index(end_marker, start_idx)
                return content[start_idx:end_idx].strip()
        except ValueError:
            continue

    return ""


# ---------------------------------------------------------------------------
# Mock Responses
# ---------------------------------------------------------------------------

def _mock_response(prompt: str, ai_policy: Dict[str, Any], original_content: Optional[str] = None) -> AIResponse:
    """Return a deterministic mock response for dry-run and fallback modes."""
    logger.info("[MOCK] Returning simulated AI response.")
    logger.debug("[MOCK] Prompt length: %d chars", len(prompt))

    # Check if original content has non-whitespace characters; if so, preserve the original
    # (including any leading/trailing whitespace) instead of using a placeholder
    stripped_content = original_content.strip() if original_content else ""
    if stripped_content:
        content = original_content
        summary = "Dry-run/fallback mode: original content preserved without AI processing."
    else:
        content = "[DRY-RUN: No changes made]"
        summary = "Dry-run mode: no AI processing performed."

    return AIResponse(
        content=content,
        summary=summary,
        model=(ai_policy.get("model") or "mock-model") + " (mock)",
        tokens_used=0,
        finish_reason="mock",
        metadata={
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "dry_run": True,
        },
    )


# ---------------------------------------------------------------------------
# Token Estimation Utilities
# ---------------------------------------------------------------------------

def estimate_tokens(text: str) -> int:
    """Estimate token count using a simple 4 chars/token heuristic."""
    return len(text) // 4


def truncate_to_tokens(text: str, max_tokens: int) -> str:
    """
    Truncate text to approx. max_tokens using the 4 chars/token heuristic.
    """
    max_chars = max_tokens * 4
    if len(text) <= max_chars:
        return text

    return text[:max_chars] + "\n\n[...content truncated due to token limit...]\n"

