# RQ-02-11-30-003: Tail Ground Clearance

**Priority:** Critical  
**Status:** Approved  
**Version:** 1.0.0

## Requirement Statement

The minimum tail ground clearance shall be 2.5 meters at Maximum Landing Weight (MLW) with landing gear extended in level attitude, providing adequate margin for rotation during takeoff and landing flare.

## Rationale

**Rotation Clearance:**
- Takeoff rotation angle: 12° maximum
- Landing flare attitude: 10° maximum
- Safety margin: 0.5m minimum
- Prevents tail strike during normal operations

**BWB Configuration:**
- Aft body extends behind main gear
- Lower tail height than conventional aircraft
- Enhanced rotation monitoring required
- Tail strike protection system

**Operational Requirements:**
- Adequate pitch authority for takeoff
- Landing flare capability
- Rejected takeoff deceleration
- Crosswind landing technique

## Critical Conditions

**Takeoff:**
- Rotation at VR (rotation speed)
- Maximum nose-up pitch: 12°
- Tail clearance at liftoff: >0.5m
- Normal rotation rate: 3°/second

**Landing:**
- Flare maneuver: 10° nose-up maximum
- Touchdown attitude: 5-7° typical
- Tail clearance at touchdown: >1.0m
- Hard landing cases considered

## Verification Method

**Static Test:**
- MLW configuration
- Level attitude measurement
- Tail position verification
- Ground contact point identification

**Dynamic Testing:**
- Rotation tests with strain gauges
- Pitch angle vs. clearance correlation
- Tail bumper contact tests (if equipped)
- Flight test validation

**Acceptance Criteria:**
- Static clearance ≥ 2.5m ±0.05m
- Clearance at 12° pitch ≥ 0.3m
- No contact in normal operations
- Tail strike warning system functional

## Tail Strike Protection

**Design Features:**
- Tail bumper/skid (if applicable)
- Reinforced structure at contact zone
- Energy absorption provisions
- Damage-tolerant design

**Monitoring Systems:**
- CAOS pitch attitude monitoring
- Tail clearance calculation
- Crew warning at 1.0m clearance
- Crew caution at 1.5m clearance

## Compliance

**Regulatory:**
- [CS-25.231](https://www.easa.europa.eu/en/document-library/certification-specifications/cs-25-amendment-27) (Ground clearance)
- [CS-25.107](https://www.easa.europa.eu/en/document-library/certification-specifications/cs-25-amendment-27) (Takeoff performance)
- [CS-25.125](https://www.easa.europa.eu/en/document-library/certification-specifications/cs-25-amendment-27) (Landing)

**Related Requirements:**
- [RQ-02-11-30-002](RQ-02-11-30-002_Belly_Clearance_1.8m_Min.md) (Belly Clearance)
- [RQ-02-11-30-005](RQ-02-11-30-005_Ground_Attitude_Limits.md) (Ground Attitude Limits)
- [RQ-02-11-10-003](../RQ-DIMENSIONS/RQ-02-11-10-003_Overall_Height_14.5m.md) (Overall Height)
