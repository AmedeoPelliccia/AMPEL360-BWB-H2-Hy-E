---
document_id: "54-00-02-10-004"
ata: "54"
ata_title: "Nacelles / Pylons"
node: "54-00-02-10_HAZARD_ANALYSIS"
title: "Hazard Classification"
project: "AMPEL360"
program: "AIR-T"
family: "Q100"
variant: "BWB"
phase: "LC02"
knot: "K07"
aor_owner: "STK_SAF"
aor_contributors: ["STK_SE","STK_CERT","STK_TEST","STK_CM","STK_MRO","STK_OPS"]
status: "DRAFT"
issue_rev: "I01-R01"
last_updated: "2025-12-29"
classification: "INTERNAL"
---

# 54-00-02-10-004 — Hazard Classification (ATA 54)

## 1. Purpose

Define the **hazard classification policy** for **ATA 54 (Nacelles / Pylons)**, including:
- controlled severity and likelihood terms,
- risk scoring approach,
- acceptance thresholds,
- required sign-offs and evidence expectations by risk level,
- mandatory fields for the hazard log master.

This document is normative for:
- hazard log scoring (`HAZARD_LOGS/54-00-02-10-001_Hazard_Log_Master.csv`)
- FHA/SSA/FTA risk arguments and closure decisions
- safety-derived requirements and traceability matrix.

## 2. Classification Inputs

A hazard entry SHALL be classified using:
- failure condition and effects (per taxonomy),
- operational context (flight phase, environment),
- exposure (frequency/duration),
- detection/annunciation and crew response assumptions,
- existing design controls and mitigations (if already defined),
- interface couplings and common cause contributors.

Where information is incomplete, record explicit assumptions and mark the entry **OPEN**.

## 3. Severity (Controlled Vocabulary)

Severity SHALL be selected from:

- **CATASTROPHIC**  
- **HAZARDOUS**  
- **MAJOR**  
- **MINOR**  
- **NO_SAFETY_EFFECT**

### 3.1 Severity guidance (ATA54-adapted)

Use the following guidance text (program policy may refine):

| Severity | Typical meaning (guidance) |
|---------|-----------------------------|
| CATASTROPHIC | Multiple fatalities and/or loss of the aircraft. |
| HAZARDOUS | Serious or fatal injury to a small number of occupants, large reduction in safety margins, or potentially uncontrollable aircraft / major structural loss. |
| MAJOR | Significant reduction in safety margins, increased crew workload, serious operational limitations; can lead to significant system damage but controllable. |
| MINOR | Slight reduction in safety margin, slight increase in crew workload, minor system damage. |
| NO_SAFETY_EFFECT | No effect on safety. |

## 4. Likelihood (Controlled Vocabulary)

Likelihood SHALL be selected from:

- **FREQUENT**
- **PROBABLE**
- **REMOTE**
- **EXTREMELY_REMOTE**
- **EXTREMELY_IMPROBABLE**

> Note: This document defines terms and scoring buckets. Quantitative mapping (probability per flight hour) can be added if required by the certification basis or program safety plan.

### 4.1 Likelihood guidance (qualitative)

| Likelihood | Guidance (qualitative) |
|-----------|-------------------------|
| FREQUENT | Expected to occur often in service. |
| PROBABLE | Will occur several times during the life of many aircraft. |
| REMOTE | Unlikely, but possible to occur during the life of an aircraft. |
| EXTREMELY_REMOTE | Very unlikely to occur. |
| EXTREMELY_IMPROBABLE | So unlikely that it is not expected to occur. |

## 5. Risk Scoring Matrix

### 5.1 Numerical mapping

Map severity and likelihood to integer scales:

**Severity score (S):**
- NO_SAFETY_EFFECT = 1
- MINOR = 2
- MAJOR = 3
- HAZARDOUS = 4
- CATASTROPHIC = 5

