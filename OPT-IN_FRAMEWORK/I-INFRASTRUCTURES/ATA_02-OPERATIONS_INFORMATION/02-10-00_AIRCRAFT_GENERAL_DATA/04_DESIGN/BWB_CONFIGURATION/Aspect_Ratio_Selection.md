# Aspect Ratio Selection

## Executive Summary

The AMPEL360 BWB aspect ratio of 3.2 was selected as the optimal balance between aerodynamic efficiency, structural weight, and operational constraints.

## Analysis Process

### Design Space Exploration

Aspect ratios from 2.5 to 4.5 were evaluated against:
- Induced drag reduction
- Structural weight penalty
- Fuel tank volume impact
- Manufacturing complexity
- Ground handling constraints

### Trade Study Results

| Aspect Ratio | L/D | Structural Weight | Score |
|--------------|-----|-------------------|-------|
| 2.5          | 19.8| Baseline          | 0.82  |
| 3.0          | 20.5| +3%               | 0.91  |
| **3.2**      | **20.8** | **+5%**      | **0.95** |
| 3.5          | 21.1| +8%               | 0.89  |
| 4.0          | 21.4| +14%              | 0.76  |

## Selected Configuration (AR = 3.2)

### Aerodynamic Benefits
- **Induced Drag:** 18% reduction vs AR=2.5
- **L/D Ratio:** 20.8 (cruise condition)
- **Oswald Efficiency:** 0.88

### Structural Considerations
- **Weight Penalty:** +5% vs baseline
- **Acceptable** for performance gains achieved
- **Wing Box Depth:** Adequate for systems integration

### Operational Advantages
- **Wingspan:** 52.0 m (fits Code F gates)
- **Ground Clearance:** 3.8 m wingtip height
- **Maneuverability:** Acceptable for commercial operations

## Supporting Analysis

### Induced Drag Equation
```
CDi = CL² / (π × AR × e)
```
Where:
- CL = Lift coefficient = 0.52 (cruise)
- AR = Aspect ratio = 3.2
- e = Oswald efficiency = 0.88

### Wing Loading
- **W/S = 850 kg/m²** at MTOW
- Optimized for cruise efficiency
- Acceptable takeoff and landing performance

## Conclusion

Aspect ratio 3.2 provides the optimal balance of aerodynamic efficiency and structural practicality for the AMPEL360 BWB configuration, enabling the target L/D ratio of 21 while maintaining commercial viability.

---

**References:**
- CFD Analysis Report BWB-AER-2025-001
- Structural Analysis Report BWB-STR-2025-003
- Trade Study Matrix BWB-DES-2025-012
