# CSDB — Common Source Database (IPC)

## Overview

This directory contains the **Common Source Database** (CSDB) for the Illustrated Parts Catalog (IPC), organized according to S1000D standards.

## Purpose

The CSDB is the central repository for S1000D-compliant data modules and supporting files that comprise the IPC publication.

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
- Parts information and nomenclature
- Illustrated parts breakdown data
- Structured XML content
- Metadata (data module code, issue info, security, etc.)
- References to illustrations

**Naming Convention**: DMC-{Model Identification Code}-{System Difference Code}-{System Code}-{SubSystem Code}-{Assembly Code}-{Disassembly Code}-{Disassembly Code Variant}-{Information Code}-{Information Code Variant}-{Item Location Code}_{Issue Number}_{Language Code}-{Country Code}.XML

### PM — Publication Modules

Publication Modules define the structure and content of IPC publications. They:
- Reference data modules to include
- Define the parts catalog hierarchy
- Specify applicability filtering
- Control publication-level metadata

### DML — Data Module Lists

Data Module Lists are reusable collections of data module references:
- Group related parts data modules
- Can be referenced by multiple PMs
- Support modular catalog structures

### ICN — Illustrations and Graphics

The ICN directory contains all illustrated parts breakdown graphics:
- Vector graphics (SVG, CGM) - preferred for IPB
- High-resolution raster images (PNG, TIFF)
- Exploded view illustrations
- Assembly/disassembly illustrations

**Naming Convention**: ICN-{ICN Identification}-{Item Location Code}_{Extension}

### BREX — Business Rules Exchange

BREX files define validation rules and constraints:
- S1000D schema customization for IPC
- Project-specific IPC validation rules
- Parts data quality rules
- Nomenclature rules

### COMMON — Common Information Sets

Reusable content fragments shared across multiple IPC data modules:
- Standard notes and warnings
- Common parts information
- Vendor information
- Standard text blocks

### APPLICABILITY — Applicability Statements

Applicability definitions for parts:
- Aircraft configuration applicability
- Effectivity dates and serial numbers
- Optional equipment applicability
- Modification applicability
- Retrofit applicability

## Data Module Types (IPC)

Common IPC data module types include:

- **Parts List**: Tabular parts lists with nomenclature
- **Illustrated Parts Breakdown**: IPB with callouts
- **Parts Information**: Detailed parts descriptions
- **Vendor Data**: Supplier and vendor information
- **Cross-Reference**: Part number cross-references
- **Applicability**: Parts applicability data

## S1000D Compliance

This CSDB structure complies with:
- **S1000D Issue 5.0** (or as specified in project standards)
- **ATA iSpec 2200** where applicable
- Project-specific S1000D implementation rules for IPC

## Workflow

1. **Create**: Author parts data modules in DM/
2. **Illustrate**: Create illustrated parts breakdowns in ICN/
3. **Validate**: Validate against BREX rules
4. **Structure**: Organize data modules using PM/ and DML/
5. **Apply**: Define parts applicability in APPLICABILITY/
6. **Publish**: Generate IPC publications from PM structure
7. **Export**: Output final deliverables

## Parts Data Management

IPC data modules typically include:
- Part numbers (OEM and customer)
- Nomenclature
- Quantity per assembly
- Units of measure
- Cage codes and vendor information
- Reference designators
- Illustration callout numbers

## Tools and Systems

CSDB management typically requires:
- S1000D authoring tools with IPC support
- Illustrated parts breakdown (IPB) creation tools
- XML editors with S1000D support
- CSDB management system
- Validation tools
- Publication assembly tools

## Document Control

- **Standard**: S1000D Issue 5.0
- **Publication Type**: IPC (Illustrated Parts Catalog)
- **Project**: AMPEL360-AIR-T
- **ATA Chapter**: 23 (Communications)
- **Status**: Active
- **Last Updated**: 2026-01-09
- **Generated with AI assistance**: GitHub Copilot, prompted by Amedeo Pelliccia
