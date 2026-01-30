# ATA 22-30 — Auto Throttle

## Overview

This section contains documentation for autothrottle/autothrust systems, including computation, mode logic, and commands to propulsion control.

## BWB + H₂ Fuel Cell Context

**BWB H₂-Electric Deltas:**
- Thrust command shaping to respect fuel cell dynamics
- Battery buffering strategy and state-of-charge management
- Inverter limits and thermal derates
- Distributed propulsion allocation logic (if multiple propulsors)
- Fuel cell system transient response constraints
- Power system mode coordination

## Scope

This section includes:
- Autothrottle mode selection and logic
- Thrust computation algorithms
- Speed hold and climb/descent thrust management
- Commands to propulsion control systems (ATA 71, 76, 78)
- Integration with FMS and flight plan management
- FADEC coordination for H₂ fuel cell systems

## Subjects

- **22-30-00**: Auto Throttle (base subject)
- Additional subjects to be defined as needed per ATA SNS extract

## Document Control

- **Section**: ATA 22-30
- **Status**: Active
- **Standard**: ATA iSpec 2200 SNS / S1000D
- **Last Updated**: 2026-01-08
