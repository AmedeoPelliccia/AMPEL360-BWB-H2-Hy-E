# 85-20-02 — Electrical Power Interface Subsystem

## Subsystem Metadata

```yaml
subsystem_id: "85-20-02"
name: "Electrical_Power_Interface_Subsystem"
description: "Ground electrical power connections for GPU interface, battery charging, and power distribution"
parent_ata: "ATA 85"
criticality: "DAL-B"
status: "active"
version: "1.0"
last_updated: "2025-11-21"
```

## Purpose

Provides the ground-aircraft electrical power interface for ground power unit (GPU) connection, battery charging (including CO2 battery containers), and power distribution during ground operations.

## Key Capabilities

- Ground Power Unit (GPU) interface — 115V/200V AC, 28V DC
- Battery charging interface — High-voltage DC charging (up to 800V)
- Power distribution and protection — Circuit breakers, ground fault detection
- Power quality monitoring — Voltage, frequency, harmonics

## Criticality

**Design Assurance Level:** DAL-B (Hazardous)

Electrical faults can cause fire, shock hazard, or equipment damage but are typically not immediately catastrophic with proper protective systems.

See: [85-20-00-004_Subsystem_Criticality_Classification.md](../85-20-00-004_Subsystem_Criticality_Classification.md)

## Architecture Documents

1. [85-20-02-001_Ground_Power_Interface_Architecture.md](./85-20-02-001_Ground_Power_Interface_Architecture.md)
2. [85-20-02-002_GPU_Connection_System.md](./85-20-02-002_GPU_Connection_System.md)
3. [85-20-02-003_Battery_Charging_Interface.md](./85-20-02-003_Battery_Charging_Interface.md)
4. [85-20-02-004_Power_Distribution_and_Protection.md](./85-20-02-004_Power_Distribution_and_Protection.md)
5. [85-20-02-005_Power_Quality_Monitoring.md](./85-20-02-005_Power_Quality_Monitoring.md)

## Integration

**Primary Dependencies:**
- [85-20-09 CO2 Battery Interface](../85-20-09_CO2_Battery_Interface_Subsystem/README.md) — High-power battery charging (Priority 1)
- [85-20-06 Data and Communications](../85-20-06_Data_and_Communications_Interface_Subsystem/README.md) — Power status reporting
- [ATA 24 — Electrical Power](../../../../../T-TECHNOLOGY_AMEDEOPELLICCIA-ON_BOARD_SYSTEMS/ATA_24-ELECTRICAL_POWER/README.md) — Aircraft electrical system

## Standards and Compliance

- [SAE ARP 599](https://www.sae.org/standards/content/arp599/) — Ground support equipment
- [MIL-STD-704F](https://www.everyspec.com/MIL-STD/MIL-STD-0700-0799/MIL-STD-704F_1083/) — Aircraft electrical power characteristics
- [IEC 60364](https://webstore.iec.ch/publication/1847) — Electrical installations of buildings (grounding)
- [CS-25.1309](https://www.easa.europa.eu/en/document-library/certification-specifications/cs-25-large-aeroplanes) — Equipment, systems, and installations

## Document Control

- **Generated with the assistance of AI (GitHub Copilot)**, prompted by **Amedeo Pelliccia**.
- **Status:** DRAFT – Subject to human review and approval.
- **Human approver:** _[to be completed]_.
- **Repository:** `AMPEL360-BWB-H2-Hy-E`
- **Last AI update:** 2025-11-21
