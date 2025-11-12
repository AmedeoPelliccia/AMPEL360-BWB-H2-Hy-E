# GenCCC: Generative Chain of Contextualized Content

**Author:** COPILOT Agent prompted by Amedeo Pelliccia  
**Version:** 1.0  
**Date:** 2025-11-11

---

## Overview

GenCCC (Generative Chain of Contextualized Content) is an automated system that:
1. **Analyzes** all cross-references in the V&V documentation
2. **Adds hyperlinks** to improve navigation between documents
3. **Generates missing content** for referenced files that don't exist

This ensures comprehensive documentation with full traceability and easy navigation.

---

## Quick Start

### Preview Changes (Dry Run)

```bash
cd 07_V_AND_V/
python3 add_hyperlinks_genCCC.py --dry-run
```

This will show what would be changed without modifying any files.

### Apply All Changes

```bash
python3 add_hyperlinks_genCCC.py
```

This will:
- Add hyperlinks to all cross-references
- Generate missing CSV and markdown files
- Create contextualized content based on usage patterns

### Apply Only Hyperlinks (No Generation)

```bash
python3 add_hyperlinks_genCCC.py --no-generate
```

### Generate Only Missing Content (No Links)

```bash
python3 add_hyperlinks_genCCC.py --no-links
```

---

## What GenCCC Does

### 1. Cross-Reference Detection

GenCCC scans all markdown files in the V&V framework and identifies:

- **Verification Documents:** VER-02-11-XXX references
- **Validation Documents:** VAL-02-11-XXX references  
- **Requirements:** REQ-02-11-XXX references
- **CSV Files:** All .csv file references
- **JSON Files:** baseline_dimensions.json and others
- **Directories:** References to parent directories (01_OVERVIEW/, etc.)

**Total References Found:** ~258 cross-references across 16 documents

### 2. Hyperlink Addition

For each cross-reference that exists, GenCCC:

