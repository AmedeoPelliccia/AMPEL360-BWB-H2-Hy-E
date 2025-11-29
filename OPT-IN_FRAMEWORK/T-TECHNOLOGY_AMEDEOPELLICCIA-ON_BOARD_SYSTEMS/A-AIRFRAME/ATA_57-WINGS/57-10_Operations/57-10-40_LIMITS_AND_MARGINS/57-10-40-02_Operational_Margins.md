# 57-10-40-02 — Operational Margins

## Purpose

Define the operational margins maintained during normal operations to provide
safety buffers relative to structural limits.

## Speed Margins

### Normal Operations

| Condition | Operating Limit | Design Limit | Margin |
|-----------|-----------------|--------------|--------|
| Max speed (VMO) | TBD KIAS | VD = TBD KIAS | TBD KIAS |
| Max Mach (MMO) | Mach 0.78 | MD = TBD | TBD |
| Max gust | TBD KEAS | VC = TBD KEAS | As designed |

### Degraded Operations

| Condition | Reduced Limit | Standard Limit | Reduction |
|-----------|---------------|----------------|-----------|
| Temporary repair | MMO - 0.02 | MMO | 0.02 Mach |
| SHM advisory | Case-specific | Standard | Engineering eval |

## Load Factor Margins

### Normal Operations

| Condition | Operating Limit | Design Limit | Margin |
|-----------|-----------------|--------------|--------|
| Max positive G | +2.5 G | +3.75 G (UL) | 50% |
| Max negative G | -1.0 G | -1.5 G (UL) | 50% |

### Advisory Thresholds

| Level | Threshold | Action |
|-------|-----------|--------|
| Normal | < 80% limit | None |
| Caution | 80-95% limit | Awareness |
| Warning | 95-100% limit | Immediate review |
| Exceedance | > 100% limit | Engineering eval |

## Fatigue Margins

### Usage Indices

| Index | Threshold | Action |
|-------|-----------|--------|
| Cumulative fatigue | < 80% life | Normal ops |
| Cumulative fatigue | 80-90% life | Enhanced monitoring |
| Cumulative fatigue | > 90% life | Planning required |

## Real-Time Margin Monitoring

Wing margin status is computed by:
- 97-40-40-10_MARGIN_CALCULATION
- 97-40-40-20_ADVISORY_LOGIC

See [57-10-40-03_Link_to_Envelope_Analytics](./57-10-40-03_Link_to_Envelope_Analytics.md).

## References

- [57-10-40-01_Structural_Limits](./57-10-40-01_Structural_Limits.md)
- [57-10-40-03_Link_to_Envelope_Analytics](./57-10-40-03_Link_to_Envelope_Analytics.md)

---

## Document Control

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT** – Subject to human review and approval.
- Human approver: _[to be completed]_.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: _2025-11-28_.

---
