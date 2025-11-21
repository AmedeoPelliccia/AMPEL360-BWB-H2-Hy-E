# 85-00-02-005 Passenger Evacuation and Rescue Safety Interfaces

## Document Information
- **Document ID**: 85-00-02-005
- **Title**: Passenger Evacuation and Rescue Safety Interfaces
- **Version**: 1.0
- **Status**: Draft
- **Last Updated**: 2025-11-21

## Purpose

This document details safety aspects of **evacuation and rescue** interfaces between the AMPEL360 BWB H₂ Hy-E aircraft and airport rescue infrastructure. It establishes requirements for exit integration, ARFF coordination, situational awareness, communication, and joint emergency response.

## Scope

This document covers:
- **BWB exit integration**: Door/slide positioning compatible with airport rescue equipment
- **ARFF coordination**: Procedures for joint emergency response with Airport Rescue and Fire Fighting
- **Situational awareness systems**: Real-time status sharing between aircraft and control room
- **Communication protocols**: Emergency voice and data channels
- **Joint drills and exercises**: Validation of evacuation performance
- **Rescue access requirements**: Stand design for ARFF vehicle positioning

## BWB Exit Integration Challenges

### Unique BWB Geometry

The Blended Wing Body configuration presents unique evacuation challenges:

**Wide Fuselage** (~70 m span):
- Requires **distributed exits** across entire width (cannot concentrate exits on narrow fuselage sides like conventional aircraft)
- Longer evacuation distances for passengers seated mid-span
- Multiple exit types required (Type A, Type I, overwing exits)

**Low Ground Clearance** (~2-3 m at wing leading edge):
- Limits slide deployment angles and lengths
- May require specialized rescue equipment for underwing access
- Ground support required for some exit types (stairs, platforms)

**Unconventional Exit Positions**:
- Forward exits on nose section (conventional position)
- **Mid-fuselage exits**: On top surface or wing leading edge (non-standard)
- Aft exits on tail section
- **Overwing exits**: Low to ground, may require step-down platforms

### Exit Compatibility with Airport Infrastructure

| **Exit Type** | **BWB Positions** | **Airport Equipment Compatibility** | **Special Requirements** |
|---------------|-------------------|-------------------------------------|-------------------------|
| Type A (forward main doors) | Nose section (2-3 exits per side) | Standard passenger boarding bridges, mobile stairs | None (conventional) |
| Type I (mid-fuselage doors) | Wing root area (2-4 exits per side) | May require custom bridge adapters or stairs | Height: 2.5-3.5 m AGL |
| Overwing exits | Wing leading edge (4-6 exits) | Low-profile platforms, ARFF ladder access | Height: 2-3 m AGL, width clearance |
| Aft exits | Tail section (1-2 exits per side) | Standard stairs or mobile platforms | Height: 3-4 m AGL |
| Ventral exits (emergency only) | Fuselage belly (optional) | Ground-level access, may require belly-up approach | Special training for ARFF |

**Stand Design Considerations**:
- Boarding bridges must **not interfere** with rescue access lanes (see [85-00-02-003](85-00-02-003_Safety_Zones_and_Separation_Criteria.md))
- Slide deployment zones must be **clear of GSE** and energy equipment at all times
- ARFF equipment (ladder trucks, platforms) must reach all exits within **3 minutes**

## ARFF Coordination Requirements

### Pre-Arrival Coordination

**Flight Approach Phase** (aircraft en route to airport):
- **Emergency declaration**: Flight crew notifies ATC, ATC alerts ARFF
- **Aircraft status**: Crew provides passenger count, nature of emergency, exit availability
- **ARFF positioning**: ARFF pre-positions vehicles based on expected runway/taxiway and anticipated stand

### On-Stand Emergency Coordination

**Emergency Declaration on Stand**:
1. **Aircraft crew**: Activates emergency alert (visual + data signal to control room)
2. **Control room**: Receives alert with aircraft ID, stand, nature of emergency
3. **ARFF dispatch**: Automatic mobilization, vehicles en route within **90 seconds**
4. **Ground supervisor**: Establishes command post, coordinates with aircraft and ARFF

**Roles and Responsibilities**:

| **Role** | **Organization** | **Responsibilities** |
|----------|------------------|---------------------|
| Aircraft Commander | Flight Crew | Declare emergency, initiate evacuation, command aircraft response |
| ARFF Incident Commander | Airport ARFF | Command external rescue, fire suppression, medical response |
| Ground Supervisor | Airport Ground Ops | Coordinate GSE, evacuate non-essential personnel, support ARFF |
| OCC Duty Manager | Airport Operations | Overall airport response coordination, liaise with authorities |
| Control Room Operator | Airport Operations | Monitor situational awareness systems, relay information |

