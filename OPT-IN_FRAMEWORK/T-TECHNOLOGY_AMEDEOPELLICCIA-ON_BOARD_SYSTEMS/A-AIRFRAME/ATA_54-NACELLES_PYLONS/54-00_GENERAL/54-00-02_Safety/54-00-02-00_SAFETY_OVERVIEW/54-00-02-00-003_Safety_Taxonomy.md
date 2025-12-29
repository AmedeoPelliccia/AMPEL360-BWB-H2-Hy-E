---
document_id: "54-00-02-00-003"
ata: "54"
ata_title: "Nacelles / Pylons"
node: "54-00-02-00_SAFETY_OVERVIEW"
title: "Safety Taxonomy"
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

# 54-00-02-00-003 — Safety Taxonomy (ATA 54)

## 1. Purpose

Define the **controlled safety taxonomy** used by **ATA 54 (Nacelles / Pylons)** artifacts, ensuring consistent:
- hazard naming and identifiers,
- failure condition categorization,
- severity/likelihood terminology alignment,
- interface hazard tagging (coupled ATA),
- traceability labels for requirements and evidence.

This taxonomy is normative for:
- Hazard Analysis (`54-00-02-10_*`)
- FHA / SSA / FTA (`54-00-02-20_*`, `54-00-02-30_*`, `54-00-02-40_*`)
- ZSA / Common Cause (`54-00-02-50_*`, `54-00-02-60_*`)
- Interfaces and traceability nodes (`54-00-02-70_*`, `54-00-02-80_*`, `54-00-02-90_*`)

## 2. Taxonomy Layers (Canonical Model)

### 2.1 Entity taxonomy (what the hazard is about)

ATA 54 hazards SHALL be tagged with one or more **Entity Types**:

- `STRUCTURE` — pylon/nacelle structure, fittings, load paths
- `ATTACHMENT` — mounts, bolts, lugs, joints, fail-safe features
- `THERMAL` — temperatures, heat flux, insulation, hot surfaces
- `ELECTRICAL` — wiring, power distribution, arcing, insulation breakdown
- `FLUID` — fuel/H₂/air/oil/hydraulics interfaces (as applicable)
- `FIRE` — ignition, propagation, detection/suppression (as applicable)
- `ICE_RAIN` — icing/anti-ice interactions (as applicable)
- `MAINTENANCE` — inspection access, task execution, human factors
- `INTERFACE` — cross-ATA boundary conditions and constraints

### 2.2 Failure condition taxonomy (how it fails)

Failure conditions SHALL be classified using controlled **Failure Condition Types**:

- `LOSS_OF_FUNCTION` — inability to perform intended function
- `DEGRADED_FUNCTION` — reduced capability, out-of-limit performance
- `UNCOMMANDED_EVENT` — unintended deployment/movement/energization
- `LEAK_OR_RELEASE` — fluid release, venting, leak (as applicable)
- `OVERHEAT` — thermal exceedance, insulation failure
- `SHORT_OR_ARC` — electrical fault modes
- `FIRE_OR_SMOKE` — fire/smoke/overheat with ignition (as applicable)
- `STRUCTURAL_FAILURE` — crack, fracture, deformation, separation
- `CASCADING_FAILURE` — propagation into other systems
- `MAINT_ERROR` — maintenance-induced latent or active failure
- `ENVIRONMENTAL_EXPOSURE` — corrosion, salt, sand, lightning, etc.

### 2.3 Hazard effect taxonomy (impact domain)

Effects SHALL be tagged using **Effect Domains**:

- `AIRCRAFT_LEVEL` — aircraft integrity, controllability, performance
- `PROPULSION_INTEGRATION` — impacts to engines/propulsors (ATA 71/72)
- `ELECTRICAL_POWER` — impacts to ATA 24 supply/protection
- `FUEL_H2` — impacts to ATA 28 (as applicable)
- `FIRE_PROTECTION` — impacts to ATA 26 (as applicable)
- `STRUCTURES` — impacts to ATA 51/57 structural integrity
- `MAINTAINABILITY` — inspection intervals, access constraints, task safety
- `CERTIFICATION` — compliance basis impact or MoC changes

### 2.4 Interface taxonomy (where it couples)

Interfaces SHALL be tagged with **Coupled ATA** codes when applicable:

`ATA24`, `ATA26`, `ATA28`, `ATA30`, `ATA51`, `ATA57`, `ATA71`, `ATA72`

(Extend only by adding new controlled values.)

## 3. Controlled Identifiers

### 3.1 Hazard IDs (HID)

All hazards SHALL have stable IDs in the hazard log master.

Recommended canonical form (stable and sortable):

`ATA54-HID-<NNNN>`

Example:
- `ATA54-HID-0007`

The authoritative list is in:
- `../54-00-02-10_HAZARD_ANALYSIS/HAZARD_LOGS/54-00-02-10-001_Hazard_Log_Master.csv`

