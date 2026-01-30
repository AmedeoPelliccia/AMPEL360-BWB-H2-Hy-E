# CSDB — Common Source Database

## Overview

This directory contains the **Common Source Database (CSDB)** following the **S1000D** international specification for technical publications.

## Purpose

The CSDB is a structured repository of modular documentation components that can be:
- Reused across multiple publications
- Maintained independently
- Version controlled
- Validated against business rules
- Published in multiple formats

## Directory Structure

```
CSDB/
├── DM/              # Data Modules
├── PM/              # Publication Modules
├── DML/             # Data Module Lists
├── ICN/             # Illustrations/Graphics
├── BREX/            # Business Rules Exchange
├── COMMON/          # Common Information Sets
└── APPLICABILITY/   # Applicability Statements
```

## Component Descriptions

### DM — Data Modules
Individual, self-contained units of documentation. Each data module covers a specific topic or task.

**Naming Convention**: `DMC-AMPEL360-{ATA}-{SECTION}-{SUBJECT}-{INFO_CODE}-{VARIANT}-{ITEM_LOCATION}_XXX_00_{LANG}_{ISSUE}.XML`

Example: `DMC-AMPEL360-24-20-00-00A-040A-A_001_00_EN-US_001-00.XML`

### PM — Publication Modules
Define the structure and organization of publications. PMs reference data modules and other PMs to create hierarchical documentation.

**Naming Convention**: `PMC-AMPEL360-{ATA}-{SECTION}-{PUBLICATION_CODE}_XXX_00_{ISSUE}.XML`

Example: `PMC-AMPEL360-24-20-00001_001_00_001-00.XML`

### DML — Data Module Lists
Lists that group related data modules together. Used for managing sets of modules.

**Naming Convention**: `DML-AMPEL360-{ATA}-{SECTION}-{LIST_ID}_{LANG}_{ISSUE}.XML`

### ICN — Illustrations/Graphics
Multimedia objects including:
- Technical illustrations
- Photographs
- Videos
- 3D models
- Interactive graphics

**Naming Convention**: `ICN-AMPEL360-{ATA}-{SECTION}-{GRAPHIC_ID}-{VARIANT}_{FORMAT}.{EXT}`

Example: `ICN-AMPEL360-24-20-001-A_001.SVG`

### BREX — Business Rules Exchange
XML-based validation rules that enforce:
- Content structure requirements
- Metadata requirements
- Allowed values and codes
- Publication-specific constraints

**File**: `BREX-AMPEL360-{PROJECT}-{VERSION}.XML`

### COMMON — Common Information Sets
Reusable content fragments that can be referenced from multiple data modules:
- Standard warnings and cautions
- Common procedures
- Standard definitions
- Reusable descriptions

**Naming Convention**: `COM-AMPEL360-{INFO_TYPE}-{ID}_{LANG}_{ISSUE}.XML`

### APPLICABILITY — Applicability Statements
Define which content applies to which product variants, configurations, or serialized items.

**File**: `APPLICCROSS-AMPEL360-{PROJECT}_{ISSUE}.XML`

## S1000D Compliance

This CSDB structure follows:
- **S1000D Issue 5.0** specification
- **ATA iSpec 2200** chapter numbering
- **AMPEL360** project-specific BREX rules

## Workflow

1. **Create**: Author data modules for specific topics/tasks
2. **Illustrate**: Create graphics and place in ICN/
3. **Structure**: Define publication structure in PM/
4. **Validate**: Apply BREX rules to ensure compliance
5. **Publish**: Transform to output formats (PDF, HTML, XML)
6. **Deliver**: Export final publications to EXPORT/ directory

## Data Module Coding

Data modules use a standardized coding scheme:

- **Model Identification Code**: AMPEL360
- **ATA Chapter**: 24 (Electrical Power)
- **Section**: 24-20
- **Info Code**: Standard S1000D information codes
- **Language**: ISO language codes (e.g., EN-US)

## References

- S1000D Issue 5.0 Specification
- ATA iSpec 2200 Standard Numbering System
- AMPEL360 BREX Documentation
- S1000D User Guide

## Document Control

- **Standard**: S1000D Issue 5.0
- **Project**: AMPEL360-AIR-T
- **Publication Type**: IPC
- **Status**: Active
- **Last Updated**: 2026-01-09
