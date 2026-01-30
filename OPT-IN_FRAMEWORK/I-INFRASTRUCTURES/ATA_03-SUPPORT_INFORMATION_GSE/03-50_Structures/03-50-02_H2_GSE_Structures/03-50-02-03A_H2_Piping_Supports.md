# 03-50-02-03A - H2 Piping Supports

## 1. Purpose
This document specifies the design requirements for structural supports of hydrogen (gaseous and liquid) piping systems in Ground Support Equipment (GSE). It addresses the unique challenges of supporting cryogenic piping with thermal contraction, high-pressure requirements, and safety considerations for hydrogen service.

## 2. Scope
This specification covers:
- LH2 transfer piping supports (-253°C)
- GH2 high-pressure piping supports (up to 700 bar)
- Thermal expansion/contraction accommodation
- Vibration isolation and seismic restraints
- Support materials and attachment methods
- Safety and emergency disconnect systems

## 3. Applicable Documents
- ASME B31.12 (Hydrogen Piping and Pipelines)
- ASME B31.3 (Process Piping)
- EN 13480 (Metallic Industrial Piping)
- MSS SP-58 (Pipe Hangers and Supports - Materials, Design, Manufacture, Selection, Application, and Installation)
- MSS SP-69 (Pipe Hangers and Supports - Selection and Application)
- SAE AS6968 (Hydrogen Aircraft Refueling)
- Reference: 03-50-02-01A (LH2 Tank Structures), 03-50-02-02A (Cryogenic Vessel Design)

## 4. Structural Description

### 4.1 Overview
Hydrogen piping support systems must accommodate extreme temperature ranges, prevent hydrogen embrittlement, allow for thermal movement, resist seismic and wind loads, and minimize heat transfer into cryogenic lines. Support design is critical for system integrity and safety.

### 4.2 Support Types and Applications

| Support Type | Application | Load Capacity | Notes |
|--------------|-------------|---------------|-------|
| Rigid Hanger | Vertical piping, fixed points | High (up to 50 kN) | No vertical movement allowed |
| Spring Hanger | Thermal expansion accommodation | Variable (1-50 kN) | Constant or variable spring |
| Sliding Support | Horizontal piping expansion | Moderate | PTFE or roller slides |
| Guided Support | Controlled movement direction | High | Prevents lateral displacement |
| Anchor | Fixed point, zero movement | Very high | Resists all forces/moments |
| Snubber | Dynamic restraint (seismic/wind) | High (50-200 kN) | Allows slow thermal movement |

### 4.3 Material Selection for Supports

#### 4.3.1 Cryogenic Service (-253°C to -100°C)
| Component | Material | Specification | Notes |
|-----------|----------|---------------|-------|
| Support Shoes | 304L/316L SS | ASTM A240 | Direct contact with cold pipe |
| Load-Bearing Pads | G-10/G-11 GFRP | ASTM D709 | Low thermal conductivity |
| Support Structure | 304 SS or 6061-T6 Al | ASTM A240, B209 | Ambient temperature |
| Insulation | Polyurethane foam | ASTM C591 | Protect support from cold |
| Fasteners | 316 SS | ASTM F593 | Cryogenic compatible |

#### 4.3.2 Gaseous H2 Service (Ambient to +80°C)
| Component | Material | Specification | Notes |
|-----------|----------|---------------|-------|
| Clamps/U-Bolts | 304/316 SS | ASTM A240 | H2 embrittlement resistant |
| Support Frames | Carbon steel (painted) | ASTM A36 | Economical, not in H2 contact |
| Fasteners | 316 SS or Grade 8 | ASTM F593, A325 | H2 compatible or isolated |

### 4.4 Thermal Movement Calculations

#### 4.4.1 LH2 Piping Contraction
| Parameter | Value | Application |
|-----------|-------|-------------|
| Operating Temperature | -253°C | Liquid hydrogen |
| Installation Temperature | +20°C | Typical ambient |
| Temperature Change (ΔT) | -273K | 
| Thermal Contraction (304 SS) | 0.31% | ΔL = α × L × ΔT |
| Example: 10 m pipe | 31 mm contraction | Significant movement |

**Design Rule**: Provide expansion loops, bellows, or sliding supports to accommodate movement.

#### 4.4.2 Support Spacing

