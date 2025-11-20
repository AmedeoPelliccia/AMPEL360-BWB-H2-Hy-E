# 02-20-12-A-504 — Test Evidence Package

**Asset ID:** 02-20-12-A-504_Test_Evidence  
**Title:** Test Evidence Package — 02-20-12 Weight & Balance Computer (WBC)  
**Subsystem:** [02-20-12_Weight_Balance_Computer](../02-20-12_Weight_Balance_Computer/)  
**Axis:** I — Infrastructures  
**Type:** Verification / Certification Evidence  
**Status:** DRAFT / PLACEHOLDER  
**Owner:** Digital Operations & Aircraft Performance Domain  

---

## 1. Purpose

This document defines the **structure, contents, and conventions** of the  
**Test Evidence Package** for the **02-20-12 Weight & Balance Computer (WBC)**.

It acts as the **index and narrative top sheet** for all WBC test evidence, by:

- Listing **test data sets**, **test procedures**, **test logs**, and **coverage artefacts**.  
- Providing **traceability hooks** into the Requirements Traceability Matrix:  
  - [02-20-12-A-501_Requirements_Traceability.md](./02-20-12-A-501_Requirements_Traceability.md)  
- Supporting DO-178C / ATA 02 / ATA 95 **certification reviews**, in conjunction with:  
  - [02-20-12-A-502_DO_178C_Compliance_Summary.md](./02-20-12-A-502_DO_178C_Compliance_Summary.md)  
  - [02-20-12-A-503_Model_Assurance_ATA_95.md](./02-20-12-A-503_Model_Assurance_ATA_95.md)  

---

## 2. Scope

The WBC Test Evidence Package covers tests for:

- **Core W&B calculations** (ALG-WB-01..03, 06)  
- **H₂ representation & mass evolution** (ALG-WB-04)  
- **CG envelope evaluation** (ALG-WB-05)  
- **Real-time CG tracking & sensor fusion** (ALG-RTCG-01/02)  
- **Optional NN-assisted CG corrections** (ALG-RTCG-03, via ATA 95)  
- **ATA 28 integration & safety guardrails** (error handling, degraded modes)  

Out of scope:

- Platform-level tests (e.g. IMA integration, ATA 42 level).  
- Pure ATA 95 model validation (covered in ATA 95 model cards / test reports).  

This document **does not repeat test case details**; it indexes and explains where the  
full procedures and logs live in the repo / cert package.

---

## 3. Evidence Folder Structure (Suggested)

Under the WBC subsystem root:

