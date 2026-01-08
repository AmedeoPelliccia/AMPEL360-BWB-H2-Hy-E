# 21-20-00-21-20-distribution — Distribution General

## Overview

This subject directory contains general documentation and data modules for **Distribution** under ATA 21-20.

This follows the **ATA iSpec 2200 Standard Numbering System (SNS)** subject-level organization with integrated **S1000D CSDB** structure.

## Directory Structure

```
21-20-00-21-20-distribution/
├─ README.md                     # This file
├─ SSOT/                         # Single Source of Truth (master content)
└─ PUB/                          # Publication Views
   ├─ AMM/                       # Aircraft Maintenance Manual
   │  ├─ CSDB/                  # Common Source Data Base
   │  │  ├─ DM/                 # Data Modules (S1000D XML)
   │  │  ├─ PM/                 # Publication Modules
   │  │  ├─ DML/                # Data Module Lists
   │  │  ├─ ICN/                # Illustrations (SVG, PNG, JPEG)
   │  │  ├─ BREX/               # Business Rules Exchange
   │  │  ├─ COMMON/             # Common content elements
   │  │  └─ APPLICABILITY/      # Applicability cross-reference
   │  ├─ EXPORT/                # Published output (PDF, HTML)
   │  ├─ bindings.csv           # DM to PM bindings
   │  └─ csdb.profile.yaml      # CSDB configuration
   └─ IPC/                       # Illustrated Parts Catalog
      ├─ CSDB/                  # (same structure as AMM)
      ├─ EXPORT/
      ├─ bindings.csv
      └─ csdb.profile.yaml
```

## SSOT (Single Source of Truth)

The **SSOT** directory contains master content before publication-specific transformation:

- Requirements and specifications
- Design documentation
- Engineering analysis
- Test procedures
- Source CAD/CAE files
- Configuration data

Content is version-controlled and serves as the authoritative source for all derived publications.

## PUB/AMM (Aircraft Maintenance Manual)

Contains maintenance-focused S1000D data modules:

| Directory | Content |
|-----------|---------|
| **DM/** | Procedural, descriptive, and fault isolation data modules |
| **PM/** | Publication structure definitions |
| **DML/** | Lists of data modules to include in publications |
| **ICN/** | Illustrations, diagrams, and photos |
| **BREX/** | S1000D validation rules |
| **COMMON/** | Reusable content snippets |
| **APPLICABILITY/** | Applicability tables for aircraft variants |

### Data Module Code (DMC) Pattern

```
DMC-AMPEL-21-20-00-<unit>-<item><variant>-<info-code><info-variant>-<lang>
```

Examples:
- `DMC-AMPEL-21-20-00-00A-520A-A` — Maintenance procedure
- `DMC-AMPEL-21-20-00-01A-040A-A` — System description
- `DMC-AMPEL-21-20-00-02A-730A-A` — Fault isolation

## PUB/IPC (Illustrated Parts Catalog)

Contains parts-focused S1000D data modules:

- Illustrated parts breakdowns
- Part numbers and nomenclature
- Assembly diagrams
- Interchangeability information
- Ordering data

### IPD (Illustrated Parts Data) Modules

IPC data modules follow S1000D IPD schema for parts catalog content.

## bindings.csv

Maps data modules to publication modules, defining the publication structure.

Format:
```csv
data_module_code,publication_module_code,sequence
DMC-AMPEL-21-20-00-00A-940A-A,PMC-AMPEL-Q100-21-20-00-00A-00A,010
DMC-AMPEL-21-20-00-01A-520A-A,PMC-AMPEL-Q100-21-20-00-00A-00A,020
```

## csdb.profile.yaml

Defines S1000D CSDB configuration for this subject:

```yaml
# S1000D CSDB Profile
publication_id: "AMM-AMPEL-Q100-21-20-00"
issue_number: "001"
in_work: "01"
security_classification: "01"
responsible_partner_company:
  enterprise_name: "AMPEL360"
  enterprise_code: "AMPEL"
```

## Authoring Workflow

1. **Create content** in SSOT using master format (Markdown, YAML, CAD)
2. **Generate S1000D data modules** from SSOT → `PUB/AMM/CSDB/DM/`
3. **Add illustrations** to `CSDB/ICN/`
4. **Define publication structure** in `CSDB/PM/`
5. **Update bindings** in `bindings.csv`
6. **Validate** against BREX rules
7. **Publish** to `EXPORT/` (PDF, HTML, SGML)

## Validation

Data modules must validate against:
- S1000D Issue 5.0+ schemas
- BREX rules in `CSDB/BREX/`
- AMPEL360 documentation standards

## References

- [ATA iSpec 2200 SNS](https://publications.airlines.org/products/ispec-2200-extract-ata-standard-numbering-system-revision-2024-1)
- S1000D Specification Issue 5.0+
- Parent Section: [21-20-distribution](../README.md)
- ATA 21 Overview: [../../README.md](../../README.md)

## Document Control

- **Subject**: 21-20-00-21-20-distribution
- **Section**: ATA 21-20
- **Status**: ACTIVE
- **Version**: 1.0
- **Date**: 2026-01-08
- **Repository**: AMPEL360-AIR-T
- **AI Assistance**: Generated with GitHub Copilot, prompted by Amedeo Pelliccia
- **Human Approver**: *[to be completed]*

---

*This subject uses the 21-xx-00 pattern as the "general" subject for section 21-20. Additional subjects can be added as 21-xx-YY when needed.*
