---
Title: "Hazard Analysis Methodology — ATA 02"
Identifier: "AMPEL360-02-00-02-007A"
Version: "1.0.0"
Status: "Draft"
AccessLevel: "Internal"
Author: "Safety"
CreatedAt: "2025-11-13"
ModifiedAt: "2025-11-13"
Scope: "Methodology for hazard analysis of ATA 02 Operations Information within I-INFRASTRUCTURES"
Abstract: "Defines the methodology for identifying, classifying, mitigating, and verifying hazards related to ATA 02 operations information, including sources, severity/DAL mapping, and traceability expectations."
Keywords: ["ATA 02", "Hazard Analysis", "Methodology", "Safety", "Operations Information"]
Compliance:
  - "ATA iSpec 2200"
  - "S1000D"
  - "AMPEL360 Doc Standard v1.1"
  - "Certification Safety Objectives — ATA 02"
Links:
  ParentGeneral: "../"
  SafetyObjectives: "./AMPEL360-02-00-02-001A_Certification_Safety_Objectives.md"
  CCA: "./AMPEL360-02-00-02-002A_Common_Cause_Analysis.md"
  ERP: "./AMPEL360-02-00-02-003A_Emergency_Response_Procedures.md"
  FTA: "./AMPEL360-02-00-02-005A_Fault_Tree_Analysis.md"
  HazardsCSV: "./02-00-02-015A_Hazard_Log.csv"
  Requirements: "../02-00-03_Requirements/"
  VAndV: "../02-00-07_V_AND_V/"
  Certification: "../02-00-10_Certification/"
ChangeLog:
  - {version: "1.0.0", date: "2025-11-13", author: "Safety", change: "Initial creation"}
---

# Hazard Analysis Methodology — ATA 02

## 1. Purpose

This document defines the **hazard analysis methodology** for **ATA 02 — Operations Information**. It specifies:

- The **process steps** used to analyse hazards related to operations information.
- The **sources** from which hazards are identified.
- The **classification scheme** (severity and DAL) applied to these hazards.
- The **traceability model** linking hazards to requirements, tests, and evidence.

It ensures consistency across programs and provides the methodological bridge between:

- High-level **Certification Safety Objectives — ATA 02**.
- Detailed artefacts such as **CCA**, **FMEA**, **FTA**, **ERP**, and **hazard lists**.

---

## 2. Process Overview

Hazard analysis for ATA 02 operations information follows a simple, repeatable lifecycle:

> **Identification → Classification → Mitigation → Verification → Residual Risk Assessment**

### 2.1 Identification

Identify potential hazards where **operations information contributes to or fails to prevent unsafe conditions**, for example:

- Incorrect, incomplete, or ambiguous data or procedures.
- Stale or mis-applied airport, infrastructure, or weather information.
- Misleading presentation, layout, or tagging (e.g., applicability errors).
- Failures in publication, distribution, or configuration control.

**Sources of hazards** include (but are not limited to):

- **Operations processes**  
  - Turnaround workflows, ground operations, dispatch, crew procedures.

- **Datasets and tables**  
  - Performance and turnaround data, constraints tables, applicability matrices.

- **Airport and infrastructure interfaces**  
  - AODB, NOTAMs, airport constraints databases, ground services interfaces.

- **Tooling and automation**  
  - Authoring tools, ETL/ingestion pipelines, publication and distribution systems, EFB platforms.

Hazards are recorded in a structured way, e.g. in `02-00-02-015A_Hazard_Log.csv`.

### 2.2 Classification

Each identified hazard is classified according to:

1. **Severity** — effect on aircraft/crew/operation.
2. **Initial risk class** — before mitigations.
3. **Design Assurance Level (DAL)** — derived from severity and applicable standards.

### 2.3 Mitigation

For each hazard:

- Define **preventive** and **detective / reactive** mitigations, which may include:
  - Design-time controls (requirements on data quality, structure, tools).
  - Process controls (reviews, approvals, configuration management).
  - Runtime controls (monitoring, ERP, operator procedures).

### 2.4 Verification

Define and perform verification activities to show that mitigations are effective, e.g.:

