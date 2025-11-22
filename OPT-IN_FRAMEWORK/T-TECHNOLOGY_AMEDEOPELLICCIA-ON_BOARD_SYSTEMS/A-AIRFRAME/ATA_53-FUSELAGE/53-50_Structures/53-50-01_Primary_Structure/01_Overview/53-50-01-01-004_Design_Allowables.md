# 53-50-01-01-004 Design Allowables

## Document Information

- **Document ID**: 53-50-01-01-004
- **Title**: Design Allowables
- **Version**: 1.0
- **Date**: 2025-11-22
- **Status**: Draft
- **Category**: Structural Design Data
- **ATA Chapter**: 53-50 - Fuselage Structures

## Purpose

This document defines the material design allowable values used for structural analysis and sizing of AMPEL360 BWB primary structure. Allowables account for material variability, environmental effects, and safety factors required by certification authorities.

## Scope

Design allowables defined for:
- CFRP composite laminates
- Aluminum alloys
- Titanium alloys
- Steel alloys
- Environmental knockdown factors
- Statistical basis and confidence levels

## Regulatory Basis

Allowables developed per:
- [CS-25.613](https://www.easa.europa.eu/en/document-library/certification-specifications/cs-25-amendment-27) - Material Strength Properties and Design Values
- [CS-25.603](https://www.easa.europa.eu/en/document-library/certification-specifications/cs-25-amendment-27) - Materials
- [CMH-17](https://www.cmh17.org/) - Composite Materials Handbook (composite allowables)
- [MMPDS](https://www.mmpds.org/) - Metallic Materials Properties Development and Standardization

## Allowable Development Process

### Statistical Basis

Per [CS-25.613](https://www.easa.europa.eu/en/document-library/certification-specifications/cs-25-amendment-27), design allowables determined using statistical methods:

**A-Basis Allowables**:
- 99% probability with 95% confidence
- Used for single-load-path, critical structure
- Lower 1st percentile value

**B-Basis Allowables**:
- 90% probability with 95% confidence
- Used for multi-load-path structure (fail-safe design)
- Lower 10th percentile value

**Typical (Mean) Values**:
- 50% probability
- Used for preliminary design only, not for certification

### Environmental Conditioning

**Room Temperature Ambient (RTA)**:
- 21°C (70°F), dry conditions
- Baseline condition for material testing

**Cold Temperature Dry (CTD)**:
- -55°C (-67°F), dry
- Minimum operating temperature

**Elevated Temperature Wet (ETW)**:
- Maximum operating temperature, moisture-saturated
- CFRP: 82°C (180°F) wet (85% RH conditioning until saturation)
- Aluminum: 120°C (250°F) (moisture not applicable)

**Design Allowables = RTA Allowables × Environmental Knockdown Factors**

## CFRP Composite Allowables

### Laminate Configurations

**Quasi-Isotropic Layup [45/0/-45/90]s**:
- Balanced properties in all directions
- Used for general skins and panels
- Good damage tolerance

**0° Dominated Layup [0/±45/90] with 60-70% 0°**:
- High axial stiffness and strength
- Used for stringers and longerons
- Optimal for uniaxial tension/compression

**±45° Dominated Layup [±45/0/90] with 60% ±45°**:
- High shear stiffness and strength
- Used for webs and shear panels

### Typical CFRP Allowables (IM7/8552, Quasi-Isotropic)

**Tension (0° direction)**:
- **A-Basis, RTA**: 750 MPa
- **B-Basis, RTA**: 820 MPa
- **A-Basis, ETW**: 675 MPa (10% knockdown)

**Compression (0° direction)**:
- **A-Basis, RTA**: 620 MPa
- **B-Basis, RTA**: 680 MPa
- **A-Basis, ETW**: 496 MPa (20% knockdown, moisture effect)

**In-Plane Shear**:
- **A-Basis, RTA**: 110 MPa
- **B-Basis, RTA**: 125 MPa
- **A-Basis, ETW**: 99 MPa (10% knockdown)

**Modulus (0° direction)**:
- **E₁ (RTA)**: 160 GPa
- **E₁ (ETW)**: 156 GPa (minimal change)

**Interlaminar Shear Strength (ILSS)**:
- **A-Basis, RTA**: 85 MPa
- **A-Basis, ETW**: 60 MPa (30% knockdown, critical for delamination)

**Open Hole Compression (OHC)**:
- **A-Basis, RTA**: 310 MPa (50% knockdown due to damage)
- Used for sizing around fastener holes and cutouts

### Environmental Knockdown Factors (CFRP)

| Property | CTD | RTA | ETW |
|----------|-----|-----|-----|
| Tension (0°) | 1.0 | 1.0 | 0.90 |
| Compression (0°) | 1.0 | 1.0 | 0.80 |
| Shear | 1.0 | 1.0 | 0.90 |
| ILSS | 1.0 | 1.0 | 0.70 |

**Note**: ETW typically critical for compression and interlaminar properties.

## Aluminum Alloy Allowables

### 2024-T3 Aluminum (Moderate Strength, Good Fatigue)

**Tensile Properties** (Room Temperature):
- **Ftu (Ultimate Tensile Strength)**: 
  - S-Basis: 470 MPa (68 ksi)
  - A-Basis: 450 MPa (65 ksi)
- **Fty (Tensile Yield Strength)**:
  - S-Basis: 345 MPa (50 ksi)
  - A-Basis: 325 MPa (47 ksi)
- **E (Modulus)**: 73.1 GPa (10.6 Msi)

**Compressive Properties**:
- **Fcy (Compressive Yield Strength)**: 345 MPa (same as tensile yield)
- **Fsu (Ultimate Shear Strength)**: 285 MPa (41 ksi)

**Elevated Temperature (120°C)**:
- **Ftu**: 400 MPa (15% reduction)
- **Fty**: 290 MPa (16% reduction)

### 7075-T6 Aluminum (High Strength)

**Tensile Properties** (Room Temperature):
- **Ftu**: 
  - S-Basis: 570 MPa (83 ksi)
  - A-Basis: 540 MPa (78 ksi)
- **Fty**:
  - S-Basis: 505 MPa (73 ksi)
  - A-Basis: 460 MPa (67 ksi)
- **E (Modulus)**: 71.7 GPa (10.4 Msi)

**Compressive Properties**:
- **Fcy**: 505 MPa
- **Fsu**: 330 MPa (48 ksi)

**Elevated Temperature (120°C)**:
- **Ftu**: 470 MPa (18% reduction)
- **Fty**: 415 MPa (18% reduction)

### 7050-T7451 Aluminum (Thick Sections, Damage Tolerance)

**Tensile Properties** (Room Temperature, Plate 25-50mm thick):
- **Ftu**: 
  - S-Basis: 525 MPa (76 ksi)
  - A-Basis: 510 MPa (74 ksi)
- **Fty**:
  - S-Basis: 455 MPa (66 ksi)
  - A-Basis: 435 MPa (63 ksi)
- **E (Modulus)**: 71.7 GPa

**Fracture Toughness** (KIC):
- 35 MPa√m (critical for damage tolerance analysis)

## Titanium Alloy Allowables

### Ti-6Al-4V (Grade 5, Annealed)

**Tensile Properties** (Room Temperature):
- **Ftu**:
  - S-Basis: 930 MPa (135 ksi)
  - A-Basis: 895 MPa (130 ksi)
- **Fty**:
  - S-Basis: 860 MPa (125 ksi)
  - A-Basis: 825 MPa (120 ksi)
- **E (Modulus)**: 114 GPa (16.5 Msi)
- **Elongation**: 10-15%

**Compressive Properties**:
- **Fcy**: 860 MPa (same as tensile yield)
- **Fsu**: 550 MPa (80 ksi)

**Elevated Temperature (300°C)**:
- **Ftu**: 620 MPa (33% reduction)
- **Fty**: 520 MPa (40% reduction)

**Cold Temperature (-55°C)**:
- **Ftu**: 1,035 MPa (11% increase)
- **Fty**: 965 MPa (12% increase)

## Steel Alloy Allowables

### 4340 Steel (Heat-Treated, High Strength)

**Tensile Properties** (Room Temperature):
- **Ftu**: 1,790 MPa (260 ksi) (typical heat treatment)
- **Fty**: 1,655 MPa (240 ksi)
- **E (Modulus)**: 205 GPa (29.7 Msi)

**Bearing Strength**:
- **Fbru**: 2,860 MPa (415 ksi) (ultimate bearing)
- **Fbry**: 2,070 MPa (300 ksi) (yield bearing)

### 300M Steel (Ultra-High Strength)

**Tensile Properties**:
- **Ftu**: 1,930 MPa (280 ksi)
- **Fty**: 1,725 MPa (250 ksi)
- **E (Modulus)**: 205 GPa

## Fastener Allowables

### Titanium Fasteners (Ti-6Al-4V)

**Bolts (Hi-Lok, Hi-Lite)**:
- **Shear Strength**: 690 MPa (100 ksi)
- **Tensile Strength**: 1,240 MPa (180 ksi)
- **Typical Diameters**: 4.8mm (3/16"), 6.35mm (1/4"), 7.94mm (5/16")

### Steel Fasteners (CRES A286)

**Bolts**:
- **Shear Strength**: 760 MPa (110 ksi)
- **Tensile Strength**: 1,380 MPa (200 ksi)

### Aluminum Rivets (2117-T4)

**Rivets**:
- **Shear Strength**: 195 MPa (28 ksi)
- **Used**: Non-critical secondary structure

## Bearing Allowables

### Composite Laminates (Bolt Bearing)

**Bearing Strength** (depends on e/D, edge distance to diameter ratio):
- **e/D ≥ 3**: 620 MPa (A-Basis, RTA)
- **e/D = 2**: 520 MPa (reduced due to edge proximity)
- **e/D < 2**: Not recommended (high stress concentration)

**Pin Bearing**:
- 10% lower than bolt bearing (due to rotation and wear)

### Aluminum (Bolt Bearing)

**7075-T6**:
- **Fbru**: 1,150 MPa (167 ksi) (e/D ≥ 2)
- **Fbry**: 760 MPa (110 ksi) (e/D ≥ 2)

**2024-T3**:
- **Fbru**: 930 MPa (135 ksi)
- **Fbry**: 620 MPa (90 ksi)

## Joint Allowables

### Bonded Joints (Adhesive)

**Film Adhesive** (e.g., FM300 or equivalent):
- **Lap Shear Strength**: 40 MPa (RTA, dry)
- **Lap Shear Strength**: 25 MPa (ETW, wet) - 38% knockdown
- **Peel Strength**: 7 N/mm (RTA), 4 N/mm (ETW)

**Design Approach**:
- Avoid reliance on adhesive alone for primary load path
- Use bonded-bolted hybrid joints for critical applications
- Adhesive augments mechanical fasteners

## Safety Factors and Margins

### Factor of Safety

Per [CS-25.303](https://www.easa.europa.eu/en/document-library/certification-specifications/cs-25-amendment-27):
- **Ultimate Load** = 1.5 × Limit Load
- Structure must withstand ultimate load for 3 seconds without failure

### Margin of Safety Calculation

**MS = (Allowable / Applied) × (1 / SF) - 1**

Where:
- **Allowable**: Material allowable stress or strength
- **Applied**: Actual stress or load on component
- **SF**: Safety Factor (typically 1.0 for ultimate loads, as 1.5 factor already in load)

**Acceptance**:
- **MS ≥ 0**: Pass (positive margin)
- **MS < 0**: Fail (negative margin, redesign required)

**Typical Margins**:
- 0.0 to 0.05: Tight design, acceptable but monitored
- 0.05 to 0.15: Good design, adequate for uncertainties
- > 0.3: Conservative, potential for optimization

## Design Data Traceability

All allowables traceable to:
- **Test Reports**: Original material qualification test data
- **Handbooks**: CMH-17 (composites), MMPDS (metals)
- **Supplier Data**: Material data sheets from qualified suppliers
- **In-House Testing**: Company-specific test programs for unique layups or conditions

## Temperature Effects Summary

| Material | -55°C | 21°C (RTA) | 82°C | 120°C | 300°C |
|----------|-------|------------|------|-------|-------|
| CFRP (tension) | 1.0 | 1.0 | 0.95 | - | - |
| CFRP (compression) | 1.0 | 1.0 | 0.85 | - | - |
| Al 7075-T6 (Ftu) | 1.03 | 1.0 | 0.93 | 0.82 | - |
| Ti-6Al-4V (Ftu) | 1.11 | 1.0 | 0.95 | 0.90 | 0.67 |
| Steel 4340 (Ftu) | 1.05 | 1.0 | 0.98 | 0.95 | 0.85 |

## References

### Standards and Handbooks
- [CMH-17](https://www.cmh17.org/) - Composite Materials Handbook
- [MMPDS](https://www.mmpds.org/) - Metallic Materials Properties Development and Standardization
- ASTM D5687 - Standard Guide for Preparation of Flat Composite Panels with Processing Guidelines for Specimen Preparation

### Regulatory Documents
- [CS-25.613](https://www.easa.europa.eu/en/document-library/certification-specifications/cs-25-amendment-27) - Material Strength Properties and Design Values
- [CS-25.603](https://www.easa.europa.eu/en/document-library/certification-specifications/cs-25-amendment-27) - Materials

### Internal References
- [53-50-01-01-003 Material Selection Summary](53-50-01-01-003_Material_Selection_Summary.md)
- [53-50-01-05-001 Stress Margin Summary](../05_Margins_and_Summaries/53-50-01-05-001_Stress_Margin_Summary.md)

---

## Document Control

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT** – Subject to human review and approval.
- Human approver: _[to be completed]_.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: 2025-11-22

---
