# 53-30-10-00 — Requirements Summary

**Document ID:** 53-30-10-00-002  
**Version:** 1.0  
**Date:** 2025-11-25  
**Status:** DRAFT

---

## 1. Purpose

This document summarizes requirements for the Harvesting subsystem of ANCHORS.

---

## 2. Functional Requirements

| Req ID | Requirement | Threshold |
|:--|:--|:--|
| REQ-H-001 | Harvest energy from cabin airflow | ≥ 2 kW |
| REQ-H-002 | Harvest waste heat | ≥ 1 kW |
| REQ-H-003 | Collect condensate water | ≥ 0.5 L/h |
| REQ-H-004 | Extract CO₂ from cabin air | ≥ 10% recirculation |

---

## 3. Performance Requirements

| Req ID | Requirement | Value |
|:--|:--|:--|
| REQ-H-010 | Airflow harvester efficiency | ≥ 60% |
| REQ-H-011 | TEG efficiency | ≥ 5% |
| REQ-H-012 | Pressure drop (per harvester) | ≤ 100 Pa |
| REQ-H-013 | Operating temperature range | -40°C to +70°C |

---

## 4. Interface Requirements

| Req ID | Requirement | Interface |
|:--|:--|:--|
| REQ-H-020 | ECS duct integration | Physical |
| REQ-H-021 | Power output to aircraft bus | 28 VDC |
| REQ-H-022 | Condensate to water system | Fluid |
| REQ-H-023 | CO₂ to capture system | Pneumatic |

---

## 5. Safety Requirements

| Req ID | Requirement | Rationale |
|:--|:--|:--|
| REQ-H-030 | No impact on ECS performance | Cabin comfort |
| REQ-H-031 | Fail-safe harvester design | Airflow continuity |
| REQ-H-032 | No containment breach | FOD prevention |

---

## Document Control

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT** — Subject to human review and approval.
- Human approver: _[to be completed]_.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: 2025-11-25
