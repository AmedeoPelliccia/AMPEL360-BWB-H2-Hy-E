---
Title: "Operational Safety Procedures — ATA 02"
Identifier: "AMPEL360-02-00-02-009A"
Version: "1.0.0"
Status: "Draft"
AccessLevel: "Internal"
Author: "Ops"
CreatedAt: "2025-11-13"
ModifiedAt: "2025-11-13"
Scope: "Operational safety procedures for ATA 02 Operations Information within I-INFRASTRUCTURES"
Abstract: "Defines operational safety procedures for managing ATA 02 operations information, including publication cadence and approvals, turnaround-critical steps and cross-checks, and degraded operations fallbacks and escalation."
Keywords: ["ATA 02", "Operational Safety", "Procedures", "Turnaround", "Degraded Operations"]
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
  HazardMethodology: "./AMPEL360-02-00-02-007A_Hazard_Analysis_Methodology.md"
  HumanFactors: "./AMPEL360-02-00-02-008A_Human_Factors_Safety.md"
  Requirements: "../02-00-03_Requirements/"
  VAndV: "../02-00-07_V_AND_V/"
  RolesResponsibilities: "../02-00-01-004A_Roles_Responsibilities.md"
  TurnaroundContent: "../../02-10_Operations/"
ChangeLog:
  - {version: "1.0.0", date: "2025-11-13", author: "Ops", change: "Initial creation"}
---

# Operational Safety Procedures — ATA 02

## 1. Purpose

This document defines **operational safety procedures** for **ATA 02 — Operations Information**, focusing on:

- Safe governance and publication of operations information (cadence, approvals, two-person rule).
- **Turnaround-critical** operational steps and required cross-checks.
- Procedures and escalation paths for **degraded operations** (e.g., data issues, tool outages, infrastructure constraints).

It links the safety framework (objectives, hazard analysis, ERP, HF) to day-to-day operational practices for managing and using ATA 02 content.

---

## 2. Publication Cadence, Approvals, and Two-Person Rule

### 2.1 Publication Cadence

ATA 02 operations information must follow a defined **publication cadence**, agreed per program, typically including:

- **Planned updates**
  - Regular cycles (e.g., monthly/quarterly) for routine updates:
    - Turnaround parameters.
    - Procedures.
    - Infrastructure-related assumptions and constraints.
  - Coordination with:
    - Airport/infra changes.
    - Fleet/configuration changes.
    - Regulatory/publication cycles.

- **Unplanned / urgent updates**
  - Issued when:
    - Safety-relevant issues are detected (see ERP).
    - Critical airport or infrastructure changes occur outside planned cycles.
  - Must follow the emergency response principles in  
    `AMPEL360-02-00-02-003A_Emergency_Response_Procedures.md`.

Programs must document their actual cadence in `../02-00-10_Certification/` or a local governance note and ensure alignment with operator expectations.

### 2.2 Approvals Workflow

All safety-relevant ATA 02 publications must follow a **controlled approval workflow**:

- **Minimum roles involved** (see `../02-00-01-004A_Roles_Responsibilities.md`):
  - Ops Information Lead (or delegate).
  - Safety Engineer (Ops).
  - Technical Publications.
  - Certification Focal (for certification-relevant content or where required by program policy).
  - HF Lead (for major structural or HF-significant changes).

- **Approval checks must include**:
  - Technical correctness and consistency with design/configuration baselines.
  - Safety impact assessment and alignment with safety objectives and hazards.
  - Human Factors aspects (clarity, workload, error traps) where applicable.
  - Traceability links to requirements, analyses, and evidence.

### 2.3 Two-Person Rule

For **safety-critical** operations information (e.g., operational limitations, critical turnaround steps, emergency procedures):

- A **two-person rule** applies to at least the following activities:
  - Final content changes to safety-critical tables, procedures, or limitations.
  - Applicability or configuration tagging for content used operationally.
  - Activation/deactivation of safety-relevant publications or ERP bulletins.

- Two-person rule means:
  - One person performs the change (**preparer**).
  - A second, independent person (**reviewer/approver**) verifies:
    - Correctness of content.
    - Correct mapping to baselines/configurations.
    - Consistency with safety/ERP requirements.

- Evidence:
  - Approvals must be logged (e.g., in CSDB metadata, front-matter, or tooling audit trails).
  - Logs must be accessible as certification evidence where needed.

---

## 3. Turnaround-Critical Steps and Cross-Checks

Turnarounds are a primary context where ATA 02 information has direct safety and performance impact.

### 3.1 Identification of Turnaround-Critical Steps

Programs should maintain a **turnaround safety-critical step set**, typically stored under `../../02-10_Operations/`, including:

- Ground handling and servicing tasks.
- Turnaround time assumptions and buffers.
- Interfaces with airport services (fuel, catering, baggage, cleaning, towing).
- Constraints (e.g., stand type, equipment access, safety zones).

Each step must identify:

- **Safety significance** (e.g., fuel safety, door safety, pushback safety).
- **Information dependencies** (which ATA 02 datasets, tables, or procedures are needed).
- **Roles involved** (e.g., ramp agent, gate agent, dispatcher, crew).

### 3.2 Cross-Checks

For safety-critical turnaround steps, define **mandatory cross-checks**, such as:

- **Data cross-checks**
  - Validate critical parameters (turnaround times, constraints, limits) against:
    - Airport AODB/NOTAMs.
    - Airline/operator SOPs.
    - Config-specific limits (weight/balance, performance).
  - Use **dual-source checks** where feasible (e.g., independent tool vs. central dataset).

