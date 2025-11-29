# 57-00-02-10 — Functional Hazards

**ATA Chapter**: 57 — Wings  
**Folder**: 57-00-02_Safety / 57-00-02-10_HAZARD_ANALYSIS  
**Status**: DRAFT  
**Owner**: Airframe & Structures Domain (ATA 57)

---

## 1. Purpose

This document provides **high-level Functional Hazard Assessment (FHA) notes** for the ATA 57 Wing domain.

It identifies the primary functional hazards associated with the wing structure and its systems.

---

## 2. Wing Functions

The wing performs the following safety-relevant functions:

| Function ID | Function Description |
| :-- | :-- |
| F-57-01 | Provide lift during all flight phases |
| F-57-02 | Transfer flight loads to fuselage |
| F-57-03 | Provide roll control via ailerons/spoilers |
| F-57-04 | Provide high-lift capability via flaps/slats |
| F-57-05 | Store fuel in integral tanks |
| F-57-06 | Prevent ice accumulation on leading edges |
| F-57-07 | Support pylons and propulsion systems |

---

## 3. Functional Hazards Summary

### 3.1 Structural Hazards

| Hazard ID | Function | Failure Condition | Severity |
| :-- | :-- | :-- | :-- |
| H-57-STR-01 | F-57-01 | Loss of wing structural integrity | Catastrophic |
| H-57-STR-02 | F-57-02 | Failure of wing-fuselage attachment | Catastrophic |
| H-57-STR-03 | F-57-07 | Failure of pylon attachment | Catastrophic |
| H-57-STR-04 | F-57-01 | Undetected fatigue damage leading to failure | Catastrophic |

### 3.2 Aeroelastic Hazards

| Hazard ID | Function | Failure Condition | Severity |
| :-- | :-- | :-- | :-- |
| H-57-AER-01 | F-57-01 | Wing flutter within flight envelope | Catastrophic |
| H-57-AER-02 | F-57-03 | Aileron control reversal | Hazardous |
| H-57-AER-03 | F-57-01 | Wing divergence | Catastrophic |

### 3.3 Control Surface Hazards

| Hazard ID | Function | Failure Condition | Severity |
| :-- | :-- | :-- | :-- |
| H-57-CTL-01 | F-57-03 | Loss of aileron function | Hazardous |
| H-57-CTL-02 | F-57-04 | Asymmetric flap deployment | Hazardous |
| H-57-CTL-03 | F-57-04 | Asymmetric slat deployment | Hazardous |
| H-57-CTL-04 | F-57-03 | Uncommanded spoiler deployment | Hazardous |

### 3.4 Fuel System Hazards (Structural)

| Hazard ID | Function | Failure Condition | Severity |
| :-- | :-- | :-- | :-- |
| H-57-FUE-01 | F-57-05 | Fuel tank structural failure | Catastrophic |
| H-57-FUE-02 | F-57-05 | Fuel leakage due to structural damage | Hazardous |

### 3.5 Ice Protection Hazards

| Hazard ID | Function | Failure Condition | Severity |
| :-- | :-- | :-- | :-- |
| H-57-ICE-01 | F-57-06 | Loss of ice protection leading to unsafe ice accumulation | Hazardous |
| H-57-ICE-02 | F-57-06 | Runback ice affecting control surfaces | Major |

---

## 4. FHA Methodology Reference

Detailed FHA methodology and case studies are provided in:

- [57-00-02-20_FHA_Methodology.md](../57-00-02-20_FHA/57-00-02-20_FHA_Methodology.md)  
- [57-00-02-20_FHA_ATA57_Summary.md](../57-00-02-20_FHA/57-00-02-20_FHA_ATA57_Summary.md)  

---

## 5. Traceability

| From | To | Description |
| :-- | :-- | :-- |
| This document | Hazard Log Master | Hazards listed here are recorded in the master log |
| This document | FHA Cases | Each hazard has a detailed FHA case |
| Hazards | Safety Requirements | Hazards drive safety requirement derivation |

---

## Document Control

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.  
- Status: **DRAFT** — Subject to human review and approval.  
- Human approver: _[to be completed]_.  
- Repository: `AMPEL360-BWB-H2-Hy-E`  
- Last AI update: 2025-11-29
