# 02-20-12-A-502 — DO-178C Compliance Summary

**Asset ID:** 02-20-12-A-502_DO_178C_Compliance_Summary  
**Title:** DO-178C Compliance Summary — 02-20-12 Weight & Balance Computer (WBC)  
**Subsystem:** [02-20-12_Weight_Balance_Computer](../02-20-12_Weight_Balance_Computer/)  
**Type:** Certification / Compliance Summary  
**Status:** DRAFT / PLACEHOLDER  
**Owner:** Digital Operations & Aircraft Performance Domain  

---

## 1. Purpose

This document provides a **concise DO-178C compliance summary** for the  
**02-20-12 Weight & Balance Computer (WBC)** subsystem.

It:

- States the **assumed software level (DAL)** and safety context for WBC.  
- Summarises how WBC development and verification processes **satisfy DO-178C objectives**.  
- Cross-references the **planning documents, traceability artefacts, and evidence** for WBC.  
- Serves as an **entry point** for certification authorities, DERs, and internal safety reviews  
  when examining the WBC software contribution to aircraft-level safety.

This is a **subsystem-focused summary**; system-level and aircraft-level DO-178C artefacts are  
managed in their respective chapters / certification folders.

---

## 2. Scope & Applicability

### 2.1 Subsystem Scope

This compliance summary applies to the **software components** implementing the functionality  
of the **02-20-12 Weight & Balance Computer**, including:

- Static W&B calculations (Ramp / Taxi / TOW / Cruise / Approach / Landing).  
- BWB CG envelope monitoring and margin evaluation.  
- H₂ fuel representation & phase-based evolution at W&B abstraction level.  
- Real-time CG tracking (deterministic + sensor-based refinement).  
- Integration logic with ATA 28 H₂ fuel system data and interfaces to:
  - 02-20-11 Electronic Flight Bag (EFB)  
  - 02-20-13 Performance Computer  
  - 02-20-01 CAOS / Analytics  
  - ATA 31 Recording  

Optional NN-based corrections (ATA 95) are treated as **augmentation** and have separate  
evidence; this document describes how deterministic WBC core maintains **safety and compliance**  
independently of NN availability.

### 2.2 DO-178C Applicability

The summary is aligned with:

- **DO-178C** — Software Considerations in Airborne Systems and Equipment Certification.  
- Associated **supplements** where applicable (e.g. DO-330 for tool qualification).  

It focuses on the **software level objectives** expected for WBC, assuming integration into a  
certified avionics environment (ATA 42 / IMA).

---

## 3. Assumed Software Level & Safety Context

### 3.1 Safety Role of WBC

The WBC provides **mass and CG data** and **CG envelope status** used by:

- Flight crew (via EFB) for **loadsheet validation and awareness**.  
- Performance Computer for **takeoff/landing performance** and **hybrid envelope** evaluations.  
- CAOS / analytics for **fleet monitoring** and **operational limits** tuning.  

Incorrect WBC outputs can, in worst-case scenarios, contribute to:

- Operation **outside certified CG envelopes**.  
- **Underestimation of takeoff/landing distances** when coupled with performance tools.  
- **Misleading crew information** in abnormal H₂ / loading conditions.

### 3.2 Proposed Software Level (Indicative)

Subject to system safety assessment and authority agreement:

- **Baseline assumption:**  
  - WBC core software is **DO-178C Level B or C**.  
- Rationale (to be finalised in system safety docs):
  - WBC data influences **safety-significant decisions** (mass/CG, envelope checks).  
  - Additional mitigations may exist (paper loadsheet, independent checks, AFM limits,  
    aircraft flight control protections, etc.).

This document is written in a level-agnostic way but **aims at Level B** as a conservative target,  
with notes where Level C simplifications may apply.

---

## 4. Planning & Lifecycle Documents

WBC software development shall follow a **documented DO-178C lifecycle**.  
At WBC level, the following planning artefacts are expected (filenames indicative):

- **PSAC — Plan for Software Aspects of Certification**  
  - `02-20-12-A-510_PSAC_WBC.md` *(placeholder)*  

- **SDP — Software Development Plan**  
  - `02-20-12-A-511_SDP_WBC.md` *(placeholder)*  

- **SVP — Software Verification Plan**  
  - `02-20-12-A-512_SVP_WBC.md` *(placeholder)*  

- **SCMP — Software Configuration Management Plan**  
  - `02-20-12-A-513_SCMP_WBC.md` *(placeholder)*  

- **SQAP — Software Quality Assurance Plan**  
  - `02-20-12-A-514_SQAP_WBC.md` *(placeholder)*  

For AMPEL360, certain plan sections may be **centralised at platform or ATA 02 level** and  
referenced by WBC-specific annexes. This document should link to those global plans once  
they are instantiated.

---

## 5. Requirements & Traceability (DO-178C Objectives)

### 5.1 Requirements Structure

WBC requirements are structured as:

