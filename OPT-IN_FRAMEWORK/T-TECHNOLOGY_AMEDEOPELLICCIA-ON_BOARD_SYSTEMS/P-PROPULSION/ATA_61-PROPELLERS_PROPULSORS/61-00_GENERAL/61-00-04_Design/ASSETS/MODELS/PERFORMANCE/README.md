# PERFORMANCE Models

**Purpose**: System-level performance prediction models for propulsor efficiency, thrust, and mission energy consumption.

---

## Overview

This directory contains performance models supporting:

- Propulsor thrust and efficiency prediction
- Operating envelope definition
- Mission energy consumption analysis
- Range and endurance calculations
- Trade study support

---

## Models

### Q100-61-MDL-PERF-PROPULSOR

Integrated propulsor performance model:

| Subdirectory | Contents |
|--------------|----------|
| `performance_maps/` | Thrust, power, efficiency maps |
| `operating_envelope/` | Altitude, speed, temperature limits |
| `results/` | Performance predictions |

**Key Outputs**:

- Thrust vs. speed and altitude
- Propulsive efficiency η_p across flight envelope
- Power required for design points
- Off-design performance degradation

### Q100-61-MDL-PERF-MISSION

Mission-level analysis model:

| Subdirectory | Contents |
|--------------|----------|
| `mission_profiles/` | Flight profiles (range, TOFL, climb) |
| `energy_consumption/` | H₂ and battery energy usage |
| `results/` | Mission analysis outputs |

**Key Outputs**:

- Energy consumption per mission segment
- H₂ fuel weight vs. mission profile
- Battery state-of-charge trajectory
- Reserve energy requirements

---

## Analysis Methods

### Propulsor Performance

- **Inputs**:
  - Aerodynamic performance maps (from CFD/BEMT)
  - Motor efficiency maps (from EM analysis)
  - Gearbox efficiency (mechanical losses)
  - Atmospheric conditions
- **Integration**: Combine component efficiencies for system η
- **Validation**: Compare to test data as available

### Mission Analysis

- **Software**: MATLAB, Python, PIANO, Pacelab WESE
- **Method**: Segment-by-segment energy balance
- **Segments**: Taxi, takeoff, climb, cruise, descent, approach, landing
- **Constraints**: Thrust available ≥ thrust required, thermal limits

---

## Performance Metrics

| Metric | Definition | Target |
|--------|------------|--------|
| Propulsive Efficiency | η_p = Thrust × V / Shaft Power | > 85% at cruise |
| System Efficiency | η_sys = Thrust × V / Fuel Energy | > 55% at cruise |
| Specific Fuel Consumption | H₂ mass / (Thrust × time) | TBD kg/(kN·h) |
| Thrust-to-Weight | Max Thrust / Propulsor Weight | > 10:1 |
| Power Density | Max Power / Motor Mass | > 10 kW/kg |

---

## Key Flight Conditions

| Condition | Altitude | Mach | Temperature |
|-----------|----------|------|-------------|
| Takeoff | SL | 0.20 | ISA+15°C |
| Top of Climb | FL350 | 0.78 | ISA |
| Cruise | FL350 | 0.82 | ISA |
| Hot Day Takeoff | SL | 0.20 | ISA+30°C |
| Cold Day Start | SL | 0.00 | ISA-30°C |

See `MODEL_LIBRARY/STANDARD_CONDITIONS/` for detailed definitions.

---

## Integration with Other Models

```
AERODYNAMIC → Thrust/Efficiency Maps
     ↓
ELECTROMAGNETIC → Motor Efficiency
     ↓
THERMAL → Derating Limits
     ↓
SYSTEM_DYNAMICS → Power System Efficiency
     ↓
PERFORMANCE → Integrated System Performance
     ↓
MISSION ANALYSIS → Energy Consumption
```

---

## Traceability

- Requirements: See `61-00-03_Requirements/`
- Validation: See `61-00-07_V_AND_V/`
- Aircraft Performance: See ATA 05 integration

---

## Document Control

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT** – Subject to human review and approval.
- Human approver: _[to be completed]_.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: 2025-12-05
