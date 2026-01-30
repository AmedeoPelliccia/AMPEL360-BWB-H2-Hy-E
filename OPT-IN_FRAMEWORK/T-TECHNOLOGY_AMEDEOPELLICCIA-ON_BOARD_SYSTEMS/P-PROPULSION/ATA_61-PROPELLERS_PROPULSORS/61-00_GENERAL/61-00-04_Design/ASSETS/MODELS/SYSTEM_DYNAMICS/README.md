# SYSTEM_DYNAMICS Models

**Purpose**: Dynamic system models for drivetrain mechanics, control systems, and power system integration for the hybrid-electric propulsor.

---

## Overview

This directory contains dynamic system models supporting:

- Drivetrain torsional vibration analysis
- Motor and pitch control system design
- Power system transient behavior
- H₂ fuel cell and CO₂ battery dynamics
- Load sharing and power management

---

## Subdirectories

### DRIVETRAIN/

Mechanical drivetrain dynamics:

| Model ID | Description | Analysis Type |
|----------|-------------|---------------|
| Q100-61-MDL-DYN-DRIVETRAIN | Torsional dynamics model | Multi-body / Lumped |

Subdirectories:

- `inertias/` — Component inertia data
- `stiffness/` — Shaft and coupling stiffness
- `damping/` — Damping coefficients
- `results/` — Natural frequencies, mode shapes

### CONTROL/

Control system models:

| Model ID | Description | Analysis Type |
|----------|-------------|---------------|
| Q100-61-MDL-DYN-MOTOR-CONTROL | Motor field-oriented control | Simulink/Modelica |
| Q100-61-MDL-DYN-PITCH-CONTROL | Variable pitch control | Simulink/Modelica |

Subdirectories for MOTOR-CONTROL:

- `controllers/` — PI/PID tuning, current/speed loops
- `plant_models/` — Motor electrical/mechanical model
- `results/` — Step response, stability margins

Subdirectories for PITCH-CONTROL:

- `pitch_actuator/` — Actuator dynamics model

### POWER_SYSTEM/

Hybrid power system dynamics:

| Model ID | Description | Analysis Type |
|----------|-------------|---------------|
| Q100-61-MDL-DYN-POWER-SYSTEM | Integrated power system | Simulink/Modelica |

Subdirectories:

- `h2_fuel_cell/` — PEM fuel cell stack model
- `co2_battery/` — CO₂ battery charge/discharge model
- `power_electronics/` — Inverter, DC-DC converter models
- `results/` — Voltage transients, load sharing

---

## Analysis Methods

### Torsional Dynamics

- **Software**: MATLAB/Simulink, Romax, SimulationX
- **Model Type**: Lumped-parameter multi-DOF
- **Outputs**: Natural frequencies, forced response, transient torques
- **Key Concern**: Resonance avoidance at operating speeds

### Control System Design

- **Software**: MATLAB/Simulink, dSPACE
- **Methods**:
  - Field-Oriented Control (FOC) for PMSM
  - PI/PID tuning for speed/torque loops
  - State-space for pitch actuation
- **Metrics**: Bandwidth, phase margin, settling time

### Power System Modeling

- **Software**: MATLAB/Simulink, Modelica (Dymola, OpenModelica)
- **Components**:
  - **H₂ PEM Fuel Cell**: Polarization curve, dynamic response, thermal coupling
  - **CO₂ Battery**: State-of-charge dynamics, charge/discharge curves
  - **Inverter**: Switching model or average model
  - **DC Bus**: Voltage regulation, capacitor sizing
- **Scenarios**: Takeoff transient, cruise steady-state, emergency power

---

## Key Models for Hybrid-Electric Integration

### Q100-61-MDL-DYN-POWER-SYSTEM

This is the critical model for hybrid-electric propulsion system design:

1. **H₂ PEM Fuel Cell Stack**:
   - Electrochemical model (Nernst equation, activation/ohmic losses)
   - Dynamic response to load changes
   - Thermal coupling with cooling system
   - H₂ supply pressure and flow effects

2. **CO₂ Battery (Closed-Loop)**:
   - Innovative peak-power buffering system
   - Charge/discharge kinetics
   - State-of-charge estimation
   - Thermal behavior during high-rate discharge

3. **Power Management**:
   - Load sharing between fuel cell and battery
   - DC bus voltage regulation
   - Fault response and reconfiguration
   - Energy optimization for mission profile

---

## Key Outputs

1. **Frequency Response**: Bode plots, Campbell diagrams
2. **Transient Response**: Step, ramp, and disturbance rejection
3. **Stability Margins**: Gain and phase margins
4. **Power Profiles**: Fuel cell vs. battery power split
5. **Voltage/Current Waveforms**: DC bus dynamics
6. **Efficiency Maps**: System efficiency vs. operating point

---

## Traceability

- Requirements: See `61-00-03_Requirements/`
- Motor Control: See `61-20-04_Propulsor_Control_Unit/`
- Power System: See `61-80_Energy/`
- Fuel Cell: See ATA 28/73 integration

---

## Document Control

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT** – Subject to human review and approval.
- Human approver: _[to be completed]_.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: 2025-12-05
