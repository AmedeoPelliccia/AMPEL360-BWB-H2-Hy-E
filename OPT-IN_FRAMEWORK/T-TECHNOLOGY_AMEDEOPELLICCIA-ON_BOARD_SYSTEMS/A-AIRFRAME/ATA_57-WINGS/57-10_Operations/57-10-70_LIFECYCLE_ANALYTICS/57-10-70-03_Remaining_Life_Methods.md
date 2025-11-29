# 57-10-70-03 — Remaining Life Methods

## Purpose

Define the methods used to calculate remaining structural life for wing
components based on usage data and inspection findings.

## Life Calculation Methods

### Safe-Life Approach

Used for components where replacement is scheduled.

```
Remaining Life (RL) = Design Life - Consumed Life
                    = N_design - Σ n_applied

Where:
  N_design = Design life in cycles/hours
  n_applied = Applied cycles/hours
```

| Component | Design Life | Life Basis |
|-----------|-------------|------------|
| Wing attach fittings | TBD cycles | Fatigue |
| Main spar caps | TBD cycles | Fatigue |
| Control surface hinges | TBD cycles | Wear + fatigue |

### Damage Tolerance Approach

Used for primary structure with inspection program.

| Parameter | Definition |
|-----------|------------|
| Threshold | Flight cycles before first inspection required |
| Interval | Flight cycles between repeat inspections |
| LOV | Limit of validity – maximum certified life |

```
Next Inspection Due = Last Inspection + Interval
End of Life = LOV (limit of validity)
```

### Condition-Based Approach

Used when SHM or inspection data indicates damage.

```
Remaining Life = f(Crack Size, Growth Rate, Critical Size)
              = (a_crit - a_current) / (da/dN)

Where:
  a_crit = Critical crack size
  a_current = Measured crack size
  da/dN = Crack growth rate
```

## Life Extension Options

### Analysis-Based Extension

| Method | Applicability | Approval |
|--------|---------------|----------|
| Refined analysis | Improved loads data | Engineering review |
| Test substantiation | Component test | Certification authority |
| Fleet leader program | Selected aircraft | Certification authority |

### Inspection-Based Extension

| Method | Applicability | Approval |
|--------|---------------|----------|
| Enhanced inspection | More frequent/detailed | Engineering approval |
| SHM credit | Continuous monitoring | Certification authority |
| Supplemental inspection | Additional methods | Engineering approval |

## Life Management System

### Tracking

| Data | Source | Update Frequency |
|------|--------|------------------|
| Cycles accumulated | Flight data | Per flight |
| Hours accumulated | Flight data | Per flight |
| Inspection status | Maintenance records | Per event |
| Damage status | Inspection/SHM | Per event |

### Forecasting

| Forecast | Method | Horizon |
|----------|--------|---------|
| Next inspection | Calendar/cycles | 90 days |
| Life limit approach | Linear projection | 1 year |
| Replacement planning | Fleet optimization | 5 years |

### Alerts

| Alert | Trigger | Lead Time |
|-------|---------|-----------|
| Inspection due | Approaching interval | 30 days / 100 cycles |
| Life limit approach | 90% consumed | 180 days |
| Life limit reached | 100% consumed | N/A (ground) |

## References

- [57-10-70-01_Usage_Index_Definition](./57-10-70-01_Usage_Index_Definition.md)
- [57-00_GENERAL](../../57-00_GENERAL/) (design life data)

---

## Document Control

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT** – Subject to human review and approval.
- Human approver: _[to be completed]_.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: _2025-11-28_.

---
