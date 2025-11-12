# RQ-02-10-60-004: Dispatch Requirements

**Requirement ID:** RQ-02-10-60-004  
**Category:** Operational  
**Priority:** High  
**Status:** Approved

## Requirement

The aircraft dispatch process shall ensure airworthiness, regulatory compliance, and operational safety through comprehensive pre-flight checks, documentation, and decision-making procedures.

## Minimum Equipment List (MEL)

**MEL Structure:**
- Category A: Immediate rectification required
- Category B: Rectification within 3 days
- Category C: Rectification within 10 days
- Category D: Rectification within 120 days

**H₂-Specific MEL Items:**
- H₂ leak detection: Category A
- H₂ tank pressure monitoring: Category A
- Fuel cell stacks: 2 operative minimum (Category A)
- H₂ quantity indication: Category B

**CAOS MEL Items:**
- Digital twin sync: Category C
- Predictive maintenance: Category C
- Performance optimization: Category D
- Decision support: Category D

## Configuration Deviation List (CDL)

**Permitted Missing Items:**
- Wing tips (must be structurally faired)
- Cargo door fairings
- Antenna fairings (specific antennas)
- **Not permitted:** Any H₂ system component

## Pre-Flight Inspection

**Flight Crew Responsibilities:**

1. **Documentation Review (15 min)**
   - Aircraft technical log
   - MEL/CDL items
   - NOTAMs and weather
   - Weight and balance
   - Fuel (H₂) availability
   - CAOS pre-flight report

2. **External Walk-Around (20 min)**
   - General condition
   - H₂ tanks and connections (visual)
   - Landing gear and tires
   - Control surfaces
   - Lights and antennas
   - Ground connection points
   - H₂ leak detection check (portable detector)

3. **Cockpit Preparation (15 min)**
   - Preflight checks per checklist
   - CAOS system initialization
   - Flight plan review
   - Performance calculations
   - Briefing (crew and passengers)

## Airworthiness Release

**Required Sign-Offs:**
- Maintenance: Certificate of Release to Service (CRS)
- Flight Crew: Pre-flight inspection complete
- Dispatcher: Flight release (if applicable)
- Refueling: H₂ refueling certificate

**Additional H₂ Requirements:**
- H₂ leak check negative (last 6 hours)
- H₂ tank pressure within limits
- Boil-off rate acceptable
- Ground safety zone observed

## Fuel (H₂) Dispatch Requirements

**Minimum Fuel:**
1. Taxi fuel
2. Trip fuel
3. Contingency fuel (5% or 5 minutes, whichever greater)
4. Alternate fuel (if required)
5. Final reserve (45 minutes holding at 1,500 ft AGL)
6. Additional fuel (if required by captain or dispatcher)

**H₂-Specific Considerations:**
- Boil-off allowance (0.3% per hour ground time)
- Tank pressure loss allowance
- Temperature effects on fuel availability
- Alternate airport H₂ availability

## Weather Minimums

**Takeoff Minimums:**
- Standard: RVR 550m (or equivalent visibility)
- Reduced: Per operator's approval and aircraft equipment
- H₂ operations: Dry runway preferred, contaminated approved with limitations

**Destination and Alternate:**
- Forecast must meet requirements at ETA
- Alternate required unless:
  - Destination has two usable runways
  - Weather forecast: ceiling 2,000 ft, visibility 5 km
  - Period: ETA -1 hour to +1 hour
- Alternate must have H₂ refueling (for H₂ aircraft)

## NOTAM Requirements

**Essential NOTAMs:**
- Runway conditions
- Navigation aid status
- H₂ refueling facility status
- Airspace restrictions
- Airport facilities

**H₂-Specific NOTAMs:**
- H₂ refueling availability at destination and alternates
- H₂ ground support equipment availability
- H₂ emergency response capability
- Special H₂ handling procedures

## Performance Dispatch

**Required Calculations:**
- Takeoff performance (TODR, V-speeds)
- En-route performance (climb, cruise, descent)
- Landing performance (LDR, VREF)
- Go-around performance

**CAOS Support:**
- Real-time performance calculation
- Runway condition assessment
- Optimal altitude and speed
- Fuel burn prediction

**Limitations:**
- Performance must meet regulatory requirements
- Conservative assumptions for degraded conditions
- Crew must verify CAOS calculations

