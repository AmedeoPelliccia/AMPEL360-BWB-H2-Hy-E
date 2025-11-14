---
Title: "Program Tailoring Template — ATA 02 Hazard Analysis"
Identifier: "AMPEL360-02-00-10-XXX"
Version: "1.0.0"
Status: "Template"
AccessLevel: "Internal"
Author: "Safety/CERT"
CreatedAt: "2025-11-14"
ModifiedAt: "2025-11-14"
Scope: "Template for program-specific tailoring of ATA 02 Hazard Analysis Methodology"
Abstract: "This template document should be instantiated for each program to confirm severity/DAL mapping and define program-specific risk classification scales and approval thresholds."
Keywords: ["ATA 02", "Hazard Analysis", "Tailoring", "Program-Specific", "Certification"]
Compliance:
  - "ATA iSpec 2200"
  - "S1000D"
  - "AMPEL360 Doc Standard v1.1"
  - "Hazard Analysis Methodology — ATA 02"
Links:
  ParentGeneral: "../"
  HazardMethodology: "../02-00-02_Safety/AMPEL360-02-00-02-007A_Hazard_Analysis_Methodology.md"
  SafetyObjectives: "../02-00-02_Safety/AMPEL360-02-00-02-001A_Certification_Safety_Objectives.md"
ChangeLog:
  - {version: "1.0.0", date: "2025-11-14", author: "Safety/CERT", change: "Initial template creation"}
---

# Program Tailoring Template — ATA 02 Hazard Analysis

## 1. Purpose

This document provides a **template** for program-specific tailoring of the [Hazard Analysis Methodology — ATA 02](../02-00-02_Safety/AMPEL360-02-00-02-007A_Hazard_Analysis_Methodology.md). Each program should create an instance of this template to document:

1. Confirmation of the severity/DAL mapping used for the program.
2. Program-specific risk classification scales.
3. Program-specific approval thresholds and governance processes.

The base methodology document (`AMPEL360-02-00-02-007A`) is **program-agnostic**. This tailoring note ensures that program-specific requirements, constraints, and certification basis are properly captured and linked.

---

## 2. Program Identification

**Program Name:** `[Insert Program Name, e.g., "AMPEL360-BWB-H2"]`

**Program Code:** `[Insert Program Code]`

**Certification Basis:** `[Insert applicable regulations, e.g., "CS-25", "FAR Part 25", etc.]`

**Certification Authority:** `[Insert authority, e.g., "EASA", "FAA", etc.]`

**Date of Tailoring:** `[Insert Date]`

**Author/Responsible Party:** `[Insert Name/Role]`

---

## 3. Severity and DAL Mapping Confirmation

### 3.1 Base Mapping (from Methodology)

The base Hazard Analysis Methodology defines the following severity/DAL mapping:

| Severity       | DAL |
|----------------|-----|
| Catastrophic   | A   |
| Hazardous      | B   |
| Major          | C   |
| Minor          | D   |
| No Effect      | E   |

### 3.2 Program Confirmation

**Confirm or modify the above mapping for this program:**

- [ ] **Confirmed**: The base mapping is adopted without changes.
- [ ] **Modified**: The mapping has been modified as follows:

  | Severity       | DAL | Program-Specific Notes |
  |----------------|-----|------------------------|
  | [e.g., Major]  | [C] | [e.g., "For ops information, Major is treated as DAL C with additional HF review."] |

**Justification for any modifications:**

`[Provide rationale if the mapping deviates from the base methodology, including references to certification basis, regulatory requirements, or program-specific risk considerations.]`

---

## 4. Risk Classification Scale

### 4.1 Initial and Residual Risk Classes

The base methodology uses a risk classification scale (e.g., 1-5) for **Initial_Class** and **Residual_Class** in the hazard CSV. Define the program-specific scale here:

| Risk Class | Description | Acceptability Criteria |
|------------|-------------|------------------------|
| 1          | [e.g., "Very Low"] | [e.g., "Acceptable without additional review."] |
| 2          | [e.g., "Low"] | [e.g., "Acceptable with documented mitigations."] |
| 3          | [e.g., "Medium"] | [e.g., "Requires safety review and approval."] |
| 4          | [e.g., "High"] | [e.g., "Requires senior safety approval and continuous monitoring."] |
| 5          | [e.g., "Very High"] | [e.g., "Unacceptable; immediate corrective action required."] |

**Notes:**

`[Provide any additional context for how risk classes are assigned, including consideration of likelihood, severity, and operational context.]`

---

## 5. Approval Thresholds and Governance

### 5.1 Approval Workflows

Define the approval thresholds for hazards based on their classification:

| Residual Risk Class | Approval Required | Notes |
|---------------------|-------------------|-------|
| 1-2                 | [e.g., "Ops Information Lead"] | [e.g., "Standard approval process."] |
| 3                   | [e.g., "Safety Engineer + Certification Focal"] | [e.g., "Requires documented evidence of mitigations."] |
| 4-5                 | [e.g., "Chief Safety Officer + Certification Authority"] | [e.g., "May require design changes or additional mitigations."] |

### 5.2 Change Control

Define the process for managing changes to hazards:

- **New hazards identified:** `[e.g., "Must be added to AMPEL360-02-00-02_Hazards.csv within 5 business days of identification."]`
- **Changes to existing hazards:** `[e.g., "Requires re-assessment and approval per Section 5.1."]`
- **Emergency changes:** `[e.g., "Streamlined approval by Safety Engineer + Certification Focal, with full review within 10 business days."]`

---

## 6. Program-Specific Considerations

### 6.1 Operational Context

Describe any program-specific operational contexts that should be considered during hazard analysis:

`[e.g., "This program includes operations at high-altitude airports with limited infrastructure, requiring additional focus on airport data ingestion and applicability tagging hazards."]`

### 6.2 Special Requirements

Identify any program-specific requirements that influence hazard analysis:

`[e.g., "The program includes neural network-based performance prediction tools; hazards related to NN model outputs must be cross-referenced with ATA 97 and ATA 98 safety analyses."]`

---

## 7. Traceability and Integration

### 7.1 Linking to Base Methodology

All hazards recorded for this program in `AMPEL360-02-00-02_Hazards.csv` must be traceable to:

- The base [Hazard Analysis Methodology — ATA 02](../02-00-02_Safety/AMPEL360-02-00-02-007A_Hazard_Analysis_Methodology.md).
- This program tailoring document.

### 7.2 Integration with Safety Artefacts

Ensure that hazards are integrated with:

- **Certification Safety Objectives** (`AMPEL360-02-00-02-001A`)
- **FTA** (`AMPEL360-02-00-02-005A`)
- **CCA** (`AMPEL360-02-00-02-002A`)
- **FMEA** (as applicable)
- **V&V and Certification Evidence** (under `../02-00-07_V_AND_V/` and this folder)

---

## 8. Review and Update

This tailoring document should be reviewed and updated:

- At the start of each certification phase (e.g., preliminary design, detailed design, type certification).
- When the certification basis or regulatory requirements change.
- After significant program changes (e.g., new configurations, new operational contexts).

**Next Review Date:** `[Insert Date]`

---

## 9. Approval

| Role | Name | Signature | Date |
|------|------|-----------|------|
| Safety Engineer | [Insert Name] | [Insert Signature] | [Insert Date] |
| Certification Focal | [Insert Name] | [Insert Signature] | [Insert Date] |
| Program Manager | [Insert Name] | [Insert Signature] | [Insert Date] |

---
