# ATA 23 — Communications (ATA iSpec 2200 SNS Structure)

## Overview

This directory contains the **ATA 23 Communications** system documentation structured according to the **ATA iSpec 2200 Standard Numbering System (SNS)** with S1000D CSDB publication management.

This structure complements the existing OPT-IN Framework organization and provides an alternative view aligned with industry-standard ATA numbering for certification and publication purposes.

## Purpose

The ATA SNS structure enables:
- Compliance with ATA iSpec 2200 standard
- S1000D-based technical publication management
- Industry-standard maintenance manual organization
- Illustrated parts catalog structuring
- Integration with existing aviation documentation systems

## Directory Structure

The structure follows the **ATA SNS subject-level (23-xx-yy)** format where:
- `xx` = **Section** (3rd–4th digits)
- `yy` = **Subject** (5th–6th digits)

### Sections

```text
ATA-23-communications/
├── 23-00-communications-general/
├── 23-10-speech-communications/
├── 23-15-satcom/
├── 23-20-data-transmission-and-automatic-calling/
├── 23-30-passenger-address-entertainment-comfort/
├── 23-40-interphone/
├── 23-50-audio-integrating/
├── 23-60-static-discharging/
├── 23-70-audio-and-video-monitoring/
└── 23-80-integrated-automatic-tuning/
```

### Subject Structure

Each section contains subjects following the pattern `23-xx-yy-<subject-name>/`:
- `23-xx-00-<section-name>/` — General subject for each section
- `23-xx-YY-<subject-name>/` — Additional subjects as defined by ATA SNS extract

### SSOT and PUB Structure

Each subject directory contains:

```text
23-xx-yy-<subject-name>/
├── SSOT/                           # Single Source of Truth
│   ├── LC01_Requirements/
│   ├── LC02_System_Requirements/
│   ├── LC03_Design/
│   ├── LC04_Analysis/
│   ├── LC05_VnV/
│   ├── LC06_Quality/
│   ├── LC07_Safety/
│   └── LC08_Certification/
└── PUB/                            # Publication views
    ├── AMM/                        # Aircraft Maintenance Manual
    │   ├── CSDB/                   # Common Source Database
    │   │   ├── DM/                 # Data Modules
    │   │   ├── PM/                 # Publication Modules
    │   │   ├── DML/                # Data Module Lists
    │   │   ├── ICN/                # Illustrations/Graphics
    │   │   ├── BREX/               # Business Rules Exchange
    │   │   ├── COMMON/             # Common information sets
    │   │   └── APPLICABILITY/      # Applicability statements
    │   ├── EXPORT/                 # Export outputs
    │   ├── bindings.csv            # Publication bindings
    │   └── csdb.profile.yaml       # CSDB profile configuration
    └── IPC/                        # Illustrated Parts Catalog
        └── (same structure as AMM)
```

## Relationship to OPT-IN Framework

This ATA SNS structure coexists with the OPT-IN Framework organization:

- **OPT-IN Framework** (`23-00_GENERAL`, `23-10_Operations`, etc.): Project lifecycle and development structure
- **ATA SNS** (`ATA-23-communications/`): Publication and certification structure

Both structures reference the same underlying systems and components but organize them for different purposes.

## S1000D CSDB Structure

The **CSDB (Common Source Database)** follows the S1000D standard and contains:

- **DM** (Data Modules): Individual documentation units
- **PM** (Publication Modules): Publication structure definitions
- **DML** (Data Module Lists): Lists referencing data modules
- **ICN** (Illustrations): Graphics, diagrams, and illustrations
- **BREX** (Business Rules Exchange): Validation rules and constraints
- **COMMON** (Common Information Sets): Reusable content
- **APPLICABILITY** (Applicability Statements): Product/variant applicability

## Publication Views

Each subject can have multiple publication views (SUB_ID):
- **AMM**: Aircraft Maintenance Manual
- **IPC**: Illustrated Parts Catalog
- Additional publications can be added as needed (e.g., WDM, CMM, FIM, SRM)

## ATA 23 SNS Sections

### 23-00 Communications — General
Chapter-level scope, architecture, partitioning, standards, redundancy, dispatch philosophy, and cross-system dependencies for aircraft communications.

### 23-10 Speech Communications
Aircraft voice communications (VHF, HF where applicable), crew audio endpoints, and operational voice routing (ATC, company, inter-crew voice paths).

### 23-15 SATCOM
Satellite communications terminals and services supporting voice and/or datalink, including antenna/steering constraints and service availability management.

### 23-20 Data Transmission and Automatic Calling
Aircraft datalink and "automatic calling" functions (ACARS/ATSU-related flows and SELCAL), message routing, and operational communications automation.

### 23-30 Passenger Address, Entertainment and Comfort
Cabin communications/services (PA, passenger information, IFE/comfort comms where included in ATA 23 scope).

### 23-40 Interphone
Interphone services (cockpit-to-cabin, maintenance/service interphone), call signaling, and station management.

### 23-50 Audio Integrating
Audio management/integration: selection, mixing, routing, recording feeds, sidetone, and crew audio control logic.

### 23-60 Static Discharging
Static discharge provisions (wicks, bonding/grounding practices as scoped to comms performance protection).

### 23-70 Audio and Video Monitoring
Monitoring/recording or surveillance-type functions where treated under ATA 23, including cabin monitoring feeds and audio/video distribution to crew stations.

### 23-80 Integrated Automatic Tuning
Automatic tuning/selection support (radio tuning integration, frequency management aids) where implemented.

## BWB + H₂ Fuel-Cell/Electric Program Considerations

- **EMC/EMI and conducted noise**: Higher-risk environment due to HV switching/inverters; make this a first-class requirement and verification stream.
- **Antenna placement on BWB**: Different blockage/shadowing and structural integration constraints; treat as design drivers for 23-10/15.
- **Domain segregation**: Keep ATA 23 functional scope clean; place cybersecurity controls under B30 governance (or ATA 46 if used), and cross-reference from ATA 23.

## Usage Guidelines

1. **For Certification Documentation**: Use this ATA SNS structure
2. **For Development/Lifecycle**: Use the parent OPT-IN Framework structure
3. **Cross-Reference**: Maintain traceability between both structures

## References

- [ATA iSpec 2200 Extract: ATA Standard Numbering System](https://publications.airlines.org/products/ispec-2200-extract-ata-standard-numbering-system-revision-2024-1)
- [ATA Chapters and Sub-chapters Reference](https://itlims-zsis.meil.pw.edu.pl/pomoce/ESL/2016/ATA_Chapters.pdf)
- [ATA Standard Numbering System](https://www.aviationhunt.com/ata-standard-numbering-system/)
- S1000D Specification (International specification for technical publications)

## Notes

- Each `23-xx-00-*` directory serves as the "general" subject for its section
- Additional subjects `23-xx-YY-*` should only be added when defined in your ATA SNS extract
- The `PUB/<SUB_ID>/CSDB` structure is self-contained for S1000D publishing
- Configuration files (`bindings.csv`, `csdb.profile.yaml`) should be populated according to project requirements

## Document Control

- **ATA Chapter**: 23
- **Structure Version**: 1.0
- **Standard**: ATA iSpec 2200 SNS Extract (Revision 2024-1) / S1000D
- **Status**: Active
- **Repository**: AMPEL360-AIR-T
- **Location**: Integrated with OPT-IN Framework
- **Last Updated**: 2026-01-09
- **Generated with AI assistance**: GitHub Copilot, prompted by Amedeo Pelliccia
