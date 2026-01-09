# DM — Data Modules

## Overview

This directory contains **Data Modules (DM)** for the Aircraft Maintenance Manual (AMM). Data Modules are the fundamental building blocks of S1000D technical publications.

## Purpose

Data Modules are self-contained, topic-based units of information that:
- Cover a single, well-defined subject or task
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
- **ATA Chapter**: `22` (Autoflight)
- **Section**: `00-99` (per ATA SNS - Standard Numbering System)
- **Subject**: `00-99` (per ATA SNS)
- **Info Code**: Standard S1000D codes (e.g., `040A` for descriptive, `520A` for procedure)
- **Variant**: `A-Z` (design or configuration variant)
- **Item Location**: `A-ZZZ` (identifies specific location or component)
- **Sequence**: `XXX` (001-999, sequential number)
- **Indenture**: `00` (hierarchical level)
- **Language**: `EN-US`, `EN-GB`, `FR-FR`, etc. (ISO language codes)
- **Issue**: `001-00` to `999-99` (issue number and in-work revision)

### Examples

**Descriptive Data Module** (Info Code 040A):
```
DMC-AMPEL360-22-00-00-040A-A-A_001_00_EN-US_001-00.XML
```
*Description: General autoflight system overview*

**Procedural Data Module** (Info Code 520A):
```
DMC-AMPEL360-22-10-00-520A-A-001_001_00_EN-US_001-00.XML
```
*Description: Autopilot system test procedure*

**Fault Isolation Data Module** (Info Code 730A):
```
DMC-AMPEL360-22-20-00-730A-A-001_001_00_EN-US_001-00.XML
```
*Description: Flight director fault isolation*

**Removal/Installation Data Module** (Info Code 520B):
```
DMC-AMPEL360-22-30-00-520B-A-001_001_00_EN-US_001-00.XML
```
*Description: Yaw damper removal and installation*

## Information Codes

Common S1000D information codes for maintenance manuals:

| Code | Description | Use Case |
|------|-------------|----------|
| **040A** | Description | System/component descriptions |
| **520A** | Procedure - Operational | Operational tests, servicing |
| **520B** | Procedure - Maintenance | Removal, installation, adjustment |
| **730A** | Fault Isolation | Troubleshooting procedures |
| **940A** | Computer Systems/Software | Software loading, configuration |

## File Structure

Each Data Module XML file contains:

1. **Identification and Status Section** - Metadata, applicability, security
2. **Content Section** - Actual technical content (procedure steps, descriptions, etc.)
3. **References** - Links to other data modules, ICNs, and publications

## Content Types

Data Modules can contain:

- **Descriptive** - System descriptions, theory of operation
- **Procedural** - Step-by-step maintenance tasks
- **Fault Isolation** - Troubleshooting logic and flowcharts
- **Crew** - Operating procedures (for flight crew manuals)
- **Learning** - Training content
- **Planning** - Planning and scheduling information

## Workflow

1. **Author**: Create data module in XML editor (e.g., Arbortext, Oxygen XML)
2. **Validate**: Check against BREX rules and S1000D schema
3. **Review**: Technical and editorial review
4. **Illustrate**: Link to ICN files for graphics
5. **Translate**: Create language variants as needed
6. **Publish**: Include in Publication Modules (PM) for final publications

## Best Practices

- **One Topic Per Module**: Each DM should address a single, discrete topic
- **Consistent Granularity**: Maintain similar level of detail across modules
- **Clear Titles**: Use descriptive titles that clearly identify content
- **Applicability**: Define product applicability accurately
- **Cross-References**: Use proper S1000D referencing mechanisms
- **Version Control**: Track all changes with issue numbers
- **Reusability**: Design modules for maximum reuse potential

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
- **ATA Chapter**: 22 (Autoflight)
- **Publication Type**: AMM (Aircraft Maintenance Manual)
- **Status**: Active
- **Last Updated**: 2026-01-09
- **Generated with AI assistance**: GitHub Copilot, prompted by Amedeo Pelliccia
