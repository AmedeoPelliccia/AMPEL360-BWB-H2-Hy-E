# 03-00-06-03-03A - Fatigue and Damage Tolerance

## 1. Purpose
Define the approach for ensuring the AMPEL360 BWB-H2-Hy-E aircraft structure meets fatigue life and damage tolerance requirements, demonstrating safe operation over the design service life with consideration for accidental damage and discrete source damage.

## 2. Scope
This document covers:
- Fatigue life analysis methodology
- Damage tolerance analysis and substantiation
- Crack growth analysis and residual strength
- Widespread fatigue damage (WFD) considerations
- Inspectability and inspection programs
- Special considerations for composite structures
- Hydrogen system fatigue and damage tolerance

## 3. Applicable Documents
- [EASA CS-25.571](https://www.easa.europa.eu/en/document-library/certification-specifications/cs-25-large-aeroplanes) - Damage Tolerance and Fatigue Evaluation of Structure
- [AC 25.571-1D](https://www.faa.gov/regulations_policies/advisory_circulars/index.cfm/go/document.information/documentID/99693) - Damage Tolerance and Fatigue Evaluation of Structure
- [ASTM E647](https://www.astm.org/e0647-15e01.html) - Measurement of Fatigue Crack Growth Rates
- [MIL-STD-1530D](https://quicksearch.dla.mil/qsDocDetails.aspx?ident_number=283915) - Aircraft Structural Integrity Program (ASIP)

## 4. Description

### 4.1 Overview
Fatigue and damage tolerance analysis ensures the aircraft structure can operate safely throughout its design service life, accounting for cyclic loading, environmental effects, manufacturing defects, and in-service damage. The BWB-H2-Hy-E structure must address unique fatigue drivers including pressurization cycles over large cabin area, cryogenic cycling in hydrogen systems, and composite fatigue behavior.

### 4.2 Requirements
**CS-25.571 Key Requirements:**
1. **Fatigue Evaluation** - Structure must withstand repeated loads of variable magnitude expected in service
2. **Damage Tolerance Evaluation** - Structure must demonstrate residual strength with damage
3. **Damage Types Considered:**
   - Accidental damage (e.g., ground handling, hail, runway debris)
   - Discrete source damage (e.g., partial failure of multi-element structure)
   - Environmental degradation (corrosion, erosion)
   - Fatigue cracking

**Design Service Goal (DSG):**
- Typical transport: 50,000-60,000 flight hours or 20,000-25,000 flights
- Structure must demonstrate safe operation for 2× DSG (extended service goal)

**Damage Tolerance Philosophy:**
- **Slow crack growth** - Inspectable structure with sufficient growth life
- **Fail-safe (multiple load paths)** - Residual strength after single element failure
- **Crack arrest features** - Limit crack propagation

### 4.3 Methodology
**Fatigue Analysis Process:**

1. **Define Fatigue Spectrum**
   - Develop loading spectrum from mission profile
   - Flight-by-flight loads (FALSTAFF, Mini-TWIST spectra)
   - Ground-air-ground cycles
   - Cabin pressurization cycles
   - Gust and maneuver loads

2. **Fatigue Life Prediction**
   - S-N approach for metallic components
   - Miner's rule for cumulative damage
   - Strain-life method for critical details
   - Composite fatigue degradation models

3. **Calculate Scatter Factor**
   - Account for material variability, manufacturing quality
   - Typical scatter factor: 4 on life (95% survival, 95% confidence)

**Damage Tolerance Analysis Process:**

1. **Identify Principal Structural Elements (PSEs)**
   - Wings, fuselage, empennage (or BWB equivalent)
   - Primary load-carrying structure
   - Single load path components

2. **Assume Initial Flaw**
   - Manufacturing defect or in-service damage
   - Size based on inspectability and NDI capability
   - Typical: 0.05" for high-quality fastener holes, 1.0" for large panels

3. **Perform Crack Growth Analysis**
   - Apply Paris law: da/dN = C(ΔK)^m
   - Calculate stress intensity factor (K) using FEA or handbook solutions
   - Determine crack growth life under spectrum loading

4. **Residual Strength Analysis**
   - Calculate critical crack length using fracture toughness (Kc)
   - Verify structure can withstand limit load with critical damage
   - Establish inspection intervals

**Composite Damage Tolerance:**
- Barely visible impact damage (BVID) approach
- Compression-after-impact (CAI) strength reduction
- No-growth assumption for matrix cracks
- Damage resistance and tolerance testing per CMH-17

**Hydrogen System Considerations:**
- Cryogenic thermal cycling effects on crack growth
- Hydrogen embrittlement of metallic components
- Low-temperature fracture toughness
- Composite performance at cryogenic temperatures

## 5. Deliverables
| Deliverable | Format | Responsible | Due |
|-------------|--------|-------------|-----|
| Fatigue & DT Analysis Plan | Markdown/PDF | Structures Lead | Project start |
| Fatigue Spectrum Development | CSV/Excel | Loads Engineer | PDR |
| Fatigue Life Analysis Report | PDF/Markdown | Fatigue Engineer | CDR |
| Damage Tolerance Analysis Report | PDF/Markdown | DT Engineer | CDR |
| Crack Growth Curves | SVG/PDF | DT Engineer | CDR |
| Inspection Program | Markdown/PDF | Structures Lead | Certification |
| Structural Repair Manual (SRM) | PDF | Structures/Maintenance | EIS |

## 6. Verification & Validation
**Acceptance Criteria:**
- Fatigue life exceeds 2× design service goal
- All PSEs demonstrate damage tolerance
- Inspection intervals established and justified
- Residual strength meets CS-25.571(b) requirements
- Full-scale fatigue testing completed (if required)
- Damage tolerance testing validates analysis

**Test Methods:**
- Coupon fatigue testing for material allowables
- Element fatigue testing for joint details
- Full-scale static testing with damage
- Full-scale fatigue testing (2× lifetime spectrum)
- Teardown inspection after fatigue test
- Composite impact and CAI testing

## 7. Cross-References
- Related ATA Chapters:
  - [ATA 05](https://en.wikipedia.org/wiki/ATA_100) - Time Limits/Maintenance Checks (inspection intervals)
  - [ATA 28](https://en.wikipedia.org/wiki/ATA_100) - Fuel System (H2 tank fatigue)
  - [ATA 51](https://en.wikipedia.org/wiki/ATA_100) - Standard Practices and Structures (repairs)
  - [ATA 53](https://en.wikipedia.org/wiki/ATA_100) - Fuselage
  - [ATA 57](https://en.wikipedia.org/wiki/ATA_100) - Wings
- Parent Document: [03-00-06_Engineering](../README.md)
- Related Documents:
  - [03-00-06-03-01A Load Analysis](./03-00-06-03-01A_Load_Analysis.md)
  - [03-00-06-03-02A Stress Analysis](./03-00-06-03-02A_Stress_Analysis.md)
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