### 3.2 Objective IDs (SO)

Objectives SHALL be identified as:

`ATA54-SO-<NNN>`

(Defined in `54-00-02-00-002_Safety_Objectives.md`.)

### 3.3 Safety Requirement IDs (SR)

Safety-derived requirements SHALL be identified as:

`ATA54-SR-<NNNN>`

Registered in:
- `../54-00-02-80_REQUIREMENTS_LINKS/54-00-02-80-002_Safety_Requirements_Index.md`

### 3.4 Evidence IDs (EVID)

Evidence artifacts SHOULD carry an evidence identifier:

`ATA54-EVID-<NNNN>`

and MUST be linked in the trace matrix:
- `../54-00-02-80_REQUIREMENTS_LINKS/54-00-02-80-003_Traceability_Matrix.md`

## 4. Severity and Likelihood Vocabulary

This document defines the **vocabulary**, not the numeric policy. The numeric policy and thresholds are in:
- `../54-00-02-10_HAZARD_ANALYSIS/54-00-02-10-004_Hazard_Classification.md`

### 4.1 Severity terms (controlled)

Use one of the following (program mapping to CS-25/ARP4761 policy TBD):

- `CATASTROPHIC`
- `HAZARDOUS`
- `MAJOR`
- `MINOR`
- `NO_SAFETY_EFFECT`

### 4.2 Likelihood terms (controlled)

Use one of the following:

- `FREQUENT`
- `PROBABLE`
- `REMOTE`
- `EXTREMELY_REMOTE`
- `EXTREMELY_IMPROBABLE`

### 4.3 Risk statement terms

- `UNACCEPTABLE` — must be mitigated
- `TOLERABLE_WITH_MITIGATION` — acceptable only with verified controls
- `ACCEPTABLE` — meets threshold with evidence

## 5. Hazard Naming Rules (Text Fields)

### 5.1 Hazard title pattern

Use clear, concise, and testable titles:

`<Failure Condition> leading to <Effect> under <Context>`

Examples:
- `STRUCTURAL_FAILURE leading to NACELLE_SEPARATION under TAKEOFF_LOADS`
- `OVERHEAT leading to MATERIAL_DEGRADATION under CONTINUOUS_HIGH_POWER`

### 5.2 Avoid ambiguous language

Avoid:
- “may”, “could”, “possibly” in titles  
Place uncertainty in a dedicated notes/assumptions field.

## 6. Tagging Rules (Mandatory Fields)

For each hazard entry (minimum taxonomy tagging):

- `hazard_id` (HID)
- `entity_type` (one or more)
- `failure_condition_type` (one or more)
- `effect_domain` (one or more)
- `coupled_ata` (zero or more)
- `severity_term` (controlled)
- `likelihood_term` (controlled)
- `risk_state` (controlled)
- `linked_objectives` (SO IDs)
- `linked_requirements` (SR IDs, once derived)
- `linked_evidence` (EVID IDs / artifact references)

## 7. Common Cause and Zonal Taxonomy

### 7.1 Common cause categories (CCA)

- `PHYSICAL_PROXIMITY`
- `SHARED_RESOURCE`
- `ENVIRONMENTAL`
- `MAINTENANCE_INDUCED`
- `LATENT_DESIGN_ERROR`
- `SOFTWARE_OR_CONTROL_COMMON_MODE` (only if applicable to ATA 54 interfaces)

### 7.2 Zonal taxonomy (ZSA)

Zones SHALL be identified with:
- `ZONE_ID` (program-defined)
- `BOUNDARY_DESCRIPTION`
- `ACCESS_CLASS` (e.g., `ROUTINE`, `LIMITED`, `RESTRICTED`)
- `PRIMARY_HAZARDS` (HIDs)

## 8. Traceability Taxonomy (Link Types)

Use controlled link types in matrices and cross-references:

- `DERIVES` (Objective → Requirement)
- `MITIGATES` (Requirement/Control → Hazard)
- `VERIFIES` (Test/Analysis → Requirement)
- `EVIDENCES` (Artifact → Hazard closure)
- `IMPACTS` (Interface note → Hazard/Requirement)
- `SUPPORTS` (Doc → Doc linkage)

## 9. Change Control

Taxonomy changes are high-impact and MUST:
- be reviewed by STK_SAF and STK_CERT,
- include migration guidance (e.g., mapping old tags to new tags),
- avoid breaking stable IDs.

## 10. Open Items / TODO

- [TODO] Instantiate numeric risk matrix and thresholds in `54-00-02-10-004_Hazard_Classification.md`
- [TODO] Confirm coupled ATA list for current baseline architecture
- [TODO] Confirm zone identifiers and access classes for nacelle/pylon zones
- [TODO] Align severity/likelihood wording to certification basis references list
