# DML — Data Module Lists

## Overview

This directory contains **Data Module Lists (DML)** for the Illustrated Parts Catalog (IPC). Data Module Lists are S1000D objects that group and organize related Data Modules for management and referencing purposes.

## Purpose

Data Module Lists:
- Group logically related parts Data Modules
- Simplify bulk operations on sets of modules
- Support publication planning and management
- Enable subset publishing
- Facilitate content review and approval workflows
- Track Data Module sets for translation
- Support configuration management

## Naming Convention

Data Module Lists follow the S1000D DML Code structure:

```
DML-AMPEL360-{ATA}-{SECTION}-{LIST_ID}_{LANG}_{ISSUE}.XML
```

### Components

- **Model ID**: `AMPEL360` (fixed)
- **ATA Chapter**: `23` (Communications)
- **Section**: `00-99` (per ATA SNS)
- **List ID**: `A` to `ZZZZZZZZ` (unique identifier for the list)
- **Language**: `EN-US`, `EN-GB`, `FR-FR`, etc. (ISO language codes)
- **Issue**: `001-00` to `999-99` (issue number and in-work revision)

### Examples

**Parts List DML**:
```
DML-AMPEL360-23-10-PARTSLIST_EN-US_001-00.XML
```
*List of all parts list data modules for speech communications*

**IPB DML**:
```
DML-AMPEL360-23-10-IPB_EN-US_001-00.XML
```
*List of all illustrated parts breakdown data modules*

**Translation Set DML**:
```
DML-AMPEL360-23-10-TRANSFR_FR-FR_001-00.XML
```
*Data modules requiring French translation*

## Use Cases

### Publication Planning

**Initial Release DML**:
```xml
<!-- Lists all DMs for first publication release -->
DML-AMPEL360-23-10-REL001_EN-US_001-00.XML
```

**Update Release DML**:
```xml
<!-- Lists only changed DMs for incremental update -->
DML-AMPEL360-23-10-UPD002_EN-US_001-00.XML
```

### Content Management

**Review Cycle DML**:
```xml
<!-- DMs pending technical review -->
DML-AMPEL360-23-10-REVIEW_EN-US_001-00.XML
```

**Approval DML**:
```xml
<!-- DMs awaiting final approval -->
DML-AMPEL360-23-10-APPROVAL_EN-US_001-00.XML
```

## File Structure

Each Data Module List XML file contains:

1. **Identification and Status Section**
   - DML code and title
   - Responsible partner company
   - Issue and security information

2. **DML Content Section**
   - List of Data Module references
   - Entry metadata (status, reason for entry)
   - Remarks and annotations

3. **DML Entry**
   - Data Module Code (DMC)
   - Issue information
   - Security classification
   - Entry type (new, changed, deleted)

## List Types

### By Content Category

- **Parts Lists**: Tabular parts data
- **IPB**: Illustrated parts breakdowns
- **Cross-Reference**: Part number cross-refs
- **Vendor Data**: Supplier information

### By Status

- **Draft**: DMs in authoring stage
- **Review**: DMs under review
- **Approved**: DMs ready for publication
- **Published**: DMs in released publications
- **Obsolete**: Superseded or withdrawn DMs

## DML Entry Types

| Type | Code | Description |
|------|------|-------------|
| **New** | `new` | Data Module added to list |
| **Changed** | `changed` | Data Module modified since last issue |
| **Deleted** | `deleted` | Data Module removed from list |
| **Unchanged** | `unchanged` | Data Module retained with no changes |

## Best Practices

- **Clear Purpose**: Each DML should have a well-defined purpose
- **Descriptive IDs**: Use meaningful list identifiers
- **Regular Updates**: Keep DMLs current with DM status
- **Proper Metadata**: Include complete entry information
- **Version Control**: Track DML changes over time

## Validation

All Data Module Lists must:
- Validate against S1000D Issue 5.0 schema
- Reference only valid Data Module Codes
- Comply with AMPEL360 BREX rules
- Have unique list identifiers
- Include all required metadata elements

## Related Directories

- `../DM/` - Data Modules referenced in lists
- `../PM/` - Publication Modules that may reference DMLs
- `../BREX/` - Validation rules for DMLs
- `../APPLICABILITY/` - Applicability filters for DM selection

## Document Control

- **Standard**: S1000D Issue 5.0
- **Project**: AMPEL360-AIR-T
- **ATA Chapter**: 23 (Communications)
- **Section**: 23-10-00 (Speech Communications)
- **Publication Type**: IPC (Illustrated Parts Catalog)
- **Status**: Active
- **Last Updated**: 2026-01-09
- **Generated with AI assistance**: GitHub Copilot, prompted by Amedeo Pelliccia
