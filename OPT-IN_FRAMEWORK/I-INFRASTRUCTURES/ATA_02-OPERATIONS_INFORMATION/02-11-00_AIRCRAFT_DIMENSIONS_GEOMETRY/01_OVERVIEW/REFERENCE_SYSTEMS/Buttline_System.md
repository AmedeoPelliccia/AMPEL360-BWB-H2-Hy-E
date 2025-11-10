# Buttline System (Y-Axis)

**Document ID:** AMPEL360-02-11-00-REF-004  
**Version:** 1.0.0

## Overview

The buttline system defines lateral positions on the AMPEL360 BWB H₂ aircraft, measured along the Y-axis from the aircraft centerline.

## Buttline Definition

**Buttline (BL):** Lateral distance in meters from the aircraft centerline.

**Notation:** "BL ±X.X" where:
- BL 0 = Centerline
- BL +X.X = Right side (starboard), X.X meters from centerline
- BL -X.X = Left side (port), X.X meters from centerline

**Example:** BL +10.0 = 10.0 meters right of centerline

## Primary Buttlines

### Centerline Region (BL 0 to ±5)

| Buttline | Distance | Description | Significance |
|----------|----------|-------------|--------------|
| **BL 0** | 0.0 m | Aircraft centerline | Symmetry axis, datum |
| **BL ±2** | ±2.0 m | Cockpit seats | Pilot/co-pilot lateral position |
| **BL ±3** | ±3.0 m | Center aisle | Main cabin centerline aisle |
| **BL ±5** | ±5.0 m | Fuselage side (notional) | Inner cabin edge |

### Inner Center Body (BL ±5 to ±15)

| Buttline | Distance | Description | Significance |
|----------|----------|-------------|--------------|
| **BL ±8.5** | ±8.5 m | MAC spanwise location | Mean aerodynamic chord |
| **BL ±10** | ±10.0 m | Inner cabin edge | Passenger seating limit |
| **BL ±12** | ±12.0 m | Fuel cell beginning | Systems integration starts |
| **BL ±15** | ±15.0 m | Main landing gear | MLG attachment point |

### Outer Center Body (BL ±15 to ±19)

| Buttline | Distance | Description | Significance |
|----------|----------|-------------|--------------|
| **BL ±17** | ±17.0 m | Outer passenger seats | Last row of seats |
| **BL ±19** | ±19.0 m | Center body edge | Transition to outer wing |

### Outer Wing (BL ±19 to ±26)

| Buttline | Distance | Description | Significance |
|----------|----------|-------------|--------------|
| **BL ±20** | ±20.0 m | Inner wing | Transition section |
| **BL ±22** | ±22.0 m | Mid wing | Primary wing structure |
| **BL ±24** | ±24.0 m | Outer wing | Aerodynamic wing section |
| **BL ±26** | ±26.0 m | Wingtip | Lateral extremity, winglet base |

## Buttline Applications

### Structural Buttlines

**Ribs and Frames:**
- Center body ribs: Every 0.6 m (BL 0, ±0.6, ±1.2, ±1.8...)
- Wing ribs: Every 0.6 m outboard of BL ±19
- Designation: "Rib BL ±XX.X"

**Spars:**
- Main wing spar: BL 0 to BL ±26 (continuous)
- Front spar: 25% local chord
- Rear spar: 65% local chord

### System Buttlines

**Fuel Cells:**
- Location: BL ±20 to BL ±25 (in wings)
- Distributed between spars
- Volume: 3.5 m³ per side

**Landing Gear:**
- Nose gear: BL 0 (centerline)
- Main gear: BL ±15.0 (attachment trunnions)
- Track: 30.0 m (main gear spacing)

### Symmetry and Balance

**Left-Right Symmetry:**
- Aircraft designed symmetric about BL 0
- Manufacturing tolerance: ±10 mm side-to-side
- Aerodynamic balance: Critical for roll control

**Lateral CG:**
- Design: BL 0 (centerline)
- Operational tolerance: ±0.1 m (fuel and payload balanced)
- Asymmetric loading: Limited by certification

## Buttline Measurement

### Measurement Procedure

1. **Establish Centerline:**
   - Locate nose apex (STA 0, BL 0, WL 0)
   - Extend longitudinal centerline aft
   - Mark centerline at multiple stations

2. **Measure Laterally:**
   - Perpendicular to centerline (parallel to Y-axis)
   - Right side: Positive buttline values
   - Left side: Negative buttline values

