---
Title: "Safety and Requirements Review Checklist — ATA 02"
Identifier: "AMPEL360-02-00-02-CHECKLIST"
Version: "1.0.0"
Status: "Active"
AccessLevel: "Internal"
Author: "Safety"
CreatedAt: "2025-11-14"
ModifiedAt: "2025-11-14"
Scope: "Checklist for safety and requirements reviews of ATA 02 Operations Information"
Abstract: "Provides a standardized checklist for reviewing safety-relevant operations information, ensuring hazards are properly recorded, traced, and mitigated per the Hazard Analysis Methodology."
Keywords: ["ATA 02", "Safety", "Checklist", "Review", "Quality Assurance"]
Compliance:
  - "ATA iSpec 2200"
  - "S1000D"
  - "AMPEL360 Doc Standard v1.1"
  - "Hazard Analysis Methodology — ATA 02"
Links:
  ParentGeneral: "../"
  HazardMethodology: "./AMPEL360-02-00-02-007A_Hazard_Analysis_Methodology.md"
  SafetyObjectives: "./AMPEL360-02-00-02-001A_Certification_Safety_Objectives.md"
  HazardsCSV: "./02-00-02-015A_Hazard_Log.csv"
ChangeLog:
  - {version: "1.0.0", date: "2025-11-14", author: "Safety", change: "Initial creation"}
---

# Safety and Requirements Review Checklist — ATA 02

## 1. Purpose

This checklist provides **standardized review criteria** for safety-relevant operations information under **ATA 02 — Operations Information**. It ensures that:

- Hazards are properly identified, recorded, and traced.
- Safety analyses (FTA, FMEA, CCA) are properly referenced.
- Emergency Response Procedures (ERP) and monitoring strategies are linked where applicable.

This checklist should be used during:

- **Content reviews** (new or updated operations information).
- **Requirements reviews** (safety-related requirements).
- **Certification readiness reviews**.

---

## 2. General Review Criteria

### 2.1 Applicability

- [ ] The content under review is identified as **safety-relevant** (impacts safety objectives, crew workload, operational margins, or regulatory compliance).
- [ ] The operational context(s) where this content applies are clearly defined (e.g., turnarounds, de-icing, taxi operations, gate changes).
- [ ] Applicability tags (aircraft type, configuration, airport, etc.) are correct and complete.

### 2.2 Traceability

- [ ] The content is traceable to:
  - [ ] **Safety objectives** in [Certification Safety Objectives — ATA 02](./AMPEL360-02-00-02-001A_Certification_Safety_Objectives.md).
  - [ ] **Requirements** in `../02-00-03_Requirements/`.
  - [ ] **Design or process documentation** as appropriate.

---

## 3. Hazard Recording and Classification

### 3.1 Hazard Identification

- [ ] All identified hazards related to this content are recorded in [02-00-02-015A_Hazard_Log.csv](./02-00-02-015A_Hazard_Log.csv).
- [ ] Each hazard has a unique **HazardID** (e.g., `HZ-02-0001`).
- [ ] Hazard **Description** clearly states the information-related failure or defect (e.g., "incorrect turnaround time", "missing precondition in de-icing procedure").

### 3.2 Hazard Classification

- [ ] Each hazard has an assigned **Severity** (Catastrophic, Hazardous, Major, Minor, No Effect).
- [ ] **Initial_Class** (initial risk before mitigations) is assigned using the program-specific risk scale.
- [ ] **Operational_Context** is clearly defined for each hazard.
- [ ] **Effect_On_Aircraft/Crew** is documented (e.g., reduced safety margins, increased workload, potential regulatory violations).

### 3.3 Methodology Compliance

- [ ] Is the hazard recorded in `Hazards.csv` using the **ATA 02 Hazard Analysis Methodology**?
  - Reference: [Hazard Analysis Methodology — ATA 02](./AMPEL360-02-00-02-007A_Hazard_Analysis_Methodology.md).
- [ ] The hazard follows the field semantics defined in **Section 4** of the methodology document.

---

## 4. Safety Analysis References

### 4.1 FTA/FMEA/CCA Integration

- [ ] Are **FTA**, **FMEA**, and **CCA** references populated in the hazard's **Notes** field?
  - [ ] FTA nodes (e.g., `FTA-02-A1.1`, `FTA-02-B3.1`) are referenced where the hazard contributes to fault tree paths.
  - [ ] FMEA rows (failure modes and causes) are referenced where applicable.
  - [ ] CCA entries (common cause conditions) are referenced if the hazard is influenced by shared infrastructure, processes, or roles.

### 4.2 ERP References

- [ ] If the hazard requires **Emergency Response Procedures (ERP)**, are ERP references populated in the hazard's **Notes** field?
  - Reference: [Emergency Response Procedures — ATA 02](./AMPEL360-02-00-02-003A_Emergency_Response_Procedures.md).
- [ ] ERP activation criteria and response steps are clearly linked to the hazard.

### 4.3 Runtime Monitoring

- [ ] If the hazard is mitigated by **runtime monitoring**, are monitoring strategies and triggers documented?
  - Reference: [Runtime Safety Monitoring — ATA 02](./AMPEL360-02-00-02-010A_Runtime_Safety_Monitoring.md).
- [ ] Monitoring metrics, thresholds, and alerting mechanisms are defined.

