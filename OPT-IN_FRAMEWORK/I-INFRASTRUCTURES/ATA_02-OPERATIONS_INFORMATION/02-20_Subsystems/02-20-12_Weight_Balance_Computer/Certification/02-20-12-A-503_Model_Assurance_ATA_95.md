# 02-20-12-A-503 — Model Assurance (ATA 95 Interface)

**Asset ID:** 02-20-12-A-503_Model_Assurance_ATA_95  
**Title:** Model Assurance for NN-Assisted WBC Functions (ATA 95 Interface)  
**Subsystem:** [02-20-12_Weight_Balance_Computer](../02-20-12_Weight_Balance_Computer/)  
**Axis:** I — Infrastructures  
**Type:** Model Assurance / Safety / Certification Asset  
**Status:** DRAFT / PLACEHOLDER  
**Owner:** Digital Operations & Aircraft Performance Domain  

---

## 1. Purpose

This document defines the **model assurance framework** for **Neural Network (NN) components**
that interact with the **02-20-12 Weight & Balance Computer (WBC)**, in line with:

- **ATA 95 — Neural Networks**  
- **DO-178C / DO-330** (for software & tools)  
- AMPEL360 **AI/ML governance** and model lifecycle

It describes **how WBC remains safe and certifiable** when **NN assistance is used**, ensuring:

- Deterministic WBC core remains **primary and sufficient** for safety.  
- NN models are treated as **bounded augmentations**, not single points of failure.  
- All NN use is **traceable**, **monitorable**, and subject to **fall-back mechanisms**.

---

## 2. Scope

### 2.1 Included

This document covers NN models that:

- Provide **auxiliary inputs** into WBC, e.g.:

  - NN-assisted **CG(t) correction** for Real-Time CG Tracking  
  - NN-assisted **H₂ consumption / distribution estimates** (if used at W&B level)  

- Are integrated via:

  - [02-20-12-005_Real_Time_CG_Tracking.md](../02-20-12-005_Real_Time_CG_Tracking.md)  
  - [02-20-12-006_Integration_with_ATA_28.md](../02-20-12-006_Integration_with_ATA_28.md)  

- Are defined and governed under **ATA 95 model cards**, for example:

  - `NN-CG-PRED-Q100-v1.0` — CG(t) correction model (placeholder)  
  - `NN-H2-DIST-Q100-v1.0` — H₂ distribution estimator (placeholder)  

WBC’s role is to **consume NN outputs under strict guardrails**, not to define or train the models.

### 2.2 Excluded

Not covered here:

- Full ATA 95 **model lifecycle documentation** (purpose, training, validation, MLOps).  
- NN models used solely by **02-20-13 Performance Computer** (see `02-20-13-005_NN_Performance_Predictor.md`).  
- Non-WBC NN applications (e.g. ATA 27/28/31 NNs).

Those are handled in dedicated ATA 95 artefacts (e.g. `95-XX-XXX_Model_Card_*.md`).

---

## 3. Relationship to Other Documents

**WBC core & certification:**

- [02-20-12-A-101_Calculation_Algorithms.md](./02-20-12-A-101_Calculation_Algorithms.md)  
- [02-20-12-A-501_Requirements_Traceability.md](./02-20-12-A-501_Requirements_Traceability.md)  
- [02-20-12-A-502_DO_178C_Compliance_Summary.md](./02-20-12-A-502_DO_178C_Compliance_Summary.md)  

**Functional design:**

- [02-20-12-005_Real_Time_CG_Tracking.md](../02-20-12-005_Real_Time_CG_Tracking.md)  
- [02-20-12-006_Integration_with_ATA_28.md](../02-20-12-006_Integration_with_ATA_28.md)  
- [02-20-12-003_CG_Envelope_Monitoring.md](../02-20-12-003_CG_Envelope_Monitoring.md)  
- [02-20-12-A-002_CG_Envelope_BWB.md](./02-20-12-A-002_CG_Envelope_BWB.md)  

**ATA 95 (NN) ecosystem (indicative paths):**

