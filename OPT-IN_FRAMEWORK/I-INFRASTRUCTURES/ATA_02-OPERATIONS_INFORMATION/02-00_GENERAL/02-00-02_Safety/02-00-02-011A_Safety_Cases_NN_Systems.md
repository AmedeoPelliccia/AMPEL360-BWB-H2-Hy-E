---
Title: "Safety Cases — NN Systems Interplay"
Identifier: "AMPEL360-02-00-02-011A"
Version: "1.0.0"
Status: "Draft"
AccessLevel: "Internal"
Author: "Safety/AI"
CreatedAt: "2025-11-13"
ModifiedAt: "2025-11-13"
Scope: "Safety case patterns for interactions between ATA 02 Operations Information and NN-based systems (e.g., ATA 95) within I-INFRASTRUCTURES"
Abstract: "Defines how to construct safety cases for the interplay between ATA 02 operations information and NN-based systems (e.g., ATA 95), including assumptions, limits, monitoring, and claim–argument–evidence structures."
Keywords: ["ATA 02", "Safety Case", "Neural Networks", "AI", "Operations Information", "ATA 95"]
Compliance:
  - "ATA iSpec 2200"
  - "S1000D"
  - "AMPEL360 Doc Standard v1.1"
  - "Certification Safety Objectives — ATA 02"
Links:
  ParentGeneral: "../"
  SafetyObjectives: "./AMPEL360-02-00-02-001A_Certification_Safety_Objectives.md"
  CCA: "./AMPEL360-02-00-02-002A_Common_Cause_Analysis.md"
  RuntimeMonitoring: "./02-00-02-010A_Runtime_Safety_Monitoring.md"
  HazardMethodology: "./AMPEL360-02-00-02-007A_Hazard_Analysis_Methodology.md"
  FTA: "./AMPEL360-02-00-02-005A_Fault_Tree_Analysis.md"
  ERP: "./AMPEL360-02-00-02-003A_Emergency_Response_Procedures.md"
  Requirements: "../02-00-03_Requirements/"
  VAndV: "../02-00-07_V_AND_V/"
  ATA95_NN: "../../95-00_GENERAL/"   # placeholder, adjust to actual ATA 95 path
ChangeLog:
  - {version: "1.0.0", date: "2025-11-13", author: "Safety/AI", change: "Initial creation"}
---

# Safety Cases — NN Interplay

## 1. Purpose

This document defines how to construct **safety cases** for the interplay between:

- **ATA 02 — Operations Information** (producer/consumer of operational data), and  
- **NN-based systems** (e.g., ATA 95 “Neural Networks / AI”) that **consume, transform, or generate** operations information.

It provides:

- A structured way to define **assumptions, limits, and monitoring** where NN systems rely on ATA 02 content.
- A **claim–argument–evidence** pattern for safety cases covering this interplay.
- Hooks into hazards, runtime monitoring, and requirements.

The intent is to keep ATA 02’s safety case **composable** with ATA 95’s NN-specific safety artefacts.

---

## 2. Scope and Interplay Scenarios

This document applies when:

- ATA 02 operations information is **input** to NN systems (e.g., turnaround prediction, congestion forecasts, slot recommendations).
- NN systems **produce or influence** information that is then:
  - Published under ATA 02, or
  - Used by human operators in conjunction with ATA 02 content.

Typical scenarios include:

- Turnaround time prediction models.
- Airport congestion or delay advisory NNs.
- Gate/stand allocation optimizers.
- Ops recommendation systems mixing NN outputs with rule-based logic.

The safety case must address **both directions**:

1. **ATA 02 → NN**: quality, validity, and applicability of inputs to NN.  
2. **NN → ATA 02 / operators**: correctness, bounds, presentation, and monitoring of NN-influenced outputs.

---

## 3. Assumptions, Limits, and Monitoring

For each NN–ATA 02 interplay scenario, safety cases must explicitly capture:

### 3.1 Assumptions

Document **assumptions** about:

- **Input data** from ATA 02:
  - Ranges, formats, completeness (e.g., “turnaround data has no gaps > X days”, “airport constraints updated ≤ Y hours old”).
  - Pre-processing steps (normalization, aggregation).
  - Applicability tags (e.g., fleet, config, airport).

- **Operational context**:
  - Use cases (turnaround planning, delay forecasting, gate assignment).
  - Expected operator behaviour (decision support vs. fully automated execution).
  - Environmental conditions (traffic levels, typical disruptions).

