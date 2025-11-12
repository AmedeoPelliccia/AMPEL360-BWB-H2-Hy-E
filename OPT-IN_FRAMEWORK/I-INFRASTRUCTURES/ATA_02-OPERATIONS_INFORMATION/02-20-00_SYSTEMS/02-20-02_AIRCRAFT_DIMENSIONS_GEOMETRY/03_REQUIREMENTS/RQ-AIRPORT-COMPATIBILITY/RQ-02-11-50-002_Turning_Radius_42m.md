# RQ-02-11-50-002: Turning Radius Requirements

**Priority:** High  
**Status:** Approved  
**Version:** 1.0.0

## Requirement Statement

The aircraft shall achieve a minimum turning radius of 42 meters (measured from center of turn to outer wingtip) during ground maneuvering with nose wheel steering at maximum deflection.

## Rationale

**Airport Compatibility:**
- Enables 180° turns on standard taxiways
- Gate and ramp maneuvering capability
- Turnaround procedures
- Emergency evacuation area access

**Taxiway Operations:**
- Taxiway intersection negotiation
- Holding bay access
- Runway exit maneuvering
- Parking position entry/exit

**Design Considerations:**
- Nose wheel steering angle: ±70° maximum
- Main gear caster angle
- Wheelbase: 15.5m
- Main gear track: 12.0m

## Turning Radius Calculation

**Geometric Analysis:**
```
Turning radius components:
- Nose wheel steering: 70° max deflection
- Wheelbase: 15.5m
- Half-span: 26.0m

Minimum turning radius (to outer wingtip):
R = √[(wheelbase/tan(steering_angle))² + half_span²]
R = √[(15.5/tan(70°))² + 26.0²]
R ≈ 42m
```

**Turn Performance:**
- Inner wingtip radius: ~16m
- Outer wingtip radius: ~42m
- Main gear path radius: ~28m
- Nose gear path radius: ~5.6m

## Verification Method

**Analysis:**
- Kinematic simulation
- CAD model verification
- Multiple turn scenarios
- Clearance margin analysis

**Ground Testing:**
- Maximum deflection turns
- Pavement marking validation
- Wingtip clearance monitoring
- Nose wheel steering load testing

**Acceptance Criteria:**
- Turning radius ≤ 42m to outer wingtip
- Nose wheel steering ±70° achievable
- No tire scrubbing issues
- Pavement stress acceptable

## Operational Procedures

**Normal Turns:**
- Progressive steering input
- Speed: 5-10 kt maximum
- Monitor wingtip clearance
- CAOS turn assist active

**Restricted Maneuvering:**
- Tight ramp areas: Wing walkers required
- Low visibility: Enhanced procedures
- Wet/icy conditions: Reduced steering angles
- Heavy weight: Steering load limitations

## Airport Infrastructure

**Taxiway Design:**
- Intersection fillets sized for 42m radius
- Holding bay design accommodates radius
- Runway exit design verified
- Gate approach paths validated

**Pavement Requirements:**
- Turning loads on pavement
- Edge loading considerations
- Multiple turn cycles
- Maintenance implications

## Compliance

**Standards:**
- [ICAO Annex 14](https://www.icao.int/safety/pages/annex-14.aspx) (Taxiway design)
- [FAA AC 150/5300-13A](https://www.faa.gov/airports/resources/advisory_circulars/)
- [CS-25](https://www.easa.europa.eu/en/document-library/certification-specifications/cs-25-amendment-27) (Ground handling)

**Related Requirements:**
- [RQ-02-11-50-001](RQ-02-11-50-001_Taxiway_Width_23m_Min.md) (Taxiway Width)
- [RQ-02-11-30-001](../RQ-CLEARANCES/RQ-02-11-30-001_Wingtip_Clearance_1.2m_Min.md) (Wingtip Clearance)
- [RQ-02-11-10-001](../RQ-DIMENSIONS/RQ-02-11-10-001_Wingspan_52m.md) (Wingspan)
- Landing gear design requirements
