# 53-80-40-04 — Regeneration Maximization Logic

| Field | Value |
|-------|-------|
| **Document ID** | 53-80-40-04 |
| **Version** | 1.0 |
| **Date** | 2025-11-27 |
| **Status** | DRAFT |
| **Classification** | ENERGY / MANAGEMENT |

---

## 1. Purpose

This document defines the algorithms and strategies for maximizing energy capture during regenerative braking and descent operations.

## 2. Regeneration Sources

| Source | Max Power | Typical Energy | Capture Target |
|--------|-----------|----------------|----------------|
| Fan motors (descent) | 800 kW | 300 kWh | 85% |
| Wheel brakes (landing) | 200 kW | 2 kWh | 50% |
| Taxi regen | 80 kW | 15 kWh | 90% |

## 3. Battery Acceptance Algorithm

```
P_accept = min(P_regen, P_battery_max × f_SOC × f_temp × f_voltage)

Where:
  f_SOC = (100 - SOC) / 10  for SOC > 90%, else 1.0
  f_temp = (45 - T_bat) / 20  for T_bat > 25°C, else 1.0
  f_voltage = (V_max - V_bat) / (V_max - V_nom)
```

## 4. Descent Regen Strategy

### 4.1 Descent Phase Optimization

| Altitude (ft) | Regen Power | Battery Acceptance |
|---------------|-------------|-------------------|
| 35,000 - 25,000 | 200 kW | High (SOC low) |
| 25,000 - 15,000 | 400 kW | Medium |
| 15,000 - 5,000 | 600 kW | Reducing |
| 5,000 - 0 | 800 kW | Limited (SOC high) |

### 4.2 Excess Power Management

When P_regen > P_battery_accept:
1. Route excess to DC-DC auxiliary loads
2. Increase cabin heating if possible
3. Charge PCM thermal storage
4. Dissipate in brake resistor (last resort)

## 5. Predictive Regen

### 5.1 Trajectory-Based Prediction

```
E_regen_available = ∫(P_regen(t) dt) over descent

P_regen(t) = f(altitude, descent_rate, aircraft_mass, drag)
```

### 5.2 SOC Targeting

Target SOC at landing: 100%
- Calculate required regen acceptance
- Adjust descent profile if needed
- Pre-discharge battery before descent if SOC > 90%

## 6. Wheel Brake Regen

### 6.1 Brake Energy Capture

| Speed (kt) | Regen Power | Duration | Energy |
|------------|-------------|----------|--------|
| 120-80 | 200 kW | 10 s | 0.56 kWh |
| 80-40 | 150 kW | 15 s | 0.63 kWh |
| 40-0 | 80 kW | 20 s | 0.44 kWh |

### 6.2 Brake Blending

- Priority: Regen braking
- Friction brakes: Supplement for high decel
- Regen fade: Below 10 kt, friction only

---

## Document Control

| Field | Value |
|-------|-------|
| **Document ID** | 53-80-40-04 |
| **Version** | 1.0 |
| **Date** | 2025-11-27 |
| **Status** | DRAFT |

### AI Disclosure

- **Generated with assistance of:** AI (GitHub Copilot), prompted by **Amedeo Pelliccia**
- **Status:** DRAFT — Subject to human review and approval
- **Repository:** `AMPEL360-BWB-H2-Hy-E`
- **Last AI update:** 2025-11-27

---

*END OF DOCUMENT*
