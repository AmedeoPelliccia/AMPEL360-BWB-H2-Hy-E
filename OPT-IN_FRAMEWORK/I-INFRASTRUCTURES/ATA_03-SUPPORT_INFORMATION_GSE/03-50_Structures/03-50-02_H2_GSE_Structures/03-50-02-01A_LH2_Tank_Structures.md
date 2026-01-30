# 03-50-02-01A - LH2 Tank Structures

## 1. Purpose
This document specifies the structural design requirements for Liquid Hydrogen (LH2) storage tanks used in Ground Support Equipment (GSE) for the AMPEL360 BWB-H2-Hy-E aircraft refueling and servicing operations. It addresses the unique challenges of cryogenic storage at -253°C.

## 2. Scope
This specification covers:
- Stationary LH2 storage tanks (ground-based)
- Mobile LH2 transport tanks (truck/trailer-mounted)
- Vacuum-insulated double-wall vessel design
- Structural supports and foundations
- Safety systems integration

## 3. Applicable Documents
- ASME BPVC Section VIII Division 1 (Pressure Vessels)
- ASME BPVC Section VIII Division 2 (Alternative Rules)
- EN 13458-1 (Cryogenic Vessels - Static Vacuum Insulated Vessels Part 1: Fundamental Requirements)
- EN 13458-2 (Part 2: Design, Fabrication, Inspection and Testing)
- ISO 21009-1 (Cryogenic Vessels - Static Vacuum Insulated Vessels)
- ASME B31.12 (Hydrogen Piping and Pipelines)
- NFPA 2 (Hydrogen Technologies Code)
- SAE AIR7601 (Guidelines for Handling Liquid Hydrogen)
- Reference: 03-50-01-01A (GSE Structural Design), 03-50-02-02A (Cryogenic Vessel Design)

## 4. Structural Description

### 4.1 Overview
LH2 storage tanks are double-wall vacuum-insulated pressure vessels designed to maintain liquid hydrogen at -253°C with minimal boil-off. The structural system includes the inner vessel (cryogenic barrier), outer vessel (vacuum jacket), insulation, and support system.

### 4.2 Tank Configuration

#### 4.2.1 Vessel Geometry
| Parameter | Typical Range | Notes |
|-----------|---------------|-------|
| Capacity | 5,000 - 50,000 liters | Based on aircraft demand |
| Operating Pressure | 3-10 bar | Balance boil-off vs. tank weight |
| Inner Vessel Material | 304L or 316L stainless steel | Austenitic for cryogenic service |
| Outer Vessel Material | Carbon steel or 304 SS | Vacuum side, ambient temperature |
| Geometry | Vertical or horizontal cylindrical | Vertical preferred for stationary |

#### 4.2.2 Double-Wall Construction
| Component | Function | Material |
|-----------|----------|----------|
| Inner Vessel | Contains LH2 at -253°C | 304L/316L SS, 3-12 mm thick |
| Insulation | Reduces heat leak | Multi-layer insulation (MLI) or perlite |
| Vacuum Space | Thermal barrier | 20-50 mm gap, <10⁻⁴ mbar |
| Outer Vessel | Maintains vacuum | Carbon steel or SS, 6-20 mm thick |
| Support System | Transmits loads with minimal heat leak | Low-conductivity supports |

### 4.3 Structural Design Requirements

#### 4.3.1 Inner Vessel (Cryogenic)
| Design Parameter | Specification | Standard |
|------------------|---------------|----------|
| Design Temperature | -253°C to +50°C | ASME VIII |
| Design Pressure | 1.5× MAWP (15 bar typical) | ASME VIII |
| Material Toughness | >27J at -196°C (Charpy V-notch) | ASME VIII-1 UCS-66 |
| Weld Joint Efficiency | 0.85 (spot radiography) to 1.0 (full RT) | ASME VIII-1 UW-11 |
| Corrosion Allowance | 0 mm (stainless in LH2 service) | ASME VIII-1 UCS-25 |
| Head Type | 2:1 elliptical or hemispherical | ASME VIII-1 UG-32 |

#### 4.3.2 Outer Vessel (Vacuum Jacket)
| Design Parameter | Specification | Standard |
|------------------|---------------|----------|
| Design Temperature | -40°C to +50°C | ASME VIII |
| Design Pressure | Full vacuum (external) + 1 bar (internal) | ASME VIII-1 UG-28 |
| Buckling Check | Factor of safety ≥ 3.0 | ASME VIII-2 Part 4 |
| Material | Carbon steel (A516 Gr 70) or 304 SS | ASME II |
| External Pressure Rings | As required by UG-29 | ASME VIII-1 |

### 4.4 Support System Design

