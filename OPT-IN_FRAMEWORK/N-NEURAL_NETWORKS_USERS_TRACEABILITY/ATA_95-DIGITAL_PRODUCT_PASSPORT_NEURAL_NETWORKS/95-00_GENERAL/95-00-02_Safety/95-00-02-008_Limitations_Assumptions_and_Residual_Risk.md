# 95-00-02-008 — Limitations, Assumptions, and Residual Risk

## 1. Purpose

This document defines the **limitations and assumptions** of the **Neural Network
Digital Product Passport (DPP)** safety framework and documents **residual risks**
that remain even after all safety controls are applied.

It clarifies:

- What the DPP safety view **can** and **cannot** represent.
- Explicit assumptions underlying the safety arguments.
- Residual risks and their acceptance rationale (ALARP principle).

---

## 2. DPP Safety Limitations

### 2.1 What the DPP Can Represent

The DPP is designed to:

- Document **known** safety-relevant attributes of NN components (ODD, limitations, failure modes).
- Provide **traceable evidence** for safety cases and certification.
- Support **operational monitoring** and feedback loops for continuous improvement.
- Enable **impact analysis** when NN components are updated or retrained.

### 2.2 What the DPP Cannot Represent

The DPP **does not**:

- **Guarantee safety** on its own. The DPP is evidence and documentation; actual safety depends on correct implementation, deployment, and operation.
- **Predict all failure modes.** Novel or emergent failure modes may occur in conditions not anticipated during development.
- **Replace human judgment.** Safety decisions (e.g., accepting residual risk, approving DPP changes) require human expertise and accountability.
- **Eliminate uncertainty.** NN systems are inherently probabilistic; the DPP documents uncertainty but does not remove it.
- **Cover non-NN safety issues.** The DPP focuses on NN-specific aspects; broader system safety relies on traditional safety processes (FHA, FMEA, etc.).

---

## 3. Explicit Assumptions

The safety arguments and DPP content rely on the following assumptions:

### 3.1 Operational Assumptions

- **Assumption A1:** The NN component is only used within its documented Operational Design Domain (ODD).
  - **Validity:** Enforced by operational procedures, flight management logic, and pilot training.
  - **Risk if violated:** Unsafe behaviour, degraded performance, or complete failure.

- **Assumption A2:** Input data quality meets specified requirements (sensor health, calibration, data integrity).
  - **Validity:** Monitored by sensor health checks and pre-processing validation.
  - **Risk if violated:** Garbage-in-garbage-out; NN outputs may be unreliable.

- **Assumption A3:** Human operators are trained and competent to supervise the NN system and intervene when necessary.
  - **Validity:** Training programs, checklists, and operational procedures.
  - **Risk if violated:** Delayed or incorrect human response to NN failures.

### 3.2 Technical Assumptions

- **Assumption T1:** The training data is representative of operational conditions within the ODD.
  - **Validity:** Data provenance documented in ATA 96 data passport.
  - **Risk if violated:** Poor generalisation, high false positive/negative rates.

- **Assumption T2:** The NN model architecture and training process are correctly implemented and free from defects.
  - **Validity:** Code reviews, unit tests, integration tests.
  - **Risk if violated:** Model may not behave as intended, even if validation tests pass.

- **Assumption T3:** Runtime monitoring systems are accurate and timely in detecting anomalies.
  - **Validity:** Monitoring system V&V, alert threshold validation.
  - **Risk if violated:** Delayed detection of NN degradation or failure.

### 3.3 Regulatory and Organisational Assumptions

- **Assumption R1:** The certification authority accepts the DPP as valid evidence for NN safety assurance.
  - **Validity:** Alignment with AMC 20-170, EASA AI Roadmap, and other guidance.
  - **Risk if violated:** Certification delays or rejection.

- **Assumption R2:** The organisation has mature change control, configuration management, and quality assurance processes.
  - **Validity:** ISO 9001, AS9100, or equivalent certification.
  - **Risk if violated:** DPP updates may be inconsistent, incomplete, or unauthorised.

---

## 4. Residual Risks

Even with all safety controls in place, some **residual risks** remain:

### 4.1 Residual Risk R1: Undetected OOD Scenarios

