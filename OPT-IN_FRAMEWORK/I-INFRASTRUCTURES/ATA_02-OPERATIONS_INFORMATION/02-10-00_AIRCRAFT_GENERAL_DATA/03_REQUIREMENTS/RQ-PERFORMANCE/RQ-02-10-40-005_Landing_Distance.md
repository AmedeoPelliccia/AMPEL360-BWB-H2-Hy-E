# RQ-02-10-40-005: Landing Distance

**Requirement ID:** RQ-02-10-40-005  
**Category:** Performance  
**Priority:** Critical  
**Status:** Approved

## Requirement

The aircraft shall achieve a landing distance not exceeding 1,800 meters (5,906 ft) at MLW under ISA sea level conditions with maximum manual braking.

**Landing Performance (MLW, ISA, Sea Level):**
- Landing Distance (LDR): 1,800 m (5,906 ft)
- Landing Distance (Available): 1,950 m (6,398 ft) with safety margin
- Landing Run: 1,200 m (3,937 ft)
- Approach Speed (VREF): 135 KIAS
- Threshold Speed: 140 KIAS

## Performance at Alternate Conditions

| Condition | LDR (m) | Required Runway (m) |
|-----------|---------|---------------------|
| ISA, Sea Level | 1,800 | 1,950 |
| ISA+15°C, Sea Level | 1,900 | 2,060 |
| ISA, 5,000 ft | 2,100 | 2,280 |
| ISA+15°C, 5,000 ft | 2,250 | 2,440 |

**Note:** Required runway length includes safety factor per CS-25

## Rationale

Landing distance requirements ensure:
- Access to same airports as for takeoff
- Safe landing with margin
- Autobrake system effectiveness
- Rejected landing capability
- Wet and contaminated runway operations
- Competitive with conventional aircraft

## Landing Configuration

**Flap Setting:** Full landing flaps (40°)
- Maximum lift coefficient
- Optimized for BWB configuration
- Steep approach capability (3.5°)

**Speedbrakes/Spoilers:**
- Automatic deployment on touchdown
- Ground spoilers reduce lift
- Enhanced braking effectiveness

## V-Speeds (MLW, ISA, SL)

| Speed | Value (KIAS) | Definition |
|-------|--------------|------------|
| VREF | 135 | Reference landing speed (1.3 × VSO) |
| Threshold | 140 | Speed at 50 ft threshold |
| Touchdown | 130 | Typical touchdown speed |
| VSO | 104 | Stall speed landing config |

## Braking System

**Autobrake Modes:**
- LOW: Smooth deceleration (passengers)
- MEDIUM: Standard operations
- HIGH: Short runway operations
- MAX: Emergency/contaminated runway

**Manual Braking:**
- Maximum manual braking: 0.45g deceleration
- Anti-skid protection
- Brake temperature monitoring (CAOS)

## Landing Procedure

**Normal Landing:**
1. Establish approach speed (VREF + wind correction)
2. Cross threshold at 50 ft
3. Smooth flare and touchdown
4. Deploy thrust reversers (if available)
5. Apply brakes (autobrake or manual)
6. Maintain directional control
7. Exit runway at appropriate taxiway

**Go-Around (from 50 ft):**
- Maximum takeoff thrust
- Pitch up to climb attitude (7.5°)
- Positive rate: retract landing gear
- Accelerate to flap retraction speeds
- Follow go-around profile

## Verification

- **Method:** Flight Test
- **Procedure:**
  - Landing distance measurements
  - Wet runway testing
  - Autobrake system validation
  - Go-around demonstrations
- **Acceptance Criteria:**
  - LDR ≤ 1,800 m at MLW, ISA, SL
  - Demonstrated compliance with CS-25.125
  - Brake energy absorption adequate
  - Wet runway performance validated

## Runway Surface Conditions

| Surface | LDR Multiplier | LDR (m) at MLW |
|---------|----------------|----------------|
| Dry | 1.0× | 1,800 |
| Wet | 1.15× | 2,070 |
| Contaminated (3mm) | 1.30× | 2,340 |

**Operational Policy:** Landing distance assessment required for contaminated runways

## CAOS Integration

- Real-time landing distance calculation
- Runway condition assessment
- Wind component analysis
- VREF computation
- Autobrake mode recommendation
- Brake temperature monitoring
- Go-around decision support

## Compliance

- CS-25.125: Landing
- CS-25.735: Brakes and braking systems
- CS-25.1587: Performance information
- AMC 25.1587: Takeoff and landing data

## Related Requirements

- RQ-02-10-20-002: MLW Specification
- RQ-02-10-10-002: Ground Clearances
- RQ-02-10-40-004: Takeoff Distance

---

**Document Control:**
- Version: 1.0
- Status: Approved
- Last Updated: 2025-11-05
- Approved By: Flight Test Engineer