**Unified Command**: For major emergencies (e.g., fire with evacuation), Aircraft Commander and ARFF Incident Commander establish **unified command** at safe location near aircraft.

### Communication Systems

#### Primary Voice Communication

**VHF Radio** (Aeronautical Mobile Service):
- **Frequency**: Dedicated emergency frequency or tower frequency
- **Participants**: Flight crew, ARFF, ground supervisor, control room
- **Limitations**: Single channel, potential congestion during complex emergencies

#### Secondary Communication

**Landline/Cellular**:
- **Direct line**: Cockpit to control room (via satellite or ground cellular)
- **ARFF commander radio**: Trunked radio system, multiple channels
- **Backup**: Handheld radios distributed to key personnel on stand

#### Data Communication

**Aircraft Emergency Status Data Link**:
- **Parameters**: Exit availability, fire detection status, H₂/CO₂ system status, passenger count
- **Update rate**: Change-of-state (immediate) + periodic (every 10 seconds)
- **Display**: Control room safety dashboard, ARFF mobile command unit

**Stand Safety Status**:
- **Parameters**: GSE positions, energy interface status (H₂/CO₂), weather (wind, visibility)
- **Update rate**: Continuous (1 Hz)
- **Purpose**: Enable ARFF to assess hazards before approaching aircraft

### Rescue Access During Emergency

**ARFF Vehicle Positioning** (based on emergency type):

**Fire Emergency**:
- **Upwind side**: Primary ARFF vehicles position upwind to avoid smoke
- **Downwind side**: Secondary vehicles for rescue from downwind exits if needed
- **Foam/water application**: From safe distance (10-15 m), prioritize fire suppression before rescue entry

**Non-Fire Evacuation** (medical, security, precautionary):
- **Multiple sides**: ARFF vehicles at forward, mid, and aft positions (both sides if possible)
- **Priority**: Exits with highest passenger flow (forward Type A doors typically)
- **Mobile stairs**: Deploy to supplement slides for elderly/disabled passengers

**Slide Deployment Coordination**:
- **Flight crew**: Commands slide deployment (armed mode → inflate on door opening)
- **ARFF**: Monitors slide inflation, positions personnel at slide base to assist passengers
- **Obstructions**: If slide cannot deploy (blocked by GSE or energy equipment) → ARFF provides alternative (stairs, ladder)

## Shared Situational Awareness Systems

### Aircraft Emergency Status Display

**Control Room Dashboard**:
- **Stand map**: Real-time aircraft position, exit positions, ARFF vehicle positions
- **Exit status**: Available (green), blocked/inoperative (red), deploying slide (yellow)
- **Fire detection**: Location of fire alarms (if any), fire suppression status
- **H₂/CO₂ status**: Interface status (safe to approach or hazard present)
- **Passenger count**: Estimated remaining on board (based on boarding data minus evacuation sensors)

**ARFF Mobile Command Unit**:
- **Tablet/ruggedized display**: Subset of control room data, optimized for field use
- **Focus**: Exit status, hazards, vehicle positioning
- **Update**: Real-time via wireless data link (LTE or airport Wi-Fi)

### Exit Availability Sensors

**Automatic Detection**:
- **Door position sensors**: Open/closed status
- **Slide deployment sensors**: Slide inflated/deflated, inflation pressure
- **Exit blocked sensors**: Optical or pressure sensors detect obstructions
- **Passenger flow sensors**: Infrared or camera-based detection of passengers exiting

**Data Transmission**:
- Exit availability data transmitted to control room and ARFF via aircraft data link
- Change-of-state updates (immediate) when exit opens, slide deploys, or passenger flow begins

### Rescue Progress Tracking

**Passenger Accountability**:
- **Boarding data**: Initial passenger count from boarding pass scans
- **Exit sensors**: Count passengers descending slides or using stairs
- **Estimated remaining**: Real-time calculation of passengers still on board
- **Alarm**: Alert if evacuation stalls (no passenger movement for >30 seconds at active exit)

**ARFF Reporting**:
- ARFF reports "all clear" for each aircraft section after search (forward, mid, aft)
- Control room tracks progress and alerts if any section not reported within expected time

## Joint Drills and Evacuation Performance Testing

### Drill Objectives

