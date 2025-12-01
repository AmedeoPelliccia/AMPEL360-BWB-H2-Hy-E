# Propulsion System Architecture — Copilot Coding Agent Instructions

| Field | Value |
|-------|-------|
| **Document ID** | P-PROPULSION-INST-001 |
| **Version** | 1.0 |
| **Date** | 2025-12-01 |
| **Status** | DRAFT |
| **Classification** | TECHNICAL |
| **Owner** | AMPEL360 Propulsion WG |

---

## Purpose

This document provides coding agent instructions for the Propulsion (P) section of the OPT-IN Framework. It defines the high-level propulsion system architecture specifications for the AMPEL360 BWB hydrogen-hybrid electric aircraft.

## Propulsion System Specifications

```text
Architecture: Distributed Electric Propulsion
Power: 16 MW (4× 4 MW ducted fans)
Primary Energy: Liquid Hydrogen (LH₂) - 3,000 kg capacity
Fuel Cells: 20 MW PEM stacks
Batteries: 5 MWh lithium-ion
Backup Fuel: 500 L SAF (Sustainable Aviation Fuel)
```

## Scope

This instruction file applies to all ATA chapters under the P-PROPULSION axis:

- ATA 60 – Standard Practices Propulsion
- ATA 61 – Propellers/Propulsors
- ATA 70 – Standard Practices Engine
- ATA 71 – Power Plant
- ATA 72 – Engine
- ATA 73 – Engine Fuel Control
- ATA 74 – Ignition
- ATA 75 – Air
- ATA 76 – Engine Controls
- ATA 78 – Exhaust
- ATA 79 – Oil

## Cross-References

- [ATA 53-70 Propulsion Interfaces](../A-AIRFRAME/ATA_53-FUSELAGE/53-70_Propulsion/README.md) — Integration with airframe structures
- [ATA 28 Fuel/SAF/Cryogenic H₂](../C2-CIRCULAR_CRYOGENICS_SYSTEMS/ATA_28-FUEL_SAF_CRYOGENIC_H2/) — Fuel systems interface

---

## Document Control

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT** – Subject to human review and approval.
- Human approver: _[to be completed]_.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: 2025-12-01

---
