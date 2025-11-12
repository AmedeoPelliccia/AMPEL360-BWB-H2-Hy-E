# Waterline System (Z-Axis)

**Document ID:** AMPEL360-02-11-00-REF-003  
**Version:** 1.0.0

## Overview

The waterline system defines vertical positions on the AMPEL360 BWB H₂ aircraft, measured along the Z-axis (positive downward) from a ground datum reference.

## Waterline Definition

**Waterline (WL):** Vertical distance in meters from the ground datum, measured upward (opposite to positive Z direction).

**Notation:** "WL X.X" where X.X is the height in meters above ground

**Example:** WL 4.0 = 4.0 meters above ground datum

## Primary Waterlines

### Ground Level Waterlines (WL 0 - 4.0)

| Waterline | Height | Description | Significance |
|-----------|--------|-------------|--------------|
| **WL 0** | 0.0 m | Ground datum | Reference plane, aircraft on gear |
| **WL 1.8** | 1.8 m | Belly structure | Lowest structural point |
| **WL 2.0** | 2.0 m | Nose gear strut | NLG attachment |
| **WL 2.2** | 2.2 m | Cargo floor | Lower deck floor |
| **WL 2.5** | 2.5 m | H₂ ground connection | Refueling point height |
| **WL 4.0** | 4.0 m | Cabin floor | Passenger deck floor level |

### Cabin Level Waterlines (WL 4.0 - 8.5)

| Waterline | Height | Description | Significance |
|-----------|--------|-------------|--------------|
| **WL 4.3** | 4.3 m | Door sill | Passenger door threshold |
| **WL 6.0** | 6.0 m | Seat cushion | Passenger seated eye level |
| **WL 6.5** | 6.5 m | Empty aircraft CG | Typical empty CG height |
| **WL 7.5** | 7.5 m | Overhead bins | Luggage storage |
| **WL 8.5** | 8.5 m | Cabin ceiling | Upper cabin boundary |

### Upper Structure Waterlines (WL 8.5 - 14.5)

| Waterline | Height | Description | Significance |
|-----------|--------|-------------|--------------|
| **WL 10.0** | 10.0 m | Upper deck floor | H₂ tank deck level |
| **WL 11.0** | 11.0 m | H₂ tank bottom | Tank lower surface |
| **WL 12.5** | 12.5 m | H₂ tank top | Tank upper surface |
| **WL 14.0** | 14.0 m | Upper surface | Top skin outer mold line |
| **WL 14.5** | 14.5 m | Highest point | Top of fuselage at STA 15 |

## Waterline Applications

### Structural Waterlines

**Frame Heights:**
- Floor frames: WL 2.2, WL 4.0, WL 8.5
- Intermediate frames: Every 0.5 m vertical
- Designation: "WL XX.X frame"

**Pressure Vessel:**
- Lower boundary: WL 2.2 (cargo floor)
- Upper boundary: WL 10.0 (upper deck)
- Pressure differential: 9.1 psi (62.7 kPa)

### Equipment Waterlines

**Major Systems Heights:**
- Landing gear retracted: WL 2.0 to WL 4.0
- Environmental systems: WL 8.5 to WL 10.0
- H₂ tanks: WL 10.0 to WL 12.5
- Avionics: WL 5.0 to WL 7.0 (distributed)

### Clearance Waterlines

**Ground Clearances:**
| Location | Station | Waterline | Clearance |
|----------|---------|-----------|-----------|
| Nose (lowest) | STA 3 | WL 2.1 | 2.1 m |
| Belly (minimum) | STA 18 | WL 1.8 | 1.8 m |
| Tail (aft body) | STA 36 | WL 2.5 | 2.5 m |
| Engine intake | BL ±12 | WL 2.8 | 2.8 m |

## Waterline Measurement

### Measurement Procedure

1. **Establish Ground Datum:**
   - Aircraft on landing gear, gear compressed to static load
   - Level surface verified
   - WL 0 defined at ground surface

2. **Level Aircraft:**
   - Pitch: 0° ± 0.3°
   - Roll: 0° ± 0.3°
   - Use aircraft leveling points

