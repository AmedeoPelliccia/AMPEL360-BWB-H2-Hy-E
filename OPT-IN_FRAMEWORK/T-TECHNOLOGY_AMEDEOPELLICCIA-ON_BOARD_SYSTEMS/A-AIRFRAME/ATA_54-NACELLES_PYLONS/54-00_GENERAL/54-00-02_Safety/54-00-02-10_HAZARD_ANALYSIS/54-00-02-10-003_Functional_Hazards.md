---
document_id: "54-00-02-10-003"
ata: "54"
ata_title: "Nacelles / Pylons"
node: "54-00-02-10_HAZARD_ANALYSIS"
title: "Functional Hazards"
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

# 54-00-02-10-003 — Functional Hazards (ATA 54)

## 1. Purpose

Identify and structure the **functional hazards** for **ATA 54 (Nacelles / Pylons)**. This document:
- defines the functional boundary for ATA 54 in the program architecture,
- enumerates candidate hazardous failure conditions at functional level,
- provides the mapping rules from functions → hazards → hazard log entries (HIDs),
- seeds FHA/SSA/FTA and interface safety nodes.

This document is a **hazard discovery artifact**; the authoritative hazard set is maintained in the hazard log master.

## 2. Scope and System Boundary

### 2.1 In-scope (ATA 54 boundary)

ATA 54 hazards cover functions and failures related to:
- nacelle/pylon structural integration and load transfer,
- attachment and mounting integrity (joints, lugs, fittings),
- zone/environment conditions affecting nacelle/pylon safety (temperature, fluids, contamination),
- routing and segregation affecting nacelle/pylon safety (cables, lines, thermal blankets),
- inspection/maintenance access features that influence safe continued airworthiness,
- interfaces crossing into coupled systems (ATA 24/26/28/30/51/71/72 etc.).

### 2.2 Out-of-scope (referenced)

Subsystem-internal hazards are owned by their ATA chapters and referenced via interface impacts. Examples:
- engine internal hazards (ATA 72),
- full aircraft electrical architecture hazards (ATA 24),
- primary structure hazards outside nacelle/pylon attachments (ATA 51/57).

## 3. Functional Decomposition (ATA 54)

Use this minimal function set as the baseline; extend per architecture.

| Function ID | Function | Notes / Interfaces |
|------------|----------|--------------------|
| ATA54-FN-01 | Provide structural support for nacelle/propulsor assembly | Interfaces: ATA51/71/72 |
| ATA54-FN-02 | Transfer loads safely into primary structure | Interfaces: ATA51 |
| ATA54-FN-03 | Maintain attachment integrity under all approved envelopes | Fatigue/damage tolerance assumptions |
| ATA54-FN-04 | Maintain safe zone environment (thermal, contamination) | Interfaces: ATA21/26/28/30 |
| ATA54-FN-05 | Ensure segregation/protection of routed items in nacelle/pylon zones | Interfaces: ATA24/28/30 |
| ATA54-FN-06 | Support inspectability and maintainability of critical features | Interfaces: SRM/MRO |

## 4. Functional Hazard Set (Candidate List)

Each hazard below MUST be instantiated as a hazard log entry (HID) if applicable to the baseline.

### 4.1 Structural / Attachment hazards

| Candidate ID | Hazardous Failure Condition | Potential Effects | Primary Interfaces |
|--------------|-----------------------------|------------------|-------------------|
| ATA54-FH-001 | Loss of nacelle/pylon structural integrity | Separation, loss of propulsion integration, aircraft-level hazard | ATA51, ATA71/72 |
| ATA54-FH-002 | Degraded load transfer capability (crack, looseness, deformation) | Progressive structural failure, vibration, secondary damage | ATA51, ATA71/72 |
| ATA54-FH-003 | Attachment/joint failure (fastener, lug, fitting) | Partial/complete separation, misalignment, damage propagation | ATA51 |
| ATA54-FH-004 | Loss of fail-safe feature / damage tolerance margin | Undetected progression to catastrophic condition | ATA51, MRO |
| ATA54-FH-005 | Uncontrolled resonance/vibration due to structural degradation | Accelerated fatigue, routed line damage, loosening | ATA71/72, ATA24 |

