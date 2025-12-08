# 03-50-06-04A - Cryogenic Stress Analysis

## 1. Purpose
Specification for thermal-structural stress analysis of cryogenic systems in Ground Support Equipment (GSE), particularly LH2 (-253°C) storage and transfer systems, addressing thermal contraction, thermal stress, and material behavior at extreme temperatures.

## 2. Scope
- Thermal-structural coupled analysis
- Thermal contraction effects
- Thermal stress in vessels and piping
- Cryogenic material properties
- Support system design for thermal cycling
- Cool-down and warm-up transients

## 3. Applicable Documents
- ASME VIII-2 Part 5 (Design by Analysis)
- EN 13458-2 (Cryogenic Vessels - Design, Fabrication, Inspection, and Testing)
- ISO 21009-1 (Cryogenic Vessels - Static Vacuum Insulated Vessels)
- ASME B31.3 Chapter IX (High-Pressure Piping)
- AWS D1.1 (Structural Welding Code)
- Reference: 03-50-02-02A (Cryogenic Vessel Design)

## 4. Structural Description

### 4.1 Cryogenic Thermal Effects
| Effect | Magnitude @ -253°C | Impact |
|--------|-------------------|--------|
| Thermal Contraction (SS 304L) | -0.31% linear | 3.1 mm/m |
| Thermal Contraction (Al 6061) | -0.42% linear | 4.2 mm/m |
| Differential Contraction (inner/outer vessel) | Significant | Support system must accommodate |
| Thermal Stress | Up to yield in constrained regions | FEA required |
| Material Property Changes | Strength increases, ductility maintained | Austenitic SS, Al alloys suitable |

### 4.2 Thermal Analysis Types
| Analysis | Purpose | Method |
|----------|---------|--------|
| Steady-State Thermal | Temperature distribution at equilibrium | FEA (thermal solver) |
| Transient Thermal | Cool-down/warm-up time history | FEA (transient thermal) |
| Heat Leak Calculation | Insulation performance | Hand calc or FEA |
| Thermal-Structural Coupled | Stress due to thermal gradients | FEA (sequential or coupled) |
| Fatigue (thermal cycling) | Accumulate damage from cycles | S-N curves or crack growth |

### 4.3 Material Properties at Cryogenic Temperature
| Material | Property | +20°C | -196°C (LN2) | -253°C (LH2) |
|----------|----------|-------|-------------|--------------|
| SS 304L | Yield Strength (MPa) | 205 | 620 | 760 |
| | Thermal Expansion (10⁻⁶/K) | 17.3 | 14.5 | 13.8 |
| | Thermal Conductivity (W/m·K) | 16 | 11 | 9 |
| | Elastic Modulus (GPa) | 193 | 210 | 215 |
| Al 6061-T6 | Yield Strength (MPa) | 275 | 415 | 450 |
| | Thermal Expansion (10⁻⁶/K) | 23.6 | 18.5 | 17.2 |
| | Thermal Conductivity (W/m·K) | 167 | 90 | 75 |
| | Elastic Modulus (GPa) | 69 | 76 | 78 |

### 4.4 Thermal Boundary Conditions
| Surface | Temperature (°C) | Heat Transfer Coefficient (W/m²·K) |
|---------|------------------|----------------------------------|
| LH2 Wetted (inner vessel) | -253 | 500-5000 (boiling) |
| Vacuum Side (inner vessel) | -253 to -200 | Radiation only (MLI) |
| Vacuum Side (outer vessel) | -10 to +20 | Radiation only |
| Ambient Exposed (outer vessel) | +20 | 10-25 (natural convection) |
| Piping (internal LH2 flow) | -253 | 1000-10000 (forced convection) |

### 4.5 Support System Thermal Design
- **Sliding Supports**: Allow horizontal movement during contraction
- **Low-Conductivity Pads**: G-10/G-11 GFRP minimize heat leak
- **Flexible Piping**: Expansion loops or bellows
- **Seismic Restraints**: Accommodate thermal movement under normal operation
- **Insulation at Supports**: Prevent cold bridging to external structure

## 5. Structural Requirements

### 5.1 Thermal Stress Limits (ASME VIII-2)
| Stress Category | Limit (ASME VIII-2) | Application |
|-----------------|---------------------|-------------|
| Primary Membrane (P_m) | ≤ S_m | General (1.5×S_y/3) |
| Primary Membrane + Bending (P_L) | ≤ 1.5 S_m | Local (vessel shells) |
| Primary + Secondary (P_L + Q) | ≤ 3 S_m | Shakedown (thermal stress) |
| Peak Stress (P_L + Q + F) | Fatigue evaluation | Cyclic loading |

**Note**: Thermal stresses are typically categorized as secondary (Q), allowing higher limits.

### 5.2 Design for Thermal Cycling
- **Cool-Down Rate**: ≤ 50°C/hour (thick sections >25 mm)
- **Warm-Up Rate**: ≤ 30°C/hour (prevent thermal shock)
- **Number of Cycles**: 10,000 minimum for LH2 systems
- **Fatigue Analysis**: Required for thermal cycling + pressure cycling

### 5.3 FEA Modeling for Cryogenic Analysis
1. **Thermal Model**:
   - Apply boundary conditions (temperature, heat flux, convection)
   - Include insulation (MLI, foam) with effective conductivity
   - Model supports with thermal contact resistance
   - Solve for steady-state or transient temperature field

2. **Structural Model**:
   - Import temperature field from thermal analysis
   - Apply pressure loads (if simultaneous)
   - Use temperature-dependent material properties
   - Solve for stress, strain, deflection

3. **Results Interpretation**:
   - Verify stress intensity (P_L + Q) ≤ 3 S_m
   - Check support displacements (accommodate or restrain?)
   - Evaluate fatigue if cycling

### 5.4 Validation and Testing
| Test | Purpose | Acceptance |
|------|---------|------------|
| Cool-Down Test | Verify thermal performance, measure strains | Strains within predicted ±20% |
| Thermal Cycling | Validate fatigue life | No cracks after 3× design cycles |
| Heat Leak Measurement | Verify insulation performance | Heat leak ≤ design value + 10% |
| Pressure Test (cold) | Structural integrity at -253°C | No leakage, no permanent deformation |

### 5.5 Emergency Scenarios
| Scenario | Thermal Effect | Structural Response |
|----------|---------------|---------------------|
| Loss of Vacuum | 100× heat leak increase | Rapid LH2 boil-off, pressure rise |
| LH2 Spill on Warm Surface | Rapid cooling (-273°C ΔT) | Thermal shock, potential brittle fracture |
| Rapid Warm-Up (heater failure) | +50°C/hour | High thermal stress, potential yielding |
| Fire Exposure (external) | +500°C on outer vessel | Vacuum degradation, inner vessel pressure rise |

## 6. Cross-References
- Parent Document: 03-50_Structures
- Related: 03-50-02-01A (LH2 Tank Structures), 03-50-02-02A (Cryogenic Vessel Design), 03-50-06-01A (FEA Structural Analysis)

## 7. Revision History
| Rev | Date | Author | Description |
|-----|------|--------|-------------|
| A | 2025-12-08 | AMPEL360 Documentation Team | Initial release |

---

## Document Control

- **Document ID:** 03-50-06-04A
- **Version:** A
- **Status:** Active
- **Last Updated:** 2025-12-08
- **Repository:** AMPEL360-BWB-H2-Hy-E
- **Owner:** AMPEL360 GSE Structures Team

---

*Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.*
