# 97-40-40-30_RUL_MODELS — Remaining Useful Life Models

## Purpose

This section contains the neural network models for Remaining Useful Life (RUL) estimation across different aircraft component categories.

## RUL Model Categories

| Section | Target Component | Model Type |
|---------|------------------|------------|
| 30-10_H2_Fuel_Cell | Fuel cell stack | Physics-informed NN |
| 30-20_Structural | Structural components | LSTM + survival |
| 30-30_Thermal | Thermal systems | CNN + regression |
| 30-40_Cycle_Based | Cyclic fatigue components | Statistical + NN hybrid |

## Model Architecture Overview

### H2 Fuel Cell RUL (30-10)
- Input: Voltage, current, temperature, humidity
- Architecture: Physics-informed neural network (PINN)
- Output: Stack RUL in operating hours

### Structural RUL (30-20)
- Input: Strain features, cycle counts
- Architecture: LSTM + Weibull survival layer
- Output: Component RUL in flight cycles

### Thermal RUL (30-30)
- Input: Temperature profile images
- Architecture: CNN + dense regression
- Output: System RUL in operating hours

### Cycle-Based RUL (30-40)
- Input: Landing cycles, maneuver counts
- Architecture: Gradient boosting + NN ensemble
- Output: Fatigue RUL in cycles

## Performance Targets

| Model | MAE Target | Coverage (80% CI) |
|-------|------------|-------------------|
| H2 Fuel Cell | < 50 hours | > 90% |
| Structural | < 100 cycles | > 85% |
| Thermal | < 100 hours | > 85% |
| Cycle-Based | < 200 cycles | > 90% |

---

## Document Control

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT** – Subject to human review and approval.
- Human approver: _[to be completed]_.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: 2025-11-28.

---
