# 02-20-13-005 — NN Performance Predictor Integration

**Document ID:** 02-20-13-005  
**ATA Chapter:** 02-20-13 Performance Tools – NN Integration  
**Aircraft Program:** AMPEL360 BWB H₂ Hy-E (Q80/Q100/Q120)  
**Document Type:** AI/NN Integration & Interface Specification  
**Status:** DRAFT / PLACEHOLDER  

---

## 1. Purpose and Scope

This document specifies the **integration layer** between:

- The **deterministic performance core**:
  - Takeoff algorithms (02-20-13-002_Takeoff_Performance.md)  
  - Landing algorithms (02-20-13-003_Landing_Performance.md)  
  - Cruise/CI algorithms (02-20-13-004_Cruise_Optimization.md)  

and the **AI/NN Performance Predictor subsystem** governed by **ATA 95 Neural Networks**.

The NN Performance Predictor layer:

- Provides **data-driven corrections and uncertainty estimates** to deterministic performance outputs.  
- Implements **guard-rails, envelope checks and fallbacks** so that safety-critical outputs remain bounded and certifiable.  
- Ensures full **traceability, logging and digital product passport (DPP)** links for every NN inference used in operations.  

Scope:

- On-board tools (EFB, FMS advisory)  
- Ground tools (dispatch / OFP generation, fleet analytics)  
- Offline analysis (model training, re-training, re-calibration hooks)  

---

## 2. References

> **TODO:** Replace placeholders with actual repo paths and add hyperlinks.

Performance tools:

- [02-20-13-002_Takeoff_Performance.md](./02-20-13-002_Takeoff_Performance.md)  
- [02-20-13-003_Landing_Performance.md](./02-20-13-003_Landing_Performance.md)  
- [02-20-13-004_Cruise_Optimization.md](./02-20-13-004_Cruise_Optimization.md)  

Requirements & V&V:

- [RQ-02-20-13-004_NN_Performance_Predictor_Requirements.md](./RQ-02-20-13-004_NN_Performance_Predictor_Requirements.md)  
- [02-20-13-VERIF.md](./VERIF.md)  
- [02-20-13-TRACE.csv](./TRACE.csv)  
- [02-20-13-EVIDENCE/](./EVIDENCE/)  

Neural Networks governance (ATA 95):

- [95-00-00_GENERAL/01_OVERVIEW/ATA_95_Purpose_Scope.md](../../N-NEURAL_NETWORKS_USERS_TRACEABILITY/…)  
- [95-00-00_GENERAL/01_OVERVIEW/Traceability_Requirements.md](../../N-NEURAL_NETWORKS_USERS_TRACEABILITY/…)  
- [95-00-00_GENERAL/01_OVERVIEW/Certification_Framework.md](../../N-NEURAL_NETWORKS_USERS_TRACEABILITY/…)  
- [95-00-00_GENERAL/01_OVERVIEW/User_Accountability_Model.md](../../N-NEURAL_NETWORKS_USERS_TRACEABILITY/…)  

Certification / guidance (to be fully referenced):

- EASA / FAA AI assurance frameworks  
- DO-178C / DO-331 extensions & related AI guidance  
- Operator policies on AI/NN use in flight ops  

---

## 3. Role in System Architecture

At high level, performance computation is structured as:

