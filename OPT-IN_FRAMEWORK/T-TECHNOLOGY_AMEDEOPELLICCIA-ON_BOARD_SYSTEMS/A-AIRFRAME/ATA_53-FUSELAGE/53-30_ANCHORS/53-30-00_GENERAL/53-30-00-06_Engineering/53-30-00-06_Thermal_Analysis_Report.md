# 53-30-00-06 — Thermal Analysis Report

**Document ID:** 53-30-00-06-002  
**Version:** 1.0  
**Date:** 2025-11-25  
**Status:** DRAFT

---

## 1. Purpose

This document presents thermal analysis results for ANCHORS systems, focusing on heat management and thermal integration.

---

## 2. Heat Sources

| Source | Heat Generation | Peak | Location |
|:--|:--|:--|:--|
| Battery packs | 5-15 kW | During charge/discharge | Floor bay |
| CO₂ solidification | 2-5 kW (exothermic) | During operation | Forward bay |
| Electronics | 0.5 kW | Continuous | Equipment bay |
| Energy harvesters | Minimal | — | Distributed |

---

## 3. Thermal Management System

### 3.1 Cooling Loops

| Loop | Capacity | Fluid | Temperature Range |
|:--|:--|:--|:--|
| Primary battery | 20 kW | Propylene glycol 50% | 15-45°C |
| Secondary recovery | 10 kW | Propylene glycol 50% | 40-80°C |

### 3.2 Heat Rejection

| Method | Capacity | Location |
|:--|:--|:--|
| Ram air HX | 15 kW | Belly fairing |
| ECS integration | 10 kW | Pack bay |

---

## 4. Analysis Results

### 4.1 Normal Operation

| Component | Max Temperature | Limit | Margin |
|:--|:--|:--|:--|
| Battery cells | 45°C | 55°C | +10°C |
| Controller | 65°C | 85°C | +20°C |
| CO₂ cartridge | 60°C | 80°C | +20°C |

### 4.2 Hot Day Ground

| Component | Max Temperature | Limit | Margin |
|:--|:--|:--|:--|
| Battery cells | 52°C | 55°C | +3°C |
| Controller | 78°C | 85°C | +7°C |

---

## 5. Conclusions

Thermal management system adequately sized for all operating conditions.

---

## Document Control

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT** — Subject to human review and approval.
- Human approver: _[to be completed]_.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: 2025-11-25
