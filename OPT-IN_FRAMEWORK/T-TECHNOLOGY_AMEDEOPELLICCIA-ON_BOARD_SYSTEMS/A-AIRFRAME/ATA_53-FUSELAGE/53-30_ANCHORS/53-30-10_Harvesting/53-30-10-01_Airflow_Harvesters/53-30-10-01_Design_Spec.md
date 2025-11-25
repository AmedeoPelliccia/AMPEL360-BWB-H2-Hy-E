# 53-30-10-01 — Design Specification

**Document ID:** 53-30-10-01-003  
**Version:** 1.0  
**Date:** 2025-11-25  
**Status:** DRAFT

---

## 1. Purpose

This document specifies the design of the Airflow Harvester.

---

## 2. Design Overview

The Airflow Harvester converts kinetic energy from ECS recirculation airflow into electrical power.

### 2.1 Operating Principle

1. Cabin recirculation air enters harvester
2. Axial turbine extracts kinetic energy
3. Generator converts to electrical power
4. Power conditioning provides 28 VDC output

---

## 3. Component Design

### 3.1 Turbine

| Parameter | Value |
|:--|:--|
| Type | Axial flow |
| Blades | 6 |
| Material | Aluminum alloy |
| Tip speed | 50 m/s max |
| RPM range | 5,000-15,000 |

### 3.2 Generator

| Parameter | Value |
|:--|:--|
| Type | Permanent magnet |
| Output | 600 W @ 12,000 RPM |
| Efficiency | 85% |
| Cooling | Air-cooled |

### 3.3 Power Conditioning

| Parameter | Value |
|:--|:--|
| Input | Variable AC |
| Output | 28 VDC ±2 V |
| Regulation | Buck-boost |

---

## 4. Materials

| Component | Material | Selection Rationale |
|:--|:--|:--|
| Housing | Al 6061-T6 | Weight, corrosion |
| Blades | Al 7075-T6 | Strength, fatigue |
| Bearings | Ceramic hybrid | Life, lubrication |
| Magnets | NdFeB | Power density |

---

## 5. Interfaces

| Interface | Description |
|:--|:--|
| Inlet | 200 mm duct flange |
| Outlet | 200 mm duct flange |
| Electrical | MIL-DTL-38999 connector |
| Mounting | 4x M8 bolts on flange |

---

## Document Control

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT** — Subject to human review and approval.
- Human approver: _[to be completed]_.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: 2025-11-25
