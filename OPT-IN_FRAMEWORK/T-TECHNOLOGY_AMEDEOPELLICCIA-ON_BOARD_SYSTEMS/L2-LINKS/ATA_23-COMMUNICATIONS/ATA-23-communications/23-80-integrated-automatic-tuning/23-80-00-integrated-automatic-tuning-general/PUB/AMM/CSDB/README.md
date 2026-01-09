# CSDB — Common Source Database (AMM)

## Overview

This directory contains the **Common Source Database** (CSDB) for the Aircraft Maintenance Manual (AMM), organized according to S1000D standards.

## Purpose

The CSDB is the central repository for S1000D-compliant data modules and supporting files that comprise the AMM publication.

## Structure

```
CSDB/
├── DM/                 # Data Modules
├── PM/                 # Publication Modules
├── DML/                # Data Module Lists
├── ICN/                # Illustrations and Graphics
├── BREX/               # Business Rules Exchange
├── COMMON/             # Common Information Sets
└── APPLICABILITY/      # Applicability Statements
```

## Directory Descriptions

### DM — Data Modules

Data Modules are the fundamental content units in S1000D. Each DM contains:
- A single topic or procedure
- Structured XML content
- Metadata (data module code, issue info, security, etc.)
- References to illustrations and common content

**Naming Convention**: DMC-{Model Identification Code}-{System Difference Code}-{System Code}-{SubSystem Code}-{Assembly Code}-{Disassembly Code}-{Disassembly Code Variant}-{Information Code}-{Information Code Variant}-{Item Location Code}_{Issue Number}_{Language Code}-{Country Code}.XML

### PM — Publication Modules

Publication Modules define the structure and content of publications. They:
- Reference data modules to include
- Define the publication hierarchy
- Specify applicability filtering
- Control publication-level metadata

### DML — Data Module Lists

Data Module Lists are reusable collections of data module references:
- Group related data modules
- Can be referenced by multiple PMs
- Support modular publication structures

### ICN — Illustrations and Graphics

The ICN directory contains all illustrations, graphics, and multimedia:
- Vector graphics (SVG, CGM)
- Raster images (PNG, JPEG, TIFF)
- 3D models (if applicable)
- Video and animation (if applicable)

**Naming Convention**: ICN-{ICN Identification}-{Item Location Code}_{Extension}

### BREX — Business Rules Exchange

BREX files define validation rules and constraints:
- S1000D schema customization
- Project-specific validation rules
- Content rules and requirements
- Quality checks

### COMMON — Common Information Sets

Reusable content fragments shared across multiple data modules:
- Warning and caution statements
- Standard notes
- Common procedures
- Boilerplate text

### APPLICABILITY — Applicability Statements

Applicability definitions for product variants:
- Aircraft configuration applicability
- Effectivity dates and serial numbers
- Optional equipment applicability
- Retrofit applicability

## Data Module Types (AMM)

Common AMM data module types include:

- **Descriptive**: System descriptions and theory of operation
- **Procedural**: Step-by-step maintenance procedures
- **Fault Isolation**: Troubleshooting procedures
- **Fault Reporting**: Fault reporting and analysis
- **Process**: Standard maintenance processes
- **Planning**: Maintenance planning data
- **Wiring**: Wiring data and diagrams

## S1000D Compliance

This CSDB structure complies with:
- **S1000D Issue 5.0** (or as specified in project standards)
- **ATA iSpec 2200** where applicable
- Project-specific S1000D implementation rules

## Workflow

1. **Create**: Author data modules in DM/
2. **Illustrate**: Create and reference illustrations in ICN/
3. **Validate**: Validate against BREX rules
4. **Structure**: Organize data modules using PM/ and DML/
5. **Apply**: Define applicability in APPLICABILITY/
6. **Publish**: Generate publications from PM structure
7. **Export**: Output final deliverables

## Tools and Systems

CSDB management typically requires:
- S1000D authoring tools
- XML editors with S1000D support
- CSDB management system
- Validation tools
- Publication assembly tools

## Document Control

- **Standard**: S1000D Issue 5.0
- **Publication Type**: AMM (Aircraft Maintenance Manual)
- **Project**: AMPEL360-AIR-T
- **ATA Chapter**: 23 (Communications)
- **Status**: Active
- **Last Updated**: 2026-01-09
- **Generated with AI assistance**: GitHub Copilot, prompted by Amedeo Pelliccia
