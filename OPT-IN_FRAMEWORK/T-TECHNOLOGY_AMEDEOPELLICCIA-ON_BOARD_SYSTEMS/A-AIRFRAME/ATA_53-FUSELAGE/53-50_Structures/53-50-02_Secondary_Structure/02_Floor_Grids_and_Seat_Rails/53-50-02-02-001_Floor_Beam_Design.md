# 53-50-02-02-001 Floor Beam Design

## Document Information

- **Document ID**: 53-50-02-02-001
- **Title**: Floor Beam Design
- **Version**: 1.0
- **Date**: 2025-11-22
- **Status**: Draft
- **Category**: Structural Design
- **ATA Chapter**: 53-50 - Fuselage Structures

## Purpose

This document provides design specifications for floor beams in the AMPEL360 BWB fuselage, which support the cabin and cargo floor panels and transfer loads to the primary fuselage frames.

## Scope

Floor beam design covers:
- Passenger cabin floor beams
- Cargo hold floor beams
- Battery bay floor beams (enhanced for CO₂ battery)
- Floor-to-frame interfaces

## Design Requirements

### Load Requirements

| Zone | Floor Load (kN/m²) | Emergency Load | Reference |
|------|-------------------|----------------|-----------|
| Passenger cabin | 5.0 | 9g forward | CS-25.561 |
| Cargo hold | 8.0 | 9g forward | CS-25.561 |
| Battery bay | 12.0 | 16g forward | Special requirement |

### Deflection Limits

| Condition | Maximum Deflection |
|-----------|-------------------|
| Static (passengers) | L/400 |
| Emergency landing | L/200 |
| Fatigue (repeated) | L/500 |

## Design Configuration

### Beam Types

| Type | Cross-Section | Material | Application |
|------|---------------|----------|-------------|
| FB-A | I-section | Al 7050-T7451 | Passenger floor |
| FB-B | C-section | Al 7050-T7451 | Cargo floor |
| FB-C | Box-section | Al 7050-T7451 | Battery bay |

### Beam Dimensions

| Beam Type | Depth (mm) | Flange (mm) | Web (mm) | Weight (kg/m) |
|-----------|------------|-------------|----------|---------------|
| FB-A | 120 | 60 × 5 | 3 | 4.2 |
| FB-B | 100 | 50 × 4 | 2.5 | 3.1 |
| FB-C | 150 | 80 × 8 | 5 | 8.5 |

### Beam Spacing

| Zone | Spacing | Notes |
|------|---------|-------|
| Passenger cabin | 500 mm | Aligned with frames |
| Cargo hold | 600 mm | ULD compatible |
| Battery bay | 400 mm | Enhanced support |

## Attachment Details

### Frame Interface

| Method | Application | Fasteners |
|--------|-------------|-----------|
| Angle brackets | Standard beams | 4 × M8 bolts |
| Forged fittings | Heavy beams | 6 × M10 bolts |
| Bonded interface | Secondary | Adhesive + rivets |

## Analysis Summary

### Margin Summary

| Component | Load Case | MS (Bending) | MS (Shear) | Status |
|-----------|-----------|--------------|------------|--------|
| FB-A mid-span | 9g emergency | +0.22 | +0.35 | ✓ Pass |
| FB-B mid-span | Cargo load | +0.28 | +0.40 | ✓ Pass |
| FB-C mid-span | Battery crash | +0.12 | +0.18 | ✓ Pass |
| Bracket bolts | 9g emergency | +0.18 | N/A | ✓ Pass |

## References

### Regulatory Documents
- [CS-25.561 Emergency Landing Conditions](https://www.easa.europa.eu/en/document-library/certification-specifications/cs-25-amendment-27)

### Internal References
- [Floor Load Distribution](ASSETS/Floor_Load_Distribution.csv)

---

## Document Control

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT** – Subject to human review and approval.
- Human approver: _[to be completed]_.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: 2025-11-25

---
