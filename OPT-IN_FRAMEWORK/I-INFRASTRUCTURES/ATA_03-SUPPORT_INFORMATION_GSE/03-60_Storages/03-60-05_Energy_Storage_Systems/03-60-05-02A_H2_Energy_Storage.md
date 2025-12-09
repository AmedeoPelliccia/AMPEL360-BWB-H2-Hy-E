# 03-60-05-02A - H2 Energy Storage

## 1. Purpose
This document specifies requirements for hydrogen energy storage systems used for power generation in GSE operations, including fuel cell systems and hydrogen-to-power conversion.

## 2. Scope
This document covers:
- Hydrogen fuel cell power generation systems
- H2 storage for energy applications (distinct from aircraft refueling)
- Power-to-Gas (P2G) and Grid-to-H2 systems
- Integration with airport electrical grid
- Combined heat and power (CHP) applications

## 3. Applicable Documents
- SAE J2719 (Hydrogen Fuel Quality for Fuel Cell Vehicles)
- IEC 62282 Series (Fuel Cell Technologies)
- NFPA 2 (Hydrogen Technologies Code)
- ISO 14687 (Hydrogen Fuel Quality - Product Specification)
- IEEE 1547 (Interconnection and Interoperability of Distributed Energy Resources)

## 4. Storage Description

### 4.1 Overview
Hydrogen energy storage systems convert stored hydrogen into electrical power through fuel cells, providing clean, reliable power for GSE operations, facility loads, and grid support. These systems enable renewable energy storage through Power-to-Gas conversion and provide backup power capability.

Key applications:
- Stationary fuel cell power plants (100 kW - 1 MW)
- Mobile fuel cell generators for remote GSE power
- Grid stabilization and peak shaving
- Backup/emergency power for critical facilities
- Combined heat and power for facility heating

### 4.2 Specifications

#### Fuel Cell System Types
| Type | Power Range | Efficiency | Application | Fuel Quality |
|------|-------------|------------|-------------|--------------|
| PEM Fuel Cell | 1-250 kW | 40-60% (elec) | Mobile, backup power | 99.97% H2 purity |
| SOFC (Solid Oxide) | 100 kW - 1 MW | 50-60% (elec), 85% (CHP) | Stationary, baseload | Tolerates impurities |
| MCFC (Molten Carbonate) | 300 kW - 3 MW | 45-55% (elec), 80% (CHP) | Large stationary | Can reform natural gas |

#### System Components
| Component | Specification | Function |
|-----------|---------------|----------|
| Fuel Cell Stack | Per type (PEM/SOFC/MCFC) | H2-to-electricity conversion |
| H2 Storage | 350-700 bar GH2 or LH2 | Fuel supply |
| Power Conditioning | Inverter, 480V 3-phase output | Grid-compatible AC power |
| Heat Recovery | CHP heat exchanger | Facility heating/cooling |
| Control System | PLC with grid interface | Load following, grid sync |

### 4.3 Capacity and Requirements

#### Power Generation Sizing Example
For airport with 20 H2-hybrid aircraft operations per day:
- **Fuel Cell Capacity**: 500 kW stationary + 50 kW mobile
- **H2 Consumption**: 
  - 500 kW × 24 hr ×0.06 kg/kWh = 720 kg H2/day (continuous)
  - Actual: ~200-300 kg/day (load-following operation)
- **Storage**: 3-day buffer = 900 kg H2 = 12,700 m³ at STP
- **Implementation**: 
  - 700 bar GH2: ~18 m³ cylinder storage
  - OR LH2: 12.7 m³ (~13,000 L dewar)

#### Grid Integration
- **Grid Connection**: 480V or 13.8 kV as appropriate
- **Islanding Capability**: Black start and standalone operation
- **Power Quality**: IEEE 1547 compliant
- **Grid Services**: Frequency regulation, demand response
- **Metering**: Bidirectional for export capability

## 5. Safety Requirements
| Requirement | Standard | Implementation |
|-------------|----------|----------------|
| H2 Storage Safety | NFPA 2, Chapter 7 | Per bulk or high-pressure storage requirements |
| Fuel Cell Safety | IEC 62282-3-100 | Fuel cell safety certification |
| Electrical Safety | NFPA 70, IEEE 1547 | Proper grounding, arc flash protection |
| Emergency Shutdown | IEC 62282 | Automatic isolation on leak detection |
| Ventilation | NFPA 2, Section 7.6 | 6 ACH minimum for fuel cell enclosures |

## 6. Cross-References
- Related ATA Chapters:
  - ATA 03-60-02 (H2/LH2 Storage Systems) - H2 storage integration
  - ATA 03-60-05-01A (Battery Storage Systems) - Complementary storage
  - ATA 03-60-05-03A (Grid Scale Storage) - Grid integration
  - ATA 24 (Electrical Power) - Aircraft systems analogy
- Parent Document: 03-60_Storages

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