3. **Verification:**
   - Check symmetry at multiple stations
   - Left-right measurements should match within tolerance

### Measurement Tools

**Primary Method:** Laser measurement
- Accuracy: ±2 mm
- Measure from centerline to component
- Parallel to Y-axis (perpendicular to centerline)

**Secondary Method:** String line and ruler
- Accuracy: ±10 mm
- Use: Field measurements and verification
- Reference: Centerline (BL 0)

### Tolerance

**Buttline Location Tolerance:**
- Critical components: ±10 mm
- Non-critical: ±50 mm
- Structural elements: ±5 mm
- Symmetry (left vs right): ±10 mm difference

## Lateral Load Distribution

### Span Loading

**Lift Distribution:**
- Maximum at BL ±8 to ±12 (center body)
- Reduces toward tips (BL ±26)
- Elliptical approximation for efficiency

**Wing Loading:**
- Center body: 82.7 kg/m² (includes non-lifting volume)
- Outer wings: 261.5 kg/m² (pure aerodynamic)

### Lateral CG Control

**Empty Aircraft:**
- Target CG: BL 0 (perfectly centered)
- Typical variation: ±50 mm (manufacturing variation)

**Operational Loading:**
- Fuel symmetric loading: ±0.05 m CG variation
- Passenger seating: Balanced left/right
- Cargo: Balanced left/right
- Maximum lateral CG offset: ±0.2 m (operational limit)

## Interior Layout by Buttline

### Cabin Configuration (at STA 20)

**Seating Layout:**
- BL 0: Center aisle (0.5 m width)
- BL ±1.5 to ±3.5: Center seating section (4 seats, 2-2)
- BL ±4: Side aisle (0.5 m width)
- BL ±5 to ±8: Mid seating section (3 seats, 1-2 or 2-1)
- BL ±9 to ±12: Outer seating section (2 seats, 1-1)
- BL ±13 to ±17: Side cargo/galley/lavatories

### Cockpit Layout

**Crew Positions:**
- Captain: BL -2.0 (left seat)
- First Officer: BL +2.0 (right seat)
- Observer seats: BL -3.5, BL +3.5 (if installed)

## Wing Geometry by Buttline

### Chord Variation

| Buttline | Chord | Description |
|----------|-------|-------------|
| BL 0 | 35.0 m | Root chord (centerline) |
| BL ±10 | 32.0 m | Inner center body |
| BL ±19 | 28.5 m | Center body edge |
| BL ±22 | 12.0 m | Mid wing |
| BL ±24 | 6.0 m | Outer wing |
| BL ±26 | 3.5 m | Wingtip chord |

### Wing Thickness

**Thickness-to-Chord Ratio:**
- BL 0 to ±10: 15% to 13%
- BL ±10 to ±19: 13% to 12%
- BL ±19 to ±24: 12% to 8%
- BL ±24 to ±26: 8% (constant)

## Wing Deflection and Flex

### Static Deflection (Under Load)

**Wingtip Droop (at MTOW):**
- Empty: BL ±26 at reference height
- Loaded: +150 mm droop (tip moves down)
- Resulting in slight dihedral reduction

**Bending Shape:**
- Maximum bending moment: BL ±19 (center body edge)
- Parabolic deflection curve outboard

## Comparison with Conventional

**Conventional Aircraft:**
- Fuselage buttlines (FBL): Center body only
- Wing buttlines (WBL): Separate numbering
- Wing station (WS): Often from centerline outward

**AMPEL360 BWB:**
- Single buttline system for entire aircraft
- Continuous from BL 0 to BL ±26
- No separate fuselage/wing buttline systems

## Documentation

### Drawing Annotation

**On Drawings:**
- Top view: Buttlines shown as lines parallel to centerline
- Labeled: "BL ±XX.X"
- Centerline (BL 0) shown bold

**Dimension Format:**
- "Component at BL +15.0" = 15.0 m right of centerline
- "Between BL +10 and BL +20" = Right side, 10 to 20 m from centerline

### Installation Instructions

**Equipment Installation:**
1. Locate centerline (BL 0)
2. Measure perpendicular distance
3. Mark buttline position
4. Install component
5. Verify symmetry (if applicable)

## Regulatory Compliance

**Standards:**
- SAE AS755: Aircraft coordinate systems
- FAA Part 25 / EASA CS-25: Structural symmetry requirements
- ATA iSpec 2200: Documentation conventions