- Tests, analyses, inspections.
- Monitoring and validation exercises.
- ERP drills or dry-run exercises.

Verification artefacts are stored under `../02-00-07_V_AND_V/` and `../02-00-10_Certification/`.

### 2.5 Residual Risk Assessment

After mitigations and verification:

- Re-assess the **residual risk**:
  - Assign **Residual_Class** consistent with your internal risk scale.
  - Confirm that residual risk is acceptable against program criteria.

If residual risk is not acceptable, iterate (new or strengthened mitigations, re-verification).

---

## 3. Hazard Classifications

### 3.1 Severity Levels

Severity is assessed using standard categories, interpreted for **operations information**:

| Severity       | Description (Ops Information Context)                                                                                      |
|----------------|----------------------------------------------------------------------------------------------------------------------------|
| Catastrophic   | Multiple fatalities and/or loss of aircraft potentially resulting from incorrect/missing ops information.                 |
| Hazardous      | Serious or fatal injuries; large reduction in safety margins; workload or confusion such that crew may be unable to cope. |
| Major          | Significant reduction in safety margins; increased crew workload or errors; possible passenger discomfort or minor injuries. |
| Minor          | Slight reduction in safety margins or slight increase in workload; minor deviations; negligible safety impact.             |
| No Effect      | No effect on operational safety; purely economic or cosmetic impact.                                                       |

### 3.2 DAL Mapping

Severity levels are mapped to **Design Assurance Levels (DAL)** as follows (simplified; program-specific tailoring is allowed):

- **Catastrophic → DAL A**
- **Hazardous → DAL B**
- **Major → DAL C**
- **Minor → DAL D**
- **No Effect → DAL E**

For ATA 02, DAL focuses on:

- Quality and integrity of safety-relevant operations information.
- Assurance levels for tools and processes that produce/publish this information.

Any deviations from this mapping (e.g., due to specific certification basis) must be documented in `../02-00-10_Certification/` and referenced here.

---

## 4. Hazard Record Structure

Hazards are typically captured in a structured artefact such as:

```
HazardID,Description,Operational_Context,Effect_On_Aircraft/Crew,Severity,Initial_Class,Mitigations,Residual_Class,Verification_Link,Notes
```

### 4.1 Field Semantics

- **HazardID**  
  Unique identifier (e.g. `H-02-001`) for reference across FTA, FMEA, CCA, requirements.

- **Description**  
  Short, clear statement of the hazard, focusing on the **information-related failure** (e.g. “Ops manual turnaround time incorrect”).

- **Operational_Context**  
  Context in which the hazard manifests (e.g. turnarounds, de-icing operations, taxi-in, gate changes).

- **Effect_On_Aircraft/Crew**  
  Operational and safety effect (e.g. reduced safety margins, increased workload, potential rule violations).

- **Severity**  
  One of: Catastrophic, Hazardous, Major, Minor, No Effect.

- **Initial_Class**  
  Initial risk ranking before mitigations (use program-specific scale, e.g. 1–5).

- **Mitigations**  
  Summary of key mitigations (design, process, runtime) associated with this hazard. Should reference:
  - Relevant requirements.
  - ERP/monitoring strategies where applicable.

- **Residual_Class**  
  Risk ranking after mitigations and verification (same scale as Initial_Class).

- **Verification_Link**  
  Pointer to verification evidence (e.g. test report, analysis document, monitoring report).

- **Notes**  
  Free text for traceability references (FTA nodes, CCA entries, ERP references, requirement IDs).

---

## 5. Traceability Model

### 5.1 Required Links

Each hazard must be traceable to:

- **Safety objectives**  
  - At least one safety objective in `Certification Safety Objectives — ATA 02`.

- **Requirements**  
  - One or more requirements in `../02-00-03_Requirements/` specifically addressing the hazard.

- **Tests and analyses**  
  - Verification activities and evidence in `../02-00-07_V_AND_V/` and/or `../02-00-10_Certification/`.

- **Safety analyses**  
  - FTA events (Top Event branches).
  - FMEA rows (failure modes and causes).
  - CCA entries (where a common cause is involved).

### 5.2 Typical Traceability Chain

A typical chain for a hazard might look like:

