# 03-60-03-01A - Cryogenic Tank Systems

## 1. Purpose
This document defines the requirements for cryogenic tank systems used in GSE operations, covering design, construction, and operational specifications for storage of cryogenic liquids at extremely low temperatures (-150°C to -270°C).

## 2. Scope
This document covers:
- Cryogenic tank design principles and construction
- Insulation systems and thermal performance
- Materials selection for cryogenic service
- Tank testing and qualification
- Operational considerations and maintenance

## 3. Applicable Documents
- ISO 21009 Series (Cryogenic Vessels - Static Vacuum Insulated Vessels)
- EN 13458 Series (Cryogenic Vessels - Operational Requirements)
- ASME BPVC Section VIII (Pressure Vessel Code)
- CGA P-12 (Safe Handling of Cryogenic Liquids)
- NFPA 55 (Compressed Gases and Cryogenic Fluids Code)
- API 620 (Design and Construction of Large, Welded, Low-Pressure Storage Tanks)
- BS 5500 (Specification for Unfired Fusion Welded Pressure Vessels)

## 4. Storage Description

### 4.1 Overview
Cryogenic tank systems provide storage for liquefied gases at temperatures below -150°C, including liquid hydrogen (-253°C), liquid nitrogen (-196°C), liquid oxygen (-183°C), and liquid helium (-269°C). These tanks employ advanced insulation technologies to minimize heat ingress and maintain cryogenic temperatures with acceptable boil-off rates.

Key design features:
- Double-wall construction with vacuum insulation
- Multi-layer insulation (MLI) or powder/perlite insulation
- Low-emissivity surfaces to reduce radiative heat transfer
- Pressure control and boil-off management systems
- Specialized materials compatible with cryogenic temperatures

### 4.2 Specifications

#### Tank Construction Types
| Type | Description | Typical Capacity | Insulation Method | Application |
|------|-------------|------------------|-------------------|-------------|
| Vertical Cylindrical | Flat or domed ends, above-ground | 10,000-200,000 L | Vacuum + MLI | Bulk LH2, LN2 |
| Horizontal Cylindrical | Saddle-mounted, above-ground | 5,000-100,000 L | Vacuum + MLI | Mobile or space-constrained |
| Spherical | Self-supporting sphere | 50,000-500,000 L | Vacuum or perlite | Large-scale storage |
| Flat-Bottom | API 620 design, above or in-ground | 100,000-5,000,000 L | Perlite or expanded foam | Very large bulk storage |

#### Material Specifications
| Component | Material Options | Service Temperature | Notes |
|-----------|------------------|---------------------|-------|
| Inner Vessel | 304L, 316L, 321 SS; 5083, 9% Ni Steel | -270°C to -150°C | Austenitic materials maintain ductility |
| Outer Vessel | Carbon steel, 304 SS | Ambient | Structural and vacuum containment |
| Piping (Process) | 304L, 316L SS | -270°C to -150°C | Vacuum-jacketed preferred |
| Supports | 304 SS or low-thermal-conductivity materials | Cryogenic to ambient | Minimize heat ingress |
| Insulation | MLI (aluminum-mylar), perlite, polyurethane foam | N/A | Vacuum required for MLI |

#### Thermal Performance
| Parameter | Specification | Notes |
|-----------|---------------|-------|
| Vacuum Level | < 10⁻³ mbar (MLI), < 50 mbar (perlite) | Operating condition |
| Heat Ingress Rate | 0.5-2.0 W/m² (MLI), 2-5 W/m² (perlite) | Depends on insulation quality |
| Boil-off Rate | 0.1-0.5% per day | For well-maintained systems |
| Hold Time (Static) | 30-60 days (LH2), 90+ days (LN2) | No withdrawal |
| Thermal Cycling Capability | Minimum 100 cycles | Room temp to operating temp |

### 4.3 Capacity and Requirements

#### Design Pressure and Safety
- **Normal Operating Pressure**: 1-10 bar absolute
- **Maximum Allowable Working Pressure (MAWP)**: 150% of operating pressure
- **Design Pressure**: 1.1 × MAWP (ASME requirement)
- **Test Pressure**: 1.3 × MAWP for pneumatic, 1.5 × MAWP for hydrostatic
- **Pressure Relief**: Multiple PRVs sized per CGA S-1.3 and ASME Section VIII

#### Structural Design Loads
- **Internal Pressure**: Per ASME Section VIII calculations
- **External Pressure (Outer Vessel)**: Vacuum + atmospheric pressure
- **Dead Load**: Empty weight + insulation + accessories
- **Live Load**: Liquid product weight, snow (if applicable)
- **Seismic Load**: Per IBC and site seismic design category
- **Wind Load**: Per ASCE 7 and local requirements
- **Thermal Stress**: Differential expansion between inner and outer vessels

#### Insulation System Design
**Multi-Layer Insulation (MLI)**:
- Layers: 30-100 layers of aluminum-coated mylar with spacer material
- Layer density: Optimized for minimum heat transfer (typically 10-30 layers/cm)
- Vacuum requirement: < 10⁻³ mbar for effective performance
- Radiation shields: Low-emissivity coatings (ε < 0.05)
- Advantages: Lowest thermal conductivity, compact
- Disadvantages: Requires high vacuum, expensive

**Powder/Perlite Insulation**:
- Material: Expanded perlite or microspherical powder
- Vacuum requirement: < 50 mbar (soft vacuum)
- Thickness: 300-600 mm typical
- Advantages: Tolerant of vacuum loss, lower cost
- Disadvantages: Larger volume, settling over time

## 5. Safety Requirements
| Requirement | Standard | Implementation |
|-------------|----------|----------------|
| Pressure Vessel Certification | ASME Section VIII, local jurisdiction | U-stamp, CRN, or equivalent |
| Pressure Relief Sizing | ASME Section VIII, CGA S-1.3 | Multiple devices, redundant capacity |
| Overfill Prevention | Automated level control | High-level alarm and shutoff |
| Vacuum Monitoring | Continuous vacuum gauge | Alarm on vacuum degradation |
| Oxygen Monitoring (LH2 service) | NFPA 2, Section 7.8 | Continuous monitoring in enclosed areas |
| Emergency Isolation | Automatic on leak detection | Fail-safe valve design |
| Inspection and Testing | Per jurisdiction and insurance | Initial, periodic (3-10 years depending on service) |
| Lightning Protection | NFPA 780 | Bonding, grounding, air terminals |

## 6. Cross-References
- Related ATA Chapters:
  - ATA 03-60-02 (H2/LH2 Storage Systems) - LH2-specific applications
  - ATA 03-60-03-02A (Vacuum Insulated Storage) - Insulation details
  - ATA 03-60-03-03A (Boil-Off Management) - Boil-off control strategies
  - ATA 03-60-08 (Storage Safety Compliance) - Safety and compliance
- Parent Document: 03-60_Storages
- Standards:
  - ISO 21009 (Cryogenic Vessels)
  - ASME BPVC Section VIII (Pressure Vessels)
  - NFPA 55 (Cryogenic Fluids Code)

## 7. Revision History
| Rev | Date | Author | Description |
|-----|------|--------|-------------|
| A | 2025-12-08 | AMPEL360 Documentation Team | Initial release |

---

## Document Control

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT** – Subject to human review and approval.
- Human approver: _[to be completed]_.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: _2025-12-08_.
