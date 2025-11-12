# Planform Geometry

**Document ID:** AMPEL360-02-11-00-BWB-001  
**Version:** 1.0.0

## Overview

The AMPEL360 planform geometry represents the top-view shape of the blended wing body, defining the aircraft's aerodynamic and structural layout.

## Planform Characteristics

### Leading Edge

**Leading Edge Sweep:**
- Root (BL 0): 37° sweep angle
- Mid-span (BL ±15): 35° sweep angle  
- Outer wing (BL ±24): 40° sweep angle
- Average: 37° sweep

**Leading Edge Shape:**
- Continuous compound curve from centerline to tip
- Smooth radius transitions at blend points
- No discontinuities or kinks
- Optimized for M0.82 cruise Mach number

**Design Features:**
- Natural laminar flow capability forward of max thickness
- Reduced wave drag at cruise speeds
- Low supersonic drag rise characteristics
- Ice protection integration

### Trailing Edge

**Trailing Edge Configuration:**
- Center body (BL 0 to ±12): Straight, 0° sweep
- Transition (BL ±12 to ±19): Linear taper, -5° forward sweep
- Outer wing (BL ±19 to ±26): Forward sweep, -12°
- Total trailing edge span: 45 m

**Control Surfaces:**
- 12 elevon segments along trailing edge
- Segment width: 3.5 m average
- Chord: 2.8 m (25% local chord)
- Total control surface area: 118 m²

### Wingtips

**Winglet Configuration:**
- Type: Blended winglet (raked design)
- Height: 3.5 m above wing plane
- Cant angle: 75° from horizontal
- Toe-in: 2° inward
- Sweep: 35° leading edge

**Winglet Benefits:**
- 8% reduction in induced drag
- Improved span loading distribution
- Reduced wingtip vortex strength
- Better climb and cruise efficiency

## Planform Dimensions

### Area Distribution

| Region | Span Range | Reference Area | % of Total |
|--------|------------|----------------|------------|
| Center Body | BL 0 to ±19 | 520 m² | 61.5% |
| Mid Wing | BL ±19 to ±24 | 225 m² | 26.6% |
| Outer Wing | BL ±24 to ±26 | 100 m² | 11.9% |
| **Total** | **BL 0 to ±26** | **845 m²** | **100%** |

### Chord Distribution

**Centerline (BL 0):**
- Root chord: 35.0 m
- Leading edge: STA 3.2 m
- Trailing edge: STA 38.2 m
- Maximum thickness location: 35% chord (STA 15.5 m)

**Center Body Edge (BL ±19):**
- Local chord: 28.5 m
- Leading edge: STA 4.5 m
- Trailing edge: STA 33.0 m
- Taper ratio: 0.81

**Outer Wing (BL ±24):**
- Local chord: 6.0 m
- Leading edge: STA 16.0 m
- Trailing edge: STA 22.0 m
- Taper ratio: 0.17

**Wingtip (BL ±26):**
- Tip chord: 3.5 m
- Leading edge: STA 18.0 m
- Trailing edge: STA 21.5 m
- Taper ratio: 0.10

## Aerodynamic Reference

### Mean Aerodynamic Chord (MAC)

**MAC:** 22.5 m

**MAC Location:**
- Spanwise: BL ±8.5 m
- Longitudinal: Leading edge at STA 8.0 m
- Trailing edge at STA 30.5 m

**Center of Gravity Reference:**
- CG range: 20% to 35% MAC
- Neutral point: 38% MAC
- Static margin: 5% to 18% MAC

### Reference Points

**Aerodynamic Center:**
- Location: 25% MAC = STA 13.6 m
- Spanwise: BL ±8.5 m
- Vertical: WL 6.0 m (approximate)

**Quarter Chord Line:**
- Sweep: 32° (less than LE sweep)
- Used for compressibility corrections
- Subsonic aerodynamic reference

## Planform Optimization

### Design Objectives

1. **Cruise Efficiency:**
   - L/D = 21 at M0.82, 35,000 ft
   - Natural laminar flow over 40% chord
   - Low wave drag characteristics

2. **Span Loading:**
   - Elliptical lift distribution approximation
   - Induced drag minimization
   - Structural efficiency

3. **Control Authority:**
   - Pitch control: Elevon effectiveness
   - Roll control: Differential elevon
   - Yaw control: Split elevons (drag rudders)

### Trade-Offs

**Aspect Ratio (3.2):**
- Lower than conventional (9-10)
- Justified by lifting body contribution
- Structural efficiency gained
- Induced drag managed through high efficiency factor (e=0.85)

**Sweep Distribution:**
- Outboard sweep increased for:
  - Aeroelastic tailoring
  - Flutter margin improvement
  - Wave drag management
- Reduced sweep inboard for:
  - Volume efficiency
  - Structural load paths
  - Passenger space

## Structural Implications

### Load Distribution

**Span-wise Load:**
- More uniform than conventional wing
- Reduced wing root bending moment
- Better fatigue characteristics

**Chord-wise Load:**
- Load carried by entire planform
- Fuselage contributes to lift
- Reduced wing box stress

### Spar Locations

**Main Spar:**
- Front spar: 25% local chord
- Rear spar: 65% local chord
- Spar spacing: ~40% chord

**Carry-Through Structure:**
- Location: STA 22 to 28
- Continuous across centerline
- Carries main wing loads

## Manufacturing Considerations

### Panel Layout

**Upper Surface:**
- 12 major composite panels
- Panel joints align with ribs
- Automated fiber placement manufacturing

**Lower Surface:**
- 14 major composite panels
- Includes landing gear doors
- Co-bonded or mechanically fastened

### Tolerances

**Planform Tolerances:**
- Leading edge: ±50 mm
- Trailing edge: ±30 mm
- Spar locations: ±10 mm
- Control surface hinge lines: ±5 mm

**Surface Quality:**
- Waviness: <2 mm per meter
- Step/gap: <0.5 mm at joints
- Surface finish: 3.2 μm Ra average

## Comparison with Conventional

| Parameter | AMPEL360 BWB | A320 (Conventional) | Difference |
|-----------|--------------|---------------------|------------|
| Wing Area | 845 m² | 122.6 m² | +590% |
| Aspect Ratio | 3.2 | 9.5 | -66% |
| Sweep (LE) | 37° | 25° | +48% |
| L/D (cruise) | 21 | 17 | +24% |
| Lifting surface | 100% | 50% (wing only) | +100% |

## Regulatory Compliance

**Certification Basis:**
- EASA CS-25: Large aeroplanes
- FAA Part 25: Airworthiness standards
- Special conditions for BWB configuration

**Testing Requirements:**
- Wind tunnel validation (completed)
- CFD correlation (validated)
- Flight test verification (planned)
