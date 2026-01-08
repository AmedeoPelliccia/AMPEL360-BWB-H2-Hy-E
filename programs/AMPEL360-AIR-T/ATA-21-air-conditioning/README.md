# ATA 21 — Air Conditioning

## Overview

This directory implements **ATA Chapter 21 – Air Conditioning** according to the **ATA iSpec 2200 Standard Numbering System (SNS)**.

The structure follows a **subject-level (21-xx-yy)** organization with integrated **S1000D CSDB** (Common Source Data Base) publication framework.

## ATA SNS Structure

ATA 21 is organized into the following **sections** (third and fourth digits):

| Section | Directory | Description |
|---------|-----------|-------------|
| **21-00** | `21-00-air-conditioning-general` | Air Conditioning General |
| **21-10** | `21-10-compression` | Compression |
| **21-20** | `21-20-distribution` | Distribution |
| **21-30** | `21-30-pressurization-control` | Pressurization Control |
| **21-40** | `21-40-heating` | Heating |
| **21-50** | `21-50-cooling` | Cooling |
| **21-60** | `21-60-temperature-control` | Temperature Control |
| **21-70** | `21-70-moisture-air-contaminant-control` | Moisture & Air Contaminant Control |

Each section contains **subjects** (fifth and sixth digits) in the format `21-xx-yy-<subject-name>`.

## Subject-Level Organization

### Subject Directory Pattern

```
21-xx-<section-name>/
└─ 21-xx-yy-21-xx-<section-name>/
   ├─ SSOT/                    # Single Source of Truth (master content)
   └─ PUB/                     # Publication Views
      ├─ AMM/                  # Aircraft Maintenance Manual
      │  ├─ CSDB/             # Common Source Data Base
      │  │  ├─ DM/            # Data Modules
      │  │  ├─ PM/            # Publication Modules
      │  │  ├─ DML/           # Data Module List
      │  │  ├─ ICN/           # Illustrations (ICN = Illustration Control Number)
      │  │  ├─ BREX/          # Business Rules Exchange
      │  │  ├─ COMMON/        # Common content elements
      │  │  └─ APPLICABILITY/ # Applicability cross-reference tables
      │  ├─ EXPORT/           # Published output (PDF, HTML, etc.)
      │  ├─ bindings.csv      # Data Module to Publication Module bindings
      │  └─ csdb.profile.yaml # CSDB configuration profile
      └─ IPC/                  # Illustrated Parts Catalog
         ├─ CSDB/             # (same structure as AMM)
         ├─ EXPORT/
         ├─ bindings.csv
         └─ csdb.profile.yaml
```

### Subject Numbering Convention

- **21-xx-00**: Reserved for "General" subject in each section
- **21-xx-YY**: Additional subjects as defined by ATA iSpec 2200 SNS

Example:
- `21-00-00-21-00-air-conditioning-general` — Air Conditioning General (section 00, subject 00)
- `21-10-00-21-10-compression` — Compression General (section 10, subject 00)

## S1000D CSDB Structure

### CSDB Subdirectories

| Directory | Purpose | Content |
|-----------|---------|---------|
| **DM/** | Data Modules | S1000D XML data modules (procedural, descriptive, fault data) |
| **PM/** | Publication Modules | Publication structure definitions |
| **DML/** | Data Module Lists | Lists of data modules to include in publications |
| **ICN/** | Illustrations | Graphics, diagrams, photos (SVG, PNG, JPEG) |
| **BREX/** | Business Rules Exchange | Validation rules for S1000D compliance |
| **COMMON/** | Common Information | Reusable content snippets and common information repositories |
| **APPLICABILITY/** | Applicability | Cross-reference tables defining applicability of data modules |

### Publication Views

#### AMM (Aircraft Maintenance Manual)
Contains maintenance procedures, troubleshooting, and servicing instructions for ATA 21 systems.

#### IPC (Illustrated Parts Catalog)
Contains illustrated parts breakdowns, part numbers, and ordering information.

### Supporting Files

#### bindings.csv
Maps data modules to publication modules, defining the structure of generated publications.

Format:
```csv
data_module_code,publication_module_code,sequence
DMC-AMPEL-21-00-00-00A-940A-A,PMC-AMPEL-Q100-21-00-00-00A-00A,010
```

#### csdb.profile.yaml
Defines S1000D CSDB configuration for the publication view.

Example:
```yaml
# S1000D CSDB Profile
publication_id: "AMM-AMPEL-Q100-21"
issue_number: "001"
in_work: "01"
security_classification: "01"
responsible_partner_company:
  enterprise_name: "AMPEL360"
  enterprise_code: "AMPEL"
```

## SSOT (Single Source of Truth)

The **SSOT** directory contains master content in modular format before publication-specific transformation:

- Requirements documents
- Design specifications
- Test procedures
- Engineering data
- Source CAD files

Content in SSOT is transformed and published into AMM, IPC, and other publication views as needed.

## Usage Guidelines

### Adding New Subjects

To add a new subject under a section:

1. Create directory: `21-xx-YY-<subject-name>/`
2. Add `SSOT/` and `PUB/` subdirectories
3. Create `PUB/AMM/` and `PUB/IPC/` with full CSDB structure
4. Populate `bindings.csv` and `csdb.profile.yaml`

### Authoring S1000D Data Modules

Data modules must follow S1000D Issue 5.0 (or higher) specification:

- **DMC**: Data Module Code following S1000D naming convention
- **XML Schema**: Compliant with S1000D schema
- **ICN**: Illustration Control Numbers for all graphics
- **Applicability**: Properly tagged for aircraft variants

### Publishing Workflow

1. Author content in **SSOT** (master format)
2. Generate **Data Modules (DM)** from SSOT
3. Create **Publication Modules (PM)** defining structure
4. Define **bindings** in `bindings.csv`
5. Generate publications in **EXPORT** (PDF, HTML, etc.)

## References

### Standards
- **ATA iSpec 2200**: Information Standards for Aviation Maintenance ([A4A Publications](https://publications.airlines.org/products/ispec-2200-extract-ata-standard-numbering-system-revision-2024-1))
- **S1000D**: International specification for technical publications using a Common Source Database
- **ATA 100**: Specification for Manufacturers' Technical Data
- **ATA SNS Common Sections**: See [toddheffley.com](https://toddheffley.com/wordpress/?p=5760)

### AMPEL360 Standards
- `OPT-IN_FRAMEWORK_STANDARD.md` — OPT-IN Framework structure
- `AMPEL360_DOCUMENTATION_STANDARD.md` — Documentation conventions
- `ATA_03_NUMBERING_GUIDE.md` — ATA numbering examples

## Document Control

- **Version**: 1.0
- **Status**: ACTIVE
- **Date**: 2026-01-08
- **Owner**: AMPEL360 Documentation Team
- **Repository**: `AMPEL360-AIR-T`
- **AI Assistance**: Generated with GitHub Copilot, prompted by Amedeo Pelliccia
- **Human Approver**: *[to be completed]*

---

*This directory structure supports deterministic CI/CD pipelines and regulatory compliance with EASA CS-25 and FAA Part 25 requirements.*
