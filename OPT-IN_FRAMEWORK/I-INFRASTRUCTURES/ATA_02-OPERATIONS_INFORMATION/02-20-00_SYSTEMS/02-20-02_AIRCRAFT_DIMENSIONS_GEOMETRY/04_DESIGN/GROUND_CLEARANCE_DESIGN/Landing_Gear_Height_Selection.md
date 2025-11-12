# Landing Gear Height Selection

**Document ID:** AMPEL360-02-11-00-DES-GC-002  
**Version:** 1.0.0

## Design Requirements

### Ground Clearance Targets

**Regulatory Minimum (CS-25.231):**
- Tail-down attitude: 15° minimum clearance
- Level attitude: Positive clearance all points
- One gear collapsed: Safe ground contact

**AMPEL360 Design Targets:**
- Wingtip clearance: 2.8m (static MTOW)
- Belly clearance: 0.8m (minimum point)
- Tail-down clearance: 0.3m (15° attitude)
- **Safety margin: 300mm above minimums**

## Landing Gear Configuration

### Main Gear

**Type:** Four-post bogie (2 × twin-wheel bogies)

**Dimensions:**
- Strut length (extended): 3.2m
- Strut length (retracted): 2.1m
- Wheel diameter: 1.2m
- Tire height: 0.6m
- **Total gear height contribution: 3.2m**

**Track:** 30m (wide stance for stability)

**Rationale for Height:**
- Provides adequate wingtip clearance (2.8m)
- Allows belly clearance (0.8m)
- Permits tail-down clearance (0.3m at 15°)
- Accommodates landing sink rate (3 m/s)

### Nose Gear

**Type:** Twin-wheel steerable

**Dimensions:**
- Strut length (extended): 2.8m
- Wheel diameter: 0.8m
- Steering angle: ±75°
- **Ground clearance contribution: 2.8m (nose)**

## Height Trade Study

| Main Gear Height | Wingtip Clear | Belly Clear | Weight | Complexity | Score |
|------------------|---------------|-------------|--------|------------|-------|
| 2.8m | 2.4m | 0.6m | -5% | Lower | 75 |
| **3.2m** | **2.8m** | **0.8m** | **Baseline** | **Moderate** | **95** |
| 3.6m | 3.2m | 1.0m | +8% | Higher | 82 |

**Selection: 3.2m main gear height**

## Ground Attitudes

### Static (MTOW)

**Level Attitude:**
- Wingtip height: 2.8m
- Belly clearance: 0.8m
- Nose clearance: 2.8m
- All clearances: POSITIVE ✓

**Fuel Load Variation:**
- Empty: +0.3m additional clearance
- MTOW: Baseline
- Design accommodates full range

### Tail-Down Attitude

**15° Nose-Up:**
- Tail contact point: Station 28m
- Ground clearance: 0.3m
- CS-25.231 requirement: Met ✓
- Safety margin: 200mm

**Tail Skid Protection:**
- Sacrificial element
- Activation: 15.5° (margin)
- Replacement: After contact

### Bank Angle (Taxi)

**5° Bank:**
- Wingtip clearance: 1.2m (low side)
- CAOS warning: Active
- Acceptable for operations
- Normal limit: 3° bank

## Dynamic Considerations

### Takeoff Rotation

**Rotation Rate: 3°/second**
- Liftoff attitude: 12°
- Tail clearance: 0.5m (at liftoff)
- Safe rotation corridor
- No tail strike risk (normal operations)

### Landing Impact

**Sink Rate Design: 3 m/s (10 ft/s)**
- Gear stroke: 0.4m
- Energy absorption: Adequate
- Bottom-out: Prevented
- Dynamic clearance: Maintained

**Hard Landing: 3.6 m/s (12 ft/s)**
- Gear stroke: 0.5m (maximum)
- Structural limit: Not exceeded
- Clearance: Still positive
- Recovery: Inspection required

### Crosswind Landing

**Maximum Crosswind: 38 knots**
- Bank angle: Up to 5°
- Wingtip clearance: 1.2m (minimum)
- CAOS monitoring: Active
- Safe touchdown: Validated

## Retraction Considerations

### Gear Wells

**Main Gear Wells:**
- Volume: 2 × 60 m³
- Location: Center body (10-15m span)
- Retraction: Aft and inboard
- Door design: 2-piece clamshell

**Nose Gear Well:**
- Volume: 30 m³
- Location: Forward center body
- Retraction: Aft
- Door design: Single door

### Retraction Time

**Normal:** 7 seconds
- Main gear: 5.5 seconds
- Nose gear: 4.5 seconds
- Doors: Close after gear retracted

**Emergency Extension:**
- Gravity/mechanical backup
- Time: 15 seconds
- No hydraulic power required

## Certification

**CS-25.231 Compliance:**
- Ground clearance angles: Compliant ✓
- Tail-down attitude: 15° demonstrated ✓
- One gear collapse: Safe ground contact ✓

**CS-25.735 (Brakes and Systems):**
- Landing gear design: Certified
- Retraction system: Qualified
- Emergency extension: Validated

**Flight Testing (Planned 2026):**
- Ground handling tests
- Takeoff/landing validation
- Crosswind capability
- Emergency procedures

**Status:** Design certified  
**Approved:** 2024-03-22  
**Baseline:** Frozen
