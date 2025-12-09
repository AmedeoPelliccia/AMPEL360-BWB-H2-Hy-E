# 03-50-01-03A - GSE Materials Selection

## 1. Purpose
This document defines the material selection criteria and specifications for Ground Support Equipment (GSE) structural components, with emphasis on H2/LH2 compatibility, cryogenic service, and long-term durability in operational environments.

## 2. Scope
This specification covers material selection for:
- Structural steel components
- Stainless steel for H2/LH2 service
- Aluminum alloys for lightweight structures
- Fasteners and joining materials
- Coatings and corrosion protection
- Gaskets, seals, and non-metallic components

## 3. Applicable Documents
- ASTM Material Specifications (as referenced in Section 4)
- ASME BPVC Section II (Materials)
- AWS A5 Series (Welding Consumables)
- ISO 15156 (Materials for H2 Service)
- NACE MR0175/ISO 15156 (Petroleum and Natural Gas Industries—Materials for Use in H2-Containing Environments)
- Reference: 03-50-01-01A (GSE Structural Design)

## 4. Structural Description

### 4.1 Overview
Material selection for GSE structures is driven by operational requirements, environmental conditions, and safety considerations. Special attention is required for hydrogen compatibility, cryogenic temperatures, and corrosion resistance.

### 4.2 Material Selection Criteria

#### 4.2.1 General Criteria
| Criterion | Requirement | Priority |
|-----------|-------------|----------|
| Strength | Adequate yield and ultimate strength | Critical |
| Ductility | Minimum 15% elongation | Critical |
| Fracture Toughness | Adequate for cryogenic service | Critical for LH2 |
| Weldability | Suitable for AWS procedures | High |
| Corrosion Resistance | 20-year service life minimum | High |
| Cost | Optimize lifecycle cost | Medium |
| Availability | Standard mill products preferred | Medium |

#### 4.2.2 H2 Compatibility Criteria
| Property | Requirement | Test Method |
|----------|-------------|-------------|
| Hydrogen Embrittlement Resistance | No crack growth at service pressure | ASTM G142 |
| Hydrogen Permeation | <1x10⁻⁸ mol/m²/s/Pa½ | ISO 17081 |
| Material Class | Class A or B per ISO 15156 | ISO 15156-2 |
| Minimum Toughness | 27J at -40°C (Charpy V-notch) | ASTM E23 |

### 4.3 Material Specifications

#### 4.3.1 Structural Steel (General GSE)
| Material | Specification | Typical Use | Notes |
|----------|---------------|-------------|-------|
| Carbon Steel | ASTM A36 | General structures, frames | Most economical |
| HSLA Steel | ASTM A572 Grade 50 | High-load applications | Higher strength-to-weight |
| Low-Temperature Steel | ASTM A333 Grade 6 | Cold climate operations | Impact-tested to -45°C |

#### 4.3.2 Stainless Steel (H2 and Cryogenic Service)
| Material | Specification | Typical Use | Notes |
|----------|---------------|-------------|-------|
| 304/304L | ASTM A240 Type 304L | General H2 piping, tanks | Good H2 resistance |
| 316/316L | ASTM A240 Type 316L | LH2 vessels, critical piping | Superior corrosion resistance |
| 321 | ASTM A240 Type 321 | Welded H2 service | Stabilized for welding |
| Duplex 2205 | ASTM A240 S31803 | High-strength H2 applications | Excellent stress corrosion resistance |

#### 4.3.3 Aluminum Alloys (Lightweight Structures)
| Material | Specification | Typical Use | Notes |
|----------|---------------|-------------|-------|
| 6061-T6 | ASTM B209 | Mobile GSE frames | Good weldability |
| 5083-H116 | ASTM B209 | Marine/corrosive environments | Excellent corrosion resistance |
| 7075-T6 | ASTM B209 | High-strength components | Limited weldability |

