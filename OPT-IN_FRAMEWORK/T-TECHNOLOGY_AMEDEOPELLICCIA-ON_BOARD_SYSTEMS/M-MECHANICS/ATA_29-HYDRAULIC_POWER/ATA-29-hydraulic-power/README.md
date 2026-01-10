# ATA 29 — Hydraulic Power (iSpec 2200 Structure)

## Overview

This directory contains the ATA 29 Hydraulic Power system documentation following the ATA iSpec 2200 chapter/section structure. The CSDB (Common Source Database) lives at the sub-subject (sys-sec-sbj) level with both PUB (S1000D) and SSOT (Single Source of Truth) alongside each other.

## Structure

This follows the canonical ATA iSpec 2200 breakdown for ATA 29:

### 29-00 — Hydraulic Power General
System overview, architecture, safety philosophy, interfaces, maintenance practices, and compliance.

### 29-10 — Main
Main hydraulic power system including reservoir, pumps, distribution, accumulators, filtration, lines, thermal management, servicing, and health monitoring.

### 29-20 — Auxiliary
Auxiliary hydraulic power including backup pumps, ram air turbine, power transfer unit, emergency accumulators, emergency logic, and auxiliary maintenance.

### 29-30 — Indicating
Hydraulic system indications including pressure, quantity, temperature, filter status, warnings/cautions, and BITE/fault codes.

## Directory Organization

Each sub-subject folder (e.g., `29-10-20-pumps-edp-emp-drive-and-inlet-protection/`) contains:

- **SSOT/**: Single Source of Truth - Engineering lifecycle data (LC01–LC14)
- **PUB/**: Publication views including S1000D CSDB structure
- **00_INDEX.md**: Index file for the sub-subject

## SSOT Lifecycle Structure (LC01–LC14)

Each SSOT directory contains the complete product lifecycle:

1. **LC01_PROBLEM_STATEMENT**: Requirements genesis and problem definition
2. **LC02_SYSTEM_REQUIREMENTS**: Requirements, traceability, interfaces
3. **LC03_DESIGN_MODELS**: Architecture, schematics, piping routing, valves, sensors, EWIS
4. **LC04_ENGINEERING_ANALYSIS**: Pressure drop, flow sizing, transients, thermal, contamination, reliability, EMI/HIRF/Lightning
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
  - **DM/**: Data Modules (maintenance tasks, descriptions)
  - **PM/**: Publication Modules (publication structure)
  - **DML/**: Data Module Lists (organization)
  - **ICN/**: Illustrations and graphics (SVG format)
  - **BREX/**: Business Rules Exchange (validation rules)
  - **COMMON/**: Reusable content (warnings, cautions)
  - **APPLICABILITY/**: Product variant applicability

- **EXPORT/**: Rendered outputs (PDF, HTML)
- **IETP/**: Interactive Electronic Technical Publication packages

## Interfaces with Other ATA Chapters

- **ATA 24**: Electrical Power — Powers pumps and controls
- **ATA 26**: Fire Protection — Zone protection and detection
- **ATA 27**: Flight Controls — Major power user
- **ATA 31**: Indicating/Recording — Warnings, cautions, BITE
- **ATA 32**: Landing Gear — Brakes and steering power user

## Document Control

- **ATA Chapter**: 29
- **Standard**: ATA iSpec 2200 / S1000D 5.0
- **Model**: AMPEL360AT
- **Status**: Active Development
- **Last Updated**: 2026-01-09

---

## References

- [ATA iSpec 2200 Specification](https://www.ata.org)
- [S1000D Issue 5.0](https://s1000d.org)
- [ATA Chapters Guide](https://itlims-zsis.meil.pw.edu.pl/pomoce/ESL/2016/ATA_Chapters.pdf)

---

## Document Control

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT** – Subject to human review and approval.
- Human approver: _[to be completed]_.
- Repository: `AMPEL360-AIR-T`
- Last AI update: _2026-01-09_.
