# 03-60-02-01A - LH2 Bulk Storage

## 1. Purpose
This document specifies the requirements and design for bulk liquid hydrogen (LH2) storage systems used in ground support operations for H2-hybrid aircraft refueling and servicing.

## 2. Scope
This document covers:
- Large-scale stationary LH2 storage tanks
- Tank specifications and construction requirements
- Insulation and boil-off management systems
- Safety systems and emergency procedures
- Integration with refueling infrastructure

## 3. Applicable Documents
- ISO 21009-1 (Cryogenic Vessels - Static Vacuum Insulated Vessels)
- ISO 13985 (Liquid Hydrogen - Land Vehicle Fuel Tanks)
- NFPA 2 (Hydrogen Technologies Code), Chapter 7
- CGA H-3 (Cryogenic Hydrogen Storage)
- ASME BPVC Section VIII (Pressure Vessel Code)
- EN 13458-2 (Cryogenic Vessels - Static Vacuum Insulated Vessels)
- SAE AS6968 (Hydrogen Aircraft Refueling Systems)

## 4. Storage Description

### 4.1 Overview
Bulk LH2 storage provides the primary hydrogen supply for aircraft refueling operations. These large-capacity cryogenic vessels maintain hydrogen in liquid state at -253°C (20K) and typically operate at pressures between 1-10 bar. Bulk storage systems are designed for stationary installation and serve as the central supply point for the airport hydrogen infrastructure.

Key design features:
- Vacuum-insulated double-wall construction
- Multi-layer insulation (MLI) systems
- Automated boil-off management
- Redundant safety systems
- Remote monitoring and control

### 4.2 Specifications

#### Tank Specifications
| Parameter | Specification | Notes |
|-----------|---------------|-------|
| Storage Capacity (per tank) | 50,000 - 100,000 liters | Typical airport installation |
| Design Pressure | 10 bar (150 psi) | Inner vessel |
| Operating Pressure | 1.5 - 6 bar | Normal operations |
| Storage Temperature | -253°C (20K) | Liquid hydrogen |
| Insulation Type | Vacuum + MLI | Perlite backup option |
| Vacuum Level | < 10⁻³ mbar | Operational requirement |
| Daily Boil-off Rate | < 0.3% of volume | With proper insulation |
| Material (Inner Vessel) | 304L or 316L Stainless Steel | Cryogenic service |
| Material (Outer Vessel) | Carbon Steel with coating | Structural protection |
| Design Life | 25-30 years | With proper maintenance |

#### System Components
| Component | Specification | Function |
|-----------|---------------|----------|
| Inner Vessel | ASME Section VIII, Div 1 | Primary containment |
| Outer Vessel | ASME Section VIII, Div 1 | Vacuum jacket |
| MLI System | 30-60 layers | Thermal insulation |
| Vacuum Pumping Port | With isolation valve | Vacuum maintenance |
| Level Gauging | Capacitance or differential pressure | Inventory management |
| Pressure Relief Devices | Multiple PRVs, burst disk | Overpressure protection |
| Fill/Withdrawal Lines | Vacuum-jacketed piping | Minimize heat ingress |

### 4.3 Capacity and Requirements

#### Installation Requirements
- **Foundation**: Reinforced concrete pad, seismic design per IBC
- **Clearances**: Minimum 15m from occupied buildings, 7.5m between tanks
- **Orientation**: Access for delivery trucks and maintenance
- **Utilities**: Electrical power (480V, 3-phase), nitrogen purge supply
- **Drainage**: Sloped surface, no impoundment of water near tank

#### Operational Capacity Planning
For typical H2-hybrid aircraft operations:
- Aircraft consumption: ~200 kg H2 per refueling
- Daily flight operations: 10-20 aircraft
- Required storage: Minimum 3-day operational buffer
- Calculation: 20 aircraft × 200 kg × 3 days = 12,000 kg LH2
- Volume required: 12,000 kg ÷ 70.8 kg/m³ = 169 m³ (169,000 L)
- Recommended: 2 × 100,000L tanks (with N+1 redundancy)

#### Boil-off Management
- **Normal Boil-off**: 0.2-0.3% per day → 300-450 liters/day for 150,000L total capacity
- **Management Options**:
  1. Reliquefaction system (energy-intensive but zero loss)
  2. Pressure building and venting (with flare stack)
  3. Utilization in facility heating or power generation (fuel cell)
- **Preferred**: Combination of pressure control and beneficial use

## 5. Safety Requirements
| Requirement | Standard | Implementation |
|-------------|----------|----------------|
| Separation Distances | NFPA 2, Table 7.3.2.4 | 15m minimum from buildings, 7.5m between tanks |
| Hydrogen Detection | NFPA 2, Section 7.8 | Multi-point detection at 25% LEL alarm, 50% LEL shutdown |
| Emergency Venting | NFPA 2, Section 7.7 | Vent stack height per API 521 calculation |
| Fire Protection | NFPA 2, Section 7.11 | Water deluge system, foam capability |
| Lightning Protection | NFPA 780 | Air terminals, grounding grid < 10 ohms |
| Pressure Relief | ASME Section VIII | Dual PRVs sized per CGA S-1.3 |
| Security Fencing | Site security plan | 2.5m fence, 30m perimeter minimum |
| Personnel Training | OSHA 1910.120, NFPA 2 | Annual cryogenic and H2 safety certification |

## 6. Cross-References
- Related ATA Chapters:
  - ATA 03-60-01 (GSE Storage Overview) - Overall strategy
  - ATA 03-60-02-02A (LH2 Dewar Storage) - Mobile LH2 storage
  - ATA 03-60-03 (Cryogenic Storage Systems) - General cryogenic requirements
  - ATA 03-60-08 (Storage Safety Compliance) - Regulatory compliance
  - ATA 28 (Fuel Systems) - Aircraft H2 fuel system interface
- Parent Document: 03-60_Storages
- Standards:
  - ISO 21009 (Cryogenic Vessels)
  - NFPA 2 (Hydrogen Technologies Code)
  - ASME BPVC Section VIII
- External Systems:
  - Airport H2 infrastructure master plan
  - Emergency response plan

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
