# ATA 26 — Fire Protection (iSpec 2200 Structure)

## Overview

This directory contains the ATA 26 Fire Protection system documentation following the ATA iSpec 2200 chapter/section structure. The CSDB (Common Source Database) lives at the sub-subject (sys-sec-sbj) level with both PUB (S1000D) and SSOT (Single Source of Truth) alongside each other.

## Structure

This follows the canonical ATA iSpec 2200 breakdown for ATA 26:

### 26-00 — Fire Protection General
System overview, architecture, controls and indications.

### 26-10 — Detection
Fire and smoke detection systems for all compartments and zones.

### 26-20 — Extinguishing
Fire extinguishing systems and equipment.

### 26-30 — Explosion Suppression
Explosion suppression, ventilation, inerting and ignition control.

## Directory Organization

Each sub-subject folder (e.g., `26-10-20-apu-fuel-cell-bay-fire-detection/`) contains:

- **SSOT/**: Single Source of Truth - Engineering lifecycle data (LC01–LC14)
- **PUB/**: Publication views including S1000D CSDB structure
- **00_INDEX.md**: Index file for the sub-subject

## SSOT Lifecycle Structure (LC01–LC14)

Each SSOT directory contains the complete product lifecycle:

1. **LC01_PROBLEM_STATEMENT**: Requirements genesis and problem definition
2. **LC02_SYSTEM_REQUIREMENTS**: Requirements, traceability, interfaces
3. **LC03_DESIGN_MODELS**: Architecture, schematics, CAD, EWIS
4. **LC04_ENGINEERING_ANALYSIS**: Thermal, smoke flow, agent distribution, EMI/HIRF/Lightning
5. **LC05_INTEGRATION_TESTING_PROTOTYPING**: Test procedures, reports, rigs
6. **LC06_QUALITY**: Inspection plans, NCR, supplier quality
7. **LC07_SAFETY_SECURITY**: FHA, PSSA, SSA, hazard logs, cybersecurity
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
  - **DM/**: Data Modules (maintenance tasks, descriptions)
  - **PM/**: Publication Modules (publication structure)
  - **DML/**: Data Module Lists (organization)
  - **ICN/**: Illustrations and graphics (SVG format)
  - **BREX/**: Business Rules Exchange (validation rules)
  - **COMMON/**: Reusable content (warnings, cautions)
  - **APPLICABILITY/**: Product variant applicability

## Document Control

- **ATA Chapter**: 26
- **Standard**: ATA iSpec 2200 / S1000D 5.0
- **Model**: AMPEL360AT
- **Status**: Active Development
- **Last Updated**: 2026-01-09

---

## References

- ATA iSpec 2200 Specification
- S1000D Issue 5.0
- [ATA Chapters Guide](https://itlims-zsis.meil.pw.edu.pl/pomoce/ESL/2016/ATA_Chapters.pdf)
