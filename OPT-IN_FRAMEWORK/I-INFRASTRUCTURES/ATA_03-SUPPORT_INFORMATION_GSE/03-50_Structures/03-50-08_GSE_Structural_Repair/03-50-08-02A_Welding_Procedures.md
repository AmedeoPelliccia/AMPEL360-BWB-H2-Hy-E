# 03-50-08-02A - Welding Procedures

## 1. Purpose
Specification for welding procedures for structural repairs of Ground Support Equipment (GSE), ensuring weld quality, integrity, and compliance with applicable codes for steel, stainless steel, and aluminum structures.

## 2. Scope
- Welding process selection
- Welding Procedure Specifications (WPS)
- Welder qualification
- H2 service welding requirements
- Quality control and inspection

## 3. Applicable Documents
- AWS D1.1 (Structural Welding Code - Steel)
- AWS D1.2 (Structural Welding Code - Aluminum)
- AWS D1.6 (Structural Welding Code - Stainless Steel)
- ASME IX (Welding and Brazing Qualifications)
- ASME B31.12 (Hydrogen Piping - Welding Requirements)

## 4. Structural Description

### 4.1 Welding Processes
| Process | Acronym | Application | Advantages | Limitations |
|---------|---------|-------------|------------|-------------|
| Shielded Metal Arc Welding | SMAW | Field repairs, thick sections | Portable, low equipment cost | Lower quality, slag removal |
| Gas Metal Arc Welding | GMAW (MIG) | General fabrication | High productivity, all positions | Requires shielding gas |
| Gas Tungsten Arc Welding | GTAW (TIG) | Stainless steel, aluminum, H2 | Highest quality, no slag | Slow, skilled operator required |
| Flux Cored Arc Welding | FCAW | Heavy fabrication | High deposition rate | Slag removal, fumes |

### 4.2 Material-Specific Welding
| Base Material | Preferred Process | Filler Material | Shielding Gas |
|---------------|------------------|-----------------|---------------|
| Carbon Steel (A36, A572) | SMAW, GMAW | E7018, ER70S-6 | CO₂ or Ar/CO₂ |
| Stainless Steel 304L | GTAW, GMAW | ER308L | Argon or Ar/2%CO₂ |
| Stainless Steel 316L | GTAW, GMAW | ER316L | Argon or Ar/2%CO₂ |
| Aluminum 6061-T6 | GTAW, GMAW | ER4043, ER5356 | Argon |
| H2 Service (any) | GTAW preferred | Match base metal | Argon (high purity) |

### 4.3 Welding Procedure Specification (WPS)
**Essential Variables** (per AWS D1.1, ASME IX):
- Base metal type and thickness
- Filler metal type and size
- Welding process
- Shielding gas type and flow rate
- Current type and range
- Voltage range
- Travel speed range
- Preheat and interpass temperature
- Post-weld heat treatment (if required)

### 4.4 Welder Qualification
| Standard | Qualification | Test | Validity |
|----------|--------------|------|----------|
| AWS D1.1 | Welder Performance Qualification (WPQ) | Coupon test (bend test, visual) | 6 months without welding |
| ASME IX | Welder Performance Qualification (WPQ) | Coupon test (RT, bend test) | 6 months without welding |
| AWS D1.6 | Same as D1.1 for stainless | Coupon test | 6 months |
| ASME B31.12 | Per ASME IX for H2 service | Coupon test + special H2 tests | 6 months |

### 4.5 H2 Service Welding
- **Process**: GTAW (TIG) preferred for root pass and critical welds
- **Filler**: Low-hydrogen (ER308L, ER316L for SS)
- **Shielding**: High-purity argon, backing gas for full-penetration welds
- **Inspection**: 100% visual + PT or MT, 100% UT or RT for critical welds
- **Testing**: Hydrostatic test + leak test (bubble test or sniffer)
- **Documentation**: Complete welding records, welder ID, WPS number

## 5. Structural Requirements

### 5.1 Weld Quality Requirements
| Property | Requirement | Standard |
|----------|-------------|----------|
| Visual Appearance | Smooth, uniform, no undercut >1 mm | AWS D1.1 |
| Weld Size | Per design (fillet size, penetration depth) | AWS D1.1 |
| Porosity | <3% of weld area (RT) | AWS D1.1 |
| Cracks | Not permitted | AWS D1.1 |
| Lack of Fusion | Not permitted | AWS D1.1 |
| Incomplete Penetration | Not permitted (full-penetration welds) | AWS D1.1 |

### 5.2 Weld Inspection
| Weld Type | Visual | NDT | Acceptance |
|-----------|--------|-----|------------|
| Structural Steel (non-critical) | 100% | 10% MT or PT | AWS D1.1 Table 6.1 |
| Structural Steel (critical) | 100% | 100% UT or MT | AWS D1.1 Table 6.1 |
| Pressure Vessels | 100% | 100% RT or UT | ASME VIII Appendix 12 |
| H2 Piping/Vessels | 100% | 100% PT + UT or RT | ASME B31.12 |
| Aluminum | 100% | PT or UT (for critical) | AWS D1.2 |

### 5.3 Preheat and PWHT
| Material | Preheat | Post-Weld Heat Treatment (PWHT) |
|----------|---------|----------------------------------|
| Carbon Steel < 12 mm | Not required | Not required |
| Carbon Steel > 12 mm | 100-150°C | Not required (structural) |
| Stainless Steel | Not required | Stress relief at 900°C (if required by code) |
| Aluminum | Not required | T6 heat treatment (if specified) |
| Pressure Vessels (per ASME) | Per code | Per code (often required) |

### 5.4 Common Weld Defects and Causes
| Defect | Cause | Prevention |
|--------|-------|------------|
| Porosity | Contamination, gas entrapment | Clean base metal, proper gas flow |
| Cracks | High restraint, hydrogen | Preheat, low-hydrogen electrodes |
| Lack of Fusion | Insufficient heat, poor technique | Increase current, proper angle |
| Undercut | Excessive current, speed | Reduce current, control technique |
| Distortion | Thermal expansion/contraction | Fixturing, weld sequence |

## 6. Cross-References
- Parent Document: 03-50_Structures
- Related: 03-50-08-01A (Structural Repair Manual), 03-50-08-04A (Cryogenic Vessel Repair)

## 7. Revision History
| Rev | Date | Author | Description |
|-----|------|--------|-------------|
| A | 2025-12-08 | AMPEL360 Documentation Team | Initial release |

---

## Document Control

- **Document ID:** 03-50-08-02A
- **Version:** A
- **Status:** Active
- **Last Updated:** 2025-12-08
- **Repository:** AMPEL360-BWB-H2-Hy-E
- **Owner:** AMPEL360 GSE Structures Team

---

*Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.*
