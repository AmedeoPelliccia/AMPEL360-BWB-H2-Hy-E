# 03-50-01-01A - GSE Structural Design

## 1. Purpose
This document establishes the structural design principles and requirements for Ground Support Equipment (GSE) used in support of the AMPEL360 BWB-H2-Hy-E aircraft operations. It defines the design philosophy, load cases, and structural integrity criteria for all GSE structural systems.

## 2. Scope
This specification covers structural design for:
- Mobile GSE equipment (tugs, loaders, service vehicles)
- Fixed GSE structures (platforms, stands, shelters)
- H2/LH2 GSE equipment (refueling systems, storage vessels)
- Aircraft servicing equipment (maintenance stands, jacks)

## 3. Applicable Documents
- ATA iSpec 2200 (Information Standards for Aviation Maintenance)
- ASME BPVC Section VIII (Pressure Vessels)
- EN 13445 (Unfired Pressure Vessels)
- EN 13458 (Cryogenic Vessels)
- AWS D1.1 (Structural Welding Code - Steel)
- ISO 21009 (Cryogenic Vessels - Static Vacuum Insulated Vessels)
- SAE AS6968 (Hydrogen Aircraft Refueling)
- Reference: 03-00-06_Engineering (GSE Engineering Overview)

## 4. Structural Description

### 4.1 Overview
GSE structural design encompasses the mechanical framework and load-bearing elements of ground support systems. The design must ensure safe operation under normal and emergency conditions, with special consideration for H2/LH2 handling requirements.

### 4.2 Design Philosophy
| Aspect | Approach | Rationale |
|--------|----------|-----------|
| Safety Factor | 2.0 minimum for static loads, 4.0 for dynamic/fatigue | Accounts for GSE operating environment uncertainty |
| Design Life | 20 years typical, 30 years for fixed installations | Economic lifecycle optimization |
| Maintainability | Modular design with accessible inspection points | Reduces downtime and maintenance cost |
| H2 Compatibility | Materials resistant to hydrogen embrittlement | Critical safety requirement |
| Environmental | Corrosion-resistant materials and coatings | Extended service life in outdoor conditions |

### 4.3 Load Categories
1. **Dead Loads**: Self-weight of GSE structure and fixed components
2. **Live Loads**: Service loads during normal operations
3. **Wind Loads**: As per local building codes for fixed installations
4. **Seismic Loads**: As required for geographic location
5. **Impact Loads**: Collision, docking, and accidental loading
6. **Thermal Loads**: Cryogenic contraction/expansion, solar heating
7. **Pressure Loads**: Internal pressure in vessels and piping

## 5. Structural Requirements

### 5.1 Design Criteria
| Requirement | Value | Standard |
|-------------|-------|----------|
| Minimum Yield Safety Factor | 2.0 | ASME BPVC |
| Ultimate Safety Factor | 3.0 | ASME BPVC |
| Fatigue Life (cycles) | 50,000 minimum | AWS D1.1 |
| Maximum Deflection | L/500 under service loads | Industry practice |
| Corrosion Allowance | 3 mm for carbon steel | ISO 12944 |

### 5.2 Material Selection Criteria
- **Structural Steel**: ASTM A36, A572 Grade 50 for general structures
- **Stainless Steel**: 304L, 316L for H2 service and cryogenic applications
- **Aluminum Alloys**: 6061-T6, 5083-H116 for weight-critical mobile GSE
- **Composite Materials**: CFRP for specialized applications (non-structural)

### 5.3 H2-Specific Requirements
- All materials in contact with hydrogen shall be tested for hydrogen embrittlement susceptibility
- Welding procedures for H2 service shall follow ASME B31.12
- Minimum operating temperature: -253°C for LH2 systems
- Pressure relief and venting systems required per NFPA 2

## 6. Cross-References
- Related ATA Chapters: 
  - ATA 03-00-06 (GSE Engineering)
  - ATA 03-30 (Anchors and Tie-downs)
  - ATA 03-40 (Software for GSE control systems)
- Parent Document: 03-50_Structures
- Related Standards:
  - 03-50-01-02A (GSE Structural Standards)
  - 03-50-01-03A (GSE Materials Selection)
  - 03-50-02 (H2 GSE Structures subsection)

## 7. Revision History
| Rev | Date | Author | Description |
|-----|------|--------|-------------|
| A | 2025-12-08 | AMPEL360 Documentation Team | Initial release |

---

## Document Control

- **Document ID:** 03-50-01-01A
- **Version:** A
- **Status:** Active
- **Last Updated:** 2025-12-08
- **Repository:** AMPEL360-BWB-H2-Hy-E
- **Owner:** AMPEL360 GSE Structures Team

---

*Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.*
