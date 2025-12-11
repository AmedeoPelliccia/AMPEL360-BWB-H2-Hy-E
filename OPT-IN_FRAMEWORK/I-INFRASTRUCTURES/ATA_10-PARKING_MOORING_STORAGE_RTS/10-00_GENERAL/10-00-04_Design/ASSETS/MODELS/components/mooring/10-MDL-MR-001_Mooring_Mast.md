# 10-MDL-MR-001 — Mooring Mast

## 1. Purpose

Permanent or semi-permanent mooring mast structure for securing aircraft during long-term outdoor storage or high-wind conditions. Provides elevated attachment points for mooring cables to improve load distribution and wind resistance.

## 2. Scope

This component applies to:

- **Aircraft Type**: AMPEL360-BWB-H2-Hy-E (and general use)
- **Installation**: Permanent outdoor parking areas
- **Load Capacity**: 200 kN total (distributed across attachment points)

## 3. Model Information

| Parameter | Value |
|-----------|-------|
| Model Number | 10-MDL-MR-001 |
| Model Type | Component |
| Component Category | Mooring |
| CAD System | CATIA V6 |
| Version | 1.0 |
| Status | ACTIVE |

## 4. Available Formats

| Format | Filename | Location | Checksum |
|--------|----------|----------|----------|
| CATIA V6 | 10-MDL-MR-001_Mooring_Mast.CATPart | `cad-native/catia/` | TBD |
| STEP | 10-MDL-MR-001_Mooring_Mast.step | `exchange-formats/step/` | TBD |
| STL | 10-MDL-MR-001_Mooring_Mast.stl | `visualization/stl/` | TBD |

## 5. Geometry Description

**Structure Type:** Tubular steel mast

**Dimensions:**
- Total Height: 6000 mm above ground
- Base Diameter: 250 mm (Ø 250 x 12 mm wall)
- Top Diameter: 180 mm (Ø 180 x 10 mm wall)
- Taper: Linear from base to top
- Foundation Depth: 1500 mm below ground
- Base Plate: 500 x 500 x 25 mm

**Attachment Points:**
- Primary ring (top): 80 kN capacity
- Secondary ring (mid-height): 40 kN capacity
- Guy wire lugs (4x): 30 kN each

**Features:**
- Lightning rod terminal at top
- Access ladder (if required by local codes)
- H2 detector mounting bracket
- Wind sock mounting provision

## 6. Materials

| Part | Material | Specification |
|------|----------|---------------|
| Mast Tube | Steel Tube | ASTM A500 Grade C |
| Base Plate | Steel Plate | ASTM A36 |
| Mooring Rings | Forged Steel | ASTM A668 |
| Anchor Bolts | High-Strength Steel | ASTM F1554 Gr. 105 |
| Foundation | Reinforced Concrete | fc' ≥ 30 MPa |
| Lightning Rod | Copper | UL 96A |
| Finish | Hot-Dip Galvanizing | ASTM A123 |

**Material Properties (ASTM A500 Grade C):**
- Tensile Strength: 427 MPa
- Yield Strength: 317 MPa
- Elongation: 23% minimum

## 7. H2/BWB Considerations

**H2 Safety Integration:**
- H2 detector housing integrated at 2m height
- Lightning protection for static discharge
- Electrical grounding to prevent sparks
- Located outside primary H2 zone (10m radius)

**BWB-Specific Layout:**
- Mast height optimized for BWB wingspan
- 4 masts positioned at 45° angles around aircraft
- Spacing accommodates 80m wingspan

**Wind Load Analysis:**
- Designed for 75 m/s wind speed
- Dynamic response analyzed for gusts
- Foundation sized for soil bearing capacity

## 8. Related Documentation

### Related Assemblies
- [10-MDL-ASM-003 — Mooring Equipment Assembly](../../assemblies/10-MDL-ASM-003_Mooring_Equipment_Assembly.md)

### Related Components
- [10-MDL-MR-002 — Mooring Cable](./10-MDL-MR-002_Mooring_Cable.md)
- [10-MDL-MR-003 — Mooring Clamp](./10-MDL-MR-003_Mooring_Clamp.md)
- [10-MDL-H2-002 — H2 Detector Housing](../h2-systems/10-MDL-H2-002_H2_Detector_Housing.md)

### Related Simulations
- [10-SIM-FEA-002 — Mooring Stress Analysis](../../simulations/fea/10-SIM-FEA-002_Mooring_Stress_Analysis.md)

### Related Standards
- **ASTM A500** — Cold-formed welded and seamless carbon steel structural tubing
- **ASCE 7** — Minimum design loads
- **UL 96A** — Lightning protection

## 9. Revision History

| Rev | Date | Author | Description |
|-----|------|--------|-------------|
| 1.0 | 2025-12-09 | AMPEL360 Design Team | Initial release |

---

## Document Control

- **Document ID**: 10-MDL-MR-001
- **Version**: 1.0
- **Status**: ACTIVE
- **Last Updated**: 2025-12-09
- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
