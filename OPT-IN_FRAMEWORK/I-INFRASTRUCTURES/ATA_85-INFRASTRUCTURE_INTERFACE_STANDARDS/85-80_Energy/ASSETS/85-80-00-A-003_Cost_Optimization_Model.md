# 85-80-00-A-003 Cost Optimization Model

## Objective Function

Minimize total energy cost over planning horizon:

```
Min: Σ (C_grid × P_grid + C_DG × P_DG + C_storage_deg × P_storage + C_DR × P_DR - R_export × P_export)
```

Subject to constraints:
- Power balance at each node
- Generator capacity limits
- Storage SOC limits
- Renewable generation availability
- Grid import/export limits

## Cost Components

| Component | Unit Cost | Notes |
|-----------|-----------|-------|
| Grid Import (Peak) | 0.18 EUR/kWh | Time-of-use rate |
| Grid Import (Off-Peak) | 0.08 EUR/kWh | Nighttime rate |
| Demand Charge | 15 EUR/kW/month | Based on peak demand |
| BESS Degradation | 0.02 EUR/kWh | Cycle-based cost |
| Diesel Generator | 0.35 EUR/kWh | Fuel + O&M |
| H2 Fuel | 8.00 EUR/kg | Green H2 cost |
| Renewable (LCOE) | 0.05 EUR/kWh | Solar+Wind average |

## Optimization Horizons

- **Real-Time**: 5-minute dispatch
- **Intra-Day**: 1-hour rolling horizon (24 hours)
- **Day-Ahead**: Hourly for next 48 hours
- **Weekly**: Daily resolution for 7 days

## Key Performance Indicators

- Total energy cost (EUR/month)
- Peak demand (kW)
- Renewable penetration (%)
- Carbon intensity (gCO2/kWh)
- BESS utilization (cycles/day)

## Document Control

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT** – Subject to human review and approval.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: _2025-11-22_.
