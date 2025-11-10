# Center Body Geometry

**Document ID:** AMPEL360-02-11-00-BWB-004  
**Version:** 1.0.0

## Overview

The center body is the core section of the AMPEL360 BWB, integrating fuselage and wing functions into a single lifting structure. It extends from the centerline (BL 0) to BL ±19 on each side and from STA 10 to STA 35 longitudinally.

## Center Body Dimensions

### Overall Dimensions

**Spanwise:**
- Width: 38.0 m (BL -19 to BL +19)
- Half-width: 19.0 m (each side)

**Longitudinal:**
- Length: 28.5 m (STA 10 to STA 35, pressurized section)
- Extended length: 35.0 m (STA 3.2 to STA 38.2, including nose and tail)

**Vertical:**
- Maximum height: 14.5 m (at STA 15, ground to top)
- Internal cabin height: 8.5 m (cabin floor to upper deck floor)
- Cabin ceiling height: 2.4 m (floor to ceiling)

### Key Stations

| Station | Description | Significance |
|---------|-------------|--------------|
| STA 10 | Forward pressure bulkhead | Cabin begins |
| STA 15 | Maximum width location | Widest point |
| STA 20 | Forward H₂ tank center | Fuel storage |
| STA 25 | Wing spar carrythrough | Main structural junction |
| STA 30 | Aft H₂ tank center | Fuel storage |
| STA 35 | Aft pressure bulkhead | Cabin ends |

## Planform Shape

### Leading Edge Profile

**Shape:** Continuous compound curve

**Sweep Distribution:**
- Nose (BL 0): 60° sweep (highly swept)
- Center (BL ±10): 35° sweep
- Edge (BL ±19): 38° sweep

**Radius:**
- Nose leading edge: 2.5 m radius
- Smooth transition to outer wing

### Trailing Edge Profile

**Shape:** Straight section at centerline, transitioning to swept

**Configuration:**
- Center (BL 0 to ±12): 0° sweep (straight)
- Transition (BL ±12 to ±19): -5° forward sweep
- Control surfaces: Elevons along entire trailing edge

### Center Body Chord

**Chord Distribution:**
| Buttline | Chord | Leading Edge | Trailing Edge |
|----------|-------|--------------|---------------|
| BL 0 | 35.0 m | STA 3.2 | STA 38.2 |
| BL ±5 | 34.0 m | STA 3.5 | STA 37.5 |
| BL ±10 | 32.0 m | STA 4.0 | STA 36.0 |
| BL ±15 | 29.5 m | STA 4.5 | STA 34.0 |
| BL ±19 | 28.5 m | STA 4.5 | STA 33.0 |

## Internal Configuration

### Deck Layout

**Lower Level (WL 1.8 to WL 4.0):**
- Cargo compartments
- Forward cargo: 60 m³
- Aft cargo: 90 m³
- Total cargo volume: 150 m³

**Main Deck (WL 4.0 to WL 8.5):**
- Passenger cabin: 1,200 m³
- Seating configuration: 220 passengers (2-3-2, 2-4-2 layouts)
- Cabin width: 36.0 m (usable, varies by station)
- Cabin length: 25.0 m (STA 10 to STA 35)

**Upper Deck (WL 8.5 to WL 12.5):**
- Systems bay: 300 m³
- Avionics: 100 m³
- H₂ fuel tanks: 350 m³ (two tanks)
- Environmental systems: 100 m³

### Cross-Section at STA 15 (Maximum Width)

**External Dimensions:**
- Width: 38.0 m
- Height (ground to top): 14.5 m
- Chord: 35.0 m
- Thickness-to-chord ratio: 15%

**Internal Layout:**
```
WL 14.5 -------- Top of fuselage --------
WL 12.5 -------- H₂ tank top -------------
WL 10.0 -------- Upper deck floor ---------
WL 8.5  -------- Cabin ceiling -----------
         |   Passenger Cabin  |
WL 4.0  -------- Cabin floor -------------
WL 2.2  -------- Cargo bay floor ----------
WL 1.8  -------- Belly structure ----------
WL 0    -------- Ground level -------------
```

**Cabin Width Distribution (at floor level, WL 4.0):**
- At centerline (BL 0): 36.0 m usable width
- Seating: 2 aisles, 7-abreast center, 2-abreast sides
- Total seats across: 11 seats

## Structural Configuration

### Main Structural Elements

**Frames:**
- Spacing: 0.5 m (closely spaced for pressure loads)
- Type: Composite hat-stiffened frames
- Depth: 250 mm average
- Material: CFRP

**Longerons/Stringers:**
- Spacing: 0.2 m (upper/lower surfaces)
- Type: Blade-stiffened
- Material: CFRP
- Function: Carry axial loads, stabilize skin

