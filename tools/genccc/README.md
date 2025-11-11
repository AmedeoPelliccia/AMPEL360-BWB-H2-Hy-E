# GenCCC - Generation Cross-Reference Content Consistency

GenCCC is an automated tool for maintaining cross-reference integrity and generating contextual documentation in the AMPEL360 BWB H₂ Hy-E aircraft project.

## Overview

This tool provides two main functions:

1. **Report Mode** (`report.py`): Generates audit reports identifying:
   - Broken internal links
   - Missing cross-references between related documents
   - Documentation structure inconsistencies
   - ATA chapter reference integrity

2. **Apply Mode** (`apply.py`): Applies automatic fixes including:
   - Fixing broken internal links by finding moved files
   - Generating missing documentation with AI-powered contextual content
   - Adding cross-references between related documents
   - Maintaining ATA structure consistency

## Usage

### Local Usage

#### Generate Report
```bash
python tools/genccc/report.py
```
Output: `cd/reports/cross_reference_audit.md`

#### Apply Fixes
```bash
python tools/genccc/apply.py
```
Note: Set `OPENAI_API_KEY` environment variable for AI-powered content generation.

### CI/CD Integration

The GenCCC workflow runs automatically on:

1. **Pull Request** (Report Mode):
   - Triggered on any markdown file changes
   - Generates cross-reference audit report
   - Posts report as artifact and PR comment
   - Non-destructive - no changes to files

2. **Comment `/genccc apply`** (Apply Mode):
   - Triggered by commenting `/genccc apply` on a PR
   - Applies automatic fixes to broken links
   - Generates missing documentation with contextual content
   - Commits changes back to the PR

## Workflow

```
┌─────────────────────┐
│  Open PR with .md   │
│     file changes    │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│   Report Job Runs   │
│  (Non-destructive)  │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│  Review Report &    │
│  Comment on PR:     │
│  "/genccc apply"    │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│   Apply Job Runs    │
│  (Fixes & Commits)  │
└─────────────────────┘
```

## Safety Features

- **Report mode is non-destructive**: Only analyzes and reports, never modifies files
- **Apply mode requires explicit trigger**: Must comment `/genccc apply` on PR
- **Conservative file generation**: Only creates files when safe to do so
- **Reviewer control**: All changes are reviewed before merging
- **Traceability**: All changes are committed with clear commit messages

## Configuration

The tool is configured to work with the AMPEL360 project structure:

- **Framework Root**: `OPT-IN_FRAMEWORK/`
- **Report Output**: `cd/reports/` (ignored by git)
- **Target Files**: All `*.md` files in the repository

## Requirements

- Python 3.11+
- OpenAI Python client (for apply mode with AI generation)
- `OPENAI_API_KEY` environment variable (optional, for AI-powered generation)

## Architecture Integration

GenCCC is designed to maintain consistency across:
- **CAOS Framework**: Computer Aided Operations and Services documentation
- **ATA iSpec 2200**: Aviation industry standard chapter structure
- **OPT-IN Framework**: 5-area documentation structure (I, N, O, P, T)

## Development

### Adding New Features

To extend GenCCC functionality:

1. **Report generation**: Modify `report.py` to add new analysis
2. **Fix application**: Modify `apply.py` to add new fix types
3. **Workflow integration**: Update `.github/workflows/genccc.yml`

### Testing

```bash
# Test report generation
python tools/genccc/report.py

# Test apply (without AI)
unset OPENAI_API_KEY
python tools/genccc/apply.py

# Test apply (with AI)
export OPENAI_API_KEY="your-key-here"
python tools/genccc/apply.py
```

## Maintenance

- Reports are generated in `cd/reports/` (git-ignored)
- Artifacts are retained for 30 days in GitHub Actions
- Workflow runs have timeout protection (10 min for report, 20 min for apply)

## Support

For issues or questions:
- Review the workflow logs in GitHub Actions
- Check the generated audit report in PR artifacts
- Refer to the main project documentation

---

**Part of the AMPEL360 BWB H₂ Hy-E Project**  
Maintaining documentation excellence for the world's first carbon-negative commercial aircraft.
