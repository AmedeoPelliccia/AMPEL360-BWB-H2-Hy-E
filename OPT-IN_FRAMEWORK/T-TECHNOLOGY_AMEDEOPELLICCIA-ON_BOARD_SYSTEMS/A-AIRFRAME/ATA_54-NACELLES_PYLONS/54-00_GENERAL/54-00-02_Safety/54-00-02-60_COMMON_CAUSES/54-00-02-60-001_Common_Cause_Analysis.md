---
document_id: "54-00-02-60-001"
ata: "54"
ata_title: "Nacelles / Pylons"
node: "54-00-02-60_COMMON_CAUSES"
title: "Common Cause Analysis"
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
last_updated: "2026-01-01"
classification: "INTERNAL"
---

# 54-00-02-60-001 — Common Cause Analysis (ATA 54)

## 1. Purpose

Document the **Common Cause Analysis (CCA)** for **ATA 54 (Nacelles / Pylons)** to identify failure modes that could affect multiple systems or redundant functions simultaneously, defeating independence assumptions in safety assessments.

## 2. Scope

CCA for ATA 54 addresses:
- common environmental exposures within nacelle/pylon zones,
- shared design features or manufacturing processes,
- shared maintenance/inspection errors,
- common software/hardware elements (if applicable),
- cascading failures between coupled systems.

## 3. CCA Categories

### 3.1 Environmental Common Causes

| ID | Category | Example Failure Mode | Affected Systems |
|----|----------|---------------------|------------------|
| CC-ENV-001 | Thermal overheat | Excessive temperature in nacelle zone | ATA 24, ATA 28, ATA 71/72 |
| CC-ENV-002 | Fire/smoke | Uncontrolled fire in nacelle volume | All systems in zone |
| CC-ENV-003 | Fluid contamination | Fuel/hydraulic leak affecting multiple routings | ATA 28, ATA 24, ATA 54 structures |
| CC-ENV-004 | Icing | Ice accretion affecting multiple surfaces/inlets | ATA 30, ATA 71/72 |
| CC-ENV-005 | Vibration | Excessive vibration from propulsor | All routed items in zone |

### 3.2 Design/Manufacturing Common Causes

| ID | Category | Example Failure Mode | Affected Systems |
|----|----------|---------------------|------------------|
| CC-DES-001 | Common material | Batch defect in structural material | All components using material |
| CC-DES-002 | Common supplier | Supplier quality issue | All components from supplier |
| CC-DES-003 | Common fastener | Fastener batch defect | All joints using fastener type |

### 3.3 Maintenance/Operational Common Causes

| ID | Category | Example Failure Mode | Affected Systems |
|----|----------|---------------------|------------------|
| CC-MNT-001 | Maintenance error | Incorrect torque applied to multiple fittings | All fittings in task |
| CC-MNT-002 | Inspection miss | Undetected damage in multiple locations | All inspected areas |
| CC-MNT-003 | Operational abuse | Out-of-envelope operation | All systems exposed |

## 4. CCA Methodology

### 4.1 Approach

1. Identify redundant or independent functions from SSA/FTA.
2. For each pair of independent functions, assess potential common causes.
3. Evaluate likelihood and consequences of common cause failure.
4. Identify design/procedural mitigations.
5. Link findings to hazard log and safety requirements.

### 4.2 Tools and References

- ARP4761 / ED-135: Common cause analysis guidance
- Zonal Safety Analysis: [`../54-00-02-50_ZSA/`](../54-00-02-50_ZSA/00_INDEX.md)
- Shared Resources Map: [`54-00-02-60-002_Shared_Resources_Map.md`](54-00-02-60-002_Shared_Resources_Map.md)

## 5. Traceability

CCA findings SHALL:
- reference hazards by HID from `../54-00-02-10_HAZARD_ANALYSIS/HAZARD_LOGS/54-00-02-10-001_Hazard_Log_Master.csv`,
- link to safety requirements in `../54-00-02-80_REQUIREMENTS_LINKS/`,
- feed interface impact notes in `../54-00-02-70_INTERFACES_SAFETY/`.

## 6. Open Items / TODO

- [TODO] Complete CCA for each identified redundant function pair.
- [TODO] Confirm mitigation adequacy for each common cause category.
- [TODO] Link CCA findings to SSA/FTA artifacts.
