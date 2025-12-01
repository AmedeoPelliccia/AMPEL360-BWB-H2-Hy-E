# 61-20-05_Cooling_Loop — ATA 61 Subsystem

## Purpose

Cooling loop subsystem for EDF propulsors. Manages thermal dissipation from high-power electric motors and power electronics through dedicated cooling circuits.

## Scope

This subsystem covers the design, integration, and operation of the cooling systems for propulsor components, including interfaces to cryogenic systems for enhanced thermal management.

## Cooling Configurations

- **Liquid Cooling**: Glycol-water or dielectric fluid loops
- **Oil Cooling**: Motor bearing and winding cooling
- **Cryogenic Interface**: LH₂ cold sink utilization (optional)
- **Air Cooling**: Ram air for heat exchangers

## Contents

This folder should contain:
- Cooling system architecture and schematics
- Heat exchanger specifications
- Pump and flow control specifications
- Thermal analysis and simulation results
- Interface definitions to cryogenic systems (ATA 28)

## Interfaces

- **61-20-01_Electric_Motor**: Primary heat source
- **61-20-04_Propulsor_Control_Unit**: PCU cooling requirements
- **61-80_Energy**: Thermal energy exchange
- **ATA 21**: Air conditioning system (potential heat sink)
- **ATA 28**: Fuel system (cryogenic interface)

## Status

- **Subsystem ID**: 61-20-05
- **Status**: Active
- **Last Updated**: 2025-12-01

## Document Control

- **Standard**: OPT-IN Framework v1.1
- **Owner**: AMPEL360 Propulsion Team

---

**Note**: This folder is part of the 61-20_Subsystems bucket under ATA 61 — Propellers/Propulsors.