## Communication Requirements

**Required Communications:**
- VHF radio: 2 operative
- HF radio: For oceanic operations
- SATCOM: For ETOPS operations
- ACARS/Datalink: Preferred for operations

## Special Operations Dispatch

**ETOPS Dispatch:**
- ETOPS maintenance program current
- ETOPS MEL items complied with
- Weather at ETOPS alternates suitable
- H₂ fuel adequate for diversion
- CAOS predictive maintenance clear

**Low Visibility Operations:**
- Aircraft equipment serviceable per OpSpec
- Crew qualified and current
- Runway equipment operative (ILS, lights)
- Weather forecast suitable

## Emergency Equipment

**Required on Every Flight:**
- Life vests: All occupants
- Emergency locator transmitter (ELT)
- Fire extinguishers: 6 minimum
- First aid kits: 3 minimum
- Megaphone or PA system
- Emergency lighting
- Crash axe

**Additional for Extended Overwater:**
- Life rafts: Capacity for all occupants
- Survival equipment
- Pyrotechnic signaling devices

## Passenger Briefing

**Standard Briefing:**
- Seatbelts and emergency exits
- Smoking prohibition
- Portable electronic devices
- Life vest location and use

**H₂-Specific Briefing (if required):**
- H₂ safety measures (no smoking, no open flames)
- Emergency evacuation procedures
- Unusual odors reporting (H₂ is odorless, but additive may be used)

## Dispatch Authority

**Captain's Authority:**
- Final authority on airworthiness
- Can refuse aircraft for any safety concern
- Can add fuel, reduce payload, or cancel flight
- Can override CAOS recommendations

**Dispatcher Authority (if applicable):**
- Joint responsibility with captain for dispatch
- Provides operational control and support
- Can recommend delay or cancellation
- Monitors flight progress

## Operational Flight Plan (OFP)

**Required Contents:**
- Aircraft identification and type
- Departure, destination, alternates
- Route and altitudes
- Fuel (H₂) plan
- Weather forecasts and NOTAMs
- Performance calculations
- ETOPS information (if applicable)
- CAOS optimization recommendations

**CAOS-Generated Supplements:**
- Predictive maintenance status
- Optimal cruise profile
- Fuel-saving recommendations
- Real-time performance update schedule

## Technical Delays and Cancellations

**Decision Process:**
1. Identify issue (crew, maintenance, CAOS)
2. Consult MEL/CDL
3. Assess operational impact
4. Consider repair vs. delay vs. cancel
5. Make dispatch decision

**CAOS Support:**
- Predicted maintenance times
- Alternative aircraft availability
- Schedule impact assessment
- Automatic rebooking recommendations (future capability)

## Record Keeping

**Required Records:**
- Flight release document
- Weight and balance manifest
- Fuel (H₂) receipt
- Technical log entries
- MEL/CDL references
- NOTAM briefing
- Weather briefing
- CAOS pre-flight report

**Retention:**
- Operational records: 3 months minimum
- Technical records: Per regulatory requirements
- CAOS logs: 12 months (anonymized data indefinitely)

## Rationale

Dispatch requirements ensure:
- Regulatory compliance
- Airworthiness verification
- Safe flight operations
- Crew and passenger safety
- Efficient operations
- H₂ system safety
- CAOS integration

## Verification

- **Method:** Documentation Review and Audit
- **Procedure:**
  - Operations Manual approval
  - Dispatch procedures audit
  - Sample dispatch reviews
- **Acceptance Criteria:**
  - Procedures approved by authority
  - Compliance rate > 99.5%
  - No safety incidents due to dispatch errors

## Compliance

- EASA Part-OPS: Commercial Air Transport Operations
- CS-25.1581: General operating and flight information
- ICAO Annex 6 Part I: Commercial Air Transport Operations
- Operator's Operations Manual
- Operator's Minimum Equipment List

## Related Requirements

- RQ-02-10-60-001: Crew Requirements
- RQ-02-10-60-002: Certification Basis
- RQ-02-10-60-003: Operational Limitations
- RQ-02-10-50-002: H2 System Specs
- RQ-02-10-50-003: CAOS Integration

---

**Document Control:**
- Version: 1.0
- Status: Approved
- Last Updated: 2025-11-05
- Approved By: Director of Flight Operations