1. **Validate 90-second evacuation**: Demonstrate compliance with [EASA CS-25.803](https://www.easa.europa.eu/)
2. **Exercise ARFF response**: Verify vehicles can reach all exits within 3 minutes
3. **Test communication**: Validate voice and data links under simulated emergency conditions
4. **Identify obstructions**: Detect any GSE, energy equipment, or stand features that impede rescue
5. **Train personnel**: Practice coordination between flight crew, ARFF, ground staff

### Drill Frequency

- **Full-scale evacuation drill**: Annually (required for aircraft type certification)
- **Desktop exercise** (tabletop simulation): Quarterly (all stakeholders)
- **ARFF familiarization**: Twice annually (hands-on with BWB mockup or aircraft)
- **New airport introduction**: Full drill before first revenue service at new station

### Drill Scenarios

#### Scenario 1: Fire on Stand with Evacuation

**Setup**:
- Simulated fire in aft cargo compartment (smoke generator)
- All passengers on board, engines off, H₂ refueling just completed
- Wind from west at 10 knots

**Objectives**:
- Flight crew declares emergency, commands evacuation via forward and mid exits (aft exits unusable due to smoke)
- ARFF mobilizes, approaches from upwind (west), establishes foam curtain to protect evacuating passengers
- Ground supervisor evacuates H₂ refueling crew, secures energy interfaces
- Validate slide deployment and passenger flow (target: <90 seconds for all passengers)

**Success Criteria**:
- All passengers evacuated within 90 seconds
- ARFF on scene within 3 minutes, fire suppression initiated within 5 minutes
- No conflicts between evacuating passengers and ARFF vehicles
- Communication clear and timely

#### Scenario 2: Medical Emergency Requiring Rapid Disembarkation

**Setup**:
- Passenger medical emergency (cardiac arrest), aircraft on stand, passengers on board
- No fire, H₂/CO₂ systems safe

**Objectives**:
- Flight crew requests priority medical access via forward door
- ARFF brings medical team and equipment to aircraft
- Passenger removed on stretcher via forward door and mobile stairs (slides not deployed)
- Normal disembarkation continues for other passengers

**Success Criteria**:
- Medical team on aircraft within 5 minutes of call
- Patient removed within 10 minutes
- No disruption to normal passenger disembarkation

#### Scenario 3: H₂ Leak During Boarding

**Setup**:
- H₂ leak detected during boarding (passengers partially boarded)
- Emergency shutdown of H₂ system, Ex zone established
- Evacuation via exits away from H₂ area

**Objectives**:
- Ground supervisor declares "stand unsafe," halts boarding
- Partially boarded passengers evacuated via forward doors only (no slides, use stairs)
- ARFF monitors H₂ concentration, provides Ex zone enforcement
- H₂ refueling crew secures leak source

**Success Criteria**:
- All passengers and crew evacuated within 5 minutes
- No personnel enter Ex zone (Zone 1, 3 m radius) except trained H₂ crew with Ex-rated equipment
- Leak contained and Ex zone cleared within 20 minutes

### Drill Evaluation and Continuous Improvement

**Post-Drill Debrief**:
- All participants (flight crew, ARFF, ground staff, observers) attend debrief within 24 hours
- **Strengths**: Identify what worked well (e.g., fast ARFF response, good communication)
- **Areas for improvement**: Identify issues (e.g., slide blocked by GSE, ARFF vehicle access delayed)
- **Action items**: Assign corrective actions with responsible parties and deadlines

**Lessons Learned**:
- Document key insights in shared lessons learned database
- Share with other airports operating BWB aircraft
- Update procedures, training, or stand design as needed

## Interface Requirements for Joint Drills

### Aircraft Availability

- **Aircraft or high-fidelity mockup** required for full-scale drills
- Mockup must include: correct exit positions, functional slides (or slide simulators), representative interior layout
- If actual aircraft unavailable, ground-based egress trainer acceptable (e.g., cabin section with exits and slides)

### Stand Configuration

- Drills conducted on **actual operational stand** (not training area) to validate real-world conditions
- All GSE, energy equipment, rescue access lanes configured as they would be during normal operations

### ARFF Equipment

- **Full ARFF response**: Primary and secondary vehicles, foam/water equipment, medical team
- Test equipment compatibility with BWB (e.g., ladder height, boom reach, foam application from safe distance)

### Instrumentation

- **Video recording**: Multiple cameras capture evacuation from different angles (for analysis)
- **Timing**: Precision stopwatches or automated timing systems (based on exit sensors)
- **H₂/CO₂ simulation**: If simulating energy system hazards, use inert gas or instrumented mockup (no actual H₂ or CO₂ for safety)

## Rescue Access Requirements Summary

**From [85-00-02-003_Safety_Zones_and_Separation_Criteria.md](85-00-02-003_Safety_Zones_and_Separation_Criteria.md)**:

- **Access lane widths**: ≥6 m for primary ARFF vehicles, ≥4 m for support vehicles
- **Clearances around exits**: 10 m forward, 3 m lateral for slide deployment
- **Rescue vehicle positioning**: Within 3 m of fuselage for ladder operations
- **Stand perimeter**: ≥5 m clearance maintained around aircraft for rescue access

**Additional Requirements**:
- **Turning radius**: Stand design must accommodate 15 m turning radius for ARFF vehicles
- **Surface strength**: Stand pavement must support 40-ton ARFF vehicles (fully loaded)
- **Lighting**: Emergency lighting (auto-activate on stand power loss) illuminates all rescue access lanes

## Cross-Reference to ATA 26 and ATA 52

### ATA 26 Fire Protection

Interface safety requirements integrate with:
- **[ATA 26 Fire Protection](../../../../T-TECHNOLOGY_AMEDEOPELLICCIA-ON_BOARD_SYSTEMS/E1-ENVIRONMENT/ATA_26-FIRE_PROTECTION/)**: On-board fire detection, suppression, and crew procedures
- **Fire detection status**: Shared with ARFF via data link (location, severity)
- **Suppression status**: ARFF aware of on-board suppression activation (allows coordination of external/internal efforts)

### ATA 52 Doors

Interface safety requirements integrate with:
- **[ATA 52 Doors](../../../../T-TECHNOLOGY_AMEDEOPELLICCIA-ON_BOARD_SYSTEMS/A-AIRFRAME/ATA_52-DOORS/)**: Door operation, slide arming, emergency exit provisions
- **Exit compatibility**: Door dimensions, slide deployment envelopes, emergency opening forces
- **Airport requirements**: Feedback from airport drills informs door/slide design changes

## Related Documents

- [85-00-02-001_Safety_Concepts_and_Objectives.md](85-00-02-001_Safety_Concepts_and_Objectives.md) - Safety objectives
- [85-00-02-002_Hazard_Analysis_at_Interface_Level.md](85-00-02-002_Hazard_Analysis_at_Interface_Level.md) - Evacuation hazards
- [85-00-02-003_Safety_Zones_and_Separation_Criteria.md](85-00-02-003_Safety_Zones_and_Separation_Criteria.md) - Rescue access lanes
- [85-00-02-006_Operational_Safety_Procedures_at_Interfaces.md](85-00-02-006_Operational_Safety_Procedures_at_Interfaces.md) - Emergency procedures
- [ASSETS/85-00-02-A-004_Evacuation_and_Rescue_Scenarios.svg](ASSETS/85-00-02-A-004_Evacuation_and_Rescue_Scenarios.svg) - Scenario diagrams
- [ATA 26 Fire Protection](../../../../T-TECHNOLOGY_AMEDEOPELLICCIA-ON_BOARD_SYSTEMS/E1-ENVIRONMENT/ATA_26-FIRE_PROTECTION/)
- [ATA 52 Doors](../../../../T-TECHNOLOGY_AMEDEOPELLICCIA-ON_BOARD_SYSTEMS/A-AIRFRAME/ATA_52-DOORS/)

## References

- **[EASA CS-25.803](https://www.easa.europa.eu/)**: Emergency evacuation
- **[EASA CS-25.807](https://www.easa.europa.eu/)**: Emergency exits
- **[EASA CS-25.809](https://www.easa.europa.eu/)**: Emergency exit arrangement
- **[ICAO Annex 14](https://www.icao.int/safety/pages/annex-14.aspx)**: Aerodromes — Volume I: Aerodrome Design and Operations
- **ICAO Doc 9137**: Airport Services Manual (Part 1: Rescue and Fire Fighting)
- **IATA Airport Handling Manual (AHM)**: Section on Emergency Response

## Document Control

- **Owner**: AMPEL360 Safety & Certification Team
- **Approver**: Chief Safety Officer
- **Review Frequency**: Quarterly
- **Next Review**: 2026-02-21
- **Repository**: AMPEL360-BWB-H2-Hy-E
- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**
- Status: **DRAFT** – Subject to human review and approval
- Human approver: _[to be completed]_
- Last AI update: 2025-11-21

---
*This document is part of the AMPEL360 OPT-IN Framework certification package.*
