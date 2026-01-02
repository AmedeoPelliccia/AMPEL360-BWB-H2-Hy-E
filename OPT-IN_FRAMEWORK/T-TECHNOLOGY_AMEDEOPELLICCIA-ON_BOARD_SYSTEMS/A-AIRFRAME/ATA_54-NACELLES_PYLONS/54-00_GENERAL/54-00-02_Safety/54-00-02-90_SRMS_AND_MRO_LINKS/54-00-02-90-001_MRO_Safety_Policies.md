---
document_id: "54-00-02-90-001"
ata: "54"
ata_title: "Nacelles / Pylons"
node: "54-00-02-90_SRMS_AND_MRO_LINKS"
title: "MRO Safety Policies"
project: "AMPEL360"
program: "AIR-T"
family: "Q100"
variant: "BWB"
phase: "LC02"
knot: "K07"
aor_owner: "STK_MRO"
aor_contributors: ["STK_SAF","STK_CERT","STK_CM"]
status: "DRAFT"
issue_rev: "I01-R01"
last_updated: "2026-01-01"
classification: "INTERNAL"
---

# 54-00-02-90-001 — MRO Safety Policies (ATA 54)

## 1. Purpose

Document **MRO (Maintenance, Repair, Overhaul) safety policies** for **ATA 54 (Nacelles / Pylons)** to ensure continued airworthiness and safe operation throughout the aircraft lifecycle.

## 2. Scope

These policies apply to:
- scheduled maintenance of nacelle/pylon structures and systems,
- unscheduled repairs,
- major modifications,
- component replacement,
- inspection programs.

## 3. Safety-Critical Maintenance Items

### 3.1 Critical Attachments

| Item | Inspection Requirement | Interval | Method |
|------|----------------------|----------|--------|
| Pylon-wing attachments | Visual + NDT | Per program | HFEC, visual |
| Nacelle-pylon attachments | Visual + NDT | Per program | HFEC, visual |
| Engine mounting fittings | Visual + NDT | Per program | HFEC, visual |
| Fail-safe members | Visual | Per program | Visual |

### 3.2 Safety-Critical Tasks

| Task Category | Description | Documentation |
|--------------|-------------|---------------|
| Torque verification | Critical fastener torque checks | AMM reference |
| Lockwire installation | Safety locking of critical fasteners | AMM reference |
| Sealant application | Fuel/fluid barrier sealing | AMM reference |
| Gap/clearance checks | Routing clearance verification | AMM reference |

## 4. Maintenance Error Prevention

### 4.1 Human Factors Considerations

| Risk Factor | Mitigation |
|-------------|------------|
| Incorrect torque | Calibrated tools, independent verification |
| Missing hardware | Procedural checklists, BUYBACK inspection |
| Wrong part installation | Part number verification, BUYBACK |
| Damage during maintenance | Ground support equipment controls, protection |

### 4.2 Critical Task Marking

Critical maintenance tasks SHALL be:
- marked as "CRITICAL" in AMM/SRM,
- subject to independent inspection (BUYBACK),
- documented with traceability to work order.

## 5. Repair Policies

### 5.1 Allowable Repairs

Repairs SHALL be performed per:
- Structural Repair Manual (SRM),
- Approved repair data (engineering disposition),
- Approved modification data.

### 5.2 Beyond SRM Repairs

Repairs beyond SRM limits require:
- engineering analysis,
- DER/ODA approval (as applicable),
- configuration control update.

## 6. Safety Reporting

### 6.1 Reportable Findings

The following SHALL be reported per safety reporting procedures:
- structural damage exceeding SRM limits,
- evidence of fatigue cracking,
- corrosion beyond allowable limits,
- evidence of overheat/fire damage,
- incorrect installation/assembly.

### 6.2 Reporting Path

Safety findings SHALL be reported to:
- STK_SAF (Safety owner),
- STK_CERT (if airworthiness-affecting),
- STK_CM (for configuration updates).

## 7. Traceability

MRO policies link to:
- Hazard log: [`../54-00-02-10_HAZARD_ANALYSIS/`](../54-00-02-10_HAZARD_ANALYSIS/00_INDEX.md)
- Safety requirements: [`../54-00-02-80_REQUIREMENTS_LINKS/`](../54-00-02-80_REQUIREMENTS_LINKS/00_INDEX.md)
- SRM reference map: [`54-00-02-90-002_SRM_Reference_Map.md`](54-00-02-90-002_SRM_Reference_Map.md)

## 8. Open Items / TODO

- [TODO] Confirm inspection intervals per program baseline.
- [TODO] Link to AMM/SRM task references when available.
- [TODO] Confirm reporting procedures and contacts.
