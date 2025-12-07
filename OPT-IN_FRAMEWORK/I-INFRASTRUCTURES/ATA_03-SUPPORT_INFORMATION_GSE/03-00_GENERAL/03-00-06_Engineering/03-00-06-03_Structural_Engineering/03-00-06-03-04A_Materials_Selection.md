# 03-00-06-03-04A - Materials Selection

## 1. Purpose
Establish criteria and processes for selecting materials for the AMPEL360 BWB-H2-Hy-E aircraft structure, ensuring optimal performance, weight efficiency, manufacturability, and compliance with safety and environmental requirements, including hydrogen compatibility.

## 2. Scope
This document covers:
- Material selection criteria and trade studies
- Metallic materials for primary and secondary structure
- Composite materials and advanced materials
- Hydrogen compatibility requirements
- Material specifications and qualification
- Supply chain and material sourcing
- Sustainability and lifecycle considerations

## 3. Applicable Documents
- [EASA CS-25.603](https://www.easa.europa.eu/en/document-library/certification-specifications/cs-25-large-aeroplanes) - Materials
- [EASA CS-25.605](https://www.easa.europa.eu/en/document-library/certification-specifications/cs-25-large-aeroplanes) - Fabrication Methods
- [MMPDS](https://www.mmpds.org/) - Metallic Materials Properties Development and Standardization (formerly MIL-HDBK-5)
- [CMH-17](https://www.cmh17.org/) - Composite Materials Handbook
- [ASTM Standards](https://www.astm.org/) - Material Testing Standards

## 4. Description

### 4.1 Overview
Material selection for the BWB-H2-Hy-E aircraft balances multiple competing requirements: structural efficiency, weight reduction, manufacturability, cost, and special requirements for hydrogen compatibility. The innovative blended-wing-body configuration enables extensive use of advanced composites, while hydrogen systems require materials resistant to embrittlement and suitable for cryogenic service.

### 4.2 Requirements
**Material Selection Criteria:**
1. **Structural Performance**
   - Strength-to-weight ratio
   - Stiffness-to-weight ratio
   - Fatigue resistance
   - Damage tolerance and fracture toughness
   - Environmental durability

2. **Manufacturing Considerations**
   - Formability and joinability
   - Process compatibility (molding, machining, welding)
   - Tooling requirements
   - Quality control and inspectability

3. **Operational Requirements**
   - Service temperature range (-55°C to +85°C typical, -253°C for H2 systems)
   - Corrosion resistance
   - Flammability and smoke toxicity (CS-25.853)
   - Lightning strike protection (CS-25.581)

4. **Hydrogen Compatibility (Critical for H2 Systems)**
   - Resistance to hydrogen embrittlement
   - Low-temperature (cryogenic) toughness
   - Thermal expansion compatibility
   - Compatibility with liquid hydrogen (LH2)

5. **Sustainability**
   - Recyclability and end-of-life considerations
   - Embodied energy and carbon footprint
   - Availability of sustainable alternatives

**Material Categories:**

**A. Primary Structure (High Strength, High Utilization)**
- **Aluminum alloys:** 2024-T3, 7075-T6, 7050-T7451
- **Advanced composites:** CFRP (carbon fiber reinforced polymer) with epoxy or toughened resin
- **Titanium alloys:** Ti-6Al-4V for high-temperature or critical joints

**B. Secondary Structure (Moderate Loads)**
- **Aluminum alloys:** 2024-T3, 6061-T6
- **GFRP (glass fiber reinforced polymer)**
- **Sandwich structures:** composite facesheets with honeycomb core

**C. Hydrogen System Materials**
- **Cryogenic tanks:** 
  - Metallic: Aluminum 2219, Inconel 718, stainless steel 316L
  - Composite: Type III (metal liner + CFRP overwrap) or Type IV (polymer liner + CFRP)
- **Piping and fittings:** Stainless steel 316L, Inconel, PTFE seals
- **Insulation:** Vacuum insulation, aerogel, MLI (multi-layer insulation)

### 4.3 Methodology
**Material Selection Process:**

1. **Define Requirements**
   - Load spectra and stress levels
   - Environmental conditions
   - Special requirements (H2 compatibility, cryogenic, etc.)
   - Cost and schedule constraints

2. **Conduct Trade Studies**
   - Compare candidate materials
   - Weight vs. cost analysis
   - Manufacturing complexity assessment
   - Risk evaluation

3. **Select Materials**
   - Choose optimal material for each application
   - Document rationale in material selection report
   - Identify qualification needs

4. **Specify Materials**
   - Develop material specifications referencing MMPDS, CMH-17, or AMS
   - Define acceptance criteria
   - Establish material control procedures

5. **Qualify Materials**
   - Conduct material testing if non-standard
   - Generate design allowables
   - Obtain regulatory acceptance

**Hydrogen Compatibility Assessment:**
- Review literature on hydrogen embrittlement susceptibility
- Conduct hydrogen charging and mechanical testing if necessary
- Verify fracture toughness at cryogenic temperatures
- Establish material handling and welding procedures to prevent hydrogen ingress

## 5. Deliverables
| Deliverable | Format | Responsible | Due |
|-------------|--------|-------------|-----|
| Material Selection Plan | Markdown/PDF | Materials Engineer | Project start |
| Material Trade Study Reports | Markdown/PDF | Materials Engineer | Conceptual design |
| Material Specifications | PDF/AMS | Materials Engineer | PDR |
| Material Qualification Reports | PDF | Test Engineer | CDR |
| Approved Materials List (AML) | CSV/Excel | Materials Engineer | CDR |
| H2 Compatibility Assessment | PDF/Markdown | Materials Engineer | PDR |

## 6. Verification & Validation
**Acceptance Criteria:**
- All materials meet structural performance requirements
- Material specifications complete and approved
- Hydrogen-compatible materials qualified for cryogenic service
- Manufacturing processes validated for selected materials
- Material traceability system established
- Regulatory approval obtained for all materials

**Test Methods:**
- Tensile, compression, shear testing per ASTM standards
- Fatigue testing (S-N curves)
- Fracture toughness testing (K_Ic, J_Ic)
- Environmental testing (corrosion, humidity, temperature)
- Cryogenic testing for H2 system materials
- Hydrogen embrittlement testing (slow strain rate, fracture mechanics)

## 7. Cross-References
- Related ATA Chapters:
  - [ATA 28](https://en.wikipedia.org/wiki/ATA_100) - Fuel System (H2 system materials)
  - [ATA 51](https://en.wikipedia.org/wiki/ATA_100) - Standard Practices and Structures
  - [ATA 53](https://en.wikipedia.org/wiki/ATA_100) - Fuselage
  - [ATA 57](https://en.wikipedia.org/wiki/ATA_100) - Wings
- Parent Document: [03-00-06_Engineering](../README.md)
- Related Documents:
  - [03-00-06-03-01A Load Analysis](./03-00-06-03-01A_Load_Analysis.md)
  - [03-00-06-03-02A Stress Analysis](./03-00-06-03-02A_Stress_Analysis.md)
  - [03-00-06-03-03A Fatigue Damage Tolerance](./03-00-06-03-03A_Fatigue_Damage_Tolerance.md)

## 8. Revision History
| Rev | Date | Author | Description |
|-----|------|--------|-------------|
| A | 2025-12-07 | AI (GitHub Copilot) | Initial release |

---

## Document Control

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT** – Subject to human review and approval.
- Human approver: _[to be completed]_.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: 2025-12-07.

---
