# ATA 24 — Electrical Power (ATA iSpec 2200 SNS Structure)

## Overview

This directory contains the **ATA 24 Electrical Power** system documentation structured according to the **ATA iSpec 2200 Standard Numbering System (SNS)** with S1000D CSDB publication management.

This structure complements the existing OPT-IN Framework organization and provides an alternative view aligned with industry-standard ATA numbering for certification and publication purposes.

## Purpose

The ATA SNS structure enables:
- Compliance with ATA iSpec 2200 standard
- S1000D-based technical publication management
- Industry-standard maintenance manual organization
- Illustrated parts catalog structuring
- Integration with existing aviation documentation systems

## Directory Structure

The structure follows the **ATA SNS subject-level (24-xx-yy)** format where:
- `xx` = **Section** (3rd–4th digits)
- `yy` = **Subject** (5th–6th digits)

### Sections

```text
ATA-24-electrical-power/
├── 24-00-electrical-power-general/          # General information
├── 24-10-generator-drive/                   # Generator drive systems
├── 24-20-ac-generation/                     # AC generation systems
├── 24-30-dc-generation/                     # DC generation systems
├── 24-40-external-power/                    # External power interfaces
├── 24-50-ac-electrical-load-distribution/   # AC load distribution
├── 24-60-dc-electrical-load-distribution/   # DC load distribution
└── 24-70-primary-and-secondary-power/       # Emergency/standby power
```

### Subject Structure

Each section contains subjects following the pattern `24-xx-yy-<subject-name>/`:
- `24-xx-00-<section-name>/` — General subject for each section
- `24-xx-YY-<subject-name>/` — Additional subjects as defined by ATA SNS extract

### SSOT and PUB Structure

Each subject directory contains:

