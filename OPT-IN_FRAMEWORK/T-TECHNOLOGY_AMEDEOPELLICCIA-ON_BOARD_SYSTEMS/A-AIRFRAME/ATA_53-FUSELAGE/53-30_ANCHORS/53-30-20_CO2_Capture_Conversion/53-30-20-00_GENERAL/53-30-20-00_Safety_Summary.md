# 53-30-20-00 — Safety Summary

**Document ID:** 53-30-20-00-004  
**Version:** 1.0  
**Date:** 2025-11-25  
**Status:** DRAFT

---

## 1. Purpose

This document summarizes safety considerations for the CO₂ Capture system.

---

## 2. Hazard Summary

| Hazard ID | Hazard | Severity | Probability |
|:--|:--|:--|:--|
| H-CO2-001 | CO₂ leak in cabin | Minor | Remote |
| H-CO2-002 | CO₂ leak in bay | Major | Remote |
| H-CO2-003 | Cartridge overpressure | Major | Extremely Remote |
| H-CO2-004 | Thermal damage | Minor | Remote |

---

## 3. Safety Features

### 3.1 Concentration Monitoring

| Location | Sensor Type | Threshold | Response |
|:--|:--|:--|:--|
| Cabin | NDIR | > 2000 ppm | Alert |
| Equipment bay | NDIR | > 20,000 ppm | Alarm + ventilation |
| Cartridge bay | NDIR | > 40,000 ppm | Isolation + vent |

### 3.2 Pressure Protection

| Component | Protection | Setting |
|:--|:--|:--|
| Manifold | Relief valve | 2.5 bar |
| Separation module | Burst disc | 4 bar |
| Cartridge | Relief valve | 3 bar |

### 3.3 Ventilation

| Bay | Ventilation Rate | Source |
|:--|:--|:--|
| Cartridge bay | 10 ACH | Dedicated |
| Equipment bay | 5 ACH | Aircraft |

---

## 4. Emergency Procedures

### CO₂ High Level

1. ANCHORS automatically isolates CO₂ system
2. Ventilation increases to maximum
3. EICAS message displayed
4. Crew may override isolation if safe

---

## Document Control

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT** — Subject to human review and approval.
- Human approver: _[to be completed]_.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: 2025-11-25