**Floor Beams:**
- Spacing: 0.6 m (passenger cabin floor)
- Type: I-beam sections
- Material: Aluminum 2024-T3
- Depth: 200 mm

**Wing Spar Carrythrough:**
- Location: STA 22 to STA 28
- Type: Box beam
- Depth: 1.2 m
- Continuous across centerline
- Carries main wing bending loads

### Pressure Cabin

**Design Pressure:**
- Maximum differential: 9.1 psi (62.7 kPa)
- Cruise altitude: 41,000 ft
- Cabin altitude: 6,000 ft

**Pressure Bulkheads:**
- Forward: STA 10 (cockpit aft bulkhead)
- Aft: STA 35 (aft cabin bulkhead)
- Type: Aluminum reinforced composite
- Thickness: 15 mm

**Pressure Vessel Shape:**
- Type: Modified oval (efficient for BWB)
- Hoop stress: Managed by frames
- Longitudinal stress: Managed by stringers

### H₂ Tank Installation

**Forward Tank:**
- Location: STA 18 to STA 22 (above cabin ceiling)
- Volume: 175 m³
- Diameter: 2.0 m
- Length: 4.0 m
- Insulation: Vacuum-insulated composite

**Aft Tank:**
- Location: STA 28 to STA 32 (above cabin ceiling)
- Volume: 175 m³
- Configuration: Same as forward tank

**Tank Support:**
- Mounting: Suspended from upper structure
- Load path: Through frames to wing structure
- Thermal isolation: Low-conductivity mounts

## Volume Distribution

### Usable Volume by Function

| Function | Volume | % of Total | Location |
|----------|--------|------------|----------|
| Passenger cabin | 1,200 m³ | 46.2% | Main deck |
| Cargo bay | 150 m³ | 5.8% | Lower deck |
| H₂ fuel tanks | 350 m³ | 13.5% | Upper deck |
| Systems bay | 300 m³ | 11.5% | Upper deck |
| Avionics | 100 m³ | 3.8% | Nose, upper |
| Structure/unusable | 500 m³ | 19.2% | Throughout |
| **Total** | **2,600 m³** | **100%** | — |

### Volume Efficiency

**Comparison with Conventional:**
- AMPEL360: 2.2 m³ per m² planform
- Conventional wide-body: 0.8 m³ per m² planform
- Advantage: +175% volume efficiency

## Aerodynamic Contribution

### Lift Generation

**Center Body Lift:**
- At cruise: 60% of total aircraft lift
- Lift coefficient: CL = 0.45 (center body alone)
- Lifting area: 520 m² (center body planform)

**Comparison:**
- Conventional fuselage: 0% lift (drag producer)
- AMPEL360 center body: Significant lift contributor

### Drag Characteristics

**Pressure Drag:**
- Reduced due to blended shape
- No fuselage-wing interference drag
- Smooth pressure recovery

**Skin Friction Drag:**
- Large wetted area offset by:
  - Natural laminar flow potential
  - Smooth surface finish
  - Optimized thickness distribution

## Manufacturing Considerations

### Assembly Sections

**Section Build:**
1. Nose section: STA 0 to STA 10
2. Forward center body: STA 10 to STA 20
3. Mid center body: STA 20 to STA 30
4. Aft center body: STA 30 to STA 38.2

**Major Assembly Joints:**
- STA 10: Forward pressure bulkhead
- STA 20: Forward H₂ tank section
- STA 30: Aft H₂ tank section
- STA 35: Aft pressure bulkhead

### Join to Outer Wings

**Joint Location:** BL ±19

**Joint Type:**
- Bolted mechanical joint
- Composite splice doublers
- Load transfer through main spars

**Loads Transferred:**
- Wing bending moment: 15,000 kN·m per side
- Shear: 2,500 kN
- Torsion: 5,000 kN·m

## Weight Distribution

**Center Body Structural Weight:**
- Structure: 8,500 kg
- Systems: 4,200 kg
- Interior: 3,800 kg
- Total: 16,500 kg

**Weight per Unit Area:**
- 31.7 kg/m² (structure only, per planform area)
- Comparison to conventional: 25% lighter

## Comparison with Conventional

| Parameter | AMPEL360 Center Body | Conventional Fuselage | Difference |
|-----------|----------------------|-----------------------|------------|
| Width | 38.0 m | 5.6 m (A320) | +580% |
| Lift contribution | 60% | 0% | Infinite |
| Volume | 2,600 m³ | 400 m³ | +550% |
| Passengers | 220 | 180 | +22% |
| Structural efficiency | 31.7 kg/m² | 42 kg/m² | +24% |
