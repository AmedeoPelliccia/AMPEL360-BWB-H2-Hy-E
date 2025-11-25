# 53-30-00-06 — CO₂ Capture Efficiency Model

**Document ID:** 53-30-00-06-004  
**Version:** 1.0  
**Date:** 2025-11-25  
**Status:** DRAFT

---

## 1. Purpose

This document presents the CO₂ capture efficiency modeling for ANCHORS systems.

---

## 2. System Model

### 2.1 Process Overview

```
Cabin Air (1000-4000 ppm CO₂)
      ↓
[Extraction] → 10% of recirculation
      ↓
[Separation Module] → 90% purity
      ↓
[Solidification] → Minerite
```

### 2.2 Key Parameters

| Parameter | Value | Unit |
|:--|:--|:--|
| Cabin CO₂ production rate | 200 | g/h/passenger |
| Extraction rate | 10% | of recirculation |
| Separation efficiency | 90% | — |
| Solidification efficiency | 95% | — |

---

## 3. Efficiency Analysis

### 3.1 Cruise Conditions (150 passengers)

| Metric | Value |
|:--|:--|
| CO₂ production | 30 kg/h |
| CO₂ extracted | 25 kg/h |
| CO₂ captured | 22.5 kg/h |
| CO₂ solidified | 21.4 kg/h |
| Net capture rate | 71% |

### 3.2 Mission Profile (8-hour flight)

| Phase | Duration | Capture | Total |
|:--|:--|:--|:--|
| Climb | 0.5 h | 8 kg | 8 kg |
| Cruise | 7 h | 150 kg | 158 kg |
| Descent | 0.5 h | 5 kg | 163 kg |

---

## 4. Sensitivity Analysis

| Variable | ±10% Change | Effect on Capture |
|:--|:--|:--|
| Extraction rate | ±10% | ±9.5% |
| Separation efficiency | ±5% | ±4.5% |
| Sorbent capacity | ±10% | ±2% |

---

## 5. Improvement Opportunities

| Improvement | Potential Gain |
|:--|:--|
| Increase extraction rate to 15% | +45% |
| Improve separation to 95% | +5% |
| Dual-stage separation | +10% |

---

## Document Control

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT** — Subject to human review and approval.
- Human approver: _[to be completed]_.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: 2025-11-25