```text
(det_inputs) ──► Deterministic Core ──► Baseline Outputs y_base
                        │
                        │ (features)
                        ▼
                NN Performance Predictor
                        │ (Δ, σ, flags, metadata)
                        ▼
                 Guard-Rails & Fusion
                        │
                        ▼
                   Final Outputs y_final
                 + NN Traceability Record
````

Key principles:

* **Deterministic core remains the source of truth.**
* NN predictions are used as:

  * **Δ-corrections** to reduce known conservatism / model bias, and/or
  * **uncertainty / confidence estimators** for monitoring and advisory purposes.
* **Hard limits and envelopes** are enforced around deterministic outputs.
* Every NN inference producing an operationally used value is **logged and traceable** under ATA 95.

---

## 4. Operational Use Cases

The NN predictor may support, but does not replace, the deterministic algorithms in:

1. **Takeoff performance advisory**

   * Refine estimated **ASD / AGD / TOFL** and margins using historical fleet data.
   * Provide **bias corrections** to deterministic tables/models for specific airports, slopes, µ-conditions.

2. **Landing performance advisory**

   * Improve **actual landing distance** predictions based on fleet braking behaviour.
   * Flag **higher-than-expected stopping distances** patterns for given runway conditions.

3. **Cruise & CI optimization**

   * Learn effective **drag / power / consumption** behaviour vs weight, altitude, Mach, winds.
   * Suggest **small CI or Mach adjustments** for better real-world eco / time trade-offs.

4. **Post-flight analytics and model tuning**

   * Large-scale analysis of **planned vs achieved** performance to feed:

     * Core model improvements,
     * NN re-training,
     * Operational recommendations.

5. **Monitoring / anomaly detection**

   * Detect **out-of-family behaviour** (e.g. systematic overrun of planned distances, abnormal power needed).
   * Raise **advisory alerts** to ops engineering and safety monitoring.

> Use cases where NN outputs impact safety-critical decisions must be supported by explicit safety case under ATA 95 and regulatory guidance.

---

## 5. Integration Modes

The integration layer supports three main modes:

1. **Advisory Mode (recommended default)**

   * NN provides **additional context / corrections**, but **final dispatch-critical numbers** are still based on deterministic outputs, possibly with strictly **bounded corrections**.
   * If NN is unavailable or fails validation, deterministic output is used unchanged.

2. **Correction Mode (bounded Δ-model)**

   * Final output: `y_final = y_base + clamp(Δ_pred, -Δ_max, +Δ_max)`
   * Δ_max, clipping logic and margin policies are defined per metric and certified case.

3. **Monitoring Mode (shadow / ghost mode)**

   * NN runs in parallel and logs predictions vs actuals.
   * No impact on operational outputs; used for **evaluation, tuning, surveillance**.

The allowed mode per **tool / operator / phase of implementation** is controlled by configuration and certification status and must be clearly documented.

---

## 6. Interfaces and Data Contracts

### 6.1 Common Inference Request

All NN performance predictors shall accept a common **request envelope**:

```text
NNPerfRequest {
  context_id              # flight / scenario identifier
  phase                   # TO, LND, CRZ, OTHER
  inputs_core             # deterministic core inputs (normalized)
  outputs_baseline        # y_base from deterministic algorithms
  env_metadata            # airport, runway id, date/time, METAR-like summary
  aircraft_state          # tail, config, weight, CG, MEL/CDL simplification
  model_selector_hints    # which NN family to load/use
}
```

> **TODO:** Define JSON / protobuf schema in ASSETS/API/02-20-13-NN_Perf_API.json.

### 6.2 Inference Response

```text
NNPerfResponse {
  y_correction            # Δ or ratio per metric (optional)
  y_prediction            # absolute predicted metric(s) (optional)
  uncertainty             # σ / confidence scores per metric
  validity_flags          # OK / WARN / REJECT / OOD
  guardrail_actions       # e.g. CLIPPED, IGNORED, BASE_ONLY
  nn_metadata {           # Digital Product Passport view
    nn_id
    nn_version
    training_dataset_id
    training_timestamp
    checksum
  }
}
```

The integration layer then applies **fusion logic**:

* Selects whether to use **y_correction**, **y_prediction**, or neither.
* Applies **clipping & monotonic constraints**.
* Produces **y_final** and a **Traceability Record** persisted for ATA 95.

---

## 7. NN Model Families and Responsibilities

NNs are grouped into **performance sub-families**:

* **NN-TO family**: Takeoff performance predictors

  * Metrics such as ASD, AGD, TOFL, margins, brake energy proxies.

* **NN-LND family**: Landing performance predictors

  * Landing distance required, braking decel profile descriptors, µ-eff estimates.

* **NN-CRZ family**: Cruise / CI predictors

  * Drag / power corrections, hydrogen consumption corrections, effective CI mapping.

Each model must:

* Declare **input feature list** and **validity envelope**.
* Declare **output variables, units and reference** (Δ vs absolute).
* Provide a **model card** (under ATA 95 DPP) describing:

  * Training data, limitations, known biases, intended use, non-intended use.

> **TODO:** Define explicit mapping between NN family IDs and paths under `ATA_95-DIGITAL_PRODUCT_PASSPORT_NEURAL_NETWORKS/95-20_Subsystems/…`.

---

## 8. Guard-Rails, Safety Policies and Fallbacks

The integration layer implements safety mechanisms:

### 8.1 Envelope / Out-of-Distribution Checks (ALG-NN-01)

* Check if `NNPerfRequest` is **inside the NN’s declared validity domain**:

  * Weight, CG, temperature, pressure, winds, runway condition, altitude, Mach…
* Use:

  * Manual envelope definitions
  * Optional OOD scores from NN itself (e.g. distance in latent space).
* If outside envelope:

  * Set `validity_flags=OOD`, `guardrail_actions=BASE_ONLY`.
  * Use baseline deterministic result; still log event.

### 8.2 Correction Bounding and Monotonicity (ALG-NN-02)

For each metric `y`:

* Define **max allowed correction** Δ_max and **sign rules**, e.g.:

  * For safety-critical distances: NN may **increase** required distances without bound, but may **reduce** them only up to **Δ_max_reduction**.
  * For fuel/time estimates: symmetric but bounded corrections may be allowed.

* Enforce:

```text
Δ_applied = clamp(Δ_pred, Δ_min_allowed, Δ_max_allowed)
y_final   = y_base + Δ_applied
```

* If NN suggests non-physical monotonic behaviour, mark `validity_flags=WARN` or `REJECT`.

### 8.3 Uncertainty-aware Fusion (ALG-NN-03)

* Use uncertainty σ to modulate trust:

  * High σ → reduce applied Δ, or ignore.
* Possible scheme:

```text
if σ > σ_max → ignore NN (BASE_ONLY)
else weight = f(σ)     # e.g. weight ∈ [0, 1]
     Δ_applied = weight * clamp(Δ_pred, ...)
