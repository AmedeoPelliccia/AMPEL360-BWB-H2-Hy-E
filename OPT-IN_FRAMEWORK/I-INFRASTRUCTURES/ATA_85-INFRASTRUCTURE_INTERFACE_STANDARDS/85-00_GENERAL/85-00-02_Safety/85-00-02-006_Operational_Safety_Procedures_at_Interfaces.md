# 85-00-02-006 Operational Safety Procedures at Interfaces

## Document Information
- **Document ID**: 85-00-02-006
- **Title**: Operational Safety Procedures at Interfaces
- **Version**: 1.0
- **Status**: Draft
- **Last Updated**: 2025-11-21

## Purpose

This document defines **operational safety procedures** at main BWB infrastructure interfaces, including safe sequences for H₂ refueling, CO₂ battery docking/undocking, ground crew coordination, and stand safety state management.

## Scope

This document covers:
- **H₂ refueling procedures**: Pre-refuel checks, connection sequence, monitoring, disconnection
- **CO₂ battery docking procedures**: Pre-docking checks, electrical connection, charging, undocking
- **Ground crew coordination**: Roles, communication, conflict avoidance
- **Stand safety states**: SAFE, RESTRICTED, UNSAFE definitions and transitions
- **Emergency procedures**: Leak response, fire response, evacuation support

## Stand Safety States

### Safety State Definitions

The stand safety state provides a high-level indication of operational status and hazard level:

#### SAFE State (Green)

**Definition**: Normal operations, all interfaces nominal, no active hazards

**Permitted Activities**:
- Passenger boarding/disembarkment
- Catering, cleaning, baggage loading
- Normal GSE operations
- H₂ refueling (with appropriate Ex zone controls)
- CO₂ battery docking/undocking (with thermal management active)

**Requirements**:
- All safety interlocks satisfied
- No active alarms or pre-alarms
- Ex zones established and enforced during H₂ operations
- Rescue access lanes clear
- Weather within limits (wind <30 knots, no lightning within 5 nm)

**Signaling**:
- Green rotating beacon at stand control point
- Control room dashboard shows "SAFE" in green
- Aircraft receives "Stand Safe" status via data link

#### RESTRICTED State (Yellow)

**Definition**: Limited operations due to minor hazard or out-of-limits condition

**Permitted Activities**:
- Essential maintenance only (no passengers)
- GSE operations outside restricted area
- Continued monitoring of degraded system

**Prohibited Activities**:
- Passenger boarding/disembarkment
- Non-essential ground crew on stand
- H₂ refueling or CO₂ battery operations (unless these are the only active systems and source of restriction)

**Example Triggers**:
- H₂ pre-alarm (10-25% LEL) — refueling may continue with enhanced monitoring, but no passengers
- CO₂ battery temperature 50-60°C — charging continues at reduced rate, but stand restricted
- Weather marginal (wind 30-40 knots, lightning 5-10 nm) — suspend passenger operations, secure aircraft
- Rescue access lane partially obstructed — allow limited ops until obstruction cleared

**Signaling**:
- Yellow flashing beacon at stand control point
- Control room dashboard shows "RESTRICTED" in yellow with reason
- Aircraft receives "Stand Restricted" status

**Transition to SAFE**:
- Condition triggering restriction resolved (e.g., H₂ concentration <10% LEL)
- Ground supervisor verifies and declares "Stand Safe"

#### UNSAFE State (Red)

**Definition**: Immediate hazard present, all non-emergency operations suspended

**Permitted Activities**:
- Emergency response only (ARFF, hazmat, emergency maintenance)

**Prohibited Activities**:
- All normal operations
- Passenger or non-essential personnel access to stand

**Example Triggers**:
- H₂ alarm (≥25% LEL) or confirmed leak
- CO₂ battery thermal runaway or fire
- Fire detected on aircraft or ground equipment
- Severe weather (wind >40 knots, lightning strike within 1 nm, tornado warning)
- Structural failure of stand or GSE creating immediate danger
- Security threat

**Signaling**:
- Red flashing beacon at stand control point, audible alarm (siren)
- Control room dashboard shows "UNSAFE" in red with reason
- Aircraft receives "Stand Unsafe" status, ARFF automatically notified

**Transition to SAFE**:
- Hazard eliminated or contained
- ARFF and ground supervisor jointly declare "Stand Safe" after inspection
- May transition through RESTRICTED state if residual monitoring or cleanup required

### Stand Safety State Transition Logic

