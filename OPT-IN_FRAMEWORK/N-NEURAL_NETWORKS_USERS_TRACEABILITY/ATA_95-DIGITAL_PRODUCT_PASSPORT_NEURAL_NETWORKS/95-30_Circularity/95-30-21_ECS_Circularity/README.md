# 95-30-21 ECS Circularity

**ATA Chapter:** 21 - Environmental Control System  
**Version:** 1.0  
**Date:** 2025-11-17  
**Status:** ACTIVE

## Purpose

This directory contains all circularity documentation for the Environmental Control System (ECS), including air quality loops, thermal recovery, and filter management strategies.

## Scope

The ECS circularity implementation focuses on:
- **Air Recirculation**: Closed-loop cabin air management with filtration
- **Thermal Recovery**: Heat recovery from fuel cells and propulsion systems
- **Filter Lifecycle**: Optimized filter usage and reusability strategies
- **Energy Efficiency**: Minimizing ECS energy consumption through circular design

## Contents

### Overview Documents
- **95-30-21-001**: ECS Circularity Overview
- **95-30-21-002**: Air Quality and Recirculation Loops
- **95-30-21-003**: Heat Recovery and Thermal Loops
- **95-30-21-004**: Filters and Reusability Strategy
- **95-30-21-005**: Links to ATA 21 and 95-20-21 NN ECS

### Assets
- **95-30-21-A-001**: ECS Circular Flow Diagram (drawio)
- **95-30-21-A-002**: Filter Lifecycle Table (csv)
- **95-30-21-A-003**: Thermal Recovery Config (yaml)
- **95-30-21-A-004**: ECS Circularity KPI Spec (json)

## Key Circularity Loops

### Primary Loops
1. **Cabin Air Recirculation**: 90% recirculation efficiency target
2. **Fuel Cell Waste Heat → Cabin Heating**: 75% thermal recovery target
3. **Filter Lifecycle Optimization**: 95% design life utilization target

### Cross-ATA Interfaces
- **ATA-70** (Propulsion): Fuel cell thermal energy source
- **ATA-49** (APU): APU waste heat integration
- **ATA-36** (Pneumatic): Bleed air coordination

## Key Performance Indicators

- **KPI-002**: Thermal Recovery Efficiency (Fuel Cells to ECS) - Target: ≥75%
- **KPI-008**: Air Recirculation Efficiency - Target: ≥90%
- **KPI-012**: Filter Lifecycle Utilization - Target: ≥95%

## Related Documents

- [95-30-00-001](../95-30-00-001_Circularity_Overview.md): Circularity Overview
- [95-30-00-003](../95-30-00-003_Cross_ATA_Circularity_Map.csv): Cross-ATA Circularity Map
- [95-30-00-006](../00_META/95-30-00-006_Circularity_KPI_Definitions.md): KPI Definitions

## Owner

**System Lead**: ECS Lead Engineer  
**Last Updated**: 2025-11-17

---

*This directory is part of the AMPEL360 OPT-IN Framework circularity documentation.*
