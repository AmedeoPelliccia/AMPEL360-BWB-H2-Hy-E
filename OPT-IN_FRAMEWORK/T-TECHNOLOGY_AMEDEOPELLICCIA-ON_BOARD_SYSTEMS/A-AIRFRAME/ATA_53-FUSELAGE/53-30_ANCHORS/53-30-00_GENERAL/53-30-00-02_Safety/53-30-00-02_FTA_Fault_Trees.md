# 53-30-00-02 — Fault Tree Analysis

**Document ID:** 53-30-00-02-005  
**Version:** 1.0  
**Date:** 2025-11-25  
**Status:** DRAFT

---

## 1. Purpose

This document presents the Fault Tree Analysis (FTA) for critical ANCHORS failure conditions, supporting the quantitative safety assessment.

---

## 2. FTA Methodology

Fault trees are developed per ARP4761 guidelines:

- Top event: Failure condition from FHA
- Gates: AND, OR, transfer gates
- Basic events: Component failures with rates

---

## 3. FTA-001: Battery Thermal Runaway

### Top Event
Battery thermal runaway in flight (FC-005)

### Fault Tree Structure

```
                    [Battery Thermal Runaway]
                              |
              ________________|________________
             |                                 |
        [Cell Failure]                 [Cooling Failure]
             |                                 |
      _______|_______                   _______|_______
     |               |                 |               |
[Manufacturing] [External      [Pump         [Coolant
   Defect]      Damage]        Failure]       Leak]
```

### Basic Event Probabilities

| Event | Probability | Source |
|:--|:--|:--|
| Manufacturing defect | TBD | Supplier data |
| External damage | TBD | Analysis |
| Pump failure | TBD | Supplier data |
| Coolant leak | TBD | Test data |

---

## 4. FTA-002: CO₂ Cartridge Leak

### Top Event
CO₂ release in equipment bay (FC-003)

### Fault Tree Structure

```
                    [CO₂ Leak in Bay]
                           |
              _____________|_____________
             |                           |
      [Cartridge Seal          [Connection
         Failure]                Failure]
             |                           |
      _______|_______             _______|_______
     |               |           |               |
[Seal Wear]    [Overpressure]  [Fitting      [Vibration
                                Loosening]    Damage]
```

---

## 5. Minimal Cut Sets

### FTA-001 Minimal Cut Sets

| MCS | Events | Order |
|:--|:--|:--|
| MCS-1 | Manufacturing defect | 1 |
| MCS-2 | External damage | 1 |
| MCS-3 | Pump failure AND no detection | 2 |

### FTA-002 Minimal Cut Sets

| MCS | Events | Order |
|:--|:--|:--|
| MCS-1 | Seal failure | 1 |
| MCS-2 | Connection failure | 1 |

---

## TODO

- [ ] Complete quantitative analysis with supplier data
- [ ] Develop FTA diagrams in SVG format
- [ ] Perform sensitivity analysis

---

## Document Control

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT** — Subject to human review and approval.
- Human approver: _[to be completed]_.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: 2025-11-25
