# FCOM - Performance Section

**Document:** Flight Crew Operations Manual - Performance  
**ATA Chapter:** 02-10-00 - Aircraft General Data  
**Version:** 1.0  
**Date:** 2025-11-05

## Purpose

This section provides flight crew with operational performance data and procedures for flight planning and in-flight operations of the AMPEL360 BWB H₂ Hy-E Q100 aircraft.

## Quick Reference Performance Data

### Aircraft Specifications Summary

| Parameter | Value |
|-----------|-------|
| Wing Span | 52.0 m (170.6 ft) |
| MTOW | 185,000 kg (407,855 lb) |
| Passenger Capacity | 220 (standard layout) |
| Maximum Range | 4,000 km (2,160 nm) |
| Cruise Speed | Mach 0.80 / 470 KTAS |
| Service Ceiling | 43,000 ft |

## Takeoff Performance

### V-Speeds Quick Reference (MTOW, Sea Level, ISA)

| Speed | Value | Description |
|-------|-------|-------------|
| V₁ | 148 KIAS | Decision speed |
| VR | 153 KIAS | Rotation speed |
| V₂ | 160 KIAS | Takeoff safety speed |
| VLOF | 155 KIAS | Liftoff speed |

**CAOS Calculation:** V-speeds automatically calculated based on:
- Actual weight
- CG position
- Temperature/pressure altitude
- Runway condition and slope
- Wind components

### Takeoff Distance Requirements (Dry Runway)

**Sea Level, ISA Conditions:**

| Weight (kg) | Takeoff Roll (m) | Total Distance (m) |
|-------------|-----------------|-------------------|
| 185,000 (MTOW) | 1,650 | 2,450 |
| 170,000 | 1,450 | 2,150 |
| 155,000 (MLW) | 1,280 | 1,900 |

**Field Condition Adjustments:**
- Wet runway: +15%
- Altitude: +7% per 1,000 ft
- Temperature: +3% per 10°C above ISA
- Tailwind: +10% per 5 kt (max 10 kt)
- Headwind: -5% per 10 kt

### Takeoff Procedure

1. **Pre-Takeoff:**
   - Verify CAOS weight and CG calculation
   - Confirm V-speeds on flight deck display
   - Set fuel cell power to takeoff mode
   - Verify all 6 fuel cell stacks operative

2. **Takeoff Roll:**
   - Advance throttle to takeoff power (18 MW)
   - Monitor acceleration and fuel cell parameters
   - Call "V₁" at decision speed
   - Call "Rotate" at VR

3. **Rotation and Liftoff:**
   - Rotate smoothly at 2-3° per second
   - Target pitch: 12-15° nose up
   - Maintain V₂ + 10 kt after liftoff
   - Positive rate: Gear up

## Climb Performance

### Standard Climb Profile

**Phase 1: Initial Climb (0 - 10,000 ft)**
- Speed: 210 KIAS
- Power: 16.5 MW (92%)
- Rate of Climb: 2,800 ft/min at MTOW
- Time: 3.6 minutes
- Fuel Used: 85 kg H₂

**Phase 2: Cruise Climb (10,000 ft - Cruise Alt)**
- Speed: 280 KIAS / Mach 0.78 (transition FL280)
- Power: 14 MW (78%)
- Rate of Climb: 1,800-2,200 ft/min
- Time to FL370: 21 minutes from 10,000 ft
- Fuel Used: 235 kg H₂

### Optimum Climb Schedule

**CAOS Recommended Profile:**
- System calculates optimal climb speed and altitude
- Considers current weight, temperature, winds
- Maximizes efficiency while meeting ATC requirements
- Updates in real-time during climb

### Step Climb Procedure

**Typical Weights for Step Climbs:**
- FL350: 185,000 kg (MTOW)
- FL370: 175,000 kg
- FL390: 165,000 kg
- FL410: 155,000 kg
- FL430: 145,000 kg (max altitude, light weight)

## Cruise Performance

### Optimal Cruise Speeds

**At FL370, Weight 165,000 kg:**

| Mach | Purpose | Fuel Flow | Range Factor |
|------|---------|-----------|--------------|
| 0.75 | Max Range Cruise | 520 kg/h | 0.85 nm/kg |
| 0.78 | Long Range Cruise | 505 kg/h | 0.91 nm/kg |
| 0.80 | Normal Cruise | 495 kg/h | 0.95 nm/kg |
| 0.82 | High Speed Cruise | 510 kg/h | 0.94 nm/kg |

