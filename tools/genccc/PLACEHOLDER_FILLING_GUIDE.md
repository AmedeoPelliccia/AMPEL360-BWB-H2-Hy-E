# CGen Placeholder Filling Guide

## Overview

The CGen Placeholder Filling feature automatically completes documentation sections marked with placeholders using AI-assisted content generation. This ensures that documentation evolves systematically while maintaining consistency and quality.

## Supported Placeholder Patterns

The tool recognizes two types of placeholders:

### 1. Legacy Pattern
```markdown
## 2. Scope

[To be completed]
```

### 2. New Convention (Recommended)
```markdown
## 3. Overview

[CGEN:TODO]
```

Or with specific hints:
```markdown
## 4. Requirements

[CGEN:Requirements]
```

Both patterns will be detected and filled automatically.

## How It Works

1. **Scans documentation files** in specified directories for placeholders
2. **Extracts document context**:
   - Document ID (e.g., `10-00-02-005-A`)
   - Document title (e.g., `LH₂ Properties and Hazards`)
   - Section number and title (e.g., `2. Scope`)
   - Surrounding content for context
3. **Generates content** using OpenAI with aerospace/safety-appropriate prompts
4. **Replaces placeholder** with generated content
5. **Preserves formatting** and document structure

## Usage

### Command Line

#### Basic Usage (Process ATA_03 by default)
```bash
python tools/genccc/fill_placeholders.py
```

#### Process Specific Directory
```bash
# Process ATA_10 documents
python tools/genccc/fill_placeholders.py \
  --target OPT-IN_FRAMEWORK/I-INFRASTRUCTURES/ATA_10-PARKING_MOORING_STORAGE_RTS

# Process ATA_03 documents (GSE)
python tools/genccc/fill_placeholders.py \
  --target OPT-IN_FRAMEWORK/I-INFRASTRUCTURES/ATA_03-SUPPORT_INFORMATION_GSE
```

#### Dry Run Mode (Preview Only)
```bash
python tools/genccc/fill_placeholders.py --dry-run --verbose
```

This will show what would be filled without making any changes.

#### Verbose Logging
```bash
python tools/genccc/fill_placeholders.py --verbose
```

### Environment Setup

The script requires the OpenAI API key to be set:

```bash
export OPENAI_API_KEY="your-api-key-here"
python tools/genccc/fill_placeholders.py
```

For CI/CD, ensure `OPENAI_API_KEY` is set in GitHub secrets.

## Integration with CGen Workflow

The placeholder filling is automatically integrated into the CGen Docs Waves workflow:

```yaml
- name: Fill CGen placeholders in documentation
  env:
    OPENAI_API_KEY: ${{ secrets.OPENAI_API_KEY }}
  run: |
    python tools/genccc/fill_placeholders.py \
      --target OPT-IN_FRAMEWORK/I-INFRASTRUCTURES/ATA_03-SUPPORT_INFORMATION_GSE \
      --verbose
```

This runs automatically:
- After CGen batch processing
- Before committing changes
- On scheduled waves (every 3 days)

## Document Structure Requirements

For best results, documents should follow this structure:

```markdown
# DOC-ID — Document Title

## 1. Purpose

Brief description of document purpose.

## 2. Scope

[To be completed]

## 3. Overview

[To be completed]

## 4. Requirements

[To be completed]

## 5. Procedures

[To be completed]

## 6. Document Control

| Attribute | Value |
|-----------|-------|
| Document ID | DOC-ID |
| Version | 1.0 |
| Status | Draft |
```

### Key Elements:

1. **Document Header**: First line with ID and title (e.g., `# 10-00-02-005-A — Title`)
2. **Numbered Sections**: Use `##` with numbers (e.g., `## 2. Scope`)
3. **Clear Section Titles**: Descriptive titles help generate better content
4. **Document Control**: Always include metadata table at the end

## Content Generation

### What Gets Generated

The AI generates contextually appropriate content based on:

- **Document type** (inferred from ID and title)
- **Section purpose** (from section title)
- **Existing content** (for consistency)
- **AMPEL360 context** (aerospace safety documentation standards)

### Content Quality

Generated content includes:

- **Technical accuracy** appropriate for aerospace documentation
- **Proper structure** with subsections, lists, and tables
- **Professional tone** suitable for certification and safety documents
- **Markdown formatting** consistent with repository standards

### Example Generated Content

For section `2. Scope`, the tool might generate:

```markdown
This document applies to all AMPEL360 ground operations where LH₂ is produced, 
delivered, stored, conditioned, transferred, or used as process/propulsion fuel, 
including but not limited to:

- Fixed LH₂ storage tanks and associated piping systems within AMPEL360-controlled areas.
- Mobile LH₂ delivery units (road tankers, containerized modules) while on site.
- LH₂ conditioning, pumping, and vaporization skids used to supply aircraft and test stands.
- LH₂ lines, couplings, and interfaces to Ground Support Equipment (GSE) for BWB H₂ Hy-E aircraft.
- Maintenance, inspection, and testing activities that may expose personnel to LH₂ or cold surfaces.

The scope excludes detailed design specifications for individual components (handled in 
dedicated design documents) and site-specific emergency response plans (covered by local 
HSE documentation). However, it provides the technical hazard basis on which those 
documents must rely.
```