- System / operational requirements under ATA 02 / fuel / safety chapters.  
- WBC-level software requirements (`RQ-02-20-12-*`), grouped by function:
  - Core W&B, CG envelopes, H₂ integration, real-time CG, ATA 28 integration, safety.  

### 5.2 Traceability

Traceability is provided primarily via:

- [02-20-12-A-501_Requirements_Traceability.md](./02-20-12-A-501_Requirements_Traceability.md)  

which offers:

- **Requirement ↔ Design / Algorithm ↔ Verification** mapping.  
- Links to **algorithm catalogue**:  
  - [02-20-12-A-101_Calculation_Algorithms.md](./02-20-12-A-101_Calculation_Algorithms.md)  

For DO-178C objectives, the RTM ensures:

- Each **High-Level Requirement** (HLR) has corresponding **software requirements / design elements**.  
- Each software requirement is covered by **test cases or analyses**.  
- Bi-directional trace: **Requirement ↔ Code / Unit ↔ Test ↔ Results**  
  (implementation-level trace matrix to be created per codebase).

---

## 6. Design, Architecture & Coding Standards

### 6.1 Design & Architecture

WBC architecture is documented in:

- [02-20-12-A-001_WB_Architecture.md](./02-20-12-A-001_WB_Architecture.md)  
- Functional docs:
  - [02-20-12-002_Load_Calculation_Engine.md](../02-20-12-002_Load_Calculation_Engine.md)  
  - [02-20-12-003_CG_Envelope_Monitoring.md](../02-20-12-003_CG_Envelope_Monitoring.md)  
  - [02-20-12-004_H2_Fuel_Integration.md](../02-20-12-004_H2_Fuel_Integration.md)  
  - [02-20-12-005_Real_Time_CG_Tracking.md](../02-20-12-005_Real_Time_CG_Tracking.md)  
  - [02-20-12-006_Integration_with_ATA_28.md](../02-20-12-006_Integration_with_ATA_28.md)  

The design clearly separates:

- **Deterministic W&B core** (ALG-WB-01..06).  
- **Runtime CG propagation and sensor fusion** (ALG-RTCG-01/02).  
- **Optional NN corrections** (ALG-RTCG-03, ATA 95) behind guarded interfaces.  

### 6.2 Coding Standards

Implementation code (language TBD – e.g. C / C++ / safety-qualified framework) shall adhere to:

- A **coding standard** specified in the SDP (naming, structure, defensive programming).  
- **Restrictions on dynamic behaviour** (no unbounded recursion, constrained dynamic memory, etc.).  
- **MISRA-like or DO-178C-compatible rules** for language subset usage.

Conformance is checked via:

- **Code reviews** (SQAP-defined independence).  
- **Static analysis** tools (tool qualification as required; see §9).  

---

## 7. Verification Strategy

### 7.1 Verification Levels

Verification is structured in:

- **Requirements-based tests**:
  - HLR / software requirements mapped to test cases as per RTM.  
- **Low-level testing / unit testing**:
  - Per algorithm / module (ALG-WB-*, ALG-RTCG-*).  
- **Integration tests**:
  - WBC ↔ EFB, WBC ↔ Performance Computer, WBC ↔ ATA 28 & ATA 31.  
- **Host and/or target testing**:
  - Host-based regression + hardware/target tests for performance, timing, and I/O.  

### 7.2 Test Artefacts (Planned)

Typical test artefacts for WBC include (placeholders):

- `TEST_DATA/02-20-12-T-001_WB_Scenarios_Ramp_TOW_LW.json`  
- `TEST_DATA/02-20-12-T-002_WB_CG_Envelopes.json`  
- `TEST_DATA/02-20-12-T-003_WB_H2_Evolution.json`  
- `TEST_DATA/02-20-12-T-005_WB_H2_Reserves_And_Imbalance.json`  
- `TEST_DATA/02-20-12-T-006_RT_CG_Scenarios.json`  
- `TEST_DATA/02-20-12-T-007_RT_CG_SensorFusion.json`  

Each test case is to be:

- Linked to **specific requirement IDs**.  
- Executed with **pass/fail criteria** and recorded results.  
- Included in **verification reports** (e.g. `02-20-12-A-520_WB_Verification_Report.md`, placeholder).

### 7.3 Coverage Objectives

Depending on the agreed software level:

- **Level B target:**  
  - **Statement coverage** & **decision coverage** of WBC code.  
- **Level C target:**  
  - At minimum, **statement coverage**, with rationale for decision coverage if not required.  

Coverage analysis tools may be used; tool qualification will be addressed per §9.

---

## 8. Configuration Management (CM)

Configuration management for WBC shall:

- Uniquely identify:
  - **Software baselines** (source code, build outputs).  
  - **Requirements**, design docs, test cases, and results.  
- Control **changes** via a defined CCB / change process (aligned with AMPEL360 OPT-IN framework).  
- Maintain **baselines** for:
  - WBC software release(s).  
  - Associated documentation and test evidence.  

