# STRUCTURAL Models

**Purpose**: Finite element and analytical structural models for propulsor components including blades, gearbox, motor, and mounting systems.

---

## Overview

This directory contains structural analysis models supporting:

- Static stress and deflection analysis
- Dynamic/modal analysis and vibration prediction
- Fatigue and damage tolerance assessment
- Rotordynamics and bearing analysis
- Bird strike and foreign object damage (FOD)

---

## Subdirectories

### FAN_BLADE/

Fan blade structural integrity models:

| Model ID | Description | Analysis Type |
|----------|-------------|---------------|
| Q100-61-MDL-STR-FAN-BLADE-STATIC | Static stress under centrifugal + aero loads | Linear/Nonlinear FEA |
| Q100-61-MDL-STR-FAN-BLADE-DYNAMIC | Modal and flutter analysis | Dynamic FEA |

### GEARBOX/

Reduction gearbox structural models:

| Model ID | Description | Analysis Type |
|----------|-------------|---------------|
| Q100-61-MDL-STR-GEARBOX-HOUSING | Housing stress and stiffness | FEA |
| Q100-61-MDL-STR-GEARBOX-GEARS | Gear tooth contact stress | Contact FEA |

### MOTOR/

Electric motor structural models:

| Model ID | Description | Analysis Type |
|----------|-------------|---------------|
| Q100-61-MDL-STR-MOTOR-ROTOR | Rotor dynamics and critical speeds | Rotordynamic FEA |
| Q100-61-MDL-STR-MOTOR-HOUSING | Housing structural analysis | FEA |

### MOUNTING/

Propulsor mount system models:

| Model ID | Description | Analysis Type |
|----------|-------------|---------------|
| Q100-61-MDL-STR-MOUNT-SYSTEM | Mount loads and deflections | FEA |

---

## Analysis Methods

### Static FEA

- **Software**: ANSYS Mechanical, Abaqus, Nastran
- **Element Types**: SOLID186/187, SHELL181, BEAM188
- **Material Models**: Linear elastic, plasticity for limit load
- **Load Cases**: 1g, 2.5g, gust, emergency landing

### Dynamic Analysis

- **Modal Analysis**: Natural frequencies and mode shapes
- **Harmonic Response**: Vibration amplitude at running speeds
- **Flutter Analysis**: Coupled aero-structural stability

### Rotordynamics

- **Campbell Diagrams**: Critical speed mapping
- **Unbalance Response**: Vibration at bearing locations
- **Bearing Stiffness/Damping**: Parametric studies

---

## Key Outputs

1. **Stress Contours**: Von Mises, principal stresses
2. **Displacement Plots**: Deflection under load
3. **Mode Shapes**: Vibration patterns and frequencies
4. **Campbell Diagrams**: Critical speed analysis
5. **Fatigue Life**: Cycles to failure predictions
6. **Margins of Safety**: MS calculations per load case

---

## Material References

See `MODEL_LIBRARY/MATERIALS/` for:

- Q100-61-MAT-COMPOSITE-CFRP (fan blades)
- Q100-61-MAT-TITANIUM-TI6AL4V (disk, hub)
- Q100-61-MAT-ALUMINUM-7075 (housing)
- Q100-61-MAT-STEEL-4340 (gears, shafts)

---

## Traceability

- Requirements: See `61-00-03_Requirements/`
- Validation: See `61-00-07_V_AND_V/`
- Certification: CS-25.571, CS-25.613, CS-25.629

---

## Document Control

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT** – Subject to human review and approval.
- Human approver: _[to be completed]_.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: 2025-12-05
