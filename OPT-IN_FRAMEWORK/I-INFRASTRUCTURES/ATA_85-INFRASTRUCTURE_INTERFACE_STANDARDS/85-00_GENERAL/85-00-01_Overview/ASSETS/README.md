# ASSETS - ATA 85-00-01 Overview

## Purpose

This folder contains design artifacts, diagrams, and data supporting the ATA 85 Infrastructure Interface Standards Overview documentation. Assets are organized according to the [AMPEL360 ASSETS Standard](../../../../../../AMPEL360_ASSETS_STANDARD.md).

## Contents

This ASSETS folder includes:

- **Diagrams**: Context diagrams, layered architecture views, and scenario illustrations
- **Data**: Cross-ATA interface mapping tables

All assets follow the naming convention: `85-00-01-A-<nnn>_<CATEGORY>_<ShortName>.<ext>`

## Asset Inventory

### Diagrams

| Asset ID | Filename | Description | Status |
|----------|----------|-------------|--------|
| A-001 | 85-00-01-A-001_BWB_Infrastructure_Context.drawio | BWB aircraft on stand with all infrastructure interfaces (editable source) | Placeholder |
| A-002 | 85-00-01-A-002_BWB_Infrastructure_Context.svg | SVG export of infrastructure context diagram | Placeholder |
| A-003 | 85-00-01-A-003_H2_and_CO2_Interface_Layers.svg | Layered view of H₂ and CO₂ battery interfaces | Placeholder |
| A-004 | 85-00-01-A-004_Evacuation_Interface_Scenarios.svg | Evacuation scenarios with rescue access | Placeholder |

### Data Tables

| Asset ID | Filename | Description | Status |
|----------|----------|-------------|--------|
| A-005 | 85-00-01-A-005_Cross_ATA_Interface_Table.xlsx | Comprehensive cross-ATA interface mapping | Placeholder |

## Usage Guidelines

### For Documentation Authors

When referencing assets in markdown documents, use relative paths:

```markdown
![BWB Infrastructure Context](ASSETS/85-00-01-A-002_BWB_Infrastructure_Context.svg)
```

Or as a link:

```markdown
See [BWB Infrastructure Context Diagram](ASSETS/85-00-01-A-002_BWB_Infrastructure_Context.svg)
```

### For Asset Creators

1. **Create assets** following the specifications in placeholder files
2. **Use the prescribed naming convention**: `85-00-01-A-<nnn>_<CATEGORY>_<ShortName>.<ext>`
3. **Update INDEX.meta.yaml** when adding or modifying assets:
   - Change status from "Placeholder" to "Draft" or "Active"
   - Add file size, software version, and completion date
4. **Remove placeholder files** once actual assets are created (or rename with `.replaced` extension)

### For Design Reviewers

- Verify assets against requirements in overview documentation
- Check diagram accuracy (dimensions, interface locations, labeling)
- Validate data tables for completeness and correctness
- Ensure consistency across related assets

## Placeholder Status

**All current assets are placeholders.** Placeholder files contain:

- Description of expected content
- File format and style guidelines
- Usage context (which documents reference the asset)
- Target completion dates (to be determined by project planning)

**Action Required:**

- Design team / technical illustrators: Create diagram assets (A-001 through A-004)
- Systems engineering team: Create cross-ATA interface table (A-005)
- Update INDEX.meta.yaml as assets are completed

## Asset Dependencies

```
A-001 (drawio source)
  └─> A-002 (SVG export) → Referenced in multiple .md documents

A-003 (SVG) → Referenced in 85-00-01-002 (H₂/CO₂ Interfaces)

A-004 (SVG) → Referenced in 85-00-01-003 (Evacuation/Rescue)

A-005 (xlsx) → Referenced in 85-00-01-001, 85-00-01-005 (Cross-ATA mapping)
```

## Authoritative Catalog

The definitive list of assets, their metadata, and status is maintained in:

**[INDEX.meta.yaml](INDEX.meta.yaml)**

This file is the single source of truth for:

- Asset inventory (IDs, filenames, formats)
- Asset status (Placeholder / Draft / Active / Deprecated)
- Asset relationships (source files, exports, references)
- Validation data (naming compliance, completeness checks)

## Version Control

- **Asset Source Files**: Commit source files (e.g., .drawio) to version control
- **Exported Files**: Commit exports (e.g., .svg, .png) for convenience, but regenerate from source if source changes
- **Data Files**: Commit data files (.xlsx, .csv) with meaningful commit messages describing changes

## Standards Compliance

Assets in this folder comply with:

- [AMPEL360 ASSETS Standard](../../../../../../AMPEL360_ASSETS_STANDARD.md) - Overall structure and naming
- [AMPEL360 Documentation Standard](../../../../../../AMPEL360_DOCUMENTATION_STANDARD.md) - Integration with documentation
- [OPT-IN Framework Standard](../../../../../../OPT-IN_FRAMEWORK_STANDARD.md) - Folder hierarchy and lifecycle

---

## Document Control

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT** – Subject to human review and approval.
- Human approver: _[to be completed]_.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: 2025-11-21

---
