# 56-21-01_04_001 — Heating Elements Design

## Document Information

- **Document ID**: 56-21-01_04_001
- **Title**: Windshield Heating Elements Design
- **ATA Chapter**: 56 – Windows
- **LRI Code**: 56-21-01_04 (LRI_04)
- **Version**: 1.0
- **Status**: DRAFT
- **Date**: 2025-12-01

---

## 1. Purpose

This document defines the design specifications for the Heating Elements integrated into the Forward Windshield Assembly for anti-ice and anti-fog protection.

## 2. Scope

The Heating Elements provide:

- Anti-ice protection for windshield panels
- Anti-fog defogging capability
- Controlled heating to prevent thermal shock

---

## 3. Design Specifications

### 3.1 Heating Film Technology

| Parameter | Value |
|-----------|-------|
| **Technology** | Conductive metal oxide (ITO or equivalent) |
| **Configuration** | Embedded in PVB interlayer |
| **Coverage** | Full panel area (95% minimum) |
| **Resistance** | Uniformly distributed |

### 3.2 Electrical Characteristics

| Parameter | Value |
|-----------|-------|
| **Operating Voltage** | 115VAC, 400Hz |
| **Power Density** | 0.8 - 1.2 W/cm² |
| **Total Power (per panel)** | [TBD] kW |
| **Control** | Zone-controlled with temperature feedback |

### 3.3 Performance Requirements

| Parameter | Value |
|-----------|-------|
| **De-icing Time** | < 5 minutes at -40°C |
| **Anti-fog Time** | < 30 seconds |
| **Temperature Uniformity** | ±5°C across panel |
| **Overheat Protection** | Auto-shutdown at 70°C |

---

## 4. Interface with Window Heating Controller

The heating elements interface with the Window Heating Controller (ATA 56-25):

| Interface | Description |
|-----------|-------------|
| Power Input | 115VAC from controller |
| Temperature Feedback | RTD sensor signals |
| Zone Control | Individual panel zone selection |

---

## 5. Traceability

- **Requirements**: See [56-21-01_04_002_HeatingElements_Requirements.md](./56-21-01_04_002_HeatingElements_Requirements.md)
- **Interfaces**: See [56-21-01_04_003_HeatingElements_Interfaces.md](./56-21-01_04_003_HeatingElements_Interfaces.md)
- **Materials**: See [56-21-01_04_004_HeatingElements_Materials.md](./56-21-01_04_004_HeatingElements_Materials.md)

---

## Document Control

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT** – Subject to human review and approval.
- Human approver: _[to be completed]_.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: _2025-12-01_.

---
