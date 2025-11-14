---
Title: "Fault Tree Analysis — ATA 02"
Identifier: "AMPEL360-02-00-02-005A"
Version: "1.0.0"
Status: "Draft"
AccessLevel: "Internal"
Author: "Safety"
CreatedAt: "2025-11-13"
ModifiedAt: "2025-11-13"
Scope: "Fault Tree Analysis for safety-relevant ATA 02 Operations Information within I-INFRASTRUCTURES"
Abstract: "Defines the top event, structure, and key branches of the Fault Tree Analysis (FTA) for unsafe operations decisions caused by incorrect ATA 02 operations information, and links to quantitative data and V&V evidence."
Keywords: ["ATA 02", "Fault Tree Analysis", "FTA", "Safety", "Operations Information"]
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
  FMEA: "./"  # to be replaced with concrete FMEA reference when available
  VAndVData: "../02-00-07_V_AND_V/"
  Requirements: "../02-00-03_Requirements/"
  Certification: "../02-00-10_Certification/"
ChangeLog:
  - {version: "1.0.0", date: "2025-11-13", author: "Safety", change: "Initial creation"}
---

# Fault Tree Analysis (FTA) — ATA 02

## 1. Purpose

This document defines the **Fault Tree Analysis (FTA)** structure for **ATA 02 — Operations Information**, focusing on unsafe operational decisions resulting from incorrect or misleading operations information.

It provides:

- A clearly defined **Top Event**.
- Main logical branches and **intermediate events** (Level 1 / Level 2).
- Interfaces to **Common Cause Analysis (CCA)**, **FMEA**, **V&V**, and **Emergency Response Procedures (ERP)**.
- A place-holder for **quantitative analysis** (minimal cut sets, probabilities) maintained alongside V&V data.

This FTA supports the **Certification Safety Objectives — ATA 02**, particularly those related to integrity, timeliness, and control of operations information.

**Hazard generation and classification** follow [Hazard Analysis Methodology — ATA 02](./AMPEL360-02-00-02-007A_Hazard_Analysis_Methodology.md).

---

## 2. Top Event

**Top Event:**  
> **Unsafe operations decision due to incorrect operations information.**

This top event covers:

- Decisions by flight crew, dispatch, ground operations, or maintenance being **unsafe or outside approved limits** because the information they relied on was:
  - Incorrect.
  - Incomplete.
  - Outdated.
  - Misleading (e.g., ambiguous or incorrectly contextualized).

The FTA focuses on the **information chain** (generation → validation → publication → use) rather than underlying system hardware failures, which are addressed in owning technical ATAs.

---

## 3. Level 1 Structure

At **Level 1**, the Top Event is typically decomposed as:

> **Top Event** = (Incorrect / Misleading Ops Data Available) **AND** (Safety Barriers Ineffective)

Expressed informally:

1. **Event A:** Incorrect or misleading operations information is made available to operators.  
2. **Event B:** Safety barriers (review, validation, monitoring, ERP) fail to prevent its use in a safety-significant decision.

The Top Event occurs when **both** conditions are true at the same time.

### 3.1 Level 1 – Event A: Incorrect / Misleading Ops Data Available

Representative contributors:

- A1: Incorrect or inconsistent data in the **source dataset** (e.g., turnaround times, constraints, limits).
- A2: Stale or **out-of-date data** relative to airport/infra or weather/NOTAM reality.
- A3: **Misapplied configuration / applicability** (e.g., wrong aircraft type, config, or airport).
- A4: **Presentation-induced misinterpretation** (e.g., ambiguous structure, missing cautions/warnings).

### 3.2 Level 1 – Event B: Safety Barriers Ineffective

Representative contributors:

- B1: **Authoring and review barriers ineffective**:
  - Safety/technical reviews incomplete, rushed, or bypassed.
- B2: **Validation & V&V barriers ineffective**:
  - Scenario-based validation, HF checks, or tool validation not performed or not covering the defect.
- B3: **Runtime monitoring and ERP ineffective**:
  - Monitoring not detecting anomalies; ERP not activated or not executed properly.
- B4: **Operator-side defenses ineffective**:
  - Operator procedures for cross-checking information not followed or inadequate.

---

## 4. Level 2 Root Cause Structure

At **Level 2**, Level 1 events are decomposed into more granular root causes aligned with your existing safety artefacts (CCA, FMEA, ERP).

### 4.1 Level 2 for Event A – Incorrect / Misleading Ops Data

Examples (map these to FMEA rows and CCA categories):

- **A1.1 – Ingestion errors**
  - ETL or data ingestion pipeline failures (e.g., partial updates, incorrect joins).
  - Unit or scaling errors during transformation (e.g., time units, distances).

- **A1.2 – Airport feed mismatch**
  - Mismatch between:
    - Airport AODB/NOTAM data and ATA 02 datasets.
  - Misconfigured or missing mapping between feed fields and internal schema.

- **A1.3 – Manual entry mistakes**
  - Human data entry errors in:
    - Turnaround parameters, limits, procedures, applicability tags.
  - Misinterpretation of source documents when transcribing or updating.

- **A1.4 – Tool failures / configuration errors**
  - Authoring or transformation tools:
    - Incorrect template logic (missing warnings, incorrect applicability).
    - Bugs in export scripts or layout engines.
  - Misconfigured applicability filters or rule sets.

- **A2.1 – Stale data ingestion**
  - Scheduled jobs disabled or failing silently.
  - Latest airport/infra updates not incorporated into ops datasets.

- **A3.1 – Applicability/tagging errors**
  - Wrong configuration codes or airport tags applied.
  - Failure to retire or re-tag information when configuration changes.

- **A4.1 – Ambiguous or incomplete presentation**
  - Missing preconditions or steps.
  - Confusing layout or overlapping constraints that invite misinterpretation.

