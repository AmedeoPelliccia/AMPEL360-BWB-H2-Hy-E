# 03-50-02-02A - Cryogenic Vessel Design

## 1. Purpose
This document establishes design principles, analytical methods, and acceptance criteria for cryogenic vessels operating at temperatures down to -253°C for LH2 service in Ground Support Equipment (GSE). It complements the LH2 tank structures specification with detailed design methodology.

## 2. Scope
This specification covers:
- Cryogenic design philosophy and codes
- Thermal-structural interaction
- Material behavior at cryogenic temperatures
- Insulation system design
- Vacuum system design
- Emergency conditions and failure modes

## 3. Applicable Documents
- ASME BPVC Section VIII Division 2 (Design by Analysis)
- EN 13458 series (Cryogenic Vessels)
- EN 13530 (Cryogenic Vessels - Large Transportable Vacuum Insulated Vessels)
- ISO 21009 (Cryogenic Vessels - Static Vacuum Insulated Vessels)
- ISO 20421 (Cryogenic Vessels - Large Transportable Vacuum Insulated Vessels)
- BS 5500 (Unfired Fusion Welded Pressure Vessels) - historical reference
- Reference: 03-50-02-01A (LH2 Tank Structures)

## 4. Structural Description

### 4.1 Overview
Cryogenic vessel design differs fundamentally from ambient-temperature pressure vessels due to extreme thermal gradients, material property changes, thermal stresses, and the necessity of superior insulation. Design must address both structural and thermal performance simultaneously.

### 4.2 Design Philosophy

| Principle | Approach | Rationale |
|-----------|----------|-----------|
| Failsafe Design | Leak-before-burst | Prevent catastrophic rupture |
| Thermal Isolation | Vacuum + MLI | Minimize boil-off |
| Material Selection | Austenitic SS or Al alloys | Ductility at -253°C |
| Support Design | Low thermal conductivity | Reduce heat leak |
| Relief System | Dual redundancy | Handle fire scenario |

### 4.3 Cryogenic Material Properties

#### 4.3.1 Stainless Steel (304L/316L)
| Property | Ambient (20°C) | Cryogenic (-196°C) | LH2 (-253°C) |
|----------|----------------|-------------------|--------------|
| Yield Strength | 205 MPa | 620 MPa | 760 MPa |
| Ultimate Strength | 515 MPa | 1100 MPa | 1270 MPa |
| Elongation | 40% | 35% | 30% |
| Charpy Impact | >100 J | >80 J | >60 J |
| Thermal Expansion | αₜ = 17.3×10⁻⁶/K | αₜ = 14.5×10⁻⁶/K | αₜ = 13.8×10⁻⁶/K |

**Key Observation**: Strength increases significantly at cryogenic temperatures while maintaining adequate ductility.

#### 4.3.2 Aluminum Alloys (5083-H116)
| Property | Ambient (20°C) | Cryogenic (-196°C) | LH2 (-253°C) |
|----------|----------------|-------------------|--------------|
| Yield Strength | 228 MPa | 415 MPa | 450 MPa |
| Ultimate Strength | 317 MPa | 510 MPa | 540 MPa |
| Elongation | 16% | 20% | 22% |
| Fracture Toughness | High | Excellent | Excellent |

**Advantage**: Aluminum alloys maintain or improve ductility at cryogenic temperatures.

### 4.4 Thermal Design Considerations

#### 4.4.1 Heat Leak Mechanisms
| Mechanism | Contribution | Control Method |
|-----------|--------------|----------------|
| Radiation | 40-50% | Multi-layer insulation (MLI) |
| Solid Conduction (supports) | 15-25% | Minimize contact area, use G-10/GFRP |
| Residual Gas Conduction | 10-20% | Maintain vacuum <10⁻⁴ mbar |
| Piping/Penetrations | 15-25% | Minimize number, add local insulation |

#### 4.4.2 Insulation Systems
| Type | Application | Performance (W/m²) | Notes |
|------|-------------|-------------------|-------|
| Multi-Layer Insulation (MLI) | Vacuum space | 0.1-0.5 | 20-80 layers aluminized mylar |
| Perlite Powder | Vacuum space (low-cost) | 1-3 | Simple but higher heat leak |
| Polyurethane Foam | Outer vessel exterior | 10-20 | Additional weather protection |
| Aerogel Blanket | Piping, complex shapes | 0.5-2 | Flexible, high-performance |

#### 4.4.3 Thermal Contraction Analysis
| Material | ΔL/L (20°C to -253°C) | Implication |
|----------|---------------------|-------------|
| 304L Stainless Steel | -0.31% | 3.1 mm per meter length |
| 6061-T6 Aluminum | -0.42% | 4.2 mm per meter length |
| Carbon Steel (A516) | -0.29% | 2.9 mm per meter length |

**Design Rule**: Support system must accommodate differential movement without overstressing inner vessel.

### 4.5 Vacuum System Design

#### 4.5.1 Vacuum Requirements
| Parameter | Specification | Purpose |
|-----------|---------------|---------|
| Initial Vacuum | <10⁻⁵ mbar | Before MLI effectiveness established |
| Operating Vacuum | <10⁻⁴ mbar | Maintain low thermal conductivity |
| Leak Rate | <10⁻⁹ mbar·L/s | Prevent vacuum degradation |
| Getter Material | Activated charcoal or molecular sieve | Absorb residual gases |

