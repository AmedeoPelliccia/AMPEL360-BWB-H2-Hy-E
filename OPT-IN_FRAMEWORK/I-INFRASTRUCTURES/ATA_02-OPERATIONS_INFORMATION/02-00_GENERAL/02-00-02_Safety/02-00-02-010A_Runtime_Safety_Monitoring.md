---
Title: "Runtime Safety Monitoring — ATA 02"
Identifier: "AMPEL360-02-00-02-010A"
Version: "1.0.0"
Status: "Draft"
AccessLevel: "Internal"
Author: "Ops/Safety"
CreatedAt: "2025-11-13"
ModifiedAt: "2025-11-13"
Scope: "Runtime monitoring of safety-relevant ATA 02 Operations Information within I-INFRASTRUCTURES"
Abstract: "Defines runtime safety monitoring concepts, KPIs, and independence requirements for ATA 02 operations information, including data freshness checks, airport feed parity checks, anomaly detection, and linkage to ERP."
Keywords: ["ATA 02", "Runtime Monitoring", "Safety", "Operations Information", "KPIs"]
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
  Hazards: "./02-00-02-015A_Hazard_Log.csv"
  Requirements: "../02-00-03_Requirements/"
  VAndV: "../02-00-07_V_AND_V/"
  OperationalSafetyProcedures: "./02-00-02-009A_Operational_Safety_Procedures.md"
ChangeLog:
  - {version: "1.0.0", date: "2025-11-13", author: "Ops/Safety", change: "Initial creation"}
---

# Runtime Safety Monitoring — ATA 02

## 1. Purpose

This document defines **runtime safety monitoring** for **ATA 02 — Operations Information**, with emphasis on:

- Monitoring the **integrity, freshness, and consistency** of safety-relevant operations information.
- Detecting **anomalies** and **common cause conditions** while in operation.
- Providing **quantitative KPIs** and **independence requirements** for monitoring functions.
- Defining how monitoring interacts with **Emergency Response Procedures (ERP)** and **Operational Safety Procedures**.

Runtime monitoring operationalizes elements identified in the **CCA**, **FMEA**, and **FTA** and provides early detection to support safe operations.

---

## 2. Monitoring Scope and Principles

Runtime monitoring covers:

- **Data quality**
  - Freshness vs. source systems and expected refresh cadence.
  - Parity with airport and infrastructure feeds.
  - Internal consistency of datasets and parameters.

- **Publication and distribution health**
  - Correct versions and applicability on all publication channels (EFB, portal, printed, APIs).

- **Usage patterns**
  - Signals that information is being misused, misunderstood, or frequently overridden.

Principles:

- Monitoring must **not rely solely on the same mechanisms** that can fail (independence).
- Monitoring should be **as automated as practical**, with clearly defined escalation.
- Monitoring outputs must be **actionable**, feeding directly into ERP and degraded operations procedures.

---

## 3. Monitoring Functions

### 3.1 Data Freshness Monitors

Monitor whether critical datasets are **up to date** relative to their authoritative sources and expected refresh rates.

Typical use:

- Turnaround and constraint datasets vs.:
  - Airport AODB.
  - NOTAM/regulatory sources.
  - Internal configuration/performance databases.

Checks:

- **Age checks**
  - Compare dataset last-update timestamps against:
    - Expected update frequency (e.g., daily/weekly).
    - Maximum allowed age for safety-relevant content.

- **Change propagation**
  - Detect cases where:
    - Source data has changed.
    - Downstream ATA 02 datasets have not updated within an acceptable latency.

Alerts:

- **Warning**: dataset approaching freshness limit.
- **Alarm**: freshness limit exceeded for safety-relevant content  
  → potential ERP trigger.

### 3.2 Airport Feed Parity Checks

Ensure **parity between ATA 02 datasets and airport/infrastructure feeds**, for example:

- Stand/runway availability.
- Taxiway closures and restrictions.
- Turnaround resource constraints (equipment, services).

Parity checks:

- Compare safety-relevant fields between:
  - ATA 02 datasets, and
  - Airport/infra feeds (AODB, NOTAMs, local airport ops systems).

- Distinguish:
  - **Acceptable lag** (within known propagation delay), vs.
  - **Persistent mismatch** (CCA-relevant issue).

Alerts:

- Generate parity alarms when mismatches:
  - Persist beyond allowed delay, or
  - Exceed a defined scope (e.g., multiple stands/periods).

### 3.3 Anomaly Detection

Identify **abnormal patterns** that may indicate underlying data or process issues:

- **Statistical anomalies**
  - Turnaround times significantly outside historical distributions.
  - Sudden shifts in operational constraints without corresponding operational or regulatory changes.

- **Usage anomalies**
  - Frequent manual overrides of particular data or procedures.
  - Repeated operator feedback about the same dataset/airport/configuration.

- **Operational anomalies**
  - Clustering of incidents, near-misses, or ERP activations around particular datasets or airports.

Approach:

- Start with **rule-based** detection aligned with known hazards and CCA conditions.
- Optionally evolve to more advanced analytics/ML, with:
  - Clear thresholds.
  - Justified features.
  - Explainable outputs.

---

## 4. Key Performance Indicators (KPIs)

Monitoring performance must be measured using defined KPIs.

### 4.1 Detection Rate

- **Definition**: proportion of safety-relevant data defects (within monitoring scope) that monitoring detects before unsafe operational use.
- **Target**: detection rate **> 99%** for defined safety-relevant defect types (to be refined per program).

Measurement:

- Seeded test cases (simulated defects) in V&V activities.
- Retrospective analysis of real incidents and discovered defects.

Evidence is captured under `../02-00-07_V_AND_V/`.

