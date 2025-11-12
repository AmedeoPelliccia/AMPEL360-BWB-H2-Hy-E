# Field Performance Design

## Executive Summary

The AMPEL360 field performance design enables operations from Code 4C/E runways (2,500m minimum) with margins for safety, all-weather operations, and varied field conditions.

## Takeoff Performance

### Runway Requirements

**MTOW Takeoff (145,000 kg):**
- **Sea Level, ISA:** 2,200 m
- **5,000 ft elevation, ISA+15:** 2,800 m
- **Design Target:** 2,500 m (Code 4E runway)

**Takeoff Segments:**
```
1. Ground Roll: 1,650 m
2. Rotation: 50 m
3. Airborne (to 35 ft): 300 m
───────────────────────────
   TODR: 2,000 m (ISA, SL)
   
With Safety Factor (1.15):
   Certified TODR: 2,300 m
```

### Takeoff Speeds

**V-Speeds (MTOW):**
- **V1 (Decision speed):** 145 KIAS
- **VR (Rotation):** 150 KIAS
- **V2 (Climb speed):** 160 KIAS
- **VLOF (Liftoff):** 155 KIAS

**Configuration:**
- Flaps: 15°
- Slats: Extended
- Fuel cells: 100% power

### Climb Performance

**Takeoff Climb Segments:**
```
1st Segment (Gear Down):
   - Gradient: 2.5% (CS-25 requires 0% for twins)
   - Rate: 1,200 fpm

2nd Segment (Gear Up):
   - Gradient: 4.5% (CS-25 requires 2.4%)
   - Rate: 2,000 fpm
   - Critical segment ✓

Final Segment (Clean):
   - Gradient: 6.0% (CS-25 requires 1.2%)
   - Rate: 2,500 fpm
```

**Safety Margins:** Exceed CS-25 by significant margin

### Balanced Field Length

**Concept:** V1 chosen so accelerate-stop = accelerate-go
- **Balanced Field:** 2,300 m at MTOW, ISA, SL
- **V1 Selection:** Optimized for runway length
- **Safety:** Abort or continue equally safe

### Obstacle Clearance

**CS-25 Requirements:**
- Clear 35 ft screen at end of TODR
- Net takeoff path clears obstacles by:
  - 35 ft vertical + 0.5% gradient

**AMPEL360 Performance:**
- Standard departure: Clears 50 ft by 300 m
- Obstacle gradient: 6% capable (exceeds 2.4% requirement)

## Landing Performance

### Runway Requirements

**MLW Landing (130,000 kg):**
- **Sea Level, ISA:** 1,650 m
- **5,000 ft, ISA+15:** 2,050 m
- **Design Target:** 1,800 m

**Landing Distance:**
```
1. Screen height (50 ft): 0 m
2. Airborne (50 ft to threshold): 400 m
3. Touchdown to braking: 100 m
4. Braking distance: 1,000 m
─────────────────────────────────
   Total LDR: 1,500 m (ISA, SL)
   
With Safety Factor (1.67):
   Certified LDR: 2,500 m
```

### Approach and Landing Speeds

**Approach Speeds (MLW):**
- **VREF (Reference speed):** 135 KIAS
- **VAP (Approach speed):** 140 KIAS
- **VTH (Threshold speed):** 137 KIAS
- **VTDZ (Touchdown speed):** 130 KIAS

**Configuration:**
- Flaps: 35° (landing)
- Slats: Extended
- Gear: Down
- Speedbrakes: Armed

### Braking Performance

**Deceleration Devices:**
- Wheel brakes: Carbon composite
- Reverse thrust: Fuel cell reversers (moderate)
- Speedbrakes: Full deployment
- Aerodynamic drag: High (BWB advantage)

**Deceleration Rates:**
- Maximum braking: 6 ft/s² (wet runway: 3 ft/s²)
- Autobrake settings: 1 (min) to 4 (max)
- Typical landing: Autobrake 2 = 1,000 m ground roll

### Go-Around Performance

**Missed Approach:**
- Configuration: Landing flaps, gear down
- Fuel cell power: 100%
- Climb gradient: 3.2% (CS-25 requires 2.1%)
- Rate of climb: 1,500 fpm

**Gear Retraction:**
- After positive climb
- Flaps to 15° simultaneously
- Acceleration to V2 + 10 kt
- Clean configuration: 180 KIAS

## Wet and Contaminated Runways

### Wet Runway Performance

**Standing Water (< 3mm):**
- Takeoff: +5% distance
- Landing: +15% distance
- Hydroplaning speed: 115 KIAS (below VREF)

