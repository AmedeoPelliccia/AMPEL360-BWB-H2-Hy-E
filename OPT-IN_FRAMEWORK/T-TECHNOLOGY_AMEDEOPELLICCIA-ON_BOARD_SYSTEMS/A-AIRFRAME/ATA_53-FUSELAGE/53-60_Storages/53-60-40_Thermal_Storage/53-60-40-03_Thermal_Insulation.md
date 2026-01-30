# 53-60-40-03 Thermal Insulation Design

## Document Information

- **Document ID**: 53-60-40-03
- **Title**: Thermal Insulation Design
- **Version**: 1.0
- **Date**: 2025-11-27
- **Status**: Draft
- **Category**: Thermal Storage
- **ATA Chapter**: 53-60 - Fuselage Storages

## Purpose

This document defines the thermal insulation design for the thermal storage system components.

## Scope

This specification covers:
- Insulation material selection
- Thermal performance requirements
- Installation methods
- Maintenance provisions

## Insulation Requirements

### Performance Requirements

| Parameter | Value | Unit | Reference |
|-----------|-------|------|-----------|
| R-value (accumulator) | ≥ 0.8 | m²K/W | REQ-TH-030 |
| R-value (piping) | ≥ 0.4 | m²K/W | REQ-TH-031 |
| Heat loss (standby) | ≤ 50 | W | REQ-TH-032 |
| Cooldown time | ≥ 4 | hours | REQ-TH-033 |

### Temperature Limits

| Component | Max Surface Temp | Reference |
|-----------|------------------|-----------|
| PCM accumulator | 70°C internal | REQ-TH-011 |
| Buffer tank | 80°C internal | REQ-TH-040 |
| Piping | 60°C internal | REQ-TH-035 |
| External surfaces | ≤ 45°C | CS 25.1359 |

## Insulation Materials

### Primary Insulation

| Material | Thickness | Application | Reference |
|----------|-----------|-------------|-----------|
| Aerogel blanket | 10 mm | High-performance areas | REQ-TH-070 |
| Closed-cell foam | 25 mm | General purpose | REQ-TH-071 |
| Mineral wool | 25 mm | High-temperature areas | REQ-TH-072 |

### Material Properties

| Property | Aerogel | Foam | Mineral Wool |
|----------|---------|------|--------------|
| Thermal conductivity | 0.015 W/m·K | 0.035 W/m·K | 0.040 W/m·K |
| Density | 150 kg/m³ | 50 kg/m³ | 100 kg/m³ |
| Max temperature | 650°C | 80°C | 750°C |
| Flammability | Non-combustible | Self-extinguishing | Non-combustible |

## Installation Design

### PCM Accumulator

| Layer | Material | Thickness |
|-------|----------|-----------|
| 1 (inner) | Aerogel blanket | 10 mm |
| 2 | Reflective foil | — |
| 3 (outer) | Protective jacket | 0.5 mm Al |

### Buffer Tank

| Layer | Material | Thickness |
|-------|----------|-----------|
| 1 (inner) | Closed-cell foam | 25 mm |
| 2 (outer) | Protective jacket | 0.5 mm Al |

### Piping

| Layer | Material | Thickness |
|-------|----------|-----------|
| 1 (inner) | Closed-cell foam | 15 mm |
| 2 (outer) | Protective wrap | 0.3 mm Al |

## Personnel Protection

Per [CS 25.1359](https://www.easa.europa.eu/en/document-library/certification-specifications/cs-25-amendment-27):

| Requirement | Description | Reference |
|-------------|-------------|-----------|
| Hot surfaces | ≤ 45°C accessible surfaces | DSR-032 |
| Warning labels | Required on surfaces > 45°C | REQ-TH-080 |
| Touch protection | Guards on high-temp areas | REQ-TH-081 |

## References

### Internal Documents
- [53-60-40-01 PCM Accumulator Design](53-60-40-01_PCM_Accumulator.md)
- [53-60-80-01 Thermal Insulation Specification](../53-60-80_Insulation/53-60-80-01_Thermal_Insulation.md)

### External Standards
- [CS-25.1359](https://www.easa.europa.eu/en/document-library/certification-specifications/cs-25-amendment-27) - Hot Surfaces

---

## Document Control

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT** – Subject to human review and approval.
- Human approver: _[to be completed]_.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: 2025-11-27

---
