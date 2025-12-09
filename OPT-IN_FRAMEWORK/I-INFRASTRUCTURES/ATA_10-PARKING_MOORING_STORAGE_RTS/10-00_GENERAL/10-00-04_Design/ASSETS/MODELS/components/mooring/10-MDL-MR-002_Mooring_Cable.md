# 10-MDL-MR-002 — Mooring Cable

## 1. Purpose

High-strength wire rope mooring cable assembly for securing aircraft to mooring masts. Designed for continuous outdoor exposure and high-cycle fatigue loading from wind oscillations.

## 2. Scope

This component applies to:

- **Aircraft Type**: AMPEL360-BWB-H2-Hy-E
- **Usage**: Mooring system (8 cables per aircraft)
- **Load Capacity**: 120 kN breaking strength (minimum)

## 3. Model Information

| Parameter | Value |
|-----------|-------|
| Model Number | 10-MDL-MR-002 |
| Model Type | Component |
| Component Category | Mooring |
| CAD System | SolidWorks |
| Version | 1.0 |
| Status | ACTIVE |

## 4. Available Formats

| Format | Filename | Location | Checksum |
|--------|----------|----------|----------|
| SolidWorks | 10-MDL-MR-002_Mooring_Cable.sldprt | `cad-native/solidworks/` | TBD |
| STEP | 10-MDL-MR-002_Mooring_Cable.step | `exchange-formats/step/` | TBD |

## 5. Geometry Description

**Cable Specification:**
- Construction: 7x19 wire rope
- Diameter: 16 mm
- Length: 15-20 m (adjustable)
- Core: Independent wire rope core (IWRC)

**End Terminations:**
- Both ends: Swaged eye terminals
- Eye inner diameter: 50 mm
- Terminal length: 200 mm

**Hardware:**
- Turnbuckle for tension adjustment
- Load indicator integrated
- Safety lockwire provisions

## 6. Materials

| Part | Material | Specification |
|------|----------|---------------|
| Wire Rope | Stainless Steel 316 | MIL-DTL-83420 Type II |
| Eye Terminals | Stainless Steel 316L | ASTM A582 |
| Turnbuckle | Stainless Steel 316 | Federal Spec. FF-T-791b |
| Thimbles | Galvanized Steel | ASTM A153 |

**Cable Properties:**
- Breaking Strength: 120 kN minimum
- Working Load Limit: 24 kN (safety factor 5)
- Fatigue Life: 2 million cycles at 40% WLL
- Corrosion Resistance: Excellent (316 SS)

## 7. H2/BWB Considerations

**H2 Safety:**
- Stainless steel construction (non-sparking)
- Grounding wire integrated in assembly
- No sharp edges or protrusions
- Fire-resistant coating applied

**BWB Application:**
- Cable lengths sized for BWB wingspan
- Angle of attachment optimized for wing loads
- Multiple cables distribute loads across structure

## 8. Related Documentation

### Related Assemblies
- [10-MDL-ASM-003 — Mooring Equipment Assembly](../../assemblies/10-MDL-ASM-003_Mooring_Equipment_Assembly.md)

### Related Components
- [10-MDL-MR-001 — Mooring Mast](./10-MDL-MR-001_Mooring_Mast.md)
- [10-MDL-MR-003 — Mooring Clamp](./10-MDL-MR-003_Mooring_Clamp.md)

### Related Standards
- **MIL-DTL-83420** — Cable assembly, tiedown
- **ASTM A582** — Free-machining stainless steel wire
- **Federal Spec. FF-T-791b** — Turnbuckles

## 9. Revision History

| Rev | Date | Author | Description |
|-----|------|--------|-------------|
| 1.0 | 2025-12-09 | AMPEL360 Design Team | Initial release |

---

## Document Control

- **Document ID**: 10-MDL-MR-002
- **Version**: 1.0
- **Status**: ACTIVE
- **Last Updated**: 2025-12-09
- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
