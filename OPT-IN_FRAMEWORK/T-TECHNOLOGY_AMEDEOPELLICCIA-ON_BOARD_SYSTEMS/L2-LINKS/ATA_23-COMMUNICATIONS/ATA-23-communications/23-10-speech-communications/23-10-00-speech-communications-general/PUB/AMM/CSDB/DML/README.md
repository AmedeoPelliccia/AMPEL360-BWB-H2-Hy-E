# DML — Data Module Lists

## Overview

This directory contains **Data Module Lists (DML)** for the Aircraft Maintenance Manual (AMM). Data Module Lists are S1000D objects that group and organize related Data Modules for management and referencing purposes.

## Purpose

Data Module Lists:
- Group logically related Data Modules
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

**System Description DML**:
```
DML-AMPEL360-23-10-SYSDESC_EN-US_001-00.XML
```
*List of all descriptive data modules for speech communications system*

**Maintenance Procedures DML**:
```
DML-AMPEL360-23-10-MAINTPROC_EN-US_001-00.XML
```
*List of all maintenance procedure data modules*

**Troubleshooting DML**:
```
DML-AMPEL360-23-10-FLTISOL_EN-US_001-00.XML
```
*List of all fault isolation data modules*

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

### Translation Management

**Translation Required**:
```xml
<!-- DMs needing translation to target language -->
DML-AMPEL360-23-10-TRANSFR_FR-FR_001-00.XML
```

**Translation Complete**:
```xml
<!-- DMs with completed French translation -->
DML-AMPEL360-23-10-COMFR_FR-FR_001-00.XML
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
   - Answer/comment information

## List Types

### By Content Category

- **Descriptive**: System descriptions and theory
- **Procedural**: Maintenance task procedures
- **Fault Isolation**: Troubleshooting procedures
- **Planning**: Maintenance planning information
- **Crew**: Flight crew procedures

### By Status

- **Draft**: DMs in authoring stage
- **Review**: DMs under review
- **Approved**: DMs ready for publication
- **Published**: DMs in released publications
- **Obsolete**: Superseded or withdrawn DMs

### By Process

- **Translation**: DMs for language conversion
- **Illustration**: DMs requiring graphics
- **Tech Review**: DMs for technical validation
- **Edit Review**: DMs for editorial review

## DML Entry Types

| Type | Code | Description |
|------|------|-------------|
| **New** | `new` | Data Module added to list |
| **Changed** | `changed` | Data Module modified since last issue |
| **Deleted** | `deleted` | Data Module removed from list |
| **Unchanged** | `unchanged` | Data Module retained with no changes |

## Workflow Integration

### Authoring Workflow

1. **Create DML**: Define scope and purpose of list
2. **Populate**: Add Data Module references
3. **Maintain**: Update as DMs are added/changed/removed
4. **Review**: Use DML to track review progress
5. **Approve**: Sign-off on complete DML set
6. **Publish**: Include DMs from approved DML

### Change Management

1. **Identify Changes**: List DMs affected by change
2. **Create Change DML**: Group changed DMs
3. **Review Impact**: Assess scope via DML
4. **Implement Changes**: Update DMs in list
5. **Release Update**: Publish changed DM set

## Best Practices

- **Clear Purpose**: Each DML should have a well-defined purpose
- **Descriptive IDs**: Use meaningful list identifiers
- **Regular Updates**: Keep DMLs current with DM status
- **Proper Metadata**: Include complete entry information
- **Version Control**: Track DML changes over time
- **Documentation**: Add remarks to clarify list purpose
- **Coordination**: Align DMLs with PM structure

## DML Management

### Creation

- Define list scope and purpose
- Assign unique list identifier
- Document selection criteria
- Populate with initial entries

### Maintenance

- Add new DM references as created
- Update entry status as DMs change
- Remove obsolete DM references
- Synchronize with publication schedule

### Review

- Verify all referenced DMs exist
- Check for missing required DMs
- Validate metadata accuracy
- Confirm applicability is correct

## Validation

All Data Module Lists must:
- Validate against S1000D Issue 5.0 schema
- Reference only valid Data Module Codes
- Comply with AMPEL360 BREX rules
- Have unique list identifiers
- Include all required metadata elements

## Common DML Patterns

### Complete System DML
Lists all DMs for entire ATA chapter:
- All information codes
- All subsections
- All variants

### Publication DML
Lists DMs included in specific publication:
- Filtered by publication scope
- Applicability-filtered
- Version-specific

### Work Package DML
Lists DMs for specific project or task:
- Project-specific modules
- Task-related content
- Time-bound scope

## Related Directories

- `../DM/` - Data Modules referenced in lists
- `../PM/` - Publication Modules that may reference DMLs
- `../BREX/` - Validation rules for DMLs
- `../APPLICABILITY/` - Applicability filters for DM selection

## Tools

Software supporting DML management:
- **S1000D Project Management Tools**: Track DM sets
- **Content Management Systems**: Organize and filter DMs
- **Publication Tools**: Select DMs via DML for publishing
- **Change Management Systems**: Track DM changes via DML

## Document Control

- **Standard**: S1000D Issue 5.0
- **Project**: AMPEL360-AIR-T
- **ATA Chapter**: 23 (Communications)
- **Section**: 23-10-00 (Speech Communications)
- **Publication Type**: AMM (Aircraft Maintenance Manual)
- **Status**: Active
- **Last Updated**: 2026-01-09
- **Generated with AI assistance**: GitHub Copilot, prompted by Amedeo Pelliccia
