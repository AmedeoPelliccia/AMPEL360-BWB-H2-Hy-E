# ICD-02-10-52-001: Door Locations Interface

**From:** ATA 02-10 Aircraft General Data  
**To:** ATA 52 Doors

**ICD ID:** ICD-02-10-52-001  
**Version:** 1.0  
**Date:** 2025-11-05  
**Status:** Active

## Purpose

This Interface Control Document defines the locations, dimensions, and operational parameters of all aircraft doors for ground operations, emergency egress, and certification compliance.

## Data Exchange

### Door Location Specifications

**Provided by ATA 02-10:**

#### Passenger Entry Doors

**Door L1 (Forward Left Entry):**
- Type: Type A passenger door
- Location: Station 10.5 m, -6.2 m BL
- Sill height: 4.2 m above ground
- Opening: 1.07 m wide × 1.83 m high
- Capacity: 110 passengers/90 seconds

**Door R1 (Forward Right Entry):**
- Type: Type A passenger door
- Location: Station 10.5 m, +6.2 m BL
- Sill height: 4.2 m above ground
- Opening: 1.07 m wide × 1.83 m high
- Capacity: 110 passengers/90 seconds

#### Emergency Exits

**Door L3 (Aft Left Emergency):**
- Type: Type III emergency exit
- Location: Station 45.0 m, -5.8 m BL
- Sill height: 3.8 m above ground
- Opening: 0.51 m wide × 1.07 m high
- Capacity: 55 passengers/90 seconds

**Door R3 (Aft Right Emergency):**
- Type: Type III emergency exit
- Location: Station 45.0 m, +5.8 m BL
- Sill height: 3.8 m above ground
- Opening: 0.51 m wide × 1.07 m high
- Capacity: 55 passengers/90 seconds

#### Service Doors

**Cargo Door (Forward):**
- Type: Class B cargo door
- Location: Station 6.0 m, -7.5 m BL
- Sill height: 2.8 m above ground
- Opening: 1.83 m wide × 1.42 m high

**Cargo Door (Aft):**
- Type: Class B cargo door
- Location: Station 48.0 m, -7.5 m BL
- Sill height: 2.8 m above ground
- Opening: 1.83 m wide × 1.42 m high

**Data Format:** Door location drawings and specification tables  
**Update Frequency:** Static (certified configuration)  
**Criticality:** High

## BWB Configuration Impact

**Unique BWB Considerations:**
- Wide fuselage enables multiple door locations
- Floor-level variations due to BWB shape
- Extended cabin length requires strategic exit placement
- Ground service equipment compatibility

**Emergency Egress Analysis:**
- Total capacity: 330 passengers/90 seconds (exceeds 220 pax requirement)
- Exit distribution meets 60 ft maximum spacing
- Dual-lane evacuation capability
- All exits accessible with 25° list

## Ground Service Interface

**Door Compatibility:**
- Passenger boarding bridges: L1, R1 doors
- Air stairs: All passenger doors
- Ground service: Cargo doors
- Emergency slides: L1, R1, L3, R3

**GSE Requirements:**
- L1/R1: Standard airport jetway, height 4.2 m
- L3/R3: Portable stairs or integrated slides
- Cargo: Scissor lift or elevated loader, height 2.8 m

## Operational Parameters

**Door Operating Times:**
- Passenger doors (power): 8-12 seconds
- Passenger doors (manual): 15-20 seconds
- Emergency exits (manual): 3-5 seconds
- Cargo doors (power): 15-20 seconds

**Environmental Conditions:**
- Operating temperature: -40°C to +52°C
- Wind limit (opening): 65 knots
- Ice/snow operation: De-icing required
- Rain operation: No restriction

## Safety Requirements

**Emergency Egress:**
- All exits meet CS-25.807 requirements
- Evacuation demonstration: 90 seconds
- Night egress lighting provided
- Escape slide deployment: 6-10 seconds

**Door Status Indication:**
- Flight deck indication: All doors
- Door interlock with pressurization
- Warning before takeoff if not secure
- CAOS monitoring of door status

## Dependencies

- Fuselage structure (ATA 53)
- Emergency escape slides (ATA 25)
- Ground service equipment (ATA 03)
- Cabin configuration (ATA 25)
- CAOS monitoring system (ATA 95)

## Responsibilities

**ATA 02-10 (Provider):**
- Define door locations and quantities
- Specify egress requirements
- Coordinate with airport operations

**ATA 52 (Consumer):**
- Design and install door systems
- Ensure operational compliance
- Maintain door integrity and function
- Integrate with slides and GSE

## Change Control

Door location or specification changes require:
1. Emergency egress reanalysis
2. Evacuation demonstration (if significant)
3. Ground operations compatibility check
4. Regulatory authority approval
5. Airport facility notification

## Certification Compliance

**CS-25 Requirements:**
- §25.783: Doors
- §25.807: Emergency exits
- §25.809: Emergency exit arrangement
- §25.810: Emergency egress assist means
- §25.813: Emergency exit access

## References

- EASA CS-25 Subpart D: Design and Construction
- FAA AC 25.783-1A: Doors
- SAE ARP4120: Recommended Evacuation Capabilities

---

**Document Control:**
- Version: 1.0
- Status: Active
- Last Updated: 2025-11-05
- Review Cycle: Per modification only
