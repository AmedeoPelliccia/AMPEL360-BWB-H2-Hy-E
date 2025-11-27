# 53-80-50-02 — ATA 21 ECS Interface

| Field | Value |
|-------|-------|
| **Document ID** | 53-80-50-02 |
| **Version** | 1.0 |
| **Date** | 2025-11-27 |
| **Status** | DRAFT |
| **Classification** | ENERGY / INTERFACE |

---

## 1. Purpose

This document defines the thermal interface between ANCHORS Energy (53-80) and the Environmental Control System (ATA 21).

## 2. Interface Overview

| Interface | Type | Direction | Content |
|-----------|------|-----------|---------|
| ICD-21-001 | Thermal | Output | HT coolant for cabin |
| ICD-21-002 | Thermal | Output | HT coolant for de-ice |
| ICD-21-003 | Signal | Bidirectional | AFDX control/status |

## 3. Thermal Interface

### 3.1 Cabin Heating

| Parameter | Value |
|-----------|-------|
| Capacity | 100 kW |
| Supply temperature | 85°C |
| Return temperature | 65°C min |
| Flow rate | 30 L/min |

### 3.2 De-icing

| Parameter | Value |
|-----------|-------|
| Capacity | 50 kW |
| Supply temperature | 85°C |
| Zones | 4 |

## 4. Signal Interface

### 4.1 To ATA 21

| Signal | Content |
|--------|---------|
| HT_SUPPLY_TEMP | Supply temperature |
| HEAT_AVAILABLE | Available capacity |
| THERMAL_STATUS | System status |

### 4.2 From ATA 21

| Signal | Content |
|--------|---------|
| HEAT_DEMAND | Required heat |
| CABIN_TEMP | Cabin temperature |
| DEICE_REQUEST | De-ice zone requests |

## 5. Operating Modes

| Mode | Heat Available | Priority |
|------|----------------|----------|
| Normal | 100% | Cabin first |
| Reduced | 50% | De-ice first |
| Minimum | 20% | Essential only |

---

## Document Control

| Field | Value |
|-------|-------|
| **Document ID** | 53-80-50-02 |
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