| Pipe Size (DN) | Schedule | Max Span (LH2) | Max Span (GH2) | Notes |
|----------------|----------|----------------|----------------|-------|
| 25 (1") | 40 | 2.0 m | 3.0 m | Increased weight when cold |
| 50 (2") | 40 | 3.0 m | 4.5 m | 
| 100 (4") | 40 | 4.5 m | 6.0 m |
| 150 (6") | 40 | 5.5 m | 7.5 m |
| 200 (8") | 40 | 6.5 m | 9.0 m |

**Note**: LH2 spacing reduced due to insulation weight and thermal stress concerns.

### 4.5 Load Analysis for Piping Supports

#### 4.5.1 Load Components
| Load Type | Description | Typical Magnitude |
|-----------|-------------|-------------------|
| Dead Load (DL) | Pipe + fluid + insulation | Per material density |
| Thermal Load (T) | Expansion/contraction forces | FEA or expansion analysis |
| Pressure Thrust | Unbalanced forces at bends | P × A (area) |
| Wind Load (W) | Per ASCE 7 | 1.0-2.5 kPa on projected area |
| Seismic Load (E) | Per response spectrum | Site-specific |
| Impact Load (I) | Accidental loads | 1.5× static equivalent |

#### 4.5.2 Load Combinations (ASME B31.12)
1. **Normal**: DL + T
2. **Operating + Wind**: DL + T + W
3. **Operating + Seismic**: DL + T + E
4. **Occasional**: 1.2 DL + 1.0 T + 1.0 E
5. **Emergency**: DL + T + I (hydrogen release/impact)

### 4.6 Vibration and Dynamic Considerations

| Source | Frequency Range | Mitigation |
|--------|----------------|------------|
| Pump/Compressor | 10-60 Hz | Vibration isolators, rigid supports near source |
| Flow-Induced | 1-20 Hz | Avoid resonance with piping natural frequency |
| Pressure Pulsation | Varies | Pulsation dampeners, flexible hose sections |
| Seismic | 0.5-10 Hz | Snubbers, seismic bracing |

**Design Criterion**: Support system natural frequency > 2× excitation frequency

## 5. Structural Requirements

### 5.1 Support Design Criteria
| Parameter | Requirement | Standard |
|-----------|-------------|----------|
| Safety Factor (static) | 2.0 on yield | ASME B31.12 |
| Safety Factor (dynamic) | 1.5 on yield | ASME B31.12 |
| Deflection Limit | < 6 mm at any support | Prevent excessive bending |
| Pipe Stress (sustained) | ≤ 0.75 Sh | ASME B31.12 |
| Pipe Stress (occasional) | ≤ 1.33 Sh | ASME B31.12 |
| Thermal Conductivity (insulating supports) | < 0.5 W/m·K | Minimize heat leak |

### 5.2 Cryogenic Support Heat Leak
| Support Type | Heat Leak per Support | Design Goal |
|--------------|----------------------|-------------|
| Rigid Support (no insulation) | 5-20 W | Use only where necessary |
| Insulated Rigid Support | 1-5 W | Standard for LH2 |
| Low-Conductivity Support (G-10 pads) | 0.5-2 W | Preferred for stationary piping |

**Total Support Heat Leak Budget**: < 10% of piping heat leak

### 5.3 Seismic Design Requirements
| Component | Seismic Force | Restraint Type |
|-----------|---------------|----------------|
| Main Support | Per response spectrum analysis | Rigid anchor or snubber |
| Lateral Bracing | 0.5× vertical support reaction | Guide or snubber |
| Vertical Restraint | Prevent uplift (0.2g vertical) | Hold-down clamp |

**Seismic Category**: GSE piping typically Seismic Design Category D (high importance)

### 5.4 Inspection and Testing
| Activity | Frequency | Acceptance Criteria |
|----------|-----------|---------------------|
| Visual Inspection | Monthly (during operation) | No visible damage, corrosion, displacement |
| Support Movement Check | After thermal cycles | Movement within predicted range |
| Torque Check (fasteners) | Annually | Per installation specification |
| NDT (welds on critical supports) | Initial + after major event | Per ASME B31.12 |
| Load Test (spring hangers) | Initial calibration | ±5% of design load |

## 6. Cross-References
- Related ATA Chapters:
  - ATA 03-00-06 (GSE Engineering)
  - ATA 03-00-13 (Subsystems & Components)
- Parent Document: 03-50_Structures
- Related Documents:
  - 03-50-02-01A (LH2 Tank Structures)
  - 03-50-02-02A (Cryogenic Vessel Design)
  - 03-50-02-04A (Insulation Structures)
  - 03-50-06-04A (Cryogenic Stress Analysis)

## 7. Revision History
| Rev | Date | Author | Description |
|-----|------|--------|-------------|
| A | 2025-12-08 | AMPEL360 Documentation Team | Initial release |

---

## Document Control

- **Document ID:** 03-50-02-03A
- **Version:** A
- **Status:** Active
- **Last Updated:** 2025-12-08
- **Repository:** AMPEL360-BWB-H2-Hy-E
- **Owner:** AMPEL360 GSE Structures Team

---

*Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.*
