# SysML Models — 61-20-05_Cooling_Loop

This folder contains SysML 1.6 textual specifications for the Cooling Loop subsystem.

## Contents

- **ATA61_Cooling_Loop.sysml** — Complete SysML package containing:
  - Block Definition Diagram (BDD) — Cooling Loop structure (Pump, Heat Exchanger, Reservoir, Valves, Sensors)
  - Internal Block Diagram (IBD) — Cooling circuit interfaces and thermal flow paths
  - Requirements Diagram (REQ) — Thermal management requirements (capacity, temperature limits, flow rate)
  - Activity Diagram (ACT) — Cooling loop startup sequence
  - Parametric Diagram (PAR) — Thermal performance constraints
  - State Machine (STM) — Cooling loop operating states

## Key Blocks

```sysml
block Cooling_Loop {
    part pump : Coolant_Pump;
    part heatExchanger : Heat_Exchanger;
    part reservoir : Coolant_Reservoir;
    part valves : Valve_Set;
    part sensors : Thermal_Sensors;
    
    value designHeatLoad : kW;
    value designFlowRate : L_per_min;
}

block Cryo_Interface {
    value coldSinkTemp : K;
    value heatExchangeRate : kW;
}
```

## Requirements Coverage

| Requirement ID | Description |
|----------------|-------------|
| REQ-61-20-05-001 | ≥ 200 kW heat dissipation |
| REQ-61-20-05-002 | Motor temp < 160°C |
| REQ-61-20-05-003 | PCU junction < 125°C |
| REQ-61-20-05-004 | Equilibrium in 120 s |
| REQ-61-20-05-005 | Min 40 L/min flow rate |
| REQ-61-20-05-006 | Redundant pump capability |
| REQ-61-20-05-007 | Leak-free for 20,000 FH |
| REQ-61-20-05-008 | 50 kW cryo assist |

## Usage

These specifications can be imported into SysML-compatible tools such as:
- Cameo Systems Modeler
- OpenMBEE
- Papyrus
- Eclipse-based SysML tools

## Document Control

- **Standard:** OPT-IN Framework v1.2
- **Owner:** AMPEL360 Propulsion Team
- **Version:** 1.0
- **Last Updated:** 2025-12-01
