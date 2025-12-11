# 10-MDL-TD-001 — Tiedown Ring

## 1. Purpose

Aircraft-mounted tiedown ring for securing the AMPEL360-BWB-H2 aircraft during parking and storage operations. This ring provides a high-strength attachment point for tiedown cables and is integrated into the aircraft primary structure.

## 2. Scope

This component applies to:

- **Aircraft Type**: AMPEL360-BWB-H2-Hy-E
- **Installation Locations**: 6 positions (4x wing, 1x nose, 1x tail)
- **Load Capacity**: 50 kN (wing points), 30 kN (nose/tail points)

## 3. Model Information

| Parameter | Value |
|-----------|-------|
| Model Number | 10-MDL-TD-001 |
| Model Type | Component |
| Component Category | Tiedown |
| CAD System | SolidWorks |
| Version | 1.0 |
| Status | ACTIVE |

## 4. Available Formats

| Format | Filename | Location | Checksum |
|--------|----------|----------|----------|
| SolidWorks | 10-MDL-TD-001_Tiedown_Ring.sldprt | `cad-native/solidworks/` | TBD |
| STEP | 10-MDL-TD-001_Tiedown_Ring.step | `exchange-formats/step/` | TBD |
| STL | 10-MDL-TD-001_Tiedown_Ring.stl | `visualization/stl/` | TBD |

## 5. Geometry Description

**Overall Dimensions:**
- Outer Diameter: 80 mm
- Inner Diameter: 40 mm (clear opening for shackle)
- Thickness: 20 mm
- Height above surface: 15 mm
- Base mounting pattern: 4x M12 bolts on 100 mm PCD

**Design Features:**
- Recessed design for aerodynamic smoothness
- Chamfered edges to prevent cable wear
- Inspection hole for crack detection
- Corrosion-resistant finish

## 6. Materials

| Part | Material | Specification |
|------|----------|---------------|
| Ring Body | Aluminum Alloy 7075-T6 | AMS 4078 |
| Mounting Bolts | Titanium Ti-6Al-4V | AMS 4967 |
| Washers | Stainless Steel 316 | AMS 5524 |

**Material Properties (7075-T6):**
- Tensile Strength: 572 MPa
- Yield Strength: 503 MPa
- Density: 2.81 g/cm³
- Corrosion Resistance: Good (with anodizing)

## 7. H2/BWB Considerations

**BWB Integration:**
- Tiedown rings integrated into wing box primary structure
- Load path through main wing spars
- Flush mounting minimizes drag
- Accessible from wing trailing edge

**H2 Safety:**
- Located outside primary H2 safety zones
- Non-sparking aluminum construction
- Grounding provision integrated

## 8. Related Documentation

### Related Assemblies
- [10-MDL-ASM-002 — Tiedown System Assembly](../../assemblies/10-MDL-ASM-002_Tiedown_System_Assembly.md)

### Related Components
- [10-MDL-TD-002 — Tiedown Fitting](./10-MDL-TD-002_Tiedown_Fitting.md)
- [10-MDL-TD-003 — Ground Anchor](./10-MDL-TD-003_Ground_Anchor.md)

### Related Specifications
- TBD: REQ-10-201 — Tiedown Ring Strength Requirements

### Related Standards
- **MIL-DTL-83420** — Tiedown provisions
- **CS-25.561** — Emergency landing conditions (structural reference)

## 9. Revision History

| Rev | Date | Author | Description |
|-----|------|--------|-------------|
| 1.0 | 2025-12-09 | AMPEL360 Design Team | Initial release |

---

## Document Control

- **Document ID**: 10-MDL-TD-001
- **Version**: 1.0
- **Status**: ACTIVE
- **Last Updated**: 2025-12-09
- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
