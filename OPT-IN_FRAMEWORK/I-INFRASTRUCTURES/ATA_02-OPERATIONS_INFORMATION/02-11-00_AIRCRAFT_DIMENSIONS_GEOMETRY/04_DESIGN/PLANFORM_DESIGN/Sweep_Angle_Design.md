# Sweep Angle Design

**Document ID:** AMPEL360-02-11-00-DES-PF-004  
**Version:** 1.0.0

## Leading Edge Sweep Configuration

**Average Sweep:** 37°  
**Type:** Compound curve (variable sweep)

### Sweep Distribution

| Station | Sweep Angle | Rationale |
|---------|-------------|-----------|
| Root (centerline) | 45° | Structural integration, center body blend |
| Inner wing (0-10m) | 40° | Smooth transition, passenger cabin |
| Mid wing (10-20m) | 37° | Cruise optimization, primary lifting surface |
| Outer wing (20-26m) | 33° | Tip effects, structural taper |

## Design Requirements

### Cruise Speed Performance

**Target:** M0.82 at 41,000 ft

**Sweep Requirements:**
- M0.75: 30° minimum
- M0.80: 35° minimum  
- **M0.82: 37° required**
- M0.85: 40° required

**Selection:** 37° average sweep
- Enables M0.82 cruise
- Margin for adverse conditions
- Acceptable structural weight

### Compressibility Effects

**Critical Mach Number:**
- Wing section: Mcrit = 0.72 (zero sweep)
- With 37° sweep: Meff = M × cos(37°) = 0.82 × 0.8 = 0.656
- Meff < Mcrit: No shock waves at cruise

**Drag Rise:**
- Wave drag onset: M0.85 (with 37° sweep)
- Cruise margin: M0.82 (safe)
- Drag divergence: M0.88

### Low Speed Considerations

**Stall Characteristics:**
- Compound sweep improves stall progression
- Root stalls first (safe)
- Tip maintains control authority
- Acceptable handling qualities

**High-Lift Performance:**
- Leading edge devices: Full span
- Trailing edge flaps: 70% span
- Sweep reduces CL,max by 15%
- Compensated by device effectiveness

## Trade Study Results

| Sweep | Mcruise | L/Dcruise | Wstructure | CL,max | Selection |
|-------|---------|-----------|------------|---------|-----------|
| 30° | M0.75 | 20.5 | -5% | 2.8 | Too slow |
| 35° | M0.80 | 20.8 | -2% | 2.6 | Marginal |
| **37°** | **M0.82** | **21.0** | **Baseline** | **2.5** | **SELECTED** |
| 40° | M0.85 | 21.1 | +5% | 2.3 | Too heavy |

## Structural Impact

**Bending Loads:**
- Sweep reduces effective span
- Lower root bending moment
- Structural weight acceptable

**Load Distribution:**
- Compound sweep optimizes lift distribution
- Reduced wing tip loads
- Better integration with center body

**Manufacturing:**
- 37° manageable for composite layup
- Standard tooling compatible
- Assembly alignment acceptable

## Aerodynamic Benefits

**Laminar Flow:**
- 37° sweep enables natural laminar flow
- Up to 40% chord on center body
- Up to 25% chord on outer wing
- Significant drag reduction

**Induced Drag:**
- Optimal lift distribution
- Reduced vortex strength at tips
- Effective AR increased
- Better cruise efficiency

**Interference Effects:**
- Smooth blending with center body
- Reduced shock-boundary layer interaction
- Lower interference drag

## Operational Considerations

**Airport Compatibility:**
- Sweep affects gate positioning
- 37° allows standard gate angles
- Turning radius manageable
- Ground operations validated

**Maintenance Access:**
- Leading edge access adequate
- Systems routing feasible
- Inspection points accessible

## Certification Aspects

**CS-25 Requirements:**
- Stall characteristics: Compliant
- Control effectiveness: Adequate
- Flutter margin: +20% above Vd
- Emergency descent: Acceptable

**Safety Considerations:**
- Stall warning adequate
- Deep stall avoided
- Spin resistance confirmed
- Emergency handling: Level 1

## Validation Testing

**Wind Tunnel:**
- Multiple sweep angles tested
- 37° optimal for L/D at M0.82
- Stall characteristics acceptable
- Pressure distribution validated

**CFD Analysis:**
- Shock wave position confirmed
- Boundary layer behavior modeled
- Laminar flow extent predicted
- Results match wind tunnel

**Flight Simulation:**
- Cruise performance validated
- Approach and landing tested
- Crosswind handling confirmed
- Pilot acceptance high

## Future Optimization

**Potential Improvements:**
- Active flow control
- Adaptive geometry (morphing)
- Load alleviation systems
- Advanced high-lift devices

**Technology Readiness:**
- Current design: TRL 6
- Production design: TRL 7
- Service entry: TRL 9 (target)

## Final Decision

**37° average sweep selected because:**

1. **Performance:** M0.82 cruise capability achieved
2. **Efficiency:** L/D = 21.0 at cruise
3. **Structural:** Acceptable weight penalty
4. **Manufacturing:** Standard composite processes
5. **Operations:** Compatible with airports
6. **Certification:** Clear compliance path
7. **Risk:** Low technical risk

**Approved:** 2024-02-15  
**Frozen:** 2024-04-01  
**Status:** Production baseline
