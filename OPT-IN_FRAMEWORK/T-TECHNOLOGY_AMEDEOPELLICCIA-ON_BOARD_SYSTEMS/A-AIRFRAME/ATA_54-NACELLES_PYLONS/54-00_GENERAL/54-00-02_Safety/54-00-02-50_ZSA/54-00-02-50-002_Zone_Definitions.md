---
document_id: "54-00-02-50-002"
ata: "54"
ata_title: "Nacelles / Pylons"
node: "54-00-02-50_ZSA"
title: "Zone Definitions"
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

# 54-00-02-50-002 — Zone Definitions (ATA 54)

## 1. Purpose

Define the **zone structure** for **ATA 54 (Nacelles / Pylons)** to support Zonal Safety Analysis (ZSA). This document establishes zone boundaries, identifiers, and environmental characterization.

## 2. Zone Map Overview

Nacelle/pylon zones are defined based on:
- physical compartmentalization,
- environmental conditions,
- installed equipment categories,
- maintenance access requirements.

## 3. Zone Definitions

### 3.1 Preliminary Zone Structure

| Zone ID | Zone Name | Description | Environmental Conditions |
|---------|-----------|-------------|-------------------------|
| Z54-001 | Nacelle Forward Section | Forward cowl area, inlet region | Moderate temp, external exposure |
| Z54-002 | Nacelle Core Section | Engine/propulsor mounting area | High temp, vibration |
| Z54-003 | Nacelle Aft Section | Exhaust/thrust reverser area (if applicable) | High temp, thermal cycling |
| Z54-010 | Pylon Upper Section | Upper pylon structure, wing interface | Moderate temp, structural loads |
| Z54-011 | Pylon Lower Section | Lower pylon structure, nacelle interface | Moderate-high temp, vibration |
| Z54-020 | Pylon Routing Bay | Cable/line routing volume within pylon | Controlled environment, segregation critical |

### 3.2 Environmental Conditions Key

| Condition | Description |
|-----------|-------------|
| High temp | Operating temperatures exceeding 100°C; thermal protection required |
| Moderate temp | Operating temperatures 0–100°C; standard materials acceptable |
| External exposure | Subject to external atmosphere, moisture, icing |
| Vibration | Subject to engine/propulsor-induced vibration; fatigue considerations |
| Segregation critical | Multiple system routings present; segregation rules apply |

## 4. Zone-Specific Considerations

### 4.1 Fire Zones (if applicable)

Fire zones within nacelle volumes SHALL be defined per [ATA 26](../54-00-02-70_INTERFACES_SAFETY/54-00-02-70-003_ATA26_Impact.md) coordination and regulatory requirements.

### 4.2 Access Provisions

Each zone SHALL have defined access provisions for:
- scheduled inspection,
- unscheduled maintenance,
- emergency egress (for occupied volumes, if any).

## 5. Traceability

Zone definitions feed:
- ZSA analysis documents in `ZONE_ANALYSIS/`,
- interface impact notes in `../54-00-02-70_INTERFACES_SAFETY/`,
- SRM/MRO considerations in `../54-00-02-90_SRMS_AND_MRO_LINKS/`.

## 6. Open Items / TODO

- [TODO] Finalize zone boundaries per aircraft configuration baseline.
- [TODO] Confirm fire zone designations with ATA 26 owner.
- [TODO] Add zone diagram references when available.
