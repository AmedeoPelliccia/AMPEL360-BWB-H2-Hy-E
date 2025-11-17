# 95-00-02-007 — Safety Incidents, Learning, and DPP Updates

## 1. Purpose

This document defines how **safety incidents and occurrences** involving Neural Network
components are captured, investigated, and used to update the **Digital Product
Passport (DPP)**.

It specifies:

- Incident reporting and investigation procedures for NN-related events.
- How lessons learned feed back into DPP records (new warnings, constraints, status changes).
- The process for deciding when DPP updates require re-approval or re-certification.

---

## 2. Incident Types and Definitions

### 2.1 Safety Incident

- An event where the NN component contributed to an unsafe condition or outcome.
- Examples:
  - NN misclassification led to incorrect system response.
  - NN failed to detect a hazard, resulting in a near-miss.
  - NN exhibited unexpected behaviour outside its ODD.

### 2.2 Near-Miss / Occurrence

- An event where the NN component performed unexpectedly, but safety margins or redundancies prevented an adverse outcome.
- Examples:
  - NN confidence dropped unexpectedly, but fallback activated successfully.
  - OOD input detected and handled, but revealed a gap in ODD definition.

### 2.3 Performance Anomaly

- A deviation from expected NN behaviour that does not immediately threaten safety but warrants investigation.
- Examples:
  - Gradual accuracy degradation over time.
  - Increased false positive/negative rate in specific conditions.

---

## 3. Incident Reporting and Investigation

### 3.1 Reporting Requirements

Any safety incident, near-miss, or significant performance anomaly involving an NN component
must be reported to:

- Project safety manager.
- Airworthiness authority (if applicable under regulatory reporting rules).
- NN DPP custodian (for DPP update consideration).

**Report contents:**

- Incident ID and date.
- Description of the event and context (flight phase, environmental conditions, etc.).
- NN component(s) involved (DPP ID, version).
- Contributing factors (data quality, OOD input, model limitation, etc.).
- Immediate actions taken (fallback, manual override, system shutdown).

### 3.2 Root Cause Analysis

A structured investigation shall be conducted to determine:

- **Primary cause:** What NN behaviour or failure led to the event?
- **Contributing factors:** Were there environmental, operational, or human factors?
- **Detection gaps:** Why was the issue not detected earlier (by testing or monitoring)?
- **Control effectiveness:** Did existing risk controls function as intended?

Tools: 5 Whys, Fishbone Diagrams, FMEA review, Fault Tree Analysis.

### 3.3 Corrective and Preventive Actions (CAPA)

Based on the investigation, determine:

- **Immediate corrective actions:** Fix the specific issue (e.g., retrain model, adjust threshold).
- **Preventive actions:** Prevent recurrence (e.g., enhance monitoring, refine ODD, improve testing).
- **Systemic improvements:** Apply lessons across similar NN components or projects.

---

## 4. DPP Update Triggers

Incident investigation outcomes may require DPP updates:

| Investigation Finding                    | DPP Update Action                                          |
|------------------------------------------|------------------------------------------------------------|
| New failure mode identified              | Add to failure mode catalogue (95-00-02-005)              |
| ODD gap discovered                       | Refine ODD definition, add exclusion or constraint        |
| Monitoring threshold insufficient        | Update alert thresholds (95-00-02-006)                    |
| Model requires retraining                | Update version, revalidate, update status to "IN_REVIEW"  |
| Risk level re-assessed                   | Update hazard links, risk controls, residual risk         |
| Component decommissioned / retired       | Update status to "RETIRED", add retirement rationale      |

---

## 5. DPP Status Lifecycle

The DPP status field reflects the safety and operational state of the NN component:

| Status              | Meaning                                                                 |
|---------------------|-------------------------------------------------------------------------|
| **DEVELOPMENT**     | Component is under development, not yet validated for deployment       |
| **VALIDATED**       | Component has passed V&V, ready for deployment                         |
| **IN_SERVICE**      | Component is deployed and operational                                  |
| **RESTRICTED**      | Component has known limitations, restricted to specific conditions     |
| **UNDER_REVIEW**    | Component is under investigation due to incident or performance issue  |
| **SUSPENDED**       | Component is temporarily grounded pending investigation or fix         |
| **RETIRED**         | Component is permanently decommissioned, no longer in service          |

Incident investigation may trigger status changes (e.g., IN_SERVICE → UNDER_REVIEW → RESTRICTED or RETIRED).

---

## 6. Change Control and Re-Approval

### 6.1 Minor Updates

Minor DPP updates (e.g., correcting typos, adding clarifying notes) do not require re-approval.

### 6.2 Significant Updates

Significant updates (e.g., new failure mode, ODD change, model retraining) require:

- **Safety review:** Assess impact on safety case and risk assessment.
- **Approval:** Safety manager or designated authority must approve the DPP change.
- **Notification:** Inform relevant stakeholders (operations, certification, training).

### 6.3 Re-Certification

If the NN component's role or criticality changes, or if major safety updates are made, re-certification may be required:

- Consult with airworthiness authority.
- Update certification artefacts (safety case, compliance matrices).
- Conduct additional V&V if necessary.

---

## 7. Learning Across the Fleet / Portfolio

Lessons learned from incidents should be disseminated:

- **Within the project:** Update all similar NN components with relevant learnings.
- **Across the organisation:** Share anonymised incident reports and best practices.
- **With the community:** Contribute to industry safety databases (e.g., ASRS, ECCAIRS) where appropriate.

---

## 8. Example: Incident-to-DPP Workflow

1. **Incident occurs:** NN object detection fails to identify obstacle, near-miss reported.
2. **Investigation:** Root cause is OOD lighting condition (sunset glare) not covered in training data.
3. **CAPA:**
   - Immediate: Add sunset exclusion to ODD.
   - Preventive: Collect sunset data, retrain model, revalidate.
   - Systemic: Review all vision-based NNs for similar ODD gaps.
4. **DPP Updates:**
   - Update ODD section with sunset exclusion.
   - Change status to RESTRICTED until retrained model is validated.
   - Add incident reference and lessons learned to DPP notes.
5. **Re-Approval:**
   - Safety manager reviews and approves updated DPP.
   - Once new model is validated, status changes to IN_SERVICE.

---

## 9. Document Control

- **Status:** `WORKING` / `FOR_REVIEW` / `APPROVED`
- **Owner:** Safety / Quality Lead
- **Last Updated:** [Date]
- **Notes:**

  - This document was **generated by AI prompted by Amedeo Pelliccia**.
  - Content must be **reviewed and approved** by designated human safety experts.