**CAOS Recommendation:** System displays optimal cruise speed based on:
- Flight plan route and winds aloft
- Cost index (if programmed)
- Fuel remaining and destination
- Real-time weather updates

### Cruise Altitude Selection

**General Guidelines:**
| Weight Range | Optimal Altitude | Fuel Flow | Notes |
|--------------|------------------|-----------|-------|
| 185-175t | FL350-360 | 550 kg/h | Early cruise |
| 175-165t | FL370-380 | 510 kg/h | Mid cruise |
| 165-155t | FL390-400 | 475 kg/h | Late cruise |
| 155-145t | FL410-430 | 455 kg/h | Extended cruise |

**CAOS Optimization:**
- Suggests step climbs when beneficial
- Accounts for forecast winds
- Calculates optimal time to request higher altitude
- Provides fuel savings estimate for each step

### Fuel Management

**Standard Cruise Consumption:**
- 495 kg H₂/hour at Mach 0.80, FL370
- Approximately 0.8 kg H₂ per 100 ASK (Available Seat Kilometers)

**Fuel Reserve Requirements:**
- Destination alternate: Based on distance
- Holding: 30 minutes at 1,500 ft
- Final reserve: 500 kg H₂ (45 minutes)
- Contingency: 5% of trip fuel

**CAOS Fuel Monitoring:**
- Continuous comparison: planned vs actual
- Burn rate trending and prediction
- Reserve fuel alerts at decision points
- Alternative airport recommendations if needed

## Descent Performance

### Standard Descent Profile

**High Altitude Descent (FL410 to FL100):**
- Speed: Mach 0.78 / 280 KIAS (transition FL280)
- Descent Rate: 1,800 - 2,200 ft/min
- Power: 4.5 MW (25% - idle descent)
- Time: 16 minutes
- Distance: 145 nm
- Fuel: 45 kg H₂

**Low Altitude Descent (10,000 ft to Sea Level):**
- Speed: 250 KIAS
- Descent Rate: 1,500 ft/min
- Time: 6.5 minutes
- Distance: 28 nm
- Fuel: 15 kg H₂

### Descent Planning

**Top of Descent (TOD) Calculation:**
```
Distance to TOD (nm) = (Altitude to lose in ft / 1000) × 3
```

**Example:** From FL370 to 3,000 ft AGL
- Altitude to lose: 37,000 - 3,000 = 34,000 ft
- TOD distance: 34 × 3 = 102 nm before arrival

**CAOS Calculation:**
- Automatic TOD calculation with wind correction
- ATC constraint management
- Speed and altitude restriction compliance
- Optimal descent profile for efficiency

## Approach and Landing Performance

### Approach Speeds

**VREF Calculation (Landing Configuration):**

| Weight (kg) | VREF (kt) | Final Approach |
|-------------|-----------|----------------|
| 155,000 (MLW) | 138 | VREF + 5 |
| 145,000 | 132 | VREF + 5 |
| 135,000 | 128 | VREF + 5 |
| 125,000 | 124 | VREF + 5 |

**Wind Corrections:**
- Gust correction: +1/2 steady wind + full gust increment
- Maximum correction: +20 kt
- CAOS automatic calculation and display

### Landing Distance Requirements

**Dry Runway, Sea Level, ISA:**

| Weight (kg) | Landing Distance (m) | Threshold Speed |
|-------------|---------------------|-----------------|
| 155,000 (MLW) | 1,850 | 133 kt |
| 145,000 | 1,700 | 127 kt |
| 135,000 | 1,600 | 123 kt |

**Field Condition Adjustments:**
- Wet runway: +15%
- Altitude: +5% per 1,000 ft
- Tailwind: +15% per 5 kt
- Downslope: +10% per 1° down

### Landing Procedure

1. **Final Approach Configuration:**
   - Speed: VREF + wind correction
   - Flaps: Landing position
   - Gear: Down and locked
   - Fuel cells: 8 MW approach power

2. **Threshold Crossing:**
   - Height: 50 ft above threshold
   - Speed: VREF + 5 kt
   - Pitch: 3-5° nose up

3. **Touchdown:**
   - Target: 300-500 m past threshold
   - Sink rate: 2-4 ft/sec
   - Pitch: 2-3° nose up at touchdown

4. **Rollout and Braking:**
   - Regenerative braking engagement
   - Wheel brakes as required
   - Minimum energy consumption

