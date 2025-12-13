# CGen Placeholder Issue Analysis and Resolution

## Issue Summary

CGen (Continuous Generation) was replacing detailed document content with placeholders instead of evolving the documentation. Files were being created or updated with only the text `[DRY-RUN: No changes made]` instead of containing meaningful documentation.

## Root Cause Analysis

### The Problem Chain

1. **CGen Batch Processing Flow**:
   - CGen processes documentation in batches using `tools/cgen_docs/run_batch.py`
   - Each document is sent to an AI model for improvement via `run_deepen_evolve_prompt()`
   - When AI is unavailable or in dry-run mode, a mock response is returned

2. **Mock Response Behavior (Original)**:
   - Located in `tools/cgen_docs/utils/ai.py`
   - The `_mock_response()` function returned a hardcoded placeholder:
     ```python
     return AIResponse(
         content="[DRY-RUN: No changes made]",
         ...
     )
     ```

3. **Content Replacement**:
   - In `run_batch.py`, the mock response content was used as `new_text`
   - This replaced the original document content entirely
   - Files ended up containing only `[DRY-RUN: No changes made]`

4. **Placeholder Filling Mismatch**:
   - `tools/genccc/fill_placeholders.py` was designed to fill placeholders
   - It only recognized patterns: `[To be completed]` and `[CGEN:...]`
   - It did NOT recognize `[DRY-RUN: No changes made]`
   - Even if it did, these files had no document structure (no sections, headings)

### Why This Happened

The BATCH_INFRA_A wave ran when:
- The OpenAI API was unavailable or credentials were not set
- CGen fell back to mock mode
- Instead of preserving original content, it replaced everything with the placeholder
- The `.cgen.yaml` sidecar files show `tokens_used: 0`, confirming no actual AI processing occurred

## The Fix

### 1. Preserve Original Content in Mock Mode

**File**: `tools/cgen_docs/utils/ai.py`

**Changes**:
```python
def run_deepen_evolve_prompt(
    prompt: str,
    ai_policy: Dict[str, Any],
    dry_run: bool = False,
    max_retries: int = 3,
    original_content: Optional[str] = None,  # NEW PARAMETER
) -> Optional[AIResponse]:
    # ...
    if dry_run:
        return _mock_response(prompt, ai_policy, original_content)
    
    client = get_api_client()
    if client is None:
        return _mock_response(prompt, ai_policy, original_content)
```

```python
def _mock_response(
    prompt: str, 
    ai_policy: Dict[str, Any], 
    original_content: Optional[str] = None  # NEW PARAMETER
) -> AIResponse:
    """Return a deterministic mock response for dry-run and fallback modes."""
    
    # If we have original content, preserve it instead of using a placeholder
    if original_content:
        content = original_content
        summary = "Dry-run/fallback mode: original content preserved without AI processing."
    else:
        content = "[DRY-RUN: No changes made]"
        summary = "Dry-run mode: no AI processing performed."
    
    return AIResponse(
        content=content,
        summary=summary,
        # ...
    )
```

### 2. Pass Original Content to AI Processing

**File**: `tools/cgen_docs/run_batch.py`

**Changes**:
```python
# Run AI processing
ai_response = run_deepen_evolve_prompt(
    prompt, 
    batch["ai_policy"], 
    dry_run=dry_run,
    original_content=original_text  # NEW: Pass original content
)
```

### 3. Recognize DRY-RUN Placeholders (Defense in Depth)

**File**: `tools/genccc/fill_placeholders.py`

**Changes**:
```python
# Placeholder patterns
PLACEHOLDER_PATTERNS = [
    re.compile(r"^\[To be completed\]\s*$"),
    re.compile(r"^\[CGEN:.*\]\s*$"),
    re.compile(r"^\[DRY-RUN:.*\]\s*$"),  # NEW: CGen dry-run placeholders
]
```

This ensures that if any files do end up with DRY-RUN placeholders, they can be detected and filled later.

## Impact and Benefits

### Before the Fix

❌ **Problem**:
- Documents were overwritten with placeholder text
- Original content was lost
- Documentation didn't evolve
- Manual recreation of content was required

### After the Fix

✅ **Solution**:
- Original content is preserved when AI is unavailable
- CGen can run safely in fallback mode
- Documents maintain their structure and content
- When AI becomes available, content can be properly improved

## Testing Recommendations

1. **Test Mock Mode**:
   ```bash
   # Without OPENAI_API_KEY set
   unset OPENAI_API_KEY
   python tools/cgen_docs/run_batch.py --batch-id BATCH_INFRA_A --verbose
   # Verify: Original content should be preserved
   ```

2. **Test Dry-Run Mode**:
   ```bash
   python tools/cgen_docs/run_batch.py --batch-id BATCH_INFRA_A --dry-run
   # Verify: No files should be modified
   ```

3. **Test Placeholder Recognition**:
   ```bash
   # Create a test file with [DRY-RUN: No changes made]
   # Run fill_placeholders.py
   python tools/genccc/fill_placeholders.py --target path/to/test --dry-run
   # Verify: Placeholder is detected
   ```

## Prevention Measures

### For Future Development

1. **Always test fallback paths**: Ensure mock/fallback modes preserve data integrity
2. **Validate before writing**: Check that new content is not just a placeholder
3. **Add content preservation guards**: Detect when content would be replaced with minimal placeholder text
4. **Document all placeholder patterns**: Keep a central registry of recognized patterns

### Configuration Recommendations

1. **Ensure API keys are set** in CI/CD:
   ```yaml
   env:
     OPENAI_API_KEY: ${{ secrets.OPENAI_API_KEY }}
   ```

2. **Add health checks** before CGen runs:
   ```bash
   if [ -z "$OPENAI_API_KEY" ]; then
     echo "Warning: OPENAI_API_KEY not set - CGen will preserve content only"
   fi
   ```

3. **Monitor token usage**: Files with `tokens_used: 0` in `.cgen.yaml` indicate mock mode was used

## Related Files

- `tools/cgen_docs/utils/ai.py` - AI integration and mock response logic
- `tools/cgen_docs/run_batch.py` - Main batch processing orchestrator
- `tools/genccc/fill_placeholders.py` - Placeholder detection and filling
- `tools/genccc/PLACEHOLDER_FILLING_GUIDE.md` - Documentation for placeholder patterns
- `.github/workflows/cgen-docs-waves.yml` - CGen workflow automation

## Lessons Learned

1. **Fallback modes must preserve data**: Never replace content with less information in fallback scenarios
2. **Pattern recognition must be complete**: All generated patterns must be recognized by downstream tools
3. **Test without API access**: Simulate unavailable external services in testing
4. **Document contract between components**: CGen writes patterns that fill_placeholders reads

---

**Document Control**

- Created: 2025-12-13
- Author: GitHub Copilot (prompted by Amedeo Pelliccia)
- Status: Analysis Complete
- Related Issue: #424 Review Comment 3574318693
- Resolution: Commit 5a82d6de
