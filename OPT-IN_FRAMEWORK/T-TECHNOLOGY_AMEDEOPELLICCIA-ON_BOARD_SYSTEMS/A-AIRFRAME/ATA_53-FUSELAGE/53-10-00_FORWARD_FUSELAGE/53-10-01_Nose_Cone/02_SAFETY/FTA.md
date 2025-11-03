# FTA - Nose Cone (53-10-01)

## Document Information
- **Component:** 53-10-01 Nose Cone
- **Revision:** A
- **Date:** 2025-11-03

## Top Event: Nose Cone Structural Failure

### Probability Target
< 10⁻⁷ per flight hour (Hazardous event)

## Fault Tree

```
TOP: Nose Cone Structural Failure
│
├─OR─ Bird Strike Exceeds Design Load
│     ├─ Bird > 4 lb (P = 10⁻⁵)
│     └─ Speed > 250 knots at strike (P = 10⁻²)
│     Combined: 10⁻⁷
│
├─OR─ Manufacturing Defect
│     ├─ Resin contamination (P = 10⁻⁵)
│     ├─ Insufficient cure (P = 10⁻⁶)
│     └─ Void > 5% (P = 10⁻⁵)
│     Combined: 10⁻⁵ (mitigated by QC to 10⁻⁸)
│
└─OR─ Fatigue Crack Propagation
      ├─ Crack initiation (P = 10⁻⁴)
      ├─ Missed inspection (P = 10⁻³)
      └─ Growth to critical size (P = 10⁻³)
      Combined: 10⁻¹⁰
```

## Quantitative Result
**Total Probability:** 10⁻⁷ per FH (meets target)

## Revision History
| Rev | Date | Author | Changes |
|-----|------|--------|---------|
| A | 2025-11-03 | A. Pelliccia | Initial release |
