# 03-00-06-06-04A - Fault Tree Analysis

## 1. Purpose
Define the methodology for conducting Fault Tree Analysis (FTA) for the AMPEL360 BWB-H2-Hy-E aircraft, providing a systematic, top-down approach to analyze failure conditions, calculate probabilities, and identify critical failure paths for safety-critical systems.

## 2. Scope
This document covers:
- Fault tree construction methodology
- Boolean logic and gate types
- Quantitative and qualitative analysis
- Cut set analysis (minimal and critical)
- Importance measures and sensitivity analysis
- Integration with FMEA and hazard analysis
- Tool selection and usage

## 3. Applicable Documents
- [SAE ARP4761](https://www.sae.org/standards/content/arp4761a/) - Guidelines and Methods for Conducting the Safety Assessment Process
- [IEC 61025](https://www.iec.ch/homepage) - Fault Tree Analysis (FTA)
- [NASA Fault Tree Handbook](https://ntrs.nasa.gov/) - Fault Tree Analysis Guidance
- [MIL-HDBK-338B](https://quicksearch.dla.mil/qsDocDetails.aspx?ident_number=35789) - Electronic Reliability Design Handbook (failure rate data)

## 4. Description

### 4.1 Overview
Fault Tree Analysis is a top-down, deductive method that starts with an undesired top event (e.g., "Loss of All Thrust") and systematically identifies combinations of lower-level failures that can cause it. For the BWB-H2-Hy-E, FTA is critical for analyzing hydrogen system failures, electric propulsion loss, and flight control system failures.

### 4.2 Requirements
**FTA Objectives:**
- Identify all combinations of failures leading to a top event
- Calculate probability of top event occurrence
- Identify single-point failures and common cause failures
- Prioritize design improvements based on criticality
- Verify compliance with CS-25.1309 probability requirements

**Top Events for FTA (Examples):**
- **Catastrophic:**
  - Loss of all propulsive thrust
  - Loss of aircraft control (all axes)
  - Catastrophic H2 fire/explosion in cabin
- **Hazardous:**
  - Loss of >50% thrust
  - Loss of single control axis
  - Major H2 leak

**Fault Tree Gate Types:**
- **AND Gate:** Output occurs if ALL inputs occur
- **OR Gate:** Output occurs if ANY input occurs
- **VOTING Gate (k-out-of-n):** Output occurs if k out of n inputs occur
- **INHIBIT Gate:** Output occurs if input occurs AND enabling condition is true
- **TRANSFER Gate:** Reference to another fault tree

### 4.3 Methodology
**Fault Tree Construction Process:**

1. **Define Top Event**
   - Select undesired event (Catastrophic or Hazardous failure condition)
   - Define precisely (e.g., "Total Loss of Thrust > 1 minute in cruise")

2. **Identify Immediate Causes**
   - What conditions or failures directly cause the top event?
   - Use AND/OR logic to connect causes to top event

3. **Develop Tree Downward**
   - For each intermediate event, identify its causes
   - Continue until reaching basic events (component failures, human errors)

4. **Define Basic Events**
   - Assign failure rates to basic events (from data sources or estimation)
   - Failure rates in per flight hour (typically)

5. **Quantitative Analysis**
   - Calculate probability of top event using Boolean algebra
   - For AND gate: P(output) = P(A) × P(B) × P(C) ... (assuming independence)
   - For OR gate: P(output) ≈ P(A) + P(B) + P(C) ... (for small probabilities)
   - Use FTA software for complex trees (e.g., Relyence, PTC Windchill)

6. **Cut Set Analysis**
   - **Cut Set:** Set of basic events that, if all occur, cause top event
   - **Minimal Cut Set (MCS):** Cut set with no subset that is itself a cut set
   - **Single-Point Failures:** MCS with only one event (critical!)

7. **Importance Measures**
   - **Fussell-Vesely Importance:** Contribution of event to top event probability
   - **Birnbaum Importance:** Sensitivity of top event to event probability change
   - Use to prioritize design improvements

**Example Fault Tree Snippet:**
```
Top Event: Total Loss of Thrust
  OR Gate
    ├─ Loss of H2 Supply
    │   OR Gate
    │     ├─ All H2 Tanks Empty (Basic Event, P=10^-6)
    │     └─ H2 Distribution Failure
    │         AND Gate
    │           ├─ Primary Distribution Line Blocked (P=10^-5)
    │           └─ Backup Distribution Line Blocked (P=10^-5)
    └─ Loss of All Electric Motors
        AND Gate
          ├─ Motor 1 Failure (P=10^-4)
          ├─ Motor 2 Failure (P=10^-4)
          └─ Motor 3 Failure (P=10^-4)
```

**Quantitative Result:**
- P(H2 Supply Loss) ≈ 10^-6 + (10^-5 × 10^-5) = 10^-6 (dominant term)
- P(All Motors Fail) = 10^-4 × 10^-4 × 10^-4 = 10^-12
- P(Total Loss of Thrust) ≈ 10^-6 + 10^-12 ≈ 10^-6

**Interpretation:** Meets <10^-9 requirement? No! Need design improvement for H2 supply redundancy.

## 5. Deliverables
| Deliverable | Format | Responsible | Due |
|-------------|--------|-------------|-----|
| Fault Tree Analysis Plan | Markdown/PDF | Safety Lead | Project start |
| Fault Tree Diagrams | PDF/FTA Tool | Safety Engineering | CDR |
| Quantitative FTA Results | PDF/Excel | Safety Engineering | CDR |
| Cut Set Analysis Report | PDF/Markdown | Safety Engineering | CDR |
| Importance Ranking | CSV/Excel | Safety Engineering | CDR |
| Recommendations for Design Improvement | Markdown | Safety Lead | CDR |

## 6. Verification & Validation
**Acceptance Criteria:**
- Fault trees constructed for all Catastrophic and Hazardous failure conditions
- All branches of fault trees traced to basic events
- Quantitative analysis demonstrates compliance with CS-25.1309
- No single-point failures lead to Catastrophic conditions
- Design improvements identified for high-importance events
- FTA results consistent with FMEA and testing

**Verification Methods:**
- Peer review of fault tree logic
- Independent recalculation of probabilities
- Cross-check with FMEA
- Validation through testing (failure injection when safe)

## 7. Cross-References
- Related ATA Chapters:
  - [ATA 28](https://en.wikipedia.org/wiki/ATA_100) - Fuel (H2 system FTA)
  - [ATA 72](https://en.wikipedia.org/wiki/ATA_100) - Engine (propulsion FTA)
  - [ATA 27](https://en.wikipedia.org/wiki/ATA_100) - Flight Controls (FCS FTA)
- Parent Document: [03-00-06_Engineering](../README.md)
- Related Documents:
  - [03-00-06-06-01A Hazard Analysis](./03-00-06-06-01A_Hazard_Analysis.md)
  - [03-00-06-06-02A FMEA FMECA](./03-00-06-06-02A_FMEA_FMECA.md)
  - [03-00-06-06-03A Safety Assessment](./03-00-06-06-03A_Safety_Assessment.md)

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
