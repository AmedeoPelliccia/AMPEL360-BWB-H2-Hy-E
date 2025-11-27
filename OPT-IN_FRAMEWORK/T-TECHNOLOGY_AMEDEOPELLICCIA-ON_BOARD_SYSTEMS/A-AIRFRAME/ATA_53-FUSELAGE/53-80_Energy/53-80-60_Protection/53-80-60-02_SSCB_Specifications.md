# 53-80-60-02 — SSCB Specifications

| Field | Value |
|-------|-------|
| **Document ID** | 53-80-60-02 |
| **Version** | 1.0 |
| **Date** | 2025-11-27 |
| **Status** | DRAFT |
| **Classification** | ENERGY / PROTECTION |

---

## 1. Purpose

This document specifies the Solid State Circuit Breakers (SSCBs) used in the ANCHORS electrical distribution system.

## 2. SSCB Inventory

| ID | Location | Rating | Function |
|----|----------|--------|----------|
| SSCB-01 | CH-E-01 | 80 A | Battery TMS |
| SSCB-02 | CH-E-02 | 50 A | CO₂ Capture |
| SSCB-03 | CH-E-03 | 20 A | Water System |
| SSCB-04 | CH-E-04 | 35 A | Thermal Pumps |
| SSCB-05 | CH-E-06 | 35 A | Emergency |
| SSCB-BT1 | Bus Tie L | 200 A | Bus tie protection |
| SSCB-BT2 | Bus Tie R | 200 A | Bus tie protection |

## 3. General Specifications

| Parameter | Value | Notes |
|-----------|-------|-------|
| Technology | SiC MOSFET | High efficiency |
| Voltage rating | 1000 VDC | With margin |
| Current ratings | 20-200 A | Per application |
| On-resistance | < 5 mΩ | At rated current |
| Trip time | < 1 ms | Short circuit |
| Reset time | < 100 ms | Electronic |
| Operating temp | -55 to +125°C | Junction |
| MTBF | 100,000 hours | — |

## 4. Protection Functions

| Function | Detection | Response |
|----------|-----------|----------|
| Overcurrent | I > I_trip | Open < 1 ms |
| I²t limit | Energy integral | Open at limit |
| Short circuit | dI/dt | Open < 100 μs |
| Overvoltage | V > 900 VDC | Open |
| Overtemperature | T > 120°C | Derating/open |

## 5. Control Interface

| Signal | Direction | Type |
|--------|-----------|------|
| Enable | Input | 28 VDC discrete |
| Trip command | Input | Digital |
| Reset command | Input | Digital |
| Status | Output | Digital |
| Current feedback | Output | Analog 0-10V |
| Trip cause | Output | Digital code |

## 6. Environmental

| Parameter | Requirement | Standard |
|-----------|-------------|----------|
| Vibration | Category S2 | DO-160G |
| Temperature | -55 to +70°C | Ambient |
| Humidity | 0-100% RH | — |
| Salt fog | 96 hours | MIL-STD-810 |
| Altitude | 0-45,000 ft | — |

---

## Document Control

| Field | Value |
|-------|-------|
| **Document ID** | 53-80-60-02 |
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
