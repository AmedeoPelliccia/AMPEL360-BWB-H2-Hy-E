# ICD — ATA 21 ECS Ventilation/Purge Interface

## 1. Purpose

This Interface Control Document defines the interface between ATA 28 Fuel System and ATA 21 Air Conditioning/Environmental Control System for ventilation and purge functions.

## 2. Interface Description

| Interface | Direction | Description |
|-----------|-----------|-------------|
| Purge Air Supply | ATA 21 → ATA 28 | Conditioned air for fuel system purging |
| Ventilation Exhaust | ATA 28 → ATA 21 | Exhaust from fuel bay ventilation |
| Temperature Control | Bidirectional | Thermal management coordination |

## 3. Data Exchange

| Signal | Type | Range | Units | Update Rate |
|--------|------|-------|-------|-------------|
| PURGE_AIR_TEMP | Analog | -40 to +85 | °C | 1 Hz |
| PURGE_AIR_FLOW | Analog | 0 to 500 | kg/h | 1 Hz |
| VENT_REQ | Discrete | 0/1 | - | On change |

## 4. References

- [ATA 21 Air Conditioning](https://www.easa.europa.eu/en/document-library/certification-specifications/cs-25-large-aeroplanes) — CS-25.831
- [CS-25.1309](https://www.easa.europa.eu/en/document-library/certification-specifications/cs-25-large-aeroplanes) — Equipment, systems, and installations

---

## Document Control

- Status: **DRAFT**
- Repository: `AMPEL360-AIR-T`

---
