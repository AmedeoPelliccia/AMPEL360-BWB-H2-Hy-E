# Sweep Angle Trade Study

**Document ID:** AMPEL360-02-11-00-DES-TRADE-004  
**Version:** 1.0.0

## Trade Study Overview

**Objective:** Select optimal leading edge sweep angle for cruise performance and structural efficiency.

## Options Evaluated

| Sweep | Mcruise | L/D | Wstruct | Manuf | CLmax | Score |
|-------|---------|-----|---------|-------|-------|-------|
| 30° | M0.75 | 20.5 | -5% | Simple | 2.8 | 68 |
| 35° | M0.80 | 20.8 | -2% | Standard | 2.6 | 82 |
| **37°** | **M0.82** | **21.0** | **Baseline** | **Standard** | **2.5** | **95** |
| 40° | M0.85 | 21.1 | +5% | Complex | 2.3 | 78 |
| 45° | M0.88 | 21.0 | +12% | Complex | 2.0 | 62 |

## Selection Criteria

**Performance (40%):**
- Cruise speed: M0.82 target
- L/D ratio: >20 target
- Low speed: Adequate CLmax

**Structural (30%):**
- Wing weight: Minimize
- Load distribution: Optimal
- Manufacturing: Feasible

**Operations (20%):**
- Route compatibility: 95% network
- Weather capability: All conditions
- Fuel efficiency: Competitive

**Risk (10%):**
- Technology readiness
- Manufacturing maturity
- Certification path

## Analysis: 37° Selection

### Aerodynamic Performance

**Cruise (M0.82):**
- Effective Mach: M × cos(37°) = 0.656
- Critical Mach: 0.72 (airfoil dependent)
- **Margin: 10% (adequate)**

**Wave Drag:**
- Onset: M0.85 (37° sweep)
- Cruise: M0.82 (below onset)
- Drag rise: Not a factor

**L/D Achievement:**
- 37° sweep: L/D = 21.0
- Meets target with margin
- Competitive with best in class

### Low Speed Performance

**CLmax (with high-lift devices):**
- 37° reduces CLmax by ~12%
- High-lift devices: +150% baseline CL
- **Resulting CLmax: 2.5 (adequate)**

**Approach Speed:**
- Target: 135 KIAS
- With CLmax = 2.5: Achievable
- Field length: 2,400m (acceptable)

**Stall Characteristics:**
- Root stalls first (design intent)
- Progressive stall (safe)
- Control maintained

### Structural Considerations

**Wing Bending Loads:**
- 37° reduces effective span load
- Root bending moment: Acceptable
- Structural weight: Baseline

**Manufacturing:**
- Composite layup: Standard process
- Fiber orientation: Manageable
- Tooling complexity: Moderate
- Cost: Acceptable

## Alternative Analysis

### 35° Sweep

**Advantages:**
- 2% lighter structure
- Better low-speed performance
- Simpler manufacturing

**Disadvantages:**
- M0.80 maximum cruise (too slow)
- Route network: 15% reduction
- Competitive position: Weaker

**Decision:** REJECTED (performance insufficient)

### 40° Sweep

**Advantages:**
- M0.85 cruise capability
- More future-proof
- Slightly better L/D (+0.1)

**Disadvantages:**
- 5% heavier structure
- Reduced CLmax (2.3)
- Higher manufacturing cost
- Target market: M0.82 sufficient

**Decision:** REJECTED (excessive for requirements)

## Validation

**CFD Analysis:**
- All sweep angles modeled
- Cruise performance: Validated
- Wave drag: Confirmed
- 37° optimal for mission

**Wind Tunnel:**
- Multiple configurations
- Force measurements
- Flow visualization
- Stall progression tested

**Flight Simulation:**
- Handling qualities: Level 1
- Approach/landing: Acceptable
- Performance: Meets requirements

## Final Decision

**37° leading edge sweep selected because:**

1. **Cruise Performance:** M0.82 capability achieved
2. **Efficiency:** L/D = 21.0 meets target
3. **Structural:** Weight penalty acceptable
4. **Low Speed:** CLmax adequate for operations
5. **Manufacturing:** Standard composite process
6. **Market:** Optimal for target routes (95%)
7. **Risk:** Low technical and schedule risk

**Sensitivity:**
- ±1°: Minimal impact
- ±2°: Noticeable but acceptable
- **Decision: ROBUST**

**Decision Date:** 2024-02-15  
**Approved:** Chief Aerodynamicist, Chief Engineer  
**Status:** Baseline frozen (2024-04-01)
