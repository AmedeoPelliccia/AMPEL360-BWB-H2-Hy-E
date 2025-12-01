# 61-20-04_Propulsor_Control_Unit — ATA 61 Subsystem

## Purpose

Propulsor Control Unit (PCU) hardware subsystem. The PCU provides electronic control of the electric motor, managing power delivery, speed control, and protection functions.

## Scope

This subsystem covers the hardware design, architecture, and integration of the propulsor control electronics for the AMPEL360 Q100 EDF propulsion system.

## Key Functions

- **Power Control**: Motor speed and torque regulation
- **Protection**: Overcurrent, overvoltage, thermal protection
- **Monitoring**: Real-time motor parameter monitoring
- **Communication**: Interface to aircraft flight control systems

## Contents

This folder should contain:
- PCU hardware architecture specifications
- Power electronics design (inverter topology)
- Control algorithms and logic (see also 61-40_Software)
- EMI/EMC compliance documentation
- Environmental qualification (DO-160)

## Interfaces

- **61-20-01_Electric_Motor**: Motor control signals
- **61-20-06_Health_Sensing**: Sensor inputs for motor health
- **61-40_Software**: Control software (executed by PCU)
- **ATA 24**: Electrical power supply
- **ATA 76**: Engine controls integration

## Status

- **Subsystem ID**: 61-20-04
- **Status**: Active
- **Last Updated**: 2025-12-01

## Document Control

- **Standard**: OPT-IN Framework v1.1
- **Owner**: AMPEL360 Propulsion Team

---

**Note**: This folder is part of the 61-20_Subsystems bucket under ATA 61 — Propellers/Propulsors.
