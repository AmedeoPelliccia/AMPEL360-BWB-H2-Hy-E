---
document_id: "54-00-02-80-002"
ata: "54"
ata_title: "Nacelles / Pylons"
node: "54-00-02-80_REQUIREMENTS_LINKS"
title: "Safety Requirements Index"
project: "AMPEL360"
program: "AIR-T"
family: "Q100"
variant: "BWB"
phase: "LC02"
knot: "K07"
aor_owner: "STK_SAF"
aor_contributors: ["STK_CERT","STK_SE","STK_CM"]
status: "DRAFT"
issue_rev: "I01-R01"
last_updated: "2026-01-01"
classification: "INTERNAL"
---

# 54-00-02-80-002 — Safety Requirements Index (ATA 54)

## 1. Purpose

Provide an index of **safety-derived requirements** for **ATA 54 (Nacelles / Pylons)** for AMPEL360 AIR-T. These requirements are derived from safety analyses (FHA, SSA, FTA, ZSA, CCA) and interface impact assessments.

## 2. Requirement Naming Convention

Safety requirements for ATA 54 follow the pattern:
```
SAF-54-XXX-YYY
```
Where:
- `SAF` = Safety requirement prefix
- `54` = ATA chapter
- `XXX` = Category code (see below)
- `YYY` = Sequential number

### Category Codes

| Code | Category |
|------|----------|
| STR | Structural safety |
| THR | Thermal / fire safety |
| ELC | Electrical safety |
| FLD | Fluid safety |
| ICE | Ice protection safety |
| MNT | Maintenance safety |
| INT | Interface safety |

## 3. Safety Requirements Index

### 3.1 Structural Safety Requirements

| Req ID | Requirement | Source | Hazard Ref |
|--------|-------------|--------|------------|
| SAF-54-STR-001 | Nacelle/pylon attachment SHALL be designed for fail-safe operation | CS-25.571, ATA54-FH-001 | ATA54-FH-001 |
| SAF-54-STR-002 | Structural joints SHALL maintain integrity under fatigue loads | CS-25.571, ATA54-FH-002 | ATA54-FH-002 |
| SAF-54-STR-003 | Damage tolerance SHALL be demonstrated for critical structure | CS-25.571, ATA54-FH-004 | ATA54-FH-004 |

### 3.2 Thermal / Fire Safety Requirements

| Req ID | Requirement | Source | Hazard Ref |
|--------|-------------|--------|------------|
| SAF-54-THR-001 | Fire zones SHALL be defined per CS-25.1181 | CS-25.1181, ATA54-FH-010 | ATA54-FH-010 |
| SAF-54-THR-002 | Thermal insulation SHALL prevent surface temperatures exceeding limits | ATA54-FH-011 | ATA54-FH-011 |

### 3.3 Electrical Safety Requirements

| Req ID | Requirement | Source | Hazard Ref |
|--------|-------------|--------|------------|
| SAF-54-ELC-001 | Electrical routing SHALL be segregated from flammable fluids | ATA54-FH-020 | ATA54-FH-020 |
| SAF-54-ELC-002 | Cable installations SHALL prevent chafing | ATA54-FH-022 | ATA54-FH-022 |

### 3.4 Fluid Safety Requirements

| Req ID | Requirement | Source | Hazard Ref |
|--------|-------------|--------|------------|
| SAF-54-FLD-001 | Fuel line routing SHALL include leak detection | ATA54-FH-012 | ATA54-FH-012 |
| SAF-54-FLD-002 | Drainage SHALL prevent fluid accumulation | ATA54-FH-013 | ATA54-FH-013 |

### 3.5 Ice Protection Safety Requirements

| Req ID | Requirement | Source | Hazard Ref |
|--------|-------------|--------|------------|
| SAF-54-ICE-001 | Ice protection SHALL prevent hazardous accumulation | CS-25.1419, ATA54-FH-030 | ATA54-FH-030 |

### 3.6 Maintenance Safety Requirements

| Req ID | Requirement | Source | Hazard Ref |
|--------|-------------|--------|------------|
| SAF-54-MNT-001 | Critical attachments SHALL be accessible for inspection | ATA54-FH-041 | ATA54-FH-041 |
| SAF-54-MNT-002 | Maintenance procedures SHALL prevent incorrect installation | ATA54-FH-040 | ATA54-FH-040 |

## 4. Traceability

Requirements in this index are traced in:
- [`54-00-02-80-003_Traceability_Matrix.md`](54-00-02-80-003_Traceability_Matrix.md)

## 5. Open Items / TODO

- [TODO] Complete requirement derivation for all identified hazards.
- [TODO] Assign verification methods to each requirement.
- [TODO] Link requirements to design artifacts.
