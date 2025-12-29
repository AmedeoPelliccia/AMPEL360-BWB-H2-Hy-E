---
document_id: "54-00-02-00-001"
ata: "54"
ata_title: "Nacelles / Pylons"
node: "54-00-02-00_SAFETY_OVERVIEW"
title: "Safety Framework"
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

# 54-00-02-00-001 — Safety Framework (ATA 54)

## 1. Purpose

Define the **safety framework** governing **ATA 54 (Nacelles / Pylons)** for AMPEL360 AIR-T, including:
- safety objectives decomposition and acceptance logic,
- hazard identification, classification, and logging rules,
- assessment coverage (FHA/SSA/FTA/ZSA/CCA),
- interface-safety handling with coupled ATA chapters,
- traceability and evidence expectations to support certification readiness.

## 2. Scope

This framework applies to:
- nacelle / pylon structures and integration architecture,
- any embedded functions hosted in nacelle volumes (as applicable),
- mechanical, thermal, electrical, and fluid interfaces crossing ATA 54 boundaries,
- maintenance / inspection constraints impacting safe operation.

Out of scope (unless explicitly referenced by an interface impact note):
- detailed system design specifications (owned by Design/Engineering nodes),
- non-ATA54 subsystem internal safety cases (owned by their ATA chapters).

## 3. Regulatory / Standard References

This framework SHALL align to the applicable certification basis and safety standards. References are managed in:
- `../54-00-02-80_REQUIREMENTS_LINKS/54-00-02-80-001_Cert_Basis_References.md`

Minimum reference set (to be instantiated for the program):
- EASA/FAA aircraft certification basis (CS-25 / Part 25) — **TODO: exact amendment(s)**
- System safety process (ARP4754A/ED-79A) — **TODO**
- Safety assessment methods (ARP4761/ED-135) — **TODO**
- Continued airworthiness practices (as applicable) — **TODO**
- Hydrogen / fuel cell related guidance if applicable via interfaces — **TODO**

## 4. Safety Governance

### 4.1 Roles and decision rights

- **Owner (AoR):** STK_SAF  
- **Sign-off AoRs (minimum):** STK_CERT, STK_CM  
- **Technical contributors:** STK_SE, STK_TEST, STK_MRO, STK_OPS (program-dependent)

Decision rights:
- hazard classification policy and acceptance criteria: **STK_SAF + STK_CERT**
- hazard log baseline release: **STK_SAF + STK_CM**
- closure of safety findings: **STK_SAF + STK_CERT + impacted AoR**

### 4.2 Configuration control

All safety artifacts are configuration controlled via PR workflow:
- every change MUST reference an issue/task id,
- hazards and requirements MUST keep stable IDs,
- evidence links MUST be updated when results are superseded.

## 5. Safety Lifecycle Coverage

This node governs the following safety work products:
- **Hazard analysis & logging** (`54-00-02-10_HAZARD_ANALYSIS/`)
- **FHA** (`54-00-02-20_FHA/`)
- **SSA** (`54-00-02-30_SSA/`)
- **FTA** (`54-00-02-40_FTA/`)
- **ZSA** (`54-00-02-50_ZSA/`)
- **Common cause** (`54-00-02-60_COMMON_CAUSES/`)
- **Interface impacts** (`54-00-02-70_INTERFACES_SAFETY/`)
- **Traceability** (`54-00-02-80_REQUIREMENTS_LINKS/`)
- **SRM/MRO linkage** (`54-00-02-90_SRMS_AND_MRO_LINKS/`)

## 6. Hazard Management Framework

### 6.1 Hazard identification sources

Hazards SHALL be identified from:
- functional decomposition (ATA 54 functions and boundaries),
- interface analyses with coupled systems,
- zone analyses (environment, access, separation),
- service history analogs (where relevant),
- maintenance tasks and repair constraints (SRM/MRO-driven hazards),
- FTA/SSA findings and common cause reviews.

### 6.2 Hazard classification

Classification rules SHALL be defined in:
- `../54-00-02-10_HAZARD_ANALYSIS/54-00-02-10-004_Hazard_Classification.md`

Each hazard entry MUST include:
- initiating events and failure conditions,
- effects and operational impact,
- severity, likelihood, and risk score (per program scale),
- mitigations/controls and their verification status.

### 6.3 Hazard log authority

The authoritative hazard log for ATA 54 is:
- `../54-00-02-10_HAZARD_ANALYSIS/HAZARD_LOGS/54-00-02-10-001_Hazard_Log_Master.csv`

Rule:
- FHA/SSA/FTA/ZSA/CCA artifacts MUST reference hazards by **hazard_id** from the Master log.

## 7. Interface Safety (Coupled ATA Chapters)

Safety-relevant interfaces SHALL be captured in:
- `../54-00-02-70_INTERFACES_SAFETY/54-00-02-70-001_Safety_Interfaces_Overview.md`

Minimum coupled ATA set (program-dependent, to be confirmed):
- ATA 24 (Electrical power)
- ATA 26 (Fire protection) — if applicable
- ATA 28 (Fuel / H₂) — if applicable
- ATA 30 (Ice & rain protection)
- ATA 51 (Structures)
- ATA 71/72 (Powerplant / propulsor integration)

For each interface impact note:
- link hazards impacted,
- identify assumptions and boundary conditions,
- point to the authoritative ICD when it exists (TBD location).

## 8. Acceptance Criteria and Safety Objectives Linkage

Safety objectives are defined in:
- `54-00-02-02-002_Safety_Objectives.md` **(TODO: confirm filename vs 54-00-02-00-002)**

Traceability:
- hazards → mitigations/controls → derived requirements → verification evidence  
is managed in:
- `../54-00-02-80_REQUIREMENTS_LINKS/54-00-02-80-003_Traceability_Matrix.md`

## 9. Evidence and Verification Expectations

Evidence types accepted for hazard mitigation closure (as applicable):
- analysis (e.g., stress/thermal, reliability, FTA cut sets),
- tests (component, rig, integration, environmental),
- inspection and maintenance procedure validation,
- operational monitoring / limits (where allowed),
- design reviews and sign-offs.

Each closed hazard SHALL have:
- evidence link(s),
- verifier (AoR),
- date/version,
- residual risk statement.

## 10. Reporting and Reviews

Minimum cadence (suggested):
- hazard log review: per major design iteration / baseline
- FHA/SSA refresh: when functional baseline or architecture changes
- interface safety review: at each ICD release
- pre-release safety readiness review: prior to any baseline tag

## 11. Open Items (to be instantiated)

- [TODO] Confirm certification basis amendments and applicable safety standard set
- [TODO] Confirm risk matrix scales and acceptance thresholds
- [TODO] Confirm authoritative ICD repository path(s)
- [TODO] Confirm naming rule for safety objectives file (00-002 vs 02-002)
- [TODO] Define zone map references for nacelle/pylon zoning