```
SAFE ←→ RESTRICTED ←→ UNSAFE
  ↑                       ↑
  └───────────────────────┘
   (Direct transition possible
    if hazard rapidly escalates
    or is immediately resolved)
```

**Responsibility**: Ground supervisor declares state changes, logged in control room system.

## H₂ Refueling Operational Procedures

### Pre-Refuel Safety Checks

**Ground Crew** (H₂ technician + safety observer):
1. **Verify stand state**: Confirm stand is SAFE and weather within limits
2. **Aircraft status**: Confirm engines off, APU off, electrical power external only
3. **Establish Ex zone**: Deploy cones/barriers at Zone 1 boundary (3 m radius from connector)
4. **Verify grounding**: Connect bonding cable, verify continuity (<1 Ω resistance)
5. **Inspect connector**: Visual check for damage, contamination, seal condition
6. **Test leak detectors**: Verify all H₂ sensors operational (expose to test gas)
7. **Communication check**: Verify voice and data link to cockpit and control room

**Flight Crew**:
1. **H₂ system status**: Confirm H₂ tank pressure <650 bar (capacity for refueling), temperature normal
2. **Isolate fuel cell**: Fuel cell system isolated from H₂ supply (valve closed)
3. **Vent clear**: Confirm H₂ vent outlets clear of obstructions, wind favorable for dispersion
4. **Refuel authorization**: Provide authorization to ground crew (via data link or intercom)

**Checklist Time**: ~10 minutes (experienced crew), may extend to 15 minutes if issues found

**Abort Criteria**:
- Weather out of limits (wind, lightning)
- Grounding resistance >1 Ω
- H₂ sensor failure
- Connector damage or contamination
- Aircraft H₂ system not ready

### H₂ Connection Sequence

**Step-by-Step** (H₂ technician performs, safety observer monitors):

1. **Position dispenser nozzle**: Align with aircraft receptacle, verify mechanical guides engaged
2. **Connect nozzle** (hand-tight): Insert nozzle, rotate collar clockwise until finger-tight
3. **Verify alignment**: Check visual indicators (green bands visible if aligned correctly)
4. **Torque nozzle**: Apply calibrated torque wrench, tighten to 50 Nm ±5 Nm
5. **Verify lock**: Check mechanical lock indicator (pin extended, green flag visible)
6. **Pressurize connector** (low pressure test): Slowly increase pressure to 50 bar, hold 30 seconds
7. **Leak check**: Technician inspects connector with H₂ leak detector (handheld), observer monitors fixed sensors
8. **Verify seal**: If no leak detected (H₂ <1% LEL at connector), proceed to refueling
9. **Enable data link**: Activate automated monitoring (pressure, temperature, flow to control room)

**Connection Time**: ~5 minutes

**Abort if**:
- Cannot achieve torque (cross-threading or damaged threads)
- Mechanical lock fails to engage
- Leak detected at >1% LEL during low-pressure test

### H₂ Refueling Monitoring

**Automated Monitoring** (every second):
- H₂ flow rate, delivered mass (kg)
- Pressure at dispenser and aircraft tank
- Temperature at connector and tank
- H₂ concentration in Ex zone (all sensors)
- Dead-man switch confirmation (operator presses button every 60 seconds)

**Operator Actions**:
- **Visual observation**: Watch for frost buildup (indicates temperature issue), vapor (indicates leak), unusual sounds
- **Confirm dead-man**: Press confirmation button every 60 seconds (if missed, auto-shutdown)
- **Monitor control panel**: Watch for alarms or pre-alarms on dispenser control unit

**Typical Refueling Time**:
- **Flow rate**: 5-8 kg/min H₂ (limited by thermal management)
- **Tank capacity**: ~200 kg H₂ (typical for long-haul BWB)
- **Refuel time**: 25-40 minutes (depending on initial tank state)

**Normal Completion**:
- Aircraft tank reaches target pressure (typically 700 bar) or target mass (kg)
- Flow rate automatically ramps down to zero over 2 minutes (gradual cool-down)
- Operator confirms refuel complete

### H₂ Disconnection Sequence

**Step-by-Step** (H₂ technician performs, safety observer monitors):

