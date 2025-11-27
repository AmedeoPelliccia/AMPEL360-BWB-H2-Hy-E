# 53-60-40-01 PCM Accumulator Design

## Document Information

- **Document ID**: 53-60-40-01
- **Title**: PCM Accumulator Design
- **Version**: 1.0
- **Date**: 2025-11-27
- **Status**: Draft
- **Category**: Thermal Storage
- **ATA Chapter**: 53-60 - Fuselage Storages

## Purpose

This document defines the Phase Change Material (PCM) accumulator design for thermal energy storage and load leveling.

## Scope

This specification covers:
- PCM selection and properties
- Accumulator construction
- Heat transfer design
- Thermal performance

## PCM Specifications

### Material Properties

| Property | Value | Unit | Reference |
|----------|-------|------|-----------|
| PCM type | Paraffin-based | — | REQ-TH-001 |
| Melting point | 45 ± 2 | °C | REQ-TH-002 |
| Latent heat | 200 | kJ/kg | REQ-TH-003 |
| Specific heat (solid) | 2.0 | kJ/kg·K | REQ-TH-004 |
| Specific heat (liquid) | 2.2 | kJ/kg·K | REQ-TH-005 |
| Thermal conductivity | 0.2 | W/m·K | REQ-TH-006 |
| Density (solid) | 900 | kg/m³ | REQ-TH-007 |
| Density (liquid) | 850 | kg/m³ | REQ-TH-008 |

### Accumulator Design

| Parameter | Value | Unit | Reference |
|-----------|-------|------|-----------|
| PCM mass | 20 | kg | MASS-53-60-40 |
| Thermal capacity | 4000 | kJ | REQ-TH-004 |
| Shell material | Aluminum 6061-T6 | — | AMS 4027 |
| Operating temperature | 30-60 | °C | REQ-TH-011 |
| Charge/discharge rate | 5-15 | kW | REQ-TH-010 |

### Heat Transfer Enhancement

| Feature | Description | Reference |
|---------|-------------|-----------|
| Fins | Aluminum internal fins | DWG-53-60-40-001 |
| Conductivity enhancement | Graphite additive 5% | REQ-TH-015 |
| Flow design | Serpentine HTF path | DWG-53-60-40-001 |

## Thermal Performance

### Charge Cycle

| Parameter | Value | Unit |
|-----------|-------|------|
| Charge time (5 kW) | 15 | min |
| Charge time (15 kW) | 5 | min |
| HTF inlet temp (charge) | 60 | °C |
| HTF outlet temp (charge) | 50-55 | °C |

### Discharge Cycle

| Parameter | Value | Unit |
|-----------|-------|------|
| Discharge time (5 kW) | 15 | min |
| Discharge time (15 kW) | 5 | min |
| HTF inlet temp (discharge) | 30 | °C |
| HTF outlet temp (discharge) | 40-45 | °C |

## Lifecycle

| Parameter | Value | Reference |
|-----------|-------|-----------|
| Cycle life | 10,000 | REQ-TH-020 |
| Capacity retention | ≥ 95% at 5,000 cycles | REQ-TH-021 |
| Thermal stability | No degradation to 100°C | REQ-TH-022 |

## References

### Internal Documents
- [53-60-40-02 Buffer Tank Specification](53-60-40-02_Buffer_Tank.md)
- [53-60-40-03 Thermal Insulation Design](53-60-40-03_Thermal_Insulation.md)

---

## Document Control

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT** – Subject to human review and approval.
- Human approver: _[to be completed]_.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: 2025-11-27

---