### 4.2 False Alarm Rate

- **Definition**: number of false safety-relevant alarms per unit of exposure (e.g. **per flight hour** or per **turnaround**).
- **Target**: false alarm rate **< 0.01/FH** (or equivalent metric, tailored per program).

Objectives:

- Maintain operator trust in alerts.
- Avoid desensitization while still detecting real events.

### 4.3 Detection Latency

- **Definition**: time between the occurrence of a safety-relevant defect and its detection by monitoring.
- **Goal**: detection latency should be short enough to enable **ERP activation** and operational response before significant exposure.

Latency thresholds must be:

- Defined per monitored defect class (e.g., minutes/hours).
- Justified and recorded in V&V artefacts.

---

## 5. Independence Requirements

To reduce **common cause failures** between the publication system and monitoring:

### 5.1 Logical and Data Independence

Monitoring should:

- Use **independent data access paths** or validated replicas where feasible.
- Implement **independent computations/checks**, not just reuse the same transformation logic prone to failure.

Minimum expectations:

- Monitoring must be able to detect:
  - Missing or incomplete updates.
  - Inconsistent outputs across publication channels.

### 5.2 Tool and Configuration Independence

Where practical:

- Use separate or independently validated tooling for monitoring.
- Avoid a single configuration repository being a common point of failure.

If reuse of tools is unavoidable:

- Add **compensating controls**:
  - Cross-validation rules.
  - Sanity checks.
  - External reference comparisons.

### 5.3 Organizational Independence

- Roles defining and approving safety-relevant monitoring logic must be captured in `../02-00-01-004A_Roles_Responsibilities.md`.
- Changes to monitoring rules for safety-relevant functions require:
  - At least one **independent reviewer** (e.g., Safety Engineer (Ops)).
  - Traceable approval records.

Independence rationale and evidence are captured in `../02-00-10_Certification/`.

---

## 6. Integration with ERP and Operational Procedures

### 6.1 Alert Categories and ERP

Monitoring alerts should be classified, for example:

- **Informational**
  - No immediate operational action.
  - Used for trend monitoring and tuning.

- **Warning**
  - Operator or safety attention required.
  - Investigation and potential adjustment of plans.

- **Alarm (Safety-Relevant)**
  - Immediate containment/mitigation required.
  - May **trigger ERP**:
    - Freeze publication.
    - Revert datasets.
    - Issue bulletins.

For each category:

- Define:
  - Criteria and thresholds.
  - Immediate procedural responses.
  - Responsible roles and channels for notifications.

### 6.2 Link to ERP and Degraded Ops

- ERP behaviour and communications are defined in:  
  `AMPEL360-02-00-02-003A_Emergency_Response_Procedures.md`.

- Degraded operations procedures and escalation are defined in:  
  `02-00-02-009A_Operational_Safety_Procedures.md`.

Monitoring outputs must:

- Use those procedures as the **default response** path for safety-relevant alarms.
- Feed back into hazard, CCA, FTA, and requirements when new patterns emerge.

---

## 7. Requirements and Verification Hooks

### 7.1 Requirements

Key monitoring expectations should be captured as requirements under `../02-00-03_Requirements/`, for example:

- Runtime monitoring for safety-relevant ATA 02 datasets shall:
  - Implement automated **freshness checks** with defined thresholds and alerts.
  - Implement **parity checks** with airport/infrastructure feeds for safety-critical parameters.
  - Achieve program-defined targets for detection rate, false alarm rate, and detection latency.
  - Meet defined **independence** criteria from the publication pipeline.

### 7.2 Verification

Verification activities include:

- **Test campaigns**
  - Inject synthetic defects into datasets and feeds.
  - Confirm:
    - Detection.
    - Alert classification.
    - Triggering of ERP and degraded ops procedures.
    - Measured detection rate, latency, and false alarms.

- **Process/tool reviews**
  - Review monitoring rule sets and independence arguments.
  - Confirm correctness and appropriateness of thresholds.

- **Operational evidence**
  - Analyse:
    - Actual monitoring alerts.
    - ERP activations.
    - Incident investigations.

Results are stored under `../02-00-07_V_AND_V/` and, where certification-relevant, `../02-00-10_Certification/`.

---

## 8. Roles & Responsibilities

Responsibilities align with `../02-00-01-004A_Roles_Responsibilities.md`, typically:

- **Ops Information Lead**
  - Ensures monitoring coverage is adequate for operational needs.

- **Safety Engineer (Ops)**
  - Defines monitoring scope for safety.
  - Interprets monitoring results with respect to safety objectives.

- **Tooling / IT Owners**
  - Implement monitoring mechanisms.
  - Maintain reliability and independence.

- **Airport/Infra Liaison**
  - Coordinates handling of parity issues with external providers.

- **HF Lead**
  - Ensures alerts and dashboards are usable and do not overload users.

---

## 9. Usage Guidelines

When designing or operating runtime monitoring for ATA 02:

1. **Start from hazards and CCA**
   - Map which hazards and common cause conditions are addressed by monitoring.

2. **Define KPIs and thresholds**
   - Set initial numeric targets for detection, latency, and false alarm rates.
   - Tailor them per program.

3. **Design for independence**
   - Avoid single points of failure shared with the publication pipeline.
   - Document independence measures and residual risks.

4. **Tie alerts to ERP and degraded operations**
   - For each monitored condition, define:
     - Alert category.
     - Immediate response.
     - ERP/degraded ops triggers.

5. **Continuously refine**
   - Use monitoring data, incidents, and ERP outcomes:
     - To tune thresholds.
     - To add/remove monitored conditions.
     - To update safety artefacts and requirements.

---
