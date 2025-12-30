---
document_id: "54-00-02-10-005"
ata: "54"
ata_title: "Nacelles / Pylons"
node: "54-00-02-10_HAZARD_ANALYSIS"
title: "Hazard Log Index"
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

# 54-00-02-10-005 — Hazard Log Index (ATA 54)

## 1. Purpose

Provide the authoritative navigation and operating rules for **ATA 54 hazard logs**, including:
- where the authoritative hazard log resides,
- how hazard IDs are created and kept stable,
- how hazards link to FHA/SSA/FTA, requirements, and evidence,
- what constitutes closure and who signs off.

This file is the “how to use the log” contract for all safety work products under `54-00-02_Safety/`.

## 2. Authoritative Files

| Artifact | Path |
|----------|------|
| **Master hazard log (authoritative)** | [`HAZARD_LOGS/54-00-02-10-001_Hazard_Log_Master.csv`](HAZARD_LOGS/54-00-02-10-001_Hazard_Log_Master.csv) |
| Hazard entry template | [`HAZARD_LOGS/54-00-02-10-002_Hazard_Log_Template.csv`](HAZARD_LOGS/54-00-02-10-002_Hazard_Log_Template.csv) |
| Functional hazard discovery | [`54-00-02-10-003_Functional_Hazards.md`](54-00-02-10-003_Functional_Hazards.md) |
| Classification policy | [`54-00-02-10-004_Hazard_Classification.md`](54-00-02-10-004_Hazard_Classification.md) |
| Safety objectives (overview) | [`../54-00-02-00_SAFETY_OVERVIEW/54-00-02-00-002_Safety_Objectives.md`](../54-00-02-00_SAFETY_OVERVIEW/54-00-02-00-002_Safety_Objectives.md) |
| Traceability matrix | [`../54-00-02-80_REQUIREMENTS_LINKS/54-00-02-80-003_Traceability_Matrix.md`](../54-00-02-80_REQUIREMENTS_LINKS/54-00-02-80-003_Traceability_Matrix.md) |

## 3. Hazard ID Policy (Stability Rules)

### 3.1 Stable hazard IDs

Each hazard SHALL have a stable identifier (HID). Recommended format:

`ATA54-HID-<NNNN>`

Example: `ATA54-HID-0007`

### 3.2 Immutability rules

- A `hazard_id` SHALL NEVER change once issued.
- If a hazard is merged/duplicated, mark the obsolete entry as `SUPERSEDED` and reference the canonical `hazard_id`.
- If a hazard is split, keep the original `hazard_id` for one branch and issue new HIDs for the others, documenting the split rationale.

### 3.3 Title changes

Hazard titles may be refined, but:
- maintain backward interpretability,
- keep the `hazard_id` unchanged,
- log the change reason in a notes/history field.

## 4. Minimum Required Fields (Master Log)

The Master log MUST contain (at minimum) the following fields per entry:

- hazard_id
- title
- entity_type (taxonomy tags)
- failure_condition_type (taxonomy tags)
- effect_domain (taxonomy tags)
- coupled_ata (list)
- flight_phase (optional but recommended)
- assumptions
- severity_term
- likelihood_term
- S_score
- L_score
- risk_score
- risk_state
- mitigations
- verification_plan (MoC: A/T/I/R)
- linked_objectives (SO IDs)
- linked_requirements (SR IDs)
- linked_evidence (artifact refs/IDs)
- owner_aor
- status (OPEN / IN_PROGRESS / CLOSED / SUPERSEDED)
- signoff_aor (as applicable)
- signoff_date (as applicable)

## 5. How to Add or Update Hazards

### 5.1 New hazard proposal workflow

1) Draft entries using:
- [`HAZARD_LOGS/54-00-02-10-002_Hazard_Log_Template.csv`](HAZARD_LOGS/54-00-02-10-002_Hazard_Log_Template.csv)

2) Assign a new `hazard_id` (next available sequence) and complete minimum fields.

3) Submit PR updating the Master:
- [`HAZARD_LOGS/54-00-02-10-001_Hazard_Log_Master.csv`](HAZARD_LOGS/54-00-02-10-001_Hazard_Log_Master.csv)

4) Review and approval:
- STK_SAF owns classification, wording, and closure logic.
- STK_CERT concurrence required per risk policy (see Section 7).

### 5.2 Reclassification rules

Reclassification is allowed if:
- assumptions change,
- design architecture changes,
- new evidence updates likelihood/severity.

Every reclassification MUST:
- update S/L and risk score consistently per classification policy,
- update the associated trace matrix entries (if impacted),
- record rationale (notes/history field).

## 6. Traceability Contract

### 6.1 Required links

Each hazard SHOULD be linked to:
- at least one safety objective (SO),
- mitigation(s) that become requirement(s) (SR) where applicable,
- MoC and evidence artifacts.

The authoritative linkage record is the traceability matrix:
- [`../54-00-02-80_REQUIREMENTS_LINKS/54-00-02-80-003_Traceability_Matrix.md`](../54-00-02-80_REQUIREMENTS_LINKS/54-00-02-80-003_Traceability_Matrix.md)

### 6.2 Downstream consumers

Hazard IDs SHALL be referenced (not redefined) by:
- FHA: `../54-00-02-20_FHA/`
- SSA: `../54-00-02-30_SSA/`
- FTA: `../54-00-02-40_FTA/`
- ZSA: `../54-00-02-50_ZSA/`
- Common cause: `../54-00-02-60_COMMON_CAUSES/`
- Interface impacts: `../54-00-02-70_INTERFACES_SAFETY/`
- SRM/MRO linkage: `../54-00-02-90_SRMS_AND_MRO_LINKS/`

## 7. Closure Rules and Sign-offs

A hazard may be set to `CLOSED` only if:
- mitigations are implemented,
- MoC is defined and executed (or formally accepted as planned under program gating),
- evidence artifacts are linked,
- residual risk is documented,
- required sign-offs are obtained.

### 7.1 Sign-off policy (minimum)

Use the policy defined in:
- [`54-00-02-10-004_Hazard_Classification.md`](54-00-02-10-004_Hazard_Classification.md)

Minimum sign-off guidance:
- **UNACCEPTABLE (R ≥ 20):** STK_SAF + STK_CERT + impacted AoR
- **TOLERABLE_WITH_MITIGATION (12–19):** STK_SAF (+ STK_CERT if severity ≥ HAZARDOUS)
- **CONTROLLED (6–11):** STK_SAF
- **ACCEPTABLE (1–5):** STK_SAF review

## 8. Quality Gates (Recommended)

Before releasing a baseline/tag:
- no `UNACCEPTABLE` hazards remain open,
- all `TOLERABLE_WITH_MITIGATION` hazards have an approved evidence plan,
- traceability matrix has no broken links (hazard → requirement → evidence),
- interface hazards have corresponding interface impact notes where applicable.

## 9. Open Items / TODO

- [TODO] Confirm final HID format if program standard deviates.
- [TODO] Add CSV schema validation rules (field constraints, enums) if enforced by CI.
- [TODO] Instantiate required coupled-ATA list for the current baseline.
