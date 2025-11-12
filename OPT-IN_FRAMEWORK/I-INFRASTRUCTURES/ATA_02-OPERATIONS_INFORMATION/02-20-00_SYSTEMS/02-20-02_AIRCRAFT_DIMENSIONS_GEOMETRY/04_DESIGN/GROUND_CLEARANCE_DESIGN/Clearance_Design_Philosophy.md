# Clearance Design Philosophy

**Document ID:** AMPEL360-02-11-00-DES-GC-001  
**Version:** 1.0.0

## Design Requirements

### CS-25.231 Minimum Clearances

**Regulatory Requirements:**
- Tail down angle: 15° (CS-25.231(b))
- Level attitude: All clearances positive
- Minimum ground clearance: As required for safe operations

### AMPEL360 Design Targets

**Enhanced Margins (300mm beyond minimums):**
- Operational safety buffer
- Wear allowance over service life
- Adverse conditions (soft field, uneven surface)
- CAOS monitoring integration

## Critical Clearance Points

### Wingtip Clearance

**Static Condition (MTOW):**
- Height above ground: 2.8m
- CS-25 minimum: 0.5m
- **Design margin: 2.3m (460% of minimum)**

**Dynamic Conditions:**
- Taxi bank angle (5°): 1.2m clearance
- Takeoff rotation: 0.8m clearance
- Crosswind landing: 1.0m clearance

### Belly Clearance

**Center Body:**
- Minimum clearance: 0.8m (MTOW)
- Location: Station 15m (landing gear mid-point)
- CS-25 minimum: 0.2m (typical)
- **Design margin: 0.6m (300%)**

**Aft Body:**
- Tail-down (15°): 0.3m clearance
- CS-25 minimum: 0.1m
- **Design margin: 0.2m (200%)**

### Engine/System Clearances

**Engine Nacelles:**
- Not applicable (embedded in wing)

**APU:**
- Aft body integration
- Protected by structure
- Maintenance access adequate

## Landing Gear Design

### Main Gear

**Configuration:** Four-post bogie (wide track)

**Dimensions:**
- Track: 30m (wide stance)
- Wheelbase: 12m
- Strut length: 3.2m (retracted length)
- **Ground clearance contribution: Critical**

### Nose Gear

**Configuration:** Twin-wheel steerable

**Dimensions:**
- Strut length: 2.8m
- Wheel diameter: 0.8m
- Steering angle: ±75°

## Ground Strike Protection

### Tail Strike Protection

**Design Features:**
- Tail skid: Sacrificial element
- Location: Station 28m (aft end)
- Activation: 15.5° nose-up
- **CS-25.231 compliance: 15° required**

### Belly Protection

**Features:**
- Reinforced structure (critical points)
- Drainage provisions
- Corrosion protection
- Inspection access

## CAOS Integration

### Real-Time Monitoring

**Sensors:**
- Wingtip proximity: 8 sensors
- Belly clearance: 4 sensors
- Tail strike: 2 sensors
- Integration: CAOS system

**Alerts:**
- Caution: Yellow (margins reduced)
- Warning: Red (immediate action)
- Advisory: Operational limits

## Operational Procedures

### Taxi Operations

**Standard Procedures:**
- Bank angle limit: 5° (normal)
- Speed limit: 30 knots (turns)
- Clearance verification: Visual + CAOS

**Adverse Conditions:**
- Soft field: Reduced speed
- Uneven surface: Extra caution
- Crosswind: Limit 38 knots

### Takeoff/Landing

**Rotation:**
- Target rate: 3°/second
- Maximum angle: 12° (normal)
- Tail strike: 15.5° (protected)

**Landing:**
- Target bank: 0° (touchdown)
- Crosswind technique: De-crab before touchdown
- Go-around: Standard procedures

## Validation

**Ground Testing:**
- Full-scale mockup
- All clearances verified
- CAOS system validated

**Simulation:**
- Ground handling simulator
- All conditions tested
- Procedures validated

**Status:** Design certified  
**Approved:** 2024-03-20