1. **Verify zero flow**: Confirm flow meter reads zero for ≥30 seconds
2. **Close aircraft valve**: Flight crew confirms aircraft inlet valve closed (via data link)
3. **Depressurize hose**: Dispenser vents hose to atmosphere (or recovery system), pressure drops to <10 bar
4. **Wait for thermal stabilization**: Allow 2 minutes for connector to warm to ambient temperature (prevents ice adhesion)
5. **Unlock connector**: Release mechanical lock (push pin, rotate collar)
6. **Disconnect nozzle**: Pull nozzle straight back (no twisting), inspect seal (should be intact, no damage)
7. **Cap aircraft receptacle**: Install protective cap on aircraft H₂ receptacle (prevents contamination, ice buildup)
8. **Stow dispenser nozzle**: Return nozzle to dispenser cradle, verify secure
9. **Disconnect bonding cable**: Remove grounding connection last (prevents static discharge)
10. **Clear Ex zone**: Remove cones/barriers, allow stand to return to unrestricted operations

**Disconnection Time**: ~5 minutes

**Post-Refuel Documentation**:
- Log refuel event: aircraft ID, date/time, delivered mass (kg), start/end pressure, anomalies (if any)
- Crew sign-off: Both technician and observer sign electronic log or paper form

### H₂ Emergency Procedures

#### H₂ Leak During Refueling (≥25% LEL)

**Automatic Actions** (initiated by leak detection system):
1. **Emergency shutdown**: Close valves (dispenser and aircraft), depressurize hose (<3 seconds)
2. **Sound alarm**: Local siren + control room alarm + ARFF notification
3. **Activate ventilation**: Increase forced-air ventilation in Ex zone (if available)

**Operator Actions** (H₂ technician and safety observer):
1. **Evacuate Ex zone**: All personnel move >10 m upwind of leak source (IMMEDIATELY)
2. **Call ARFF**: If not auto-notified, call emergency services (phone or radio)
3. **Monitor from safe distance**: Use handheld H₂ detector to monitor concentration from upwind position
4. **Do NOT attempt repair**: Wait for ARFF or H₂ specialist to assess

**ARFF Actions**:
1. **Approach from upwind**: ARFF vehicles position ≥10 m upwind, monitor H₂ concentration
2. **Establish perimeter**: Expand exclusion zone to 20 m radius (all non-essential personnel)
3. **Assess leak severity**: Use thermal imaging (H₂ leak creates cold spot) and gas detectors
4. **Wait for dispersion**: If leak has stopped (valves closed), monitor until H₂ concentration <10% LEL (typically 5-10 minutes with good ventilation)
5. **Safe to approach**: If leak continues, coordinate with H₂ specialist (may require emergency cap or additional shutdown valves)

**Stand State**: Declare UNSAFE until leak source identified, repaired, and concentration <10% LEL for 5 minutes.

#### Fire at H₂ Interface

**Immediate Actions** (any observer):
1. **Activate alarm**: Pull manual alarm or call emergency services
2. **Evacuate**: All personnel move >20 m from fire source

**Automatic Actions**:
1. **Emergency shutdown**: Close H₂ valves
2. **Notify ARFF**: Automatic alert with location and H₂ hazard flag

**ARFF Actions**:
1. **Approach cautiously**: H₂ fire may be nearly invisible (pale blue flame), use thermal imaging
2. **Do NOT extinguish immediately** (if safe): H₂ jet fire (if leak is burning) is safer than unburned H₂ accumulating → **let burn while closing source**
3. **Cool surroundings**: Apply water spray to adjacent surfaces (aircraft, equipment) to prevent fire spread
4. **Close source**: Coordinate H₂ supply shutdown (may require closing valves upstream of dispenser if local valves damaged)
5. **Extinguish after source closed**: Once H₂ supply stopped, extinguish residual fire with dry chemical or foam

**Stand State**: Declare UNSAFE until fire extinguished and damage assessed.

## CO₂ Battery Docking Operational Procedures

### Pre-Docking Safety Checks

**Ground Crew** (Battery technician + spotter):
1. **Verify stand state**: Confirm stand is SAFE
2. **Container status**: Verify battery container BMS reports "Ready for Dock" (temperature, SOC, no faults)
3. **Thermal management**: Confirm cooling system operational (flow rate, temperature)
4. **Dock status**: Verify electrical contactors open (no voltage at interface), mechanical alignment guides clear
5. **Communication check**: Verify data link between container BMS and dock controller

**Flight Crew or Aircraft System**:
1. **Energy system status**: Confirm aircraft energy management system ready for external power input (during charging) or output (during discharging)
2. **Isolate if required**: For safety, aircraft high-voltage bus may be isolated during initial connection

**Checklist Time**: ~5 minutes

### CO₂ Battery Docking Sequence

**Step-by-Step** (Automated system with operator monitoring):

