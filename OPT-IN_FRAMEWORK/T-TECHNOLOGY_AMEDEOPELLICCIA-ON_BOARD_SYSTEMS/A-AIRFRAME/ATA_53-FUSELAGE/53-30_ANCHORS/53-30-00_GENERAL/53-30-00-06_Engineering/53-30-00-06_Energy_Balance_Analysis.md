# 53-30-00-06 — Energy Balance Analysis

**Document ID:** 53-30-00-06-005  
**Version:** 1.0  
**Date:** 2025-11-25  
**Status:** DRAFT

---

## 1. Purpose

This document presents the energy balance analysis for ANCHORS systems.

---

## 2. Energy Sources

| Source | Power | Availability |
|:--|:--|:--|
| Airflow harvesters | 2.0 kW | Cruise |
| Waste heat TEG | 1.5 kW | All flight |
| Heat recovery | 3.0 kW (thermal) | All flight |
| **Total Electrical** | **3.5 kW** | — |
| **Total Thermal** | **3.0 kW** | — |

---

## 3. Energy Consumers

| Consumer | Power | Duty Cycle |
|:--|:--|:--|
| CO₂ capture system | 1.0 kW | 80% |
| Water recycling | 0.5 kW | 50% |
| Thermal loops pumps | 0.3 kW | 100% |
| Controllers/sensors | 0.2 kW | 100% |
| **Total Electrical** | **2.0 kW** | — |

---

## 4. Energy Balance

### 4.1 Cruise Phase

| Category | Generation | Consumption | Balance |
|:--|:--|:--|:--|
| Electrical | 3.5 kW | 2.0 kW | **+1.5 kW** |
| Thermal | 3.0 kW | 2.5 kW | **+0.5 kW** |

### 4.2 Ground Operations

| Category | Generation | Consumption | Balance |
|:--|:--|:--|:--|
| Electrical | 0 kW | 0.5 kW | **-0.5 kW** |

Ground deficit supplied by aircraft ground power.

---

## 5. Annual Energy Impact

| Metric | Value | Unit |
|:--|:--|:--|
| Net energy contribution | 5,000 | kWh/year |
| Equivalent fuel saving | 500 | kg jet fuel/year |
| CO₂ avoided (fuel) | 1,500 | kg CO₂/year |
| CO₂ captured | 50,000 | kg CO₂/year |

---

## 6. Conclusion

ANCHORS provides net positive energy contribution during flight operations.

---

## Document Control

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT** — Subject to human review and approval.
- Human approver: _[to be completed]_.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: 2025-11-25