- **Description:** NN encounters an input scenario outside its ODD that is not detected by OOD monitors.
- **Likelihood:** Remote (due to OOD detection, fallback logic, and pilot supervision).
- **Severity:** Major (could lead to incorrect system response).
- **Mitigation:** Continuous monitoring, incident reporting, and ODD refinement.
- **Acceptance Rationale:** Risk is ALARP; further mitigation would require perfect OOD detection (not achievable with current technology).

### 4.2 Residual Risk R2: Silent Performance Degradation

- **Description:** NN performance degrades gradually without triggering monitoring alerts.
- **Likelihood:** Remote (due to KPI monitoring and periodic revalidation).
- **Severity:** Minor to Major (depends on rate of degradation and detection lag).
- **Mitigation:** Scheduled retraining, drift detection, and trend analysis.
- **Acceptance Rationale:** Risk is ALARP; more frequent monitoring/retraining is cost-prohibitive.

### 4.3 Residual Risk R3: Adversarial Attack Success

- **Description:** Adversarial input bypasses defences and causes NN to produce incorrect output.
- **Likelihood:** Remote to Extremely Remote (depends on threat model and attack sophistication).
- **Severity:** Major to Catastrophic (depends on NN criticality).
- **Mitigation:** Input sanitisation, adversarial training, cybersecurity measures, multi-layered defences.
- **Acceptance Rationale:** Risk is ALARP; perfect adversarial robustness is not achievable; reliance on defence-in-depth.

### 4.4 Residual Risk R4: Human Oversight Failure

- **Description:** Human operator fails to detect or respond to NN failure or anomaly.
- **Likelihood:** Remote (due to training, procedures, and alerting systems).
- **Severity:** Major to Catastrophic (depends on criticality of the function).
- **Mitigation:** Human factors design, alerting, training, and procedural safeguards.
- **Acceptance Rationale:** Risk is ALARP; human error cannot be eliminated, only reduced through design and training.

### 4.5 Residual Risk R5: Emergent Failure Modes

- **Description:** Novel failure mode not anticipated during development emerges in operation.
- **Likelihood:** Remote to Extremely Remote (due to extensive V&V and operational monitoring).
- **Severity:** Minor to Catastrophic (unknown until discovered).
- **Mitigation:** Operational monitoring, incident investigation, continuous improvement.
- **Acceptance Rationale:** Risk is inherent in any complex system; addressed through learning and adaptation.

---

## 5. ALARP (As Low As Reasonably Practicable)

For each residual risk, the project must demonstrate that risk has been reduced to a level that is **As Low As Reasonably Practicable (ALARP)**, considering:

- **Costs:** Financial, schedule, and resource costs of further risk reduction.
- **Benefits:** Expected safety improvement from additional mitigations.
- **State of the art:** Whether further mitigation is technically feasible with current technology.
- **Regulatory guidance:** Compliance with applicable safety standards and guidance material.

ALARP decisions must be documented, justified, and approved by the safety manager or certification authority.

---

## 6. Continuous Review

Limitations, assumptions, and residual risks are **not static**:

- **Operational experience** may reveal new limitations or invalidate assumptions.
- **Technological advances** may enable better mitigation of residual risks.
- **Regulatory updates** may impose new requirements or change acceptance criteria.

The DPP safety framework (including this document) should be reviewed and updated:

- After significant incidents or near-misses.
- At major project milestones (e.g., certification, entry into service).
- Periodically (e.g., annually) as part of continuous improvement.

---

## 7. Communication to Stakeholders

Limitations, assumptions, and residual risks must be clearly communicated to:

- **Operators and pilots:** So they understand the boundaries and limitations of the NN system.
- **Maintenance personnel:** So they can maintain and troubleshoot the system correctly.
- **Certification authorities:** So they can make informed decisions about safety acceptance.
- **Passengers and the public:** Through appropriate disclosure (if applicable).

Transparency builds trust and enables informed risk management.

---

## 8. Document Control

- **Status:** `WORKING` / `FOR_REVIEW` / `APPROVED`
- **Owner:** Safety / Certification Lead
- **Last Updated:** [Date]
- **Notes:**

  - This document was **generated by AI prompted by Amedeo Pelliccia**.
  - Content must be **reviewed and approved** by designated human safety experts.
