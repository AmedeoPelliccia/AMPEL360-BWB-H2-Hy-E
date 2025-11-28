# 53-80-50-03 — ATA 72 Propulsion Interface

| Field | Value |
|-------|-------|
| **Document ID** | 53-80-50-03 |
| **Version** | 1.0 |
| **Date** | 2025-11-27 |
| **Status** | DRAFT |
| **Classification** | ENERGY / INTERFACE |

---

## 1. Purpose

This document defines the interface between ANCHORS Energy (53-80) and the Propulsion System (ATA 72) for energy exchange.

## 2. Interface Overview

| Interface | Type | Direction | Content |
|-----------|------|-----------|---------|
| ICD-72-020 | Thermal | Input | Waste heat from FC/TG |
| ICD-72-021 | Power | Input | Regeneration power |
| ICD-72-022 | Signal | Bidirectional | AFDX control/status |

## 3. Thermal Interface

### 3.1 Fuel Cell Waste Heat

| Parameter | Value |
|-----------|-------|
| Capacity | 250 kW |
| Temperature | 75-80°C |
| Coolant flow | 60 L/min |

### 3.2 Turbo-Generator Heat

| Parameter | Value |
|-----------|-------|
| Capacity | 180 kW |
| Temperature | 90-120°C (exhaust) |
| Recovery | Via HX-02 |

## 4. Regeneration Interface

| Parameter | Value |
|-----------|-------|
| Max regen power | 800 kW |
| Voltage | 650-850 VDC |
| Source | Fan motor generators |
| Duration | Descent phase (~25 min) |

## 5. Signal Interface

### 5.1 From ATA 72

| Signal | Content |
|--------|---------|
| FC_POWER | Fuel cell output |
| TG_POWER | Turbo-gen output |
| REGEN_AVAIL | Available regen |
| WASTE_HEAT | Thermal output |

### 5.2 To ATA 72

| Signal | Content |
|--------|---------|
| REGEN_ACCEPT | Accepted regen power |
| THERMAL_ACCEPT | Accepted heat |
| POWER_REQUEST | Power demand |

---

## Document Control

| Field | Value |
|-------|-------|
| **Document ID** | 53-80-50-03 |
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