These Level 2 events should be cross-linked to:

- CCA entries (physical, functional, latent CCCs).
- FMEA rows (Function/Item, Failure Mode, Cause, Effects).

### 4.2 Level 2 for Event B – Safety Barriers Ineffective

Examples:

- **B1.1 – Review process gaps**
  - Safety/technical review not performed or performed by unqualified personnel.
  - Workload or schedule pressure leading to truncated reviews.

- **B1.2 – Inadequate review criteria**
  - Checklists not covering new data types / new tools.
  - No explicit checks for common CCA-derived conditions.

- **B2.1 – Incomplete validation coverage**
  - V&V scenarios not covering specific combinations (airport, weather, configuration).
  - Insufficient HF assessment of information layout and usability.

- **B2.2 – Tool validation deficiencies**
  - Authoring/publication tools not validated for their critical uses.
  - Changes in tools without regression validation.

- **B3.1 – Monitoring blind spots**
  - Monitoring not tracking:
    - Data freshness.
    - Consistency across channels (EFB vs. portal vs. printed).
  - Alerts not configured or thresholds set inappropriately.

- **B3.2 – ERP not triggered or ineffective**
  - Issues detected but not escalated to ERP.
  - ERP execution incomplete (e.g., bulletins not sent to all affected operators).

- **B4.1 – Operator procedure gaps**
  - Lack of cross-checks (e.g., against NOTAMs, local procedures).
  - Training gaps in recognizing suspect information.

---

## 5. Quantification and Minimal Cut Sets

### 5.1 Quantitative Inputs

Quantitative analysis (probabilities, cut set frequencies) is maintained under:

- `../02-00-07_V_AND_V/` — **V&V and quantitative safety analysis data**.

Inputs include:

- Failure and error rates from FMEA and reliability data.
- Monitoring statistics (e.g., rate of stale data detection).
- Incident and feedback data from runtime monitoring and ERP activations.

### 5.2 Minimal Cut Sets

Based on the tree structure, **minimal cut sets** for the Top Event typically combine:

- An information failure (e.g., **A1.x**, **A2.x**, **A3.x**, **A4.x**).
- A barrier failure (e.g., **B1.x**, **B2.x**, **B3.x**, **B4.x**).

Example qualitative minimal cut sets (to be quantified program-by-program):

- {A1.1 ingestion error, B1.1 review process gap}  
- {A2.1 stale data ingestion, B3.1 monitoring blind spot}  
- {A3.1 applicability error, B2.1 incomplete validation coverage}  

Formal minimal cut set calculations and numeric results shall be stored in the V&V repository and referenced from here.

> **Note:** This document defines the logical structure and naming. Numerical values, cut set rankings, and sensitivity analyses reside in `../02-00-07_V_AND_V/` and certification artefacts under `../02-00-10_Certification/`.

---

## 6. Interfaces with Other Safety Artefacts

### 6.1 Certification Safety Objectives

This FTA supports and should be consistent with:

- `AMPEL360-02-00-02-001A_Certification_Safety_Objectives.md`

Each major branch should trace back to one or more safety objectives (e.g., integrity, timeliness, change control of ops information).

### 6.2 Common Cause Analysis (CCA)

- CCA (`AMPEL360-02-00-02-002A_Common_Cause_Analysis.md`) provides **common cause events** that:
  - Should be explicitly represented as **common cause nodes** in the FTA (e.g., shared data source failure, template defect, publication pipeline failure).
- Ensure that:
  - Level 2 causes referencing shared infrastructure/processes are aligned with CCA categories.

### 6.3 FMEA

- FMEA rows (e.g., `AMPEL360-02-00-02_FMEA_Ops_Datasets.csv`) should:
  - Map `Failure_Mode` and `NN/IT_Cause` to Level 2 events.
  - Provide failure rates or qualitative ratings used in FTA quantification.

### 6.4 ERP and Runtime Monitoring

- ERP (`AMPEL360-02-00-02-003A_Emergency_Response_Procedures.md`) and runtime monitoring define:
  - **Mitigation events** that can be modeled as **barrier successes/failures** in the FTA.
  - Detection and response paths for certain cut sets.

---

## 7. Traceability and Maintenance

- Each **Level 1 and Level 2 event** should have:
  - A unique identifier (e.g., `FTA-02-A1.1`) referenced in:
    - FMEA tables.
    - CCA entries.
    - Requirements and monitoring design.
- Requirements implementing mitigations should be captured in:
  - `../02-00-03_Requirements/` with back-references to this FTA.

When:

- New failure modes or CCCs are identified (via FMEA, incidents, or ERP),
- Or new barriers/mitigations are introduced,

then:

1. Update this FTA structure (add/update nodes).  
2. Update mapping and references in:
   - CCA.
   - FMEA.
   - Requirements.
   - V&V quantitative data.

---

## 8. Usage Guidelines

When conducting safety work on ATA 02:

1. **Use this FTA as the central logical model** for:
   - How incorrect ops information can lead to unsafe decisions.
   - How barriers interact to prevent or fail to prevent the Top Event.

2. **Align other artefacts with the FTA**:
   - Ensure that each new FMEA row, CCA entry, or requirement can be mapped to one or more FTA events.

3. **Drive quantitative updates from V&V**:
   - When new data is available (e.g., monitoring statistics, incident rates), update:
     - The quantitative analysis in `../02-00-07_V_AND_V/`.
     - Cut set rankings and DAL justifications in certification artefacts.

4. **Feed back from ERP and incidents**:
   - After ERP activations or incidents involving ATA 02:
     - Review whether the FTA structure needs updating.
     - Add new events or adjust probabilities as learning emerges.

---
