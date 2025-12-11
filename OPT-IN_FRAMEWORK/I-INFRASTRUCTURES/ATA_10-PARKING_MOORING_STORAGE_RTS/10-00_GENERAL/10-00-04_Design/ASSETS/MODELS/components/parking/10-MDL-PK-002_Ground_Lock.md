# 10-MDL-PK-002 — Ground Lock

## 1. Purpose

Mechanical ground lock device for securing landing gear in the extended position during parking and maintenance. Provides positive mechanical lock to prevent gear collapse.

## 2. Scope

This component applies to:

- **Aircraft Type**: AMPEL360-BWB-H2-Hy-E
- **Landing Gear**: Main and nose landing gear
- **Quantity**: 3 locks per aircraft (1 per gear)

## 3. Model Information

| Parameter | Value |
|-----------|-------|
| Model Number | 10-MDL-PK-002 |
| Model Type | Component |
| Component Category | Parking |
| CAD System | SolidWorks |
| Version | 1.0 |
| Status | ACTIVE |

## 4. Available Formats

| Format | Filename | Location | Checksum |
|--------|----------|----------|----------|
| SolidWorks | 10-MDL-PK-002_Ground_Lock.sldprt | `cad-native/solidworks/` | TBD |
| STEP | 10-MDL-PK-002_Ground_Lock.step | `exchange-formats/step/` | TBD |
| STL | 10-MDL-PK-002_Ground_Lock.stl | `visualization/stl/` | TBD |

## 5. Geometry Description

**Design Type:** Adjustable scissor-type lock

**Dimensions:**
- Collapsed Length: 600 mm
- Extended Length: 900-1200 mm (adjustable)
- Width: 150 mm
- Weight: 12 kg
- Load Capacity: 150 kN

**Features:**
- Telescoping adjustment
- Positive locking mechanism
- "Remove Before Flight" streamer attachment
- Padded contact points
- Storage/transport handles

## 6. Materials

| Part | Material | Specification |
|------|----------|---------------|
| Main Structure | Aluminum Alloy 6061-T6 | AMS 4027 |
| Locking Pins | Stainless Steel 17-4PH | AMS 5643 |
| Contact Pads | Polyurethane | Non-marring |
| Hardware | Stainless Steel 316 | ASTM F593 |

## 7. H2/BWB Considerations

**BWB Landing Gear:**
- Adjustable length for BWB gear geometry
- Compatible with BWB-specific gear design
- Low weight for ground crew handling

**Safety:**
- High-visibility yellow/red color scheme
- "Remove Before Flight" streamer (1m long)
- Anti-static discharge provision

## 8. Related Documentation

### Related Assemblies
- [10-MDL-ASM-001 — BWB Parking Configuration](../../assemblies/10-MDL-ASM-001_BWB_Parking_Configuration.md)

### Related Components
- [10-MDL-PK-001 — Wheel Chock](./10-MDL-PK-001_Wheel_Chock.md)
- [10-MDL-PK-003 — Parking Brake Lock](./10-MDL-PK-003_Parking_Brake_Lock.md)

### Related Standards
- **SAE ARP5150** — Landing gear ground locks
- **MIL-HDBK-516C** — Airworthiness certification criteria

## 9. Revision History

| Rev | Date | Author | Description |
|-----|------|--------|-------------|
| 1.0 | 2025-12-09 | AMPEL360 Design Team | Initial release |

---

## Document Control

- **Document ID**: 10-MDL-PK-002
- **Version**: 1.0
- **Status**: ACTIVE
- **Last Updated**: 2025-12-09
- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