## Best Practices

### 1. Use Clear Section Titles

❌ **Avoid**:
```markdown
## 3. Info

[To be completed]
```

✅ **Prefer**:
```markdown
## 3. Overview

[To be completed]
```

### 2. Provide Context in Document Title

❌ **Avoid**:
```markdown
# DOC-001 — Document

[To be completed]
```

✅ **Prefer**:
```markdown
# 10-00-02-005-A — LH₂ Properties and Hazards

[To be completed]
```

### 3. Fill Sections Incrementally

Rather than leaving all sections as placeholders, fill what you know and let the tool complete the rest. This provides better context.

### 4. Review Generated Content

Always review AI-generated content for:
- Technical accuracy
- Completeness
- Compliance with standards
- Appropriate references

### 5. Iterate if Needed

If generated content isn't quite right:
1. Add more context to surrounding sections
2. Use more specific section titles
3. Run the tool again

## Troubleshooting

### Problem: "OPENAI_API_KEY not set"

**Solution**: Set the environment variable:
```bash
export OPENAI_API_KEY="your-key-here"
```

### Problem: "No placeholders found"

**Causes**:
- Placeholders don't match expected patterns
- File has already been filled
- Wrong target directory

**Solution**: Verify placeholders exactly match `[To be completed]` or `[CGEN:...]`

### Problem: Generated content has errors

**Solutions**:
1. Check that document header is properly formatted
2. Ensure section titles are clear and descriptive
3. Provide more context in adjacent sections
4. Review and edit generated content manually

### Problem: Script fails with API errors

**Causes**:
- Invalid API key
- Rate limiting
- Network issues

**Solutions**:
1. Verify API key is valid
2. Add delays between requests (script handles this automatically)
3. Check network connectivity

## Safety and Quality Assurance

### Human Review Required

All AI-generated content must be reviewed by qualified personnel before:
- Being used in certification documentation
- Being referenced in safety-critical procedures
- Being submitted to regulatory authorities

### Version Control

- All changes are tracked in Git
- Generated content is marked with AI assistance attribution
- Document Control sections include AI generation metadata

### Iterative Improvement

The tool learns from:
- Document structure patterns
- Existing high-quality content
- Cross-references in the repository

As more documents are completed, generation quality improves.

## Examples

### Example 1: Safety Document

**Input**:
```markdown
# 10-00-02-005-B — Leak Detection Response

## 1. Purpose

This document defines procedures for detecting and responding to hydrogen leaks.

## 2. Scope

[To be completed]
```

**Generated Output**:
```markdown
## 2. Scope

This document applies to:

- All personnel working in areas where hydrogen is stored, handled, or transferred
- Ground operations supervisors responsible for hydrogen safety
- Emergency response teams
- Maintenance personnel working on hydrogen systems

The scope covers:
- Detection methods for hydrogen leaks (fixed and portable sensors)
- Response procedures for confirmed and suspected leaks
- Evacuation procedures and safe distances
- Communication protocols during leak events
- Post-incident assessment and return-to-service criteria

Excluded from scope:
- Design specifications for detection equipment (see ATA 10-00-04)
- Detailed emergency response plans (see site-specific HSE documentation)
```

### Example 2: Training Document

**Input**:
```markdown
# 03-10-00-015 — GSE Operator Training Requirements

## 1. Purpose

Define training requirements for Ground Support Equipment operators.

## 3. Training Modules

[CGEN:TODO]
```

**Generated Output**:
```markdown
## 3. Training Modules

### 3.1 Initial Training

**Module 1: GSE Fundamentals (4 hours)**
- Types of ground support equipment
- Safety protocols and hazards
- Pre-operation inspections
- Basic operation procedures

**Module 2: Hydrogen Systems Safety (8 hours)**
- Hydrogen properties and hazards
- Personal protective equipment
- Leak detection and response
- Emergency procedures
- Hands-on emergency drills

**Module 3: Equipment-Specific Training (varies)**
- Specific GSE system operation
- Maintenance procedures
- Troubleshooting
- Documentation requirements

### 3.2 Refresher Training

- Annual refresher (4 hours)
- Covers regulatory updates and incident lessons learned
- Practical assessment and competency check

### 3.3 Certification Requirements

- Written examination (minimum 80% pass rate)
- Practical demonstration
- Supervisor observation and sign-off
- Recertification every 24 months
```

## Reference Document

See `10-00-02-005-A_LH2_Properties_Hazards.md` for a complete example of a fully filled document that serves as a reference pattern for the tool's output quality.

## Support and Feedback

For issues or suggestions:
- Check workflow logs in GitHub Actions
- Review generated content carefully
- Submit feedback through issue tracking
- Contribute improvements to the tool

---

**Part of the AMPEL360 CGen Documentation Automation**  
Generated with the assistance of AI (GitHub Copilot), prompted by Amedeo Pelliccia.
