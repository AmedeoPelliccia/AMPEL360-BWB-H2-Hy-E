# 53-50-02-01-001 Secondary Structure Philosophy

## Document Information

- **Document ID**: 53-50-02-01-001
- **Title**: Secondary Structure Philosophy
- **Version**: 1.0
- **Date**: 2025-11-22
- **Status**: Draft
- **Category**: Structural Design
- **ATA Chapter**: 53-50 - Fuselage Structures

## Purpose

This document establishes the design philosophy for secondary structure in the AMPEL360 BWB fuselage, defining the approach to non-primary load-bearing components that support systems, equipment, and cabin interiors.

## Scope

Secondary structure includes:
- Floor structure (beams, panels, seat rails)
- Cabin interior attachments (ceiling, sidewall, overhead bins)
- Monument hard points (galleys, lavatories)
- System support brackets (ECS ducts, cable trays, hydraulics)
- Equipment mounting provisions

## Design Philosophy

### Classification

| Structure Type | Function | Design Approach |
|----------------|----------|-----------------|
| Primary | Main load path | Fail-safe, damage tolerant |
| Secondary | Support structure | Damage tolerant where critical |
| Tertiary | Non-structural | Standard design |

### Secondary Structure Principles

1. **Load Transfer**: Efficiently transfer local loads to primary structure
2. **Weight Efficiency**: Minimize weight while meeting requirements
3. **Maintainability**: Allow access and removal for maintenance
4. **Crashworthiness**: Meet emergency landing requirements per [CS-25.561](https://www.easa.europa.eu/en/document-library/certification-specifications/cs-25-amendment-27)

## Design Requirements

### Structural Requirements

| Requirement | Value | Basis |
|-------------|-------|-------|
| Floor load (passenger) | 5.0 kN/m² | CS-25.561 |
| Floor load (cargo) | 8.0 kN/m² | Operations |
| Seat rail pull | 16g forward | CS-25.561(b) |
| Overhead bin load | 4.0 kN/bay | CS-25.787 |
| Monument crash load | 9g forward | CS-25.561 |

### Material Selection

| Application | Material | Rationale |
|-------------|----------|-----------|
| Floor beams | Al 7050-T7451 | High strength, fatigue |
| Floor panels | Sandwich (Nomex core) | Light weight |
| Seat rails | Al 6061-T6 extrusion | Wearability |
| Brackets | Al 2024-T3 or CFRP | Standard, light |

## Integration Approach

### Interface with Primary Structure

- **Floor-to-Frame**: Floor beams attached to fuselage frames
- **Sidewall-to-Skin**: Liner brackets attached to frame clips
- **Overhead-to-Frame**: Bin supports attached to frame caps

### Load Path Hierarchy

```
        Passenger/Equipment Loads
                  ↓
         Secondary Structure
         (Floors, Bins, Rails)
                  ↓
         Interface Fittings
                  ↓
         Primary Structure
         (Frames, Skins)
```

## BWB-Specific Considerations

The BWB configuration presents unique challenges:
- Wide cabin floor requiring multiple support columns
- Distributed overhead bin supports across curved ceiling
- Integration of CO₂ battery bay in floor structure
- H₂ system routing provisions

## References

### Regulatory Documents
- [CS-25.561 Emergency Landing Conditions](https://www.easa.europa.eu/en/document-library/certification-specifications/cs-25-amendment-27)
- [CS-25.787 Stowage Compartments](https://www.easa.europa.eu/en/document-library/certification-specifications/cs-25-amendment-27)

### Internal References
- [53-50-02-01-002 Load Cases and Combinations](53-50-02-01-002_Load_Cases_and_Combinations.md)

---

## Document Control

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT** – Subject to human review and approval.
- Human approver: _[to be completed]_.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: 2025-11-25

---