> **Hazard (H-02-XXX)**  
> → **FTA node(s)** (e.g. FTA-02-A1.1, B3.1)  
> → **FMEA row(s)** (functions, failure modes, causes)  
> → **Requirements** (Req IDs in `../02-00-03_Requirements/`)  
> → **Mitigations in design/process/tooling**  
> → **Verification evidence** (tests, analyses, monitoring)  
> → **Residual risk assessment** (Hazard CSV)

This chain should be navigable via identifiers recorded in the hazard CSV (e.g. in `Notes` or a dedicated references field).

---

## 6. Integration with Other Safety Artefacts

### 6.1 Certification Safety Objectives

- Use `AMPEL360-02-00-02-001A_Certification_Safety_Objectives.md` as the **starting point**.  
- For each hazard, indicate which safety objective(s) it supports or threatens.

### 6.2 CCA, FMEA, FTA

- **CCA**:  
  - Identify whether the hazard is influenced by **common cause conditions** (e.g., shared data sources, publication pipeline).
- **FMEA**:  
  - Ensure the hazard is represented via relevant failure modes and causes.
- **FTA**:  
  - Map the hazard to paths in the FTA leading to the Top Event.

### 6.3 ERP and Runtime Monitoring

- For hazards involving **data defects, publication issues, or time-critical information**:
  - Identify if **ERP** (Emergency Response Procedures) is part of the mitigation strategy.
  - Specify monitoring metrics and triggers that would detect the hazard or its precursors.

---

## 7. Methodological Usage Guidelines

When performing hazard analysis for ATA 02:

1. **Start from context**  
   - Select an operational context (e.g., turnarounds, de-icing, gate operations) and list operations-information–dependent tasks.

2. **Identify hazards**  
   - Ask: “What if the operations information here is wrong, missing, stale, or misleading?”  
   - Capture hazards in the hazard CSV, using a consistent naming and ID scheme.

3. **Classify**  
   - Assign severity based on worst credible effect on safety.  
   - Derive DAL and Initial_Class accordingly.

4. **Define mitigations**  
   - Combine:
     - Design-time controls (data and tool requirements).
     - Process controls (reviews, configuration management).
     - Runtime controls (monitoring, ERP, operator procedures).

5. **Plan and execute verification**  
   - For each mitigation, define **how** it will be verified (test, analysis, inspection, monitoring evidence).  
   - Record verification links.

6. **Assess residual risk**  
   - Update Residual_Class once verification confirms mitigation effectiveness.  
   - If residual risk is not acceptable, iterate.

7. **Maintain traceability**  
   - Ensure IDs and references are updated across:
     - Hazards CSV.
     - Requirements, FTA, FMEA, CCA.
     - V&V and certification documents.

---

## 8. What to do next / how to approach this

1. **Instantiate a canonical hazard table for ATA 02**
   - Create or update `02-00-02-015A_Hazard_Log.csv` using the field semantics in Section 4 and incorporate your existing `H-02-001` entry.

2. **Wire methodology into the safety chain**
   - From:
     - `Certification Safety Objectives — ATA 02`
     - `Fault Tree Analysis — ATA 02`
     - `Common Cause Analysis — ATA 02`
   - Add short references like: “Hazard generation and classification follow [Hazard Analysis Methodology — ATA 02](AMPEL360-02-00-02-007A_Hazard_Analysis_Methodology.md).”

3. **Standardize across programs**
   - Treat this document as **program-agnostic**.  
   - For each program, create a short tailoring note in `../02-00-10_Certification/` that:
     - Confirms severity/DAL mapping.
     - Defines any program-specific risk classification scales or approval thresholds.

4. **Integrate into workflow**
   - In safety/requirements review checklists, add:
     - “Is the hazard recorded in Hazards.csv using the ATA 02 methodology?”
     - “Are FTA/FMEA/CCA and ERP references populated in the hazard’s Notes/Refs?”

5. **Plan enhancements**
   - Later, add:
     - A small script to validate hazard CSV entries (required fields, valid severity/DAL, existing reference IDs).
     - A generated summary (e.g., in `02-90_Tables_Schemas_Diagrams`) that visualizes the hazard portfolio per operational context and per severity.
