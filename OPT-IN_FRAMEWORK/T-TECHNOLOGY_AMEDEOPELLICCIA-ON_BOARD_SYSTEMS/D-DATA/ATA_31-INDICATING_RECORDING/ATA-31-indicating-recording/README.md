# ATA 31 — Indicating/Recording (ATA iSpec 2200 SNS Structure)

## Overview

This directory contains the **ATA 31 Indicating/Recording** system documentation structured according to the **ATA iSpec 2200 Standard Numbering System (SNS)** with S1000D CSDB publication management.

This structure complements the existing OPT-IN Framework organization and provides an alternative view aligned with industry-standard ATA numbering for certification and publication purposes.

## Purpose

The ATA SNS structure enables:
- Compliance with ATA iSpec 2200 standard
- S1000D-based technical publication management
- Industry-standard maintenance manual organization
- Illustrated parts catalog structuring
- Integration with existing aviation documentation systems

## Directory Structure

The structure follows the **ATA SNS subject-level (31-xx-yy)** format where:
- `xx` = **Section** (3rd–4th digits)
- `yy` = **Subject** (5th–6th digits)

### Sections

```text
ATA-31-indicating-recording/
├── 31-00-indicating-recording-general/           # General information
├── 31-10-instrument-and-control-panels/          # Panel systems
├── 31-20-independent-instruments/                # Standby instruments
├── 31-30-recorders/                              # Flight data & voice recorders
├── 31-40-central-computers/                      # Data concentrators & IMA
├── 31-50-central-warning-systems/                # CAS/ECAM/EICAS alerting
├── 31-60-central-display-systems/                # PFD/ND/MFD displays
├── 31-70-automatic-data-reporting-systems/       # ACMS & health monitoring
└── ASSETS/                                       # Diagrams, models, and shared resources
```

### Subject Structure

Each section contains subjects following the pattern `31-xx-yy-<subject-name>/`:
- `31-xx-00-<section-name>/` — General subject for each section
- `31-xx-YY-<subject-name>/` — Additional subjects as defined by ATA SNS extract

### SSOT and PUB Structure

Each subject directory contains:

```text
31-xx-yy-<subject-name>/
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
    │   └── ...
    └── IPC/                        # Illustrated Parts Catalog
        └── (same structure as AMM)
```

## Relationship to OPT-IN Framework

This ATA SNS structure coexists with the OPT-IN Framework organization:

- **OPT-IN Framework** (`31-00_GENERAL`, `31-10_Operations`, etc.): Project lifecycle and development structure
- **ATA SNS** (`ATA-31-indicating-recording/`): Publication and certification structure

Both structures reference the same underlying systems and components but organize them for different purposes.

## ATA 31 Sections Overview

### 31-00 Indicating/Recording — General
Chapter-level scope, system architecture (sensors → concentrators → alerts → displays → recorders), HMI philosophy, event/time model, and interfaces with related ATA chapters.

**Subjects:**
- 31-00-00: General overview
- 31-00-10: System architecture and dataflow
- 31-00-20: HMI philosophy, symbology, colors, and priorities
- 31-00-30: Time sync, stamping, and event model
- 31-00-40: Interfaces (ATA 22/24/42/45/46)
- 31-00-90: Configuration baselines and compliance

### 31-10 Instrument and Control Panels
Physical panels (overhead, glareshield, pedestal, maintenance), annunciators, lighting/dimming, and wiring/BITE.

**Subjects:**
- 31-10-00: Panels general
- 31-10-10: Overhead and system control panels
- 31-10-20: Glareshield master warning/caution and annunciators
- 31-10-30: Center pedestal audio alert controls
- 31-10-40: Maintenance panels and test controls
- 31-10-50: Panel lighting, dimming, and fail indications

### 31-20 Independent Instruments
Standby/independent displays and instruments, independent power, clock/chronometer, and time synchronization.

**Subjects:**
- 31-20-00: Independent instruments general
- 31-20-10: Standby flight display and power source
- 31-20-20: Standby attitude, airspeed, altitude, and compass
- 31-20-30: Clock, time of day, chronometer, and time sync
- 31-20-40: Independent warning indication lamps

### 31-30 Recorders
FDR, CVR, QAR, DAU, data offload interfaces, crash survivability, and dataset traceability (FOQA/health).

**Subjects:**
- 31-30-00: Recorders general
- 31-30-10: Flight data recorder (FDR) and DAU
- 31-30-20: Cockpit voice recorder (CVR)
- 31-30-30: Quick access recorder (QAR) / FOQA
- 31-30-40: Data loading, download, and offload interfaces
- 31-30-50: Crash survivability, location, power, and tests

