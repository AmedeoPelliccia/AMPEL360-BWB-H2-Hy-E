# 53-60-30-01 Water Tank Design

## Document Information

- **Document ID**: 53-60-30-01
- **Title**: Water Tank Design
- **Version**: 1.0
- **Date**: 2025-11-27
- **Status**: Draft
- **Category**: Water Storage
- **ATA Chapter**: 53-60 - Fuselage Storages

## Purpose

This document defines the design specifications for the water storage tank used to collect and store recovered water from cabin humidity, fuel cell byproduct, and atmospheric condensation.

## Scope

This specification covers:
- Tank structure and dimensions
- Material specifications
- Mounting and installation
- Service provisions

## Tank Specifications

### Dimensions and Capacity

| Parameter | Value | Unit | Reference |
|-----------|-------|------|-----------|
| Capacity | 100 | L | REQ-H2O-001 |
| Length | 500 | mm | DWG-53-60-30-001 |
| Width | 400 | mm | DWG-53-60-30-001 |
| Height | 500 | mm | DWG-53-60-30-001 |
| Mass (empty) | 5 | kg | MASS-53-60-30 |
| Mass (full) | 105 | kg | MASS-53-60-30 |

### Operating Conditions

| Parameter | Value | Unit | Reference |
|-----------|-------|------|-----------|
| Operating pressure | 0-0.5 | bar | REQ-H2O-010 |
| Operating temperature | 5-50 | °C | REQ-H2O-011 |
| Design pressure | 1.0 | bar | REQ-H2O-012 |
| Freeze protection | Down to 0°C | — | REQ-H2O-015 |

### Tank Configuration

```
┌─────────────────────────────────────────┐
│           WATER STORAGE TANK            │
│  ┌───────────────────────────────────┐  │
│  │         Vent / Overflow           │──┼── To drain mast
│  ├───────────────────────────────────┤  │
│  │                                   │  │
│  │      Flexible Bladder             │  │
│  │      (Potable Water)              │  │
│  │                                   │  │
│  │  ┌─────────┐                      │  │
│  │  │ Level   │ Capacitive sensor    │  │
│  │  │ Sensor  │                      │  │
│  │  └─────────┘                      │  │
│  │                                   │  │
│  ├───────────────────────────────────┤  │
│  │         Drain Sump                │──┼── To service panel
│  └───────────────────────────────────┘  │
│  ┌─────────┐  ┌─────────┐  ┌─────────┐  │
│  │ Fill    │  │ Supply  │  │ Temp    │  │
│  │ Port    │  │ Port    │  │ Sensor  │  │
│  └─────────┘  └─────────┘  └─────────┘  │
└─────────────────────────────────────────┘
```

## Materials

| Component | Material | Specification | Reference |
|-----------|----------|---------------|-----------|
| Tank shell | Stainless 316L | AMS 5653 | REQ-H2O-020 |
| Bladder | HDPE (food-grade) | FDA 21 CFR 177 | REQ-H2O-020 |
| Fittings | Stainless 316L | AMS 5653 | REQ-H2O-022 |
| Insulation | Closed-cell foam | — | REQ-H2O-023 |

## Mounting

| Parameter | Value | Reference |
|-----------|-------|-----------|
| Mount type | Strapped | DWG-53-60-30-001 |
| Structural attach | 4× mounting brackets | DWG-53-60-30-001 |
| Isolation | Rubber bushings | REQ-H2O-030 |

## References

### Internal Documents
- [53-60-30-02 Bladder Assembly Specification](53-60-30-02_Bladder_Assembly.md)
- [53-60-30-03 Level Sensing System](53-60-30-03_Level_Sensing.md)

---

## Document Control

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT** – Subject to human review and approval.
- Human approver: _[to be completed]_.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: 2025-11-27

---
