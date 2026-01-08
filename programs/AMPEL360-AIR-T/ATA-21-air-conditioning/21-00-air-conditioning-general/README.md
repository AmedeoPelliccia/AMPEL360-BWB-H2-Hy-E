# ATA 21-00 — Air Conditioning General

## Overview

**General air conditioning system overview, architecture, and common elements**

This section is part of **ATA Chapter 21 – Air Conditioning** and follows the **ATA iSpec 2200 Standard Numbering System (SNS)**.

## Section Structure

```
21-00-air-conditioning-general/
└─ 21-00-00-21-00-air-conditioning-general/   # General subject (default)
   ├─ SSOT/                          # Single Source of Truth
   └─ PUB/                           # Publication Views
      ├─ AMM/                        # Aircraft Maintenance Manual
      │  ├─ CSDB/                   # S1000D Common Source Data Base
      │  │  ├─ DM/                  # Data Modules
      │  │  ├─ PM/                  # Publication Modules
      │  │  ├─ DML/                 # Data Module Lists
      │  │  ├─ ICN/                 # Illustrations
      │  │  ├─ BREX/                # Business Rules Exchange
      │  │  ├─ COMMON/              # Common content
      │  │  └─ APPLICABILITY/       # Applicability tables
      │  ├─ EXPORT/                 # Published output
      │  ├─ bindings.csv            # DM to PM bindings
      │  └─ csdb.profile.yaml       # CSDB profile
      └─ IPC/                        # Illustrated Parts Catalog
         └─ (same structure as AMM)
```

## Subjects

### 21-00-00 — General (Default)

The `21-00-00-21-00-air-conditioning-general` subject contains general information, common procedures, and overview documentation for this section.

**Additional subjects can be added** as `21-00-YY-<subject-name>` when specific subsystems or components require dedicated documentation per ATA iSpec 2200 SNS.

## Content Organization

### SSOT (Single Source of Truth)
Master content repository containing:
- System requirements and specifications
- Design documentation
- Engineering analysis and calculations
- Test procedures and results
- Source CAD files and models

### PUB (Publication Views)

#### AMM (Aircraft Maintenance Manual)
- Maintenance procedures
- Troubleshooting guides
- Servicing instructions
- Inspection intervals
- Repair methods

#### IPC (Illustrated Parts Catalog)
- Illustrated parts breakdowns
- Part numbers and descriptions
- Assembly diagrams
- Ordering information
- Interchangeability data

## S1000D Data Modules

Data modules in this section should use the following DMC pattern:

```
DMC-AMPEL-21-00-<subject>-<unit>-<item>-<variant>-<info-code>-<lang>
```

Example:
```
DMC-AMPEL-21-00-00-00A-520A-A  # Procedural DM
DMC-AMPEL-21-00-00-01A-040A-A  # Descriptive DM
DMC-AMPEL-21-00-00-02A-730A-A  # Fault Isolation DM
```

## Usage

1. **Author content** in SSOT directory using master format
2. **Transform to S1000D** data modules in `PUB/AMM/CSDB/DM/` or `PUB/IPC/CSDB/DM/`
3. **Create illustrations** in `CSDB/ICN/` directory
4. **Define publication structure** in `CSDB/PM/`
5. **Map bindings** in `bindings.csv`
6. **Generate publications** to `EXPORT/` directory

## References

- [ATA iSpec 2200 Extract: ATA Standard Numbering System](https://publications.airlines.org/products/ispec-2200-extract-ata-standard-numbering-system-revision-2024-1)
- [ATA Chapters and Sub-chapters Reference](https://toddheffley.com/wordpress/?p=5760)
- S1000D Specification Issue 5.0+
- Parent: [ATA 21 Air Conditioning](../README.md)

## Document Control

- **Section**: ATA 21-00
- **Status**: ACTIVE
- **Version**: 1.0
- **Date**: 2026-01-08
- **Repository**: AMPEL360-AIR-T
- **AI Assistance**: Generated with GitHub Copilot, prompted by Amedeo Pelliccia
- **Human Approver**: *[to be completed]*

---

*For additional subjects beyond 21-00-00, create `21-00-YY-<subject-name>` directories following the same structure.*