**Likelihood score (L):**
- EXTREMELY_IMPROBABLE = 1
- EXTREMELY_REMOTE = 2
- REMOTE = 3
- PROBABLE = 4
- FREQUENT = 5

**Risk Score (R):**  
`R = S × L`  (range 1–25)

### 5.2 Risk bands and actions

| R (S×L) | Risk State | Required action | Closure requirements |
|---------|------------|-----------------|----------------------|
| 20–25 | UNACCEPTABLE | MUST mitigate; redesign or add controls | STK_SAF + STK_CERT sign-off; objective/requirement created; verification evidence required |
| 12–19 | TOLERABLE_WITH_MITIGATION | MUST mitigate or justify residual risk | STK_SAF sign-off; STK_CERT if severity ≥ HAZARDOUS; evidence plan required |
| 6–11 | CONTROLLED | Controls may be procedural/design; justify | STK_SAF sign-off; evidence proportional to severity |
| 1–5 | ACCEPTABLE | Record and monitor | STK_SAF review; minimal evidence |

> Program may impose stricter thresholds for certain hazard types (e.g., structural separation hazards).

## 6. Special Handling Rules (ATA54)

The following conditions SHALL trigger elevated scrutiny regardless of computed R:

- **Structural separation** (partial or complete nacelle/pylon separation)  
  → always treat as **minimum HAZARDOUS**, typically **CATASTROPHIC**, pending architecture specifics.

- **Fire / smoke / ignition source** in nacelle/pylon zones (if applicable)  
  → require explicit interface alignment with ATA26 and evidence planning.

- **Common cause contributors** (shared resources, routing segregation failures)  
  → require linkage to Common Cause Analysis and Interface Safety notes.

- **Maintenance-induced latent hazards** on critical attachments  
  → require linkage to SRM/MRO node and task validation evidence.

## 7. Mandatory Hazard Log Fields (Minimum Dataset)

Each hazard entry in the Master log SHALL include at minimum:

- `hazard_id`
- `title`
- `entity_type` (controlled tags)
- `failure_condition_type` (controlled tags)
- `effect_domain` (controlled tags)
- `coupled_ata` (list)
- `flight_phase` (if applicable)
- `assumptions`
- `severity_term`
- `likelihood_term`
- `S_score`
- `L_score`
- `risk_score`
- `risk_state`
- `mitigations` (design/procedural)
- `verification_plan` (MoC: A/T/I/R)
- `linked_objectives` (SO IDs)
- `linked_requirements` (SR IDs)
- `linked_evidence` (artifact refs / IDs)
- `owner_aor`
- `status` (OPEN / IN_PROGRESS / CLOSED)
- `signoff_aor` and `signoff_date` (as applicable)

## 8. Means of Compliance (MoC) Categories

Use controlled MoC codes:

- **MoC-A:** Analysis
- **MoC-T:** Test
- **MoC-I:** Inspection / procedure validation
- **MoC-R:** Review

MoC and evidence are captured in:
- `../54-00-02-80_REQUIREMENTS_LINKS/54-00-02-80-003_Traceability_Matrix.md`

## 9. Residual Risk and Closure Rules

A hazard may be marked **CLOSED** only if:
- mitigations are defined and implemented,
- MoC is executed (or formally accepted as planned with defined gating),
- evidence artifacts are linked,
- required sign-offs are recorded,
- residual risk statement is documented (especially for R ≥ 12 or severity ≥ HAZARDOUS).

## 10. Change Control

Any change to:
- severity/likelihood scales,
- risk thresholds,
- special handling rules,
requires:
- STK_SAF approval,
- STK_CERT concurrence,
- update to all impacted hazards (reclassification sweep) with clear versioning.

## 11. Open Items / TODO

- [TODO] Align qualitative likelihood guidance to the program’s quantitative expectations (if mandated).
- [TODO] Confirm certification basis mapping to severity terminology and acceptance thresholds.
- [TODO] Confirm any architecture-specific “always catastrophic” hazard types for this baseline.
