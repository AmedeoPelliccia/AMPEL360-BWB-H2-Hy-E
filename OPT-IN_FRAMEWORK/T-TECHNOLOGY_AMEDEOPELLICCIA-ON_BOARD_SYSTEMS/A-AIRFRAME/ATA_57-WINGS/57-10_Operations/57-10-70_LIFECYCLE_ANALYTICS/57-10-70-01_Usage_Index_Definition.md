# 57-10-70-01 — Usage Index Definition

## Purpose

Define the usage indices used to track cumulative structural usage and
fatigue consumption for the wing structure.

## Index Types

### Flight-Based Indices

| Index | Formula | Units | Description |
|-------|---------|-------|-------------|
| Flight cycles | N_FC | count | Pressurization cycles |
| Flight hours | FH | hours | Block-to-block time |
| Extended range cycles | N_ER | count | Flights > TBD km |
| Short-haul cycles | N_SH | count | Flights < TBD km |

### Load-Based Indices

| Index | Formula | Units | Description |
|-------|---------|-------|-------------|
| Fatigue index | FI = Σ(n_i/N_i) | - | Miner's sum |
| Severity index | SI = Σ(G × t) | G·s | Integrated load factor |
| Exceedance count | N_EX | count | Limit exceedances |
| Hard landing count | N_HL | count | > TBD G landings |

### Component-Specific Indices

| Component | Index | Description |
|-----------|-------|-------------|
| Flap | N_flap | Flap extension cycles |
| Slat | N_slat | Slat extension cycles |
| Spoiler | N_spoiler | Spoiler deployment cycles |
| Aileron | θ_aileron | Cumulative deflection |

## Index Calculation

### Fatigue Index (FI)

```
FI = Σ (n_i / N_i)

Where:
  n_i = Applied cycles at stress level i
  N_i = Allowable cycles at stress level i (from S-N curve)
```

The fatigue index represents consumed life:
- FI = 0: New structure
- FI = 1.0: Design life consumed
- FI > 1.0: Beyond design life (requires evaluation)

### Severity Index (SI)

```
SI = Σ (|G - 1.0| × Δt)

Where:
  G = Load factor
  Δt = Time at load factor (seconds)
```

Higher SI indicates more severe usage than average.

## Index Thresholds

| Index | Normal | Enhanced Monitoring | Action Required |
|-------|--------|---------------------|-----------------|
| FI | < 0.7 | 0.7–0.9 | > 0.9 |
| SI (per flight) | < TBD | TBD–TBD | > TBD |
| Exceedances | 0 | 1–3 cumulative | > 3 cumulative |

## Index Storage

| Location | Content | Retention |
|----------|---------|-----------|
| Aircraft system | Current indices | Permanent |
| Ground database | Historical indices | Permanent |
| CAOS | Trend data | Per policy |

## References

- [57-10-70-02_Fleet_Analytics_Interface](./57-10-70-02_Fleet_Analytics_Interface.md)
- [57-10-70-03_Remaining_Life_Methods](./57-10-70-03_Remaining_Life_Methods.md)

---

## Document Control

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT** – Subject to human review and approval.
- Human approver: _[to be completed]_.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: _2025-11-28_.

---
