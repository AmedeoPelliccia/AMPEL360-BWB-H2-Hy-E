# Finite Element Analysis (FEA) Model Standards

## Purpose

This document establishes standards for FEA modeling of AMPEL360 BWB fuselage structure to ensure consistency, accuracy, and traceability.

## General Requirements

### Software
- **Primary Tool**: ANSYS, Abaqus, or equivalent
- **Version Control**: Document software version used
- **Licensing**: Verify valid license and analyst qualification

### Model Documentation
Every FEA model must include:
- Model description and purpose
- Geometry representation
- Material properties
- Boundary conditions and loads
- Mesh details
- Analysis type and settings

## Element Types

### Shell Elements
- **Application**: Skins, frames, webs
- **Element Type**: QUAD4, QUAD8 (preferred for curved surfaces)
- **Minimum Aspect Ratio**: 1:3 (length:width)
- **Warpage**: < 10 degrees

### Solid Elements
- **Application**: Fittings, lugs, highly-loaded regions
- **Element Type**: HEX8, TET10
- **Minimum Aspect Ratio**: 1:5

### Beam Elements
- **Application**: Stringers, longerons, simple beams
- **Element Type**: BEAM2, BEAM3

## Mesh Quality Criteria

| Criterion | Target | Maximum |
|-----------|--------|---------|
| Aspect Ratio | 1:1 - 1:3 | 1:5 |
| Warpage (degrees) | < 5 | < 10 |
| Jacobian | > 0.7 | > 0.5 |
| Element Size Transition | 1:2 ratio | 1:3 ratio |

## Material Properties

- Use certified allowables from [53-50-01-01-004 Design Allowables](../../53-50-01_Primary_Structure/01_Overview/53-50-01-01-004_Design_Allowables.md)
- Document material coordinate systems
- Account for environmental conditions (hot/wet)

## Boundary Conditions

- Represent realistic constraints (avoid over-constraint)
- Document all applied loads and load cases
- Verify equilibrium (reaction forces balance applied loads)

## Analysis Types

### Linear Static
- For strength and stiffness evaluation
- Check for convergence

### Nonlinear Static
- For post-buckling, contact, large deformations
- Document solution settings and convergence criteria

### Buckling (Eigenvalue)
- For stability analysis
- Report first 5-10 modes
- Verify modes represent physical behavior

### Fatigue
- Use stress results from static analysis
- Apply fatigue spectra
- Calculate life or damage index

## Verification and Validation

### V&V Checklist
- [ ] Model represents geometry accurately
- [ ] Mesh quality acceptable
- [ ] Material properties correct
- [ ] Boundary conditions realistic
- [ ] Loads applied correctly
- [ ] Solution converged
- [ ] Results reviewed for anomalies
- [ ] Sanity check with hand calculations

### Hand Calculation Checks
- Simple beam bending for basic stress check
- Euler buckling for column stability
- Pressure vessel equations for shells

## Reporting

FEA results must include:
- Stress contour plots (von Mises, principal stresses)
- Displacement plots
- Reaction force summary
- Margin of safety calculations
- Convergence plots

---

## Document Control
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Version: 1.0
- Last Update: 2025-11-22

---
