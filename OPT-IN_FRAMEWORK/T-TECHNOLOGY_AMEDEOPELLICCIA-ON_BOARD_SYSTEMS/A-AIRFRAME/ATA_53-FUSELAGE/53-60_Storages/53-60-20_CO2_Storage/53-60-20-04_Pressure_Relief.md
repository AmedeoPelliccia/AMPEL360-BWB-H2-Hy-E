# 53-60-20-04 Pressure Relief System

## Document Information

- **Document ID**: 53-60-20-04
- **Title**: Pressure Relief System
- **Version**: 1.0
- **Date**: 2025-11-27
- **Status**: Draft
- **Category**: CO₂ Storage
- **ATA Chapter**: 53-60 - Fuselage Storages

## Purpose

This document defines the pressure relief system specifications for the CO₂ storage system.

## Scope

This specification covers:
- Relief valve specifications
- Burst disc specifications
- Vent routing
- Safety interlocks

## Pressure Relief Specifications

### Relief Valve

| Parameter | Value | Unit | Reference |
|-----------|-------|------|-----------|
| Set pressure | 2.5 | bar | DSR-004 |
| Full flow pressure | 2.75 | bar | REQ-CO2-070 |
| Reseat pressure | 2.0 | bar | REQ-CO2-071 |
| Flow capacity | 50 | kg/hr | REQ-CO2-072 |
| Type | Spring-loaded poppet | — | DWG-53-60-20-004 |

### Burst Disc

| Parameter | Value | Unit | Reference |
|-----------|-------|------|-----------|
| Burst pressure | 4.0 ± 0.2 | bar | REQ-CO2-075 |
| Temperature range | -40 to +100 | °C | REQ-CO2-076 |
| Material | Stainless 316L | — | AMS 5653 |
| Size | DN15 | — | DWG-53-60-20-004 |

### Vent Routing

| Parameter | Value | Reference |
|-----------|-------|-----------|
| Vent location | Overboard, bottom | DWG-53-60-20-004 |
| Line size | DN15 | REQ-CO2-080 |
| Material | Stainless 316L | AMS 5653 |
| Ice protection | Heated | REQ-CO2-081 |

## Safety Features

| Feature | Description | Reference |
|---------|-------------|-----------|
| Dual relief | Valve + burst disc | DSR-004 |
| Telltale | Burst disc indicator | REQ-CO2-085 |
| Vent blockage | Anti-ice provision | REQ-CO2-081 |
| BITE | Relief valve position | REQ-CO2-086 |

## Test Requirements

| Test | Criteria | Reference |
|------|----------|-----------|
| Relief valve set pressure | 2.5 ±0.1 bar | TST-CO2-001 |
| Burst disc rupture | 4.0 ±0.2 bar | TST-CO2-002 |
| Leak test | No leak at 2.0 bar | TST-CO2-003 |
| Flow capacity | ≥ 50 kg/hr at 2.75 bar | TST-CO2-004 |

## References

### Internal Documents
- [53-60-00-04 Safety Requirements](../53-60-00_General/53-60-00-04_Safety_Requirements.md)
- [53-60-70-01 Relief Valve Specification](../53-60-70_Pressure_Systems/53-60-70-01_Relief_Valve_Spec.md)

### External Standards
- [CS-25.1435](https://www.easa.europa.eu/en/document-library/certification-specifications/cs-25-amendment-27) - Hydraulic Systems

---

## Document Control

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT** – Subject to human review and approval.
- Human approver: _[to be completed]_.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: 2025-11-27

---
