# 53-80-20-02 — Coolant System Specification

| Field | Value |
|-------|-------|
| **Document ID** | 53-80-20-02 |
| **Version** | 1.0 |
| **Date** | 2025-11-27 |
| **Status** | DRAFT |
| **Classification** | ENERGY / THERMAL |

---

## 1. Purpose

This document specifies the coolant system for the ANCHORS thermal distribution network, including pumps, reservoirs, piping, and fluid management.

## 2. Coolant Fluid

### 2.1 Primary Coolant Specification

| Property | Requirement | Test Method |
|----------|-------------|-------------|
| Base fluid | Propylene glycol/water | — |
| Concentration | 50% ± 2% PG | Refractometer |
| Freeze protection | -35°C minimum | ASTM D1177 |
| pH | 8.0-10.5 | ASTM D1287 |
| Reserve alkalinity | > 5 mL | ASTM D1121 |
| Inhibitor package | Aircraft grade | OEM spec |
| Silicate free | Yes | — |
| Phosphate free | Yes | — |

### 2.2 Coolant Properties Table

| Temperature (°C) | Density (kg/m³) | Cp (kJ/kg·K) | Viscosity (mPa·s) | k (W/m·K) |
|------------------|-----------------|--------------|-------------------|-----------|
| -20 | 1065 | 3.35 | 15.0 | 0.38 |
| 0 | 1055 | 3.42 | 8.0 | 0.40 |
| 20 | 1048 | 3.48 | 4.5 | 0.41 |
| 40 | 1040 | 3.52 | 2.8 | 0.42 |
| 60 | 1030 | 3.55 | 1.9 | 0.42 |
| 80 | 1018 | 3.58 | 1.4 | 0.41 |

## 3. Pump System

### 3.1 HT Pump Specifications

| Parameter | Value | Unit |
|-----------|-------|------|
| Type | Centrifugal, magnetically coupled | — |
| Flow rate (nominal) | 100 | L/min |
| Flow rate (max) | 150 | L/min |
| Head (nominal) | 30 | m |
| Motor power | 3 | kW |
| Motor voltage | 540-850 | VDC |
| Efficiency | > 70% | — |
| Speed range | 1000-5000 | RPM |
| Control | Variable frequency | — |
| Seal type | Magnetic coupling (sealless) | — |
| MTBF | 20,000 | hours |

### 3.2 LT Pump Specifications

| Parameter | Value | Unit |
|-----------|-------|------|
| Type | Centrifugal, magnetically coupled | — |
| Flow rate (nominal) | 150 | L/min |
| Flow rate (max) | 220 | L/min |
| Head (nominal) | 25 | m |
| Motor power | 4 | kW |
| Motor voltage | 540-850 | VDC |
| Efficiency | > 72% | — |
| Speed range | 1000-4500 | RPM |
| Control | Variable frequency | — |
| Seal type | Magnetic coupling (sealless) | — |
| MTBF | 20,000 | hours |

### 3.3 Pump Performance Curves

```
┌─────────────────────────────────────────────────────────────────┐
│                    HT PUMP PERFORMANCE                          │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│   Head (m)                                                      │
│    40│                                                          │
│      │  ████  3000 RPM                                         │
│    35│    ████                                                  │
│      │      ████  4000 RPM                                     │
│    30│─ ─ ─ ─████ ─ ─ ─ ─ ─ Operating Point                    │
│      │          ████  5000 RPM                                 │
│    25│            ████                                          │
│      │              ████                                        │
│    20│                ████                                      │
│      │                  ████                                    │
│    15├────┬────┬────┬────┬────┬────┬────┬────                  │
│         50   75   100  125  150  175  200                       │
│                     Flow (L/min)                                │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

## 4. Expansion System

### 4.1 HT Expansion Tank

| Parameter | Value | Unit |
|-----------|-------|------|
| Total volume | 15 | L |
| Expansion volume | 6 | L |
| Pre-charge pressure | 1.5 | bar |
| Maximum pressure | 4.0 | bar |
| Material | Stainless steel | — |
| Diaphragm | EPDM | — |
| Level sensor | Ultrasonic | — |

### 4.2 LT Expansion Tank

| Parameter | Value | Unit |
|-----------|-------|------|
| Total volume | 20 | L |
| Expansion volume | 8 | L |
| Pre-charge pressure | 1.2 | bar |
| Maximum pressure | 3.5 | bar |
| Material | Stainless steel | — |
| Diaphragm | EPDM | — |
| Level sensor | Ultrasonic | — |

### 4.3 Expansion Calculation

```
Volume expansion = V₀ × β × ΔT

