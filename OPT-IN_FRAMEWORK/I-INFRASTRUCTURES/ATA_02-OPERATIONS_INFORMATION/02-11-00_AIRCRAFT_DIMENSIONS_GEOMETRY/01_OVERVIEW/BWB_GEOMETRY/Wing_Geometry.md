# Wing Geometry

**Document ID:** AMPEL360-02-11-00-BWB-003  
**Version:** 1.0.0

## Wing Definition

In the AMPEL360 BWB configuration, the "wing" is not a distinct component but rather the outer portion of the integrated lifting surface. For operational purposes, the wing is defined as the region outboard of the center body (BL ±19 and beyond).

## Wing Sections

### Inner Wing (BL ±19 to BL ±22)

**Geometric Parameters:**
- Span (per side): 3.0 m
- Root chord (at BL ±19): 28.5 m
- Tip chord (at BL ±22): 12.0 m
- Taper ratio: 0.42
- Sweep (LE): 38°
- Dihedral: 2°

**Internal Structure:**
- Transition from cabin to pure wing structure
- Last passenger seats at BL ±20
- Fuel cell integration begins
- Main landing gear bay at BL ±18

**Functions:**
- Lift generation
- Structural transition
- Passenger accommodation (inner portion)
- Systems integration

### Mid Wing (BL ±22 to BL ±24)

**Geometric Parameters:**
- Span (per side): 2.0 m
- Root chord (at BL ±22): 12.0 m
- Tip chord (at BL ±24): 6.0 m
- Taper ratio: 0.50
- Sweep (LE): 40°
- Dihedral: 3°

**Internal Structure:**
- Pure aerodynamic section
- Wing box structural depth: 0.7 m
- Fuel cell stacks
- Flight control actuators

**Functions:**
- Primary lift generation
- Structural load carrying
- Fuel cell storage
- Control surface support

### Outer Wing (BL ±24 to BL ±26)

**Geometric Parameters:**
- Span (per side): 2.0 m
- Root chord (at BL ±24): 6.0 m
- Tip chord (at BL ±26): 3.5 m
- Taper ratio: 0.58
- Sweep (LE): 42°
- Dihedral: 4°

**Internal Structure:**
- Thin aerodynamic section
- Wing box depth: 0.4 m
- Minimal internal volume
- Winglet attachment structure

**Functions:**
- Lift distribution optimization
- Induced drag reduction
- Structural termination
- Winglet support

## Wing Planform Parameters

### Overall Wing (BL ±19 to ±26)

**Dimensions:**
- Semi-span: 7.0 m (each side)
- Total span: 14.0 m (both wings combined)
- Wing area: 325 m² (outer wings only, excludes center body)
- Aspect ratio (wing only): 0.60 (low due to integration)

**Sweep:**
- Leading edge: 38° average
- Trailing edge: -8° (forward sweep)
- Quarter chord: 32°

### Wing Loading

**At MTOW (85,000 kg):**
- Total wing loading: 100.6 kg/m² (845 m² total planform)
- Outer wing loading: 261.5 kg/m² (325 m² wing area only)
- Center body loading: 82.7 kg/m² (520 m² center body)

Note: Lower center body loading due to lift distribution across entire BWB.

## Airfoil Distribution

### Spanwise Airfoil Variation

| Buttline | Airfoil Type | t/c | Camber | Purpose |
|----------|--------------|-----|--------|---------|
| BL ±19 | Transition BWB | 12% | 2.5% | Blend to wing |
| BL ±20 | Modified SC(2) | 11% | 2.2% | High lift |
| BL ±22 | BWB Wing | 10% | 2.0% | Cruise efficiency |
| BL ±24 | Low drag | 8% | 1.5% | Laminar flow |
| BL ±26 | Tip section | 8% | 1.2% | Tip efficiency |

### Twist Distribution

**Geometric Twist (Washout):**
- Root (BL ±19): 0° (reference)
- Mid (BL ±22): -1°
- Outer (BL ±24): -2°
- Tip (BL ±26): -3°

**Purpose:**
- Prevent tip stall
- Optimize span loading
- Improve stall characteristics
- Reduce induced drag

## Wing Structure

### Main Structural Elements

**Spars:**
- Front spar: 25% local chord
- Rear spar: 65% local chord
- Carry-through: Continuous across BL 0
- Material: CFRP composite