## Range Planning

### Maximum Range Capability

**Standard Configuration (220 passengers):**

| Conditions | Range (km) | Range (nm) | Block Time |
|------------|-----------|------------|------------|
| ISA, No Wind | 4,000 | 2,160 | 6:15 |
| ISA +10°C | 3,850 | 2,079 | 6:20 |
| 50 kt Headwind | 3,450 | 1,863 | 6:35 |
| 50 kt Tailwind | 4,550 | 2,457 | 5:55 |

**CAOS Range Calculation:**
- Real-time range ring display
- Wind and temperature updates
- Alternate airport monitoring
- Fuel reserve compliance checking

### Payload-Range Trade-offs

| Payload (kg) | Passengers | Range (km) | Range (nm) |
|--------------|-----------|-----------|------------|
| 25,000 | 220 + cargo | 3,200 | 1,728 |
| 22,000 | 220 pax | 4,000 | 2,160 |
| 18,000 | 180 pax | 4,500 | 2,430 |
| 10,000 | 100 pax | 5,200 | 2,808 |

## CAOS Digital Twin Integration

### Flight Deck Integration

**Real-Time Performance Displays:**
- Current vs predicted fuel burn
- Optimum altitude recommendation
- Time and fuel to destination
- Reserve fuel status and alerts
- Alternative airports in range

**Performance Predictions:**
- Updated every 30 seconds
- 99% accuracy correlation
- Accounts for actual weather
- Considers fuel cell performance
- CG position effects included

### AI Performance Assistance

**Route Optimization:**
- Best altitude for conditions
- Speed adjustments for efficiency
- Weather avoidance routing
- Traffic flow optimization

**Fuel Management:**
- Automatic fuel transfer for optimal CG
- Consumption monitoring and trending
- Reserve fuel protection
- Diversion planning if needed

**Predictive Analysis:**
- Performance degradation detection
- Fuel cell health monitoring
- System efficiency tracking
- Maintenance alerts

## Emergency Performance

### One Fuel Cell Stack Inoperative

**Performance Penalties:**
- Maximum altitude: FL300
- Maximum speed: Mach 0.75
- Range reduction: 35%
- Increased fuel burn: +25%

**Operational Limitations:**
- No operations above 30,000 ft
- Return to suitable airport
- Land at nearest suitable if multiple failures

### Drift-Down Performance

**One Stack Out at FL370:**
- Initial descent rate: 800 ft/min
- Stabilization altitude: 24,000 ft
- Time to stabilize: 16 minutes
- Distance covered: 75 nm

## Weather Considerations

### Performance in Icing Conditions

**Ice Accretion Effects:**
- Stall speed increase: +10 kt
- Drag increase: +15%
- Fuel burn increase: +12%
- Use CAOS anti-ice system monitoring

### Performance in Turbulence

**Speed Adjustments:**
- Moderate turbulence: Reduce to turbulence penetration speed
- Severe turbulence: 280 KIAS / M0.78 (turbulence speed)
- CAOS provides turbulence prediction ahead

## Related Documents

- AFM Section 5 - Performance (5.1, 5.2)
- FCOM Limitations Section
- FCOM Normal Procedures
- FCOM Abnormal Procedures
- CAOS User Guide
- Weight and Balance Manual

## Performance Planning Tools

### Quick Reference Formulas

**Time-Distance-Fuel:**
- Time (min) = Distance (nm) / Ground Speed (nm/min)
- Fuel (kg) = Time (hr) × Fuel Flow (kg/hr)

**Descent Planning:**
- Start descent 3 nm per 1,000 ft to lose
- Add 1 nm per 10 kt tailwind
- Subtract 1 nm per 10 kt headwind

**Required Fuel:**
```
Trip Fuel + Alternate Fuel + Reserve (500kg) + Contingency (5% trip)
```

### Flight Planning Checklist

☐ Verify MTOW not exceeded (185,000 kg)  
☐ Check CG within limits (15-42% MAC)  
☐ Calculate V-speeds for actual conditions  
☐ Verify runway length adequate for weight  
☐ Confirm fuel sufficient for destination + alternate + reserves  
☐ Review CAOS performance predictions  
☐ Brief crew on performance considerations  

---

**Document Control:**
- Status: Released - Flight Operations
- Classification: Flight Crew Use
- Training Required: Yes - Performance Planning
- Digital Access: CAOS flight deck display
- Revision Cycle: Quarterly or upon performance data update
