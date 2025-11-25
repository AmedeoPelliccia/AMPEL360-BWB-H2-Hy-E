# 53-30-00-02 — Preliminary System Safety Assessment

**Document ID:** 53-30-00-02-003  
**Version:** 1.0  
**Date:** 2025-11-25  
**Status:** DRAFT

---

## 1. Purpose

This document presents the Preliminary System Safety Assessment (PSSA) for ANCHORS systems, establishing the safety architecture and derived safety requirements.

---

## 2. PSSA Objectives

Per ARP4761:

1. Derive safety requirements from FHA
2. Allocate requirements to system architecture
3. Establish failure probability budgets
4. Identify common cause failure concerns

---

## 3. Safety Architecture

### 3.1 Independence Requirements

| System | Required Independence |
|:--|:--|
| Battery thermal management | Dual independent cooling loops |
| CO₂ capture | Single system with manual backup |
| Water recycling | Single system with bypass |
| Energy harvesting | No independence required |

### 3.2 Monitoring Requirements

| Hazard | Monitoring Requirement |
|:--|:--|
| Battery thermal runaway | Cell-level temperature sensing |
| CO₂ leak | Concentration monitoring in bays |
| Water contamination | Quality sensors at output |

---

## 4. Derived Safety Requirements

| DSR ID | Requirement | Traces to |
|:--|:--|:--|
| DSR-001 | Battery cells shall be thermally isolated | FC-005 |
| DSR-002 | Cooling loop failure shall be detected within 5s | FC-005 |
| DSR-003 | CO₂ bay shall have ventilation provisions | FC-003 |
| DSR-004 | Battery bay fire suppression shall be automatic | FC-005 |
| DSR-005 | Thermal runaway shall not propagate between cells | FC-005 |

---

## 5. Probability Budget Allocation

For FC-005 (Battery Thermal Runaway) - Hazardous (< 10⁻⁷):

| Contributor | Allocated Budget |
|:--|:--|
| Cell manufacturing defect | < 10⁻⁸ |
| Cooling system failure | < 10⁻⁸ |
| External damage | < 10⁻⁸ |
| Control system malfunction | < 10⁻⁸ |

---

## 6. Common Cause Analysis

Potential common cause failures:

| CCA ID | Common Cause | Affected Systems | Mitigation |
|:--|:--|:--|:--|
| CCA-001 | Electrical bus failure | Cooling, monitoring | Backup power |
| CCA-002 | Software error | All controlled systems | DAL assessment |
| CCA-003 | Coolant leak | Thermal management | Leak detection |

---

## TODO

- [ ] Complete fault tree development
- [ ] Finalize probability allocations
- [ ] Coordinate with subsystem suppliers

---

## Document Control

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT** — Subject to human review and approval.
- Human approver: _[to be completed]_.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: 2025-11-25
