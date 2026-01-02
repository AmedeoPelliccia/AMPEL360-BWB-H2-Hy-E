---
document_id: "54-00-02-60-002"
ata: "54"
ata_title: "Nacelles / Pylons"
node: "54-00-02-60_COMMON_CAUSES"
title: "Shared Resources Map"
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

# 54-00-02-60-002 — Shared Resources Map (ATA 54)

## 1. Purpose

Document the **shared resources** within **ATA 54 (Nacelles / Pylons)** domains that could serve as common cause failure sources. This map supports Common Cause Analysis (CCA) by identifying where multiple systems or functions share physical, electrical, or logical resources.

## 2. Shared Resource Categories

### 2.1 Physical/Structural Resources

| Resource ID | Resource Type | Description | Shared By |
|-------------|--------------|-------------|-----------|
| SR-PHY-001 | Mounting structure | Pylon primary structure | Nacelle attachment, cable routing, line routing |
| SR-PHY-002 | Attachment hardware | Common fastener sets | Multiple structural joints |
| SR-PHY-003 | Thermal blankets | Shared thermal protection | Multiple systems in zone |
| SR-PHY-004 | Access panels | Common access provisions | Maintenance for multiple systems |

### 2.2 Electrical Resources

| Resource ID | Resource Type | Description | Shared By |
|-------------|--------------|-------------|-----------|
| SR-ELC-001 | Power bus | Shared electrical bus in pylon | Multiple electrical loads |
| SR-ELC-002 | Grounding path | Common grounding structure | All electrical systems |
| SR-ELC-003 | Cable tray | Shared cable routing path | Multiple cable runs |

### 2.3 Fluid Resources (if applicable)

| Resource ID | Resource Type | Description | Shared By |
|-------------|--------------|-------------|-----------|
| SR-FLD-001 | Drainage paths | Common drainage provisions | Multiple fluid systems |
| SR-FLD-002 | Venting paths | Shared venting volume | Multiple vented systems |

### 2.4 Environmental Resources

| Resource ID | Resource Type | Description | Shared By |
|-------------|--------------|-------------|-----------|
| SR-ENV-001 | Cooling airflow | Shared cooling path | Multiple heat-generating components |
| SR-ENV-002 | Zone atmosphere | Common zone environment | All equipment in zone |

## 3. Resource-to-Hazard Mapping

Each shared resource SHALL be assessed for potential to cause common mode failures. Mapping to hazard log:

| Resource ID | Potential Hazard | Hazard ID Reference |
|-------------|-----------------|---------------------|
| SR-PHY-001 | Structural failure affecting multiple routings | TBD (link to HID) |
| SR-ELC-001 | Power loss to multiple loads | TBD (link to HID) |
| SR-ENV-002 | Environmental degradation affecting multiple systems | TBD (link to HID) |

## 4. Interfaces

This map interfaces with:
- CCA document: [`54-00-02-60-001_Common_Cause_Analysis.md`](54-00-02-60-001_Common_Cause_Analysis.md)
- Zone definitions: [`../54-00-02-50_ZSA/54-00-02-50-002_Zone_Definitions.md`](../54-00-02-50_ZSA/54-00-02-50-002_Zone_Definitions.md)
- Interface safety notes: [`../54-00-02-70_INTERFACES_SAFETY/`](../54-00-02-70_INTERFACES_SAFETY/00_INDEX.md)

## 5. Open Items / TODO

- [TODO] Complete shared resource inventory per baseline configuration.
- [TODO] Map each resource to specific hazard IDs.
- [TODO] Assess segregation adequacy for shared resources.