The WBC CM approach is described in:

- `02-20-12-A-513_SCMP_WBC.md` *(placeholder)*  
- Repository-level CM tooling, including **doc-meta enforcers / geometry baseline watchdogs**,  
  where applicable for WBC artefacts.

---

## 9. Tool Qualification

Any tools whose outputs **cannot be fully verified** and that **replace or automate** DO-178C  
processes must be considered for **tool qualification** (DO-330).

Potential candidate tools in the WBC context (to be confirmed):

- **Code generators / model-based tools**, if used.  
- **Test automation frameworks** generating test code / procedures.  
- **Coverage measurement tools** used for DO-178C coverage evidence.  
- **Static analysis tools**:
  - If considered **verification tools**, may require qualification commensurate with software level.

A WBC-specific **Tool Assessment & Qualification Plan** section is expected in the PSAC / SVP.

---

## 10. Software Quality Assurance (SQA)

SQA for WBC shall provide **independent assurance** that:

- Processes defined in PSAC/SDP/SVP/SCMP/SQAP are **followed and effective**.  
- Reviews (requirements, design, code, tests) are conducted with appropriate independence.  
- Non-conformities are **recorded, tracked, and resolved**.  
- Evidence is in place to support DO-178C objectives (e.g. review checklists, audit reports).

The SQAP defines:

- **Independence level** appropriate for the software level.  
- **Sampling vs exhaustive** reviews rationale (if applied).  

---

## 11. Problem Reporting & Change Control

WBC problem reporting & change control shall:

- Use a **formal defect tracking system** (tool TBD), with linkage to:
  - Requirement IDs  
  - Code changes (commits)  
  - Test cases and results  
- Classify **problem severity** and **safety impact**.  
- Ensure:
  - Corrective actions are **verified**.  
  - Impact on **existing baselines** and **certification evidence** is assessed.  

Each WBC software release intended for certification must be accompanied by a:

- **Problem Report Status** summary:
  - Open PRs (with rationale for acceptability).  
  - Closed PRs and associated verification.

---

## 12. Evidence Package & Data Item Index

For DO-178C, WBC evidence will be grouped into a **subsystem DO-178C package**,  
referenced from the overall ATA 02 / AMPEL360 certification dossier.

Indicative contents (placeholders):

- **Planning**  
  - PSAC, SDP, SVP, SCMP, SQAP (02-20-12-A-51x series).  

- **Requirements & Design**  
  - WBC requirements specifications (`RQ-02-20-12-*` docs).  
  - Architecture & design assets (`02-20-12-00x`, `02-20-12-A-00x`).  
  - Algorithm specification: [02-20-12-A-101_Calculation_Algorithms.md](./02-20-12-A-101_Calculation_Algorithms.md).  

- **Traceability**  
  - [02-20-12-A-501_Requirements_Traceability.md](./02-20-12-A-501_Requirements_Traceability.md).  
  - Implementation / test trace matrix (code-level, to be created).  

- **Verification**  
  - Test cases & procedures.  
  - Test logs & results.  
  - Coverage reports.  
  - Verification report (e.g. `02-20-12-A-520_WB_Verification_Report.md`, placeholder).  

- **Configuration & Quality**  
  - CM records for WBC releases.  
  - SQA audit reports.  
  - Problem report summaries.

This current **Compliance Summary** (A-502) provides a **narrative top sheet** that references  
these detailed artefacts.

---

## 13. Open Items & Next Steps

At this stage, the WBC DO-178C compliance framework is **conceptually defined**, with the  
following main open items:

1. **Finalize DAL & safety allocation**  
   - Confirm Level B vs C for WBC in the system safety assessment.  

2. **Instantiate planning documents**  
   - Create WBC PSAC/SDP/SVP/SCMP/SQAP or reference higher-level plans.  

3. **Harden requirement set**  
   - Finalise `RQ-02-20-12-*` documents and align RTM (A-501).  

4. **Define tool chain and qualification needs**  
   - Identify critical tools, decide on DO-330 qualification scope.  

5. **Populate verification artefacts**  
   - Implement test cases & data files.  
   - Run tests and collect coverage evidence.  

6. **Create formal evidence package**  
   - Bundle WBC data items into a subsystem DO-178C package for review.

These items should be tracked in the **WBC certification plan** and subsystem CCB.

---

## 14. Document Control

> **Originator:** AI prompted by Amedeo Pelliccia  
> **Subsystem:** 02-20-12 Weight & Balance Computer  
> **Asset:** DO-178C Compliance Summary — WBC  
> **Toolchain:** MCP Doc Control + AMPEL360 OPT-IN Framework  

| Version | Date       | Author / Team                         | Notes                                           |
| ------- | ---------- | ------------------------------------- | ----------------------------------------------- |
| 0.1.0   | 2025-11-20 | AMPEL360 Digital Ops & Performance WG | Initial DO-178C compliance summary for WBC      |