3. **Measure Vertically:**
   - Laser or plumb bob from ground datum
   - Perpendicular to ground plane
   - Record height of component

### Measurement Tools

**Primary Method:** Laser level or theodolite
- Accuracy: ±2 mm vertical
- Range: 0 to 20 m
- Self-leveling capability

**Secondary Method:** Ruler and level
- Accuracy: ±5 mm
- Use: Field verification
- Reference: Always from WL 0

### Tolerance

**Waterline Location Tolerance:**
- Critical components: ±5 mm
- Non-critical: ±20 mm
- Floor/deck levels: ±3 mm

## CG Vertical Position

### Vertical CG Calculation

**Empty Aircraft CG:**
- Typical: WL 6.5 m
- Range: WL 6.0 to WL 7.0 (depending on configuration)

**Loaded Aircraft CG:**
- With passengers: WL 6.2 m (lower, passengers below empty CG)
- With full H₂: WL 7.8 m (higher, tanks above empty CG)

**Vertical Stability:**
- CG below center of lift (aerodynamic center) = stable
- Typical separation: 1.0 m (CG at WL 6.5, AC at WL 7.5)

### Vertical CG Limits

**No specific vertical CG limits** for conventional longitudinal stability, but:
- Affects ground handling (rollover threshold)
- Influences lateral stability
- Considered in crosswind landing certification

## Interior Heights

### Cabin Interior

**Main Cabin (STA 10 to 35):**
- Floor: WL 4.0
- Ceiling: WL 8.5
- Interior height: 2.4 m (centerline)
- Aisle height: 2.1 m minimum

**Cockpit (STA 5 to 10):**
- Floor: WL 4.0
- Ceiling: WL 7.0
- Interior height: 3.0 m (for visibility)

### Cargo Compartment

**Lower Cargo Bay:**
- Floor: WL 2.2
- Ceiling: WL 4.0
- Interior height: 1.8 m (accommodates LD3-45 containers at 1.63 m)

### Upper Deck

**Systems/H₂ Tanks:**
- Floor: WL 8.5
- Ceiling: WL 10.0 (structure)
- H₂ tanks: WL 11.0 to WL 12.5
- Access height: 1.5 m (below tanks)

## Ground Service Heights

### Door Sill Heights

**Passenger Doors:**
- Door sill: WL 4.3 m
- Standard passenger stairs: 3.5 to 6.0 m range
- Compatible: Yes, within range

**Cargo Doors:**
- Cargo door sill: WL 2.2 m
- Standard wide-body loaders: 2.0 to 3.0 m
- Compatible: Yes

### Service Points

**Ground Service Equipment:**
- H₂ refueling: WL 2.5 m (ground-level access)
- External power: WL 2.0 m
- Potable water: WL 2.5 m
- Waste drain: WL 1.8 m

## Aerodynamic Reference

### Aerodynamic Center Height

**Center of Lift (Approximate):**
- Vertical location: WL 7.5 m (at typical cruise)
- Varies with angle of attack
- Used for moment calculations

**Neutral Point:**
- Vertical position not relevant for conventional stability
- But important for BWB pitch control authority

## Comparison with Conventional

**Similarities:**
- Waterline system measured from ground
- Cabin floor as key reference
- Compatible with ground equipment

**BWB-Specific:**
- Large vertical span (14.5 m vs 11.8 m typical)
- Multiple functional levels (cargo, cabin, upper deck, H₂)
- CG height lower relative to overall height (better stability)

## Documentation

### Drawing Annotation

**On Drawings:**
- Waterline shown as horizontal lines
- Labeled: "WL XX.X"
- Side view shows WL distribution

**Dimension Format:**
- "Component at WL 6.5" = Height of 6.5 m above ground
- "Between WL 4.0 and WL 8.5" = Cabin height region

## Regulatory Compliance

**Standards:**
- FAA Part 25: Ground clearance requirements
- EASA CS-25: Emergency egress height limits
- ICAO Annex 14: Ground servicing compatibility
- SAE AS755: Aircraft coordinate systems
