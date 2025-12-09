# 03-50-07-02A - NDT Methods

## 1. Purpose
Specification for Non-Destructive Testing (NDT) methods for Ground Support Equipment (GSE) structures to detect internal and surface defects without damaging the component.

## 2. Scope
- NDT method selection and application
- Ultrasonic Testing (UT)
- Magnetic Particle Testing (MT)
- Liquid Penetrant Testing (PT)
- Radiographic Testing (RT)
- Eddy Current Testing (ET)
- Personnel qualification

## 3. Applicable Documents
- ASME BPVC Section V (Nondestructive Examination)
- ASTM E1417 (Liquid Penetrant Testing)
- ASTM E709 (Magnetic Particle Testing)
- ASTM E165 (Liquid Penetrant Examination)
- ISO 17638 (Ultrasonic Testing of Welds)
- ASNT SNT-TC-1A (Personnel Qualification)

## 4. Structural Description

### 4.1 NDT Method Selection
| Method | Detects | Material | Advantages | Limitations |
|--------|---------|----------|------------|-------------|
| Ultrasonic (UT) | Internal defects, thickness | All | Volumetric, portable | Requires coupling, trained operator |
| Magnetic Particle (MT) | Surface/near-surface cracks | Ferromagnetic | Sensitive, economical | Ferromagnetic only, cleanup required |
| Liquid Penetrant (PT) | Surface-breaking defects | All | Simple, low-cost | Surface defects only, surface prep critical |
| Radiographic (RT) | Internal defects, porosity | All | Permanent record | Radiation hazard, expensive, slow |
| Eddy Current (ET) | Surface/near-surface defects | Conductive | Fast, no coupling | Shallow depth, calibration required |
| Visual (VT) | Surface defects | All | Simple, economical | Surface only, subjective |

### 4.2 Ultrasonic Testing (UT)
- **Applications**: Weld inspection, thickness measurement, lamination detection
- **Equipment**: UT flaw detector, transducer (0.5-10 MHz), couplant
- **Techniques**: Straight beam (thickness), angle beam (welds), phased array
- **Acceptance**: ASME VIII Appendix 12 or AWS D1.1
- **Personnel**: ASNT Level II minimum

### 4.3 Magnetic Particle Testing (MT)
- **Applications**: Welds, high-stress areas (ferromagnetic materials only)
- **Equipment**: Yoke, prods, or coil for magnetization; iron particles (wet or dry)
- **Techniques**: Continuous or residual, AC or DC magnetization
- **Acceptance**: No linear indications >5 mm, no rounded indications >10 mm
- **Personnel**: ASNT Level II minimum

### 4.4 Liquid Penetrant Testing (PT)
- **Applications**: Welds, castings, non-ferromagnetic materials
- **Equipment**: Penetrant, developer, cleaner
- **Techniques**: Visible dye or fluorescent
- **Acceptance**: No linear indications >3 mm, no rounded indications >5 mm
- **Personnel**: ASNT Level I minimum (supervised)

### 4.5 Radiographic Testing (RT)
- **Applications**: Welds (full-penetration), castings
- **Equipment**: X-ray or gamma source, film or digital detector
- **Acceptance**: ASME VIII UW-51 or AWS D1.1
- **Personnel**: ASNT Level II minimum, radiation safety training

### 4.6 Eddy Current Testing (ET)
- **Applications**: Tube inspection, surface cracks, coating thickness
- **Equipment**: ET instrument, probe (pencil, encircling, array)
- **Acceptance**: Per calibration standard
- **Personnel**: ASNT Level II minimum

## 5. Structural Requirements

### 5.1 Inspection Frequency
| Component | NDT Method | Frequency |
|-----------|------------|-----------|
| Pressure Vessel Welds | UT or RT | Initial + every 10 years |
| Structural Welds (critical) | UT or MT | Initial + after repair |
| LH2 Tank Welds | UT + PT | Initial + every 5 years |
| Lifting Lugs | MT or PT | Annual |
| Chassis Welds | VT + MT (sample) | Every 5 years |

### 5.2 Acceptance Criteria (Welds per AWS D1.1)
- **Cracks**: Not permitted (any size)
- **Lack of Fusion**: Not permitted
- **Incomplete Penetration**: Not permitted (full-penetration welds)
- **Porosity**: <3% of weld area on radiograph
- **Undercut**: <1 mm depth

### 5.3 Personnel Qualification
| Level | Training | Experience | Certification |
|-------|----------|------------|---------------|
| Level I | 40 hours | 400 hours | Method-specific |
| Level II | 80 hours | 800 hours | Method-specific, interpretation |
| Level III | Extensive | 4000 hours | All methods, procedure writing |

## 6. Cross-References
- Parent Document: 03-50_Structures
- Related: 03-50-07-01A (Visual Inspection), 03-50-07-03A (Crack Detection)

## 7. Revision History
| Rev | Date | Author | Description |
|-----|------|--------|-------------|
| A | 2025-12-08 | AMPEL360 Documentation Team | Initial release |

---

## Document Control

- **Document ID:** 03-50-07-02A
- **Version:** A
- **Status:** Active
- **Last Updated:** 2025-12-08
- **Repository:** AMPEL360-BWB-H2-Hy-E
- **Owner:** AMPEL360 GSE Structures Team

---

*Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.*