1. Calculates the relative path from source to target
2. Converts plain text to markdown link format
3. Preserves existing links (won't duplicate)
4. Updates files with proper navigation

**Example Transformation:**

**Before:**
```markdown
- [VER-02-11-005](DIMENSION_VERIFICATION/VER-02-11-005_Principal_Dimensions_Table_Check.md): Principal Dimensions Table Check
- Principal_Dimensions_Table.csv
```

**After:**
```markdown
- [VER-02-11-005](./VER-02-11-005_Principal_Dimensions_Table_Check.md): Principal Dimensions Table Check
- [Principal_Dimensions_Table.csv](../../01_OVERVIEW/PRINCIPAL_DIMENSIONS/Principal_Dimensions_Table.csv)
```

**Expected Results:**
- ~63 hyperlinks added across 17 markdown files
- Improved navigation between V&V documents
- Easy access to source data files

### 3. Content Generation

For references to files that don't exist, GenCCC generates:

#### A. Requirement CSV Files

Based on the requirement number ranges and usage context, GenCCC creates:

- `Dimensional_Requirements.csv` (REQ-02-11-001 to 006)
- `BWB_Geometry_Requirements.csv` (REQ-02-11-007 to 012)
- `Ground_Clearance_Requirements.csv` (REQ-02-11-013 to 018)
- `Reference_System_Requirements.csv` (REQ-02-11-019 to 024)
- `Airport_Compatibility_Requirements.csv` (REQ-02-11-025 to 030)
- `Tolerance_Requirements.csv` (REQ-02-11-031+)

**Structure:**
```csv
Requirement_ID,Description,Parameter,Value,Unit,Tolerance,Source,Verification_Method,Priority
REQ-02-11-001,Wingspan Specification,Wingspan,52.0,m,±0.1,Principal_Dimensions_Table.csv,[VER-02-11-001](DIMENSION_VERIFICATION/VER-02-11-001_Wingspan_Measurement.md),High
```

#### B. Missing CSV Templates

For other referenced CSV files, GenCCC generates appropriate templates based on:
- Filename patterns
- Usage context in V&V documents
- Standard data structures

#### C. Markdown Document Templates

For any referenced .md files that don't exist, GenCCC creates placeholder documents with:
- Proper header and metadata
- Purpose statement
- Content requirements section
- Document control footer

**Expected Generation:**
- ~19 files (6 requirement CSVs + 13 other templates)
- All contextualized based on how they're referenced
- Ready for team to populate with specific data

---

## GenCCC Architecture

### Contextual Intelligence

GenCCC doesn't just create generic templates—it generates **contextualized content** by:

1. **Analyzing usage patterns:** How is this file referenced? What information is expected?
2. **Mapping relationships:** What verification documents reference this requirement?
3. **Inferring structure:** Based on naming conventions and cross-references, what format is needed?
4. **Maintaining consistency:** Ensuring generated content matches existing documentation patterns

### Example: Requirement CSV Generation

When GenCCC sees multiple references to `REQ-02-11-001` through `REQ-02-11-006` in dimension verification documents, it:

1. Recognizes these are dimensional requirements
2. Extracts the parameters being verified (wingspan, length, height, etc.)
3. Pulls values from the V&V documents that reference them
4. Creates a requirement CSV with proper traceability
5. Maps each requirement to its verification document

This creates a **chain of contextualized content** that maintains full traceability.

---

## Generated File Locations

### Requirements (Created in ../03_REQUIREMENTS/)
```
03_REQUIREMENTS/
├── Dimensional_Requirements.csv
├── BWB_Geometry_Requirements.csv
├── Ground_Clearance_Requirements.csv
├── Reference_System_Requirements.csv
├── Airport_Compatibility_Requirements.csv
└── Tolerance_Requirements.csv
```

### Data Files (Created in ../01_OVERVIEW/TABLES/)
```
01_OVERVIEW/TABLES/
├── Principal_Dimensions_Table.csv (if missing)
├── Critical_Clearances.csv (if missing)
├── Station_Locations.csv (if missing)
├── Dimension_Summary.csv (if missing)
├── Geometry_Parameters.csv (if missing)
└── Airport_Compatibility.csv (if missing)
```

**Note:** GenCCC checks if files exist before generating. Many of these files already exist in the repository, so GenCCC will only create the ones that are truly missing.

---

## Command Line Options

### Full Usage

```bash
python3 add_hyperlinks_genCCC.py [OPTIONS]

Options:
  --dry-run          Preview changes without modifying files
  --no-links         Skip adding hyperlinks (only generate content)
  --no-generate      Skip content generation (only add links)
  --path PATH        Path to V&V directory (default: current directory)
  -h, --help         Show help message
```

### Common Workflows

#### 1. Initial Setup (Recommended)

```bash
# First, preview everything
python3 add_hyperlinks_genCCC.py --dry-run

# Review the output, then apply changes
python3 add_hyperlinks_genCCC.py

# Commit changes
git add .
git commit -m "Add hyperlinks and generate missing V&V content (GenCCC)"
```

#### 2. Update Links Only

If new V&V documents are added:

```bash
python3 add_hyperlinks_genCCC.py --no-generate
```

#### 3. Generate New Content Only

If references to new files are added:

```bash
python3 add_hyperlinks_genCCC.py --no-links
```

---

## Safety Features

1. **Dry Run Mode:** Always preview changes before applying
2. **Existing File Protection:** Never overwrites existing files
3. **Link Detection:** Won't create duplicate links
4. **Relative Paths:** All links use relative paths for portability
5. **Backup Recommended:** Use git to track changes and revert if needed

---

## Expected Output

### Before GenCCC

```
Cross-references found: 258
With hyperlinks: 13 (5%)
Without hyperlinks: 245 (95%)
Missing referenced files: 20
```

### After GenCCC

```
Cross-references found: 258
With hyperlinks: 76 (29%)  ← Improved!
Without hyperlinks: 182 (71%)
Missing referenced files: 0  ← All generated!
```

**Note:** Not all cross-references should be hyperlinked (e.g., references in text that aren't meant to be clickable). GenCCC focuses on the most valuable navigational links.

---

## Integration with V&V Workflow

### When to Run GenCCC

1. **After creating new V&V documents** - To add links to new content
2. **When adding new references** - To generate missing files
3. **During documentation reviews** - To ensure all links are current
4. **Before major milestones** - To validate documentation completeness

### GenCCC in CI/CD

Consider adding GenCCC checks to your CI pipeline:

```yaml
# .github/workflows/docs-check.yml
- name: Check Documentation Links
  run: |
    cd 07_V_AND_V/
    python3 add_hyperlinks_genCCC.py --dry-run --no-generate
    # Fail if missing links found
```

---

## Maintenance

### Updating GenCCC

If new reference patterns emerge:

1. Edit the `patterns` dictionary in `GenCCC.__init__`
2. Add new resolver methods (`_resolve_*_path`)
3. Add new content generators (`_gen_*`)

### Testing Changes

Always use `--dry-run` first to preview:

```bash
python3 add_hyperlinks_genCCC.py --dry-run > preview.txt
# Review preview.txt
```

---

## Troubleshooting

### Issue: "File not found" errors

**Solution:** Check that you're running the script from the `07_V_AND_V/` directory.

### Issue: Generated content not as expected

**Solution:** Review and manually edit generated files. GenCCC creates templates—human review is expected.

### Issue: Too many files generated

**Solution:** Use `--no-generate` and add hyperlinks only. Then manually create specific files.

### Issue: Links not added

**Solution:** Check if links already exist. GenCCC won't duplicate existing links.

---

## Future Enhancements

Potential GenCCC improvements:

1. **AI-Enhanced Content:** Use LLM APIs to generate more detailed content
2. **Smart Link Prioritization:** ML-based relevance scoring for links
3. **Automatic Documentation Updates:** Keep all docs in sync automatically
4. **Cross-Repository Links:** Link to external documentation
5. **Broken Link Detection:** Continuous validation of all hyperlinks

---

## Related Documentation

- [Cross_Reference_Report.md](./Cross_Reference_Report.md) - Detailed analysis of all cross-references
- [README.md](./README.md) - V&V framework overview
- [14_META_GOVERNANCE](../14_META_GOVERNANCE/) - Documentation standards

---

## Contact

For questions or issues with GenCCC:
- Review the Cross_Reference_Report.md for detailed analysis
- Check the V&V framework README.md for context
- Consult the V&V Manager (see README.md for contact info)

---

**Document Control:**
- Version: 1.0
- Status: Active
- Last Updated: 2025-11-11
- Author: COPILOT Agent prompted by Amedeo Pelliccia