**Operations:**
- Autobrakes recommended: Setting 3
- Thrust reversers: Maximum
- Antiskid: Active

### Contaminated Runway

**Slush/Snow (up to 15mm):**
- Takeoff: +25% distance
- Landing: +40% distance
- Operations: Restricted or prohibited

**Ice:**
- Operations: Prohibited without treatment
- Braking coefficient < 0.25: No operations
- Safety priority: De-icing required

## Hot and High Performance

### High Altitude Airports

**Example: Denver (KDEN, 5,430 ft):**
```
Conditions: ISA+15, MTOW
Takeoff Distance: 2,950 m
Available Runway: 3,658 m (12,000 ft)
Margin: 708 m (24% margin) ✓

Climb Gradient: 2.8% (adequate)
```

**High Altitude Strategy:**
- Reduced MTOW if necessary
- Extended flap setting: 20° option
- Favorable wind: Takeoff into wind

### High Temperature Effects

**ISA+20 Performance Degradation:**
- Takeoff distance: +18%
- Climb gradient: -20% (still adequate)
- Fuel cell efficiency: -3% (minimal)

**Thermal Management:**
- Fuel cell cooling: Adequate to ISA+30
- H2 tank insulation: Effective
- No temperature limitations up to ISA+20

## Short Field Operations

### Code 4C Runway Operations

**Minimum Runway:** 1,800 m (5,905 ft)
- **MTOW Takeoff:** Possible with reduced weight
- **MLW Landing:** Possible with normal margins
- **Operational Weight:** 125,000 kg (86% MTOW)

**Short Field Technique:**
- Maximum flaps: 20° takeoff
- Minimum V1: 140 KIAS
- Steep approach: 3.5° glideslope
- Maximum braking: Autobrake 4

### Remote/Island Operations

**Design Consideration:**
- Many H2-ready airports may be smaller
- Performance designed for flexibility
- Safety margins maintained

**Example Airports:**
- Funchal (LPMA): 2,781 m runway ✓
- Innsbruck (LOWI): 2,000 m runway (weight restricted)
- Saint Martin (TNCM): 2,179 m runway ✓

## Obstacle Clearance Procedures

### Standard Departure Procedures (SDP)

**Climb Performance:**
- Net gradient: 4.5% (2nd segment)
- Turn capability: After 400 ft AGL
- Obstacle clearance: Min 35 ft vertical

**BWB Advantages:**
- High L/D: Excellent climb performance
- Low drag: Sustained climb capability
- Fuel cell instant power: No engine spool-up delay

### Engine-Out Procedures

**Single Fuel Cell Failure:**
- **Performance:** 80% total power remaining
- **Climb Gradient:** 2.5% (exceeds CS-25 2.4% requirement)
- **Ceiling:** FL280 (adequate for most routes)

**Diversion:** All airports within range have landing capability

## Crosswind Limits

### Demonstrated Crosswind

**Certification Testing:**
- **Maximum demonstrated:** 35 kt
- **Crosswind component:** 30 kt typical limit
- **Tail wind component:** 15 kt limit

**BWB Characteristics:**
- Wide gear track: Excellent lateral stability
- Low profile: Reduced weather vaning
- Control authority: Adequate for crosswinds

### Wind Limitations

**Takeoff Limits:**
- Headwind: Beneficial (reduces takeoff distance)
- Tailwind: 15 kt maximum (regulatory)
- Crosswind: 30 kt maximum (operational)

**Landing Limits:**
- Headwind: Beneficial (reduces landing distance)
- Tailwind: 15 kt maximum
- Crosswind: 30 kt maximum
- Gusts: Add 50% of gust increment

## Certification Compliance

### CS-25 Takeoff Requirements

**CS-25.105:** Takeoff
- All-engines: V2 ≥ 1.13 VSR ✓
- One-engine-out: V2 ≥ 1.08 VSR ✓

**CS-25.111:** Takeoff Path
- Net takeoff gradient: Exceeds requirements ✓
- Obstacle clearance: 35 ft + 0.5% gradient ✓

### CS-25 Landing Requirements

**CS-25.125:** Landing
- Approach speed: 1.23 VSR or 1.3 VS ✓
- Landing distance: Certified LDR × 0.6 = actual ✓

**CS-25.119:** Landing Climb
- All-engines: Gradient ≥ 3.2% ✓
- One-engine-out: Gradient ≥ 2.1% ✓

---

**References:**
- Takeoff Performance: PA-TO-2025-001
- Landing Performance: PA-LDG-2025-001
- Flight Crew Operating Manual: FCOM Section 03.01-03.02
- CS-25 Certification: CRT-FLD-2025-001
- Airport Analysis: AAM-2025-001
