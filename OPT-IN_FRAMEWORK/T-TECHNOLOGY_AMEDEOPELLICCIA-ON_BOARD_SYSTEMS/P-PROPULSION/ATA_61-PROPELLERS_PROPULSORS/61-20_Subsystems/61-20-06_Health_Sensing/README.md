# 61-20-06_Health_Sensing — ATA 61 Subsystem

## Purpose

Health sensing subsystem for EDF propulsors. Provides real-time monitoring of propulsor health through vibration, strain, temperature, and electromagnetic sensors.

## Scope

This subsystem covers the sensor systems used for condition monitoring, predictive maintenance, and fault detection in the AMPEL360 Q100 propulsion system.

## Sensor Types

- **Vibration Sensors**: Accelerometers for rotor imbalance and bearing health
- **Strain Gauges**: Blade and structural load monitoring
- **Temperature Sensors**: Motor winding, bearing, and cooling fluid temperatures
- **EM Sensors**: Electromagnetic field monitoring for motor health

## Contents

This folder should contain:
- Sensor specifications and selection criteria
- Sensor placement diagrams
- Data acquisition architecture
- Health monitoring algorithms (see also 61-40_Software)
- Predictive maintenance integration

## Interfaces

- **61-20-01_Electric_Motor**: Motor health sensing
- **61-20-02_Ducted_Fan**: Fan vibration and blade health
- **61-20-04_Propulsor_Control_Unit**: Sensor data interface
- **61-40_Software**: Health monitoring and ML diagnostics
- **ATA 45**: Central maintenance system integration
- **ATA 95**: Digital Product Passport data logging

## Status

- **Subsystem ID**: 61-20-06
- **Status**: Active
- **Last Updated**: 2025-12-01

## Document Control

- **Standard**: OPT-IN Framework v1.1
- **Owner**: AMPEL360 Propulsion Team

---

**Note**: This folder is part of the 61-20_Subsystems bucket under ATA 61 — Propellers/Propulsors.
