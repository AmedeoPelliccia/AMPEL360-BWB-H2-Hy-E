# ICD-SHM-000: SHM Master Interface Register

## Document ID
**ICD-SHM-000**

## Title
Structural Health Monitoring - Master Interface Control Document Register

## Purpose
This document serves as the master register for all Interface Control Documents (ICDs) related to the Structural Health Monitoring (SHM) system integration across ATA chapters.

## Scope
Covers all SHM interfaces with:
- Electrical power systems (ATA 24)
- Indicating and recording systems (ATA 31)
- Integrated Modular Avionics (ATA 42)
- Central Maintenance System (ATA 45)
- Information systems (ATA 46)
- Wing structure (ATA 57)
- Hydrogen fuel systems (ATA 73)

## Interface Summary Matrix

| ICD Number | Title | Source ATA | Target ATA | Status | Priority |
|------------|-------|------------|------------|--------|----------|
| [ICD-53-24-SHM-001](./ICD-53-24-SHM-001_Electrical_Power_Interface.md) | Electrical Power Interface | 53 | 24 | Draft | Critical |
| [ICD-53-31-SHM-001](./ICD-53-31-SHM-001_Display_Recording_Interface.md) | Display Recording Interface | 53 | 31 | Draft | Critical |
| [ICD-53-42-SHM-001](./ICD-53-42-SHM-001_IMA_Processing_Interface.md) | IMA Processing Interface | 53 | 42 | Draft | Critical |
| [ICD-53-45-SHM-001](./ICD-53-45-SHM-001_CMS_Maintenance_Interface.md) | CMS Maintenance Interface | 53 | 45 | Draft | Critical |
| ICD-53-46-SHM-001 | Information Systems Interface | 53 | 46 | Planned | Major |
| [ICD-53-57-SHM-001](./ICD-53-57-SHM-001_Wing_Body_Junction_Interface.md) | Wing Body Junction Interface | 53 | 57 | Draft | Critical |
| ICD-53-73-SHM-001 | H2 Tank Structure Interface | 53 | 73 | Planned | Critical |

## Interface Categories

### Category A: Power and Signal Interfaces
| Interface | Type | Protocol | Data Rate |
|-----------|------|----------|-----------|
| 24 → SHM | Power | 28 VDC | N/A |
| SHM → 31 | Data | ARINC 429 | 100 kbps |
| SHM ↔ 42 | Data | AFDX | 100 Mbps |
| SHM ↔ 45 | Data | ARINC 624 | 10 Mbps |
| SHM ↔ 46 | Data | Ethernet | 100 Mbps |

### Category B: Structural Interfaces
| Interface | Type | Physical | Notes |
|-----------|------|----------|-------|
| 53 ↔ 57 | Sensor Network | Sensor harness | Wing-body junction |
| 53 ↔ 73 | Sensor Network | Sensor harness | Cryogenic zone |

## Traceability to Parent Requirement

All ICDs trace to parent requirement:
- **[53-00-03-01-005](../../A-AIRFRAME/ATA_53-FUSELAGE/53-00_GENERAL/53-00-03_Requirements/01_Structural_Integrity/53-00-03-01-005_Compatibility_with_SHM_Assumptions.md)**: Compatibility with SHM Assumptions

## ICD Document Locations

| ICD | Primary Location | Mirror Location |
|-----|------------------|-----------------|
| ICD-53-24-SHM-001 | L2-LINKS/INTERFACE_CONTROL/SHM_INTERFACES/ | ATA_53/53-00-05_Interfaces/SHM/ |
| ICD-53-31-SHM-001 | L2-LINKS/INTERFACE_CONTROL/SHM_INTERFACES/ | ATA_53/53-00-05_Interfaces/SHM/ |
| ICD-53-42-SHM-001 | L2-LINKS/INTERFACE_CONTROL/SHM_INTERFACES/ | ATA_53/53-00-05_Interfaces/SHM/ |
| ICD-53-45-SHM-001 | L2-LINKS/INTERFACE_CONTROL/SHM_INTERFACES/ | ATA_53/53-00-05_Interfaces/SHM/ |
| ICD-53-46-SHM-001 | L2-LINKS/INTERFACE_CONTROL/SHM_INTERFACES/ | — |
| ICD-53-57-SHM-001 | L2-LINKS/INTERFACE_CONTROL/SHM_INTERFACES/ | ATA_57/57-00-05_Interfaces/SHM/ |
| ICD-53-73-SHM-001 | L2-LINKS/INTERFACE_CONTROL/SHM_INTERFACES/ | ATA_73/73-00-05_Interfaces/SHM/ |

## Change Control

Interface changes require:
1. Change request submission
2. Impact assessment by both ATA chapter owners
3. Review by SHM Systems Lead
4. Approval by Configuration Control Board
5. ICD revision and distribution

## Status Legend

| Status | Definition |
|--------|------------|
| Draft | Initial document, under development |
| Review | Under technical review |
| Approved | Reviewed and approved, released |
| Superseded | Replaced by newer version |

## Priority Legend

| Priority | Definition |
|----------|------------|
| Critical | Required for SHM basic functionality |
| Major | Required for full SHM capability |
| Minor | Enhancement or optimization |

---

## Document Control

| Field | Value |
|-------|-------|
| Generated with | AI assistance (GitHub Copilot) |
| Prompted by | **Amedeo Pelliccia** |
| Status | **DRAFT** |
| Human Approver | _[to be completed]_ |
| Repository | `AMPEL360-BWB-H2-Hy-E` |
| File Path | `OPT-IN_FRAMEWORK/T-TECHNOLOGY_AMEDEOPELLICCIA-ON_BOARD_SYSTEMS/L2-LINKS/INTERFACE_CONTROL/SHM_INTERFACES/` |
| Last AI Update | 2025-11-27 |

---
