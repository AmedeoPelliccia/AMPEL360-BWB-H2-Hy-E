# 53-80-70-02 — Thermal Monitoring System

| Field | Value |
|-------|-------|
| **Document ID** | 53-80-70-02 |
| **Version** | 1.0 |
| **Date** | 2025-11-27 |
| **Status** | DRAFT |
| **Classification** | ENERGY / MONITORING |

---

## 1. Purpose

This document defines the thermal monitoring system for the ANCHORS dual thermal bus system.

## 2. Monitored Parameters

### 2.1 HT Bus Monitoring

| Parameter | Sensor | Range | Accuracy |
|-----------|--------|-------|----------|
| HT supply temp | RTD Pt100 | -40 to 120°C | ±0.5°C |
| HT return temp | RTD Pt100 | -40 to 120°C | ±0.5°C |
| HT flow rate | Ultrasonic | 0-200 L/min | ±2% |
| HT pressure | Pressure transducer | 0-6 bar | ±1% |
| HT level | Ultrasonic | 0-100% | ±2% |

### 2.2 LT Bus Monitoring

| Parameter | Sensor | Range | Accuracy |
|-----------|--------|-------|----------|
| LT supply temp | RTD Pt100 | -40 to 80°C | ±0.5°C |
| LT return temp | RTD Pt100 | -40 to 80°C | ±0.5°C |
| LT flow rate | Ultrasonic | 0-300 L/min | ±2% |
| LT pressure | Pressure transducer | 0-5 bar | ±1% |
| LT level | Ultrasonic | 0-100% | ±2% |

## 3. Heat Exchanger Monitoring

| HX | Inlet Temp | Outlet Temp | ΔT | Heat Transfer |
|----|------------|-------------|-----|---------------|
| HX-01 (FC) | ✓ | ✓ | Calc | Calc |
| HX-02 (Turbine) | ✓ | ✓ | Calc | Calc |
| HX-03 (Coupling) | ✓×2 | ✓×2 | Calc | Calc |
| HX-04 (Cabin) | ✓ | ✓ | Calc | Calc |
| HX-05 (De-ice) | ✓ | ✓ | Calc | Calc |
| HX-06/07 (Rad) | ✓ | ✓ | Calc | Calc |

## 4. Calculated Parameters

| Parameter | Calculation | Unit |
|-----------|-------------|------|
| Heat transfer | Q = ṁ × Cp × ΔT | kW |
| Thermal efficiency | Q_recovered / Q_available | % |
| COP | Q_cabin / P_pumps | — |
| Energy recovered | ∫Q dt | kWh |

## 5. Display

| Metric | Unit | Display |
|--------|------|---------|
| HT bus temp | °C | Numeric + indicator |
| LT bus temp | °C | Numeric + indicator |
| Heat recovery | kW | Bar chart |
| Thermal efficiency | % | Gauge |
| Energy recovered | kWh | Numeric |

---

## Document Control

| Field | Value |
|-------|-------|
| **Document ID** | 53-80-70-02 |
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
