# 61-20-01_Electric_Motor — ATA 61 Subsystem

## Purpose

Electric motor subsystem for EDF (Electric Ducted Fan) propulsors. Each propulsor integrates a 4 MW electric motor that converts electrical power into mechanical thrust.

## Scope

This subsystem covers the design, specification, integration, and lifecycle management of the high-power electric motors used in the AMPEL360 Q100 distributed propulsion system.

## Key Specifications

- **Power Rating**: 4 MW per motor
- **Quantity**: 4 motors (4× 4 MW ducted fans)
- **Integration**: Direct-drive to ducted fan
- **Cooling Interface**: Connected to 61-20-05_Cooling_Loop

## Contents

This folder should contain:
- Motor design specifications
- Performance characteristics (torque-speed curves)
- Electrical interface requirements
- Thermal management requirements
- Certification evidence for motor systems

## Interfaces

- **61-20-02_Ducted_Fan**: Mechanical coupling
- **61-20-04_Propulsor_Control_Unit**: Control commands
- **61-20-05_Cooling_Loop**: Thermal management
- **ATA 24**: Electrical power supply
- **ATA 72**: Engine/propulsion integration

## Status

- **Subsystem ID**: 61-20-01
- **Status**: Active
- **Last Updated**: 2025-12-01

## Document Control

- **Standard**: OPT-IN Framework v1.1
- **Owner**: AMPEL360 Propulsion Team

---

**Note**: This folder is part of the 61-20_Subsystems bucket under ATA 61 — Propellers/Propulsors.
