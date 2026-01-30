# ICD — ATA 26 Fire Protection and Detection Interface

## 1. Purpose

This Interface Control Document defines the interface between ATA 28 Fuel System and ATA 26 Fire Protection System for fire/overheat detection and suppression.

## 2. Interface Description

| Interface | Direction | Description |
|-----------|-----------|-------------|
| H2 Leak Detection | ATA 28 → ATA 26 | Hydrogen concentration alerts |
| Fire Detection | ATA 26 → ATA 28 | Fuel bay fire alerts |
| Fuel Shutoff Command | ATA 26 → ATA 28 | Emergency fuel isolation |

## 3. Data Exchange

| Signal | Type | Range | Units | Update Rate |
|--------|------|-------|-------|-------------|
| H2_CONC_BAY1 | Analog | 0 to 100 | % LEL | 10 Hz |
| FIRE_DET_BAY1 | Discrete | 0/1 | - | On change |
| FUEL_SHUTOFF_CMD | Discrete | 0/1 | - | On change |

## 4. Safety Requirements

- H2 leak detection threshold: 25% LEL (Lower Explosive Limit)
- Fire detection response: < 1 second
- Fuel shutoff activation: < 2 seconds

## 5. References

- [CS-25.1181](https://www.easa.europa.eu/en/document-library/certification-specifications/cs-25-large-aeroplanes) — Designated fire zones
- [CS-25.1183](https://www.easa.europa.eu/en/document-library/certification-specifications/cs-25-large-aeroplanes) — Flammable fluid lines, fittings, and components

---

## Document Control

- Status: **DRAFT**
- Repository: `AMPEL360-AIR-T`

---
