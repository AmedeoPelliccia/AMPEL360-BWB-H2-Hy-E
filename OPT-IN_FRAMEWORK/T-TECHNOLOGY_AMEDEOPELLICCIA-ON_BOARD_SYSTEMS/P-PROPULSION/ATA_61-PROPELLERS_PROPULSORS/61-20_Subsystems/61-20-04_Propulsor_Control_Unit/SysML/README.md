# SysML Models — 61-20-04_Propulsor_Control_Unit

This folder contains SysML 1.6 textual specifications for the Propulsor Control Unit (PCU) subsystem.

## Contents

- **ATA61_PCU.sysml** — Complete SysML package containing:
  - Block Definition Diagram (BDD) — PCU structure (Inverter, Controller, Protection, Communication)
  - Internal Block Diagram (IBD) — PCU interfaces and power/control flow
  - Requirements Diagram (REQ) — PCU-specific requirements (power, response, EMC, HIRF, protection, DAL)
  - Activity Diagram (ACT) — PCU control loop sequence
  - Parametric Diagram (PAR) — Power conversion and efficiency constraints
  - State Machine (STM) — PCU operating states

## Key Blocks

```sysml
block Propulsor_Control_Unit {
    part inverter : Power_Inverter;
    part controller : Control_Processor;
    part protection : Protection_Module;
    part communication : Comm_Interface;
    
    port thrustCommand : ThrustCommand_In;
    port motorControl : MotorControl_Out;
}

block Power_Inverter {
    part switchingModule : IGBT_Module[6];
    value nominalPower : MW = 4;
    value efficiency : percent;
}
```

## Requirements Coverage

| Requirement ID | Description |
|----------------|-------------|
| REQ-61-20-04-001 | 4 MW power at ≥ 98% efficiency |
| REQ-61-20-04-002 | Response time ≤ 50 ms |
| REQ-61-20-04-003 | DO-160G EMC compliance |
| REQ-61-20-04-004 | HIRF Level 3 operation |
| REQ-61-20-04-005 | Overcurrent trip < 10 μs |
| REQ-61-20-04-006 | Fail-operational capability |
| REQ-61-20-04-007 | DAL-A software per DO-178C |
| REQ-61-20-04-008 | 80 kW heat dissipation |

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
