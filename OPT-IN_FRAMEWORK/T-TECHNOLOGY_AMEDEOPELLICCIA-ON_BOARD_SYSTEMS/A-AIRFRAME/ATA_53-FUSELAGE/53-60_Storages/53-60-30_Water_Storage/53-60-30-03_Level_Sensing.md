# 53-60-30-03 Level Sensing System

## Document Information

- **Document ID**: 53-60-30-03
- **Title**: Level Sensing System
- **Version**: 1.0
- **Date**: 2025-11-27
- **Status**: Draft
- **Category**: Water Storage
- **ATA Chapter**: 53-60 - Fuselage Storages

## Purpose

This document defines the level sensing system specifications for the water storage tank.

## Scope

This specification covers:
- Sensor technology selection
- Performance requirements
- Installation requirements
- Signal interface

## Sensor Specifications

### Performance Requirements

| Parameter | Value | Unit | Reference |
|-----------|-------|------|-----------|
| Measurement range | 0-100 | % | REQ-H2O-030 |
| Accuracy | ±2 | % | REQ-H2O-030 |
| Resolution | 1 | % | REQ-H2O-031 |
| Update rate | 1 | Hz | REQ-H2O-032 |
| Response time | ≤ 1 | sec | REQ-H2O-033 |

### Sensor Technology

| Type | Description | Reference |
|------|-------------|-----------|
| Primary | Capacitive | REQ-H2O-034 |
| Backup | Ultrasonic | REQ-H2O-035 |
| Discrete | Low level switch | REQ-H2O-036 |

### Environmental Requirements

| Parameter | Value | Unit | Reference |
|-----------|-------|------|-----------|
| Temperature range | -40 to +85 | °C | REQ-H2O-040 |
| Humidity | 0-100 | % RH | REQ-H2O-041 |
| Vibration | MIL-STD-810G | — | REQ-H2O-042 |
| EMI | DO-160G Cat M | — | REQ-H2O-043 |

## Sensor Configuration

### Capacitive Sensor

| Parameter | Value | Reference |
|-----------|-------|-----------|
| Probe length | 450 mm | DWG-53-60-30-003 |
| Probe material | Stainless 316L | AMS 5653 |
| Dielectric constant (water) | 80 | — |
| Dielectric constant (air) | 1 | — |

### Low Level Switch

| Parameter | Value | Reference |
|-----------|-------|-----------|
| Set point | 10% | REQ-H2O-050 |
| Hysteresis | 2% | REQ-H2O-051 |
| Output | Discrete 28 VDC | REQ-H2O-052 |

## Signal Interface

| Signal | Type | Range | Reference |
|--------|------|-------|-----------|
| Level (analog) | 4-20 mA | 0-100% | ICD-53-60-30-001 |
| Level (digital) | ARINC 429 | Label 203 | ICD-53-60-30-001 |
| Low level | Discrete | 28 VDC | ICD-53-60-30-001 |
| Sensor fail | Discrete | 28 VDC | ICD-53-60-30-001 |

## Built-In Test (BIT)

| Test | Description | Frequency |
|------|-------------|-----------|
| Initiated BIT | Full self-test | On command |
| Continuous BIT | Range/reasonableness | Continuous |
| Power-up BIT | Initialization check | At power-on |

## Installation

| Requirement | Description |
|-------------|-------------|
| Mounting | Top of tank, vertical |
| Sealing | O-ring, leak-tested |
| Wiring | Shielded, per DO-160G |
| Access | Service panel accessible |

## References

### Internal Documents
- [53-60-30-01 Water Tank Design](53-60-30-01_Tank_Design.md)

### External Standards
- [DO-160G](https://www.rtca.org/content/standards-guidance-documents) - Environmental Conditions

---

## Document Control

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT** – Subject to human review and approval.
- Human approver: _[to be completed]_.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: 2025-11-27

---