### 4.2 Thermal / Fire / Fluid-related hazards (as applicable)

| Candidate ID | Hazardous Failure Condition | Potential Effects | Primary Interfaces |
|--------------|-----------------------------|------------------|-------------------|
| ATA54-FH-010 | Overheat in nacelle/pylon zones | Material degradation, ignition source creation | ATA26, ATA30 |
| ATA54-FH-011 | Thermal insulation failure leading to hot surface exposure | Fire risk, component overheating, maintenance hazard | ATA26 |
| ATA54-FH-012 | Fluid leak affecting nacelle/pylon environment (fuel/H₂/other) | Fire, contamination, structural degradation | ATA28, ATA26 |
| ATA54-FH-013 | Inadequate drainage/venting leading to accumulation | Increased ignition likelihood, corrosion | ATA28, ATA26 |

### 4.3 Electrical / routing / segregation hazards

| Candidate ID | Hazardous Failure Condition | Potential Effects | Primary Interfaces |
|--------------|-----------------------------|------------------|-------------------|
| ATA54-FH-020 | Electrical arcing/short in nacelle/pylon zones | Fire, loss of power to essential loads, ignition | ATA24, ATA26 |
| ATA54-FH-021 | Inadequate segregation of routed items (power vs fluid vs thermal) | Common cause failures, cascading effects | ATA24, ATA28, ATA30 |
| ATA54-FH-022 | Chafing/abrasion of harnesses/lines due to structural features | Loss of function, leak, short, smoke | ATA24, ATA28 |

### 4.4 Icing / environmental exposure hazards (as applicable)

| Candidate ID | Hazardous Failure Condition | Potential Effects | Primary Interfaces |
|--------------|-----------------------------|------------------|-------------------|
| ATA54-FH-030 | Ice accretion affecting nacelle/pylon features | Load anomalies, vibration, structural exceedance | ATA30 |
| ATA54-FH-031 | Corrosion/contamination in critical attachments | Loss of margins, inspection issues | MRO, ATA51 |

### 4.5 Maintenance / human factors hazards

| Candidate ID | Hazardous Failure Condition | Potential Effects | Primary Interfaces |
|--------------|-----------------------------|------------------|-------------------|
| ATA54-FH-040 | Maintenance error on critical attachment (wrong torque, missing lock) | Latent failure leading to separation | MRO, SRM |
| ATA54-FH-041 | Inadequate inspection access leading to missed damage | Undetected progression to hazardous condition | MRO |
| ATA54-FH-042 | Incorrect installation/configuration after repair/modification | Structural misalignment, overload, chafing | CM, MRO |

## 5. Mapping Rules to Hazard Log

### 5.1 Authority

All accepted hazards SHALL be recorded in:
- `HAZARD_LOGS/54-00-02-10-001_Hazard_Log_Master.csv`

### 5.2 Minimum mapping fields

For each candidate hazard that applies, the hazard log entry MUST include:
- stable hazard_id (HID)
- hazard title (per taxonomy naming rules)
- linked function(s) (ATA54-FN-xx)
- linked candidate hazard (ATA54-FH-xxx) for provenance
- severity/likelihood terms (per classification policy)
- interfaces (coupled ATA tags)
- proposed mitigations and verification approach

## 6. Outputs and Downstream Consumers

This document feeds:
- FHA methodology and case list (`../54-00-02-20_FHA/`)
- SSA strategy and models (`../54-00-02-30_SSA/`)
- FTA top events and cut sets (`../54-00-02-40_FTA/`)
- ZSA (zone-driven hazards) (`../54-00-02-50_ZSA/`)
- Common cause analysis (`../54-00-02-60_COMMON_CAUSES/`)
- Interface impact notes (`../54-00-02-70_INTERFACES_SAFETY/`)
- Safety requirements and traceability (`../54-00-02-80_REQUIREMENTS_LINKS/`)

## 7. Open Items / TODO

- [TODO] Confirm architecture baseline assumptions (propulsor type, routing, zone definitions).
- [TODO] Instantiate HID mapping for applicable hazards and link to hazard log entries.
- [TODO] Add program-specific severity/likelihood scoring references once defined.
- [TODO] Add explicit interface ICD links once ICDs exist.
