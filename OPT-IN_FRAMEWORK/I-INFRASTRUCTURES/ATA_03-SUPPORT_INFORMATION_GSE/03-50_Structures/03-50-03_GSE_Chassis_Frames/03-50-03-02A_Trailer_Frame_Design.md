# 03-50-03-02A - Trailer Frame Design

## 1. Purpose
This document specifies the structural design requirements for trailer frames used in towed Ground Support Equipment (GSE), including LH2 transport trailers, equipment trailers, and service trailers.

## 2. Scope
This specification covers:
- Trailer frame structural design
- Towing interface and coupling systems
- Axle and suspension mounting
- Landing gear and support systems
- Regulatory compliance (road transport)

## 3. Applicable Documents
- SAE J2314 (Truck-Trailer Compatibility)
- ISO 1102 (Mechanical Coupling for 50 mm Ball)
- ISO 11407 (Commercial Vehicles - Mechanical Coupling - Fifth Wheel)
- FMVSS 571.121 (Air Brake Systems)
- EC Directive 96/53/EC (Weights and Dimensions of Road Vehicles)
- AWS D1.1 (Structural Welding Code - Steel)
- Reference: 03-50-03-01A (Mobile GSE Chassis)

## 4. Structural Description

### 4.1 Overview
Trailer frames are specialized chassis designed for towed operation, optimized for road transport of GSE equipment and fluids. LH2 trailers require special consideration for cryogenic loads and thermal cycling.

### 4.2 Frame Types
| Type | Capacity | Application | Axles |
|------|----------|-------------|-------|
| Single-Axle Utility | 1-5 tonnes | Light equipment, tools | 1 |
| Tandem-Axle | 10-20 tonnes | LH2 transport (5000-15000 L) | 2 |
| Tri-Axle | 20-40 tonnes | Large LH2 tanks, heavy equipment | 3 |
| Low-Boy | 15-30 tonnes | Large equipment, wide loads | 2-3 |

### 4.3 Key Components
| Component | Function | Material | Design Load |
|-----------|----------|----------|-------------|
| Main Beams | Primary longitudinal strength | A572 Gr 50 | Bending, torsion |
| Cross-Members | Lateral stiffness | A36 steel | Distributed load |
| Tow Coupling | Connects to tug vehicle | High-strength steel | 50-500 kN |
| Landing Gear | Support when uncoupled | Steel with crank mechanism | 1.5× static load |
| Tank Saddles (LH2 trailers) | Support cryogenic vessel | SS 304 or insulated | Thermal + static |
| Axle Mounts | Suspension attachment | High-strength steel | 3× static axle load |

### 4.4 LH2 Trailer Specific Requirements
| Parameter | Specification | Notes |
|-----------|---------------|-------|
| Tank Capacity | 5,000-50,000 liters | DOT or TC approval required |
| Tank Support | Sliding saddles | Accommodate thermal contraction |
| Insulation Clearance | 200 mm minimum | Prevent thermal bridging |
| Emergency Shutoff | Remote activation | Within 3 m of tank |
| Static Grounding | Continuous electrical path | Prevent static ignition |

## 5. Structural Requirements

### 5.1 Design Criteria
| Parameter | Requirement | Standard |
|-----------|-------------|----------|
| Towing Load | 2× static towing force | ISO 11407 |
| Vertical Load | 1.5× GVWR | SAE J2314 |
| Braking Load | 0.6g deceleration | FMVSS 121 |
| Safety Factor | 2.0 on yield, 3.5 on ultimate | AISC 360 |
| Fatigue Life | 500,000 km | SAE J1099 |

### 5.2 Road Transport Compliance
- Maximum length: 16.5 m (EU), varies by jurisdiction
- Maximum width: 2.55 m standard, 3.0 m with permit
- Maximum height: 4.0 m
- Axle load limits: Per local regulations (typically 9-11 tonnes/axle)

## 6. Cross-References
- Related ATA Chapters: ATA 03-00-06 (GSE Engineering)
- Parent Document: 03-50_Structures
- Related: 03-50-03-01A (Mobile GSE Chassis), 03-50-02-01A (LH2 Tank Structures)

## 7. Revision History
| Rev | Date | Author | Description |
|-----|------|--------|-------------|
| A | 2025-12-08 | AMPEL360 Documentation Team | Initial release |

---

## Document Control

- **Document ID:** 03-50-03-02A
- **Version:** A
- **Status:** Active
- **Last Updated:** 2025-12-08
- **Repository:** AMPEL360-BWB-H2-Hy-E
- **Owner:** AMPEL360 GSE Structures Team

---

*Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.*
