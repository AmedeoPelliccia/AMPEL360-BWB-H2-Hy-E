# 03-60-02-03A - GH2 High Pressure Storage

## 1. Purpose
This document specifies requirements for high-pressure gaseous hydrogen (GH2) storage systems used in ground support operations, including 350 bar and 700 bar storage for aircraft servicing and backup supply.

## 2. Scope
This document covers:
- High-pressure GH2 cylinder specifications
- Cascade storage systems for aircraft refueling
- Storage rack and module design
- Pressure control and regulation systems
- Safety systems and operational procedures

## 3. Applicable Documents
- ISO 19881 (Gaseous Hydrogen - Land Vehicle Fuel Containers)
- SAE J2579 (Fuel Systems in Fuel Cell and Other Hydrogen Vehicles)
- SAE AS6968 (Hydrogen Aircraft Refueling Systems)
- NFPA 2 (Hydrogen Technologies Code)
- CGA G-5.4 (Standard for Hydrogen Piping Systems at User Locations)
- DOT/PHMSA 49 CFR Part 180 (Continuing Qualification and Maintenance of Packagings)
- EN 17124 (Hydrogen Fuel - Product Specification and Quality Assurance - Proton Exchange Membrane Fuel Cell Applications)

## 4. Storage Description

### 4.1 Overview
High-pressure gaseous hydrogen storage provides compressed hydrogen at 350 bar (5,000 psi) or 700 bar (10,000 psi) for aircraft refueling operations, emergency backup supply, and fuel cell power generation. These systems use Type III or Type IV composite cylinders arranged in cascade configurations to optimize filling efficiency and storage density.

Key system characteristics:
- Multi-bank cascade arrangement for fast filling
- Automated pressure management and sequencing
- Remote monitoring and leak detection
- Redundant pressure relief and safety systems
- Integration with bulk LH2 supply via vaporization

### 4.2 Specifications

#### Cylinder Specifications
| Parameter | Type III Cylinder | Type IV Cylinder | Notes |
|-----------|-------------------|------------------|-------|
| Storage Pressure | 350 bar / 700 bar | 350 bar / 700 bar | Nominal working pressure |
| Material | Aluminum liner + carbon fiber | Polymer liner + carbon fiber | Type IV lighter but more expensive |
| Capacity (per cylinder) | 80-120 liters (water) | 80-120 liters (water) | Typical sizes |
| H2 Storage Mass | 1.5-2.5 kg (350 bar) | 1.5-2.5 kg (350 bar) | Per 100L cylinder |
| H2 Storage Mass | 3.0-5.0 kg (700 bar) | 3.0-5.0 kg (700 bar) | Per 100L cylinder |
| Empty Weight | 60-90 kg | 45-65 kg | Type IV 25-30% lighter |
| Design Life | 15-20 years | 15-20 years | With proper maintenance |
| Service Interval | 3-5 years | 3-5 years | Re-certification required |
| Pressure Relief | Thermally-activated PRD | Thermally-activated PRD | TPRD per ISO 19881 |

#### Cascade System Configuration
| Configuration | Banks | Pressure Levels | Total Capacity | Typical Use |
|---------------|-------|-----------------|----------------|-------------|
| Small Cascade | 3 | Low/Med/High | 50-100 kg H2 | Single refueling point |
| Medium Cascade | 4 | Low/Med/High/Buffer | 150-300 kg H2 | Multiple service points |
| Large Cascade | 5-6 | Progressive staging | 500+ kg H2 | Central supply hub |

### 4.3 Capacity and Requirements

#### Storage Rack Design
- **Configuration**: ISO container (20ft or 40ft) or fixed rack structure
- **Orientation**: Horizontal cylinders preferred for stability
- **Seismic Design**: IBC Seismic Design Category per location
- **Restraints**: Steel bands or brackets at minimum 2 points per cylinder
- **Access**: Removable panels for cylinder replacement
- **Grounding**: All conductive components bonded, < 10 ohms to ground

#### Capacity Planning Example
For airport serving 20 H2-hybrid aircraft per day:
- Average H2 consumption per aircraft: 200 kg
- Peak demand (morning departure wave): 10 aircraft in 2 hours = 2,000 kg H2
- Recommended cascade capacity: 3,000 kg H2 (50% reserve)
- At 700 bar, 3 kg H2 per cylinder → 1,000 cylinders required
- Typical 40ft container module: 100 cylinders → 10 container modules
- Plus: Connection to bulk LH2 with vaporization for continuous refill

#### Pressure Management System
- **Low Bank**: 100-300 bar (initial fill, bulk of mass transfer)
- **Medium Bank**: 300-500 bar (intermediate fill)
- **High Bank**: 500-700 bar (topping to full pressure)
- **Buffer Bank**: 700 bar (reserve, fast response)
- **Automatic Sequencing**: PLC-controlled valves, optimizes usage
- **Continuous Refill**: From LH2 vaporizer, maintains all banks

## 5. Safety Requirements
| Requirement | Standard | Implementation |
|-------------|----------|----------------|
| Separation Distances | NFPA 2, Table 7.2.3.4(a) | 7.5m from buildings, 3m between racks |
| Hydrogen Detection | NFPA 2, Section 7.8 | Multi-zone detection, 25% LEL alarm |
| Pressure Relief | ISO 19881, Section 8 | TPRD on each cylinder, vent manifold |
| Fire Protection | NFPA 2, Section 7.11 | Water spray deluge system |
| Cylinder Testing | DOT/TC/ISO requirements | Periodic hydrostatic or acoustic emission |
| Lightning Protection | NFPA 780 | Bonding, grounding, air terminals |
| Impact Protection | NFPA 2, Section 7.4 | Bollards, guardrails around storage |
| Personnel Training | NFPA 2, Chapter 14 | High-pressure gas handling certification |

### Emergency Procedures
1. **Hydrogen Leak Detection**:
   - Automatic isolation of affected bank
   - Activation of emergency ventilation
   - Remote shutdown of refueling operations
   - Emergency services notification

2. **Fire Exposure**:
   - Automatic deluge activation
   - Isolation of all supply lines
   - Controlled venting via PRDs
   - Establishment of evacuation zone (100m radius)

3. **Cylinder Failure**:
   - TPRD activation prevents catastrophic rupture
   - Vent stack directs release vertically
   - Automatic system shutdown
   - Post-incident investigation before restart

## 6. Cross-References
- Related ATA Chapters:
  - ATA 03-60-01 (GSE Storage Overview) - Overall strategy
  - ATA 03-60-02-01A (LH2 Bulk Storage) - Integration with LH2 supply
  - ATA 03-60-08-01A (H2 Storage Regulations) - Regulatory compliance
  - ATA 28 (Fuel Systems) - Aircraft H2 system interface
  - SAE AS6968 (H2 Refueling) - Refueling system integration
- Parent Document: 03-60_Storages
- Technical Standards:
  - ISO 19881 (GH2 Containers)
  - SAE J2579 (Fuel Systems Safety)
  - NFPA 2 (Hydrogen Technologies Code)

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
