# Station System (X-Axis)

**Document ID:** AMPEL360-02-11-00-REF-002  
**Version:** 1.0.0

## Overview

The station system defines longitudinal positions along the AMPEL360 BWB H₂ aircraft from nose to tail, measured along the X-axis of the body axis system.

## Station Definition

**Station (STA):** Distance in meters along the X-axis from the nose apex datum point.

**Notation:** "STA X.X" where X.X is the distance in meters

**Example:** STA 15.0 = 15.0 meters aft of nose apex

## Primary Stations

### Forward Stations (STA 0 - 10)

| Station | Location | Description | Significance |
|---------|----------|-------------|--------------|
| **STA 0** | 0.0 m | Nose apex | Datum point, forward extremity |
| **STA 2.5** | 2.5 m | Nose landing gear | NLG centerline, tow point |
| **STA 3.2** | 3.2 m | Leading edge root | Root chord leading edge |
| **STA 5** | 5.0 m | Cockpit forward bulkhead | Pressurization begins |
| **STA 8** | 8.0 m | Windshield center | Pilot eye position |
| **STA 10** | 10.0 m | Cockpit aft bulkhead | Cabin begins |

### Center Body Stations (STA 10 - 30)

| Station | Location | Description | Significance |
|---------|----------|-------------|--------------|
| **STA 12** | 12.0 m | Forward passenger door | L1 door location |
| **STA 15** | 15.0 m | Maximum width | Center body widest point |
| **STA 18** | 18.0 m | Main landing gear | MLG centerline |
| **STA 20** | 20.0 m | Forward H₂ tank center | Forward fuel tank |
| **STA 22** | 22.0 m | Front wing spar | Wing structural junction |
| **STA 25** | 25.0 m | Wing center | Spar carrythrough |
| **STA 28** | 28.0 m | Rear wing spar | Aft structural junction |
| **STA 30** | 30.0 m | Aft H₂ tank center | Aft fuel tank |

### Aft Stations (STA 30 - 38.2)

| Station | Location | Description | Significance |
|---------|----------|-------------|--------------|
| **STA 32** | 32.0 m | Aft cargo door | Cargo loading |
| **STA 35** | 35.0 m | Aft pressure bulkhead | Pressurization ends |
| **STA 36** | 36.0 m | APU location | Auxiliary power unit |
| **STA 38.2** | 38.2 m | Trailing edge root | Aft extremity, root chord TE |

## Station Application

### Structural Stations

**Frame Stations:**
- Major frames: Every 2.0 m
- Minor frames: Every 0.5 m
- Frame designation: "Frame STA XX.X"

**Example Major Frames:**
- Frame STA 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38

### System Stations

**Equipment Bays:**
- Forward avionics: STA 3 to STA 8
- Main systems: STA 10 to STA 35
- APU bay: STA 35 to STA 38

**H₂ System:**
- Forward tank: STA 18 to STA 22
- Aft tank: STA 28 to STA 32
- Feed lines: Along centerline

### Loading Stations

**Center of Gravity Calculation:**

**Empty Aircraft CG:** STA 22.5 (typical, varies with build)

**Payload Stations:**
- Cockpit crew: STA 8.0
- Forward cabin: STA 15.0 (rows 1-10)
- Mid cabin: STA 22.5 (rows 11-20)
- Aft cabin: STA 30.0 (rows 21-30)
- Forward cargo: STA 13.0
- Aft cargo: STA 32.0

**Fuel (H₂) Stations:**
- Forward tank CG: STA 20.0
- Aft tank CG: STA 30.0

## Station Measurement

### Measurement Procedure

1. **Establish Datum:**
   - Locate nose apex (forward-most point)
   - Mark as STA 0

2. **Level Aircraft:**
   - Pitch: Level to ±0.3°
   - Roll: Level to ±0.3°

3. **Measure Longitudinally:**
   - Laser measurement from STA 0
   - Parallel to aircraft centerline
   - Record distance to component

### Measurement Tools

**Primary Method:** Laser distance measurement
- Accuracy: ±1 mm
- Range: 0 to 50 m
- Alignment: Parallel to X-axis

**Secondary Method:** Steel tape measure
- Accuracy: ±5 mm
- Use: Field measurements
- Reference: Always from STA 0

### Tolerance

**Station Location Tolerance:**
- Critical components: ±10 mm
- Non-critical: ±50 mm
- Frame stations: ±5 mm

## Station Numbering Convention

### Notation Rules

**Format:** STA XX.X
- XX: Meter value (0 to 38)
- X: Tenth of meter (0.0 to 0.9)

**Examples:**
- STA 15.0 = Fifteen meters, zero tenths
- STA 18.5 = Eighteen meters, five tenths
- STA 0.0 = Datum point

### Intermediate Stations

**Sub-Stations:**
- Between major stations
- Measured to nearest 0.1 m
- Example: Equipment at STA 14.3

## Loading and CG Calculations

### Station Moments

**Moment Arm:** Distance from datum (STA 0) to load CG

**Calculation:**
```
Moment = Weight × Station
```

**Example:**
- Passenger weight: 80 kg
- Passenger station: STA 22.5
- Moment: 80 kg × 22.5 m = 1,800 kg·m

### CG Calculation

**Formula:**
```
CG Station = Σ(Weight × Station) / Σ(Weight)
```

**Example:**
- Empty aircraft: 45,000 kg at STA 22.5 → 1,012,500 kg·m
- Fuel: 5,000 kg at STA 25.0 → 125,000 kg·m
- Payload: 18,000 kg at STA 23.0 → 414,000 kg·m
- Total weight: 68,000 kg
- Total moment: 1,551,500 kg·m
- CG: 1,551,500 / 68,000 = STA 22.8

### CG Limits

**Operational CG Range:**
- Forward limit: 20% MAC = STA 12.5
- Aft limit: 35% MAC = STA 16.3
- Normal range: 22% to 32% MAC

Note: MAC (Mean Aerodynamic Chord) has leading edge at STA 8.0

## Comparison with Conventional Aircraft

**Conventional Aircraft:**
- Fuselage stations (FS) measured from arbitrary datum
- Often datum is forward of nose (negative stations possible)
- Wing stations separate from fuselage stations

**AMPEL360 BWB:**
- Single station system for entire aircraft
- Datum at physical nose apex (no negative stations)
- Continuous through center body and wings

## Documentation

### Drawing Annotation

**On Drawings:**
- Station lines shown vertical (perpendicular to X-axis)
- Labeled: "STA XX.X"
- Major stations bold, minor stations thin

**Dimension Format:**
- "Component at STA 18.0" = Located at X = 18.0 m
- "Between STA 10 and STA 15" = X = 10 to 15 m

### Installation Instructions

**Equipment Installation:**
1. Identify required station
2. Measure from STA 0
3. Verify with adjacent known stations
4. Mark centerline (BL 0)
5. Install component

## Regulatory Compliance

**Standards:**
- SAE AS755: Aircraft axis systems
- ATA iSpec 2200: Documentation standards
- ISO 1151: Flight dynamics terminology
