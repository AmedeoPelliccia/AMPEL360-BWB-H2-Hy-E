# ICD — ATA 24 Electrical Power and Bonding Interface

## 1. Purpose

This Interface Control Document defines the interface between ATA 28 Fuel System and ATA 24 Electrical Power System for power supply and electrical bonding.

## 2. Interface Description

| Interface | Direction | Description |
|-----------|-----------|-------------|
| 28VDC Power | ATA 24 → ATA 28 | Primary DC power for fuel system |
| 115VAC Power | ATA 24 → ATA 28 | AC power for pumps and heaters |
| Electrical Bonding | Bidirectional | Static dissipation and lightning protection |

## 3. Electrical Requirements

| Load | Voltage | Current | Priority |
|------|---------|---------|----------|
| Fuel Pumps | 115VAC | 15A | Essential |
| Sensors | 28VDC | 2A | Essential |
| Valves | 28VDC | 5A | Essential |
| Heaters | 115VAC | 25A | Non-Essential |

## 4. References

- [CS-25.1351](https://www.easa.europa.eu/en/document-library/certification-specifications/cs-25-large-aeroplanes) — General electrical requirements
- [CS-25.1353](https://www.easa.europa.eu/en/document-library/certification-specifications/cs-25-large-aeroplanes) — Electrical equipment and installations

---

## Document Control

- Status: **DRAFT**
- Repository: `AMPEL360-AIR-T`

---