**Ribs:**
- Spacing: 0.6 m typical
- Type: CFRP plate ribs with lightening holes
- Function: Maintain airfoil shape, transfer loads

**Skin:**
- Upper skin: 15-25 mm CFRP
- Lower skin: 20-30 mm CFRP
- Stiffeners: Blade type, 0.15 m spacing

### Wing Box Design

**Wing Box Dimensions (at BL ±22):**
- Chord: 12.0 m
- Structural depth: 0.7 m (at spar)
- Box chord: 4.8 m (40% local chord)
- Enclosed area: 3.36 m²

**Structural Capability:**
- Ultimate bending moment: 15,000 kN·m (per side)
- Shear load: 2,500 kN
- Torsion: 5,000 kN·m
- Safety factor: 1.5 (ultimate load)

## Control Surfaces

### Elevons (Outboard)

**Configuration:**
- 4 segments per wing (8 total)
- Span per segment: 1.75 m
- Chord: 2.8 m (average)
- Area per segment: 4.9 m²
- Total elevon area: 39.2 m²

**Deflection:**
- Up: +25°
- Down: -15°
- Differential: ±15° (roll control)

**Actuation:**
- Type: Electro-hydraulic
- Redundancy: Dual actuators per segment
- Rate: 30°/second

### Trailing Edge Flaps

**High-Lift System:**
- Type: Plain flaps (no slats on BWB)
- Span: BL ±19 to BL ±24
- Deflection: 0° to 30°
- Area: 58 m²

**Performance:**
- ΔCL,max: +0.8 (30° flaps)
- Takeoff setting: 15°
- Landing setting: 30°

## Wing Fuel Cells

### Fuel Cell Integration

**Location:**
- Primary zone: BL ±20 to BL ±25
- Between front and rear spars
- Above lower skin, below upper skin

**Capacity:**
- Volume per wing: 3.5 m³
- Total wing fuel cells: 7.0 m³ (both wings)
- Weight: 350 kg per wing (empty)

**System:**
- Type: PEM fuel cell stacks
- Power output: 500 kW per wing
- Cooling: Integrated heat exchangers

## Wing Performance

### Aerodynamic Characteristics

**Lift Coefficient:**
- Cruise (clean): CL = 0.50
- Maximum (30° flaps): CL,max = 1.8
- Stall (clean): CL,stall = 1.4

**Drag Characteristics:**
- Minimum drag: CD,min = 0.0180 (total aircraft)
- Wing contribution: 45% of total drag
- Induced drag factor: k = 0.035

### Structural Characteristics

**Wing Weight:**
- Outer wing structure (both): 2,800 kg
- Weight per area: 8.6 kg/m² (wing area only)
- Comparison to conventional: 30% lighter

**Load Distribution:**
- Root bending moment: 40% lower than conventional
- Distributed load: More uniform
- Stress concentrations: Reduced

## Wing Deflection

### Under Load Conditions

**Static Deflection (at MTOW):**
- Wingtip (BL ±26): +150 mm up (droop when loaded)
- Mid-wing (BL ±22): +80 mm
- Deflection shape: Parabolic

**Dynamic Deflection (Gust):**
- Maximum gust (50 ft/s): +250 mm
- Frequency: 2.5 Hz (first bending mode)
- Damping: 2% critical

## Manufacturing

### Wing Assembly

**Build Sequence:**
1. Spar assembly
2. Rib installation
3. Lower skin bonding
4. System integration
5. Upper skin closure
6. Control surface attachment

**Join to Center Body:**
- Location: BL ±19
- Method: Bolted joint with composite doublers
- Load transfer: Through main spars

### Quality Requirements

**Tolerances:**
- Wing twist: ±0.3°
- Skin contour: ±5 mm
- Spar alignment: ±2 mm
- Rib spacing: ±3 mm

## Comparison

| Parameter | AMPEL360 Wing | Conventional | Notes |
|-----------|---------------|--------------|-------|
| Span (outboard) | 14.0 m | 35.8 m | BWB has center body |
| Wing area | 325 m² | 122.6 m² | More area due to integration |
| Aspect ratio | 0.6 | 9.5 | Low due to BWB design |
| Root bending moment | 15,000 kN·m | 25,000 kN·m | 40% reduction |
| Weight efficiency | 8.6 kg/m² | 12.5 kg/m² | 31% better |