- **NN system behaviour**:
  - Intended function (classification, prediction, recommendation).
  - Training data coverage vs. intended use domain.
  - Expected performance envelopes.

Assumptions must be **verifiable and monitored** or justified as non-critical.

### 3.2 Limits

Define **limits** on:

- **Use domain**:
  - Airports, fleets, routes, seasons, traffic regimes for which the NN is valid.
  - Data quality thresholds (e.g., minimum data density, completeness).

- **Output usage**:
  - Whether outputs are:
    - Advisory only (operator retains final decision with clear fallback).
    - Used in automated decision-making with defined constraints.
  - Where NN output **must not** be used (e.g., outside trained domain, degraded feeds).

- **Performance and confidence**:
  - Minimum acceptable accuracy/coverage metrics for safety-relevant uses.
  - Confidence thresholds above/below which:
    - Output is suppressed.
    - Additional cross-checks or human review is required.

These limits should map to concrete **requirements** in `../02-00-03_Requirements/` and **monitoring rules** in `02-00-02-010A_Runtime_Safety_Monitoring.md`.

### 3.3 Monitoring

Monitoring must be able to detect when:

- **Assumptions are violated**:
  - Data distributions drift outside training/validation domains.
  - Data freshness or parity assumptions fail.
- **NN behaviour degrades**:
  - Performance drops below thresholds.
  - Output patterns become anomalous (compared to historical or expected behaviour).
- **Safety metrics** are impacted:
  - Increased ERP activations or incidents correlated with NN usage.

Monitoring patterns reuse:

- Data freshness and parity checks (from Runtime Safety Monitoring).
- Anomaly detection (for both data and NN outputs).
- Feedback from ERP activations and incidents.

---

## 4. Safety Case Pattern — Claims, Arguments, Evidence

Use a structured **Claim–Argument–Evidence (CAE)** pattern (or equivalent GSN-style pattern) for NN–ATA 02 interplay.

### 4.1 Top-Level Claim

Example top-level claim:

> **C0:** “The interplay between ATA 02 operations information and NN-based systems used in [context] is acceptably safe for its intended use.”

This is decomposed into subclaims.

### 4.2 Subclaims

Representative subclaims:

- **C1: Input Integrity**  
  “ATA 02 information provided to the NN is sufficiently accurate, complete, timely, and correctly contextualized for the intended NN use.”

- **C2: NN Behaviour within Safe Bounds**  
  “Within its defined domain and limits, the NN behaves predictably, with sufficient performance and explainability for the intended safety role.”

- **C3: Output Use and Human Factors**  
  “NN-influenced outputs are used in a way that supports safe decision-making, accounts for human factors, and prevents over-reliance or misinterpretation.”

- **C4: Monitoring and Adaptation**  
  “Runtime monitoring detects relevant degradations or assumption violations quickly enough, and effective corrective actions (including ERP) are in place.”

Each subclaim should be mapped to **hazards**, **requirements**, and **verification**.

### 4.3 Arguments

Examples of argument structures:

- **A1 (for C1):**  
  - A1a: ATA 02 datasets used as NN inputs are governed by quality, freshness, and configuration requirements.  
  - A1b: Data pre-processing and mapping steps are specified and verified.  
  - A1c: Hazards from incorrect inputs are identified (hazard analysis, CCA) and mitigated.

- **A2 (for C2):**  
  - A2a: NN training/validation data covers the intended domain.  
  - A2b: Performance, robustness, and limitations are characterised and documented.  
  - A2c: Out-of-scope detection and fallback behaviour are defined.

- **A3 (for C3):**  
  - A3a: HF assessments show that how outputs are displayed and used does not overload or mislead operators.  
  - A3b: Procedures specify how to interpret and cross-check NN recommendations.  
  - A3c: Change notices and training cover NN behaviour and caveats.

- **A4 (for C4):**  
  - A4a: Runtime monitoring is in place for inputs, outputs, and NN performance.  
  - A4b: ERP and degraded ops procedures are triggered when issues are detected.  
  - A4c: A feedback loop updates hazards, requirements, and NN configurations.

### 4.4 Evidence Types

Typical **evidence** items:

- Data quality reports and configuration management records for ATA 02 inputs.
- NN design, training, validation, and robustness analysis artefacts (ATA 95).
- Hazard analysis, CCA, FMEA, and FTA entries specific to NN–data interplay.
- HF studies (e.g., workload/SA assessments of NN-assisted workflows).
- Runtime monitoring reports and ERP activation logs.
- Test reports and V&V artefacts stored in `../02-00-07_V_AND_V/`.

