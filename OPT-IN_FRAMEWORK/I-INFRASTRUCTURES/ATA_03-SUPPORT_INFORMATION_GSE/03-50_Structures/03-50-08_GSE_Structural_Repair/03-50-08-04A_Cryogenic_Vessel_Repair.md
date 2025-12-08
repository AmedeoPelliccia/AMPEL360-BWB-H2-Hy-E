# 03-50-08-04A - Cryogenic Vessel Repair

## 1. Purpose
Specification for repair of cryogenic pressure vessels used in LH2 Ground Support Equipment (GSE), addressing the unique challenges of welding, inspection, and testing at extreme low temperatures.

## 2. Scope
- Repair of LH2 storage tanks and vessels
- Weld repair procedures for cryogenic service
- Post-repair testing and certification
- Return-to-service requirements
- Special considerations for -253°C service

## 3. Applicable Documents
- ASME BPVC Section VIII (Pressure Vessels)
- ASME IX (Welding and Brazing Qualifications)
- EN 13458-2 (Cryogenic Vessels - Design, Fabrication, Inspection and Testing)
- ISO 21009 (Cryogenic Vessels - Static Vacuum Insulated Vessels)
- ASME B31.12 (Hydrogen Piping and Pipelines)
- AWS D1.6 (Structural Welding Code - Stainless Steel)

## 4. Structural Description

### 4.1 Common Cryogenic Vessel Repairs
| Damage Type | Typical Repair | Procedure |
|-------------|---------------|-----------|
| Crack in Inner Vessel | Weld repair | Remove crack, weld, PWHT if required, test |
| Corrosion/Pitting | Weld build-up | Grind out, weld fill, blend, test |
| Nozzle Leak | Re-weld or replace | Cut out, weld new nozzle, full inspection |
| Vacuum Degradation | Re-evacuate, getter replacement | Leak test, repair leaks, pump down |
| Support Failure | Replace support | Non-welded repair preferred (minimize heat input) |
| Insulation Damage | Replace MLI | Remove outer layers, replace, re-evacuate |

### 4.2 Materials for Cryogenic Repair
| Material | Application | Filler Metal | Notes |
|----------|-------------|--------------|-------|
| 304L Stainless Steel | Inner vessel (common) | ER308L | Excellent cryogenic properties |
| 316L Stainless Steel | Inner vessel (enhanced corrosion) | ER316L | Superior corrosion resistance |
| 5083 Aluminum | Lightweight vessels | ER5183, ER5356 | Good cryogenic ductility |
| 9% Nickel Steel | Large LH2 tanks | ENiCrMo-3 | Excellent toughness at -196°C |

### 4.3 Welding Procedures for Cryogenic Vessels
- **Process**: GTAW (TIG) for root and critical passes, GMAW for fill/cap
- **Filler Metal**: Low ferrite (<5 FN) for 304L/316L to avoid embrittlement
- **Shielding**: Argon (high purity), backing gas for full-penetration welds
- **Interpass Temperature**: < 150°C (minimize heat input, reduce distortion)
- **Cleaning**: Between passes (stainless wire brush, solvent wipe)
- **Inspection**: 100% PT between passes, final UT or RT

### 4.4 Post-Weld Heat Treatment (PWHT)
| Code | PWHT Requirement | Temperature | Purpose |
|------|-----------------|-------------|---------|
| ASME VIII-1 (SS) | Not required (typically) | N/A | Austenitic SS self-stress-relieves |
| ASME VIII-1 (9% Ni) | Required | 580-620°C | Stress relief |
| ASME VIII-2 | Per design analysis | Variable | Reduce residual stress if required |
| EN 13458 | Per risk assessment | Variable | Stress relief if cyclic loading |

**Note**: PWHT of austenitic stainless steel may sensitize material (carbide precipitation); use 304L/316L (low carbon) to avoid.

### 4.5 Special Considerations
- **Thermal Cycling**: Repair must withstand 10,000+ thermal cycles (-253°C to +20°C)
- **Vacuum Integrity**: All welds must be leak-tight (<10⁻⁹ mbar·L/s)
- **Material Properties**: Verify filler metal has adequate cryogenic toughness (Charpy >27 J @ -196°C)
- **Hydrogen Embrittlement**: Use low-hydrogen processes, avoid high-strength materials

## 5. Structural Requirements

### 5.1 Inspection Requirements
| Inspection Type | Timing | Method | Acceptance |
|-----------------|--------|--------|------------|
| Visual | During welding | VT per AWS D1.6 | Smooth, uniform, no undercut |
| Liquid Penetrant | Between weld passes + final | PT per ASTM E1417 | No linear indications |
| Radiographic | Final (critical welds) | RT per ASME Section V | ASME VIII acceptance |
| Ultrasonic | Final (alternative to RT) | UT per ASME Section V | ASME VIII Appendix 12 |
| Leak Test | After hydrostatic test | Helium leak detector | <10⁻⁹ mbar·L/s |

### 5.2 Hydrostatic Test
- **Test Pressure**: 1.5× MAWP (Maximum Allowable Working Pressure)
- **Hold Time**: 30 minutes minimum (or per original design)
- **Temperature**: Ambient (not cryogenic during hydrostatic test)
- **Acceptance**: No visible leakage, no permanent deformation
- **Documentation**: Test pressure, duration, results, inspector sign-off

### 5.3 Leak Test (Vacuum Integrity)
- **Method**: Helium mass spectrometer leak detector
- **Test Procedure**: Evacuate vacuum space, spray helium on suspect areas
- **Acceptance**: Leak rate < 10⁻⁹ mbar·L/s (static vacuum vessels per ISO 21009)
- **Alternative**: Pressure decay test if helium detector unavailable

### 5.4 Cryogenic Performance Test
- **Cool-Down Test**: Fill with LN2 (liquid nitrogen, -196°C) as surrogate for LH2
- **Boil-Off Measurement**: Measure heat leak (compare to original specification)
- **Thermal Cycling**: 3 cycles minimum to -196°C (verify no cracks, leaks)
- **Acceptance**: Boil-off within 110% of original design value
- **Safety**: Purge all H2, inert vessel before LN2 introduction

### 5.5 Return-to-Service Requirements
- All inspection and test requirements satisfied
- Repair documentation complete (WPS, PQR, welder ID, inspection reports)
- Engineering approval of repair (if major repair)
- Hydrostatic test certificate
- Leak test certificate
- Updated vessel data plate (if required by code)
- Operator training on any modifications

## 6. Cross-References
- Parent Document: 03-50_Structures
- Related: 03-50-02-01A (LH2 Tank Structures), 03-50-02-02A (Cryogenic Vessel Design), 03-50-08-01A (Structural Repair Manual), 03-50-08-02A (Welding Procedures)

## 7. Revision History
| Rev | Date | Author | Description |
|-----|------|--------|-------------|
| A | 2025-12-08 | AMPEL360 Documentation Team | Initial release |

---

## Document Control

- **Document ID:** 03-50-08-04A
- **Version:** A
- **Status:** Active
- **Last Updated:** 2025-12-08
- **Repository:** AMPEL360-BWB-H2-Hy-E
- **Owner:** AMPEL360 GSE Structures Team

---

*Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.*
