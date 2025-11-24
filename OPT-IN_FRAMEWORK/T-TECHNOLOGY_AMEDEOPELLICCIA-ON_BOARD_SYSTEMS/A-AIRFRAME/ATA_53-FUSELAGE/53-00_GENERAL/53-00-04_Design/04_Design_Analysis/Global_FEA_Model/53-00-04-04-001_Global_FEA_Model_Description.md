# Global FEA Model Description

## 1. Purpose

This document describes the **Global Finite Element Analysis (FEA) Model** for the AMPEL360 BWB fuselage structure (ATA 53).

---

## 2. Model Overview

### 2.1 Model Scope

The global FEA model encompasses the complete fuselage primary structure from Stations 0 to 900, including:

- Pressure shell (skins, frames, stringers)
- Floor structure
- Center wing box integration
- Landing gear bay structure
- Door cutout reinforcements
- Empennage attachment structure

### 2.2 Model Statistics

```yaml
model_statistics:
  total_elements: TBD
  node_count: TBD
  element_types:
    - CQUAD4 (shell elements for skins)
    - CBAR (beam elements for frames/stringers)
    - CROD (rod elements for fasteners)
    - RBE2/RBE3 (rigid elements for interfaces)
  coordinate_system: "Aircraft body axes (X-forward, Y-right, Z-up)"
  units:
    length: "mm"
    force: "N"
    mass: "kg"
```

---

## 3. Modeling Approach

### 3.1 Shell Representation

- Skin panels: 2D shell elements (CQUAD4)
- Average element size: 50-100mm for global model
- Refined mesh at stress concentrations

### 3.2 Beam Representation

- Frames and stringers: 1D beam elements (CBAR)
- Cross-section properties per structural drawings
- Offset from skin neutral axis

### 3.3 Connections

- Skin-to-frame: Coincident nodes + MPC/RBE2
- Frame-to-stringer: Coincident nodes
- Inter-zone splices: RBE2 with appropriate DOF

---

## 4. Material Properties

Material properties are defined in [53-00-04-04-003_Material_Properties.csv](./53-00-04-04-003_Material_Properties.csv).

### 4.1 Primary Materials

| Material ID | Description | E11 (GPa) | E22 (GPa) | G12 (GPa) | ν12 |
|-------------|-------------|-----------|-----------|-----------|-----|
| MAT-001 | CFRP IM7/8552 UD | 161 | 11.4 | 5.2 | 0.32 |
| MAT-002 | CFRP T800/3900 UD | 168 | 10.0 | 5.0 | 0.30 |
| MAT-003 | Ti-6Al-4V | 113.8 | - | 44 | 0.34 |
| MAT-004 | Al 7075-T6 | 71.7 | - | 27 | 0.33 |

---

## 5. Boundary Conditions

Boundary conditions are described in [53-00-04-04-004_Boundary_Conditions.md](./53-00-04-04-004_Boundary_Conditions.md).

### 5.1 Standard BC Set

- Wing attachment: Constrained at spar-fuselage interface
- Empennage: Appropriate for empennage attachment analysis
- Landing gear: Ground reaction point constraints

---

## 6. Load Cases

Load cases are summarized in [53-00-04-04-005_Load_Cases_Summary.csv](./53-00-04-04-005_Load_Cases_Summary.csv).

---

## 7. Model Validation

### 7.1 Static Checks

- Mass distribution comparison with weight report
- Stiffness matrix eigenvalue check
- Load equilibrium verification

### 7.2 Dynamic Checks

- Free-free modal analysis
- Comparison with GVT data (when available)

---

## 8. Document Control

- **Document ID**: 53-00-04-04-001
- **Version**: 1.0
- **Date**: 2025-11-24
- **Owner**: ATA 53 Stress Team Lead
- **Repository**: `AMPEL360-BWB-H2-Hy-E`

---

## Document Control

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT** – Subject to human review and approval.
- Human approver: _[to be completed]_.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: _2025-11-24_.

---