Where:
  V₀ = Initial volume (L)
  β  = Coefficient of expansion (≈ 0.0007 /°C for 50% PG)
  ΔT = Temperature change (°C)

HT System:
  Cold volume = 80 L at -40°C
  Hot volume = 80 × (1 + 0.0007 × 130) = 87.3 L
  Expansion = 7.3 L (< 15 L tank capacity) ✓

LT System:
  Cold volume = 100 L at -40°C
  Hot volume = 100 × (1 + 0.0007 × 110) = 107.7 L
  Expansion = 7.7 L (< 20 L tank capacity) ✓
```

## 5. Piping System

### 5.1 Piping Specifications

| Line | Material | Size (ID) | Wall | Pressure | Temperature |
|------|----------|-----------|------|----------|-------------|
| HT Main | SS316L | 25 mm | 2 mm | PN25 | 120°C |
| HT Branch | SS316L | 16 mm | 1.5 mm | PN25 | 120°C |
| LT Main | SS316L | 32 mm | 2 mm | PN16 | 80°C |
| LT Branch | SS316L | 20 mm | 1.5 mm | PN16 | 80°C |

### 5.2 Flexible Connections

| Location | Type | Size | Motion |
|----------|------|------|--------|
| Pump inlet/outlet | Metal bellows | DN25/32 | ±5 mm |
| Heat exchanger | PTFE hose | DN16/20 | ±10 mm |
| Cross-fuselage | Metal bellows | DN25 | ±15 mm |

### 5.3 Fittings

| Type | Material | Standard |
|------|----------|----------|
| Compression | SS316 | AS5202 |
| Flange | SS316L | SAE J518 |
| Quick disconnect | SS with EPDM | MIL-DTL-27066 |

## 6. Fill and Drain

### 6.1 Fill System

| Component | Specification |
|-----------|---------------|
| Fill port | Quick disconnect, 1/2" |
| Fill pump | External GSE, 10 L/min |
| Air bleed | Automatic at high points |
| Vacuum fill | Recommended for bubble-free |

### 6.2 Drain System

| Component | Specification |
|-----------|---------------|
| Drain port | Quick disconnect, 3/4" |
| Low points | Drain valves at all low points |
| Drain time | < 15 minutes for full drain |
| Residual | < 2% volume |

## 7. Fluid Management

### 7.1 Monitoring Parameters

| Parameter | Sensor | Range | Accuracy | Rate |
|-----------|--------|-------|----------|------|
| Coolant level HT | Ultrasonic | 0-100% | ±2% | 1 Hz |
| Coolant level LT | Ultrasonic | 0-100% | ±2% | 1 Hz |
| Coolant quality | Conductivity | 0-5000 µS | ±5% | 0.1 Hz |
| Coolant color | Optical | — | — | 0.01 Hz |

### 7.2 Maintenance Intervals

| Action | Interval | Condition |
|--------|----------|-----------|
| Visual inspection | Daily | Pre-flight |
| Level check | Weekly | — |
| Quality test | 500 FH | Conductivity, pH |
| Full analysis | 2000 FH | Lab test |
| Coolant change | 5000 FH or 3 years | Whichever first |
| Flush and refill | With coolant change | — |

---

## Document Control

| Field | Value |
|-------|-------|
| **Document ID** | 53-80-20-02 |
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