1. **Position container**: Drive or remote-control battery container transporter to dock approach zone (±1 m of centerline)
2. **Activate auto-docking**: Initiate automatic docking sequence (container uses sensors to align with dock within ±50 mm)
3. **Mechanical engagement**: Container connector engages with dock connector (mechanical guides ensure alignment)
4. **Verify mechanical lock**: Indicator shows green (connector locked, cannot be pulled apart accidentally)
5. **Pre-charge electrical connection**: Low-voltage pilot signal energizes (verifies continuity, no short circuit)
6. **High-voltage connection**: If pilot signal OK, dock controller closes high-voltage contactors (soft-start, ramp voltage gradually)
7. **Verify electrical connection**: Monitor voltage and insulation resistance (must be >100 kΩ/V)
8. **Enable thermal management**: Activate cooling flow through container (verify inlet/outlet temperature sensors)
9. **Ready for charge/discharge**: Container and dock signal "Ready" to energy management system

**Docking Time**: ~10 minutes (including alignment and electrical safety checks)

### CO₂ Battery Charging Monitoring

**Automated Monitoring** (every 100 ms):
- Voltage, current, power (kW)
- Cell temperatures (all 200+ sensors)
- Coolant flow rate, inlet/outlet temperature
- Insulation resistance (check every 10 seconds)
- BMS status (warnings, faults)

**Operator Actions**:
- **Periodic inspection**: Walk around container every 30 minutes, check for unusual sounds, odors, vibration
- **Monitor control panel**: Watch for alarms or temperature trends
- **Weather watch**: If severe weather approaching, may suspend charging and secure container

**Typical Charging Time**:
- **Charge rate**: 200-400 kW (depending on SOC and temperature)
- **Capacity**: 2-3 MWh (typical CO₂ battery container)
- **Charge time**: 5-10 hours (0% to 100% SOC), partial charges much faster

### CO₂ Battery Undocking Sequence

**Step-by-Step** (Automated system with operator monitoring):

1. **Ramp down current**: Energy management system reduces charge/discharge current to zero over 30 seconds
2. **Verify zero current**: Confirm <1 A for ≥10 seconds
3. **Open high-voltage contactors**: Dock controller opens contactors (voltage drops to zero at interface)
4. **Verify electrical isolation**: Test insulation resistance and zero voltage
5. **Disable thermal management**: Stop cooling flow (may continue for 5 minutes after disconnect to cool container)
6. **Mechanical unlock**: Release mechanical lock (actuator or manual lever)
7. **Disengage connector**: Container automatically or manually retracted (~0.5 m) to fully separate connector
8. **Cap connectors**: Install protective caps on container and dock connectors (prevent contamination, arcing if touched)
9. **Move container**: Drive container away to staging area or to aircraft for installation

**Undocking Time**: ~10 minutes (including cool-down and safety checks)

### CO₂ Battery Emergency Procedures

#### Thermal Runaway During Charging

**Detection**: BMS detects rapid temperature rise (>5°C/min) or temperature >70°C

**Automatic Actions**:
1. **Emergency disconnect**: Open high-voltage contactors immediately (<0.1 seconds)
2. **Sound alarm**: Local siren + control room alarm + ARFF notification
3. **Activate fire suppression**: Dock's inert gas system discharges into container (or water mist for cooling)
4. **Continue cooling**: Maintain maximum cooling flow if safe (to slow thermal cascade)

**Operator Actions**:
1. **Evacuate immediate area**: All personnel move >10 m from container
2. **Verify disconnect**: Visually confirm contactors open (indicator lights, zero current display)
3. **Monitor from safe distance**: Use thermal imaging camera to monitor temperature

**ARFF Actions**:
1. **Approach cautiously**: Thermal runaway may produce toxic gases (HF, CO), wear SCBA
2. **Establish exclusion zone**: 20 m radius, upwind positioning
3. **Cool container**: Apply water mist or foam from safe distance (10-15 m) to limit heat propagation
4. **Wait for stabilization**: Allow container to cool (may take hours), monitor with thermal imaging
5. **Coordinate removal**: Once cooled to <50°C and no re-ignition risk, coordinate container removal to hazmat area

**Stand State**: Declare UNSAFE until container removed and dock inspected/cleared.

## Ground Crew Coordination Procedures

### Role Definitions

