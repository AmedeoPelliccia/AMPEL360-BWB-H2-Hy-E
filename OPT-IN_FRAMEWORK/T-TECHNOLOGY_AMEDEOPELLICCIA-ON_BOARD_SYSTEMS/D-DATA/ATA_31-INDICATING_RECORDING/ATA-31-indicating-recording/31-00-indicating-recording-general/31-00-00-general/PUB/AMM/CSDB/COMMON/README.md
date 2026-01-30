# COMMON Directory — ATA 31-00-00 General

## Purpose

Contains **S1000D-compliant Common Information Sets** - reusable, atomic content modules that are referenced by multiple Data Modules (DMs) and Publication Modules (PMs) to ensure consistency, avoid duplication, and maintain a single source of truth for critical information across the Aircraft Maintenance Manual (AMM).

## Role in SSOT + PUB Model

The `COMMON/` directory serves as the **controlled content primitives layer** within the Common Source Database (CSDB):

- **Atomic & Reusable**: Each COMMON file represents a single, well-defined information object
- **Non-structural**: COMMON files contain content, not publication structure (PMs define structure)
- **Referenced, Not Embedded**: Data Modules reference COMMON files via `<commonInfoRef>` tags
- **Authoritative**: COMMON files are the single source of truth for warnings, definitions, procedures, and standards
- **Traceable**: All COMMON files are versioned and change-controlled per S1000D requirements

## Directory Contents

This COMMON directory contains 13 reusable information sets organized into 5 categories:

### 1. Safety & Operational Statements (3 files)

Critical safety warnings applicable to all ATA 31 maintenance and operational procedures:

| File | ID | Description |
|------|-----|-------------|
| `COM-AMPEL360AT-SAFETY-GENERAL-WARNINGS_EN-US_001-00.XML` | W001-W005 | General safety warnings for indicating and recording systems |
| `COM-AMPEL360AT-SAFETY-ELECTRICAL-HAZARDS_EN-US_001-00.XML` | W101-W105 | Electrical hazard warnings including high voltage, ESD, and lightning protection |
| `COM-AMPEL360AT-SAFETY-DATA-INTEGRITY_EN-US_001-00.XML` | W201-W206 | Data integrity, cybersecurity, and FDR/CVR handling warnings |

**Referenced By**: DMC-...-040A, DMC-...-520A, DMC-...-520B, DMC-...-730A, DMC-...-940A

### 2. Standard Definitions & Terminology (3 files)

Single source of truth for cockpit indication language and recording system terminology:

| File | ID | Description |
|------|-----|-------------|
| `COM-AMPEL360AT-DEFINITION-INDICATIONS_EN-US_001-00.XML` | D001-D012 | Definitions of indications, alerts, messages, warnings, cautions, PFD, MFD, EICAS, ECAM |
| `COM-AMPEL360AT-DEFINITION-RECORDING-LOGIC_EN-US_001-00.XML` | D101-D111 | Recording terminology: FDR, CVR, QAR, data frames, parameters, snapshots, logging |
| `COM-AMPEL360AT-DEFINITION-BIT-STATUS_EN-US_001-00.XML` | D201-D212 | Built-In Test definitions: BIT, CBIT, PBIT, IBIT, fault codes, isolation, NFF |

**Referenced By**: DMC-...-040A, DMC-...-520A, DMC-...-730A, DMC-...-940A

### 3. Human-Machine Interface (HMI) Conventions (3 files)

Standards ensuring consistency across displays and indications per SAE ARP4102, ARINC 661:

| File | ID | Description |
|------|-----|-------------|
| `COM-AMPEL360AT-HMI-COLOR-CODING_EN-US_001-00.XML` | HMI-COLOR-001 to 003 | Display color standards (red=warning, amber=caution, etc.), contrast, accessibility |
| `COM-AMPEL360AT-HMI-SYMBOLS-LEGEND_EN-US_001-00.XML` | HMI-SYM-001 to 004 | Standard symbology, icons, text fonts for cockpit displays |
| `COM-AMPEL360AT-HMI-PRIORITY-LEVELS_EN-US_001-00.XML` | HMI-PRI-001 to 005 | Alert priority classification, suppression logic, aural standards, acknowledgement |

**Referenced By**: DMC-...-040A, DMC-...-730A

### 4. Standard Maintenance Practices (2 files)

ATA-agnostic maintenance procedures used across multiple systems:

| File | ID | Description |
|------|-----|-------------|
| `COM-AMPEL360AT-MAINT-POWER-ON-OFF_EN-US_001-00.XML` | P001-P003 | Aircraft power-up/power-down procedures, selective power application |
| `COM-AMPEL360AT-MAINT-DATA-BUS-CONNECTION_EN-US_001-00.XML` | P101-P104 | Data bus connector inspection, ARINC 429/664 testing, troubleshooting |

**Referenced By**: DMC-...-520A, DMC-...-520B, DMC-...-730A, DMC-...-940A

### 5. Software & Data Handling Constraints (2 files)

Shared rules for avionics data integrity per DO-178C, DO-326A, ED-202A:

