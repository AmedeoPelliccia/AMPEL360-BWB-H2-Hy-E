# Q100-61-INST-DEF-CONTROLLER-TO-NACELLE — Controller to Nacelle Installation Definition

## Overview

This definition specifies the interface and mounting requirements for installing the motor controller (inverter) within the nacelle structure. This installation requires careful thermal management due to power electronics heat dissipation.

## Scope

- Controller mounting provisions
- Thermal management interface
- Power and signal connections
- EMI shielding requirements
- Maintenance access

## Key Interfaces

| Interface | Type | Description |
|-----------|------|-------------|
| Mounting Rails | Mechanical | Slide-in mounting system |
| Heat Sink | Thermal | Cold plate cooling interface |
| DC Power Input | Electrical | From H₂ FC and CO₂ battery |
| AC Power Output | Electrical | To motor phases |
| Control Signals | Electrical | FADEC interface |
| Cooling Manifold | Fluid | Liquid cooling circuit |

## Related Documents

- [installation_definition.yaml](installation_definition.yaml) — Structured definition
- [thermal_requirements.md](thermal_requirements.md) — Thermal management specifications

## Traceability

- **Requirements**: REQ-61-CTRL-001 through REQ-61-CTRL-020
- **ICDs**: ICD-61-020 (Controller Interface)
- **Drawings**: Q100-61-DRW-EMD-CTRL-001

---

## Document Control

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT** – Subject to human review and approval.
- Human approver: _[to be completed]_.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: _2025-12-05_.

---