```text
24-xx-yy-<subject-name>/
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

- **OPT-IN Framework** (`24-00_GENERAL`, `24-10_Operations`, etc.): Project lifecycle and development structure
- **ATA SNS** (`ATA-24-electrical-power/`): Publication and certification structure

Both structures reference the same underlying systems and components but organize them for different purposes.

## ATA 24 Sections Overview

### 24-00 Electrical Power — General
Chapter-level scope, electrical architecture philosophy (including H₂ fuel cell + battery buffering), domains, redundancy, dispatch, and certification/verification framing.

**Subjects:**
- 24-00-00: Chapter overview
- 24-00-01: Scope & boundaries
- 24-00-02: Electrical architecture overview (AC/LVDC/HVDC concept)
- 24-00-03: Power quality & limits
- 24-00-04: Load classification
- 24-00-05: Redundancy & dispatch philosophy
- 24-00-06: Interfaces & dependencies
- 24-00-07: Monitoring & BITE overview
- 24-00-08: Safety & compliance basis
- 24-00-10: Verification strategy
- 24-00-90: Program delta: Fuel-cell transient constraints & buffering strategy
- 24-00-91: Program delta: HV architecture & EMI environment
- 24-00-92: Program delta: Thermal/power derating coordination

### 24-10 Generator Drive
Mechanical/electromechanical drive chain that produces generator shaft power and its control/monitoring. For hydrogen-electric, this often maps to motor-generator coupling, gearboxes, or dedicated turbogenerators/APU-equivalent.

**Subjects:**
- 24-10-00: Generator drive overview
- 24-10-01: Drive architecture & variants
- 24-10-02: Mechanical interfaces
- 24-10-03: Control & regulation interface
- 24-10-04: Cooling/lubrication interfaces
- 24-10-05: Monitoring & protections
- 24-10-06: Maintenance & inspection tasks
- 24-10-10: Verification & qualification
- 24-10-90: Program delta: Electric MG transient torque limits / regen constraints

### 24-20 AC Generation
AC generation sources and conditioning (variable frequency vs constant frequency, inverter-based AC, regulation, paralleling rules).

**Subjects:**
- 24-20-00: AC generation overview
- 24-20-01: AC sources (main, APU/aux, emergency)
- 24-20-02: Regulation & control
- 24-20-03: Paralleling / transfer logic
- 24-20-04: AC power quality
- 24-20-05: Protections
- 24-20-07: BITE & fault isolation
- 24-20-10: Verification
- 24-20-90: Program delta: Inverter-dominated grid stability

### 24-30 DC Generation
DC generation and conversion chain (rectifiers, DC/DC, HVDC buses, battery charging, fuel cell DC coupling).

**Subjects:**
- 24-30-00: DC generation overview
- 24-30-01: DC sources (fuel cell stacks, rectified AC, batteries)
- 24-30-02: Conversion stages
- 24-30-03: Battery charging & energy buffering control
- 24-30-04: DC quality
- 24-30-05: Protections
- 24-30-07: BITE & diagnostics
- 24-30-10: Verification
- 24-30-90: Program delta: HVDC insulation monitoring & fault containment strategy

### 24-40 External Power
Ground power interfaces (AC and/or DC), connectors, interlocks, contactors, acceptance limits, and safety constraints.

**Subjects:**
- 24-40-00: External power overview
- 24-40-01: Interfaces & connectors
- 24-40-02: Acceptance criteria
- 24-40-03: Switching & contactors
- 24-40-04: Ground safety & HV protocols
- 24-40-07: Monitoring & BITE
- 24-40-10: Verification
- 24-40-90: Program delta: DC fast-charge / high-power ground service constraints

### 24-50 AC Electrical Load Distribution
AC bus architecture, contactors, bus ties, load shedding, essential bus rules, and distribution protections.

**Subjects:**
- 24-50-00: AC distribution overview
- 24-50-01: Bus topology
- 24-50-02: Switching logic
- 24-50-03: Load management & shedding
- 24-50-04: Circuit protection & coordination
- 24-50-07: Monitoring, metering & BITE
- 24-50-10: Verification

### 24-60 DC Electrical Load Distribution
DC buses (LVDC/HVDC), distribution units, contactors/SSPCs, insulation monitoring, fault containment, and load shedding.

**Subjects:**
- 24-60-00: DC distribution overview
- 24-60-01: DC bus topology
- 24-60-02: Switching devices (contactors/SSPCs) and control
- 24-60-03: Load management & shedding
- 24-60-04: Protections & selectivity
- 24-60-05: Grounding/return paths and bonding considerations
- 24-60-07: Monitoring, metering & BITE
- 24-60-10: Verification

### 24-70 Primary & Secondary Power
Emergency/standby/secondary sources and essential distribution strategy (batteries, emergency generation, RAT-equivalent if any, "keep-alive" architecture).

**Subjects:**
- 24-70-00: Primary/secondary power overview
- 24-70-01: Emergency/standby sources
- 24-70-02: Essential power architecture
- 24-70-03: Automatic reconfiguration logic
- 24-70-04: Endurance/energy budgeting
- 24-70-07: Monitoring & BITE
- 24-70-10: Verification

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

## Program Deltas for AMPEL360

The AMPEL360 hydrogen-electric aircraft introduces several program-specific deltas:
- **Fuel Cell Integration**: Transient constraints and buffering strategies (24-00-90)
- **High-Voltage Architecture**: HVDC buses and EMI environment (24-00-91)
- **Thermal Management**: Power derating coordination (24-00-92)
- **Advanced Generation**: Electric motor-generator sets (24-10-90)
- **Inverter Stability**: AC microgrid behavior (24-20-90)
- **HVDC Safety**: Insulation monitoring and fault containment (24-30-90)
- **Ground Services**: DC fast-charge capabilities (24-40-90)

## References

- [ATA iSpec 2200 Extract: ATA Standard Numbering System](https://publications.airlines.org/products/ispec-2200-extract-ata-standard-numbering-system-revision-2024-1)
- [ATA Chapters Reference (Wikipedia)](https://en.wikipedia.org/wiki/ATA_100)
- [ATA Chapters and Sub-chapters](https://itlims-zsis.meil.pw.edu.pl/pomoce/ESL/2016/ATA_Chapters.pdf)
- [Todd Heffley's ATA Chapter Guide](https://toddheffley.com/wordpress/?p=5760)
- S1000D Specification (International specification for technical publications)

## Notes

- Each `24-xx-00-*` directory serves as the "general" subject for its section
- Additional subjects `24-xx-YY-*` should only be added when defined in your ATA SNS extract
- The `PUB/<SUB_ID>/CSDB` structure is self-contained for S1000D publishing
- Configuration files (`bindings.csv`, `csdb.profile.yaml`) should be populated according to project requirements

## Document Control

- **ATA Chapter**: 24
- **Structure Version**: 1.0
- **Standard**: ATA iSpec 2200 SNS / S1000D
- **Status**: Active
- **Repository**: AMPEL360-AIR-T
- **Location**: Integrated with OPT-IN Framework
- **Generated with**: AI assistance (GitHub Copilot), prompted by Amedeo Pelliccia
- **Last Updated**: 2026-01-09
