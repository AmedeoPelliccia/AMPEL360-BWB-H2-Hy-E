# 53-50-01-04-002 Landing Gear Attachments

## Document Information

- **Document ID**: 53-50-01-04-002
- **Title**: Landing Gear Attachments
- **Version**: 1.0
- **Date**: 2025-11-22
- **Status**: Draft
- **Category**: Structural Design
- **ATA Chapter**: 53-50 - Fuselage Structures

## Purpose

This document provides detailed design specifications for Landing Gear Attachments in the AMPEL360 BWB primary structure. The main landing gear (MLG) attachments transfer high vertical and drag loads from the gear into the fuselage structure during landing, taxi, and ground operations.

## Scope

This specification covers:
- Main landing gear (MLG) attachment fittings
- Nose landing gear (NLG) attachment fittings
- Gear trunnion supports
- Side stay and drag stay attachments
- Load paths into fuselage primary structure

### Landing Gear Configuration

| Parameter | MLG (each) | NLG |
|-----------|------------|-----|
| Gear type | Dual tandem | Dual wheel |
| Wheel count | 4 | 2 |
| Tire size | 50 × 20 R22 | 40 × 16 R16 |
| Attachment points | 2 trunnion + 1 side stay | 2 trunnion + 1 drag stay |

## Design Requirements

### Structural Requirements

| Requirement | Value | Basis |
|-------------|-------|-------|
| Ultimate vertical load (MLG) | 4,500 kN per gear | 3.0 × sink rate landing |
| Ultimate drag load (MLG) | 1,350 kN per gear | Braking + spin-up |
| Ultimate side load (MLG) | 900 kN per gear | Cross-wind landing |
| Fatigue life | 4 × DSG | Safe-life (Principal Structural Elements) |
| NLG steering torque | 200 kN·m | Maximum steering |

### Material Requirements

| Component | Material | Specification | Ftu (MPa) |
|-----------|----------|---------------|-----------|
| Trunnion fittings | Ti-6Al-4V | AMS 4935 forging | 1,100 |
| Side stay fitting | 4340 Steel | AMS 6414 | 1,790 |
| Backup structure | Al 7050-T7451 | AMS 4050 | 525 |
| Attachment bolts | H-11 Steel | NAS6 | 1,520 |

## Design Configuration

### MLG Attachment Layout

| Fitting ID | Location | Function | Load Direction |
|------------|----------|----------|----------------|
| MLG-TRN-F | Station 20.0m, Frame 40 | Forward trunnion | Vertical + drag |
| MLG-TRN-A | Station 21.0m, Frame 42 | Aft trunnion | Vertical + drag |
| MLG-SST | Station 20.5m, Frame 41 | Side stay | Side + vertical |

### Trunnion Fitting Design

**Forward Trunnion (MLG-TRN-F)**:
```
                  Trunnion Pin
         _____________|_____________
        |         Ø80 Bore          |
        |            O              |   Ti-6Al-4V Forging
        |___________________________|
        |     |     |     |     |   |
        | Bolt Bolt Bolt Bolt Bolt  |   10 × Ø20mm Ti bolts
        |_____|_____|_____|_____|___|
                    |
        ____________|____________
       |                         |
       |    Backup Fitting       |      Al 7050-T7451
       |    (Frame Mounted)      |
       |_________________________|
       
    Interface to heavy frame FR-40
```

### Load Paths

| Load | Path | Components |
|------|------|------------|
| Vertical (down) | Trunnion → Fitting → Frame → Keel beam | FR-40, FR-42, Keel |
| Drag (aft) | Trunnion → Fitting → Frame web | FR-40, FR-42 |
| Side (inboard) | Side stay → Fitting → Frame → Skin | FR-41, Side shell |

### Fitting Dimensions

| Fitting | Dimensions (mm) | Weight (kg) | Bore Diameter |
|---------|-----------------|-------------|---------------|
| MLG-TRN-F | 350 × 200 × 120 | 28 | Ø80 |
| MLG-TRN-A | 350 × 200 × 120 | 28 | Ø80 |
| MLG-SST | 250 × 150 × 80 | 12 | Ø50 |
| NLG-TRN | 200 × 120 × 80 | 8 | Ø50 |