---

## 5. Mitigation and Residual Risk

### 5.1 Mitigations

- [ ] **Mitigations** for each hazard are documented in the `Mitigations` field of the hazard CSV.
- [ ] Mitigations include:
  - [ ] **Design-time controls** (requirements on data quality, structure, tools).
  - [ ] **Process controls** (reviews, approvals, configuration management).
  - [ ] **Runtime controls** (monitoring, ERP, operator procedures).

### 5.2 Verification

- [ ] Each mitigation has a corresponding **Verification_Link** in the hazard CSV.
- [ ] Verification evidence (tests, analyses, inspections, monitoring reports) is available and stored under:
  - [ ] `../02-00-07_V_AND_V/` (Verification and Validation folder).
  - [ ] `../02-00-10_Certification/` (Certification evidence folder).

### 5.3 Residual Risk

- [ ] **Residual_Class** (residual risk after mitigations) is assigned and documented in the hazard CSV.
- [ ] Residual risk is **acceptable** according to program-specific criteria (see [Program Tailoring Template](../02-00-10_Certification/Program_Tailoring_Template.md)).
- [ ] If residual risk is **not acceptable**, additional mitigations are planned and documented.

---

## 6. Requirements and Approval

### 6.1 Derived Requirements

- [ ] Safety-related requirements derived from hazards are documented in `../02-00-03_Requirements/`.
- [ ] Requirements are marked with appropriate safety tags/attributes (e.g., `SafetyLevel`, `SafetyCritical: true`).
- [ ] Requirements trace back to:
  - [ ] Hazards in `02-00-02-015A_Hazard_Log.csv`.
  - [ ] Safety objectives in [Certification Safety Objectives — ATA 02](./AMPEL360-02-00-02-001A_Certification_Safety_Objectives.md).

### 6.2 Approval Status

- [ ] The content under review has been **approved by qualified safety and certification roles** per program governance:
  - [ ] Safety Engineer (Ops).
  - [ ] Certification Focal.
  - [ ] Ops Information Lead (as applicable).
  - [ ] Technical Publications (as applicable).

- [ ] Approval is documented in:
  - [ ] Review records or sign-off sheets.
  - [ ] Configuration management system.

---

## 7. Configuration and Publication Control

### 7.1 Versioning and EIS Tagging

- [ ] The content has correct **version and EIS tags** consistent with `02-00-11_EIS_Versions_Tags` (if applicable).
- [ ] Changes to safety-relevant content are controlled and traceable to:
  - [ ] Source safety analyses (FHA, FTA, CCA, FMEA).
  - [ ] Approved change requests or safety bulletins.

### 7.2 Publication Consistency

- [ ] The content is consistent across all publication channels (e.g., central portal, EFB, printed copies).
- [ ] If the content includes safety-critical warnings, cautions, or limitations, these are:
  - [ ] Clearly formatted and positioned.
  - [ ] Verified to be present in all distribution formats.

---

## 8. Special Considerations

### 8.1 Human Factors

- [ ] If the content involves **crew or operator interaction**, a Human Factors assessment has been performed or is not required.
- [ ] Usability, workload, and situation awareness implications are considered and documented.

### 8.2 Neural Networks (if applicable)

- [ ] If the content relies on **neural network models** (e.g., performance prediction, anomaly detection), cross-references to ATA 97 and ATA 98 safety analyses are provided.

### 8.3 Airport and Infrastructure Dependencies

- [ ] If the content relies on **airport or infrastructure data feeds** (e.g., AODB, NOTAMs, weather feeds), data ingestion and freshness are verified.
- [ ] Monitoring for stale or incorrect data is in place.

---

## 9. Review Sign-Off

**Content/Document ID:** `[Insert ID]`

**Reviewer Name:** `[Insert Name]`

**Reviewer Role:** `[e.g., Safety Engineer, Certification Focal, Ops Information Lead]`

**Review Date:** `[Insert Date]`

**Review Outcome:**

- [ ] **Approved**: All checklist items are satisfied.
- [ ] **Approved with comments**: Minor issues noted; corrective actions documented.
- [ ] **Rejected**: Major issues identified; content requires rework.

**Comments/Actions:**

`[Provide any additional comments, observations, or required corrective actions.]`

**Signature:** `[Insert Signature]`

---

## 10. References

- [Hazard Analysis Methodology — ATA 02](./AMPEL360-02-00-02-007A_Hazard_Analysis_Methodology.md)
- [Certification Safety Objectives — ATA 02](./AMPEL360-02-00-02-001A_Certification_Safety_Objectives.md)
- [Fault Tree Analysis — ATA 02](./AMPEL360-02-00-02-005A_Fault_Tree_Analysis.md)
- [Common Cause Analysis — ATA 02](./AMPEL360-02-00-02-002A_Common_Cause_Analysis.md)
- [Emergency Response Procedures — ATA 02](./AMPEL360-02-00-02-003A_Emergency_Response_Procedures.md)
- [Runtime Safety Monitoring — ATA 02](./AMPEL360-02-00-02-010A_Runtime_Safety_Monitoring.md)
- [02-00-02-015A_Hazard_Log.csv](./02-00-02-015A_Hazard_Log.csv)
- [Program Tailoring Template](../02-00-10_Certification/Program_Tailoring_Template.md)

---
