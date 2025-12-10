# 03-80-02-01A - H2 Energy Infrastructure

## 1. Purpose
This document specifies the hydrogen energy infrastructure required for Ground Support Equipment (GSE) operations, including production, storage, distribution, and refueling systems.

## 2. Scope
This specification covers:
- H2 production facilities and technologies
- H2 storage systems (gaseous and liquid)
- H2 distribution networks and transport
- H2 refueling stations for GSE
- Safety systems and monitoring
- Integration with airport operations

## 3. Applicable Documents
- SAE AS6968 (Hydrogen Aircraft Refueling Standards)
- ISO 19880-1 (Gaseous Hydrogen Fueling Stations - General Requirements)
- ISO 19881 (Gaseous Hydrogen - Land Vehicle Fuel Containers)
- ISO 19882 (Gaseous Hydrogen - Thermally Activated Pressure Relief Devices)
- NFPA 2 (Hydrogen Technologies Code)
- ISO 14687 (Hydrogen Fuel Quality - Product Specification)
- IEC 60079 (Explosive Atmospheres)

## 4. Energy System Description

### 4.1 Overview
The H2 energy infrastructure for GSE operations encompasses all systems required to produce, store, distribute, and dispense hydrogen fuel safely and efficiently. This infrastructure supports both fuel cell electric vehicles and H2 combustion engines across the GSE fleet.

### 4.2 Specifications
| Parameter | Specification | Notes |
|-----------|---------------|-------|
| H2 Production Capacity | 500-5000 kg/day | Scalable based on demand |
| H2 Purity | ≥99.97% (ISO 14687 Type I Grade D) | Fuel cell quality |
| Storage Pressure | 200-900 bar | Multi-pressure system |
| Refueling Pressure | 350 bar, 700 bar | Standard GSE pressures |
| Refueling Time | 3-5 minutes | Per vehicle |
| System Availability | 99.5% minimum | With redundancy |

### 4.3 Performance Requirements

#### 4.3.1 H2 Production Systems
**On-Site Electrolysis**:
- Production rate: 500-5000 kg H2/day
- Electrolyzer types: PEM and/or Alkaline
- Input: Renewable electricity + demineralized water
- Efficiency: >60% (HHV basis)
- Purity: Direct fuel cell grade output
- Response time: <5 minutes from standby to full production

**Key Components**:
- Electrolyzer stacks
- Power electronics and control systems
- Water treatment and supply systems
- H2 purification and drying systems
- Compression systems (if required)
- Cooling systems

#### 4.3.2 H2 Storage Systems
**Gaseous Storage**:
- Type: Composite overwrapped pressure vessels (COPV), Type III/IV
- Pressure ratings: 200, 450, 500, 700, 900 bar
- Capacity: 100-10,000 kg total storage
- Configuration: Cascade storage for optimal refueling
- Safety: Pressure relief devices, leak detection, fire suppression

**Liquid Storage** (if applicable):
- Temperature: -253°C (cryogenic)
- Capacity: Up to 50,000 kg
- Insulation: Vacuum-insulated cryogenic tanks
- Boil-off management: Re-liquefaction or use systems

#### 4.3.3 H2 Distribution Systems
**On-Site Distribution**:
- Piping: Stainless steel (316L) or composite materials
- Pressure: 50-900 bar depending on application
- Leak detection: Continuous monitoring along distribution routes
- Safety zones: Appropriate setbacks and barriers
- Redundancy: Multiple feed paths for critical applications

**Mobile Distribution** (if applicable):
- Tube trailers: 200-500 bar, up to 1,000 kg capacity
- Liquid tankers: Cryogenic, up to 4,000 kg capacity
- Safety: Transport in accordance with ADR/RID regulations

#### 4.3.4 H2 Refueling Stations
**Design Specifications**:
- Dispenser types: 350 bar and 700 bar
- Filling protocol: SAE J2601 compliant
- Communication: SAE J2799 (infrared communication)
- Throughput: 10-30 vehicles per dispenser per day
- User interface: Touchscreen, multi-language support

**Safety Systems**:
- Emergency shutdown (ESD) system
- H2 leak detection (1% LEL sensitivity)
- Fire detection and suppression
- Ventilation systems (natural or forced)
- Safety signage and barriers
- Personnel protection equipment stations

### 4.4 System Architecture

#### 4.4.1 Integrated H2 Energy Hub
The H2 energy infrastructure is designed as an integrated hub:

1. **Production Zone**: Electrolyzers + renewable energy interface
2. **Storage Zone**: High-pressure gaseous and/or liquid H2 storage
3. **Distribution Zone**: Piping networks, compression stations
4. **Refueling Zone**: Dispenser stations for GSE fleet
5. **Control Center**: Centralized monitoring and control
6. **Safety Zone**: Emergency response and safety systems

#### 4.4.2 Scalability and Modularity
- Modular design allowing capacity increases in 500 kg/day increments
- Expansion provisions in site design and utility connections
- Phased implementation approach (pilot → full-scale)

## 5. Safety and Environmental Requirements
| Requirement | Standard | Implementation |
|-------------|----------|----------------|
| H2 Fueling Station Safety | SAE AS6968, ISO 19880-1, NFPA 2 | Design, operation, maintenance per standards |
| Pressure Equipment | ASME BPVC Section VIII, EN 13445 | Vessel design and certification |
| Electrical Classification | IEC 60079, NFPA 70 | Hazardous area classification, equipment |
| Fire Safety | NFPA 2, ISO 22734 | Detection, suppression, emergency response |
| Environmental Protection | ISO 14001 | EMS, spill prevention, waste management |
| Operational Safety | ISO 19880-5 | Safety procedures, training, audits |

## 6. Cross-References
- Related ATA Chapters: ATA 03 (Support Information/GSE)
- Parent Document: 03-80_Energy
- Related GSE ANCHORS: 03-30_ANCHORS
- Related GSE Propulsion: 03-70_Propulsion
- Related GSE Storages: 03-60_Storages
- Energy Strategy: 03-80-01-01A_GSE_Energy_Strategy
- Energy Requirements: 03-80-01-02A_GSE_Energy_Requirements
- Green H2 Production: 03-80-02-02A_Green_H2_Production
- H2 Distribution: 03-80-02-03A_H2_Distribution_Systems
- H2 Energy Conversion: 03-80-02-04A_H2_Energy_Conversion
- H2 Safety: 03-80-08-02A_H2_Energy_Safety

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
