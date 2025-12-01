# 56-21 — Cockpit Windshields

## Overview

This subsystem covers all cockpit windshield assemblies for the AMPEL360 BWB aircraft. The unique Blended Wing Body configuration requires specialized windshield designs that accommodate the wider cockpit geometry while maintaining structural integrity and optical clarity.

## Subsystem Structure

### 56-21-00_GENERAL

General subsystem documentation including:

- Subsystem overview and architecture
- Common specifications and standards
- Safety considerations specific to BWB windshields

### 56-21-01_LRU — Forward Windshield Assembly

Primary Line Replaceable Unit containing all forward-facing cockpit windows.

**Line Replaceable Items (LRIs):**

| LRI | Component | Description |
|-----|-----------|-------------|
| LRI_01 | Left Windshield Panel | Captain-side forward view panel |
| LRI_02 | Right Windshield Panel | First Officer-side forward view panel |
| LRI_03 | Center Windshield Panel | BWB-specific center view panel |
| LRI_04 | Heating Elements | Integrated anti-ice/anti-fog elements |
| LRI_05 | Frame Retention System | Structural attachment and sealing |

## Key Interfaces

| Interface | Connected System | ATA | Description |
|-----------|------------------|-----|-------------|
| IF-56-21-001 | Window Heating Controller | 56-25 | Heating power and control |
| IF-56-21-002 | Electrical Power | 24 | Primary power supply |
| IF-56-21-003 | Rain Repellent System | 56-26 | Rain removal interfaces |
| IF-56-21-004 | Wiper Systems | 56-27 | Mechanical wiper interfaces |
| IF-56-21-005 | Flight Deck Structure | 53 | Structural mounting |

## BWB-Specific Considerations

The AMPEL360 BWB configuration requires:

1. **Wider Field of View**: Center panel (LRI_03) unique to BWB design
2. **Curved Geometry**: Panels conform to blended body contours
3. **Enhanced Structural Requirements**: Higher loads due to integrated fuselage-wing design
4. **Optical Optimization**: Reduced distortion across curved surfaces

## Related Documentation

- [LRU Overview](./56-21-01_LRU/56-21-01_001_LRU_Overview.md)
- [Window Heating System](../56-25_WindowHeating/README.md)
- [CIR Diagrams](../../56-90_Tables_Schemas_Diagrams/ATA_56-90_CIR/)

---

## Document Control

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT** – Subject to human review and approval.
- Human approver: _[to be completed]_.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: _2025-12-01_.

---
