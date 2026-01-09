# ICD — ATA 73 Powerplant/Fuel Cell Boundary Interface

## 1. Purpose

This Interface Control Document defines the interface between ATA 28 Fuel System and ATA 73 Engine Fuel and Control (or Fuel Cell System) at the engine/fuel cell boundary.

## 2. Interface Description

| Interface | Direction | Description |
|-----------|-----------|-------------|
| GH2 Supply | ATA 28 → ATA 73 | Gaseous hydrogen to fuel cell/engine |
| Fuel Demand Signal | ATA 73 → ATA 28 | Fuel flow rate request |
| Shutoff Valve Control | Bidirectional | Emergency fuel isolation |

## 3. Fuel Delivery Requirements

| Parameter | Normal | Max | Units |
|-----------|--------|-----|-------|
| GH2 Flow Rate | 50 | 150 | kg/h |
| Delivery Pressure | 300 | 400 | kPa |
| Delivery Temperature | 20 | 80 | °C |

## 4. Data Exchange

| Signal | Type | Range | Units | Update Rate |
|--------|------|-------|-------|-------------|
| FUEL_DEMAND | Analog | 0 to 150 | kg/h | 100 Hz |
| FUEL_FLOW_ACTUAL | Analog | 0 to 150 | kg/h | 100 Hz |
| FC_SHUTOFF_CMD | Discrete | 0/1 | - | On change |
| FC_SHUTOFF_CONF | Discrete | 0/1 | - | On change |

## 5. References

- [CS-25.903](https://www.easa.europa.eu/en/document-library/certification-specifications/cs-25-large-aeroplanes) — Engines
- [CS-25.1181](https://www.easa.europa.eu/en/document-library/certification-specifications/cs-25-large-aeroplanes) — Designated fire zones

---

## Document Control

- Status: **DRAFT**
- Repository: `AMPEL360-AIR-T`

---
