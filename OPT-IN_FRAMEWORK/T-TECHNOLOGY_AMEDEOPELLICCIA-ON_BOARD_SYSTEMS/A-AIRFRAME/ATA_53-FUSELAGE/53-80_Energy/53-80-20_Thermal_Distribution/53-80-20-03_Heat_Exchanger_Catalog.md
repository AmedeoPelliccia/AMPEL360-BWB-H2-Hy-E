# 53-80-20-03 — Heat Exchanger Catalog

| Field | Value |
|-------|-------|
| **Document ID** | 53-80-20-03 |
| **Version** | 1.0 |
| **Date** | 2025-11-27 |
| **Status** | DRAFT |
| **Classification** | ENERGY / THERMAL |

---

## 1. Purpose

This document provides a catalog of all heat exchangers used in the ANCHORS thermal distribution system, including specifications, performance data, and interface requirements.

## 2. Heat Exchanger Summary

| HX ID | Name | Type | Capacity | Location |
|-------|------|------|----------|----------|
| HX-01 | FC Primary Cooler | Liquid-Liquid | 200 kW | FC bay |
| HX-02 | Turbine HX | Exhaust Gas-Liquid | 150 kW | Engine bay |
| HX-03 | HT/LT Coupling | Plate | 80 kW | Central |
| HX-04 | Cabin Heater | Liquid-Air | 100 kW | ATA 21 interface |
| HX-05 | De-icing HX | Liquid-Air | 50 kW | Wing LE |
| HX-06 | Main Radiator L | Liquid-Air | 100 kW | Lower fuselage |
| HX-07 | Main Radiator R | Liquid-Air | 100 kW | Lower fuselage |
| HX-08 | PCM Charging HX | Liquid-PCM | 50 kW | Storage bay |

## 3. Detailed Specifications

### 3.1 HX-01: Fuel Cell Primary Cooler

| Parameter | Value | Unit |
|-----------|-------|------|
| Type | Shell and tube | — |
| Capacity | 200 | kW |
| Hot side inlet | FC coolant, 80°C | — |
| Hot side outlet | FC coolant, 65°C | — |
| Cold side inlet | HT bus, 80°C | — |
| Cold side outlet | HT bus, 85°C | — |
| Hot side flow | 60 | L/min |
| Cold side flow | 80 | L/min |
| Pressure drop (each) | 30 | kPa |
| Material | SS316L | — |
| Weight (dry) | 15 | kg |

### 3.2 HX-02: Turbine Heat Exchanger

| Parameter | Value | Unit |
|-----------|-------|------|
| Type | Finned tube | — |
| Capacity | 150 | kW |
| Hot side | Exhaust gas, 200-400°C | — |
| Cold side inlet | HT bus, 80°C | — |
| Cold side outlet | HT bus, 90°C | — |
| Cold side flow | 40 | L/min |
| Gas pressure drop | 2 | kPa |
| Liquid pressure drop | 25 | kPa |
| Material | Inconel/SS316L | — |
| Weight (dry) | 25 | kg |

### 3.3 HX-03: HT/LT Coupling Heat Exchanger

| Parameter | Value | Unit |
|-----------|-------|------|
| Type | Plate (brazed) | — |
| Capacity | 80 | kW |
| HT side inlet | 85°C | — |
| HT side outlet | 70°C | — |
| LT side inlet | 50°C | — |
| LT side outlet | 60°C | — |
| HT side flow | 25 | L/min |
| LT side flow | 40 | L/min |
| Approach temperature | 5 | °C |
| Pressure drop (each) | 25 | kPa |
| Material | SS316L | — |
| Weight (dry) | 8 | kg |

### 3.4 HX-04: Cabin Heater

| Parameter | Value | Unit |
|-----------|-------|------|
| Type | Air handling unit coil | — |
| Capacity | 100 | kW |
| Liquid inlet | HT bus, 85°C | — |
| Liquid outlet | HT bus, 65°C | — |
| Air inlet | Cabin air, 20°C | — |
| Air outlet | Heated air, 40°C | — |
| Liquid flow | 30 | L/min |
| Air flow | 3000 | L/s |
| Liquid pressure drop | 20 | kPa |
| Air pressure drop | 200 | Pa |
| Material | Aluminum/SS | — |
| Weight (dry) | 12 | kg |

