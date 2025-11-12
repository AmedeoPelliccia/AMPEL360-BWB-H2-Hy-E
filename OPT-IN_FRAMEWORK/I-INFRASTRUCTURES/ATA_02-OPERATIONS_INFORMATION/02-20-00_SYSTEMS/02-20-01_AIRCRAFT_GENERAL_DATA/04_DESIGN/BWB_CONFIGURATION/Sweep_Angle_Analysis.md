# Sweep Angle Analysis

## Executive Summary

The AMPEL360 BWB leading edge sweep angle of 37° was selected to optimize high-speed cruise performance while maintaining structural efficiency and control authority.

## Design Requirements

### Cruise Performance
- **Target Mach Number:** M = 0.78
- **Cruise Altitude:** 39,000 ft
- **Wave Drag:** Minimize transonic effects
- **Laminar Flow:** Maximize extent on upper surface

### Structural Efficiency
- **Wing Box Layout:** Optimize spar arrangement
- **Load Paths:** Efficient transfer to center body
- **Torsional Rigidity:** Adequate flutter margins

## Sweep Angle Selection

### Analysis Matrix

| LE Sweep | Critical Mach | Structural Weight | Control | Score |
|----------|--------------|-------------------|---------|-------|
| 30°      | M=0.75       | Baseline          | Good    | 0.78  |
| 35°      | M=0.77       | +2%               | Good    | 0.88  |
| **37°**  | **M=0.80**   | **+3%**           | **Fair**| **0.92** |
| 40°      | M=0.82       | +6%               | Poor    | 0.81  |
| 45°      | M=0.85       | +11%              | Poor    | 0.68  |

## Selected Configuration (37° LE Sweep)

### Aerodynamic Performance

**Critical Mach Number**
- **Mcrit = 0.80** (exceeds M=0.78 cruise requirement)
- **Margin:** 2.6% above operating Mach
- **Wave drag rise:** Delayed to M=0.82

**Quarter Chord Sweep**
- **Λc/4 = 32°**
- Derived from leading edge geometry
- Optimizes subsonic lift distribution

**Trailing Edge Sweep**
- **ΛTE = -12°** (forward swept)
- Improves lateral stability
- Enhances aileron effectiveness

### Structural Implications

**Wing Box Design**
- Three-spar configuration
- Front spar: 15% chord
- Rear spar: 70% chord
- Center spar: 40% chord (load relief)

**Weight Impact**
- **+3% vs 35° sweep**
- Acceptable for performance gains
- Composite construction mitigates penalty

### Control Considerations

**Roll Authority**
- Reduced by sweep angle
- Compensated by:
  - Increased aileron span (30% semi-span)
  - Differential thrust capability
  - Spoiler augmentation

**Yaw Stability**
- Enhanced by forward swept trailing edge
- Vertical stabilizer sizing reduced
- Improved spiral stability

## High-Lift System Integration

### Leading Edge Devices
- **Full-span Krueger flaps**
- Deployment compatible with 37° sweep
- CL,max = 2.8 (landing configuration)

### Trailing Edge Flaps
- **Double-slotted Fowler flaps**
- 60% semi-span coverage
- Forward sweep aids deployment kinematics

## Flutter Considerations

### Critical Speeds
- **Flutter speed:** VF > 1.4 × VD
- **Divergence speed:** VD = 420 KEAS
- **Sweep reduces flutter risk**

### Damping Characteristics
- Adequate structural damping
- CAOS active flutter suppression as backup
- Ground vibration testing planned

## Conclusion

The 37° leading edge sweep angle provides optimal balance of:
- High-speed cruise efficiency (M=0.78)
- Structural practicality (+3% weight)
- Adequate control authority
- Flutter margin compliance

This configuration enables AMPEL360 to achieve its performance targets while maintaining safety and operational flexibility.

---

**References:**
- CFD Report BWB-AER-2025-004: Transonic Analysis
- Flutter Analysis BWB-STR-2025-008
- Control Authority Study BWB-FLT-2025-006
- High-Lift Performance BWB-AER-2025-011
