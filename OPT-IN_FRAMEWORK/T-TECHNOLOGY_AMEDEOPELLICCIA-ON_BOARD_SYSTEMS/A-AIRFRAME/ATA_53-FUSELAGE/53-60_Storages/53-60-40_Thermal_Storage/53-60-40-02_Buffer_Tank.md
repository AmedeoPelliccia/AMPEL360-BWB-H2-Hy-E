# 53-60-40-02 Buffer Tank Specification

## Document Information

- **Document ID**: 53-60-40-02
- **Title**: Buffer Tank Specification
- **Version**: 1.0
- **Date**: 2025-11-27
- **Status**: Draft
- **Category**: Thermal Storage
- **ATA Chapter**: 53-60 - Fuselage Storages

## Purpose

This document defines the buffer tank specifications for thermal fluid storage and hydraulic expansion accommodation.

## Scope

This specification covers:
- Tank design and construction
- Expansion accommodation
- Pressure management
- Temperature requirements

## Buffer Tank Specifications

### Tank Design

| Parameter | Value | Unit | Reference |
|-----------|-------|------|-----------|
| Capacity (total) | 10 | L | REQ-TH-030 |
| Capacity (working) | 8 | L | REQ-TH-031 |
| Expansion volume | 2 | L | REQ-TH-032 |
| Operating pressure | 0-3.0 | bar | REQ-TH-033 |
| Design pressure | 5.0 | bar | REQ-TH-034 |

### Operating Conditions

| Parameter | Value | Unit | Reference |
|-----------|-------|------|-----------|
| Operating temperature | 30-60 | °C | REQ-TH-011 |
| Design temperature | 80 | °C | REQ-TH-040 |
| HTF type | Water-glycol 50/50 | — | REQ-TH-041 |
| Expansion coefficient | 0.0005 | 1/°C | — |

### Tank Construction

| Component | Material | Specification |
|-----------|----------|---------------|
| Tank shell | Stainless 316L | AMS 5653 |
| End caps | Stainless 316L | AMS 5653 |
| Bladder | EPDM | AMS 3216 |
| Insulation | Closed-cell foam | 25 mm |

## Expansion System

### Bladder Type

| Feature | Description | Reference |
|---------|-------------|-----------|
| Type | Replaceable bladder | DWG-53-60-40-002 |
| Precharge | Nitrogen, 1.0 bar | REQ-TH-050 |
| Expansion ratio | 1:4 | REQ-TH-051 |
| Service life | 10 years | REQ-TH-052 |

### Pressure Relief

| Parameter | Value | Reference |
|-----------|-------|-----------|
| Relief pressure | 3.0 bar | DSR-031 |
| Burst disc | 5.0 bar | REQ-TH-055 |
| Vent routing | Overboard | DWG-53-60-40-002 |

## Connections

| Port | Size | Function |
|------|------|----------|
| Inlet/outlet | DN15 | HTF circuit |
| Drain | DN8 | Service drain |
| Fill/bleed | M8 | Initial charge |
| Pressure sensor | M10 | Monitoring |

## Level Monitoring

| Parameter | Value | Reference |
|-----------|-------|-----------|
| Sensor type | Float switch | REQ-TH-060 |
| Low level alarm | 30% | REQ-TH-061 |
| High level alarm | 95% | REQ-TH-062 |

## References

### Internal Documents
- [53-60-40-01 PCM Accumulator Design](53-60-40-01_PCM_Accumulator.md)
- [53-60-40-04 Heat Exchanger Integration](53-60-40-04_Heat_Exchanger.md)

---

## Document Control

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT** – Subject to human review and approval.
- Human approver: _[to be completed]_.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: 2025-11-27

---
