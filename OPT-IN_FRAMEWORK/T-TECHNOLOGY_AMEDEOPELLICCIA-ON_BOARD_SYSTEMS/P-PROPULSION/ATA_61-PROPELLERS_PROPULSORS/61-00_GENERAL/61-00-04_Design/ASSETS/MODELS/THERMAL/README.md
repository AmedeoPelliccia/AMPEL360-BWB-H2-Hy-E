# THERMAL Models

**Purpose**: Thermal analysis models for heat generation, transfer, and cooling system design for propulsor components.

---

## Overview

This directory contains thermal analysis models supporting:

- Motor winding and core temperature prediction
- Cooling system sizing and performance
- Controller/power electronics thermal management
- Gearbox oil cooling design
- System-level thermal network analysis

---

## Subdirectories

### MOTOR/

Electric motor thermal management:

| Model ID | Description | Analysis Type |
|----------|-------------|---------------|
| Q100-61-MDL-THM-MOTOR | Motor thermal analysis | CFD + Network |

Subdirectories:

- `heat_sources/` — Loss maps from EM analysis
- `cooling/` — Cooling jacket geometry and flow
- `results/` — Temperature predictions

### CONTROLLER/

Power electronics thermal management:

| Model ID | Description | Analysis Type |
|----------|-------------|---------------|
| Q100-61-MDL-THM-CONTROLLER | Controller thermal analysis | CFD + Network |

Subdirectories:

- `heat_sources/` — Semiconductor loss data
- `results/` — Junction temperature predictions

### GEARBOX/

Gearbox oil cooling system:

| Model ID | Description | Analysis Type |
|----------|-------------|---------------|
| Q100-61-MDL-THM-GEARBOX | Gearbox thermal analysis | Network Model |

Subdirectories:

- `oil_cooling/` — Oil system parameters

### SYSTEM/

Propulsor-level thermal integration:

| Model ID | Description | Analysis Type |
|----------|-------------|---------------|
| Q100-61-MDL-THM-PROPULSOR-SYSTEM | Integrated thermal network | Lumped Parameter |

Subdirectories:

- `thermal_network/` — Node and resistance definitions
- `results/` — System temperature distributions

---

## Analysis Methods

### CFD Thermal

- **Software**: ANSYS CFX/Fluent, STAR-CCM+
- **Physics**: Conjugate heat transfer
- **Turbulence**: Realizable k-ε, SST
- **Boundary Conditions**: Heat flux from losses, coolant flow rate

### Thermal Network (Lumped Parameter)

- **Software**: MATLAB/Simulink, Amesim, Flowmaster
- **Nodes**: Motor windings, core, housing, coolant, ambient
- **Resistances**: Conduction, convection, radiation
- **Capacitances**: Thermal mass for transient analysis

---

## Key Inputs

1. **Heat Sources**:
   - Copper losses (I²R in windings)
   - Iron losses (hysteresis + eddy current in core)
   - Magnet losses (eddy currents in PMs)
   - Windage and friction losses
   - Gear mesh losses

2. **Cooling Parameters**:
   - Coolant type (water-glycol, oil, air)
   - Flow rate and inlet temperature
   - Heat exchanger effectiveness

3. **Operating Conditions**:
   - Ambient temperature per flight phase
   - Power profile (takeoff, climb, cruise)

---

## Key Outputs

1. **Temperature Maps**: Spatial temperature distribution
2. **Hot Spot Prediction**: Maximum winding/magnet temperature
3. **Transient Profiles**: Temperature vs. time for mission
4. **Derating Curves**: Power limit vs. ambient temperature
5. **Cooling Requirements**: Flow rate, heat rejection capacity

---

## Traceability

- Requirements: See `61-00-03_Requirements/`
- EM Model Inputs: See `ELECTROMAGNETIC/MOTOR/`
- Cooling System: See `61-20-05_Cooling_Loop/`

---

## Document Control

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT** – Subject to human review and approval.
- Human approver: _[to be completed]_.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: 2025-12-05
