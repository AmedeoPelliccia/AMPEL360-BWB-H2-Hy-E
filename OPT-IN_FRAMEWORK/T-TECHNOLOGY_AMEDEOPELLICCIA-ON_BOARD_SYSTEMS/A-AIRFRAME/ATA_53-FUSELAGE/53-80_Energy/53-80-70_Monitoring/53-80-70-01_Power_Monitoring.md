# 53-80-70-01 — Power Monitoring System

| Field | Value |
|-------|-------|
| **Document ID** | 53-80-70-01 |
| **Version** | 1.0 |
| **Date** | 2025-11-27 |
| **Status** | DRAFT |
| **Classification** | ENERGY / MONITORING |

---

## 1. Purpose

This document defines the power monitoring system for the ANCHORS electrical distribution network.

## 2. Monitored Parameters

### 2.1 Bus Level Monitoring

| Parameter | Sensor | Range | Accuracy | Rate |
|-----------|--------|-------|----------|------|
| HVDC bus voltage | Voltage transducer | 0-1000 VDC | ±0.5% | 10 Hz |
| Bus current | Current transducer | 0-300 A | ±1% | 10 Hz |
| Power (calculated) | — | 0-250 kW | ±1.5% | 10 Hz |
| Power quality | FFT analyzer | 0-500 kHz | ±2% | 1 Hz |

### 2.2 Channel Level Monitoring

| Channel | Voltage | Current | Power |
|---------|---------|---------|-------|
| CH-01 Battery TMS | ✓ | ✓ | ✓ |
| CH-02 CO₂ Capture | ✓ | ✓ | ✓ |
| CH-03 Water System | ✓ | ✓ | ✓ |
| CH-04 Thermal Pumps | ✓ | ✓ | ✓ |
| CH-05 Controls | ✓ | ✓ | ✓ |

## 3. Sensor Specifications

### 3.1 Voltage Transducers

| Parameter | Value |
|-----------|-------|
| Input range | 0-1000 VDC |
| Output | 0-10 VDC |
| Accuracy | ±0.5% |
| Isolation | 2500 VAC |
| Response | < 1 ms |

### 3.2 Current Transducers

| Parameter | Value |
|-----------|-------|
| Technology | Hall effect |
| Input range | 0-300 A |
| Output | 4-20 mA |
| Accuracy | ±1% |
| Bandwidth | 100 kHz |

## 4. Data Acquisition

| Parameter | Specification |
|-----------|---------------|
| Sampling rate | 1 kHz |
| Resolution | 16-bit |
| Channels | 16 analog |
| Interface | AFDX |
| Buffer | 1 s pre-trigger |

## 5. Display Parameters

| Metric | Unit | Display |
|--------|------|---------|
| Bus voltage | VDC | Numeric + bar |
| Total current | A | Numeric + bar |
| Total power | kW | Numeric + trend |
| Channel power | kW | Per-channel bars |
| Efficiency | % | Gauge |
| Energy consumed | kWh | Numeric |

---

## Document Control

| Field | Value |
|-------|-------|
| **Document ID** | 53-80-70-01 |
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
