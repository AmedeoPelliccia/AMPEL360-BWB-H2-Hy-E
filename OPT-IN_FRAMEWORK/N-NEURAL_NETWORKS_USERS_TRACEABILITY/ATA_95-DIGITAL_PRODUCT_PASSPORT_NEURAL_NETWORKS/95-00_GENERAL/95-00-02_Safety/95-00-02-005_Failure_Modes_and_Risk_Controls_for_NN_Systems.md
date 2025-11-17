# 95-00-02-005 — Failure Modes and Risk Controls for NN Systems

## 1. Purpose

This document catalogues **Neural Network-specific failure modes** and describes
how the **Digital Product Passport (DPP)** captures the associated **risk controls
and mitigations**.

It defines:

- Common failure modes for NN components in safety-critical systems.
- How DPP content describes risk controls, mitigations, and operational constraints.
- The interface between DPP and FMEA/FTA processes.

---

## 2. NN-Specific Failure Modes

Neural networks can fail in ways that differ from traditional software:

### 2.1 Incorrect Output

- **Description:** NN produces an output that is factually wrong or unsafe.
- **Causes:** Training data issues, distribution shift, adversarial inputs, model overfitting.
- **DPP Controls:**
  - ODD definition and input validation.
  - Runtime confidence scoring and threshold checks.
  - Fallback to non-NN baseline when confidence is low.

### 2.2 Performance Degradation

- **Description:** NN accuracy or latency degrades over time.
- **Causes:** Drift in operational environment, sensor aging, software updates.
- **DPP Controls:**
  - Monitoring KPIs for accuracy, precision, recall, latency.
  - Alert triggers when performance falls below thresholds.
  - Scheduled retraining or model refresh procedures.

### 2.3 Out-of-Distribution (OOD) Inputs

- **Description:** NN receives inputs outside its training distribution or ODD.
- **Causes:** Unusual environmental conditions, sensor failures, novel scenarios.
- **DPP Controls:**
  - OOD detection mechanisms (e.g., uncertainty estimation, novelty detection).
  - Documented fallback behaviour when OOD is detected.
  - Links to test evidence for OOD handling.

### 2.4 Adversarial Attack

- **Description:** Malicious or unintentional inputs crafted to fool the NN.
- **Causes:** Cybersecurity threats, sensor spoofing, physical perturbations.
- **DPP Controls:**
  - Input sanitisation and anomaly detection.
  - Adversarial robustness testing results.
  - Cybersecurity measures (access control, integrity checks).

### 2.5 Data Quality Issues

- **Description:** NN receives corrupted, noisy, or incomplete input data.
- **Causes:** Sensor malfunctions, transmission errors, pre-processing failures.
- **DPP Controls:**
  - Data quality checks at runtime (range checks, consistency checks).
  - Documented sensor health monitoring.
  - Fallback to alternative sensors or manual input.

### 2.6 Model Version Mismatch

- **Description:** Wrong model version is deployed or loaded.
- **Causes:** Configuration errors, deployment automation failures.
- **DPP Controls:**
  - Model version verification at deployment (hash checks, digital signatures).
  - Configuration management and traceability in DPP.
  - Continuous integration checks for version consistency.

---

## 3. Risk Controls and Mitigations in DPP

For each identified failure mode, the DPP shall document:

### 3.1 Control Description

- **Type:** Design feature, runtime monitor, procedural control, or administrative measure.
- **Implementation:** How the control is realised (e.g., software module, hardware redundancy, operator checklist).

### 3.2 Verification Evidence

- **Test Results:** Links to test reports demonstrating control effectiveness.
- **Validation Data:** Performance metrics, edge case testing, stress testing.

### 3.3 Residual Risk

- **Likelihood:** After controls are applied, what is the residual likelihood of the failure mode?
- **Severity:** What is the worst-case impact if the control fails?
- **Acceptance Rationale:** Why the residual risk is acceptable (ALARP, regulatory compliance).

---

## 4. Interface with FMEA/FTA

### 4.1 FMEA Integration

- The DPP failure mode catalogue should align with the project-level **Failure Modes and Effects Analysis (FMEA)**.
- Each DPP entry may reference:
  - FMEA ID for the failure mode.
  - Severity, occurrence, and detectability ratings.
  - Recommended actions and closure status.

**Example:**

```yaml
failure_modes:
  - mode_id: FM-NN-001
    description: "False positive in obstacle detection"
    fmea_reference: FMEA-SYS-456
    severity: Major
    occurrence: Remote
    detectability: High
    controls:
      - "Confidence threshold check"
      - "Redundant sensor fusion"
      - "Fallback to manual control"
```

### 4.2 FTA Integration

- **Fault Tree Analysis (FTA)** decomposes system-level hazards into contributing faults.
- DPP entries can be referenced as **basic events** or **intermediate events** in the fault tree.
- This enables quantitative risk assessment if failure rates are available.

---

## 5. Operational Constraints

Some failure modes may be mitigated by **operational constraints** rather than technical controls:

- **Example 1:** NN object detection is only used in daylight conditions (night-time is excluded from ODD).
- **Example 2:** NN-based autopilot is only engaged above 10,000 feet (low-altitude excluded).

These constraints must be:

- Documented in the DPP ODD and limitations sections.
- Enforced by operational procedures (pilot checklists, flight management system logic).
- Monitored and audited to ensure compliance.

---

## 6. Continuous Improvement

The DPP failure mode catalogue is a **living document**:

- New failure modes discovered during testing or operation should be added.
- Effectiveness of controls should be reviewed based on operational data.
- Lessons learned from incidents should inform updates to controls and constraints.

---

## 7. Document Control

- **Status:** `WORKING` / `FOR_REVIEW` / `APPROVED`
- **Owner:** Safety / Systems Engineering Lead
- **Last Updated:** [Date]
- **Notes:**

  - This document was **generated by AI prompted by Amedeo Pelliccia**.
  - Content must be **reviewed and approved** by designated human safety experts.
