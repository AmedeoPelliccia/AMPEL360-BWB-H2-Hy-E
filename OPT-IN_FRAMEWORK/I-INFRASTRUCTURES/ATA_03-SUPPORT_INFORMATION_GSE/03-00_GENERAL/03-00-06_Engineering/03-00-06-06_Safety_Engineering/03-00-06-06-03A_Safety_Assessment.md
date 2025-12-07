# 03-00-06-06-03A - Safety Assessment

## 1. Purpose
Define the comprehensive safety assessment process for the AMPEL360 BWB-H2-Hy-E aircraft, integrating results from hazard analysis, FMEA, fault tree analysis, and testing to demonstrate compliance with CS-25.1309 and achieve certification authority approval.

## 2. Scope
This document covers:
- System Safety Assessment (SSA) methodology
- Integration of FHA, PSSA, FMEA, and FTA results
- Quantitative safety analysis and failure rate allocation
- Common Cause Analysis (CCA)
- Safety verification and validation
- Safety case documentation and presentation
- Coordination with certification authority

## 3. Applicable Documents
- [SAE ARP4761](https://www.sae.org/standards/content/arp4761a/) - Guidelines and Methods for Conducting the Safety Assessment Process
- [EASA CS-25.1309](https://www.easa.europa.eu/en/document-library/certification-specifications/cs-25-large-aeroplanes) - Equipment, Systems, and Installations
- [SAE ARP4754A](https://www.sae.org/standards/content/arp4754a/) - Guidelines for Development of Civil Aircraft and Systems
- [AC 25.1309-1A](https://www.faa.gov/regulations_policies/advisory_circulars/) - System Design and Analysis

## 4. Description

### 4.1 Overview
The Safety Assessment synthesizes all safety analyses (FHA, PSSA, FMEA, FTA, CCA) to demonstrate that the aircraft design meets safety requirements and that failure conditions meet their allocated probability targets. For the BWB-H2-Hy-E, special emphasis is placed on hydrogen system safety and novel propulsion architecture safety validation.

### 4.2 Requirements
**CS-25.1309 Requirements (Summary):**
- Systems must be designed such that:
  - Minor failure conditions are **probable** (frequent occurrence acceptable)
  - Major failure conditions are **remote** (<10^-5 per flight hour)
  - Hazardous failure conditions are **extremely remote** (<10^-7 per flight hour)
  - Catastrophic failure conditions are **extremely improbable** (<10^-9 per flight hour)
- Single failures must not lead to Catastrophic conditions
- Common Cause failures must be minimized through design independence

**Safety Assessment Deliverables:**
- System Safety Assessment (SSA) Report
- Failure rate predictions and allocations
- Fault tree analyses for top-level failure conditions
- Common Cause Analysis results
- Safety test reports
- Compliance matrix to CS-25.1309

### 4.3 Methodology
**System Safety Assessment Process:**

1. **Integrate Preliminary Analyses**
   - Compile FHA results (failure conditions and severity)
   - Integrate PSSA architecture and safety requirements
   - Incorporate FMEA failure mode data

2. **Quantitative Safety Analysis**
   - **Fault Tree Analysis (FTA):** Construct fault trees for Hazardous and Catastrophic conditions
   - **Failure Rate Data:** Use component reliability data (MIL-HDBK-217, NPRD, supplier data)
   - **Calculate Probabilities:** Sum of products through fault tree to top event
   - **Compare to Requirements:** Verify calculated probabilities meet CS-25.1309 targets

3. **Common Cause Analysis (CCA)**
   - **Zonal Safety Analysis:** Identify shared physical locations (fire zones, routing)
   - **Particular Risk Analysis:** Analyze common design, manufacturing, maintenance errors
   - **Common Mode Analysis:** Identify shared failure mechanisms
   - **Mitigation:** Ensure physical and functional independence (separation, dissimilar design)

4. **Safety Verification**
   - **Testing:** Failure injection, redundancy validation, safety function testing
   - **Analysis:** Review of fault trees, FMEA, design features
   - **Inspection:** Physical verification of separation, independence
   - **Service Experience:** Use data from similar systems (when available)

5. **Safety Validation**
   - Demonstrate system performs safely in operational environment
   - Conduct flight testing with fault injection (if safe to do so)
   - Validate assumptions in safety analysis

6. **Safety Case Preparation**
   - Document all safety activities and results
   - Prepare SSA report per ARP4761 format
   - Create compliance matrix to CS-25.1309
   - Address certification authority questions

**Example Safety Argument (for H2 System):**
- **Claim:** LH2 leak in passenger cabin is Extremely Improbable (<10^-9)
- **Evidence:**
  - Tank design: Type IV CFRP tank, burst tested to 3× operating pressure
  - Leak detection: Dual-redundant H2 sensors in all compartments
  - Isolation: Automatic shutoff valves on leak detection
  - Ventilation: Emergency ventilation system activated on detection
  - FTA calculation: P(leak & no detection & no isolation & no ventilation) < 10^-10
- **Conclusion:** Claim supported, meets CS-25.1309

## 5. Deliverables
| Deliverable | Format | Responsible | Due |
|-------------|--------|-------------|-----|
| System Safety Assessment (SSA) Report | PDF | Safety Lead | Pre-certification |
| Fault Tree Analyses | PDF/FTA tool | Safety Engineering | CDR |
| Failure Rate Allocation Document | Excel/CSV | Reliability Engineering | CDR |
| Common Cause Analysis Report | PDF/Markdown | Safety Engineering | CDR |
| Safety Verification Test Reports | PDF | Test Engineering | Integration/Flight test |
| CS-25.1309 Compliance Matrix | CSV/Excel | Safety Lead | Pre-certification |

## 6. Verification & Validation
**Acceptance Criteria:**
- SSA demonstrates compliance with CS-25.1309 for all failure conditions
- All Catastrophic and Hazardous conditions have validated probability <10^-9 and <10^-7 respectively
- No single failures lead to Catastrophic outcomes
- Common Cause Analysis shows adequate independence
- Safety testing validates safety functions
- Certification authority accepts safety case

**Verification Methods:**
- Independent review of SSA by safety experts
- Certification authority audit of safety assessment
- Flight testing with monitoring of safety-critical functions

## 7. Cross-References
- Related ATA Chapters:
  - [ATA 05](https://en.wikipedia.org/wiki/ATA_100) - Time Limits/Maintenance Checks
  - [ATA 28](https://en.wikipedia.org/wiki/ATA_100) - Fuel (H2 system safety)
  - [ATA 72](https://en.wikipedia.org/wiki/ATA_100) - Engine (propulsion safety)
- Parent Document: [03-00-06_Engineering](../README.md)
- Related Documents:
  - [03-00-06-06-01A Hazard Analysis](./03-00-06-06-01A_Hazard_Analysis.md)
  - [03-00-06-06-02A FMEA FMECA](./03-00-06-06-02A_FMEA_FMECA.md)
  - [03-00-06-06-04A Fault Tree Analysis](./03-00-06-06-04A_Fault_Tree_Analysis.md)

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
