# 10-MDL-H2-001 — H2 Vent Valve

## 1. Purpose

Hydrogen vent valve for safe release of gaseous hydrogen from fuel tanks during parking and storage operations. Provides controlled venting to prevent pressure buildup while minimizing H2 release to atmosphere.

## 2. Scope

This component applies to:

- **Aircraft Type**: AMPEL360-BWB-H2-Hy-E
- **System**: H2 fuel tank venting system
- **Quantity**: 4 valves per aircraft (1 per fuel tank compartment)
- **Operating Pressure**: 0-10 bar

## 3. Model Information

| Parameter | Value |
|-----------|-------|
| Model Number | 10-MDL-H2-001 |
| Model Type | Component |
| Component Category | H2 System |
| CAD System | CATIA V6 |
| Version | 1.0 |
| Status | ACTIVE |

## 4. Available Formats

| Format | Filename | Location | Checksum |
|--------|----------|----------|----------|
| CATIA V6 | 10-MDL-H2-001_H2_Vent_Valve.CATPart | `cad-native/catia/` | TBD |
| STEP | 10-MDL-H2-001_H2_Vent_Valve.step | `exchange-formats/step/` | TBD |
| STL | 10-MDL-H2-001_H2_Vent_Valve.stl | `visualization/stl/` | TBD |

## 5. Geometry Description

**Valve Type:** Spring-loaded pressure relief valve

**Dimensions:**
- Overall Length: 150 mm
- Body Diameter: 50 mm
- Inlet Connection: 25 mm (AN fitting)
- Outlet Connection: 25 mm (AN fitting)
- Weight: 1.2 kg

**Features:**
- Adjustable set pressure (5-10 bar)
- Manual override capability
- Position indicator
- Leak detection port
- Freeze protection

## 6. Materials

| Part | Material | Specification |
|------|----------|---------------|
| Valve Body | Stainless Steel 316L | AMS 5507 |
| Seat | PTFE | Cryogenic grade |
| Spring | Inconel 718 | AMS 5662 |
| Seals | PTFE/Viton | H2 compatible |
| Fittings | Stainless Steel 316 | MS fittings |

**Material Compatibility:**
- H2 embrittlement resistant
- Cryogenic temperature rated (-253°C to +100°C)
- Fire resistant construction

## 7. H2/BWB Considerations

**H2 Safety Features:**
- Fail-safe open design
- Dual seal system
- Flame arrestor integrated
- Static dissipative materials
- Spark-proof construction

**BWB Integration:**
- Mounted on upper wing surface
- Vent outlet directed upward
- H2 detector co-located
- Lightning protection bonding

**Operational Modes:**
- **Normal Parking**: Closed, manual operation only
- **Fueling/Defueling**: Open for tank pressure control
- **Emergency**: Automatic pressure relief
- **Maintenance**: Manual override access

## 8. Related Documentation

### Related Assemblies
- [10-MDL-ASM-004 — H2 Safety Equipment Assembly](../../assemblies/10-MDL-ASM-004_H2_Safety_Equipment_Assembly.md)

### Related Components
- [10-MDL-H2-002 — H2 Detector Housing](./10-MDL-H2-002_H2_Detector_Housing.md)
- [10-MDL-H2-003 — Cryo Insulation Cover](./10-MDL-H2-003_Cryo_Insulation_Cover.md)

### Related Specifications
- TBD: REQ-10-401 — H2 Vent System Requirements

### Related Standards
- **SAE AS6968** — Hydrogen aircraft systems
- **ISO 14687** — Hydrogen fuel quality
- **SAE AIR7901** — Hydrogen propulsion for aircraft
- **API 2000** — Venting atmospheric and low-pressure storage tanks

## 9. Revision History

| Rev | Date | Author | Description |
|-----|------|--------|-------------|
| 1.0 | 2025-12-09 | AMPEL360 H2 Systems Team | Initial release |

---

## Document Control

- **Document ID**: 10-MDL-H2-001
- **Version**: 1.0
- **Status**: ACTIVE
- **Classification**: Safety Critical
- **Last Updated**: 2025-12-09
- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
