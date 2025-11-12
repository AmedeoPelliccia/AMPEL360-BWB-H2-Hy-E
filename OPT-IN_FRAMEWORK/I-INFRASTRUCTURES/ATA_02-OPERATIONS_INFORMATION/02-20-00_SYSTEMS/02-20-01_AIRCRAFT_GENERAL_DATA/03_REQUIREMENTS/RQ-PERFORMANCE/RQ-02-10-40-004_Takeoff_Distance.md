# RQ-02-10-40-004: Takeoff Distance

**Requirement ID:** RQ-02-10-40-004  
**Category:** Performance  
**Priority:** Critical  
**Status:** Approved

## Requirement

The aircraft shall achieve a takeoff distance not exceeding 2,400 meters (7,874 ft) at MTOW under ISA sea level conditions to ensure compatibility with major airports worldwide.

**Takeoff Performance (MTOW, ISA, Sea Level):**
- Takeoff Distance (TODR): 2,400 m (7,874 ft)
- Balanced Field Length (BFL): 2,450 m (8,038 ft)
- Takeoff Run: 1,650 m (5,413 ft)
- Rotation Speed (VR): 155 KIAS
- Liftoff Speed (VLOF): 162 KIAS
- V2 Speed: 170 KIAS

## Performance at Alternate Conditions

| Condition | TODR (m) | BFL (m) |
|-----------|----------|---------|
| ISA, Sea Level | 2,400 | 2,450 |
| ISA+15°C, Sea Level | 2,650 | 2,720 |
| ISA, 5,000 ft | 3,150 | 3,250 |
| ISA+15°C, 5,000 ft | 3,600 | 3,720 |

## Rationale

Takeoff distance requirements ensure:
- Access to 95% of commercial airports worldwide
- Hot and high airport operations
- Single-engine-out safety margins
- Competitive with current narrowbody aircraft
- Regulatory compliance

## Runway Compatibility

**Target Airports (examples):**
- Short runway capability: 2,400-2,500 m
- London City (LCY): 1,508 m runway (payload-limited operations)
- Major hubs: All runways compatible

## Takeoff Configuration

**Flap Setting:** Takeoff flaps (15°)
- Optimized for BWB configuration
- Enhanced lift coefficient
- Reduced takeoff speed

**BWB Advantages:**
- High lift coefficient from integrated body
- Reduced induced drag
- Efficient ground effect utilization

## V-Speeds (MTOW, ISA, SL)

| Speed | Value (KIAS) | Definition |
|-------|--------------|------------|
| V1 (Decision Speed) | 150 | Takeoff decision speed |
| VR (Rotation) | 155 | Rotation speed |
| VLOF (Liftoff) | 162 | Liftoff speed |
| V2 (Takeoff Safety) | 170 | Takeoff safety speed (OEI) |
| VFTO (Final Takeoff) | 185 | Final takeoff speed |

## Verification

- **Method:** Flight Test
- **Procedure:** 
  - Accelerate-stop tests
  - Accelerate-go tests (OEI)
  - Balanced field length determination
- **Acceptance Criteria:**
  - TODR ≤ 2,400 m at MTOW, ISA, SL
  - One-engine-out climb gradient ≥ 2.4% at V2
  - Demonstrated compliance with CS-25.105, 25.107, 25.109
  - Certification flight tests successful

## Operational Procedures

**Standard Takeoff:**
1. Align on centerline
2. Advance thrust levers to takeoff power
3. Monitor engine parameters (CAOS)
4. Call V1 at decision speed
5. Rotate at VR (smooth, ~3°/sec)
6. Maintain V2+10 until obstacle clearance
7. Accelerate and retract flaps per schedule

**Rejected Takeoff:**
- Initiate below V1
- Throttle idle
- Maximum braking
- Spoilers deployed automatically

## CAOS Integration

- Real-time takeoff performance calculation
- Runway condition assessment
- Wind component analysis
- V-speed computation
- Takeoff thrust optimization
- Rejected takeoff decision support

## Compliance

- CS-25.105: Takeoff
- CS-25.107: Takeoff speeds
- CS-25.109: Accelerate-stop distance
- CS-25.111: Takeoff path
- CS-25.113: Takeoff distance and takeoff run

## Related Requirements

- RQ-02-10-20-001: MTOW Specification
- RQ-02-10-10-002: Ground Clearances
- RQ-02-10-40-005: Landing Distance

---

**Document Control:**
- Version: 1.0
- Status: Approved
- Last Updated: 2025-11-05
- Approved By: Flight Test Engineer
