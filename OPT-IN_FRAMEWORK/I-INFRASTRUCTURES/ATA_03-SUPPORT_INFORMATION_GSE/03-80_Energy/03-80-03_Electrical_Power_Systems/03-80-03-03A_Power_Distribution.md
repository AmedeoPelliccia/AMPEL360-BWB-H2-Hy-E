# 03-80-03-03A - Power Distribution

## 1. Purpose
This document specifies electrical power distribution systems for Ground Support Equipment (GSE) operations, including charging infrastructure, distribution networks, and load management.

## 2. Scope
This specification covers:
- EV charging infrastructure (Level 2 and DC fast charging)
- Distribution networks within GSE operational areas
- Cable management and routing
- Load balancing and management
- Safety and protection systems

## 3. Applicable Documents
- IEC 61851 (Electric Vehicle Conductive Charging System)
- SAE J1772 (Electric Vehicle and Plug-in Hybrid Electric Vehicle Conductive Charge Coupler)
- IEC 60364 (Low-Voltage Electrical Installations)
- NFPA 70 (National Electrical Code)
- ISO 15118 (Road Vehicles - Vehicle to Grid Communication Interface)

## 4. Energy System Description

### 4.1 Overview
Power distribution systems deliver electrical energy from primary sources (grid, on-site generation) to end-use points including EV charging stations, building facilities, and direct equipment connections.

### 4.2 Specifications
| Parameter | Specification | Notes |
|-----------|---------------|-------|
| Distribution Voltage | 400V AC, 230V AC, 800V DC | Multiple voltage levels |
| Charging Power | Level 2: 7-22 kW, DC Fast: 50-350 kW | Per charger |
| Distribution Capacity | 100 kW - 5 MW | Per operational zone |
| Cable Type | Copper or aluminum, XLPE insulation | Underground preferred |
| Protection | RCD, MCB, MCCB | Per IEC/NFPA standards |

### 4.3 Performance Requirements

#### 4.3.1 Charging Infrastructure
- **Availability**: 98% operational availability per charging station
- **Charging Speed**: Support for rapid charging to minimize equipment downtime
- **Compatibility**: Support for multiple connector types (Type 2, CCS, CHAdeMO)
- **Smart Charging**: Communication capability per ISO 15118
- **Safety**: Ground fault protection, overcurrent protection, emergency stop

### 4.4 EV Charging Infrastructure

#### 4.4.1 Level 2 AC Charging
**Specifications**:
- Voltage: 400V three-phase AC
- Power: 7-22 kW per charging point
- Connector: IEC 62196 Type 2 (Mennekes)
- Charging time: 2-8 hours (depends on battery capacity)

**Applications**:
- Overnight charging for light-duty GSE
- Slow charging during extended downtime
- Cost-effective for lower power requirements

#### 4.4.2 DC Fast Charging
**Specifications**:
- Voltage: 200-920V DC
- Power: 50-350 kW per charging station
- Connector: CCS (Combined Charging System), CHAdeMO (if required)
- Charging time: 15-60 minutes to 80% SOC

**Applications**:
- Rapid charging during operational breaks
- Heavy-duty GSE with large battery packs
- High-utilization equipment requiring minimal downtime

### 4.5 Distribution Network Architecture

**Centralized vs. Distributed**:
- Centralized: Main distribution from substation to charging hubs
- Distributed: Multiple smaller distribution points throughout facility
- Hybrid: Combination approach for flexibility

**Underground Cable Distribution**:
- Preferred for safety, aesthetics, and protection
- Cable trenches or duct banks
- Pull boxes at intervals for cable pulling and maintenance access

## 5. Safety and Environmental Requirements
| Requirement | Standard | Implementation |
|-------------|----------|----------------|
| EV Charging Safety | IEC 61851, SAE J1772 | Design and installation per standards |
| Electrical Installation | IEC 60364, NFPA 70 | Wiring, protection, grounding |
| RCD Protection | IEC 61008, IEC 61009 | Ground fault protection |
| Cable Installation | IEC 60502, NFPA 70 | Cable selection and installation |

## 6. Cross-References
- Related ATA Chapters: ATA 03 (Support Information/GSE)
- Parent Document: 03-80_Energy
- Grid Power Supply: 03-80-03-01A_Grid_Power_Supply
- Battery Energy Systems: 03-80-05_Battery_Energy_Systems
- Energy Management Systems: 03-80-06_Energy_Management_Systems

## 7. Revision History
| Rev | Date | Author | Description |
|-----|------|--------|-------------|
| A | 2025-12-08 | AMPEL360 GSE Energy WG | Initial release |

---

## Document Control

- **Status**: DRAFT – Subject to review and approval
- **Classification**: Internal Use
- **Owner**: AMPEL360 GSE Energy Working Group
- **Next Review**: 2026-03-08
- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: 2025-12-08

---
