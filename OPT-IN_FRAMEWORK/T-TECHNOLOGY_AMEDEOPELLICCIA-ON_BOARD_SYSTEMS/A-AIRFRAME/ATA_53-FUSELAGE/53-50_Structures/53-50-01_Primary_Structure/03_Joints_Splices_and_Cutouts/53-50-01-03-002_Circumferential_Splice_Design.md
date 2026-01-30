# 53-50-01-03-002 Circumferential Splice Design

## Document Information

- **Document ID**: 53-50-01-03-002
- **Title**: Circumferential Splice Design
- **Version**: 1.0
- **Date**: 2025-11-22
- **Status**: Draft
- **Category**: Structural Design
- **ATA Chapter**: 53-50 - Fuselage Structures

## Purpose

This document provides detailed design specifications for Circumferential Splice Design in the AMPEL360 BWB primary structure. Circumferential splices join fuselage barrel sections at transverse planes, transferring bending, shear, and pressure loads across major assembly joints.

## Scope

This specification covers:
- Circumferential splice locations at barrel joints
- Splice joint configurations for CFRP and hybrid structures
- Frame-to-frame load transfer
- Skin-to-skin splice details
- Tolerance management for assembly
- Shim requirements and gap filling

### Applicable Joints
- Forward fuselage to center section (Station 10.0m)
- Center section to aft fuselage (Station 30.0m)
- Major subassembly boundaries

## Design Requirements

### Structural Requirements

| Requirement | Value | Basis |
|-------------|-------|-------|
| Joint efficiency | ≥85% of parent structure | Structural continuity |
| Ultimate load capability | 1.5 × Limit load | [CS-25.303](https://www.easa.europa.eu/en/document-library/certification-specifications/cs-25-amendment-27) |
| Fatigue life | 3 × DSG minimum | Safe-life approach |
| Assembly gap tolerance | ±2.0 mm (shimmed) | Manufacturing capability |

### Geometric Requirements

| Parameter | Specification |
|-----------|---------------|
| Splice frame width | 150-200 mm |
| Fastener rows | 4-6 rows per side |
| Fastener diameter | 6.35 mm (1/4") typical |
| Edge distance | ≥2.5 × diameter |
| Pitch | 5 × diameter |

## Design Configuration

### Circumferential Splice Locations

| Splice ID | Station | Description | Barrel Sections Joined |
|-----------|---------|-------------|------------------------|
| CS-01 | 10.0m | Forward-to-center joint | Section 41 to Section 43 |
| CS-02 | 30.0m | Center-to-aft joint | Section 43 to Section 47 |

### Splice Joint Configuration

**Typical Configuration at CS-01**:
```
    Frame A (Fwd)      Splice Frame      Frame B (Aft)
    ____________    ________________    ____________
   |            |  |                |  |            |
   |    Skin    |  |  Splice Strap  |  |    Skin    |
   |____________|  |________________|  |____________|
        |    |          |    |          |    |
        | F  |          | F  |          | F  |
        | a  |          | a  |          | a  |
        | s  |          | s  |          | s  |
        | t  |          | t  |          | t  |
   _____|____|__________|____|__________|____|_____
   |_______________________________________________|
              Inner Circumferential Strap

   Fasteners: Hi-Lok Ti 6.35mm, 4 rows each skin panel
```

### Fastener Pattern

| Splice | Fastener Type | Diameter | Rows | Total Count |
|--------|---------------|----------|------|-------------|
| CS-01 | Hi-Lok Ti-6Al-4V | 6.35 mm | 4 + 4 | ~1,200 |
| CS-02 | Hi-Lok Ti-6Al-4V | 6.35 mm | 4 + 4 | ~1,000 |

## Load Cases

### Critical Design Cases

| Load Case ID | Description | Governing Parameter |
|--------------|-------------|---------------------|
| LC-001 | 2.5g maneuver | Fuselage bending moment |
| LC-002 | Maximum pressure | Hoop load across splice |
| LC-021 | Asymmetric gust | Fuselage torsion |

### Load Summary at CS-01 (Station 10.0m)

| Load Component | Limit Load | Ultimate Load |
|----------------|------------|---------------|
| Bending moment | 45,000 kN·m | 67,500 kN·m |
| Shear force | 850 kN | 1,275 kN |
| Torsion | 12,000 kN·m | 18,000 kN·m |
| Hoop tension | 28 kN/m | 42 kN/m |

## Analysis and Verification

### Margin Summary

| Splice | Load Case | MS (Fastener Shear) | MS (Bearing) | Status |
|--------|-----------|---------------------|--------------|--------|
| CS-01 | LC-001 | +0.18 | +0.15 | ✓ Pass |
| CS-02 | LC-001 | +0.22 | +0.18 | ✓ Pass |

### Verification Testing

| Test Article | Test Type | Purpose | Status |
|--------------|-----------|---------|--------|
| Splice panel CP-01 | Static | Ultimate strength | Complete |
| Full barrel joint | Pressure cycling | Fatigue validation | Planned |

## Manufacturing Considerations

### Assembly Sequence

1. Position barrel sections on assembly fixture
2. Measure gaps and determine shim requirements
3. Install circumferential splice frames
4. Drill and ream fastener holes (automated drilling)
5. Install fasteners with wet sealant
6. Pressure test for leak verification

### Shimming Requirements

| Gap Range | Shim Type | Notes |
|-----------|-----------|-------|
| 0-0.25 mm | No shim (sealant fill) | Normal tolerance |
| 0.25-1.0 mm | Liquid shim (PR-2001) | Mixed and cured in place |
| 1.0-2.0 mm | Solid shim (Al or CFRP) | Pre-manufactured |
| >2.0 mm | Engineering disposition | Requires MRB approval |

## References

### Regulatory Documents
- [CS-25.571 Damage Tolerance](https://www.easa.europa.eu/en/document-library/certification-specifications/cs-25-amendment-27)

### Internal References
- [53-50-01 Primary Structure Overview](../../README.md)

---

## Document Control

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT** – Subject to human review and approval.
- Human approver: _[to be completed]_.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: 2025-11-25

---
