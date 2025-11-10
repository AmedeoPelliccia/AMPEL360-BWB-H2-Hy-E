# RQ-02-11-30-005: Ground Attitude Limits

**Priority:** Critical  
**Status:** Approved  
**Version:** 1.0.0

## Requirement Statement

The aircraft ground attitude limits shall be defined and enforced to prevent structural contact with the ground during all normal and abnormal ground operations, including taxi, takeoff, and landing.

## Ground Attitude Definitions

**Level Attitude:**
- Reference: Waterline system parallel to ground
- Pitch angle: 0° ±0.5°
- Roll angle: 0° ±1.0°
- Standard measurement condition

**Maximum Nose-Up (Rotation):**
- Pitch angle: 12° maximum
- Tail clearance: ≥0.3m minimum
- Normal rotation rate: 3°/sec
- Maximum rotation rate: 5°/sec

**Maximum Nose-Down:**
- Pitch angle: -3° maximum (nose down)
- Wingtip clearance maintained
- Brake application limit
- Nose gear load limits

**Maximum Bank Angle:**
- Roll angle: ±5° maximum (ground ops)
- Wingtip clearance: ≥0.8m minimum
- Crosswind landing limit
- Taxiway banking consideration

## Rationale

**Safety Limits:**
- Prevent tail strike during rotation
- Prevent wingtip strike in crosswind
- Maintain structural clearances
- Enable safe ground maneuvering

**Operational Envelope:**
- Normal operations: Conservative limits
- Emergency operations: Extended limits
- Pilot training scenarios
- Ground handling procedures

## Monitoring and Protection

**CAOS Ground Monitoring:**
- Real-time attitude calculation
- Inertial measurement unit (IMU) input
- Ground clearance estimation
- Predictive warning system

**Crew Alerting:**
- Advisory: Yellow caution at 80% of limit
- Warning: Red warning at 95% of limit
- Aural warning for critical conditions
- Override capability (with acknowledgment)

## Verification Method

**Analysis:**
- Geometric model validation
- Clearance calculations
- Loading condition effects
- Dynamic simulation

**Testing:**
- Ground rotation tests
- Crosswind landing tests
- Maximum bank angle validation
- Tail strike protection verification

**Acceptance Criteria:**
- All limits validated by test
- Monitoring system functional
- Crew procedures approved
- Training program complete

## Operational Procedures

**Normal Operations:**
- Standard rotation technique
- Crosswind landing procedures
- Taxiway turn limits
- Parking attitude verification

**Abnormal Operations:**
- Overweight landing procedures
- Single engine operations
- Asymmetric loading conditions
- Emergency maneuvers

## Compliance

**Regulatory:**
- [CS-25.231](https://www.easa.europa.eu/en/document-library/certification-specifications/cs-25-amendment-27) (Ground clearance)
- [CS-25.107](https://www.easa.europa.eu/en/document-library/certification-specifications/cs-25-amendment-27) (Takeoff)
- [CS-25.125](https://www.easa.europa.eu/en/document-library/certification-specifications/cs-25-amendment-27) (Landing)
- [CS-25.237](https://www.easa.europa.eu/en/document-library/certification-specifications/cs-25-amendment-27) (Wind velocities)

**Related Requirements:**
- [RQ-02-11-30-001](RQ-02-11-30-001_Wingtip_Clearance_1.2m_Min.md) (Wingtip Clearance)
- [RQ-02-11-30-002](RQ-02-11-30-002_Belly_Clearance_1.8m_Min.md) (Belly Clearance)
- [RQ-02-11-30-003](RQ-02-11-30-003_Tail_Clearance_2.5m_Min.md) (Tail Clearance)