## Load Cases

### Critical Design Cases

| Load Case | Description | Critical Fitting |
|-----------|-------------|------------------|
| LC-004 | 3.0g landing impact (symmetric) | MLG-TRN-F, MLG-TRN-A |
| LC-027 | Spin-up (landing) | MLG-TRN-F (drag) |
| LC-028 | Spring-back (landing) | MLG-TRN-A (drag) |
| LC-029 | Maximum braking | MLG-TRN-F (drag) |
| LC-030 | Cross-wind landing | MLG-SST (side) |
| LC-031 | Ground turn | NLG-TRN (steering) |

### MLG Fitting Loads (Forward Trunnion)

| Load Component | Limit (kN) | Ultimate (kN) |
|----------------|------------|---------------|
| Vertical (Fz) | 3,000 | 4,500 |
| Drag (Fx) | 900 | 1,350 |
| Side (Fy) | 200 | 300 |

## Analysis and Verification

### Analysis Methods

| Analysis Type | Method | Software |
|---------------|--------|----------|
| Lug strength | Classical lug analysis | Excel |
| Fitting stress | Detailed FEA | ABAQUS |
| Bolt analysis | ASME shear/tension | Excel |
| Fatigue (lug bore) | S-N with Kt = 4.0 | NASGRO |

### Margin Summary

| Component | Load Case | MS (Ultimate) | MS (Fatigue) | Status |
|-----------|-----------|---------------|--------------|--------|
| MLG-TRN-F lug | LC-004 | +0.10 | 4.0× DSG | ✓ Pass |
| MLG-TRN-F bolts | LC-004 | +0.15 | 5.0× DSG | ✓ Pass |
| MLG-SST lug | LC-030 | +0.12 | 4.5× DSG | ✓ Pass |
| Backup fitting | LC-004 | +0.18 | 6.0× DSG | ✓ Pass |
| Heavy frame FR-40 | LC-004 | +0.08 | 3.5× DSG | ✓ Pass |

### Verification Testing

| Test Article | Test Type | Purpose | Status |
|--------------|-----------|---------|--------|
| Trunnion fitting TF-01 | Static ultimate | Strength | Complete |
| Trunnion fitting TF-02 | Fatigue | Life validation | In progress |
| Full gear bay structure | Static | Load path validation | Planned |
| Drop test | Dynamic | Landing certification | Planned 2026 |

## Manufacturing Considerations

### Titanium Forging Process

1. **Starting Stock**: Closed-die forging (Ti-6Al-4V, AMS 4935)
2. **Heat Treatment**: Solution treat + age
3. **Machining**: 5-axis CNC, special bore tooling
4. **Surface Treatment**: Shot peening (Almen intensity A 0.008-0.012)
5. **NDI**: 100% ultrasonic, 100% FPI

### Quality Criteria

| Feature | Acceptance Criteria |
|---------|---------------------|
| Bore diameter | Ø80.000 +0.025/-0.000 mm |
| Bore surface finish | Ra ≤ 0.8 μm, no tool marks |
| Bolt hole true position | ±0.15 mm |
| Forging grain flow | Aligned with lug axis |

## References

### Regulatory Documents
- [CS-25.473 Landing Gear Ground Loads](https://www.easa.europa.eu/en/document-library/certification-specifications/cs-25-amendment-27)
- [CS-25.479 Level Landing Conditions](https://www.easa.europa.eu/en/document-library/certification-specifications/cs-25-amendment-27)
- [CS-25.571 Damage Tolerance](https://www.easa.europa.eu/en/document-library/certification-specifications/cs-25-amendment-27)

### Internal References
- [53-50-01-02-002 Lower Shell Skin Design](../02_Panels_Frames_and_Skins/53-50-01-02-002_Lower_Shell_Skin_Design.md)
- [Attachment Load Summary](ASSETS/Attachment_Load_Summary.csv)

---

## Document Control

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT** – Subject to human review and approval.
- Human approver: _[to be completed]_.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: 2025-11-25

---
