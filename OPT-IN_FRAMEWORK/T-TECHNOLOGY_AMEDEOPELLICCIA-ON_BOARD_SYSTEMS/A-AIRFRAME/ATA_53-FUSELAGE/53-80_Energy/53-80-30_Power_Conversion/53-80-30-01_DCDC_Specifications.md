# 53-80-30-01 — DC-DC Converter Specifications

| Field | Value |
|-------|-------|
| **Document ID** | 53-80-30-01 |
| **Version** | 1.0 |
| **Date** | 2025-11-27 |
| **Status** | DRAFT |
| **Classification** | ENERGY / CONVERSION |

---

## 1. Purpose

This document specifies the DC-DC power converters used in the ANCHORS energy system for voltage conversion and power conditioning.

## 2. Converter Inventory

| ID | Function | Input | Output | Power | Bidirectional |
|----|----------|-------|--------|-------|---------------|
| DCDC-01 | Battery Interface | 650-850 VDC | 650-850 VDC | 200 kW | Yes |
| DCDC-02 | 28V Systems | 650-850 VDC | 28 VDC | 10 kW | No |
| DCDC-03 | 270V Legacy | 650-850 VDC | 270 VDC | 30 kW | No |
| DCDC-04 | 48V Thermal | 650-850 VDC | 48 VDC | 25 kW | No |

## 3. DCDC-01: Battery Interface Converter

### 3.1 Specifications

| Parameter | Value | Unit |
|-----------|-------|------|
| Topology | Dual Active Bridge | — |
| Input voltage | 650-850 | VDC |
| Output voltage | 650-850 | VDC |
| Power rating | 200 | kW |
| Peak power (30 s) | 250 | kW |
| Efficiency (full load) | 98% | — |
| Efficiency (25% load) | 96% | — |
| Switching frequency | 100 | kHz |
| Isolation | 2500 | VAC |
| Weight | 45 | kg |
| Cooling | Liquid | — |

### 3.2 Operating Modes

| Mode | Direction | Power | Application |
|------|-----------|-------|-------------|
| CHARGE | Bus → Battery | 200 kW | FC excess, regen |
| DISCHARGE | Battery → Bus | 200 kW | Peak demand |
| STANDBY | — | 0.5 kW | Idle, monitoring |
| PRECHARGE | Bus → Battery | 10 kW | Startup |

## 4. DCDC-02: 28V Systems Converter

### 4.1 Specifications

| Parameter | Value | Unit |
|-----------|-------|------|
| Topology | Phase-shifted full bridge | — |
| Input voltage | 650-850 | VDC |
| Output voltage | 28 | VDC |
| Output tolerance | ±2% | — |
| Power rating | 10 | kW |
| Efficiency | 94% | — |
| Switching frequency | 150 | kHz |
| Ripple | < 100 | mVpp |
| Weight | 8 | kg |
| Cooling | Air forced | — |

### 4.2 Load Allocation

| Load | Power | Priority |
|------|-------|----------|
| Avionics | 3 kW | 1 |
| Control systems | 2 kW | 1 |
| Sensors | 1 kW | 1 |
| Lighting | 2 kW | 3 |
| Miscellaneous | 2 kW | 4 |

## 5. DCDC-03: 270V Legacy Converter

### 5.1 Specifications

| Parameter | Value | Unit |
|-----------|-------|------|
| Input voltage | 650-850 | VDC |
| Output voltage | 270 | VDC |
| Output tolerance | ±5% | — |
| Power rating | 30 | kW |
| Efficiency | 96% | — |
| Weight | 12 | kg |
| Cooling | Liquid | — |

## 6. DCDC-04: 48V Thermal Converter

### 6.1 Specifications

| Parameter | Value | Unit |
|-----------|-------|------|
| Input voltage | 650-850 | VDC |
| Output voltage | 48 | VDC |
| Output tolerance | ±3% | — |
| Power rating | 25 | kW |
| Efficiency | 95% | — |
| Weight | 10 | kg |
| Cooling | Air forced | — |

### 6.2 Load Allocation

| Load | Power |
|------|-------|
| HT circulation pump | 3 kW |
| LT circulation pump | 4 kW |
| Radiator fans | 4 kW |
| Valve actuators | 2 kW |
| Reserve | 12 kW |

## 7. Protection Features

| Protection | DCDC-01 | DCDC-02 | DCDC-03 | DCDC-04 |
|------------|---------|---------|---------|---------|
| Input overvoltage | 900 VDC | 900 VDC | 900 VDC | 900 VDC |
| Input undervoltage | 600 VDC | 600 VDC | 600 VDC | 600 VDC |
| Output overvoltage | 880 VDC | 30 VDC | 285 VDC | 52 VDC |
| Overcurrent | 120% | 120% | 120% | 120% |
| Overtemperature | 85°C | 85°C | 85°C | 85°C |
| Short circuit | Yes | Yes | Yes | Yes |

---

## Document Control

| Field | Value |
|-------|-------|
| **Document ID** | 53-80-30-01 |
| **Version** | 1.0 |
| **Date** | 2025-11-27 |
| **Status** | DRAFT |
| **Author** | AMPEL360 Power Electronics Team |

### AI Disclosure

- **Generated with assistance of:** AI (GitHub Copilot), prompted by **Amedeo Pelliccia**
- **Status:** DRAFT — Subject to human review and approval
- **Repository:** `AMPEL360-BWB-H2-Hy-E`
- **Last AI update:** 2025-11-27

---

*END OF DOCUMENT*