Evidence should be **indexed** and referenced via identifying fields in front-matter or safety databases.

---

## 5. Integration with ATA 02 Safety Artefacts

### 5.1 Hazards and Analyses

For NN interplay:

- Add specific hazards in `02-00-02-015A_Hazard_Log.csv` such as:
  - Misleading NN recommendations due to incorrect ATA 02 input data.
  - Unsafe over-reliance on NN outputs in degraded data conditions.
- Map them to:
  - CCA entries (common causes in shared datasets/pipelines).  
  - FTA nodes for NN-related paths to the “Unsafe operations decision” top event.  
  - FMEA rows linking functions, failure modes, and NN causes.

### 5.2 Requirements

Define requirements in `../02-00-03_Requirements/` for:

- Input data quality and labelling for NN consumption.
- Boundaries and disclaimers on NN outputs published under ATA 02.
- Runtime monitoring and ERP triggers specific to NN-related issues.
- HF constraints on how NN outputs are presented and used.

Requirements should reference this document and the corresponding NN/ATA 95 safety artefacts.

### 5.3 Runtime Monitoring and ERP

- Monitoring patterns from `02-00-02-010A_Runtime_Safety_Monitoring.md` must include:
  - Checks for data and concept drift relevant to NN usage.
  - Alerts specific to high-risk NN behaviour (e.g., anomalous recommendations).

- ERP (`AMPEL360-02-00-02-003A_Emergency_Response_Procedures.md`) must cover:
  - Freezing NN-based functions or outputs when safety is in doubt.
  - Reverting to non-NN backups or conservative procedures.

---

## 6. Template for NN–ATA 02 Safety Case Instantiation

For each NN use case, instantiate a concise template:

1. **Use Case ID and Description**  
   - NN function, ATA 02 datasets used, operational context.

2. **Assumptions**  
   - Data, operational, and NN behavioural assumptions.

3. **Limits and Applicability**  
   - Domain of use, performance thresholds, disallowed conditions.

4. **Hazards and Mitigations**  
   - Hazard IDs, mappings to CCA/FMEA/FTA, high-level mitigations.

5. **Monitoring and ERP Linkage**  
   - Monitored signals, thresholds, alert categories, ERP triggers.

6. **Claims, Arguments, Evidence Table**  
   - C1–C4 mapping to specific evidence artefacts.

7. **Change Management**  
   - How changes to data, NN models, or procedures update this safety case.

This template can live as a separate artefact in `../02-00-10_Certification/` or under ATA 95, with this document as the governance pattern.

---

## 7. Usage Guidelines

When introducing or modifying NN systems that interact with ATA 02:

1. **Identify interplay zones**  
   - List which ATA 02 datasets the NN consumes and which ATA 02 outputs are influenced.

2. **Apply this safety case pattern**  
   - Instantiate the use case template.
   - Populate assumptions, limits, monitoring, and CAE structure.

3. **Align with existing safety artefacts**  
   - Ensure hazards, CCA, FTA, FMEA, ERP, HF, and runtime monitoring are updated accordingly.

4. **Maintain traceability**  
   - Use consistent IDs across ATA 02 and ATA 95 artefacts.
   - Link to V&V evidence and certification records.

---

## What to do next / how to approach this

1. **Create a small NN–ATA 02 use case template**  
   - Add a short markdown or table (either in this file or under `../02-00-10_Certification/`) that teams can copy for each NN use case (e.g., “NN Turnaround Predictor”).

2. **Wire into ATA 95**  
   - From ATA 95 general/safety docs, reference this file as the **ATA 02 side** of the joint safety case, and define how NN-specific evidence is linked.

3. **Add requirements cluster**  
   - Introduce a “NN Interplay — ATA 02” requirement subset in `../02-00-03_Requirements/` with IDs that can be referenced from this safety case.

4. **Optimize workflow**  
   - In any NN-related change process, add checklist items:
     - “NN–ATA 02 safety case updated?”  
     - “Assumptions/limits reflected in monitoring and ERP?”  
     - “HF and training implications reviewed?”

5. **Plan for automation**  
   - Longer-term, consider a small script or model-based safety-case tool to:
     - Generate CAE/GSN fragments from structured hazard/requirement/monitoring data.
     - Keep the NN–ATA 02 safety case in sync with evolving artefacts.