- `OPT-IN_FRAMEWORK/N-NEURAL_NETWORKS_USERS_TRACEABILITY/ATA_95_NEURAL_NETWORKS/95-00-00_GENERAL/`  
  - `01_OVERVIEW/ATA_95_Purpose_Scope.md`  
  - `01_OVERVIEW/Certification_Framework.md`  
  - `01_OVERVIEW/Traceability_Requirements.md`  
  - `01_OVERVIEW/User_Accountability_Model.md`  

This document sits at the **boundary** between 02-20-12 and ATA 95.

---

## 4. NN Roles in WBC

### 4.1 Deterministic vs NN-Assisted Architecture

Per [A-101 §11–13](./02-20-12-A-101_Calculation_Algorithms.md), WBC supports:

- **Deterministic core algorithms:**

  - `ALG-RTCG-01` — Runtime CG propagation (model only)  
  - `ALG-RTCG-02` — Sensor-based CG refinement  

- **Optional NN augmentation:**

  - `ALG-RTCG-03` — NN-assisted CG corrections (bounded ΔCG)

**Principle:** *Deterministic + sensor fusion path must always be adequate for safety*.
NNs may **improve accuracy or robustness** but never reduce determinism or traceability.

### 4.2 Example NN Use Cases (WBC View)

1. **CG(t) Correction Model (`NN-CG-PRED-*`)**

   - Inputs (conceptual):  
     - Deterministic CG(t) estimate,  
     - H₂ tank states (ATA 28),  
     - Aircraft configuration,  
     - Selected environmental / flight parameters.  
   - Outputs:  
     - `ΔCG_nn [%MAC]` + confidence/uncertainty.  
   - Used in `ALG-RTCG-03` as **bounded correction** on top of fused CG.

2. **H₂ Distribution Estimator (`NN-H2-DIST-*`)** *(optional)*

   - Inputs: partial sensor set (e.g. some gauges degraded).  
   - Outputs: estimated **H₂ per tank/group** with confidence.  
   - WBC may treat this as **additional input** to `ALG-WB-04` under strict limits.

In both cases, WBC enforces:

- **Hard bounds** on corrections.  
- **Quality thresholds** (ignore NN if uncertainty too high).  
- **Full fall-back** to deterministic path if NN unavailable or flagged.

---

## 5. Assurance Objectives (WBC Perspective)

From the WBC point of view, NN usage shall satisfy the following **assurance goals**:

1. **Role Clarity**  
   - NN models are **clearly scoped** as **assistive / corrective** components.  
   - Safety-critical decisions remain grounded in deterministic logic & envelopes.

2. **Bounded Influence**  
   - NN outputs must be passed through **saturation / bounding logic**.  
   - NN must **not** be able to drive CG estimates beyond physically plausible ranges or beyond envelope logic.

3. **Traceability & Accountability**  
   - Each NN model used by WBC is identified by a **model ID/version**.  
   - Model usage is **logged** and **traceable** to ATA 95 model cards and training/eval datasets.

4. **Detectability & Fallback**  
   - WBC can detect **NN unavailability, low confidence, drift**.  
   - Fallback to **deterministic-only mode** is well-defined and communicated to consumers.

5. **Certification Alignment**  
   - NN contributions and their limits are reflected in:

     - WBC **requirements** (`RQ-02-20-12-RT-003`, etc.).  
     - **RTM** (A-501).  
     - DO-178C / ATA 95 combined safety argument.

---

## 6. WBC–ATA 95 Interface Contract

### 6.1 Data Contract (Conceptual)

For each NN model integrated with WBC, ATA 95 provides:

```text
NNModelInterface {
  model_id: string,          # e.g. "NN-CG-PRED-Q100-v1.0"
  model_role: enum,          # CG_CORRECTION, H2_ESTIMATION, ...
  inputs_schema: json-schema,
  outputs_schema: json-schema,
  validity_domain: { ... },  # operational domain (altitude, mass, etc.)
  safety_bounds: {
    max_delta_cg_percent,
    max_delta_mass_kg,       # if relevant
    max_uncertainty
  },
  monitoring_signals: {
    error_metrics, drift_indicators, health flags
  }
}
````

WBC, in turn, guarantees to:

* **Check all safety bounds** before accepting NN outputs.
* **Reject / ignore** outputs outside the declared domain or with invalid health flags.
* Record NN usage in **WBC logs** / ATA 31 as appropriate.

### 6.2 Control & Status Flags

WBC shall maintain at least the following **status indicators**:

* `NN_AVAILABLE` — model loaded & callable.
* `NN_USED_FOR_SAMPLE` — NN output accepted (for that time-step).
* `NN_REJECTED_LOW_CONFIDENCE` — available but below confidence threshold.
* `NN_REJECTED_OUT_OF_DOMAIN` — inputs outside model validity domain.
* `NN_DISABLED_BY_CONFIG` — formally disabled for that aircraft / flight / mode.

These flags are available to:

* CAOS / analytics for **model performance monitoring**.
* Safety / certification teams for **assurance reports**.

---

## 7. Guardrails & Fallback Logic in WBC

### 7.1 CG Correction Bounded Application

Per `ALG-RTCG-03` (A-101 §13), WBC applies NN corrections as:

```text
ΔCG := clamp(nn_output.delta_cg_percent,
             -bounds.max_delta_percent,
             +bounds.max_delta_percent)

if nn_output.uncertainty <= bounds.max_uncertainty:
    cg_final := cg_fused + ΔCG
else:
    cg_final := cg_fused      # ignore NN
