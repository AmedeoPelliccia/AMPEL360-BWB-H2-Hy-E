# 03-60-05-04A - Mobile Energy Storage

## 1. Purpose
This document specifies requirements for mobile energy storage systems used in GSE operations, including portable power units, mobile battery packs, and transportable energy systems.

## 2. Scope
This document covers:
- Mobile battery power units
- Portable fuel cell generators
- Transportable energy storage containers
- Mobile charging stations
- Emergency/backup mobile power systems

## 3. Applicable Documents
- UL 2743 (Portable Fuel Cell Power Systems)
- IEC 62040 (Uninterruptible Power Systems)
- SAE J2954 (Wireless Power Transfer)
- DOT regulations for transportable batteries
- NFPA 1 (Fire Code)

## 4. Storage Description

### 4.1 Overview
Mobile energy storage provides flexible, transportable power for GSE operations, remote aircraft servicing, emergency response, and temporary power needs. Systems range from small portable units to containerized megawatt-scale installations.

### 4.2 Specifications

#### Mobile Energy Storage Types
| System Type | Capacity | Power | Mobility | Application |
|-------------|----------|-------|----------|-------------|
| Portable Battery Pack | 1-10 kWh | 1-5 kW | Hand-carried | Tools, small equipment |
| Battery Cart | 10-100 kWh | 10-50 kW | Wheeled/towed | GSE charging, temp power |
| Battery Container | 100-500 kWh | 100-250 kW | Truck-mounted | Remote operations, events |
| Fuel Cell Generator | 5-100 kW continuous | 5-100 kW | Trailer-mounted | Long-duration power |

#### Performance Requirements
| Parameter | Specification | Notes |
|-----------|---------------|-------|
| Output Voltage | 120V/240V AC, 12V/48V DC | Selectable or simultaneous |
| Power Quality | <5% THD | Clean power for electronics |
| Runtime | 4-24 hours at rated power | Depends on capacity and load |
| Recharge Time | 2-8 hours | Depends on charger capacity |
| Operating Temp | -20°C to +50°C | With thermal management |
| Ingress Protection | IP54 minimum | Outdoor operations |

### 4.3 Capacity and Requirements

#### Fleet Sizing for Airport Operations
- **Small Units (1-10 kWh)**: 20-30 units for small tools, emergency lighting
- **Medium Units (10-100 kWh)**: 10-15 units for GSE charging, temp power
- **Large Units (100-500 kWh)**: 2-3 units for major events, contingency
- **Fuel Cell Generators**: 3-5 units for extended operations, backup

#### Operational Considerations
- **Charging Infrastructure**: Dedicated charging points at storage facility
- **Transport**: Carts, trucks, or self-propelled units
- **Maintenance**: Centralized facility for inspection and testing
- **Tracking**: RFID/GPS for asset management
- **Rotation**: Scheduled rotation to ensure all units remain operational

#### Safety Features
- **Thermal Management**: Active cooling for lithium-ion systems
- **BMS**: Cell-level monitoring and balancing
- **Fire Detection**: Integrated smoke/heat detection
- **Manual Disconnect**: Readily accessible isolation switch
- **Overload Protection**: Automatic shutdown on overload
- **Ground Fault Protection**: GFCI/RCD protection

## 5. Safety Requirements
| Requirement | Standard | Implementation |
|-------------|----------|----------------|
| Battery Safety | UL 2743, IEC 62133 | Certified battery packs |
| Electrical Safety | NFPA 70, OSHA 1910 Subpart S | Proper grounding, GFCI |
| Fire Extinguisher | NFPA 1, user manual | Class ABC extinguisher with each unit |
| Transportation | DOT/IATA regulations | Packaging and labeling per regulations |
| Operator Training | Site-specific | Operation, emergency procedures |

## 6. Cross-References
- Related ATA Chapters:
  - ATA 03-60-05-01A (Battery Storage Systems) - Charging infrastructure
  - ATA 03-60-05-02A (H2 Energy Storage) - Fuel cell generators
  - ATA 03-10 (Operations) - Operational integration
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