- **Procedural cross-checks**
  - Where a single step can introduce high risk, require:
    - Read-back or confirmation (e.g., “challenge–response” style).
    - Confirmation of critical parameters by two parties (e.g., dispatcher and captain).

- **Tool cross-checks**
  - For key planning tools:
    - Compare outputs for plausibility (e.g., turnaround time vs. historical/expected norms).
    - Flag anomalies (e.g., unusually low turnaround times) for manual review.

### 3.3 Handling Detected Inconsistencies

If a cross-check shows **inconsistent or suspect turnaround information**:

1. **Do not use** the suspect dataset as the primary reference.
2. **Escalate** via:
   - Local ops supervision and Safety Engineer (Ops).
   - Activation of ERP if the inconsistency is safety-critical.
3. **Fallback** to:
   - Last confirmed safe dataset, if valid.
   - Conservative operational assumptions (see Section 4).

All such cases should trigger updates in hazard/FMEA records where recurrent patterns emerge.

---

## 4. Degraded Operations: Fallbacks and Escalation

Degraded operations scenarios include:

- Loss or degradation of key datasets or information systems.
- Significant mismatches between ATA 02 content and real-world conditions.
- Tool outages, communications issues, or airport infrastructure disruptions.

### 4.1 Fallback Principles

Fallbacks should:

- **Prioritize safety over punctuality or efficiency**.
- Use **conservative assumptions** where data is incomplete or suspect.
- Ensure clear communication of:
  - Differences from nominal procedures or parameters.
  - Limitations of fallback methods.

Typical fallbacks include:

- Using **simplified or pre-defined contingency procedures** stored in ATA 02 or operator SOPs.
- Reverting to **last known safe dataset** (if still applicable).
- Using **manual calculations or look-up tables** as interim measures.

### 4.2 Escalation Matrix

Define a **degraded ops escalation matrix** mapping conditions to actions and roles. Example structure:

- **Condition Type A: Data issue**
  - Symptoms:
    - Ops dataset inconsistencies.
    - Stale or missing data.
  - Immediate action:
    - Suspend use of suspect data.
    - Trigger ERP if safety-relevant.
  - Escalate to:
    - Ops Information Lead.
    - Safety Engineer (Ops).
    - Technical Publications.
    - Certification Focal (if safety/cert basis impacted).

- **Condition Type B: Tool outage**
  - Symptoms:
    - Publication platform unavailable.
    - EFB sync failures affecting multiple crews.
  - Immediate action:
    - Switch to alternative channels (cached copies, printed backups) where safe.
    - Confirm validity of backups.
  - Escalate to:
    - IT/tools owners.
    - Ops Information Lead.
    - Airport/Infra Liaison if airport systems involved.

- **Condition Type C: Airport/infra disruption**
  - Symptoms:
    - Rapid changes (runway closure, stand changes).
    - Conflicts between ATA 02 information and current airport constraints.
  - Immediate action:
    - Use most authoritative real-time sources (NOTAMs, ATC, airport ops).
    - If conflicts with ATA 02 content are safety-relevant, trigger ERP.
  - Escalate to:
    - Airport/Infra Liaison.
    - Safety Engineer (Ops).
    - Operator/airline safety/ops contacts as applicable.

Programs should instantiate a concrete matrix (table/chart) in this file or a linked diagram under `../../02-90_Tables_Schemas_Diagrams/`.

---

## 5. Integration with Safety, HF, and Requirements

### 5.1 Safety Artefacts

Operational safety procedures must be consistent with and traceable to:

- **Certification Safety Objectives — ATA 02**  
- **CCA** (for identifying common causes behind degraded operations scenarios).  
- **FTA** and **FMEA** (mapping failure modes and barrier functions).

Where new degraded ops scenarios or turnaround-critical steps are identified, update hazards, FTA, FMEA, and CCA as needed.

### 5.2 Human Factors

- Procedures and fallbacks must be **HF-aware**:
  - Avoid overloading crew/operators during degraded ops.
  - Ensure instructions and change notices are clear, concise, and actionable.
- Link HF assessments and training (as per `AMPEL360-02-00-02-008A_Human_Factors_Safety.md`) to:
  - Turnaround-critical procedures.
  - Degraded ops scenarios where workload and SA are at risk.

### 5.3 Requirements and Verification

Translate key operational safety rules into **requirements** under `../02-00-03_Requirements/`, for example:

- “Safety-critical changes to ATA 02 operational limits shall implement a two-person rule for content change and applicability tagging.”
- “Turnaround-critical procedures shall include defined cross-checks and, where applicable, dual-source data validation.”
- “Degraded operations procedures shall specify fallbacks and escalation paths for data, tools, and airport/infra disruptions.”

Verify these requirements via:

- Process audits (publication logs, approvals).
- Scenario-based tests (turnaround simulations).
- Degraded ops drills and ERP exercises.

---

## 6. Usage Guidelines

When working with ATA 02 operational content:

1. **Follow the approvals and two-person rule**  
   - Do not bypass required reviewers for safety-relevant changes.
   - Ensure approvals are logged and traceable.

2. **Respect turnaround-critical procedures**  
   - Implement required cross-checks in operations workflows and tools.
   - Escalate if turnaround data or procedures appear inconsistent or unsafe.

3. **Apply degraded ops fallbacks and escalation**  
   - Recognize degraded conditions early.
   - Use the escalation matrix to reach the right roles quickly.
   - Activate ERP when safety is at risk due to information issues.

4. **Feed back into the safety system**  
   - After degraded ops events or ERP activations:
     - Review whether procedures, hazards, or requirements need updates.
     - Capture lessons learned into `02-00-02` safety artefacts and `02-00-03` requirements.

---