```

Additional WBC guardrails:

* **Envelope consistency check**:

  * If `cg_final` would drive state **more out-of-envelope** than `cg_fused`, WBC may:

    * Clamp `cg_final` to **no worse than fused**; or
    * Refuse NN correction altogether for that sample.

* **Numerical sanity**:

  * Any `NaN`, `INF`, or obviously invalid NN output ⇒ immediate rejection.

### 7.2 Operational Modes

At minimum, WBC supports:

* **Mode 1 — Deterministic Only**

  * NN components **not loaded or disabled**.
  * WBC maintains full functionality via deterministic algorithms only.

* **Mode 2 — Deterministic + NN-Augmented (Monitored)**

  * NN components active, providing corrections.
  * All NN usage is **logged**; CAOS / ATA 95 monitors long-term behaviour.

Transition rules (e.g. if NN health degrades) are defined in
`02-20-12-005_Real_Time_CG_Tracking.md` and ATA 95 model docs.

---

## 8. Requirements & Traceability (NN-Related)

### 8.1 WBC NN-Related Requirements (Excerpt)

From [A-501](./02-20-12-A-501_Requirements_Traceability.md):

* **RQ-02-20-12-RT-003** —
  *If NN-based corrections are used, they shall be bounded, monitored, and always backed
  by deterministic fallback.*

* **RQ-02-20-12-SAF-00X** *(to be defined)* —
  NN usage and failures must be **detectable** and result in **safe degraded modes**.

### 8.2 Algorithm Mapping

| Algorithm ID | Role                       | NN Aspect                                                    |
| ------------ | -------------------------- | ------------------------------------------------------------ |
| ALG-RTCG-01  | Deterministic CG(t)        | Baseline, no NN                                              |
| ALG-RTCG-02  | Sensor-based refinement    | Baseline + ATA 28 sensors, no NN                             |
| ALG-RTCG-03  | NN-assisted CG corrections | Applies `ΔCG_nn` under guardrails, logs NN usage & decisions |

### 8.3 Cross-ATA Traceability

Each WBC-integrated NN model is referenced by:

* **ATA 95 model card** ID and version.
* **WBC configuration** (which models are allowed per aircraft / variant).
* **RTM** entry linking:

  * `RQ-02-20-12-RT-003`
  * `ALG-RTCG-03`
  * ATA 95 model card + tests (`95-XX-XXX-*`)

---

## 9. Verification & Evidence (Excerpt)

### 9.1 WBC-Level Tests

From WBC perspective, NN assurance focuses on:

* **Correct guardrail behaviour**:

  * Tests where NN suggests large ΔCG ⇒ WBC clamps or rejects.
  * Inputs outside model domain ⇒ WBC rejects NN usage.

* **Fallback correctness**:

  * Simulated NN unavailability ⇒ WBC remains fully functional & reports fallback.
  * NN degraded status ⇒ deterministic-only behaviour with proper status flags.

Suggested test artefacts:

* `TEST_DATA/02-20-12-T-008_RT_CG_NN_Augmentation.json`

  * Scenarios with:

    * Nominal NN corrections inside bounds.
    * Out-of-domain inputs.
    * High-uncertainty outputs.
    * Deliberately malformed NN outputs (robustness tests).

### 9.2 ATA 95 Evidence (Referenced, Not Owned by WBC)

ATA 95 provides:

* Model cards (purpose, architecture, training data, performance, limitations).
* Training & validation reports.
* Robustness / out-of-distribution analyses.
* On-line monitoring & drift detection strategies.

This WBC document **requires** that:

* For each NN used by WBC, a **valid model card and evidence set exists** in ATA 95.
* WBC configuration explicitly points to the **approved model version(s)**.

---

## 10. Logging, Monitoring & Drift

WBC shall log, in a **model-agnostic way**:

* For each relevant time-step (or sampled subset):

  * `cg_fused` (without NN), `cg_final` (with NN if used).
  * `ΔCG_nn` applied (or reason for rejection).
  * NN status flags (`NN_USED_FOR_SAMPLE`, `NN_REJECTED_*`).

These logs are available to:

* ATA 95 monitoring functions (e.g. drift detection), via CAOS / ATA 31.
* Safety / performance teams for **post-flight analysis** and **model re-certification**.

If **drift** is detected by ATA 95 monitoring, WBC may be commanded to:

* **Switch permanently to deterministic-only mode** for affected aircraft or fleet.
* Or apply **tighter bounds** on NN corrections (config update).

---

## 11. Certification & Safety Argument (Sketch)

The **safety argument** for NN use in WBC rests on:

1. **Deterministic sufficiency**

   * All safety-critical functions (mass, CG, envelope checks) are fully realised by deterministic algorithms (`ALG-WB-*`, `ALG-RTCG-0[1–2]`).

2. **NN as bounded augmentation**

   * NN outputs are always **post-processed**, **bounded**, and **optional**.

3. **Separation of concerns**

   * WBC enforces **guardrails and fallbacks**;
   * ATA 95 ensures **model quality** (data, training, validation, monitoring).

4. **Traceability & evidence**

   * Requirements captured in `RQ-02-20-12-RT-*` and ATA 95 requirements.
   * Combined RTM and ATA 95 documentation provide a consistent chain from
     requirements → models → integration → tests → in-service monitoring.

This high-level argument is refined in:

* [02-20-12-A-502_DO_178C_Compliance_Summary.md](./02-20-12-A-502_DO_178C_Compliance_Summary.md)
* ATA 95 certification framework docs.

---

## 12. Open Items & Next Steps

Current open items (to be tracked in WBC + ATA 95 CCBs):

1. **Define concrete model IDs & roles** for WBC use (e.g. `NN-CG-PRED-Q100-v1.0`).
2. **Complete ATA 95 model cards** and link them explicitly here.
3. **Define detailed WBC configuration schema** for enabling/disabling NN models per variant.
4. **Implement and test guardrail logic**, including stress / robustness tests.
5. **Establish joint WBC–ATA 95 monitoring dashboards** in CAOS.
6. **Integrate NN aspects into the overall safety case** (system safety assessment).

---

## 13. Document Control

> **Originator:** AI prompted by Amedeo Pelliccia
> **Subsystem:** 02-20-12 Weight & Balance Computer
> **Asset:** Model Assurance for NN-Assisted WBC Functions (ATA 95 Interface)
> **Toolchain:** MCP Doc Control + AMPEL360 OPT-IN Framework

| Version | Date       | Author / Team                         | Notes                                                      |
| ------- | ---------- | ------------------------------------- | ---------------------------------------------------------- |
| 0.1.0   | 2025-11-20 | AMPEL360 Digital Ops & Performance WG | Initial WBC–ATA 95 model assurance framework (placeholder) |

```
```
