# 03-60-05-01A - Battery Storage Systems

## 1. Purpose
This document specifies requirements for battery storage systems used for electric GSE, including charging infrastructure, safety systems, and operational procedures.

## 2. Scope
This document covers:
- Battery storage facility design
- Charging system infrastructure
- Battery types and specifications (Li-ion, Lead-acid)
- Safety systems including thermal runaway detection
- Maintenance and lifecycle management

## 3. Applicable Documents
- NFPA 855 (Standard for the Installation of Stationary Energy Storage Systems)
- UL 9540 (Energy Storage Systems and Equipment)
- IEC 62619 (Safety Requirements for Secondary Lithium Cells and Batteries)
- SAE J2954 (Wireless Power Transfer for Light-Duty Plug-In/Electric Vehicles)
- IEEE 1625 (Rechargeable Batteries for Multi-Cell Mobile Computing Devices)
- OSHA 1910.178 (Powered Industrial Trucks)

## 4. Storage Description

### 4.1 Overview
Battery storage systems provide power storage for electric ground support equipment, reducing emissions and noise in airport operations. Systems include both integrated battery packs in GSE and centralized charging/storage facilities for battery exchange operations.

Key system components:
- Charging infrastructure (Level 2 and Level 3/DC fast charging)
- Battery storage racks for spare battery packs
- Thermal management and fire suppression
- Battery management systems (BMS) with monitoring
- Energy management integration with facility power

### 4.2 Specifications

#### Battery Types and Applications
| Battery Type | Energy Density | Cycle Life | Typical Use | Safety Considerations |
|--------------|----------------|------------|-------------|----------------------|
| Lithium-ion (NMC) | 150-250 Wh/kg | 1,000-3,000 cycles | Electric tugs, scissor lifts | Thermal runaway risk, requires active cooling |
| Lithium Iron Phosphate (LFP) | 90-160 Wh/kg | 2,000-5,000 cycles | Belt loaders, cargo carts | Safer chemistry, lower thermal risk |
| Lead-Acid (AGM) | 30-50 Wh/kg | 500-1,000 cycles | Legacy GSE, backup power | Hydrogen gas during charging |

#### Charging Infrastructure
| Charger Type | Power Level | Charge Time | Application |
|--------------|-------------|-------------|-------------|
| Level 1 (AC) | 1.4-1.9 kW | 8-12 hours | Overnight charging |
| Level 2 (AC) | 7.2-19.2 kW | 2-4 hours | Typical GSE charging |
| Level 3 (DC Fast) | 50-350 kW | 20-60 minutes | Rapid turnaround, opportunity charging |

### 4.3 Capacity and Requirements

#### Facility Design
- **Footprint**: 800-1,200 m² for typical airport
- **Charging Stations**: 50-100 positions
- **Fire Separation**: 3m between lithium-ion charging bays
- **Ventilation**: 6-12 ACH, hydrogen detection for lead-acid
- **Fire Suppression**: Clean agent (FM-200, Novec 1230) or water mist
- **Thermal Monitoring**: IR cameras or point sensors on each charging bay

#### Electrical Infrastructure
- **Power Supply**: 480V 3-phase, 1-2 MW total capacity
- **Load Management**: Smart charging with demand response
- **Backup Power**: UPS for BMS and safety systems
- **Energy Storage**: Optional grid-scale battery for peak shaving

#### Safety Systems
- **Thermal Runaway Detection**: Multi-sensor (smoke, temperature, VOC)
- **Automatic Fire Suppression**: Triggered by thermal runaway detection
- **Emergency Shutdown**: Isolate charging in <5 seconds
- **Battery Quarantine**: Dedicated area for damaged/off-gassing batteries
- **Ventilation Purge**: Emergency high-volume ventilation

## 5. Safety Requirements
| Requirement | Standard | Implementation |
|-------------|----------|----------------|
| Fire Detection | NFPA 855, Section 6 | Multi-criteria detection (smoke, heat, gas) |
| Fire Suppression | NFPA 855, Section 7 | Clean agent or water mist, automatic activation |
| Thermal Runaway Prevention | UL 9540, UL 9540A | Cell-level BMS, thermal management |
| Electrical Safety | NFPA 70 (NEC), Article 625 | GFCI protection, proper grounding |
| Hydrogen Ventilation (Lead-Acid) | OSHA 1910.178(g) | Ventilation in charging areas |
| Personnel Training | NFPA 855, Chapter 11 | Battery safety and emergency response |
| Emergency Response Plan | NFPA 855, Section 10 | Include battery fire procedures |

## 6. Cross-References
- Related ATA Chapters:
  - ATA 03-60-01-03A (GSE Storage Facilities) - Facility integration
  - ATA 03-60-05-02A (H2 Energy Storage) - Alternative energy storage
  - ATA 03-60-08 (Storage Safety Compliance) - Safety requirements
  - ATA 24 (Electrical Power) - Power system integration
- Parent Document: 03-60_Storages
- Standards:
  - NFPA 855 (Energy Storage Systems)
  - UL 9540 (ESS Safety)
  - IEC 62619 (Battery Safety)

## 7. Revision History
| Rev | Date | Author | Description |
|-----|------|--------|-------------|
| A | 2025-12-08 | AMPEL360 Documentation Team | Initial release |

---

## Document Control

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT** – Subject to human review and approval.
- Human approver: _[to be completed]_.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: _2025-12-08_.
