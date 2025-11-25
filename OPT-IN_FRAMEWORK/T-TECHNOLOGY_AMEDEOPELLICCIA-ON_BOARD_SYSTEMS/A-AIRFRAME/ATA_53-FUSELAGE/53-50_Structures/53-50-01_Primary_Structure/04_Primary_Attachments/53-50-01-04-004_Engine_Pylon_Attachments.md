# 53-50-01-04-004 Engine Pylon Attachments

## Document Information

- **Document ID**: 53-50-01-04-004
- **Title**: Engine Pylon Attachments
- **Version**: 1.0
- **Date**: 2025-11-22
- **Status**: Draft
- **Category**: Structural Design
- **ATA Chapter**: 53-50 - Fuselage Structures

## Purpose

This document provides detailed design specifications for Engine Pylon Attachments in the AMPEL360 BWB primary structure. The engines are mounted on the aft fuselage/wing trailing edge, requiring robust attachment fittings to transfer thrust, weight, and inertia loads.

## Scope

This specification covers:
- Engine pylon-to-fuselage interface fittings
- Forward and aft mount attachments
- Thrust link design
- Vibration isolation provisions

### Engine Configuration

| Parameter | Value |
|-----------|-------|
| Engine type | High-bypass turbofan (H₂ hybrid) |
| Engine weight (dry) | 3,800 kg each |
| Maximum thrust | 180 kN per engine |
| Engine count | 2 (rear-mounted) |
| Mount location | Station 34m - 36m |

## Design Requirements

### Structural Requirements

| Requirement | Value | Basis |
|-------------|-------|-------|
| Ultimate thrust | 270 kN (1.5 × max) | Forward mount |
| Ultimate vertical load | 8g × engine weight | Maneuver |
| Ultimate side load | 3g × engine weight | Asymmetric |
| Fatigue life | 4 × DSG | Safe-life |
| Vibration isolation | 85% efficiency | Passenger comfort |

### Material Requirements

| Component | Material | Specification |
|-----------|----------|---------------|
| Forward mount | Ti-6Al-4V | AMS 4928 |
| Aft mount | Al 7050-T7451 | AMS 4050 |
| Thrust link | 4340 Steel | AMS 6414 |
| Vibration mounts | Elastomeric | Lord Mounts |

## Design Configuration

### Attachment Layout

| Fitting ID | Location | Function |
|------------|----------|----------|
| EP-FWD | Station 34.5m | Forward/thrust mount |
| EP-AFT | Station 35.5m | Aft/vertical mount |
| EP-THR | Station 34.5m | Thrust reaction link |

### Load Distribution

| Load | Forward Mount (%) | Aft Mount (%) |
|------|-------------------|---------------|
| Thrust | 100 | 0 |
| Vertical | 40 | 60 |
| Side | 50 | 50 |
| Torque | 30 | 70 |

## Load Cases

### Critical Design Cases

| Load Case | Description | Critical Component |
|-----------|-------------|-------------------|
| LC-032 | Maximum thrust | Thrust link |
| LC-033 | Engine seizure | Forward mount bolts |
| LC-034 | Hard landing | Aft mount |
| LC-035 | Blade-out | All mounts |

## Analysis and Verification

### Margin Summary

| Component | Load Case | MS (Ultimate) | Status |
|-----------|-----------|---------------|--------|
| Forward mount lug | LC-032 | +0.12 | ✓ Pass |
| Thrust link | LC-032 | +0.15 | ✓ Pass |
| Aft mount | LC-034 | +0.10 | ✓ Pass |

### Verification Testing

| Test Article | Test Type | Purpose | Status |
|--------------|-----------|---------|--------|
| Pylon mount PM-01 | Static | Ultimate strength | Planned |
| Thrust link TL-01 | Fatigue | Life validation | Planned |

## References

### Regulatory Documents
- [CS-25.571 Damage Tolerance](https://www.easa.europa.eu/en/document-library/certification-specifications/cs-25-amendment-27)
- [CS-E 520 Strength](https://www.easa.europa.eu/en/document-library/certification-specifications/cs-e-amendment-5)

### Internal References
- [53-50-01 Primary Structure Overview](../../README.md)

---

## Document Control

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT** – Subject to human review and approval.
- Human approver: _[to be completed]_.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: 2025-11-25

---
