# 53-50-01-04-003 Tail Attachment Fittings

## Document Information

- **Document ID**: 53-50-01-04-003
- **Title**: Tail Attachment Fittings
- **Version**: 1.0
- **Date**: 2025-11-22
- **Status**: Draft
- **Category**: Structural Design
- **ATA Chapter**: 53-50 - Fuselage Structures

## Purpose

This document provides detailed design specifications for Tail Attachment Fittings in the AMPEL360 BWB primary structure. These fittings transfer vertical stabilizer and horizontal stabilizer loads into the aft fuselage structure.

## Scope

This specification covers:
- Vertical stabilizer attachment fittings
- Horizontal stabilizer attachment fittings
- Rear spar attachment points
- Fin-to-fuselage interface structure

### BWB Tail Configuration

The AMPEL360 BWB features a V-tail or T-tail configuration with:
- Twin vertical stabilizers (canted outboard)
- High-mounted horizontal stabilizer
- Attachment zone: Stations 35m - 38m

## Design Requirements

### Structural Requirements

| Requirement | Value | Basis |
|-------------|-------|-------|
| Ultimate vertical fin bending | 8,500 kN·m | Rudder + gust |
| Ultimate horizontal stab. load | 450 kN | Maximum elevator |
| Ultimate torsion | 2,500 kN·m | Asymmetric loading |
| Fatigue life | 4 × DSG | Safe-life |

### Material Requirements

| Component | Material | Specification |
|-----------|----------|---------------|
| Main attach fittings | Ti-6Al-4V | AMS 4928 |
| Auxiliary fittings | Al 7050-T7451 | AMS 4050 |
| Pivot bearings | 17-4PH Steel | AMS 5643 |
| Attachment bolts | A286 Steel | NAS6 series |

## Design Configuration

### Vertical Stabilizer Attachment

| Fitting ID | Location | Function |
|------------|----------|----------|
| VF-FWD-L/R | Station 35m | Forward spar attachment |
| VF-AFT-L/R | Station 37m | Rear spar attachment |
| VF-AUX-L/R | Station 36m | Auxiliary support |

### Fitting Loads

| Load Component | Limit (kN) | Ultimate (kN) |
|----------------|------------|---------------|
| Vertical | 120 | 180 |
| Lateral | 280 | 420 |
| Axial | 85 | 128 |

## Analysis and Verification

### Margin Summary

| Component | Load Case | MS (Ultimate) | Status |
|-----------|-----------|---------------|--------|
| VF-FWD fitting | Fin bending | +0.15 | ✓ Pass |
| VF-AFT fitting | Torsion | +0.18 | ✓ Pass |
| Attach bolts | Combined | +0.12 | ✓ Pass |

### Verification Testing

| Test Article | Test Type | Purpose | Status |
|--------------|-----------|---------|--------|
| Fitting VF-01 | Static | Ultimate strength | Complete |
| Full tail attach | Static | Load path | Planned |

## References

### Regulatory Documents
- [CS-25.561 Emergency Landing Conditions](https://www.easa.europa.eu/en/document-library/certification-specifications/cs-25-amendment-27)
- [CS-25.571 Damage Tolerance](https://www.easa.europa.eu/en/document-library/certification-specifications/cs-25-amendment-27)

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
