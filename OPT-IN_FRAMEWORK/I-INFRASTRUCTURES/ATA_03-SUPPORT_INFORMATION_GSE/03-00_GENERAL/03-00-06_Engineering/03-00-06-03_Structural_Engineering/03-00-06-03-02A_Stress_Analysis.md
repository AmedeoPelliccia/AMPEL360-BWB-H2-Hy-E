# 03-00-06-03-02A - Stress Analysis

## 1. Purpose
Establish the methodology for conducting stress analysis of the AMPEL360 BWB-H2-Hy-E aircraft structure, ensuring all structural components meet strength requirements and demonstrate positive margins of safety for certification.

## 2. Scope
This document covers:
- Stress analysis methods and approaches
- Finite element analysis (FEA) procedures
- Classical stress analysis techniques
- Margin of safety calculations
- Stress concentrations and critical details
- Composite stress analysis considerations
- Hydrogen system structural integrity

## 3. Applicable Documents
- [EASA CS-25](https://www.easa.europa.eu/en/document-library/certification-specifications/cs-25-large-aeroplanes) - Subpart C: Structure, §25.301-§25.625
- [NACA Technical Note 527](https://ntrs.nasa.gov/citations/19930081305) - Stress Analysis of Aircraft Structures (classical reference)
- [ASTM E1049](https://www.astm.org/e1049-85r17.html) - Cycle Counting in Fatigue Analysis
- [CMH-17](https://www.cmh17.org/) - Composite Materials Handbook (for composite stress analysis)

## 4. Description

### 4.1 Overview
Stress analysis determines the structural response (stresses, strains, deflections) under applied loads, verifying that the structure can safely carry all design loads with adequate margins. For the BWB-H2-Hy-E, stress analysis addresses the unique load paths in the blended configuration, composite material behavior, and cryogenic effects from hydrogen storage.

### 4.2 Requirements
**Analysis Requirements per CS-25.301-305:**
- Structure shall withstand **limit loads** without detrimental permanent deformation
- Structure shall withstand **ultimate loads** (1.5× limit) without failure for at least 3 seconds
- Positive margins of safety required for all structural elements
- Special factor of 1.15 applies to castings (CS-25.621)
- Composite structures follow special certification requirements (AMC 20-29)

**Stress Analysis Objectives:**
1. Verify structural adequacy for all load cases
2. Calculate margins of safety (MS ≥ 0 required)
3. Identify critical structural elements and failure modes
4. Support structural optimization and weight reduction
5. Provide data for fatigue and damage tolerance analysis

**Margin of Safety Definition:**
```
MS = (Allowable Stress / Applied Stress) - 1

Where:
- Allowable Stress = Material ultimate strength / Safety Factor
- Applied Stress = Maximum stress under ultimate load
- MS ≥ 0 indicates acceptable design
```

### 4.3 Methodology
**Stress Analysis Approaches:**

1. **Finite Element Analysis (FEA)**
   - Primary method for complex structures
   - Models: shell, beam, solid elements as appropriate
   - Linear elastic analysis for most conditions
   - Nonlinear analysis for large deflections, contact, plasticity
   - Software: NASTRAN, ANSYS, Abaqus

2. **Classical Stress Analysis**
   - Hand calculations for simple components
   - Beam theory, plate theory, thin-walled sections
   - Used for preliminary design and FEA validation
   - Reference: Bruhn, Roark's Formulas for Stress

3. **Composite Stress Analysis**
   - Laminate theory for layered composites
   - Progressive failure analysis
   - Interlaminar stress evaluation
   - Bolted joint analysis with bearing/bypass

**Analysis Process:**

1. **Model Development**
   - Create FEA mesh from CAD geometry
   - Define material properties and layups
   - Apply boundary conditions
   - Apply loads from load analysis

2. **Stress Calculation**
   - Run FEA solver
   - Extract stress results (von Mises, principal, shear)
   - Identify peak stress locations

3. **Margin of Safety Evaluation**
   - Compare stresses to allowables
   - Calculate MS for critical elements
   - Document negative margins

4. **Iteration and Optimization**
   - Redesign areas with negative margins
   - Optimize weight in areas with excessive margins
   - Re-analyze and verify

**Critical Details Requiring Special Attention:**
- Wing-body junction in BWB configuration
- Hydrogen tank attachment and support structure
- Landing gear attachment and load introduction
- Door and window cutouts
- Bolted and bonded joint analysis
- Skin-stringer interface (composites)

## 5. Deliverables
| Deliverable | Format | Responsible | Due |
|-------------|--------|-------------|-----|
| Stress Analysis Plan | Markdown/PDF | Structures Lead | Project start |
| FEA Models | NASTRAN/ANSYS | Stress Engineer | PDR/CDR |
| Stress Analysis Reports | PDF/Markdown | Stress Engineer | CDR |
| Margin of Safety Summary | CSV/Excel | Stress Engineer | CDR |
| Critical Details Analysis | PDF | Stress Engineer | CDR |
| Structural Substantiation Report | PDF | Structures Lead | Certification |

## 6. Verification & Validation
**Acceptance Criteria:**
- All critical load cases analyzed
- Positive margins of safety for all structural elements
- FEA models validated against test data or hand calculations
- Composite failure criteria properly applied
- Stress concentration factors appropriate
- Analysis documented per certification requirements

**Verification Methods:**
- Independent check of critical analyses
- FEA benchmark problems for validation
- Comparison with coupon and element test results
- Static structural testing of critical components
- Full-scale structural testing (optional)
- Peer review by external experts

## 7. Cross-References
- Related ATA Chapters:
  - [ATA 05](https://en.wikipedia.org/wiki/ATA_100) - Time Limits/Maintenance Checks
  - [ATA 28](https://en.wikipedia.org/wiki/ATA_100) - Fuel System (H2 tank stress)
  - [ATA 53](https://en.wikipedia.org/wiki/ATA_100) - Fuselage
  - [ATA 57](https://en.wikipedia.org/wiki/ATA_100) - Wings
- Parent Document: [03-00-06_Engineering](../README.md)
- Related Documents:
  - [03-00-06-03-01A Load Analysis](./03-00-06-03-01A_Load_Analysis.md)
  - [03-00-06-03-03A Fatigue Damage Tolerance](./03-00-06-03-03A_Fatigue_Damage_Tolerance.md)
  - [03-00-06-03-04A Materials Selection](./03-00-06-03-04A_Materials_Selection.md)

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