### 31-40 Central Computers
Data concentrators, signal acquisition, alert logic engine, display rendering, IMA hosting/partitioning, and BITE/diagnostics.

**Subjects:**
- 31-40-00: Central computers general
- 31-40-10: Data concentrators and signal acquisition
- 31-40-20: Alert logic hosting and prioritization engine
- 31-40-30: Display management and rendering control
- 31-40-40: Partitioning, IMA hosting, and resource budgets
- 31-40-50: BITE diagnostics and maintenance interfaces

### 31-50 Central Warning Systems
CAS/ECAM/EICAS message model, priorities/inhibits, aural alerts, master warning/caution, checklists/procedural cues, and alert consistency.

**Subjects:**
- 31-50-00: Central warning general
- 31-50-10: CAS/ECAM/EICAS message model and priorities
- 31-50-20: Aural warnings (voice, gong, chime) and inhibits
- 31-50-30: Master warning/caution lights and reset logic
- 31-50-40: Checklists and crew procedural cues integration
- 31-50-50: Fault isolation and alert consistency rules

### 31-60 Central Display Systems
Display units (PFD/ND/MFD), synoptics, source switching, degraded modes/reversion, HUD/EVS integration, and calibration/test.

**Subjects:**
- 31-60-00: Central display general
- 31-60-10: PFD/ND/MFD display units and degraded modes
- 31-60-20: Engine/system pages and synoptics
- 31-60-30: Display source switching, reversion, and standby
- 31-60-40: HUD or EVS display integration
- 31-60-50: Maintenance tests, color calibration, and BITE

### 31-70 Automatic Data Reporting Systems
ACMS logging, event triggers, health monitoring KPIs, data links integration, cybersecurity/integrity, and ground tools/export.

**Subjects:**
- 31-70-00: Automatic data reporting general
- 31-70-10: ACMS logging, event triggers, and report sets
- 31-70-20: Health monitoring KPIs and condition reporting
- 31-70-30: Data links (WiFi/SATCOM/VHF) integration boundaries
- 31-70-40: Cybersecurity, integrity, and evidence hash chains
- 31-70-50: Ground tools, export packaging, and onboarding

## S1000D CSDB Structure

The **CSDB (Common Source Database)** follows the S1000D standard and contains:

- **DM** (Data Modules): Individual documentation units
- **PM** (Publication Modules): Publication structure definitions
- **DML** (Data Module Lists): Lists referencing data modules
- **ICN** (Illustrations): Graphics, diagrams, and illustrations
- **BREX** (Business Rules Exchange): Validation rules and constraints
- **COMMON** (Common Information Sets): Reusable content
- **APPLICABILITY** (Applicability Statements): Product/variant applicability

## Cross-References

### Related ATA Chapters
- **ATA 22**: Auto Flight (alert inhibits, mode annunciation)
- **ATA 24**: Electrical Power (power quality, time sync)
- **ATA 42**: Integrated Modular Avionics (IMA hosting, partitioning)
- **ATA 45**: Central Maintenance System (BITE, fault codes)
- **ATA 46**: Information Systems (datalink, reporting)

### Related OPT-IN Framework Sections
- **31-00_GENERAL**: Lifecycle development documentation
- **31-20_Subsystems**: Functional subsystem design details
- **31-40_Software**: Display and alerting control algorithms
- **31-90_Tables_Schemas_Diagrams**: Data tables and documentation

## References

1. **ATA iSpec 2200 Extract**: [Standard Numbering System](https://publications.airlines.org/products/ispec-2200-extract-ata-standard-numbering-system-revision-2024-1)
2. **ATA 100 Overview**: [Wikipedia](https://en.wikipedia.org/wiki/ATA_100)
3. **ATA Chapters Reference**: [ITLIMS ZSIS](https://itlims-zsis.meil.pw.edu.pl/pomoce/ESL/2016/ATA_Chapters.pdf)

## Document Control

| Field | Value |
|-------|-------|
| **Document Type** | ATA SNS Structure |
| **ATA Chapter** | 31 — Indicating/Recording |
| **Standard** | ATA iSpec 2200 SNS / S1000D Issue 5.0 |
| **Project** | AMPEL360-AIR-T |
| **Model** | BWB-H2-Hy-E |
| **Status** | Active |
| **Version** | 1.0 |
| **Created** | 2026-01-10 |
| **Generated with** | AI assistance (GitHub Copilot), prompted by Amedeo Pelliccia |
| **Repository** | github.com/AmedeoPelliccia/AMPEL360-AIR-T |
