# Cross-Section Geometry

**Document ID:** AMPEL360-02-11-00-BWB-002  
**Version:** 1.0.0

## Overview

The AMPEL360 cross-section geometry defines the airfoil shapes and internal volume distribution across the span and length of the blended wing body.

## Key Cross-Sections

### Center Body (Station 15.0m, BL 0)

**External Dimensions:**
- Chord: 35.0 m
- Maximum thickness: 5.25 m (15% t/c ratio)
- Width: 38.0 m
- Leading edge radius: 2.5 m

**Internal Configuration:**
- Cabin height: 2.4 m (floor to ceiling)
- Cabin width: 36.0 m (usable)
- Upper deck (H₂): 2.5 m height
- Floor structure: 0.4 m depth

**Structural Elements:**
- Upper skin: 25 mm composite
- Lower skin: 30 mm composite (landing gear loads)
- Pressure bulkheads: 15 mm aluminum
- Floor beams: 200 mm I-beams at 0.6 m spacing

### Mid-Wing Section (Station 30.0m, BL ±12)

**External Dimensions:**
- Chord: 20.0 m
- Maximum thickness: 2.4 m (12% t/c ratio)
- Thickness location: 40% chord

**Internal Configuration:**
- Passenger cabin: Continues into wing
- Cabin width: 8.0 m at this station
- Cabin height: 2.1 m
- Systems bay: 0.8 m above cabin

**Transition Characteristics:**
- Smooth blend from center body
- Airfoil shape emerges
- Load-bearing skin structure
- Fuel cell integration space

### Outer Wing (Station 25.0m, BL ±24)

**External Dimensions:**
- Chord: 6.0 m
- Maximum thickness: 0.48 m (8% t/c ratio)
- Thickness location: 35% chord

**Internal Configuration:**
- Pure aerodynamic surface
- Fuel cell stacks: 0.3 m height
- Structural depth: 0.48 m total
- Control surface mechanisms

**Aerodynamic Features:**
- Laminar flow airfoil
- Low drag characteristics
- Ailerons/elevons integration
- Ice protection leading edge

## Airfoil Sections

### Center Body Airfoil

**Type:** Modified NASA SC(2)-0714 (BWB variant)

**Characteristics:**
- Thickness: 15% chord
- Camber: 3.5% (lifting body)
- Leading edge radius: Large (2.5 m)
- Trailing edge angle: 12°

**Performance:**
- Cl,max: 1.8 (clean)
- Cl,cruise: 0.45
- Cd,min: 0.0045
- L/D contribution: High due to large area

### Transition Airfoil (BL ±15)

**Type:** Custom BWB transition section

**Characteristics:**
- Thickness: 12% chord
- Camber: 2.5%
- Smooth shape blending
- Reduced leading edge radius

**Performance:**
- Cl,max: 1.6
- Cl,cruise: 0.50
- Cd,min: 0.0040
- Transition efficiency: 95%

### Outer Wing Airfoil

**Type:** Modified NACA 64-series (low drag)

**Characteristics:**
- Thickness: 8% chord
- Camber: 1.5%
- Natural laminar flow: 40% chord
- Sharp trailing edge

**Performance:**
- Cl,max: 1.4
- Cl,cruise: 0.55
- Cd,min: 0.0035
- Laminar flow maintained to M0.82

## Volume Distribution

### Pressurized Volume

**Total:** 1,850 m³

**Distribution by Station:**
| Station | Volume | Use |
|---------|--------|-----|
| STA 5-15 | 600 m³ | Cockpit, forward cabin |
| STA 15-25 | 800 m³ | Main cabin, center body |
| STA 25-35 | 450 m³ | Aft cabin, cargo |

**Distribution by Level:**
| Level | Volume | Use |
|-------|--------|-----|
| Lower (WL 2-4) | 150 m³ | Cargo bay |
| Main (WL 4-8.5) | 1,200 m³ | Passenger cabin |
| Upper (WL 8.5-12.5) | 500 m³ | Systems, avionics |

### Unpressurized Volume

**Total:** 800 m³

**H₂ Fuel Tanks:**
- Forward tank: 175 m³ (STA 18-22)
- Aft tank: 175 m³ (STA 28-32)
- Total H₂ volume: 350 m³

**Other Volumes:**
- Landing gear bays: 150 m³
- Wing systems: 200 m³
- Aerodynamic fairings: 100 m³

## Structural Cross-Sections

### Load-Bearing Structure

**Wing Box:**
- Front spar: 25% chord
- Rear spar: 65% chord
- Rib spacing: 0.6 m typical
- Skin thickness: 15-35 mm composite

**Center Body Frame:**
- Frame spacing: 0.5 m
- Frame depth: 200-300 mm
- Composite hat-stiffened construction
- Pressure-resistant design

### Material Distribution

**Upper Surface:**
- Skin: CFRP (carbon fiber reinforced polymer)
- Stringers: CFRP, blade-stiffened
- Spars: CFRP, I-beam section

**Lower Surface:**
- Skin: CFRP with metal doublers (landing gear)
- Stringers: CFRP, hat-stiffened
- Floor beams: Aluminum I-beams

## Aerodynamic Considerations

### Pressure Distribution

**Cruise Condition (M0.82, 35,000 ft):**
- Center body: Positive pressure (lifting)
- Upper surface: Favorable pressure gradient (laminar flow)
- Lower surface: Mild adverse gradient (turbulent)

**Maximum Loading:**
- Peak Cp: -1.2 (upper surface at 15% chord)
- Minimum Cp: +0.3 (lower surface at 60% chord)

### Flow Characteristics

**Laminar Flow:**
- Extent: 40% chord on outer wing
- Reynolds number: 25 million (cruise)
- Transition location: Controlled by design

**Boundary Layer:**
- Thickness at TE: 50 mm (turbulent)
- Displacement thickness: 15 mm
- Separation: None in cruise

## Cross-Section Variations

### Spanwise Variation

The cross-section shape varies smoothly from centerline to wingtip:

**BL 0 to BL ±10:** Thick lifting body (15% to 13% t/c)  
**BL ±10 to BL ±20:** Transition to wing (13% to 10% t/c)  
**BL ±20 to BL ±26:** Aerodynamic wing (10% to 8% t/c)

### Longitudinal Variation

The cross-section also varies along the length:

**Forward (STA 0-10):** Blunt nose, cockpit shape  
**Mid (STA 10-30):** Maximum volume, constant section  
**Aft (STA 30-38):** Tapering, reduced thickness

## Manufacturing Implications

### Panel Assembly

**Section Build-Up:**
1. Lower skin panel with stringers
2. Spar assembly
3. Rib installation
4. Upper skin panel attachment
5. System integration

**Tooling:**
- Large mandrel tools for skin panels
- Precision jigs for spar alignment
- Assembly fixtures for section join

### Quality Control

**Dimensional Tolerance:**
- Skin contour: ±5 mm
- Spar position: ±3 mm
- Cross-section area: ±2%

**Inspection Methods:**
- Laser scanning for surface verification
- CMM for critical features
- Ultrasonic for bond quality

## Comparison with Conventional

| Feature | AMPEL360 BWB | Conventional | Advantage |
|---------|--------------|--------------|-----------|
| Volume efficiency | 2.2 m³/m² | 0.8 m³/m² | +175% |
| Structural efficiency | 0.18 kg/m³ | 0.25 kg/m³ | +28% |
| Wetted area ratio | 2.2 | 3.8 | +42% |
| Pressure vessel | Efficient oval | Circular tube | Better |