```text
02-20-12_Weight_Balance_Computer/
├── ASSETS/
│   ├── 02-20-12-A-001_WB_Architecture.md
│   ├── 02-20-12-A-002_CG_Envelope_BWB.md
│   ├── 02-20-12-A-003_H2_Fuel_Effects.md
│   ├── 02-20-12-A-101_Calculation_Algorithms.md
│   ├── 02-20-12-A-501_Requirements_Traceability.md
│   ├── 02-20-12-A-502_DO_178C_Compliance_Summary.md
│   ├── 02-20-12-A-503_Model_Assurance_ATA_95.md
│   └── 02-20-12-A-504_Test_Evidence.md      ← You are here
│
├── TEST_DATA/
│   ├── 02-20-12-T-001_WB_Scenarios_Ramp_TOW_LW.json
│   ├── 02-20-12-T-002_WB_CG_Envelopes.json
│   ├── 02-20-12-T-003_WB_H2_Evolution.json
│   ├── 02-20-12-T-005_WB_H2_Reserves_And_Imbalance.json
│   ├── 02-20-12-T-006_RT_CG_Scenarios.json
│   ├── 02-20-12-T-007_RT_CG_SensorFusion.json
│   └── 02-20-12-T-008_RT_CG_NN_Augmentation.json
│
└── ASSETS/Reports/
    ├── 02-20-12-Verification_Report.md
    ├── 02-20-12-Coverage_Summary.md
    └── Test_Logs/
        ├── 02-20-12-T-001_WB_Scenarios_Ramp_TOW_LW.log
        ├── 02-20-12-T-002_WB_CG_Envelopes.log
        ├── 02-20-12-T-003_WB_H2_Evolution.log
        ├── 02-20-12-T-005_WB_H2_Reserves_And_Imbalance.log
        ├── 02-20-12-T-006_RT_CG_Scenarios.log
        ├── 02-20-12-T-007_RT_CG_SensorFusion.log
        └── 02-20-12-T-008_RT_CG_NN_Augmentation.log
````

*(Paths and formats are indicative; adapt to your actual CI/CD outputs as needed.)*

---

## 4. Test Data Sets (T-IDs)

The table below gives a **high-level view** of each test data set.
Detailed test-case definitions belong in their own files and the Verification Report.

| Test Data ID                                     | Purpose (Summary)                                         | Primary Requirements (see A-501)                 | Primary Algorithms (see A-101)             |
| ------------------------------------------------ | --------------------------------------------------------- | ------------------------------------------------ | ------------------------------------------ |
| 02-20-12-T-001_WB_Scenarios_Ramp_TOW_LW.json     | Core W&B for Ramp / Taxi / TOW / Landing Weight scenarios | WB-CORE-001/002, SAF-001                         | ALG-WB-01, ALG-WB-02, ALG-WB-03, ALG-WB-06 |
| 02-20-12-T-002_WB_CG_Envelopes.json              | BWB CG envelope in/near/out points                        | CG-001/002/003                                   | ALG-WB-02, ALG-WB-05                       |
| 02-20-12-T-003_WB_H2_Evolution.json              | H₂ evolution patterns & induced CG drift                  | H2-001/002/003                                   | ALG-WB-03, ALG-WB-04                       |
| 02-20-12-T-005_WB_H2_Reserves_And_Imbalance.json | H₂ reserves, boil-off & imbalance cases                   | H2-003, SAF-001                                  | ALG-WB-03, ALG-WB-04, ALG-WB-05            |
| 02-20-12-T-006_RT_CG_Scenarios.json              | Deterministic Runtime CG(t) vs reference                  | RT-001                                           | ALG-RTCG-01                                |
| 02-20-12-T-007_RT_CG_SensorFusion.json           | Sensor fusion, degraded sensors, ATA 28 faults            | RT-002, ATA28-002, SAF-001                       | ALG-RTCG-02                                |
| 02-20-12-T-008_RT_CG_NN_Augmentation.json        | NN corrections, bounds, fallback behaviour                | RT-003, SAF-00X (NN safe use), ATA 95 cross-refs | ALG-RTCG-03                                |

> **Note:** Requirement IDs like `WB-CORE-001` above are shorthand for full
> IDs (e.g. `RQ-02-20-12-WB-CORE-001`) defined in [A-501](./02-20-12-A-501_Requirements_Traceability.md).

---

## 5. Test Procedures & Logs

### 5.1 Test Procedures

Formal test procedures may be stored as:

* Markdown procedures:

  * `ASSETS/Reports/02-20-12-T-001_WB_Scenarios_Procedure.md`
  * `ASSETS/Reports/02-20-12-T-002_CG_Envelopes_Procedure.md`
  * ... or centralised at a higher test framework level.

Each procedure should specify:

* **Preconditions** (configuration, variant, initial states).
* **Steps** (including how to feed `TEST_DATA/*.json` into the test harness).
* **Expected results** (numeric tolerances, envelope status, error codes).

### 5.2 Test Logs

Execution logs are archived under:

* `ASSETS/Reports/Test_Logs/`

Each `*.log` file (format flexible: text, JSON, JUnit XML, etc.) should include:

* Test framework version and configuration.
* Hash / version of the **code under test**.
* Reference to the **test data file** and **procedure**.
* Pass/fail outcome per test case.
* Any relevant numeric diffs vs reference values.

Example naming convention:

* `02-20-12-T-006_RT_CG_Scenarios.log`

  * Contains multiple CG(t) scenario runs, each with requirement & algorithm IDs.

---

## 6. Verification Report & Coverage Summary

### 6.1 Verification Report

The main narrative verification report for WBC is:

* `ASSETS/Reports/02-20-12-Verification_Report.md` *(placeholder)*

Expected contents:

* Summary of **test scope & environment**.
* Mapping from **requirements → test cases** (referencing A-501).
* Overview of **results** (tests executed / passed / failed / waived).
* Discussion of **numerical aspects** (tolerances, stability, corner cases).
* Conclusions vs **DO-178C objectives** (in concert with A-502).

### 6.2 Coverage Summary

Coverage evidence is summarised in:

* `ASSETS/Reports/02-20-12-Coverage_Summary.md` *(placeholder)*

Expected content:

* Coverage metrics:

  * Statement coverage (and decision coverage if applicable).
  * Per-module and per-algorithm breakdown (ALG-WB-*, ALG-RTCG-*).
* Tools used and version(s).
* Any **justified gaps**:

  * Dead defensive code with rationale.
  * Configuration-dependent code not exercised in this version.

Raw coverage artefacts (tool-native formats) can be kept under:

* `ASSETS/Reports/Coverage_Raw/` *(to be created as needed)*

---

## 7. Link to Requirements Traceability (A-501)

The Test Evidence Package must stay aligned with
[02-20-12-A-501_Requirements_Traceability.md](./02-20-12-A-501_Requirements_Traceability.md).

For each requirement row in the RTM:

* At least one **test data set** (`T-*`) and **log** must be referenced.
* If a requirement is **verified by analysis or review** instead of test, the
  corresponding **analysis report** should be referenced from A-501 and the
  Verification Report.

A minimal cross-reference table (to be **maintained in A-501**, not duplicated):

* `Req ID → Algorithm(s) → Test Data ID(s) → Log file(s) → Verdict`.

This document (A-504) merely explains the **conventions** and folder structure that
make that RTM consumable for cert reviewers.

---

## 8. Problem Reports & Anomalies

Test execution may uncover:

* **Defects in WBC logic** (implementation or requirements).
* **Test harness issues**.
* **Out-of-date reference data** (e.g. envelope definitions).

All anomalies should be:

1. Recorded in the **problem reporting system** (tool TBD).
2. Referenced from:

   * Relevant test log(s) in `ASSETS/Reports/Test_Logs/`.
   * The Verification Report (`02-20-12-Verification_Report.md`).

For DO-178C-style releases, each WBC software baseline should have a section in
the Verification Report summarising:

* Open problem reports (with safety impact analysis).
* Closed problem reports and their associated **re-tests**.

---

## 9. NN & ATA 95–Related Test Evidence

From the WBC perspective, NN-related test evidence in `02-20-12-T-008_RT_CG_NN_Augmentation.json`
and its log file should demonstrate:

* Correct behaviour of **guardrails** and **fallback** (`ALG-RTCG-03`), per
  [02-20-12-A-503_Model_Assurance_ATA_95.md](./02-20-12-A-503_Model_Assurance_ATA_95.md).

ATA 95 will additionally provide:

* Dedicated NN test reports and metrics (outside this subsystem folder).
* These are linked **from** WBC RTM and Model Assurance docs, but **owned** by ATA 95.

---

## 10. Usage in Certification Packages

When building the subsystem / aircraft-level certification package, the contents of:

* `TEST_DATA/`
* `ASSETS/Reports/02-20-12-Verification_Report.md`
* `ASSETS/Reports/02-20-12-Coverage_Summary.md`
* `ASSETS/Reports/Test_Logs/`

are bundled as the **WBC test evidence volume**, referenced by:

* [02-20-12-A-502_DO_178C_Compliance_Summary.md](./02-20-12-A-502_DO_178C_Compliance_Summary.md)
* Higher-level ATA 02 / AMPEL360 certification index documents.

---

## 11. Document Control

> **Originator:** AI prompted by Amedeo Pelliccia
> **Subsystem:** 02-20-12 Weight & Balance Computer
> **Asset:** Test Evidence Package — WBC
> **Toolchain:** MCP Doc Control + AMPEL360 OPT-IN Framework

| Version | Date       | Author / Team                         | Notes                                             |
| ------- | ---------- | ------------------------------------- | ------------------------------------------------- |
| 0.1.0   | 2025-11-20 | AMPEL360 Digital Ops & Performance WG | Initial WBC test evidence structure & description |

```
```
