# SPDX-License-Identifier: Apache-2.0
# SPDX-FileCopyrightText: 2026 Amedeo Pelliccia <amedeo.pelliccia@icloud.com>
# ATA 27 — Flight Controls (iSpec 2200 Structure)

## Overview

This directory contains the ATA 27 Flight Controls system documentation following the ATA iSpec 2200 chapter/section structure. The CSDB (Common Source Database) lives at the sub-subject (sys-sec-sbj) level with both PUB (S1000D) and SSOT (Single Source of Truth) alongside each other.

> **Note (BWB mapping):** BWB (Blended Wing Body) aircraft configurations may use non-conventional control surfaces such as elevons, split surfaces, or drag rudders. Even with these alternative control surface arrangements, content is indexed into these standard ATA sections for maintainability and operator familiarity.

## Structure

This follows the canonical ATA iSpec 2200 breakdown for ATA 27:

### 27-00 — Flight Controls General
System overview, architecture, control laws, inceptors, and general maintenance practices.

### 27-10 — Aileron and Tab
Roll control surfaces including BWB elevon mapping, actuators, and control modes.

### 27-20 — Rudder and Tab
Yaw control surfaces including drag rudder/BWB mapping, actuators, and yaw damper interfaces.

### 27-30 — Elevator and Tab
Pitch control surfaces including BWB elevon mapping, feel/centering systems.

### 27-40 — Horizontal Stabilizer
Trimmable horizontal stabilizer (THS) including BWB configuration mapping.

### 27-50 — Flaps
High-lift trailing edge devices, power drive units, and asymmetry protection.

### 27-60 — Spoiler, Drag Devices, and Variable Aero Fairings
Spoilers, speedbrakes, ground spoilers, and BWB-specific drag devices.

### 27-70 — Gust Lock and Dampener
Gust lock mechanisms, damping functions, and ATA 22 interfaces.

### 27-80 — Lift Augmenting
Leading edge devices (slats, droop nose), actuation, and asymmetry protection.

## Directory Organization

Each sub-subject folder (e.g., `27-10-20-actuators-pcu-ema-eha-and-sensors/`) contains:

- **SSOT/**: Single Source of Truth - Engineering lifecycle data (LC01–LC14)
- **PUB/**: Publication views including S1000D CSDB structure
- **00_INDEX.md**: Index file for the sub-subject

## SSOT Lifecycle Structure (LC01–LC14)

Each SSOT directory contains the complete product lifecycle:

1. **LC01_PROBLEM_STATEMENT**: Requirements genesis and problem definition
2. **LC02_SYSTEM_REQUIREMENTS**: Requirements, traceability, interfaces (ICDs for ATA22, ATA24, ATA29, ATA31)
3. **LC03_DESIGN_MODELS**: Architecture, schematics, actuator selection, EWIS
4. **LC04_ENGINEERING_ANALYSIS**: Loads sizing, EHA/EMA power budget, thermal, reliability, EMI/HIRF/Lightning
5. **LC05_INTEGRATION_TESTING_PROTOTYPING**: Test procedures, reports, rigs
6. **LC06_QUALITY**: Inspection plans, NCR, supplier quality
7. **LC07_SAFETY_SECURITY**: FHA, PSSA, SSA, hazard logs
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

## Document Control

- **ATA Chapter**: 27
- **Standard**: ATA iSpec 2200 / S1000D 5.0
- **Model**: AMPEL360AT
- **Status**: Active Development
- **Last Updated**: 2026-01-09

---

## References

- [ATA iSpec 2200 Specification](https://publications.airlines.org/)
- [S1000D Issue 5.0](http://www.s1000d.org/)
- [ATA Chapters Guide](https://itlims-zsis.meil.pw.edu.pl/pomoce/ESL/2016/ATA_Chapters.pdf)
