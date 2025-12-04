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
AI integration utilities for CGen Docs Waves.

This module provides the interface to AI models for document processing.
It handles API calls, retries, and response parsing.
"""

import logging
import os
import time
from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Any, Dict, List, Optional

logger = logging.getLogger(__name__)

# Environment variables for API configuration
OPENAI_API_KEY_VAR = "OPENAI_API_KEY"
GITHUB_COPILOT_API_VAR = "GITHUB_TOKEN"


@dataclass
class AIResponse:
    """Container for AI model response data."""

    content: str
    summary: str = ""
    model: str = ""
    tokens_used: int = 0
    finish_reason: str = ""
    metadata: Dict[str, Any] = field(default_factory=dict)


def get_api_client():
    """Get the appropriate API client based on environment.

    Returns:
        API client instance or None if no credentials available
    """
    # Check for OpenAI API key
    openai_key = os.environ.get(OPENAI_API_KEY_VAR)
    if openai_key:
        try:
            import openai

            return openai.OpenAI(api_key=openai_key)
        except ImportError:
            logger.warning("OpenAI package not installed")

    return None


def run_deepen_evolve_prompt(
    prompt: str,
    ai_policy: Dict[str, Any],
    dry_run: bool = False,
    max_retries: int = 3,
) -> Optional[AIResponse]:
    """Execute the deepen and evolve prompt against an AI model.

    Args:
        prompt: The complete prompt to send to the model
        ai_policy: AI policy configuration from batch
        dry_run: If True, return mock response without calling API
        max_retries: Maximum number of retry attempts

    Returns:
        AIResponse with model output, or None on failure
    """
    if dry_run:
        return _mock_response(prompt, ai_policy)

    client = get_api_client()
    if client is None:
        logger.warning("No API client available, using mock response")
        return _mock_response(prompt, ai_policy)

    model = ai_policy.get("model", "gpt-4o")
    fallback_model = ai_policy.get("fallback_model", "gpt-4o-mini")
    max_tokens = ai_policy.get("max_output_tokens", 8000)
    temperature = ai_policy.get("temperature", 0.2)

    for attempt in range(max_retries):
        try:
            current_model = model if attempt == 0 else fallback_model

            logger.info("Calling AI model: %s (attempt %d)", current_model, attempt + 1)

            response = client.chat.completions.create(
                model=current_model,
                messages=[
                    {
                        "role": "system",
                        "content": (
                            "You are the CGen Docs Wave assistant for AMPEL360 BWB H2 Hy-E Q100. "
                            "Your role is to improve documentation while maintaining structure "
                            "and certification-friendly wording."
                        ),
                    },
                    {"role": "user", "content": prompt},
                ],
                max_tokens=max_tokens,
                temperature=temperature,
            )

            choice = response.choices[0]
            content = choice.message.content or ""

            # Extract summary from content if present
            summary = _extract_summary(content)

            return AIResponse(
                content=content,
                summary=summary,
                model=current_model,
                tokens_used=response.usage.total_tokens if response.usage else 0,
                finish_reason=choice.finish_reason or "",
                metadata={
                    "prompt_tokens": (
                        response.usage.prompt_tokens if response.usage else 0
                    ),
                    "completion_tokens": (
                        response.usage.completion_tokens if response.usage else 0
                    ),
                    "timestamp": datetime.now(timezone.utc).isoformat(),
                },
            )

        except Exception as e:
            logger.warning("API call failed (attempt %d): %s", attempt + 1, e)
            if attempt < max_retries - 1:
                wait_time = (attempt + 1) * 2
                logger.info("Retrying in %d seconds...", wait_time)
                time.sleep(wait_time)
            else:
                logger.error("All API attempts failed")
                return None

    return None


def _extract_summary(content: str) -> str:
    """Extract the CGen Wave Summary from content.

    Args:
        content: Full AI response content

    Returns:
        Summary text or empty string
    """
    start_marker = "<!-- CGen Wave Summary -->"
    end_marker = "<!-- /CGen Wave Summary -->"

    # Also try alternate markers
    if start_marker not in content:
        start_marker = "<!-- CGen Wave Summary"
        end_marker = "-->"

    try:
        if start_marker in content:
            start_idx = content.index(start_marker) + len(start_marker)
            if end_marker in content[start_idx:]:
                end_idx = content.index(end_marker, start_idx)
                return content[start_idx:end_idx].strip()
    except ValueError:
        pass

    return ""


def _mock_response(prompt: str, ai_policy: Dict[str, Any]) -> AIResponse:
    """Generate a mock response for dry-run mode.

    Args:
        prompt: The prompt that would be sent
        ai_policy: AI policy configuration

    Returns:
        Mock AIResponse
    """
    logger.info("[MOCK] Would call model: %s", ai_policy.get("model", "gpt-4o"))
    logger.debug("[MOCK] Prompt length: %d chars", len(prompt))

    return AIResponse(
        content="[DRY-RUN: No changes made]",
        summary="Dry-run mode - no AI processing performed",
        model=ai_policy.get("model", "gpt-4o") + " (mock)",
        tokens_used=0,
        finish_reason="mock",
        metadata={
            "dry_run": True,
            "timestamp": datetime.now(timezone.utc).isoformat(),
        },
    )


def estimate_tokens(text: str) -> int:
    """Estimate the number of tokens in text.

    Args:
        text: Text to estimate tokens for

    Returns:
        Estimated token count (rough approximation)
    """
    # Rough estimate: 1 token ≈ 4 characters
    return len(text) // 4


def truncate_to_tokens(text: str, max_tokens: int) -> str:
    """Truncate text to approximately max_tokens.

    Args:
        text: Text to truncate
        max_tokens: Maximum tokens to allow

    Returns:
        Truncated text
    """
    max_chars = max_tokens * 4
    if len(text) <= max_chars:
        return text

    return text[:max_chars] + "\n\n[...content truncated due to token limit...]"
