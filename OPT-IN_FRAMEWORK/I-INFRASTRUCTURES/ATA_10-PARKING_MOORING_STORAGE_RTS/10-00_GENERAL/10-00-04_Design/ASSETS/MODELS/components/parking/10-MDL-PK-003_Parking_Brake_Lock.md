# 10-MDL-PK-003 — Parking Brake Lock

## 1. Purpose

External locking device for maintaining parking brake application during extended parking periods. Prevents inadvertent brake release due to hydraulic pressure loss or system malfunction.

## 2. Scope

This component applies to:

- **Aircraft Type**: AMPEL360-BWB-H2-Hy-E
- **Brake System**: Main landing gear hydraulic brakes
- **Quantity**: 2 locks per aircraft (1 per main gear)

## 3. Model Information

| Parameter | Value |
|-----------|-------|
| Model Number | 10-MDL-PK-003 |
| Model Type | Component |
| Component Category | Parking |
| CAD System | SolidWorks |
| Version | 1.0 |
| Status | ACTIVE |

## 4. Available Formats

| Format | Filename | Location | Checksum |
|--------|----------|----------|----------|
| SolidWorks | 10-MDL-PK-003_Parking_Brake_Lock.sldprt | `cad-native/solidworks/` | TBD |
| STEP | 10-MDL-PK-003_Parking_Brake_Lock.step | `exchange-formats/step/` | TBD |
| STL | 10-MDL-PK-003_Parking_Brake_Lock.stl | `visualization/stl/` | TBD |

## 5. Geometry Description

**Design Type:** Clamp-style brake lock

**Dimensions:**
- Overall Length: 300 mm
- Width: 150 mm
- Height: 100 mm
- Weight: 3 kg
- Jaw Opening: 20-60 mm (adjustable)

**Features:**
- Ratchet locking mechanism
- Quick-release lever
- Padded brake contact surfaces
- "Remove Before Flight" tag attachment
- Corrosion-resistant finish

## 6. Materials

| Part | Material | Specification |
|------|----------|---------------|
| Body | Aluminum Alloy 7075-T6 | AMS 4078 |
| Clamp Jaws | Hardened Steel | AISI 4140 |
| Pads | Rubber | Non-marring, heat resistant |
| Hardware | Stainless Steel 316 | ASTM F593 |
| Finish | Anodized | MIL-A-8625 Type II |

## 7. H2/BWB Considerations

**BWB Application:**
- Compatible with BWB brake caliper design
- Adjustable for various brake disk thicknesses
- Lightweight for easy ground crew handling

**H2 Safety:**
- Non-sparking materials
- Static discharge provision
- High-visibility color (red/yellow)

## 8. Related Documentation

### Related Assemblies
- [10-MDL-ASM-001 — BWB Parking Configuration](../../assemblies/10-MDL-ASM-001_BWB_Parking_Configuration.md)

### Related Components
- [10-MDL-PK-001 — Wheel Chock](./10-MDL-PK-001_Wheel_Chock.md)
- [10-MDL-PK-002 — Ground Lock](./10-MDL-PK-002_Ground_Lock.md)

### Related Standards
- **SAE AS8037** — Minimum performance standards for parking brakes
- **ATA 32** — Landing gear chapter (brake systems)

## 9. Revision History

| Rev | Date | Author | Description |
|-----|------|--------|-------------|
| 1.0 | 2025-12-09 | AMPEL360 Design Team | Initial release |

---

## Document Control

- **Document ID**: 10-MDL-PK-003
- **Version**: 1.0
- **Status**: ACTIVE
- **Last Updated**: 2025-12-09
- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
