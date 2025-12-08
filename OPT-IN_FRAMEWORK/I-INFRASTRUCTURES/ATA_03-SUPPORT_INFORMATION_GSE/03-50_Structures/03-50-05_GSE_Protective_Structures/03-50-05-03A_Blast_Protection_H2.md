# 03-50-05-03A - Blast Protection for H2 Systems

## 1. Purpose
Specification for structural design of blast protection systems for hydrogen Ground Support Equipment (GSE), including blast walls, venting systems, and deflagration protection to mitigate risks from hydrogen ignition events.

## 2. Scope
- Blast walls and barriers
- Deflagration venting structures
- Containment structures for H2 equipment
- Separation distances and isolation
- Emergency pressure relief structures

## 3. Applicable Documents
- NFPA 2 (Hydrogen Technologies Code)
- NFPA 68 (Explosion Protection by Deflagration Venting)
- EN 14994 (Gas Explosion Venting Protective Systems)
- API 521 (Pressure-Relieving and Depressuring Systems)
- UFC 3-340-02 (Structures to Resist the Effects of Accidental Explosions)
- SAE AIR7601 (Guidelines for Handling Liquid Hydrogen)

## 4. Structural Description

### 4.1 Overview
Hydrogen deflagrations generate rapid pressure rise and thermal radiation. Protective structures must either contain the pressure or safely vent it while shielding personnel and equipment from blast effects.

### 4.2 H2 Explosion Characteristics
| Parameter | Value | Notes |
|-----------|-------|-------|
| Deflagration Pressure | 8-10× initial pressure | In confined spaces |
| Flame Speed | 2-5 m/s (unconfined) | Can accelerate in confinement |
| Pressure Rise Rate | 100-500 bar/s | Depends on confinement |
| Ignition Energy | 0.02 mJ minimum | Extremely easy to ignite |
| Flame Temperature | 2045°C | High thermal radiation |
| Detonation Pressure | 15-20× initial pressure | Requires strong confinement |

### 4.3 Blast Wall Design
| Wall Type | Construction | Capacity | Application |
|-----------|--------------|----------|-------------|
| Reinforced Concrete | 200-400 mm thick | 100-500 kPa overpressure | Permanent installations |
| Precast Concrete Panels | 150-300 mm thick | 50-200 kPa | Modular protection |
| Steel Plate with Infill | 10 mm plate + sand/concrete | 50-300 kPa | Mobile/temporary |
| Earth Berm | Compacted soil, 1:1 slope | 50-150 kPa | Low-cost, large area |
| Composite Panels | Steel + polymer foam | 30-100 kPa | Lightweight, modular |

### 4.4 Deflagration Venting
| Parameter | Specification | Standard |
|-----------|---------------|----------|
| Vent Area | 0.1-0.25 m²/m³ enclosure volume | NFPA 68 |
| Activation Pressure | 0.1-0.5 bar | Minimize internal pressure |
| Vent Panel | Hinged or frangible | Must open reliably |
| Discharge Direction | Away from personnel/equipment | Safety consideration |
| Flame Arrestor | If required by code | Prevent external ignition |

### 4.5 Separation Distances
| Scenario | Minimum Separation | Basis |
|----------|-------------------|-------|
| H2 Storage to Building | 15-25 m | NFPA 2, quantity-dependent |
| LH2 Tank to Property Line | 30-60 m | NFPA 2, API 2510 |
| Refueling Dispenser to Building | 10-15 m | NFPA 2 |
| Between H2 Storage Units | 10 m or 1× tank diameter | NFPA 2 |
| H2 Vent Stack to Air Intake | 10 m horizontal, 3 m vertical | NFPA 2 |

### 4.6 Protective Structure Components
| Component | Function | Design Criteria |
|-----------|----------|-----------------|
| Blast Wall | Pressure barrier | Withstand peak overpressure |
| Foundation | Anchor blast wall | Resist sliding, overturning |
| Vent Panel | Pressure relief | Open at design pressure |
| Flame Arrestor | Prevent flame propagation | Flow resistance acceptable |
| Drainage | Remove cryogenic spills | Slope away from equipment |

## 5. Structural Requirements

### 5.1 Design Criteria
| Parameter | Requirement | Standard |
|-----------|-------------|----------|
| Blast Overpressure | Design for 8× initial pressure | Conservative for deflagration |
| Safety Factor | 1.5 on ultimate strength | UFC 3-340-02 |
| Impulse Loading | Consider dynamic effects | Time-history analysis |
| Fragment Resistance | Withstand projected debris | Risk-based analysis |
| Thermal Protection | Radiation heat flux up to 250 kW/m² | H2 flame exposure |
| Service Life | 20 years minimum | Corrosion protection required |

### 5.2 Blast Wall Structural Design
- **Material**: Reinforced concrete (preferred) or steel
- **Thickness**: 200 mm minimum for concrete, 10 mm for steel
- **Reinforcement**: Both faces for concrete (flexure)
- **Foundation**: Adequate for overturning moment
- **Joints**: Design to prevent blast leakage

### 5.3 Venting System Design
- **Vent Size**: Per NFPA 68 nomographs or computational analysis
- **Vent Relief Pressure**: 0.1-0.5 bar typical
- **Vent Orientation**: Upward or away from occupied areas
- **Duct Length**: Minimize (increases back pressure)
- **Flame Arrestor**: If required, design for flow rate

### 5.4 Analysis Methods
| Method | Application | Software |
|--------|-------------|----------|
| Empirical (NFPA 68) | Simple geometries, well-vented | Charts, spreadsheets |
| CFD Simulation | Complex geometries, confinement | FLACS, AutoReaGas |
| FEA Blast Analysis | Structural response | LS-DYNA, ABAQUS/Explicit |
| Risk Assessment | Consequence analysis | Quantitative Risk Assessment |

### 5.5 Emergency Scenarios
| Scenario | Design Consideration |
|----------|---------------------|
| Internal Deflagration | Vent sizing, wall strength |
| External Vapor Cloud | Separation distance, ignition sources |
| LH2 Spill and Ignition | Drainage, blast wall placement |
| Jet Fire | Thermal radiation, safe distances |
| BLEVE (unlikely for LH2) | Catastrophic failure, fragmentation |

## 6. Cross-References
- Related ATA Chapters: ATA 03-00-06 (GSE Engineering)
- Parent Document: 03-50_Structures
- Related: 03-50-02 (H2 GSE Structures), 03-50-05-01A (Enclosures/Cabinets)

## 7. Revision History
| Rev | Date | Author | Description |
|-----|------|--------|-------------|
| A | 2025-12-08 | AMPEL360 Documentation Team | Initial release |

---

## Document Control

- **Document ID:** 03-50-05-03A
- **Version:** A
- **Status:** Active
- **Last Updated:** 2025-12-08
- **Repository:** AMPEL360-BWB-H2-Hy-E
- **Owner:** AMPEL360 GSE Structures Team

---

*Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.*
