# 85-20-03 — Passenger Boarding Interface Subsystem

## Subsystem Metadata

```yaml
subsystem_id: "85-20-03"
name: "Passenger_Boarding_Interface_Subsystem"
description: "Jetway/bridge interface, door controls, and accessibility provisions for passenger boarding"
parent_ata: "ATA 85"
criticality: "DAL-C"
status: "active"
version: "1.0"
last_updated: "2025-11-21"
```

## Purpose

Provides safe and efficient passenger boarding and deplaning interface including jetway docking, door sensors and controls, and accessibility provisions for passengers with reduced mobility (PRM).

## Key Capabilities

- Jetway docking system — Automated or manual jetway positioning and alignment
- Door interface sensors and controls — Door position, locking status, interlock signals
- PRM accessibility interface — Wheelchair lifts, assistance equipment interfaces
- Boarding monitoring — Passenger count, flow rate, safety verification

## Criticality

**Design Assurance Level:** DAL-C (Major)

Failures can cause passenger injuries but are typically not catastrophic with proper procedures and crew oversight.

See: [85-20-00-004_Subsystem_Criticality_Classification.md](../85-20-00-004_Subsystem_Criticality_Classification.md)

## Architecture Documents

1. [85-20-03-001_Boarding_Interface_Architecture.md](./85-20-03-001_Boarding_Interface_Architecture.md)
2. [85-20-03-002_Jetway_Docking_System.md](./85-20-03-002_Jetway_Docking_System.md)
3. [85-20-03-003_Door_Interface_Sensors_and_Controls.md](./85-20-03-003_Door_Interface_Sensors_and_Controls.md)
4. [85-20-03-004_PRM_Accessibility_Interface.md](./85-20-03-004_PRM_Accessibility_Interface.md)
5. [85-20-03-005_Boarding_Monitoring_System.md](./85-20-03-005_Boarding_Monitoring_System.md)

## Integration

**Primary Dependencies:**
- [85-20-04 Evacuation and Rescue](../85-20-04_Evacuation_and_Rescue_Interface_Subsystem/README.md) — Door mode coordination (Priority 1)
- [85-20-07 Stand and Gate Infrastructure](../85-20-07_Stand_and_Gate_Infrastructure_Subsystem/README.md) — Jetway positioning (Priority 1)
- [ATA 52 — Doors](../../../../../T-TECHNOLOGY_AMEDEOPELLICCIA-ON_BOARD_SYSTEMS/ATA_52-DOORS/README.md) — Aircraft door systems

## Standards and Compliance

- [CS-25.807](https://www.easa.europa.eu/en/document-library/certification-specifications/cs-25-large-aeroplanes) — Emergency exits
- [ICAO Annex 9](https://www.icao.int/safety/pages/annex-9.aspx) — Facilitation (PRM requirements)
- [ADA Standards](https://www.ada.gov/law-and-regs/design-standards/) — Accessibility (US) / similar international standards
- Airport-specific jetway interface standards

## Document Control

- **Generated with the assistance of AI (GitHub Copilot)**, prompted by **Amedeo Pelliccia**.
- **Status:** DRAFT – Subject to human review and approval.
- **Human approver:** _[to be completed]_.
- **Repository:** `AMPEL360-BWB-H2-Hy-E`
- **Last AI update:** 2025-11-21
