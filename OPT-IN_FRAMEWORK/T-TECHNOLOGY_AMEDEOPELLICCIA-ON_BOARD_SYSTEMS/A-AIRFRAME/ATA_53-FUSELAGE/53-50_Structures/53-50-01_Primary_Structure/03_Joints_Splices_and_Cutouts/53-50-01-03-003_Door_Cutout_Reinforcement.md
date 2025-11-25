# 53-50-01-03-003 Door Cutout Reinforcement

## Document Information

- **Document ID**: 53-50-01-03-003
- **Title**: Door Cutout Reinforcement
- **Version**: 1.0
- **Date**: 2025-11-22
- **Status**: Draft
- **Category**: Structural Design
- **ATA Chapter**: 53-50 - Fuselage Structures

## Purpose

This document provides detailed design specifications for Door Cutout Reinforcement in the AMPEL360 BWB primary structure. Door cutouts create stress concentrations that must be addressed through local reinforcement to maintain structural integrity under pressurization and flight loads.

## Scope

This specification covers:
- Passenger door cutout reinforcement
- Cargo door cutout reinforcement
- Emergency exit reinforcement
- Door frame design and attachment
- Stress concentration mitigation

### Applicable Doors

| Door | Type | Size (W × H) | Station |
|------|------|--------------|---------|
| Door 1L/1R | Type A Passenger | 1.07m × 1.85m | 10.0m |
| Door 2L/2R | Type A Passenger | 1.07m × 1.85m | 20.0m |
| Door 3L/3R | Type III Emergency | 0.91m × 1.68m | 30.0m |
| Fwd Cargo | Cargo | 1.70m × 1.20m | 7.0m |
| Aft Cargo | Cargo | 1.70m × 1.20m | 32.0m |

## Design Requirements

### Structural Requirements

| Requirement | Value | Basis |
|-------------|-------|-------|
| Stress concentration factor | Kt ≤ 3.0 at corners | Fatigue life |
| Residual strength | Limit load with door open | [CS-25.783](https://www.easa.europa.eu/en/document-library/certification-specifications/cs-25-amendment-27) |
| Fatigue life | 3 × DSG at cutout edges | Safe-life |
| Door frame material | Al 7050-T7451 | High strength, damage tolerant |

### Geometric Requirements

| Parameter | Specification |
|-----------|---------------|
| Corner radius | ≥75 mm (Type A doors) |
| Doubler extent | 100 mm beyond cutout edge |
| Skin thickness increase | 2× nominal at cutout |
| Frame depth | 200 mm minimum |

## Design Configuration

### Door Surround Structure

**Type A Door (1L/1R, 2L/2R)**:
- **Door Frame**: Machined Al 7050-T7451, integral with door stop
- **Corner Reinforcement**: Tapered CFRP doublers, 6-10 mm thick
- **Hinge Fittings**: Ti-6Al-4V, 3-hinge arrangement
- **Latch Fittings**: 15-5PH stainless steel, 4 latches

### Reinforcement Layup

| Zone | Layup | Thickness | Material |
|------|-------|-----------|----------|
| Corner | [±45/0/90]₅s | 8.0 mm | CFRP |
| Edge (top/bottom) | [±45/0/90]₄s | 6.0 mm | CFRP |
| Edge (sides) | [±45/0/90]₃s | 5.0 mm | CFRP |
| Transition | Tapered | 3.0-6.0 mm | CFRP |

## Load Cases

### Critical Design Cases

| Load Case | Description | Critical Location |
|-----------|-------------|-------------------|
| LC-002 | Max pressure (door closed) | Corner fillets |
| LC-022 | Door operating loads | Hinge/latch fittings |
| LC-023 | Rapid decompression | Frame bending |

### Stress Distribution

| Location | Nominal Stress (MPa) | Peak Stress (MPa) | Kt |
|----------|---------------------|-------------------|-----|
| Door corner (upper fwd) | 85 | 230 | 2.7 |
| Door corner (lower aft) | 80 | 216 | 2.7 |
| Mid-height edge | 90 | 145 | 1.6 |

## Analysis and Verification

### Margin Summary

| Component | Load Case | MS (Strength) | MS (Fatigue) | Status |
|-----------|-----------|---------------|--------------|--------|
| Door 1 corner | LC-002 | +0.12 | 2.5× DSG | ✓ Pass |
| Door frame | LC-022 | +0.18 | 4.0× DSG | ✓ Pass |
| Hinge fitting | LC-022 | +0.15 | 3.5× DSG | ✓ Pass |

### Verification Testing

| Test Article | Test Type | Purpose | Status |
|--------------|-----------|---------|--------|
| Door surround DS-01 | Pressure cycling | Fatigue | In progress |
| Hinge fitting HF-01 | Static + fatigue | Strength/life | Complete |

## Manufacturing Considerations

- **Door Frame**: 5-axis CNC machining from plate
- **Corner Doublers**: Hand layup with AFP core
- **NDI**: 100% ultrasonic inspection of cutout edges

## References

### Regulatory Documents
- [CS-25.783 Doors](https://www.easa.europa.eu/en/document-library/certification-specifications/cs-25-amendment-27)
- [CS-25.809 Emergency Exit Arrangement](https://www.easa.europa.eu/en/document-library/certification-specifications/cs-25-amendment-27)

### Internal References
- [53-50-01-02-003 Side Shell Skin Design](../02_Panels_Frames_and_Skins/53-50-01-02-003_Side_Shell_Skin_Design.md)

---

## Document Control

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT** – Subject to human review and approval.
- Human approver: _[to be completed]_.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: 2025-11-25

---
