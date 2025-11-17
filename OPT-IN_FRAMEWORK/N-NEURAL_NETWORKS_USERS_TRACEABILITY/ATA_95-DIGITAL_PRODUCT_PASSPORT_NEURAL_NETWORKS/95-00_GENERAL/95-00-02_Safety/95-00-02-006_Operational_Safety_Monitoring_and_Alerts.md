# 95-00-02-006 — Operational Safety Monitoring and Alerts

## 1. Purpose

This document defines the **operational safety monitoring requirements** for
Neural Network components and how these are reflected in the **Digital Product
Passport (DPP)**.

It specifies:

- Safety-relevant KPIs, metrics, and thresholds that must be monitored during operation.
- Alerting mechanisms and escalation procedures.
- How monitoring data is logged, analysed, and fed back into DPP updates.

---

## 2. Why Operational Monitoring is Critical for NN Safety

Unlike traditional software, NN systems can:

- **Degrade silently** due to distribution shift, sensor drift, or data quality issues.
- **Exhibit emergent behaviour** in novel scenarios not covered by testing.
- **Accumulate risk** over time as operational conditions diverge from training assumptions.

Therefore, **continuous monitoring** is essential to detect anomalies early and trigger
corrective actions before safety is compromised.

---

## 3. Safety-Relevant KPIs and Metrics

The DPP shall document the following monitoring requirements:

### 3.1 Performance Metrics

- **Accuracy / Precision / Recall:** For classification or detection tasks.
- **Latency / Response Time:** To ensure timely decision-making.
- **Confidence Scores:** Distribution of model confidence over time.

**Thresholds:**

- **Warning:** Performance drops below 90% of baseline.
- **Alert:** Performance drops below 80% of baseline → require immediate review.

### 3.2 Input Quality Metrics

- **Out-of-Distribution (OOD) Detection Rate:** Frequency of OOD inputs.
- **Data Quality Indicators:** Missing data, noise levels, sensor health.
- **Input Range Violations:** Inputs outside expected bounds.

**Thresholds:**

- **Warning:** OOD rate exceeds 5% of inputs.
- **Alert:** OOD rate exceeds 10% → consider retraining or ODD refinement.

### 3.3 System Health Metrics

- **Model Version Mismatches:** Detected inconsistencies between deployed and expected model.
- **Hardware Health:** GPU/TPU utilisation, memory usage, temperature.
- **Software Errors:** Exception rates, crashes, timeout events.

**Thresholds:**

- **Alert:** Any critical hardware or software failure → immediate fallback to safe mode.

### 3.4 Operational Context Metrics

- **ODD Violations:** Instances where the system is used outside its validated operating envelope.
- **Human Override Rate:** Frequency of manual intervention or pilot override.
- **Fallback Activations:** How often the system reverts to baseline or manual control.

**Thresholds:**

- **Warning:** Override rate exceeds expected baseline.
- **Alert:** Fallback activations indicate systemic issue → require root cause analysis.

---

## 4. Alerting Mechanisms

### 4.1 Alert Levels

| Level       | Description                                      | Action                                      |
|-------------|--------------------------------------------------|---------------------------------------------|
| **INFO**    | Routine logging, no immediate action required   | Log for trend analysis                      |
| **WARNING** | Minor deviation, monitor closely                | Notify operations team, schedule review     |
| **ALERT**   | Significant deviation, immediate action needed  | Notify safety manager, consider fallback    |
| **CRITICAL**| Safety-critical failure, immediate intervention | Engage fail-safe mode, ground/maintenance   |

### 4.2 Alert Triggers

Alerts are triggered when:

- A monitored metric exceeds its threshold.
- A critical error or exception occurs.
- OOD or adversarial input is detected.
- Model version mismatch or integrity violation is detected.

### 4.3 Escalation Procedures

- **Tier 1:** Automated system response (fallback, safe mode).
- **Tier 2:** Operations team notification (review logs, assess risk).
- **Tier 3:** Safety manager / airworthiness authority notification (incident investigation, potential grounding).

---

## 5. Data Logging and Audit Trails

### 5.1 What to Log

All safety-relevant events and metrics must be logged, including:

- Model inputs and outputs (or representative samples).
- Confidence scores and uncertainty estimates.
- Alert triggers and system responses.
- Human overrides and manual interventions.
- Environmental and operational context (flight phase, weather, sensor status).

### 5.2 Log Retention

- **Flight-critical logs:** Retain for the operational lifetime of the aircraft plus regulatory retention period.
- **Aggregate statistics:** Retain indefinitely for trend analysis and continuous improvement.

### 5.3 Audit and Compliance

Logs must be:

- **Tamper-evident:** Protected against unauthorised modification.
- **Accessible:** Available for investigation, certification audit, and regulatory inspection.
- **Analysable:** In a structured format (e.g., JSON, Parquet) suitable for automated analysis.

---

## 6. Feedback Loop to DPP

Operational monitoring data informs DPP updates:

| Observation                              | DPP Update Action                                          |
|------------------------------------------|------------------------------------------------------------|
| Performance degradation detected         | Update status field, add warning, schedule retraining     |
| New failure mode observed                | Add to failure mode catalogue, update risk controls       |
| ODD violation detected repeatedly        | Refine ODD definition, add exclusion or constraint        |
| Successful fallback operation validated  | Confirm fallback control effectiveness in DPP evidence    |
| Incident or near-miss reported           | Link incident report to DPP, update lessons learned       |

---

## 7. Integration with ATA 98 (Runtime Monitoring)

- **ATA 98** covers the technical implementation of runtime monitoring for NN systems.
- **This section (95-00-02-006)** defines the **safety requirements** that ATA 98 implementations must meet.
- Cross-reference between the two ensures consistency:
  - ATA 98 provides the "how" (monitoring architecture, data pipelines, dashboards).
  - 95-00-02-006 provides the "what" and "why" (safety KPIs, thresholds, alert logic).

---

## 8. Document Control

- **Status:** `WORKING` / `FOR_REVIEW` / `APPROVED`
- **Owner:** Safety / Operations Lead
- **Last Updated:** [Date]
- **Notes:**

  - This document was **generated by AI prompted by Amedeo Pelliccia**.
  - Content must be **reviewed and approved** by designated human safety experts.
