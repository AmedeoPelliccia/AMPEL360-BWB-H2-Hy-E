# 53-80-40-03 — Thermal Optimization Strategy

| Field | Value |
|-------|-------|
| **Document ID** | 53-80-40-03 |
| **Version** | 1.0 |
| **Date** | 2025-11-27 |
| **Status** | DRAFT |
| **Classification** | ENERGY / MANAGEMENT |

---

## 1. Purpose

This document defines thermal optimization strategies for maximizing heat recovery while maintaining component temperatures within safe limits.

## 2. Optimization Objective

```
Maximize: Q_recovered = Q_cabin + Q_deice + Q_battery + Q_PCM

Subject to:
  T_HT_min ≤ T_HT ≤ T_HT_max
  T_LT_min ≤ T_LT ≤ T_LT_max
  T_component ≤ T_component_max (for all components)
  Q_source = Q_sink + Q_storage + Q_rejected
```

## 3. Heat Recovery Priority

| Priority | Sink | Condition | Capacity |
|----------|------|-----------|----------|
| 1 | Cabin heating | T_cabin < T_setpoint | 100 kW |
| 2 | De-icing | Ice detected | 50 kW |
| 3 | Battery preconditioning | T_bat < 15°C | 30 kW |
| 4 | PCM charging | PCM < 90% charged | 50 kW |
| 5 | Radiator | Excess heat | 200 kW |

## 4. Mode-Based Strategy

### 4.1 Ground Cold Start

| Action | Purpose | Duration |
|--------|---------|----------|
| Run HT pump at max | Circulate FC heat | Until T_HT > 70°C |
| Open cabin valve 100% | Preheat cabin | Until T_cabin > 18°C |
| Route to battery HX | Preheat battery | Until T_bat > 15°C |
| Minimize radiator | Conserve heat | Throughout |

### 4.2 Cruise Optimization

| Condition | Strategy |
|-----------|----------|
| Q_source > Q_sink | Store excess in PCM |
| Q_source < Q_sink | Draw from PCM |
| PCM full | Increase cabin setpoint |
| PCM empty | Reduce de-ice if safe |

### 4.3 Descent Mode

| Action | Purpose |
|--------|---------|
| Reduce FC output | Less waste heat |
| Discharge PCM to cabin | Use stored heat |
| Minimize radiator | Conserve remaining heat |

## 5. Predictive Control

### 5.1 Thermal Prediction

```
T_bus(t+Δt) = T_bus(t) + (Q_in - Q_out) × Δt / (m × Cp)

Q_in = predicted heat from sources
Q_out = scheduled heat to sinks + radiator
m = thermal mass of bus
Cp = specific heat of coolant
```

### 5.2 Look-Ahead Optimization

- Horizon: 10 minutes
- Update rate: 1 Hz
- Anticipate descent to pre-charge PCM
- Anticipate cold conditions to pre-heat

## 6. Efficiency Metrics

| Metric | Target | Calculation |
|--------|--------|-------------|
| Thermal recovery ratio | ≥ 65% | Q_recovered / Q_available |
| Radiator rejection | ≤ 35% | Q_radiator / Q_available |
| COP equivalent | ≥ 3.0 | Q_cabin / P_pumps |

---

## Document Control

| Field | Value |
|-------|-------|
| **Document ID** | 53-80-40-03 |
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
