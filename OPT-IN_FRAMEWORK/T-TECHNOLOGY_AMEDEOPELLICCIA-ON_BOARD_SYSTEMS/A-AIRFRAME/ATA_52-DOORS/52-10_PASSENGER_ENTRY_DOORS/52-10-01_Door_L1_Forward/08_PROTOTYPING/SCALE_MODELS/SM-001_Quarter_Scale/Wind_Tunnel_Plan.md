# Wind Tunnel Test Plan
## SM-001 Quarter-Scale Aerodynamic Testing

**Document:** SM-001-WT-PLAN  
**Status:** Optional  
**Date:** 2025-11-03

### Test Objectives

1. Measure door drag contribution
2. Map surface pressure distribution
3. Identify flow separation regions
4. Validate CFD predictions

### Test Matrix

| Run | Velocity (m/s) | AoA (deg) | Sideslip (deg) | Config |
|-----|----------------|-----------|----------------|--------|
| 1-10 | 30 | 0 | 0 | Baseline |
| 11-20 | 50 | 0 | 0 | Baseline |
| 21-30 | 70 | 0 | 0 | Baseline |
| 31-40 | 50 | -5 to +10 | 0 | AoA sweep |
| 41-50 | 50 | 0 | ±15 | Sideslip |

### Data Acquisition

- Pressure transducers (0-5 psi range)
- 6-component force balance
- High-speed video (flow viz)
- Data rate: 1000 Hz

### Acceptance Criteria

- [ ] All pressure taps functional
- [ ] Drag within ±10% of CFD
- [ ] No unexpected flow separation
- [ ] Model survives all runs

---

**Document Control:** SM-001-WT-001  
**Revision:** A
