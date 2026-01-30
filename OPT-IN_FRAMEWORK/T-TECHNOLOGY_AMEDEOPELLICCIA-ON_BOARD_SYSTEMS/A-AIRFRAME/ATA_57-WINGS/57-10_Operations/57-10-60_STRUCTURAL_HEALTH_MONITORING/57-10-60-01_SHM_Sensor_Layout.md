# 57-10-60-01 — SHM Sensor Layout

## Purpose

Define the Structural Health Monitoring (SHM) sensor layout for the wing
structure, including sensor types, locations, and coverage.

## Sensor Types

| Sensor Type | Technology | Parameter Measured |
|-------------|------------|-------------------|
| Strain gauges | Foil/fiber | Local strain |
| Fiber optic | Bragg grating | Distributed strain, temperature |
| Acoustic emission | Piezoelectric | Crack initiation/growth |
| Comparative vacuum | CVMS | Disbond/delamination |
| Load cells | Strain gauge | Attachment loads |

## Sensor Zones

### Zone 1 – Wing Root

| Sensor ID | Type | Location | Critical Function |
|-----------|------|----------|-------------------|
| SHM-57-001 | Strain | Upper spar cap | Root bending |
| SHM-57-002 | Strain | Lower spar cap | Root bending |
| SHM-57-003 | Fiber optic | Root rib | Load distribution |
| SHM-57-004 | Load cell | Wing-body attach | Total wing load |

### Zone 2 – Inboard Wing

| Sensor ID | Type | Location | Critical Function |
|-----------|------|----------|-------------------|
| SHM-57-010 | Strain | Upper skin | Panel stress |
| SHM-57-011 | Strain | Lower skin | Panel stress |
| SHM-57-012 | Fiber optic | Front spar | Shear/bending |
| SHM-57-013 | Fiber optic | Rear spar | Shear/bending |

### Zone 3 – Mid-Span

| Sensor ID | Type | Location | Critical Function |
|-----------|------|----------|-------------------|
| SHM-57-020 | Strain | Upper skin | Panel stress |
| SHM-57-021 | Strain | Lower skin | Panel stress |
| SHM-57-022 | Acoustic emission | Spar caps | Crack detection |

### Zone 4 – Outboard Wing

| Sensor ID | Type | Location | Critical Function |
|-----------|------|----------|-------------------|
| SHM-57-030 | Strain | Upper skin | Panel stress |
| SHM-57-031 | Strain | Lower skin | Panel stress |
| SHM-57-032 | Fiber optic | Control surface attach | Hinge loads |

### Zone 5 – Wing Tip

| Sensor ID | Type | Location | Critical Function |
|-----------|------|----------|-------------------|
| SHM-57-040 | Strain | Tip structure | Tip loads |
| SHM-57-041 | Accelerometer | Tip | Flutter monitoring |

## Coverage Summary

| Zone | Primary Structure | Control Surfaces | Fastenings |
|------|-------------------|------------------|------------|
| Root | 100% | N/A | 100% |
| Inboard | 80% | 50% | Key joints |
| Mid-span | 60% | 50% | Key joints |
| Outboard | 40% | 75% | Key joints |
| Tip | 50% | 100% | Key joints |

## References

- [57-10-60-02_SHM_Data_Paths](./57-10-60-02_SHM_Data_Paths.md)
- [57-10-60-03_SHM_Alarm_Policies](./57-10-60-03_SHM_Alarm_Policies.md)

---

## Document Control

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT** – Subject to human review and approval.
- Human approver: _[to be completed]_.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: _2025-11-28_.

---
