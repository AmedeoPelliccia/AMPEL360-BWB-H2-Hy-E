# SysML Models — 61-20-06_Health_Sensing

This folder contains SysML 1.6 textual specifications for the Health Sensing subsystem.

## Contents

- **ATA61_Health_Sensing.sysml** — Complete SysML package containing:
  - Block Definition Diagram (BDD) — Health Sensing structure (Vibration, Strain, Temperature, EM sensors)
  - Internal Block Diagram (IBD) — Sensor interfaces and data acquisition chain
  - Requirements Diagram (REQ) — Health monitoring requirements (detection, accuracy, latency, coverage)
  - Activity Diagram (ACT) — Health monitoring process flow
  - Parametric Diagram (PAR) — Health indicator calculations
  - State Machine (STM) — Health monitoring states
  - Allocation Diagram — Sensor to component mapping

## Key Blocks

```sysml
block Health_Sensing_System {
    part vibrationSensors : Vibration_Sensor_Set;
    part strainGauges : Strain_Gauge_Set;
    part temperatureSensors : Temperature_Sensor_Set;
    part emSensors : EM_Sensor_Set;
    part dataAcquisition : DAQ_Unit;
    part signalProcessor : Signal_Processor;
}

block Vibration_Sensor_Set {
    part motorVibration : Accelerometer[3];
    part fanVibration : Accelerometer[2];
    part bearingVibration : Accelerometer[2];
}
```

## Requirements Coverage

| Requirement ID | Description |
|----------------|-------------|
| REQ-61-20-06-001 | Detect ≥ 0.5 g imbalance |
| REQ-61-20-06-002 | Bearing defect 10 FH before failure |
| REQ-61-20-06-003 | Crack detection ≥ 5 mm |
| REQ-61-20-06-004 | ±1°C temperature accuracy |
| REQ-61-20-06-005 | ≥ 50 kHz sampling rate |
| REQ-61-20-06-006 | ≤ 10 ms data latency |
| REQ-61-20-06-007 | < 1 false alarm per 1000 FH |
| REQ-61-20-06-008 | ≥ 95% failure mode coverage |
| REQ-61-20-06-009 | DPP event logging |

## Health Index Calculation

```sysml
constraint healthIndex = w1*vibHealth + w2*strainHealth + w3*tempHealth + w4*emHealth;
```

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
