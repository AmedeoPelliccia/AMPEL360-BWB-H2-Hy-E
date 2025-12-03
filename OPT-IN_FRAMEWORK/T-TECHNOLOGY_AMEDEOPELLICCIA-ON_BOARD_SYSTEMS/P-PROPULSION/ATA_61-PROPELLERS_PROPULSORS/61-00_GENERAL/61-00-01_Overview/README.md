# 61-00-01_Overview

## Purpose

ATA domain description and global architecture for the AMPEL360 Q100 Electric Ducted Fan (EDF) propulsion system.

## Scope

This folder is part of the **61-00_GENERAL** layer, which provides governance and lifecycle management for ATA Chapter 61 — Propellers/Propulsors. It establishes the foundational understanding of the propulsor domain, architecture, terminology, and traceability to related systems.

## Contents

### Core Documentation

| Document ID | Title | Description |
|-------------|-------|-------------|
| [61-00-01-001](61-00-01-001_ATA_61_Domain_Description.md) | ATA 61 Domain Description | Defines scope, boundaries, and key concepts of the Propellers/Propulsors domain |
| [61-00-01-002](61-00-01-002_Global_Architecture.md) | Global Architecture | High-level architecture including H₂/hybrid-electric propulsion integration |
| [61-00-01-003](61-00-01-003_Terminology_Glossary.md) | Terminology Glossary | Standardized terms specific to ATA 61 within AMPEL360 context |
| [61-00-01-004](61-00-01-004_Traceability_Matrix.md) | Traceability Matrix | Links to lifecycle phases, related ATA chapters, and requirements |

### Key Highlights

- **Propulsion Type**: Distributed Electric Propulsion (DEP) with four Electric Ducted Fans
- **Power Source**: Hydrogen-electric (H₂ fuel cells or H₂ turbine generators)
- **Aircraft Configuration**: Blended Wing Body (BWB) with Boundary Layer Ingestion (BLI)

## Status

- **Phase**: Overview
- **Lifecycle Position**: 01 of 14
- **Status**: Active
- **Last Updated**: 2025-12-03

## Consistency Checklist

- [x] README follows canonical 14-folder structure
- [x] Domain description documentation added
- [x] Global architecture documentation added
- [x] Terminology glossary added
- [x] Traceability matrix created linking to 61-00-02_Safety
- [x] Links to related ATA chapters established

## Related Folders

### Next Lifecycle Phase

→ [61-00-02_Safety](../61-00-02_Safety/README.md) — Safety framework and analysis methods

### Lifecycle Sequence

Part of the canonical 14-folder lifecycle:

1. **Overview** (current) → 2. Safety → 3. Requirements → 4. Design → 5. Interfaces → 6. Engineering → 7. V&V → 8. Prototyping → 9. Production Planning → 10. Certification → 11. EIS/Versions/Tags → 12. Services → 13. Subsystems/Components → 14. Ops/Std/Sustain

### Related ATA Chapters

| ATA | Description | Relationship |
|-----|-------------|--------------|
| [ATA 24](../../../../E2-ENERGY/ATA_24-ELECTRICAL_POWER/) | Electrical Power | Power supply to propulsors |
| [ATA 28](../../../../C2-CIRCULAR_CRYOGENICS_SYSTEMS/ATA_28-FUEL_SAF_CRYOGENIC_H2/) | Fuel (SAF & Cryogenic H₂) | H₂ thermal interface, fuel for power generation |
| [ATA 54](../../../../A-AIRFRAME/ATA_54-NACELLES_PYLONS/) | Nacelles/Pylons | Structural mounting, aerodynamic integration |
| [ATA 71](../../ATA_71-POWER_PLANT/) | Power Plant | Overall propulsion system integration |
| [ATA 76](../../ATA_76-ENGINE_CONTROLS/) | Engine Controls | Control system integration |

---

## Document Control

- **Standard**: OPT-IN Framework v1.1 (ATA 95 canonical template)
- **Owner**: AMPEL360 Documentation WG
- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT** – Subject to human review and approval.
- Human approver: _[to be completed]_.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: _2025-12-03_.

---
