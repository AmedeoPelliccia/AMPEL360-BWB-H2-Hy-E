# 03-50-04-04A - Cargo Loader Structures

## 1. Purpose
Specification for structural design of cargo and baggage loader platforms, including belt loaders, container loaders, and elevated work platforms for aircraft cargo operations.

## 2. Scope
- Belt loader structures
- Container/pallet loader frames
- Scissor lift cargo platforms
- Loading bridge structures
- Restraint and positioning systems

## 3. Applicable Documents
- ISO 3691 (Industrial Trucks - Safety Requirements)
- SAE AS4084 (Cargo Handling Equipment)
- OSHA 1910.178 (Powered Industrial Trucks)
- EN 12312-8 (Aircraft Ground Support Equipment - Conveyor Belt Loaders)
- AWS D1.1 (Structural Welding Code)

## 4. Structural Description

### 4.1 Loader Types
| Type | Capacity | Height Range | Application |
|------|----------|--------------|-------------|
| Belt Loader | 450-900 kg | 1.5-7 m | Baggage, bulk cargo |
| Container Loader | 6,800-13,600 kg | 1.2-5.5 m | LD-3, LD-8, PMC containers |
| Pallet Loader | 6,800-9,000 kg | 1.2-4.5 m | 88"×125" pallets |
| High Loader | 3,000-7,000 kg | 2-8 m | Main deck cargo |
| Catering Loader | 2,000-4,000 kg | 2-7 m | Meal carts, supplies |

### 4.2 Structural Components
| Component | Function | Material | Design Criteria |
|-----------|----------|----------|-----------------|
| Base Frame | Platform support | Steel A572 Gr 50 | Bending, torsion |
| Scissor Mechanism | Height adjustment | Steel tube/box | Compression, buckling |
| Platform Deck | Load surface | Aluminum or steel | 15 kPa live load |
| Conveyor Support | Belt loader frame | Aluminum alloy | Belt tension + cargo |
| Container Guides | Alignment system | Steel angle/channel | Side loads, impact |
| Restraints | Cargo securing | Steel with locks | 2× cargo weight |
| Leveling System | Stabilization | Hydraulic jacks | 1.5× platform capacity |

### 4.3 Load Requirements
| Load Type | Magnitude | Application |
|-----------|-----------|-------------|
| Cargo Load | Per loader rating (4,500-13,600 kg) | Platform or conveyor |
| Impact Load | 1.5× static cargo load | Dynamic loading/unloading |
| Wind Load (stowed) | 120 km/h | ASCE 7 |
| Wind Load (operational) | 40 km/h | Operational limit |
| Slope Operation | ±5° side, ±10° longitudinal | Uneven apron surface |

### 4.4 Hydraulic/Pneumatic Systems
- **Lift Cylinders**: 2× static load capacity, safety valves
- **Positioning Actuators**: Hold position under full load + wind
- **Emergency Lowering**: Manual or powered backup system
- **Pressure Relief**: Prevent overload (1.5× rated pressure)

## 5. Structural Requirements

### 5.1 Design Criteria
| Parameter | Requirement | Standard |
|-----------|-------------|----------|
| Platform Capacity | Per specification (4,500-13,600 kg) | SAE AS4084 |
| Safety Factor (structure) | 2.0 on yield | AISC 360 |
| Safety Factor (hydraulics) | 1.5× rated pressure | ISO 4413 |
| Deflection Limit | L/300 under rated load | Design practice |
| Stability Factor | 1.5 minimum (tip over) | ISO 3691 |
| Service Life | 50,000 cycles or 20 years | Operational profile |

### 5.2 Operational Requirements
- **Platform Tilt**: Level within ±1° (automatic or manual)
- **Side Shift**: ±300 mm typical (container alignment)
- **Raise/Lower Speed**: 0.1-0.3 m/s (controlled)
- **Drive Speed**: 0-25 km/h (towed or self-propelled)
- **Emergency Stop Distance**: < 2 m at full speed

### 5.3 Safety Features
- Overload sensors and alarms (110% capacity warning)
- Tilt sensors and automatic shutdown (>3° slope)
- Emergency lowering capability (hydraulic failure)
- Platform edge barriers (prevent cargo fall)
- Collision avoidance (proximity sensors)
- Visual/audible alarms during operation

## 6. Cross-References
- Parent Document: 03-50_Structures
- Related: 03-50-04-01A (Maintenance Platforms), 03-50-03-01A (Mobile GSE Chassis)

## 7. Revision History
| Rev | Date | Author | Description |
|-----|------|--------|-------------|
| A | 2025-12-08 | AMPEL360 Documentation Team | Initial release |

---

## Document Control

- **Document ID:** 03-50-04-04A
- **Version:** A
- **Status:** Active
- **Last Updated:** 2025-12-08
- **Repository:** AMPEL360-BWB-H2-Hy-E
- **Owner:** AMPEL360 GSE Structures Team

---

*Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.*