#### 4.3.4 Fasteners and Hardware
| Component | Material | Specification | Application |
|-----------|----------|---------------|-------------|
| Structural Bolts | ASTM A325, A490 | ASTM F3125 | High-strength connections |
| Stainless Bolts | 316 SS | ASTM F593 | H2 service, corrosive environments |
| Nuts | Grade 8, 316 SS | ASTM A563, F594 | Match bolt grade |
| Washers | Hardened steel, SS | ASTM F436, F844 | Structural connections |

### 4.4 Hydrogen Embrittlement Considerations

#### 4.4.1 Susceptible Materials (Avoid in H2 Service)
- High-strength steels (>1000 MPa yield)
- Precipitation-hardened stainless steels (17-4PH, 15-5PH)
- Martensitic stainless steels
- Titanium alloys (in gaseous H2)

#### 4.4.2 Recommended Materials for H2 Service
- Austenitic stainless steels (300 series)
- Aluminum alloys (all common grades)
- Copper and copper alloys
- Nickel-based alloys (Inconel, Monel)

### 4.5 Cryogenic Materials (LH2 Service at -253°C)

| Material | Suitability | Maximum Strength Retention | Notes |
|----------|-------------|---------------------------|-------|
| 304L/316L SS | Excellent | 100%+ (strengthens) | Preferred for LH2 |
| 5083 Aluminum | Excellent | 100%+ | Good ductility at cryogenic |
| 6061-T6 Aluminum | Good | ~95% | Suitable for most applications |
| 9% Ni Steel | Excellent | 100%+ | For large cryogenic tanks |
| Carbon Steel | Poor | Brittle fracture risk | Not suitable below -45°C |

## 5. Structural Requirements

### 5.1 Material Qualification Requirements
| Requirement | Specification | Frequency |
|-------------|---------------|-----------|
| Material Test Reports (MTR) | Per ASTM spec | Every heat/lot |
| Charpy Impact Testing | ASTM E23 | Per specification requirement |
| Tensile Testing | ASTM E8 | Per MTR requirements |
| Chemical Analysis | Certified mill test | Every heat |
| H2 Compatibility Testing | ASTM G142 | For new H2 applications |

### 5.2 Corrosion Protection Requirements
| Environment | Protection Method | Standard |
|-------------|------------------|----------|
| Outdoor (atmospheric) | Hot-dip galvanizing or coating system | ASTM A123, ISO 12944 |
| Marine/coastal | Stainless steel or enhanced coating | ISO 12944-C5 |
| H2 Service | Stainless steel (no coating on wetted surfaces) | ASME B31.12 |
| Buried/underground | Cathodic protection + coating | NACE SP0169 |

### 5.3 Weld Filler Material Requirements
| Base Material | Filler Material | Specification | Notes |
|---------------|-----------------|---------------|-------|
| A36, A572 | E7018, E70XX | AWS A5.1, A5.5 | Low-hydrogen electrodes |
| 304/304L | ER308L | AWS A5.9 | SMAW, GMAW, GTAW |
| 316/316L | ER316L | AWS A5.9 | Cryogenic and H2 service |
| 6061 Aluminum | ER4043, ER5356 | AWS A5.10 | Match base metal composition |

## 6. Cross-References
- Related ATA Chapters:
  - ATA 03-00-06 (GSE Engineering)
- Parent Document: 03-50_Structures
- Related Documents:
  - 03-50-01-01A (GSE Structural Design)
  - 03-50-01-02A (GSE Structural Standards)
  - 03-50-02 (H2 GSE Structures)
  - 03-50-08 (GSE Structural Repair - welding procedures)

## 7. Revision History
| Rev | Date | Author | Description |
|-----|------|--------|-------------|
| A | 2025-12-08 | AMPEL360 Documentation Team | Initial release |

---

## Document Control

- **Document ID:** 03-50-01-03A
- **Version:** A
- **Status:** Active
- **Last Updated:** 2025-12-08
- **Repository:** AMPEL360-BWB-H2-Hy-E
- **Owner:** AMPEL360 GSE Structures Team

---

*Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.*
