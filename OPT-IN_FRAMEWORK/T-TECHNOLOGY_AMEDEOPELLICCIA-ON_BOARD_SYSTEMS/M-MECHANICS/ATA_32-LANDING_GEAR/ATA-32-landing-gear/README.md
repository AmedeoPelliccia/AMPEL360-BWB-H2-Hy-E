# SPDX-License-Identifier: Apache-2.0
# SPDX-FileCopyrightText: 2026 Amedeo Pelliccia <amedeo.pelliccia@icloud.com>
# ATA 32 — Landing Gear (iSpec 2200 Structure — Option B: Distributed Electro-Hydraulic)

## Overview

This directory contains the ATA 32 Landing Gear system documentation following the ATA iSpec 2200 chapter/section structure. The CSDB (Common Source Database) lives at the sub-subject (sys-sec-sbj) level with both PUB (S1000D) and SSOT (Single Source of Truth) alongside each other.

> **Architecture Option B:** This landing gear system uses the **Distributed Electro-Hydraulic** architecture featuring:
> - **EHPU** (Electro-Hydraulic Power Units) — local hydraulic power generation
> - **EHA** (Electro-Hydrostatic Actuators) — self-contained actuation units
> - **EHB** (Electro-Hydraulic Brakes) — local braking with metering and accumulators
> - **Short hydraulic lines** — minimal central hydraulic dependency
> - **Explicit interfaces to ATA 24** (electrical power, peaks, shedding), **ATA 31** (indication), and **ATA 45** (CMS/BITE)

## Structure

This follows the canonical ATA iSpec 2200 breakdown for ATA 32:

### 32-00 — Landing Gear General
System overview, Option B architecture philosophy, interfaces (ATA 24/31/45), local hydraulic circuits, safety (WOW, brake-hot, towing/jacking), and fault containment.

### 32-10 — Main Gear and Doors
Main landing gear (MLG) structure, shock strut, local actuation (PCU/EHA), doors, locks, position sensing, and WOW.

### 32-20 — Nose Gear and Doors
Nose landing gear (NLG) structure, centering/shimmy, local actuation (PCU/EHA), doors, locks, towing/jacking provisions.

### 32-30 — Extension and Retraction
Core Option B functionality: EHPU local power units, components (motor, pump, reservoir, accumulator), manifolds, sequencing, alternate/emergency extension, and interfaces to ATA 24/31/45.

### 32-40 — Wheels and Brakes
EHB (Electro-Hydraulic Braking) architecture, wheels/tires/pressure monitoring, brake control unit (antiskid, autobrake), temperature monitoring, parking/emergency braking.

### 32-50 — Steering
Electro-hydraulic steering actuator (EHA module), control laws, feedback sensors, centering, shimmy damping, tow mode/reversion.

### 32-60 — Position Indication and Warning
Gear position sensing, WOW/squat switches, EHPU/EHB health monitoring, warnings/cautions, BITE export to CMS (ATA 45).

### 32-70 — Supplementary Gear
Ground handling (pins, jacks, towbar), EHPU fluid servicing, nitrogen servicing (accumulators, shock struts), LRU replacement procedures.

## Directory Organization

Each sub-subject folder (e.g., `32-10-20-mlg-local-actuation-pcus-eha-and-sensors/`) contains:

- **SSOT/**: Single Source of Truth - Engineering lifecycle data (LC01–LC14)
- **PUB/**: Publication views including S1000D CSDB structure
- **00_INDEX.md**: Index file for the sub-subject

## SSOT Lifecycle Structure (LC01–LC14)

Each SSOT directory contains the complete product lifecycle:

1. **LC01_PROBLEM_STATEMENT**: Requirements genesis and problem definition
2. **LC02_SYSTEM_REQUIREMENTS**: Requirements, traceability, interfaces (ICDs for ATA 24, ATA 29, ATA 31, ATA 45)
3. **LC03_DESIGN_MODELS**: Architecture, schematics, EHPU/EHA/EHB selection, EWIS
4. **LC04_ENGINEERING_ANALYSIS**: Loads sizing, EHPU power budget, thermal, reliability, EMI/HIRF/Lightning
5. **LC05_INTEGRATION_TESTING_PROTOTYPING**: Test procedures, reports, rigs
6. **LC06_QUALITY**: Inspection plans, NCR, supplier quality
7. **LC07_SAFETY_SECURITY**: FHA, PSSA, SSA, hazard logs (WOW, brake-hot, fault containment)
8. **LC08_CERTIFICATION_FIRST_FLIGHT**: Compliance matrix, MoC, flight test support
9. **LC09_GREEN_BASELINES**: Materials and emissions
10. **LC10_INDUSTRIALIZATION_CM**: MBOM/PBOM, CM baselines, work instructions
11. **LC11_OPERATIONS**: Operational limitations
12. **LC12_SUPPORT_SERVICES**: Service bulletins
13. **LC13_MRO_SUSTAINMENT**: MSG-3 tasks
14. **LC14_RETIREMENT_CIRCULARITY**: Disposal and recycling

## PUB Structure (S1000D)

Each PUB directory contains S1000D CSDB organization:

- **AMM/CSDB/**: Aircraft Maintenance Manual Common Source Database
  - **DM/**: Data Modules (040A description, 520A test, 720A remove/install, 730A fault isolation, 940A SW config)
  - **PM/**: Publication Modules (publication structure)
  - **DML/**: Data Module Lists (organization)
  - **ICN/**: Illustrations and graphics (SVG format)
  - **BREX/**: Business Rules Exchange (validation rules)
  - **COMMON/**: Reusable content (warnings, cautions)
  - **APPLICABILITY/**: Product variant applicability

## ATA Cross-References

| ATA Chapter | Interface Type | Description |
|-------------|----------------|-------------|
| [ATA 24 — Electrical Power](../../E3-ELECTRONICS/ATA_24-ELECTRICAL_POWER/) | Power Source | EHPU motor power, peak loads, shedding logic |
| [ATA 29 — Hydraulic Power](../ATA_29-HYDRAULIC_POWER/) | Minimal | Option B minimizes central hydraulic dependency |
| [ATA 31 — Indicating/Recording](../../I-INFORMATION_INTELLIGENCE_INTERFACES/ATA_31-INDICATING_RECORDING/) | Indication | Gear position, warnings, cautions |
| [ATA 45 — Central Maintenance](../../I-INFORMATION_INTELLIGENCE_INTERFACES/ATA_45-CENTRAL_MAINTENANCE/) | Diagnostics | BITE data export, fault codes, trends |

## Document Control

- **ATA Chapter**: 32
- **Standard**: ATA iSpec 2200 / S1000D 5.0
- **Model**: AMPEL360AT
- **Architecture**: Option B — Distributed Electro-Hydraulic (EHPU/EHA/EHB)
- **Status**: Active Development
- **Last Updated**: 2026-01-10

---

## References

- [ATA iSpec 2200 Specification](https://publications.airlines.org/)
- [S1000D Issue 5.0](http://www.s1000d.org/)
- [ATA Chapters Guide](https://itlims-zsis.meil.pw.edu.pl/pomoce/ESL/2016/ATA_Chapters.pdf)
