# DM — Data Modules

## Overview

This directory contains **Data Modules (DM)** for the Illustrated Parts Catalog (IPC). Data Modules are the fundamental building blocks of S1000D technical publications.

## Purpose

Data Modules for IPC are self-contained, topic-based units of information that:
- Contain parts lists and illustrated parts breakdowns
- Can be authored, managed, and updated independently
- Are reusable across multiple publications
- Support single-source, modular documentation
- Enable efficient content management and translation

## Naming Convention

Data Modules follow the S1000D Data Module Code (DMC) structure:

```
DMC-AMPEL360-{ATA}-{SECTION}-{SUBJECT}-{INFO_CODE}-{VARIANT}-{ITEM_LOCATION}_XXX_00_{LANG}_{ISSUE}.XML
```

### Components

- **Model ID**: `AMPEL360` (fixed)
- **ATA Chapter**: `23` (Communications)
- **Section**: `00-99` (per ATA SNS - Standard Numbering System)
- **Subject**: `00-99` (per ATA SNS)
- **Info Code**: Standard S1000D codes (e.g., `941A` for parts list, `941B` for illustrated parts breakdown)
- **Variant**: `A-Z` (design or configuration variant)
- **Item Location**: `A-ZZZ` (identifies specific location or component)
- **Sequence**: `XXX` (001-999, sequential number)
- **Indenture**: `00` (hierarchical level)
- **Language**: `EN-US`, `EN-GB`, `FR-FR`, etc. (ISO language codes)
- **Issue**: `001-00` to `999-99` (issue number and in-work revision)

### Examples

**Parts List Data Module** (Info Code 941A):
```
DMC-AMPEL360-23-10-00-941A-A-A_001_00_EN-US_001-00.XML
```
*Description: Speech communications parts list*

**Illustrated Parts Breakdown** (Info Code 941B):
```
DMC-AMPEL360-23-10-00-941B-A-001_001_00_EN-US_001-00.XML
```
*Description: VHF radio illustrated parts breakdown*

## Information Codes

Common S1000D information codes for parts catalogs:

| Code | Description | Use Case |
|------|-------------|----------|
| **941A** | Parts List | Tabular parts lists |
| **941B** | Illustrated Parts Breakdown | IPB with callouts |
| **941C** | Parts Information | Detailed parts descriptions |
| **00PA** | Parts Data | Alternate parts data format |

## File Structure

Each Data Module XML file contains:

1. **Identification and Status Section** - Metadata, applicability, security
2. **Content Section** - Parts lists, illustrated breakdowns
3. **References** - Links to other data modules, ICNs, and publications

## Content Types

IPC Data Modules contain:

- **Parts Lists** - Tabular parts with quantities and nomenclature
- **Illustrated Parts Breakdowns** - Graphics with callouts to parts
- **Parts Information** - Detailed parts descriptions
- **Cross-References** - Part number interchangeability
- **Vendor Data** - Supplier information

## Workflow

1. **Author**: Create data module in XML editor
2. **Validate**: Check against BREX rules and S1000D schema
3. **Review**: Technical and editorial review
4. **Illustrate**: Link to ICN files for IPB graphics
5. **Translate**: Create language variants as needed
6. **Publish**: Include in Publication Modules (PM) for final publications

## Best Practices

- **Accurate Part Numbers**: Verify all part numbers
- **Clear Nomenclature**: Use standard terminology
- **Applicability**: Define product applicability accurately
- **Cross-References**: Include vendor cross-references
- **Version Control**: Track all changes with issue numbers

## Validation

All Data Modules must:
- Validate against S1000D Issue 5.0 schema
- Comply with AMPEL360 BREX rules (in BREX/ directory)
- Pass quality checks for consistency and completeness
- Include all required metadata elements

## Related Directories

- `../PM/` - Publication Modules that reference these data modules
- `../DML/` - Data Module Lists that group related modules
- `../ICN/` - Illustrations referenced from data modules
- `../COMMON/` - Common content snippets used in modules
- `../BREX/` - Validation rules applied to modules

## Document Control

- **Standard**: S1000D Issue 5.0
- **Project**: AMPEL360-AIR-T
- **ATA Chapter**: 23 (Communications)
- **Section**: 23-10-00 (Speech Communications)
- **Publication Type**: IPC (Illustrated Parts Catalog)
- **Status**: Active
- **Last Updated**: 2026-01-09
- **Generated with AI assistance**: GitHub Copilot, prompted by Amedeo Pelliccia