```

### 8.4 Fallback Logic (ALG-NN-04)

NN inference is considered **optional** for system availability:

* If any failure in NN path (timeout, corruption, unverified checksum):

  * Fallback to deterministic core only.
  * Raise monitoring event but **no impact on operational output computation**.

---

## 9. Traceability, Logging and DPP Integration

Every NN inference that influences outputs must generate a **trace entry**:

```text
NNPerfTraceEntry {
  timestamp
  tool_id                # EFB / dispatch / server instance
  flight_id / context_id
  nn_id, nn_version
  inputs_hash            # hash of normalized NN inputs
  y_base, y_final
  Δ_pred, Δ_applied
  σ, validity_flags
  guardrail_actions
}
```

Integration with ATA 95 DPP:

* Each `nn_id` is resolvable to a **Digital Product Passport** entry under ATA 95:

  * Model architecture, training dataset, responsibilities, approvals.
* `02-20-13-TRACE.csv` will include **cross-links** to NN IDs for:

  * Requirements coverage
  * Verification & validation campaigns
  * In-service monitoring records.

Privacy / data protection:

* Trace entries must avoid storing **personal data**.
* Tail / flight identifiers are handled according to operator data policies.

---

## 10. Verification, Validation and Monitoring Strategy

### 10.1 Offline NN V&V (under ATA 95)

* Covered primarily in ATA 95 artefacts:

  * Dataset description & quality checks
  * Training/validation procedure
  * Bias & robustness analysis
  * Adversarial / stress testing.

This document focuses on **integration-level V&V**.

### 10.2 Integration-Level Tests (ALG-NN-05)

1. **Black-box regression tests**

   * For a library of standard scenarios, compare:

     * `(y_base, y_final, guardrail_actions, flags)` vs baselines.
   * Ensure guardrails behave as specified.

2. **Boundary / envelope tests**

   * Systematic sweeps across NN validity boundary.
   * Confirm:

     * OOD detection triggers appropriately.
     * Fallback to baseline is correct and logged.

3. **Monotonicity and safety properties**

   * Check that increasing factors (e.g. weight) do not cause **unsafe** decreases in required distance after fusion.

4. **Failure injection**

   * Simulate NN timeouts, corrupted responses, invalid metadata.
   * Confirm robust fallback behaviour.

5. **In-service monitoring**

   * Compare `y_final` vs actual measured performance (where available).
   * Monitor drift; trigger **retraining or model decommissioning** as required.

References and results are to be documented in:

* [02-20-13-VERIF.md](./VERIF.md)
* [02-20-13-EVIDENCE/NN_Performance_Predictor/](./EVIDENCE/NN_Performance_Predictor/)

---

## 11. Security and Integrity Considerations

The integration layer must ensure:

* **Model authenticity and integrity**:

  * Signed model artefacts.
  * Version and checksum checks before activation.

* **Inference request integrity**:

  * Normalization, bounds checking on inputs.
  * Protection against malformed / malicious requests (especially in server deployments).

* **Configuration management**:

  * Only approved NN versions for a given tool & operator.
  * Rollback mechanisms and clear mapping between configuration and cert status.

Security requirements are aligned with ATA 95 and general cybersecurity requirements for avionics / ops tools.

---

## 12. Open Points / TODOs

* [ ] Finalize **list of metrics** where NN corrections are allowed, and define per-metric Δ_max and sign rules.
* [ ] Define **exact schemas** for `NNPerfRequest` and `NNPerfResponse` (JSON / protobuf) and publish under ASSETS/API.
* [ ] Complete mapping of NN families to ATA 95 DPP structure and establish naming conventions (`NN-TO-xxx`, `NN-LND-xxx`, `NN-CRZ-xxx`).
* [ ] Align integration safety case with **EASA/FAA AI assurance frameworks** and AMPEL360 certification roadmaps.
* [ ] Add **worked examples**:
  - Takeoff case with NN distance correction and clipping.
  - Landing case where OOD detection disables correction.
  - Cruise case with CI adjustment based on NN advice.

---

*Editor’s note:*
This is a **skeleton integration specification**. Detailed API definitions, configuration tables, safety case references and model-specific constraints will be added as the NN subsystems under ATA 95 mature and enter incremental certification phases.

```
```
