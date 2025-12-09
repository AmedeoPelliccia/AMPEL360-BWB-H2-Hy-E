# 03-50-08-03A - Composite Repair

## 1. Purpose
Specification for composite (fiber-reinforced polymer) repair of non-critical Ground Support Equipment (GSE) structural components, including cracks, corrosion damage, and reinforcement applications.

## 2. Scope
- Composite repair design and application
- Surface preparation
- Composite materials and lay-up
- Curing and quality control
- Limitations and restrictions

## 3. Applicable Documents
- AC 43.13-1B Chapter 5 (Aircraft Composite Repairs)
- ASTM D7565 (Determining Tensile Properties of Fiber Reinforced Polymer Matrix Composites Used for Strengthening of Civil Structures)
- ACI 440.2R (Guide for the Design and Construction of Externally Bonded FRP Systems for Strengthening Concrete Structures)
- ISO 24817 (Petroleum, Petrochemical and Natural Gas Industries - Composite Repairs for Pipework)

## 4. Structural Description

### 4.1 Composite Repair Systems
| System | Matrix | Reinforcement | Cure | Application |
|--------|--------|---------------|------|-------------|
| Wet Lay-Up | Epoxy resin | Carbon or glass fabric | Room temp or elevated | Cracks, minor corrosion |
| Pre-Preg | Pre-impregnated resin | Carbon or glass fabric | Elevated temp (autoclave) | High-quality repairs |
| Resin Infusion | Epoxy resin | Dry fabric | Vacuum-assisted | Large areas |
| Fiberglass Wrap | Polyester or epoxy | E-glass fabric | Room temp | Piping, cylindrical structures |

### 4.2 Material Selection
| Fiber Type | Tensile Strength (GPa) | Modulus (GPa) | Cost | Application |
|------------|----------------------|---------------|------|-------------|
| Carbon (high-strength) | 3.5-4.5 | 230-240 | High | High-stress areas, weight-critical |
| Carbon (high-modulus) | 2.5-3.5 | 300-400 | Very High | Stiffness-critical |
| E-Glass | 3.5 | 70 | Low | General repairs, economical |
| S-Glass | 4.5 | 85 | Moderate | Higher performance than E-glass |
| Aramid (Kevlar) | 3.0 | 125 | Moderate | Impact resistance |

### 4.3 Repair Configurations
| Configuration | Application | Design |
|---------------|-------------|--------|
| Single-Sided Patch | External repair, access from one side | Thicker patch, tapered edges |
| Double-Sided Patch | Crack repair, access from both sides | Balanced lay-up |
| Wrap (cylindrical) | Piping, tanks | Hoop orientation for pressure |
| Reinforcement (flat) | Strengthen weak section | 0°/90° lay-up or unidirectional |

### 4.4 Design Considerations
- **Stress Analysis**: FEA to determine required patch thickness
- **Load Transfer**: Taper patch edges (1:20-1:50 slope) to minimize peel stress
- **Fiber Orientation**: Align with principal stress direction
- **Environmental**: Temperature, moisture, UV exposure
- **Fatigue**: Limited fatigue data; use conservative design

### 4.5 Limitations
- **Not Approved For**:
  - Primary structural members (without engineering evaluation)
  - H2 pressure vessels (not code-approved)
  - Cryogenic service (matrix brittleness)
  - High-temperature areas (>120°C for most epoxies)
- **Approved For** (with evaluation):
  - Non-critical secondary structure
  - Crack arrest (stop-gap until permanent repair)
  - Corrosion reinforcement (non-pressure)
  - Reinforcement of overloaded areas

## 5. Structural Requirements

### 5.1 Surface Preparation
1. **Clean**: Remove paint, grease, oil (solvent wipe)
2. **Abrade**: Grind or grit blast to achieve bonding surface (roughness Ra 25-100 µm)
3. **Profile**: Taper crack edges, remove sharp corners
4. **Clean Again**: Remove dust and residue
5. **Dry**: Ensure surface is dry (moisture <3% by weight)
6. **Prime**: Apply primer if specified (typically not required for epoxy on metal)

### 5.2 Lay-Up Procedure
1. **Cut Fabric**: Layers per design, largest on bottom (against metal)
2. **Mix Resin**: Per manufacturer instructions, pot life typically 30-60 minutes
3. **Apply Resin**: Saturate each layer, remove air bubbles (squeegee or roller)
4. **Stack Layers**: Build up to design thickness, stagger seams
5. **Consolidate**: Apply pressure (vacuum bag or roller) to remove voids
6. **Cure**: Room temperature (7 days) or elevated temperature (per resin data sheet)

### 5.3 Quality Control
| Parameter | Requirement | Test Method |
|-----------|-------------|-------------|
| Fiber Volume Fraction | 50-65% | Burn-off test (ASTM D2584) |
| Void Content | <2% | Ultrasonic or visual (translucent samples) |
| Bond Strength | > 10 MPa (adhesion) | Pull-off test (ASTM D4541) |
| Cure | Tg > service temperature + 20°C | DSC (Differential Scanning Calorimetry) |
| Thickness | ± 10% of design | Ultrasonic or micrometer |

### 5.4 Inspection
- **Visual**: Uniform appearance, no dry spots, no wrinkles
- **Tap Test**: Coin tap to detect delamination (dull sound = defect)
- **Ultrasonic (UT)**: Detect voids, delamination (if critical)
- **Pull-Off Test**: Adhesion test on witness panel or edge of repair

### 5.5 Post-Repair Monitoring
- **Initial**: Inspect at 1 week, 1 month, 6 months
- **Routine**: Annual visual inspection
- **Loading**: Monitor for disbonding under cyclic loading
- **Environmental**: Check for UV degradation, moisture ingress

## 6. Cross-References
- Parent Document: 03-50_Structures
- Related: 03-50-08-01A (Structural Repair Manual), 03-50-06-02A (Fatigue Analysis)

## 7. Revision History
| Rev | Date | Author | Description |
|-----|------|--------|-------------|
| A | 2025-12-08 | AMPEL360 Documentation Team | Initial release |

---

## Document Control

- **Document ID:** 03-50-08-03A
- **Version:** A
- **Status:** Active
- **Last Updated:** 2025-12-08
- **Repository:** AMPEL360-BWB-H2-Hy-E
- **Owner:** AMPEL360 GSE Structures Team

---

*Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.*
