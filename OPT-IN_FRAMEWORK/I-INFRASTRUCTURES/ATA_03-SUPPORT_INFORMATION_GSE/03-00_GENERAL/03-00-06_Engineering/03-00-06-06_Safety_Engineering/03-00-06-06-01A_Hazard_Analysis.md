# 03-00-06-06-01A - Hazard Analysis

## 1. Purpose
Establish the methodology for conducting comprehensive hazard analysis of the AMPEL360 BWB-H2-Hy-E aircraft, identifying potential hazards, assessing their severity and likelihood, and defining mitigations to achieve acceptable safety levels for certification.

## 2. Scope
This document covers:
- Functional Hazard Assessment (FHA)
- Preliminary System Safety Assessment (PSSA)
- System Safety Assessment (SSA)
- Hydrogen-specific hazard identification
- BWB configuration-specific hazards
- Safety requirements derivation
- Hazard tracking and resolution

## 3. Applicable Documents
- [SAE ARP4761](https://www.sae.org/standards/content/arp4761a/) - Guidelines and Methods for Conducting the Safety Assessment Process
- [EASA CS-25.1309](https://www.easa.europa.eu/en/document-library/certification-specifications/cs-25-large-aeroplanes) - Equipment, Systems, and Installations
- [SAE ARP4754A](https://www.sae.org/standards/content/arp4754a/) - Guidelines for Development of Civil Aircraft and Systems
- [ISO 26262](https://www.iso.org/standard/68383.html) - Functional Safety (reference for automotive, adapted for aviation)

## 4. Description

### 4.1 Overview
Hazard analysis systematically identifies failure conditions, evaluates their effects on the aircraft and occupants, and ensures appropriate design features and procedures are in place to mitigate risks. For the BWB-H2-Hy-E, special attention is required for hydrogen system hazards and novel BWB configuration failure modes.

### 4.2 Requirements
**Safety Assessment Process per ARP4761:**
1. **Functional Hazard Assessment (FHA)** - Identify functions and failure conditions
2. **Preliminary System Safety Assessment (PSSA)** - Develop safety requirements
3. **System Safety Assessment (SSA)** - Verify safety requirements are met

**Failure Condition Classifications per CS-25.1309:**
- **No Safety Effect:** No effect on safety
- **Minor:** Nuisance, slight reduction in safety margin
- **Major:** Significant reduction in safety margin, crew workload increases
- **Hazardous:** Large reduction in safety margin, serious injuries possible
- **Catastrophic:** Multiple fatalities, hull loss

**Probability Requirements:**
- **Minor:** < 10^-3 per flight hour
- **Major:** < 10^-5 per flight hour
- **Hazardous:** < 10^-7 per flight hour
- **Catastrophic:** < 10^-9 per flight hour (extremely improbable)

### 4.3 Methodology
**Functional Hazard Assessment (FHA):**
1. **Identify Functions:** List all aircraft and system functions
2. **Identify Failure Conditions:** Determine how each function can fail
3. **Assess Effects:** Evaluate impact on aircraft, crew, passengers
4. **Classify Severity:** Assign Minor, Major, Hazardous, or Catastrophic
5. **Derive Safety Requirements:** Define requirements to mitigate hazards

**Example FHA Entries:**
| Function | Failure Condition | Effect | Classification | Safety Requirement |
|----------|-------------------|--------|----------------|---------------------|
| Provide Thrust | Total loss of thrust | Forced landing | Hazardous | Dual propulsion systems, OEI capability |
| Store Hydrogen | LH2 leak in cabin | Fire/explosion hazard | Catastrophic | Leak detection, isolation, ventilation |
| Control Flight | Loss of pitch control | Loss of aircraft control | Catastrophic | Triple-redundant flight control, dissimilar actuation |

**Preliminary System Safety Assessment (PSSA):**
- Develop system architecture to meet safety requirements
- Allocate failure rate budgets to subsystems
- Identify design features (redundancy, monitoring, fault tolerance)
- Identify Common Cause Failures (CCF) and single points of failure
- Define verification activities

**System Safety Assessment (SSA):**
- Verify actual system meets safety requirements
- Conduct FMEA, FTA, Common Cause Analysis
- Validate failure rates through testing and analysis
- Demonstrate compliance with probability requirements
- Prepare safety case for certification authority

**Hydrogen-Specific Hazards:**
- Cryogenic LH2 leak and fire/explosion
- Hydrogen embrittlement of structural materials
- Boil-off gas accumulation and venting
- Overpressure in storage tanks
- Loss of thermal insulation leading to rapid boil-off

**BWB Configuration Hazards:**
- Non-traditional load paths and structural failure modes
- Large cabin area pressurization hazards
- Center body structural damage affecting propulsion and fuel systems
- Passenger evacuation from wide-body interior

## 5. Deliverables
| Deliverable | Format | Responsible | Due |
|-------------|--------|-------------|-----|
| Safety Assessment Plan (SAP) | PDF | Safety Lead | Project start |
| Functional Hazard Assessment (FHA) | PDF/CSV | Safety Engineering | Conceptual design |
| Preliminary System Safety Assessment (PSSA) | PDF | Safety Engineering | PDR |
| System Safety Assessment (SSA) | PDF | Safety Engineering | Pre-certification |
| Hazard Log | CSV/Excel | Safety Engineering | Ongoing |
| Safety Case Report | PDF | Safety Lead | Certification phase |

## 6. Verification & Validation
**Acceptance Criteria:**
- All functions and failure conditions identified
- All hazards classified by severity
- Safety requirements derived and allocated
- SSA demonstrates compliance with probability requirements
- No unmitigated Catastrophic or Hazardous single-point failures
- Certification authority accepts safety case

**Verification Methods:**
- FHA review with stakeholders
- PSSA review at design reviews
- SSA validation through testing, analysis, and inspection
- Independent safety audits

## 7. Cross-References
- Related ATA Chapters:
  - [ATA 05](https://en.wikipedia.org/wiki/ATA_100) - Time Limits/Maintenance Checks
  - [ATA 28](https://en.wikipedia.org/wiki/ATA_100) - Fuel (H2 hazards)
  - [ATA 72](https://en.wikipedia.org/wiki/ATA_100) - Engine (propulsion hazards)
  - [ATA 73](https://en.wikipedia.org/wiki/ATA_100) - Engine Fuel and Control
- Parent Document: [03-00-06_Engineering](../README.md)
- Related Documents:
  - [03-00-06-06-02A FMEA FMECA](./03-00-06-06-02A_FMEA_FMECA.md)
  - [03-00-06-06-03A Safety Assessment](./03-00-06-06-03A_Safety_Assessment.md)
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
