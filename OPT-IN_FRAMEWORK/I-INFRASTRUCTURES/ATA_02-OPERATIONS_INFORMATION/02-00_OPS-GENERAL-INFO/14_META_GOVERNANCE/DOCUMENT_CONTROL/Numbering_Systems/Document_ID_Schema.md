# Document ID Schema

**Document ID:** AMPEL360-02-00-00-META-DOCID  
**Version:** 1.0.0  
**Effective Date:** 2025-09-01

## Purpose

This document defines the complete document identification schema for all AMPEL360 documentation.

## Schema Format

**PREFIX-ATA-SECTION-SUBSECTION-TYPE-SEQUENCE**

### Components

**PREFIX (AMPEL360 or Project Code)**
- Standard prefix: `AMPEL360`
- Project-specific codes allowed for special programs

**ATA (2 digits)**
- ATA chapter number (02, 28, 52, etc.)

**SECTION (2 digits)**
- Section within ATA chapter (00, 10, 20, etc.)

**SUBSECTION (2 digits)**
- Subsection detail (00, 01, 02, etc.)

**TYPE (3-10 characters)**
- Document type identifier
- Examples: META, PROC, SPEC, ICD, TEST, TRAIN

**SEQUENCE (3 digits, optional)**
- Sequential number for multiple documents of same type
- Example: 001, 002, 003

## Document Types

| Code | Type | Description |
|------|------|-------------|
| **META** | Meta | Governance, control, management documents |
| **OVERVIEW** | Overview | Conceptual, philosophical documentation |
| **SAFETY** | Safety | Safety analyses, procedures, frameworks |
| **REQ** | Requirements | Requirements specifications |
| **DESIGN** | Design | Design documentation, standards |
| **ICD** | Interface | Interface Control Documents |
| **PROC** | Procedure | Operational procedures |
| **TEST** | Test | Test plans, reports, procedures |
| **TRAIN** | Training | Training materials, courses |
| **QA** | Quality | Quality records, audits, reports |
| **CR** | Change | Change requests |
| **SPEC** | Specification | Technical specifications |

## Examples

```
AMPEL360-02-00-00-META-GOV
│       │  │  │  │    └─ Document name/descriptor
│       │  │  │  └────── Document type
│       │  │  └───────── Subsection
│       │  └──────────── Section  
│       └─────────────── ATA chapter
└─────────────────────── Prefix

AMPEL360-02-32-00-PROC-001
└─ H₂ Refueling Procedure #1

AMPEL360-28-10-00-SPEC-TANK
└─ H₂ Storage Tank Specification

AMPEL360-02-00-05-ICD-001
└─ Interface Control Document #1
```

## Folder-Level Documents

Within 14-folder structure (01_OVERVIEW through 14_META_GOVERNANCE):
- Use folder number as part of context
- Example: Document in 02_SAFETY folder
  - `AMPEL360-02-00-00-SAFETY-FMEA` (not 02_SAFETY in ID)

## Compliance

Complies with:
- ATA iSpec 2200
- S1000D (DMC mapping documented separately)
- ISO 9001 document control
- AMPEL360 internal standards

---

**Document Control:**
- Document ID: AMPEL360-02-00-00-META-DOCID
- Version: 1.0.0
- Status: Released
- Owner: Documentation Manager
