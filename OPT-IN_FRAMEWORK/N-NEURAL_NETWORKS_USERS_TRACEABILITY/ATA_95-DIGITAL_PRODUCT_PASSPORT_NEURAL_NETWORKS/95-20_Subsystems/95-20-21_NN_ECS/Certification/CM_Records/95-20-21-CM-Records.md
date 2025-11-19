# 95-20-21 — Configuration Management Records (CM Records)

**Document ID**: 95-20-21-CM-Records  
**Subsystem**: 95-20-21 NN_ECS  
**Type**: Configuration Management Records Index  
**Certification Level**: DO-178C Level C  
**Status**: WORKING  
**Last Updated**: 2025-11-19  

---

## 1. Purpose

This document provides an **index and structure** for the **Configuration Management (CM) records** associated with the ECS Neural Network Subsystem (95-20-21 NN_ECS).

It supports and is governed by the **Software Configuration Management Plan (SCMP)**:

→ [`../95-20-21-SCMP.md`](../95-20-21-SCMP.md)

The records listed here are **certification evidence** and are referenced by:

- [`../95-20-21-PSAC.md`](../95-20-21-PSAC.md)  
- [`../95-20-21-SDP.md`](../95-20-21-SDP.md)  
- [`../95-20-21-SAS.md`](../95-20-21-SAS.md)  
- Verification and coverage reports:  
  - [`../ASSETS/Reports/95-20-21-Verification_Report.md`](../ASSETS/Reports/95-20-21-Verification_Report.md)  
  - [`../ASSETS/Reports/95-20-21-Coverage_Summary.md`](../ASSETS/Reports/95-20-21-Coverage_Summary.md)  

---

## 2. CM Records Directory Structure

All CM artefacts for 95-20-21 are stored under:

```text
Certification/CM_Records/
├── 95-20-21-CM_Records.md          # This index
├── Baselines/
│   ├── 95-20-21-BL_SW_v1.0.yaml
│   ├── 95-20-21-BL_SW_v1.1.yaml
│   └── ...
├── Releases/
│   ├── 95-20-21-REL_Q100_SW_v1.0.md
│   ├── 95-20-21-REL_Q100_SW_v1.1.md
│   └── ...
├── CCB_Minutes/
│   ├── 95-20-21-CCB_2025-10-15.md
│   ├── 95-20-21-CCB_2025-11-05.md
│   └── ...
├── Problem_Reports/
│   ├── 95-20-21-PR-0001.md
│   ├── 95-20-21-PR-0002.md
│   └── ...
└── Traceability_Snapshots/
    ├── 95-20-21-TRACE_Snapshot_2025-11-01.csv
    └── 95-20-21-TRACE_Snapshot_2025-11-15.csv
````

> Nota: los nombres son plantilla; pueden adaptarse mientras se mantenga consistencia y trazabilidad.

---

## 3. Software Baselines

Software baselines define the **frozen configuration** (code + models + docs + tests) used in specific verification campaigns and certification milestones.

**Location:**

* `Certification/CM_Records/Baselines/`

### 3.1 Baseline Record Template

Each baseline file (e.g. `95-20-21-BL_SW_v1.2.yaml`) should capture:

* Subsystem / scope
* Git commit hashes / tags
* ONNX model hashes
* Document versions (SRS, SDS, SCS, SVP, etc.)
* Test suite versions
* Toolchain versions

Suggested fields:

```yaml
baseline_id: "95-20-21-BL_SW_v1.2"
subsystem: "95-20-21 NN_ECS"
status: "FROZEN"

git:
  repo: "AMPEL360-BWB-H2-Hy-E"
  tag: "95-20-21_SW_v1.2"
  commit: "<hash>"

models:
  - id: "95-20-21-A-101"
    name: "Cabin Temperature Predictor"
    version: "1.2"
    file: "OPT-IN_FRAMEWORK/.../Models/Trained/temp_predictor_v1.2.onnx"
    sha256: "<hash>"

documents:
  srs_version: "1.0"
  sds_version: "1.0"
  scs_version: "1.0"
  svp_version: "1.0"

tools:
  onnxruntime_version: "X.Y.Z"
  python_version: "3.12"
  coverage_tool: "..."

frozen_on: "2025-11-18"
frozen_by: "Configuration Manager"
```

---

## 4. Releases

Releases describe **what is delivered** to:

* IMA / aircraft integration
* Test rigs
* Certification authorities

**Location:**

* `Certification/CM_Records/Releases/`

Typical content for a release record (e.g. `95-20-21-REL_Q100_SW_v1.2.md`):

* Release ID and date
* Target (e.g. AMPEL360-Q100-001)
* Reference to baseline: `95-20-21-BL_SW_v1.2`
* List of included artefacts (binaries, ONNX, configs)
* Known limitations
* Link to test evidence and reports

---

## 5. Configuration Control Board (CCB) Minutes

Changes impacting the certified configuration must be reviewed and approved by the CCB.

**Location:**

* `Certification/CM_Records/CCB_Minutes/`

Each CCB file (e.g. `95-20-21-CCB_2025-11-05.md`) should include:

* Date and attendees
* Change requests reviewed (PRs, issues)
* Decisions (approved/rejected/deferred)
* Impact analysis (safety, verification, schedule)
* Actions and owners

These records are referenced in:

* [`../95-20-21-SCMP.md`](../95-20-21-SCMP.md)
* [`../95-20-21-SAS.md`](../95-20-21-SAS.md)

---

## 6. Problem Reports (PR) & Resolutions

Problem Reports and resolutions provide the defect history and justification for the **final software quality status**.

**Location:**

* `Certification/CM_Records/Problem_Reports/`

Each PR file (e.g. `95-20-21-PR-0001.md`) should include at least:

* PR ID
* Title and description
* Affected components (models, modules, documents)
* Severity and safety impact
* Root cause analysis
* Corrective action
* Regression tests executed
* Status (OPEN / CLOSED / DEFERRED)

These PRs are referenced in:

* [`../95-20-21-SQAP.md`](../95-20-21-SQAP.md)
* [`../95-20-21-Verification_Report.md`](../ASSETS/Reports/95-20-21-Verification_Report.md)
* [`../95-20-21-SAS.md`](../95-20-21-SAS.md)

---

## 7. Traceability Snapshots

Traceability snapshots preserve **point-in-time** copies of the trace matrix for key milestones (e.g. prior to baselining, release, or major CCB).

**Location:**

* `Certification/CM_Records/Traceability_Snapshots/`

Typically derived from:
→ `../../TRACE/95-20-21-TRACE.csv`

Each snapshot should record:

* Snapshot date & reason
* Reference baseline / release
* Hash or checksum of the CSV
* Link to associated reports (VR, coverage, SAS)

---

## 8. Relationship with SCMP

This CM Records index is governed by the policies defined in:

→ [`../95-20-21-SCMP.md`](../95-20-21-SCMP.md)

In particular:

* Creation, update, and baselining rules
* Access control
* Archiving and retention
* Tooling and repositories used for CM

---

## 9. Document Control

* **Document ID**: 95-20-21-CM-Records
* **Location**: `Certification/CM_Records/95-20-21-CM_Records.md`
* **Version**: 1.0
* **Status**: WORKING
* **Owner**: Configuration Management – AMPEL360
* **AI Assistance**: Drafted with AI assistance (ChatGPT), prompted by **Amedeo Pelliccia**; content subject to human review and formal approval.
* **Approval**: Pending certification authority review

```