#### 4.4.1 Inner Vessel Supports
| Support Type | Description | Heat Leak Consideration |
|--------------|-------------|------------------------|
| Bottom Support | Ring support or legs | Minimize contact area |
| Side Supports (horizontal) | Saddles with low-conductivity pads | G-10 or similar low-k material |
| Top Suspension (vertical) | Tie rods from top head | Tension-only, minimize cross-section |
| Seismic Restraints | Lateral bracing | Allow thermal contraction |

**Heat Leak Budget**: Total support heat leak < 10% of total vessel heat leak

#### 4.4.2 External Support Structure
| Component | Design Load | Material |
|-----------|-------------|----------|
| Foundation | 1.5× (DL + LL + seismic) | Reinforced concrete |
| Anchor Bolts | Tension and shear per AISC | ASTM A307 or A325 |
| Base Plate | Distribute foundation loads | ASTM A36 steel plate |
| Seismic Isolators | As required by analysis | Elastomeric or friction |

### 4.5 Thermal Considerations

#### 4.5.1 Thermal Contraction
| Parameter | Value | Implication |
|-----------|-------|-------------|
| LH2 Temperature | -253°C | 
| Thermal Contraction (SS 304L) | ~0.3% linear | 3 mm per meter |
| Differential Movement | Inner vs outer vessel | Sliding supports required |
| Piping Flexibility | Expansion loops or bellows | ASME B31.12 |

#### 4.5.2 Heat Leak Analysis
| Source | Typical Heat Leak | Mitigation |
|--------|------------------|------------|
| Insulation | 40-60% of total | Optimize MLI layers or use perlite |
| Support System | 10-20% | Use low-conductivity materials |
| Piping Penetrations | 20-30% | Minimize penetrations, add MLI |
| Residual Gas Conduction | 5-10% | Maintain vacuum <10⁻⁴ mbar |

**Design Target**: Total heat leak < 1 W/m² (stationary), < 5 W/m² (mobile)

## 5. Structural Requirements

### 5.1 Design Criteria Summary
| Requirement | Value | Standard |
|-------------|-------|----------|
| Inner Vessel Design Pressure | 15 bar (typical) | ASME VIII |
| Inner Vessel Test Pressure | 22.5 bar (1.5× DP) | ASME VIII |
| Outer Vessel External Pressure | 1 bar (full vacuum) | ASME VIII-1 UG-28 |
| Seismic Design | Per site-specific analysis | ASCE 7 |
| Wind Load | Per local code | ASCE 7 |
| Safety Factor (pressure) | 3.5 on burst | ASME VIII |
| Safety Factor (support) | 2.0 on yield | AISC 360 |
| Vacuum Integrity | Leak rate < 10⁻⁹ mbar·L/s | EN 13458 |
| Service Life | 20 years minimum | Per specification |

### 5.2 Pressure Relief Requirements
| System | Relief Capacity | Standard |
|--------|----------------|----------|
| Inner Vessel | Handle fire exposure scenario | API 520, CGA S-1.3 |
| Outer Vessel | Vacuum loss scenario | ASME VIII |
| Set Pressure | 1.1× MAWP | ASME VIII |
| Relief Valve Sizing | Per CGA S-1.2 (LH2 specific) | CGA S-1.2 |

### 5.3 Inspection and Testing Requirements
| Test/Inspection | Requirement | Frequency |
|-----------------|-------------|-----------|
| Hydrostatic Test | 1.5× MAWP, inner vessel | Initial certification |
| Pneumatic Test | 1.15× MAWP, outer vessel | Initial certification |
| Vacuum Leak Test | <10⁻⁹ mbar·L/s | Initial + every 5 years |
| Visual Inspection | External condition | Annual |
| NDT (UT, RT) | Critical welds | Per ASME VIII |
| Vacuum Pressure Check | Monitor degradation | Continuous (instrumented) |

### 5.4 Material Certification
- All materials require certified Material Test Reports (MTR)
- Impact testing at -196°C for inner vessel materials
- Weld procedure qualification per ASME IX
- Hydrogen embrittlement assessment per ASME B31.12

## 6. Cross-References
- Related ATA Chapters:
  - ATA 03-00-06 (GSE Engineering)
  - ATA 03-00-13 (Subsystems & Components)
- Parent Document: 03-50_Structures
- Related Documents:
  - 03-50-01-03A (GSE Materials Selection)
  - 03-50-02-02A (Cryogenic Vessel Design)
  - 03-50-02-03A (H2 Piping Supports)
  - 03-50-02-04A (Insulation Structures)
  - 03-50-06-04A (Cryogenic Stress Analysis)

## 7. Revision History
| Rev | Date | Author | Description |
|-----|------|--------|-------------|
| A | 2025-12-08 | AMPEL360 Documentation Team | Initial release |

---

## Document Control

- **Document ID:** 03-50-02-01A
- **Version:** A
- **Status:** Active
- **Last Updated:** 2025-12-08
- **Repository:** AMPEL360-BWB-H2-Hy-E
- **Owner:** AMPEL360 GSE Structures Team

---

*Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.*
