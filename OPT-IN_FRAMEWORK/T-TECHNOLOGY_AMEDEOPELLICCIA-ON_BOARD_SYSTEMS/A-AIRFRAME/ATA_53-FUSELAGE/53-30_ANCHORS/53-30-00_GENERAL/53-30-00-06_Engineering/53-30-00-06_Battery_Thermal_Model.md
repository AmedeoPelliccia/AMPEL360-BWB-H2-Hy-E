# 53-30-00-06 — Battery Thermal Model

**Document ID:** 53-30-00-06-007  
**Version:** 1.0  
**Date:** 2025-11-25  
**Status:** DRAFT

---

## 1. Purpose

This document presents the battery thermal model for ANCHORS Battery Loop systems.

---

## 2. Battery Configuration

| Parameter | Value |
|:--|:--|
| Chemistry | LFP (LiFePO₄) |
| Nominal voltage | 800 V |
| Capacity | 100 kWh per pack |
| Number of packs | 2 (quick-swap) |
| Cells per pack | 240 (series-parallel) |

---

## 3. Heat Generation Model

### 3.1 Sources

| Source | Formula | Peak Value |
|:--|:--|:--|
| Ohmic losses | I²R | 8 kW |
| Reversible heat | I·T·dE/dT | ±1 kW |
| Side reactions | Arrhenius | < 0.5 kW |

### 3.2 Operating Profiles

| Mode | Current | Heat Generation |
|:--|:--|:--|
| Charge (C/2) | 125 A | 5 kW |
| Discharge (1C) | 250 A | 10 kW |
| Cruise | 50 A | 1 kW |

---

## 4. Cooling System Model

### 4.1 Cold Plate Performance

| Parameter | Value |
|:--|:--|
| Heat transfer coefficient | 500 W/m²K |
| Contact area | 0.5 m² per pack |
| Coolant flow | 10 L/min |
| ΔT coolant | 5°C |

### 4.2 System Capacity

| Condition | Cooling Capacity | Heat Load | Margin |
|:--|:--|:--|:--|
| Normal | 15 kW | 5 kW | +10 kW |
| Peak discharge | 15 kW | 12 kW | +3 kW |
| Ground hot day | 12 kW | 8 kW | +4 kW |

---

## 5. Thermal Runaway Analysis

| Stage | Temperature | Time | Response |
|:--|:--|:--|:--|
| Normal | < 45°C | — | Normal cooling |
| Warning | 55°C | — | Increase cooling |
| Critical | 70°C | t=0 | Isolate, max cooling |
| Runaway | 130°C | t+2s | Vent, suppress |

---

## Document Control

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT** — Subject to human review and approval.
- Human approver: _[to be completed]_.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: 2025-11-25
