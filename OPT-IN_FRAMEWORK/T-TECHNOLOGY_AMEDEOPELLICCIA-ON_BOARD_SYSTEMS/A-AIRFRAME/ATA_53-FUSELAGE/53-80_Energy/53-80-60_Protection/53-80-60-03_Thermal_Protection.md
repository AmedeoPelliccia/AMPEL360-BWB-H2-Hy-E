# 53-80-60-03 — Thermal Protection Design

| Field | Value |
|-------|-------|
| **Document ID** | 53-80-60-03 |
| **Version** | 1.0 |
| **Date** | 2025-11-27 |
| **Status** | DRAFT |
| **Classification** | ENERGY / PROTECTION |

---

## 1. Purpose

This document defines the thermal protection strategy for the ANCHORS thermal distribution system.

## 2. Protection Setpoints

### 2.1 HT Bus Protection

| Condition | Threshold | Response |
|-----------|-----------|----------|
| Over-temp warning | 95°C | Increase radiator |
| Over-temp high | 100°C | Reduce sources |
| Over-temp critical | 105°C | Emergency cooling |

### 2.2 LT Bus Protection

| Condition | Threshold | Response |
|-----------|-----------|----------|
| Over-temp warning | 60°C | Increase radiator |
| Over-temp high | 65°C | Reduce loads |
| Over-temp critical | 70°C | Emergency mode |

## 3. Flow Protection

| Condition | Threshold | Response |
|-----------|-----------|----------|
| HT low flow | < 50 L/min | Backup pump |
| LT low flow | < 75 L/min | Backup pump |
| Total loss | < 20 L/min | Emergency shutdown |

## 4. Pressure Protection

| Condition | Threshold | Response |
|-----------|-----------|----------|
| Low pressure | < 1.0 bar | Warning, reduce flow |
| High pressure | > 3.5 bar | Relief valve opens |
| Relief active | > 4.0 bar | Passive vent |

## 5. Leak Detection

| Method | Sensitivity | Response |
|--------|-------------|----------|
| Level sensor | 85% volume | Warning |
| Pressure decay | 10% in 1 min | Alarm |
| Visual indicator | — | Maintenance |

## 6. Thermal Runaway Prevention

| Protection | Battery | PE Components |
|------------|---------|---------------|
| Temp limit | 45°C | 85°C |
| Rate limit | 5°C/min | 10°C/min |
| Differential | 5°C cell-to-cell | — |
| Response | Isolate, max cool | Reduce power |

---

## Document Control

| Field | Value |
|-------|-------|
| **Document ID** | 53-80-60-03 |
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
