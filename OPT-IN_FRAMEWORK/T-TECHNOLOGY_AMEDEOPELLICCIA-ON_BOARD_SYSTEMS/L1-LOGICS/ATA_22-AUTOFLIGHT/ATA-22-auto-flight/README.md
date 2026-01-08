# ATA 22 — Auto Flight (ATA iSpec 2200 SNS Structure)

## Overview

This directory contains the **ATA 22 Auto Flight** system documentation structured according to the **ATA iSpec 2200 Standard Numbering System (SNS)** with S1000D CSDB publication management.

This structure complements the existing OPT-IN Framework organization and provides an alternative view aligned with industry-standard ATA numbering for certification and publication purposes.

## Purpose

The ATA SNS structure enables:
- Compliance with ATA iSpec 2200 standard
- S1000D-based technical publication management
- Industry-standard maintenance manual organization
- Illustrated parts catalog structuring
- Integration with existing aviation documentation systems

## Directory Structure

The structure follows the **ATA SNS subject-level (22-xx-yy)** format where:
- `xx` = **Section** (3rd–4th digits)
- `yy` = **Subject** (5th–6th digits)

### Sections

```text
ATA-22-auto-flight/
├── 22-00-auto-flight-general/          # General information
├── 22-10-autopilot/                    # Autopilot systems
├── 22-20-speed-attitude-correction/    # Speed-Attitude Correction
├── 22-30-auto-throttle/                # Auto Throttle systems
├── 22-40-system-monitor/               # System Monitor functions
└── 22-50-aerodynamic-load-alleviating/ # Aerodynamic Load Alleviating
```

### BWB + H₂ Fuel Cell / Electric Context

**ATA 22** is scoped to **flight guidance/automatic flight functions** (autopilot/auto-throttle/monitoring/load alleviation), not primary flight controls, communications, or power generation.

#### Key BWB Deltas:

- **22-00 General**: Architecture, modes philosophy, redundancy concept, integration boundaries, dispatch criteria, maintenance overview. BWB specific: mode logic and limitations tied to BWB envelope (pitch-moment management, trim strategy, high-lift interactions), electrical power quality assumptions (ride-through, brownout behavior), DAL allocation rationale.

- **22-10 Autopilot**: Automatic control laws, engagement/disengagement logic, fail-operational/fail-passive behavior. BWB specific: distributed control effectors (elevons/spoilers/drag devices) coordination and reconfiguration handling; integration with FBW laws and gust response.

- **22-20 Speed–Attitude Correction**: Speed/attitude capture and correction functions. BWB specific: tighter coupling to energy state management (electric propulsion responsiveness, thrust limits, fuel cell transient constraints) and load alleviation constraints.

- **22-30 Auto Throttle**: Autothrottle/autothrust computation and mode logic. BWB H₂-electric specific: thrust command shaping to respect fuel cell dynamics, battery buffering strategy, inverter limits, thermal derates, and distributed propulsion allocation logic.

- **22-40 System Monitor**: Monitoring, built-in tests, fault detection/isolation, mode inhibition. BWB specific: expanded monitoring of cross-domain dependencies (power availability, network health, flight control reconfiguration state), and robust graceful degradation mode tables.

- **22-50 Aerodynamic Load Alleviating**: Gust/load alleviation functions (structural load reduction via control law scheduling). BWB specific: more prominent due to large lifting surfaces and structural bending sensitivities; close integration with FBW and structural monitoring; explicit constraints to avoid adverse aeroelastic excitation.

### Subject Structure

Each section contains subjects following the pattern `22-xx-yy-<subject-name>/`:
- `22-xx-00-<section-name>/` — General subject for each section
- `22-xx-YY-<subject-name>/` — Additional subjects as defined by ATA SNS extract

### SSOT and PUB Structure

Each subject directory contains:

```text
22-xx-yy-<subject-name>/
├── SSOT/                           # Single Source of Truth
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

- **OPT-IN Framework** (`22-00_GENERAL`, `22-10_Operations`, etc.): Project lifecycle and development structure
- **ATA SNS** (`ATA-22-auto-flight/`): Publication and certification structure

Both structures reference the same underlying systems and components but organize them for different purposes.

## Boundary Map (What is NOT ATA 22)

The following systems are **not** part of ATA 22 and belong to other chapters:

- **Flight controls / actuators / FCC for surfaces**: **ATA 27** (Flight Controls)
- **Navigation sensors / GNSS / INS / RNAV**: **ATA 34** (Navigation)
- **Communications (VHF/HF/SATCOM)**: **ATA 23** (Communications)
- **Electrical generation/distribution**: **ATA 24** (Electrical Power)
- **Displays / indicating / warnings**: **ATA 31** (Indicating/Recording)
- **Fire detection/suppression**: **ATA 26** (Fire Protection)
- **IMA / avionics computing platform**: **ATA 42** (Integrated Modular Avionics)
- **FMS** content: Often under **ATA 34-60** (Flight Management Computing) in many schemes

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

## Usage Guidelines

1. **For Certification Documentation**: Use this ATA SNS structure
2. **For Development/Lifecycle**: Use the parent OPT-IN Framework structure
3. **Cross-Reference**: Maintain traceability between both structures

## References

- [ATA iSpec 2200 Extract: ATA Standard Numbering System](https://publications.airlines.org/products/ispec-2200-extract-ata-standard-numbering-system-revision-2024-1)
- [ATA Chapters Reference](https://itlims-zsis.meil.pw.edu.pl/pomoce/ESL/2016/ATA_Chapters.pdf)
- [ATA 100 on Wikipedia](https://en.wikipedia.org/wiki/ATA_100)
- S1000D Specification (International specification for technical publications)

## Notes

- Each `22-xx-00-*` directory serves as the "general" subject for its section
- Additional subjects `22-xx-YY-*` should only be added when defined in your ATA SNS extract
- The `PUB/<SUB_ID>/CSDB` structure is self-contained for S1000D publishing
- Configuration files (`bindings.csv`, `csdb.profile.yaml`) should be populated according to project requirements

## Document Control

- **ATA Chapter**: 22
- **Structure Version**: 1.0
- **Standard**: ATA iSpec 2200 SNS / S1000D
- **Status**: Active
- **Repository**: AMPEL360-AIR-T
- **Location**: Integrated with OPT-IN Framework
- **Last Updated**: 2026-01-08
- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
