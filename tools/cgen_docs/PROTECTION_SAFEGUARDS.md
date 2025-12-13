# CGen Workflow Protection Safeguards

## Overview

The CGen (Continuous Generation) workflows have been enhanced with comprehensive safeguards to prevent accidental deletion or replacement of validated, comprehensive documentation with AI-generated content.

## Problem

Previously, the CGen Docs Waves workflow (`cgen-docs-waves.yml`) would:
1. Process ALL Markdown files in the scope directories
2. Use AI to "deepen" documentation content
3. With `write_mode: "inplace"`, directly overwrite original files
4. Potentially replace comprehensive, validated documentation with inferior AI-generated content

This could result in loss of high-quality, human-reviewed documentation.

## Solution

Multiple layers of protection have been added:

### 1. Document Protection Logic

The `is_document_protected()` function in `tools/cgen_docs/run_batch.py` checks documents before processing:

#### Protection Criteria (in priority order):

1. **Status-Based Protection** (HIGHEST PRIORITY)
   - Documents with these statuses are ALWAYS protected:
     - `APPROVED`
     - `VALIDATED`
     - `RELEASED`
     - `FINAL`
     - `ACCEPTED`
   - Status is checked in the Document Control section
   - Even short documents with these statuses are protected

2. **Content-Based Protection**
   - Documents are protected if they are:
     - **Comprehensive**: >1500 characters
     - **Substantive**: >15 lines of actual content
     - **Complete**: <3 placeholders (`[To be completed]`, `[CGEN:...]`, etc.)

3. **Placeholder Ratio Check**
   - Documents with many placeholders relative to sections are NOT protected
   - If placeholders ≥ 30% of sections, document can be improved

### 2. Quality Checks During Processing

Even if a document passes protection checks and is processed:

- **Content Reduction Guard**: If AI output is >30% shorter than original, the workflow automatically switches to `draft_sidecar` mode
- This prevents massive content deletions
- Original file is preserved, draft is created for review

### 3. Safe Default Configuration

All batch configurations now use `draft_sidecar` mode by default:

```yaml
ai_policy:
  write_mode: "draft_sidecar"  # Changed from "inplace"
  draft_suffix: "_CGEN_DRAFT"
```

This means:
- Original files are NEVER overwritten
- AI output is saved to `*_CGEN_DRAFT.md` files
- Human review required before merging

### 4. Enhanced Logging

Processing now reports:
- Protected documents (with reason)
- Skipped documents
- Documents with quality issues
- Draft files created

Example output:
```
⚠️  SKIPPING protected document: 10-00-04_Design/10-00-04-001_Design_Philosophy.md
    Reason: document is comprehensive with minimal placeholders

Wave complete:
  Total documents: 45
  Protected/skipped: 12
  Processed: 33
  Changed: 8
```

## How to Use

### For Document Authors

To protect your comprehensive documentation:

1. **Add a status field** in Document Control section:
   ```markdown
   ## Document Control
   
   - Status: **APPROVED**
   - Version: 2.0
   ```

2. **Keep comprehensive content**: Documents with substantial content (>1500 chars, good structure) are automatically protected

3. **Minimize placeholders**: Use specific content instead of `[To be completed]`

### For CGen Workflow Users

When reviewing CGen PRs:

1. **Check for draft files**: Look for `*_CGEN_DRAFT.md` files
2. **Review AI changes**: Compare draft with original
3. **Approve good changes**: Rename draft to replace original if improvements are good
4. **Reject poor changes**: Delete draft if AI output is inferior

### Manual Override

If you need to force CGen to process a protected document:

1. **Temporary**: Remove the protected status temporarily
2. **Careful**: Review AI output before accepting
3. **Restore**: Add protected status back after review

## Testing

Protection logic has been tested with:
- Short documents (not protected)
- Documents with many placeholders (not protected)
- Comprehensive documents (protected)
- Documents with APPROVED status (protected)
- Real repository documents (working as expected)

## Files Modified

- `tools/cgen_docs/run_batch.py` - Protection logic
- `cd/cgen_docs/batches/BATCH_INFRA_A.yaml` - Safe defaults
- `cd/cgen_docs/batches/BATCH_ONBOARD_A.yaml` - Safe defaults
- `cd/cgen_docs/batches/BATCH_ONBOARD_B.yaml` - Safe defaults
- `.github/workflows/cgen-docs-waves.yml` - Documentation comments

## Benefits

✅ **Prevents data loss**: Validated docs cannot be overwritten  
✅ **Safe by default**: Draft mode preserves originals  
✅ **Quality control**: Content reduction triggers safety mode  
✅ **Clear visibility**: Protected documents are logged  
✅ **Human oversight**: Review required before accepting changes  

## Related Tools

The `fill_placeholders.py` tool is separate and only fills actual placeholders:
- Only processes lines matching `[To be completed]` or `[CGEN:...]`
- Does NOT overwrite comprehensive content
- Preserves existing text

## Document Control

- **Created**: 2025-12-13
- **Author**: GitHub Copilot (prompted by Amedeo Pelliccia)
- **Status**: ACTIVE
- **Repository**: AMPEL360-BWB-H2-Hy-E
- **Related Issue**: Fix CGen workflow deleting comprehensive documentation
