# AERODYNAMIC Models

**Purpose**: Computational and analytical aerodynamic models for propulsor components including fan blades, propellers, and nacelles.

---

## Overview

This directory contains aerodynamic analysis models supporting:

- Fan blade performance prediction
- Propeller thrust and efficiency calculation
- Nacelle drag and flow quality assessment
- Blade-element momentum theory (BEMT) models
- Computational Fluid Dynamics (CFD) simulations

---

## Subdirectories

### FAN_BLADE/

High-bypass ratio fan blade aerodynamic models:

| Model ID | Description | Analysis Type |
|----------|-------------|---------------|
| Q100-61-MDL-AERO-FAN-BLADE-CFD | Full 3D CFD simulation | RANS/URANS CFD |
| Q100-61-MDL-AERO-FAN-BLADE-BEMT | Blade Element Momentum Theory | Analytical |

### PROPELLER/

Open-fan propeller aerodynamic models:

| Model ID | Description | Analysis Type |
|----------|-------------|---------------|
| Q100-61-MDL-AERO-PROP-CR | Contra-rotating propeller CFD | CFD |
| Q100-61-MDL-AERO-PROP-VP | Variable pitch propeller | BEMT + CFD |

### NACELLE/

Nacelle flow and drag models:

| Model ID | Description | Analysis Type |
|----------|-------------|---------------|
| Q100-61-MDL-AERO-NACELLE-EXT | External nacelle flow | CFD |
| Q100-61-MDL-AERO-NACELLE-INT | Internal duct flow | CFD |

---

## Analysis Methods

### CFD (Computational Fluid Dynamics)

- **Software**: ANSYS Fluent, OpenFOAM, or equivalent
- **Mesh**: Structured/unstructured hybrid
- **Turbulence**: k-ω SST, Spalart-Allmaras
- **Boundary Conditions**: Total pressure inlet, static pressure outlet

### BEMT (Blade Element Momentum Theory)

- **Software**: MATLAB/Python custom codes, XROTOR
- **Inputs**: Airfoil polars, blade geometry, operating conditions
- **Outputs**: Thrust, torque, efficiency vs. advance ratio

---

## Key Outputs

1. **Performance Maps**: Thrust, torque, power vs. RPM and flight condition
2. **Pressure Distributions**: Cp plots for blade sections
3. **Flow Visualization**: Streamlines, velocity contours
4. **Efficiency Predictions**: Propulsive efficiency across envelope

---

## Traceability

- Requirements: See `61-00-03_Requirements/`
- Validation: See `61-00-07_V_AND_V/`
- Geometry: See `ASSETS/PARTS/` and `ASSETS/ASSEMBLIES/`

---

## Document Control

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT** – Subject to human review and approval.
- Human approver: _[to be completed]_.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: 2025-12-05
