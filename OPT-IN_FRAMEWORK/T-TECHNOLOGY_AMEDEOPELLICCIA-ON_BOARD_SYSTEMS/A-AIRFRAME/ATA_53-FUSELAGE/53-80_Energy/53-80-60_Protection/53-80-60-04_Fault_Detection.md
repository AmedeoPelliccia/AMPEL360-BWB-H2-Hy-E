# 53-80-60-04 — Fault Detection Logic

| Field | Value |
|-------|-------|
| **Document ID** | 53-80-60-04 |
| **Version** | 1.0 |
| **Date** | 2025-11-27 |
| **Status** | DRAFT |
| **Classification** | ENERGY / PROTECTION |

---

## 1. Purpose

This document defines the fault detection and isolation logic for ANCHORS energy systems.

## 2. Fault Categories

| Category | Examples | Response Time |
|----------|----------|---------------|
| Critical | Short circuit, thermal runaway | < 10 ms |
| Major | Overcurrent, over-temp | < 100 ms |
| Minor | Sensor fail, efficiency drop | < 1 s |
| Advisory | Degradation, maintenance | Event |

## 3. Detection Methods

### 3.1 Electrical Faults

| Fault | Method | Threshold |
|-------|--------|-----------|
| Overcurrent | Current sensor | > 120% rated |
| Short circuit | dI/dt | > 10 kA/ms |
| Ground fault | GFI | > 30 mA |
| Overvoltage | Voltage sensor | > 900 VDC |
| Undervoltage | Voltage sensor | < 600 VDC |
| Arc fault | Frequency analysis | Arc signature |

### 3.2 Thermal Faults

| Fault | Method | Threshold |
|-------|--------|-----------|
| Over-temperature | RTD | > limits |
| Under-temperature | RTD | < limits |
| Thermal runaway | Rate of rise | > 5°C/min |
| Coolant leak | Level sensor | < 85% |
| Pump failure | Flow sensor | < 50% |

## 4. Fault Isolation

| Fault Location | Isolation Method |
|----------------|------------------|
| Load fault | Trip load SSCB |
| Channel fault | Trip channel SSCB |
| Bus fault | Open bus tie |
| Source fault | Trip source contactor |
| Thermal fault | Close isolation valve |

## 5. Fault Logging

| Data | Capture |
|------|---------|
| Timestamp | ms resolution |
| Fault code | Enumerated |
| Pre-fault data | 1 s buffer |
| Post-fault data | 5 s buffer |
| System state | All parameters |

---

## Document Control

| Field | Value |
|-------|-------|
| **Document ID** | 53-80-60-04 |
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
