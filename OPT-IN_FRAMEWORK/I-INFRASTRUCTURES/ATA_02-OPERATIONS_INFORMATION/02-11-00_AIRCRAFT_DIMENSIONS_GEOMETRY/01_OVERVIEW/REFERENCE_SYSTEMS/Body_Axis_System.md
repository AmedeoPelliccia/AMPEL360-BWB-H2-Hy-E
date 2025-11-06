# Body Axis System

**Document ID:** AMPEL360-02-11-00-REF-001  
**Version:** 1.0.0

## Overview

The body axis system is the primary coordinate system for the AMPEL360 BWB H₂ aircraft, defining the reference frame for all measurements, analyses, and operations.

## Coordinate System Definition

### Axes Orientation

**X-Axis (Longitudinal):**
- Direction: Positive forward (toward nose)
- Origin: Nose apex
- Use: Stations, longitudinal positions

**Y-Axis (Lateral):**
- Direction: Positive to the right (starboard)
- Origin: Aircraft centerline
- Use: Buttlines, spanwise positions

**Z-Axis (Vertical):**
- Direction: Positive downward (toward ground)
- Origin: Ground datum at nose apex
- Use: Waterlines, vertical positions

### Handedness

**Right-Hand Rule:**
- Thumb: +X (forward)
- Index finger: +Y (right)
- Middle finger: +Z (down)
- System: Right-handed orthogonal

## Origin Definition

**Primary Datum Point:**
- Location: Nose apex (forward-most point)
- Coordinates: (0, 0, 0)
- Ground reference: At ground level when aircraft on landing gear

**Why Nose Apex:**
- Fixed structural point
- Easily identifiable
- Does not change with loading
- Logical reference for forward/aft measurements

## Axis Applications

### X-Axis (Stations)

**Primary Use:** Longitudinal position measurement

**Key Positions:**
- STA 0: Nose apex (datum)
- STA 15: Maximum width
- STA 25: Wing center
- STA 38.2: Aft extremity

**Applications:**
- Component location
- Center of gravity calculation
- Load distribution
- Structural analysis

### Y-Axis (Buttlines)

**Primary Use:** Lateral position measurement

**Key Positions:**
- BL 0: Centerline
- BL ±19: Center body edge
- BL ±26: Wingtip

**Applications:**
- Symmetry verification
- Span loading
- Lateral CG
- Wing deflection measurement

### Z-Axis (Waterlines)

**Primary Use:** Vertical position measurement

**Key Positions:**
- WL 0: Ground datum
- WL 4.0: Cabin floor
- WL 14.5: Top of aircraft

**Applications:**
- Height measurements
- Vertical CG
- Load heights
- Clearance verification

## Transformations

### Flight Mechanics Axes

**Conversion to Stability Axes:**
- Origin: Center of gravity (not nose)
- X: Along velocity vector
- Y: Same as body axis
- Z: Perpendicular to X in vertical plane

**Transformation:**
- Translation: (Xcg, 0, Zcg) from nose
- Rotation: Angle of attack (α) about Y-axis

### Wind Axes

**Conversion:**
- Origin: Center of gravity
- X: Along relative wind
- Y: Same as body axis (no sideslip assumption)
- Z: Perpendicular to X

**Transformation:**
- Translation: To CG
- Rotation: α (angle of attack), β (sideslip angle)

## Measurement Conventions

### Sign Conventions

**Positive Directions:**
- Forward: +X
- Right wing: +Y
- Down: +Z

**Angular Rotations (Right-hand rule):**
- Roll (φ): About +X axis, right wing down is positive
- Pitch (θ): About +Y axis, nose up is positive
- Yaw (ψ): About +Z axis, nose right is positive

### Distance Measurements

**Absolute Coordinates:**
- Always measured from datum (0,0,0)
- Example: STA 15 means X = 15.0 m from nose apex

**Relative Measurements:**
- Stated explicitly as "relative to" or "from"
- Example: "5.0 m aft of STA 10" = STA 15

## Usage in Different Disciplines

### Structural Analysis

**Primary System:** Body axes

**Applications:**
- Load paths
- Stress analysis
- Deflection measurement
- Failure analysis

### Aerodynamics

**Systems Used:**
- Body axes for geometry
- Stability axes for coefficients
- Wind axes for flight mechanics

**Conversions:** Through angle of attack and sideslip

### Weight and Balance

**Primary System:** Body axes

**Critical Points:**
- Empty weight CG: Measured in body axes
- Loaded CG: Must remain in limits (% MAC)
- Datum: Nose apex (STA 0)

### Systems Integration

**Primary System:** Body axes

**Applications:**
- Component installation locations
- Wiring runs
- Hydraulic lines
- All measured in body axes

## Reference Conditions

### Aircraft Attitude

**Standard Measurement Attitude:**
- Aircraft level (pitch = 0°, roll = 0°)
- Landing gear extended and compressed to static load
- Empty weight condition

**Datum Plane:**
- Horizontal plane through datum point
- Aircraft sitting on gear, level attitude

### Tolerances

**Leveling Accuracy:**
- Pitch: ±0.3°
- Roll: ±0.3°
- Yaw: ±0.5° (relative to ground reference)

**Measurement Accuracy:**
- X-axis: ±10 mm (stations)
- Y-axis: ±10 mm (buttlines)
- Z-axis: ±5 mm (waterlines)

## Documentation Standards

### Coordinate Notation

**Format:** (X, Y, Z) or (STA, BL, WL)

**Examples:**
- (15.0, 0, 6.0) = STA 15, BL 0, WL 6.0
- (25.0, +10.0, 4.0) = STA 25, BL +10 (right), WL 4.0

### Drawing Conventions

**Views:**
- Top view: Looking down (-Z direction)
- Side view: Looking from right (-Y direction)
- Front view: Looking aft (-X direction)

**Dimensions:**
- Always referenced to body axes
- Stated as STA, BL, or WL values
- Relative dimensions clearly marked

## Comparison with Conventional

**Similarities:**
- X forward, Y right, Z down (same as most aircraft)
- Right-hand coordinate system
- Nose as forward datum

**BWB-Specific Considerations:**
- No distinct fuselage/wing break
- Center body spans large Y-range
- Datum at nose apex (not fuselage station 0 which may differ)

## Regulatory Compliance

**Standards:**
- ISO 1151: Flight dynamics coordinate systems
- SAE AS755: Aircraft coordinate systems
- MIL-STD-8591: Aircraft axis system

**Certification:**
- EASA CS-25: Referenced in structural analysis
- FAA Part 25: Referenced in documentation
