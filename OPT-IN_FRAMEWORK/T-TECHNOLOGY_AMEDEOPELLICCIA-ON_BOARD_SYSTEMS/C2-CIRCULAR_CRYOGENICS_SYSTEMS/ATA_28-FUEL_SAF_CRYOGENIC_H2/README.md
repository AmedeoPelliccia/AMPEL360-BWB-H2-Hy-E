# ATA 28 — FUEL SAF CRYOGENIC H2

## Overview

This is ATA Chapter 28: FUEL SAF CRYOGENIC H2, part of the T — TECHNOLOGY AMEDEOPELLICCIA — ON BOARD SYSTEMS axis.

## Quick Navigation

- **[00_INDEX.md](./00_INDEX.md)** — Master index with links to all sections
- **[ATA-28-fuel/](./ATA-28-fuel/)** — iSpec 2200 section breakdown (28-00/10/20/30/40)
- **[ASSETS/](./ASSETS/)** — System diagrams and models

## Structure

This chapter follows the mandatory OPT-IN Framework structure and includes the **ATA 28 iSpec 2200 Section Breakdown**:

### ATA-28-fuel (iSpec 2200 Semantics)

The `ATA-28-fuel/` directory implements the standard ATA 28 fuel system breakdown with deep sub-subject leaves (28-xx-yy) where SSOT and PUB/AMM/CSDB reside:

| Section | Description |
|---------|-------------|
| [28-00 General](./ATA-28-fuel/28-00-fuel-general/00_INDEX.md) | System overview, safety concept, interfaces, maintenance practices |
| [28-10 Storage](./ATA-28-fuel/28-10-storage/00_INDEX.md) | LH2 tank, insulation, pressure relief, filling/defueling, boil-off |
| [28-20 Distribution](./ATA-28-fuel/28-20-distribution/00_INDEX.md) | Feed lines, pumps, vaporizers, pressure regulation, crossfeed |
| [28-30 Dump](./ATA-28-fuel/28-30-dump/00_INDEX.md) | Overboard vent, controlled dump, emergency depressurization |
| [28-40 Indicating](./ATA-28-fuel/28-40-indicating/00_INDEX.md) | Quantity, pressure/temperature, leak detection, fault messages |

### 28-00_GENERAL (Lifecycle Folders)

The GENERAL layer contains 14 mandatory lifecycle folders covering the complete development cycle:

1. **28-00-01_Overview**: System overview and global architecture
2. **28-00-02_Safety**: Safety framework and analysis
3. **28-00-03_Requirements**: Requirements and traceability
4. **28-00-04_Design**: Design specifications and patterns
5. **28-00-05_Interfaces**: Interface control documents
6. **28-00-06_Engineering**: Analysis, models, and simulation
7. **28-00-07_V_AND_V**: Verification and validation
8. **28-00-08_Prototyping**: Prototype development
9. **28-00-09_Production_Planning**: Manufacturing planning
10. **28-00-10_Certification**: Certification evidence
11. **28-00-11_EIS_Versions_Tags**: Configuration management
12. **28-00-12_Services**: Maintenance and service
13. **28-00-13_Subsystems_Components**: Component breakdown
14. **28-00-14_Ops_Std_Sustain**: Operational standards

### Cross-ATA Root Buckets

The following buckets are mandatory in every ATA chapter:

- **28-10_Operations**: Operational procedures and use cases
- **28-20_Subsystems**: Functional subsystems (design-driven internal structure)
- **28-30_ANCHORS**: Sustainability, LCA, and circular economy
- **28-40_Software**: Software, control logic, and AI/ML
- **28-50_Structures**: Physical structures and frames
- **28-60_Storages**: Tanks, reservoirs, and storage
- **28-70_Propulsion**: Propulsion interfaces (if applicable)
- **28-80_Energy**: Energy management and distribution
- **28-90_Tables_Schemas_Diagrams**: Data tables and documentation

## References

- [ATA iSpec 2200](https://itlims-zsis.meil.pw.edu.pl/pomoce/ESL/2016/ATA_Chapters.pdf) — ATA chapter breakdown
- [CS-25](https://www.easa.europa.eu/en/document-library/certification-specifications/cs-25-large-aeroplanes) — EASA Certification Specifications for Large Aeroplanes

---

## Document Control

- **ATA Chapter**: 28
- **Status**: Active
- **Owner**: AMPEL360 Documentation WG
- **Standard**: OPT-IN Framework v1.1
- **Last Updated**: 2026-01-09
- AI assistance: GitHub Copilot, prompted by **Amedeo Pelliccia** (documentation generation and hyperlinking support).

---
