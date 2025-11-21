# 85-20-07 — Stand and Gate Infrastructure Subsystem

## Subsystem Metadata

```yaml
subsystem_id: "85-20-07"
name: "Stand_and_Gate_Infrastructure_Subsystem"
description: "Aircraft positioning, visual guidance, ground services integration, and stand monitoring"
parent_ata: "ATA 85"
criticality: "DAL-C"
status: "active"
version: "1.0"
last_updated: "2025-11-21"
```

## Purpose

Provides ground infrastructure for safe and accurate aircraft positioning at the stand, visual guidance during taxi-in and pushback, and integration with ground service equipment.

## Key Capabilities

- Aircraft positioning system — Automated or manual guidance to parking position
- Visual guidance system — Lead-in lights, docking system, stop position indicators
- Ground services integration — GSE positioning, service coordination
- Stand monitoring and control — Camera systems, sensors, control room integration

## Criticality

**Design Assurance Level:** DAL-C (Major)

Positioning errors can cause aircraft damage or ground crew injury but typically not catastrophic.

See: [85-20-00-004_Subsystem_Criticality_Classification.md](../85-20-00-004_Subsystem_Criticality_Classification.md)

## Architecture Documents

1. [85-20-07-001_Stand_Infrastructure_Architecture.md](./85-20-07-001_Stand_Infrastructure_Architecture.md)
2. [85-20-07-002_Aircraft_Positioning_System.md](./85-20-07-002_Aircraft_Positioning_System.md)
3. [85-20-07-003_Visual_Guidance_System.md](./85-20-07-003_Visual_Guidance_System.md)
4. [85-20-07-004_Ground_Services_Integration_System.md](./85-20-07-004_Ground_Services_Integration_System.md)
5. [85-20-07-005_Stand_Monitoring_and_Control.md](./85-20-07-005_Stand_Monitoring_and_Control.md)

## Integration

**Primary Dependencies:**
- [85-20-03 Passenger Boarding](../85-20-03_Passenger_Boarding_Interface_Subsystem/README.md) — Jetway positioning (Priority 1)
- [85-20-04 Evacuation and Rescue](../85-20-04_Evacuation_and_Rescue_Interface_Subsystem/README.md) — Emergency access (Priority 1)
- [85-20-05 Cargo and Servicing](../85-20-05_Cargo_and_Servicing_Interface_Subsystem/README.md) — Cargo loader positioning (Priority 2)
- [85-20-06 Data and Communications](../85-20-06_Data_and_Communications_Interface_Subsystem/README.md) — Stand status reporting (Priority 2)

## Standards and Compliance

- [ICAO Annex 14](https://www.icao.int/safety/pages/annex-14.aspx) — Aerodromes (stand markings, lighting)
- [SAE ARP 4102/3](https://www.sae.org/standards/) — Visual docking guidance systems
- Airport-specific stand design standards

## Document Control

- **Generated with the assistance of AI (GitHub Copilot)**, prompted by **Amedeo Pelliccia**.
- **Status:** DRAFT – Subject to human review and approval.
- **Human approver:** _[to be completed]_.
- **Repository:** `AMPEL360-BWB-H2-Hy-E`
- **Last AI update:** 2025-11-21