| File | ID | Description |
|------|-----|-------------|
| `COM-AMPEL360AT-SW-DATA-HANDLING-GENERAL_EN-US_001-00.XML` | SW-DH-001 to 004 | Software loading security, data download/handling, integrity validation, traceability |
| `COM-AMPEL360AT-SW-CONFIGURATION-CONTROL_EN-US_001-00.XML` | SW-CC-001 to 004 | Configuration identification, change management, status accounting, CCB procedures |

**Referenced By**: DMC-...-520A, DMC-...-940A

## Naming Convention

All COMMON files follow S1000D Issue 5.0 naming standards:

```
COM-[ModelID]-[Type]-[Subtype]_[Lang]-[Country]_[Issue]-[InWork].XML
```

**Example**: `COM-AMPEL360AT-SAFETY-GENERAL-WARNINGS_EN-US_001-00.XML`

- **COM**: Common Information Repository indicator
- **AMPEL360AT**: Model Identification Code (AMPEL360 AIR-T)
- **SAFETY-GENERAL-WARNINGS**: Type and subtype describing content
- **EN-US**: Language (English) and country (United States)
- **001-00**: Issue number 001, in-work number 00 (released)

## Usage in Data Modules

Data Modules reference COMMON files using `<commonInfoRef>` or `<commonRepository>` references:

```xml
<commonInfoRef>
  <infoEntityIdent>
    <infoEntityCode>COM-AMPEL360AT-SAFETY-GENERAL-WARNINGS_EN-US_001-00</infoEntityCode>
  </infoEntityIdent>
</commonInfoRef>
```

## Governance & BREX Expectations

COMMON modules must comply with the following Business Rules Exchange (BREX) constraints:

### Mandatory Requirements

- ✅ **Must** be language-scoped (EN-US, FR-FR, etc.)
- ✅ **Must** be referenced, never embedded directly in DMs
- ✅ **Must** include proper S1000D XML schema declarations
- ✅ **Must** include document control metadata (version, date, author, status)

### Prohibited Content

- ❌ **Must NOT** contain ATA-specific task steps or maintenance sequences
- ❌ **Must NOT** include `<proceduralStep>` with task logic (use general practice statements only)
- ❌ **Must NOT** contain product-specific configuration data (use APPLICABILITY for that)

### Change Control

- 📝 **Must** include `<reasonForUpdate>` on every revision
- 📝 **Must** maintain version history and traceability
- 📝 **Must** undergo CCB approval for changes affecting safety or certification

## Relationship to Other CSDB Elements

```
┌──────────────────────────────────────────────────────────┐
│                    Publication (PM)                      │
│          Defines structure and organization              │
└────────────┬─────────────────────────────────────────────┘
             │ references
             ▼
┌──────────────────────────────────────────────────────────┐
│              Data Module List (DML)                      │
│        Controlled grouping of related DMs                │
└────────────┬─────────────────────────────────────────────┘
             │ contains
             ▼
┌──────────────────────────────────────────────────────────┐
│              Data Modules (DM)                           │
│      ATA-specific maintenance procedures & content       │
└────────────┬─────────────────────────────────────────────┘
             │ references via <commonInfoRef>
             ▼
┌──────────────────────────────────────────────────────────┐
│         COMMON Information Sets (YOU ARE HERE)           │
│      Reusable knowledge atoms, definitions, warnings     │
└──────────────────────────────────────────────────────────┘
```

## Cross-ATA Reuse

These COMMON files may be referenced by other ATA chapters:

- **ATA 22** (Auto Flight): References HMI conventions, BIT definitions
- **ATA 23** (Communications): References data bus procedures, electrical hazards
- **ATA 34** (Navigation): References software configuration control, HMI standards

## Standards Compliance

All COMMON files comply with:

- **S1000D Issue 5.0**: Technical publication standard
- **ATA iSpec 2200**: Chapter structure and numbering
- **SAE ARP4102/6/7**: Display design and crew alerting guidelines
- **ARINC 661**: Cockpit display system interfaces
- **DO-178C**: Software development assurance
- **DO-326A / ED-202A**: Airworthiness security process
- **CS-25.1322**: Flight crew alerting (EASA)
- **14 CFR Part 25**: Airworthiness standards (FAA)

## Validation

All XML files have been validated against:

- S1000D Issue 5.0 XML Schema (comrep.xsd)
- AMPEL360-AIR-T BREX rules (BREX-AMPEL360AT-AIR-T_001-00.XML)
- Project-specific naming conventions

## Future Enhancements

Potential additions to this COMMON directory:

- Tool specifications for specialized test equipment
- Abbreviations and acronyms repository
- Notes and operational tips repository
- Cross-reference maps between ATA chapters

## Document Control

- **Directory**: COMMON
- **Subject**: 31-00-00-general (Indicating & Recording - General)
- **Publication**: AMM (Aircraft Maintenance Manual)
- **Standard**: S1000D Issue 5.0
- **Status**: Active
- **Created**: 2026-01-10
- **Last Updated**: 2026-01-10
- **Generated with**: AI assistance (GitHub Copilot), prompted by **Amedeo Pelliccia**
- **Repository**: AMPEL360-AIR-T
- **Total Files**: 13 XML common information sets