| **Role** | **Responsibilities** | **Qualifications** |
|----------|---------------------|-------------------|
| **Ground Supervisor** | Overall stand safety, coordinate all GSE, declare stand state | Airport ground ops training, BWB familiarization |
| **H₂ Technician** | Perform H₂ refueling operations, monitor leak detectors | H₂ safety training, Ex zone certified |
| **H₂ Safety Observer** | Monitor H₂ technician, Ex zone enforcement, emergency response | H₂ safety training, first responder certified |
| **Battery Technician** | Perform CO₂ battery docking/undocking, monitor BMS | High-voltage safety training, battery systems certified |
| **GSE Operators** | Catering, baggage, cleaning, etc. | Standard airport GSE training, BWB stand layout familiarization |
| **Spotter** | Guide GSE movements near aircraft, ensure clearances | Airport ground ops training |

### Communication Protocols

**Primary Communication**: VHF radio (dedicated ground ops frequency for each stand or stand group)

**Standard Phrases**:
- **"Stand SAFE"**: Ground supervisor declares stand in SAFE state, all operations permitted
- **"Stand RESTRICTED, reason [...]"**: Ground supervisor declares RESTRICTED state, specifies reason (e.g., "H₂ pre-alarm, no passengers")
- **"Stand UNSAFE, evacuate"**: Ground supervisor declares UNSAFE state, all non-emergency personnel evacuate immediately
- **"Clear to approach [area]"**: Supervisor authorizes GSE or personnel to enter specific area (e.g., "Clear to approach forward cargo door")
- **"Hold position"**: Supervisor commands all GSE to stop movement
- **"Emergency, emergency, emergency"**: Any observer declares emergency (fire, injury, etc.), all acknowledge and respond

**Read-Back Required**: Any safety-critical instruction must be read back by recipient ("Clear to approach forward cargo door" → "Roger, clear to approach forward cargo door, GSE 123")

### Conflict Avoidance Procedures

**Spatial Separation** (see [85-00-02-003](85-00-02-003_Safety_Zones_and_Separation_Criteria.md)):
- H₂ refueling area: No GSE within 5 m during refueling (except H₂ dispenser truck itself)
- CO₂ battery area: No GSE within 3 m during docking/charging
- Passenger areas: No energy system operations (H₂, CO₂) within 5 m of passenger boarding doors or flow paths

**Temporal Separation**:
- **H₂ refueling before boarding**: Ideally complete H₂ refuel before passengers board (if scheduling permits)
- **CO₂ battery docking after disembarkation**: Dock/undock batteries after passengers have disembarked (reduces stand congestion)
- **Sequential GSE**: Stagger GSE operations (e.g., catering first, then baggage, then cleaning) to reduce traffic on stand

**Visual Indicators**:
- H₂ refueling active: Flashing amber beacon on H₂ dispenser truck + cones around Ex zone
- CO₂ battery charging: Flashing amber beacon on dock + "High Voltage" signs illuminated
- Passenger boarding: Green rotating beacon on boarding bridge(s)

### Cross-Reference to ATA 02-20 Ground Operations

Procedures integrate with:
- **[ATA 02-20-14 Ground Ops](../../../ATA_02-OPERATIONS_INFORMATION/)**: Standard ground handling procedures, turnaround checklist
- **[ATA 02-20-21 H₂ Operations Management](../../../ATA_02-OPERATIONS_INFORMATION/)**: Detailed H₂ system operational procedures (if exists)

## Related Documents

- [85-00-02-001_Safety_Concepts_and_Objectives.md](85-00-02-001_Safety_Concepts_and_Objectives.md) - Safety objectives
- [85-00-02-002_Hazard_Analysis_at_Interface_Level.md](85-00-02-002_Hazard_Analysis_at_Interface_Level.md) - Interface hazards
- [85-00-02-003_Safety_Zones_and_Separation_Criteria.md](85-00-02-003_Safety_Zones_and_Separation_Criteria.md) - Safety zones
- [85-00-02-004_H2_and_CO2_Energy_Safety_Interfaces.md](85-00-02-004_H2_and_CO2_Energy_Safety_Interfaces.md) - Technical safety details
- [85-00-02-007_Safety_Monitoring_and_Alerting_Interfaces.md](85-00-02-007_Safety_Monitoring_and_Alerting_Interfaces.md) - Monitoring systems
- [ATA 02 Operations Information](../../../ATA_02-OPERATIONS_INFORMATION/)

## References

- **IATA Ground Operations Manual (IGOM)**
- **NFPA 2**: Hydrogen Technologies Code (Fueling operations procedures)
- **SAE J2601**: Fueling protocols for light duty gaseous hydrogen surface vehicles (applicable principles for aircraft)
- **IEC 62485**: Safety requirements for secondary batteries and battery installations (stationary applications)

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
