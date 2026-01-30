# 53-60-10-02 Thermal Jacket Specification

## Document Information

- **Document ID**: 53-60-10-02
- **Title**: Thermal Jacket Specification
- **Version**: 1.0
- **Date**: 2025-11-27
- **Status**: Draft
- **Category**: Battery Storage
- **ATA Chapter**: 53-60 - Fuselage Storages

## Purpose

This document defines the thermal jacket specifications for the QuickSwap battery pack, providing thermal runaway containment and operating temperature management.

## Scope

This specification covers:
- Thermal barrier construction
- Fire containment performance
- Operating temperature range
- Insulation requirements

## Thermal Jacket Specifications

### Performance Requirements

| Parameter | Value | Unit | Reference |
|-----------|-------|------|-----------|
| Operating temperature | -40 to +60 | °C | REQ-BAT-010 |
| Fire containment time | ≥ 5 | min | DSR-005 |
| Thermal conductivity | ≤ 0.02 | W/m·K | REQ-BAT-011 |
| Thickness | 10-15 | mm | DWG-53-60-10-002 |

### Construction

| Layer | Material | Thickness | Function |
|-------|----------|-----------|----------|
| Outer shell | Aluminum 6061-T6 | 1.5 mm | Protection |
| Fire barrier | Ceramic fiber | 5.0 mm | Thermal runaway containment |
| Insulation | Aerogel blanket | 5.0 mm | Thermal management |
| Inner liner | Silicone-coated fabric | 0.5 mm | Chemical barrier |

### Thermal Performance

| Condition | Internal Temp | External Temp | Duration |
|-----------|--------------|---------------|----------|
| Normal operation | 25-45°C | Ambient | Continuous |
| Cold soak | -40°C | -40°C | ≥ 8 hours |
| Hot soak | 60°C | 60°C | ≥ 8 hours |
| Thermal runaway | >600°C | ≤ 150°C | ≥ 5 min |

## Fire Containment

### Test Requirements

| Test | Criteria | Reference |
|------|----------|-----------|
| Propagation resistance | No cell-to-cell propagation | UL 2580 |
| External flame | 5 min containment | CS 25.863 |
| Gas venting | Controlled release | DSR-006 |

## References

### Internal Documents
- [53-60-10-01 Pack Housing Design](53-60-10-01_Pack_Housing_Design.md)
- [53-60-10-06 Safety Analysis](53-60-10-06_Safety_Analysis.md)

### External Standards
- [CS-25.863](https://www.easa.europa.eu/en/document-library/certification-specifications/cs-25-amendment-27) - Flammable Fluid Fire Protection
- UL 2580 - Batteries for Use in Electric Vehicles

---

## Document Control

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT** – Subject to human review and approval.
- Human approver: _[to be completed]_.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: 2025-11-27

---
