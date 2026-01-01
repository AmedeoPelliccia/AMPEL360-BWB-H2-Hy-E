---
document_id: "54-00-02-90-002"
ata: "54"
ata_title: "Nacelles / Pylons"
node: "54-00-02-90_SRMS_AND_MRO_LINKS"
title: "SRM Reference Map"
project: "AMPEL360"
program: "AIR-T"
family: "Q100"
variant: "BWB"
phase: "LC02"
knot: "K07"
aor_owner: "STK_MRO"
aor_contributors: ["STK_SAF","STK_SE","STK_CM"]
status: "DRAFT"
issue_rev: "I01-R01"
last_updated: "2026-01-01"
classification: "INTERNAL"
---

# 54-00-02-90-002 — SRM Reference Map (ATA 54)

## 1. Purpose

Provide a **reference map** linking **safety-critical items** from **ATA 54 (Nacelles / Pylons)** safety analyses to their corresponding **Structural Repair Manual (SRM)** sections.

## 2. SRM Structure Overview

The SRM for ATA 54 is organized as:
- Chapter 54-00: General
- Chapter 54-10: Cowling
- Chapter 54-20: Pylon/Strut Structure
- Chapter 54-30: Attachments
- Chapter 54-40: Fairings
- Chapter 54-50: Nacelle Structure

## 3. Safety Item to SRM Mapping

### 3.1 Critical Structural Items

| Safety Item | Hazard Ref | SRM Section | Repair Category |
|-------------|------------|-------------|-----------------|
| Pylon primary structure | ATA54-FH-001, ATA54-FH-002 | 54-20-XX | Major repair |
| Pylon-wing attachment | ATA54-FH-001, ATA54-FH-003 | 54-30-XX | Major repair |
| Nacelle-pylon attachment | ATA54-FH-001, ATA54-FH-003 | 54-30-XX | Major repair |
| Engine mounting fittings | ATA54-FH-001 | 54-30-XX | Major repair |
| Fail-safe members | ATA54-FH-004 | 54-20-XX | Major repair |

### 3.2 Thermal/Fire Protection Items

| Safety Item | Hazard Ref | SRM Section | Repair Category |
|-------------|------------|-------------|-----------------|
| Thermal blankets | ATA54-FH-011 | 54-XX-XX | Minor repair |
| Fire barriers | ATA54-FH-010 | 54-XX-XX | Minor repair |
| Firewall penetrations | ATA54-FH-010 | 54-XX-XX | Minor repair |

### 3.3 Routing/Segregation Items

| Safety Item | Hazard Ref | SRM Section | Repair Category |
|-------------|------------|-------------|-----------------|
| Cable clamps/supports | ATA54-FH-022 | 54-XX-XX | Minor repair |
| Line clamps/supports | ATA54-FH-012 | 54-XX-XX | Minor repair |
| Segregation barriers | ATA54-FH-021 | 54-XX-XX | Minor repair |

## 4. Damage Limits Reference

### 4.1 Structural Damage Limits

| Structure | Damage Type | Allowable Limit | SRM Reference |
|-----------|-------------|-----------------|---------------|
| Pylon skin | Dent | TBD depth/area | 54-20-XX |
| Pylon skin | Scratch | TBD depth | 54-20-XX |
| Pylon skin | Corrosion | TBD depth | 54-20-XX |
| Attachment fitting | Crack | None allowable | 54-30-XX |
| Attachment fitting | Corrosion | TBD | 54-30-XX |

### 4.2 Beyond Limits Actions

When damage exceeds SRM limits:
1. Report to engineering per MRO safety policies,
2. Obtain approved repair data,
3. Perform repair per approved data,
4. Update configuration records.

## 5. Inspection Interval Links

| Inspection Type | Interval | SRM Reference | Hazard Ref |
|----------------|----------|---------------|------------|
| Visual inspection | Per program | 54-XX-XX | ATA54-FH-002, ATA54-FH-031 |
| NDT (HFEC) | Per program | 54-XX-XX | ATA54-FH-002, ATA54-FH-004 |
| Detailed inspection | Per program | 54-XX-XX | ATA54-FH-041 |

## 6. Traceability

SRM references link to:
- Hazard log: [`../54-00-02-10_HAZARD_ANALYSIS/`](../54-00-02-10_HAZARD_ANALYSIS/00_INDEX.md)
- Safety requirements: [`../54-00-02-80_REQUIREMENTS_LINKS/`](../54-00-02-80_REQUIREMENTS_LINKS/00_INDEX.md)
- MRO policies: [`54-00-02-90-001_MRO_Safety_Policies.md`](54-00-02-90-001_MRO_Safety_Policies.md)

## 7. Open Items / TODO

- [TODO] Complete SRM section references when SRM is developed.
- [TODO] Confirm damage limits per structural analysis.
- [TODO] Link to actual SRM document when available.