### 3.5 HX-05: De-icing Heat Exchanger

| Parameter | Value | Unit |
|-----------|-------|------|
| Type | Surface heater | — |
| Capacity | 50 | kW |
| Liquid inlet | HT bus, 85°C | — |
| Liquid outlet | HT bus, 70°C | — |
| Surface temperature | 5-15°C above ambient | — |
| Liquid flow | 15 | L/min |
| Liquid pressure drop | 40 | kPa |
| Material | Aluminum | — |
| Weight (dry) | 20 | kg |

### 3.6 HX-06/07: Main Radiators

| Parameter | Value | Unit |
|-----------|-------|------|
| Type | Fin-tube with fan | — |
| Capacity (each) | 100 | kW |
| Liquid inlet | LT bus, 55°C | — |
| Liquid outlet | LT bus, 45°C | — |
| Air inlet | Ram air / ambient | — |
| Liquid flow | 50 | L/min |
| Air flow | Variable | — |
| Fan power | 2 | kW |
| Liquid pressure drop | 20 | kPa |
| Material | Aluminum | — |
| Weight (dry) | 18 | kg |

### 3.7 HX-08: PCM Charging Heat Exchanger

| Parameter | Value | Unit |
|-----------|-------|------|
| Type | Immersed coil | — |
| Capacity | 50 | kW |
| Liquid inlet | LT bus, 55°C | — |
| Liquid outlet | LT bus, 48°C | — |
| PCM temperature | 48°C (phase change) | — |
| Liquid flow | 20 | L/min |
| Pressure drop | 15 | kPa |
| Material | Aluminum/SS | — |
| Weight (dry) | 5 | kg |

## 4. Performance Curves

### 4.1 Radiator Performance

```
┌─────────────────────────────────────────────────────────────────┐
│             RADIATOR CAPACITY vs AIR FLOW                       │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│   Capacity (kW)                                                 │
│   120│                                    ████████              │
│      │                               █████                      │
│   100│ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ██████─ ─ ─ Design Point       │
│      │                     █████                                │
│    80│                █████                                     │
│      │           █████      ΔT = 10°C (ambient to coolant)     │
│    60│      █████                                               │
│      │  ████                                                    │
│    40│██                                                        │
│      │                                                          │
│    20├────┬────┬────┬────┬────┬────┬────┬────                  │
│         1000 2000 3000 4000 5000 6000 7000                      │
│                    Air Flow (L/s)                               │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

## 5. Interface Requirements

### 5.1 Mechanical Interfaces

| HX | Inlet Connection | Outlet Connection | Mounting |
|----|------------------|-------------------|----------|
| HX-01 | DN25 Flange | DN25 Flange | Frame mount |
| HX-02 | DN25 QD | DN25 QD | Engine bay |
| HX-03 | DN20 Flange | DN20 Flange | Bracket |
| HX-04 | DN25 QD | DN25 QD | AHU integral |
| HX-05 | DN16 QD | DN16 QD | Wing structure |
| HX-06/07 | DN32 Flange | DN32 Flange | Fuselage frame |
| HX-08 | DN20 Flange | DN20 Flange | Tank integral |

### 5.2 Control Interfaces

| HX | Control Type | Signal | Interface |
|----|--------------|--------|-----------|
| HX-01 | Flow valve | 0-10V | Analog |
| HX-02 | Bypass valve | PWM | Digital |
| HX-03 | 3-way valve | 0-10V | Analog |
| HX-04 | Modulating valve | AFDX | Digital |
| HX-05 | On/Off valve | Discrete | 28V |
| HX-06/07 | Fan speed + bypass | PWM | Digital |
| HX-08 | Flow valve | 0-10V | Analog |

---

## Document Control

| Field | Value |
|-------|-------|
| **Document ID** | 53-80-20-03 |
| **Version** | 1.0 |
| **Date** | 2025-11-27 |
| **Status** | DRAFT |
| **Author** | AMPEL360 Thermal Systems Team |

### AI Disclosure

- **Generated with assistance of:** AI (GitHub Copilot), prompted by **Amedeo Pelliccia**
- **Status:** DRAFT — Subject to human review and approval
- **Repository:** `AMPEL360-BWB-H2-Hy-E`
- **Last AI update:** 2025-11-27

---

*END OF DOCUMENT*