#### 4.5.2 Vacuum Port Design
- **Port Size**: DN 25-50 (1"-2") typical
- **Valve Type**: Bakeable all-metal valve
- **Burst Disk**: Protect against overpressure if vacuum lost
- **Vacuum Gauge**: Thermocouple or cold cathode type

### 4.6 Thermal-Structural Interaction

#### 4.6.1 Support System Load Cases
| Load Case | Inner Vessel Temp | Outer Vessel Temp | Support Stress |
|-----------|------------------|-------------------|----------------|
| Cold Fill | -253°C | +20°C | Maximum differential |
| Warm Hold | -253°C | -10°C (frost) | Steady-state |
| Emergency Warmup | -200°C to +20°C | +20°C | Thermal shock |
| Transport (mobile) | -253°C | +40°C (solar) | Maximum gradient |

#### 4.6.2 FEA Requirements
- **Software**: ANSYS, ABAQUS, or equivalent
- **Element Type**: 3D solid elements for complex geometry, shell for vessels
- **Thermal Analysis**: Steady-state for normal, transient for upset
- **Structural Analysis**: Linear elastic for design, plastic for limit load
- **Coupled Analysis**: Thermal-structural for support system

## 5. Structural Requirements

### 5.1 Design Criteria
| Criterion | Requirement | Verification Method |
|-----------|-------------|---------------------|
| Primary Stress | ≤ 2/3 Sy at temperature | ASME VIII-2 elastic analysis |
| Primary + Secondary Stress | ≤ 2 Sy | Shakedown analysis |
| Stress Intensity | ≤ 3 Sm | Fatigue evaluation |
| Buckling (outer vessel) | Safety factor ≥ 3.0 | ASME VIII-2 Part 4 |
| Support Stress | ≤ 0.5 Sy (cryogenic) | FEA + hand calculations |
| Deflection | Piping nozzle movement <6 mm | Ensure piping flexibility |

### 5.2 Pressure Cycling (Fatigue)
| Parameter | Specification | Standard |
|-----------|---------------|----------|
| Design Cycles | 10,000 minimum | Per customer requirements |
| Pressure Range | 0 to MAWP | Full range |
| Cycle Rate | Slow (hours) for LH2 | Thermal equilibrium |
| Fatigue Analysis Method | ASME VIII-2 Part 5 | Curve-based or fracture mechanics |
| Fatigue Safety Factor | 2.0 on cycles or 10 on stress | ASME VIII-2 |

### 5.3 Emergency Conditions

#### 5.3.1 Loss of Vacuum
- **Scenario**: Vacuum degrades to atmospheric pressure
- **Consequence**: Heat leak increases 100-1000×
- **Protection**: Inner vessel pressure relief, outer vessel overpressure protection
- **Analysis**: Inner vessel must withstand 24-hour boil-off pressure rise

#### 5.3.2 Fire Exposure
- **Scenario**: External fire (hydrocarbon pool fire)
- **Heat Flux**: 100-250 kW/m² per CGA S-1.3
- **Protection**: Pressure relief sized for fire case per API 520
- **Analysis**: Vessel must not rupture before relief activates

#### 5.3.3 Overpressure (Inner Vessel)
- **Scenario**: Relief valve failure
- **Design**: Burst pressure > 2× MAWP (safety factor > 3.5)
- **Material**: Adequate ductility to yield before fracture
- **Relief**: Dual relief valves with independent actuation

### 5.4 Testing and Certification
| Test | Requirement | Standard |
|------|-------------|----------|
| Hydrostatic (inner vessel) | 1.5× MAWP × 1 hour | ASME VIII-1 UG-99 |
| Pneumatic (outer vessel) | 1.15× design × hold | ASME VIII-1 UG-100 |
| Helium Leak Test | <10⁻⁹ mbar·L/s | EN 13458-2 |
| Cool-down Test | 3 cycles to -253°C | Verify thermal performance |
| Vacuum Performance | <10⁻⁴ mbar achieved | Measure vacuum quality |
| Boil-off Test | Measure heat leak | Verify insulation system |

## 6. Cross-References
- Related ATA Chapters:
  - ATA 03-00-06 (GSE Engineering)
- Parent Document: 03-50_Structures
- Related Documents:
  - 03-50-02-01A (LH2 Tank Structures)
  - 03-50-02-03A (H2 Piping Supports)
  - 03-50-02-04A (Insulation Structures)
  - 03-50-06-04A (Cryogenic Stress Analysis)
  - 03-50-08-04A (Cryogenic Vessel Repair)

## 7. Revision History
| Rev | Date | Author | Description |
|-----|------|--------|-------------|
| A | 2025-12-08 | AMPEL360 Documentation Team | Initial release |

---

## Document Control

- **Document ID:** 03-50-02-02A
- **Version:** A
- **Status:** Active
- **Last Updated:** 2025-12-08
- **Repository:** AMPEL360-BWB-H2-Hy-E
- **Owner:** AMPEL360 GSE Structures Team

---

*Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.*
