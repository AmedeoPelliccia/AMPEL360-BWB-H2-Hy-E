# 85-00-01-007 Safety and Resilience Concepts

## Document Information

- **Document ID**: 85-00-01-007
- **Title**: Safety and Resilience Concepts
- **Version**: 1.0
- **Date**: 2025-11-21
- **Status**: Draft
- **Category**: Safety & Resilience
- **ATA Chapter**: 85 - Infrastructure Interface Standards

## Purpose

This document establishes safety and resilience concepts for the AMPEL360 BWB infrastructure interfaces. It addresses the unique hazards introduced by hydrogen propulsion and CO₂ battery systems, ensures safe coexistence of energy operations with passenger flows, and defines degraded-mode operations when infrastructure systems are unavailable or impaired.

## Scope

This specification covers:

- Hazard identification and risk mitigation for infrastructure interfaces
- Separation and segregation principles (H₂, CO₂, passengers, GSE)
- Redundancy and degraded-mode operation strategies
- Emergency scenarios and response procedures
- Integration with aircraft and airport safety management systems
- Resilience metrics and continuous improvement

## Fundamental Safety Principles

### Defense in Depth

Multiple layers of protection ensure that a single failure does not result in a hazardous condition:

1. **Prevention**: Design to eliminate or minimize hazards (e.g., leak-tight H₂ systems)
2. **Detection**: Early warning systems (e.g., H₂ leak detectors, thermal monitoring)
3. **Mitigation**: Automatic protective actions (e.g., emergency shutoff valves)
4. **Response**: Emergency procedures and equipment (e.g., fire suppression, evacuation)
5. **Recovery**: Restoration procedures and lessons learned (e.g., incident investigation, design improvements)

### Fail-Safe Design

Systems are designed to default to a safe state upon failure:

- **H₂ Refuelling**: Loss of control signal or power → automatic valve closure → refuelling stops
- **CO₂ Battery Docking**: Loss of electrical connection → charging stops → battery remains in safe state
- **Emergency Interlocks**: Loss of interlock signal → all ground operations inhibited → safe condition maintained

### Separation and Redundancy

Critical systems have physical or functional separation and backup capabilities:

- **H₂ Refuelling Ports**: Primary (port) and secondary (starboard) for redundancy
- **GPU Connections**: Primary (forward) and secondary (aft) for extended maintenance
- **Emergency Exits**: 16 total exits (12 Type A doors + 4 Type III overwing) – redundancy far exceeds regulatory minimum

## Hazard Analysis and Risk Mitigation

### H₂ Refuelling Hazards

#### Hazard 1: H₂ Leak During Refuelling

**Risk Level (Unmitigated)**: High (Probability: Medium, Severity: Catastrophic)

**Mitigations:**
1. **Design**: Leak-tight connectors (SAE AS50881 compliant), tested to 700 bar
2. **Detection**: Multiple H₂ sensors (catalytic bead + infrared), 0.1% LEL sensitivity, < 1 second response
3. **Automatic Response**: Leak detection → emergency shutoff valve closure (< 1 second) + alarm
4. **Ventilation**: Natural or forced ventilation to prevent accumulation (H₂ rises rapidly)
5. **Exclusion Zone**: 10m radius, no ignition sources, no personnel during active transfer
6. **Training**: Ground crew trained on H₂ properties, leak response, emergency procedures

**Risk Level (Mitigated)**: Low (Probability: Low, Severity: Moderate - prompt detection and response prevent catastrophic outcome)

#### Hazard 2: H₂ Fire at Refuelling Point

**Risk Level (Unmitigated)**: High (Probability: Low, Severity: Catastrophic)

**Mitigations:**
1. **Prevention**: Eliminate ignition sources (no hot work, bonding and grounding, explosion-proof equipment)
2. **Detection**: Fire detection (UV/IR flame detectors, heat detectors) in refuelling zone
3. **Suppression**: Water deluge system (H₂ fire is cooled, not smothered - water is effective)
4. **Emergency Stop**: Manual E-stop buttons (ground and cockpit) + automatic on fire detection
5. **ARFF Response**: Airport fire services notified automatically, < 3 minute response time
6. **Procedure**: Controlled depressurization if safe, otherwise maintain supply (burnout under control better than uncontrolled release)

**Risk Level (Mitigated)**: Low (Probability: Very Low, Severity: Moderate - multiple layers prevent ignition, rapid response contains fire)

#### Hazard 3: Overpressure in Aircraft H₂ Tank

**Risk Level (Unmitigated)**: Medium (Probability: Low, Severity: Critical)

**Mitigations:**
1. **Design**: Tanks designed to 1.5x operating pressure (1,050 bar for 700 bar system), burst pressure > 2.25x (1,575 bar)
2. **Monitoring**: Real-time pressure monitoring (1 Hz), automatic refuelling stop at 95% capacity
3. **Relief Valves**: Pressure relief valves set at 750 bar (on aircraft tanks) - vent to atmosphere
4. **Interlock**: Ground refuelling equipment monitors tank pressure, stops at setpoint
5. **Procedure**: Pre-refuelling verification of tank pressure and condition

**Risk Level (Mitigated)**: Very Low (Probability: Very Low, Severity: Minor - multiple automatic safeguards prevent overpressure)

### CO₂ Battery Hazards

#### Hazard 4: Thermal Runaway in CO₂ Battery

**Risk Level (Unmitigated)**: Medium (Probability: Low, Severity: Critical)

**Mitigations:**
1. **Design**: Battery cells with inherent thermal stability (solid-state technology)
2. **Monitoring**: 12 temperature sensors per module, continuous monitoring (1 Hz), high-rate sampling (10 Hz) during charging
3. **Cooling**: Active liquid cooling with redundant pumps, emergency air cooling backup
4. **Automatic Response**: Temperature > 55°C or rate of rise > 2°C/min → charging stops + cooling increases + alarm
5. **Manual Response**: Ground crew can manually disconnect battery and evacuate if condition worsens
6. **Fire Suppression**: Dry powder or CO₂ fire extinguishers available at stands (water-based suppressants avoided for electrical fire)

**Risk Level (Mitigated)**: Very Low (Probability: Very Low, Severity: Minor - solid-state battery inherently stable, active cooling prevents runaway)

#### Hazard 5: Electrical Arc During Battery Docking

**Risk Level (Unmitigated)**: Low (Probability: Low, Severity: Moderate)

**Mitigations:**
1. **Design**: High-current connectors rated for 350A (derated to 200A continuous use)
2. **Sequence**: Mechanical docking verified (position sensors) before electrical connection
3. **Pre-Charge**: Ground equipment pre-charges connection to equalize voltage (prevents inrush current)
4. **Arc Suppression**: Connector design with arc-suppression features (magnetic blowout)
5. **Procedure**: Visual and electronic verification of proper alignment before connection

**Risk Level (Mitigated)**: Very Low (Probability: Very Low, Severity: Minor - proper sequencing and design features eliminate arc potential)

### Passenger and Ground Crew Safety

#### Hazard 6: Passenger Exposure to H₂ Operations

**Risk Level (Unmitigated)**: Medium (Probability: Medium, Severity: Moderate)

**Mitigations:**
1. **Temporal Separation**: H₂ refuelling early in turnaround (while passengers disembark), complete before boarding
2. **Physical Separation**: Exclusion zone (10m radius) around refuelling point, barriers or markings
3. **Monitoring**: H₂ leak detectors operational during refuelling, alarm if leak detected
4. **Procedure**: Boarding prohibited during active H₂ refuelling (interlock in ground handling system)
5. **Signage**: Clear signage warning of H₂ operations in progress (for ground crew and passengers)

**Risk Level (Mitigated)**: Very Low (Probability: Very Low, Severity: Negligible - separation ensures no passenger exposure)

#### Hazard 7: Ground Crew Injury During GSE Operations

**Risk Level (Unmitigated)**: Medium (Probability: Medium, Severity: Moderate)

**Mitigations:**
1. **Training**: All ground crew trained on BWB-specific operations, H₂ safety, emergency procedures
2. **PPE**: High-visibility vests, safety shoes, hearing protection, gloves (standard GSE operations)
3. **Communication**: Clear radio communication protocols, visual signals for coordination
4. **Clear Zones**: Defined clear zones around GSE (5m for cargo loaders, 10m for H₂ bowser, 3m for pushback tractor)
5. **Automation**: Future transition to autonomous or semi-autonomous GSE to reduce crew exposure

**Risk Level (Mitigated)**: Low (Probability: Low, Severity: Minor - training and procedures minimize injury risk)

## Separation and Segregation Principles

### Spatial Separation

**H₂ Refuelling Zone:**
- Location: Port or starboard side, mid-fuselage (stations 12-13m)
- Exclusion radius: 10m during active refuelling
- Segregation: No passenger boarding/deplaning doors within exclusion zone
- Access control: Barriers, signage, or procedural controls (depending on airport)

**CO₂ Battery Servicing Zone:**
- Location: Ventral bays, stations 18-22m
- Access: Under-fuselage, segregated from passenger and cargo operations
- Timing: Can be concurrent with cargo loading (on opposite side) or passenger boarding (safely above battery bays)

**Passenger Flow Zones:**
- Primary: Forward doors (1L/R, 2L/R, 3L/R) for boarding/deplaning via jetway or stairs
- Secondary: Aft doors (4L/R, 5L/R, 6L/R) if dual boarding used
- Separation from: H₂ refuelling (at least 15m), CO₂ battery servicing (vertical separation, 2.5m clearance)

**Cargo Operations:**
- Forward cargo door: Port side, station 9m (can be concurrent with aft passenger boarding on starboard)
- Aft cargo door: Starboard side, station 25m (can be concurrent with forward passenger boarding on port)

### Temporal Separation

**Turnaround Sequence (60-minute example with separation enforced):**

| Time | Operation | Zone | Compatible Operations |
|------|-----------|------|----------------------|
| T+0 | Arrival | - | - |
| T+5 | Passenger Disembarkation | Forward/Aft Passenger Zones | Cargo unloading (opposite side) |
| T+10 | **H₂ Refuelling Start** | **H₂ Zone** | **Cargo unloading (opposite side), Disembarkation continues if outside exclusion zone** |
| T+15 | Disembarkation Complete | - | H₂ refuelling continues |
| T+20 | Catering/Cleaning | Passenger Zones | H₂ refuelling continues, CO₂ battery servicing |
| T+25 | **H₂ Refuelling Complete** | **H₂ Zone Clear** | Catering/cleaning continues, CO₂ battery servicing |
| T+30 | CO₂ Battery Servicing (if needed) | CO₂ Zone | Catering/cleaning, cargo loading |
| T+40 | Cargo Loading Complete | - | CO₂ battery servicing continues |
| T+45 | **Passenger Boarding Start** (H₂ must be complete) | Passenger Zones | CO₂ battery servicing (can continue, if needed) |
| T+55 | Boarding Complete | - | - |
| T+60 | Pushback Ready | - | - |

**Key Interlocks:**
- H₂ refuelling must complete before passenger boarding begins
- Cargo loading can be concurrent with H₂ refuelling (on opposite side)
- CO₂ battery servicing can overlap with passenger boarding (vertical separation, no interference)

## Redundancy and Degraded-Mode Operations

### H₂ Refuelling Infrastructure Unavailable

**Scenario**: Airport H₂ infrastructure down (equipment failure, supply shortage, safety incident)

**Options:**

1. **Alternative Refuelling Location**
   - Divert to alternate airport with H₂ capability (flight planning considers H₂ availability)
   - Range: 4,000 km nominal (with reserves, can reach alternate within 3,500 km)

2. **Delayed Departure**
   - Wait for H₂ infrastructure restoration (acceptable for planned maintenance)
   - Alternative energy source: Ground power for hotel services (passengers wait in terminal)

3. **Partial Refuelling (Future Capability)**
   - Battery swap or partial charge of CO₂ batteries to extend range with reduced H₂ load
   - Reduces payload or range, but maintains operational capability

**Impact:**
- Schedule disruption: Delay or cancellation
- Operational cost: Diversion cost, passenger compensation
- Safety: No safety impact (flight not dispatched without adequate H₂)

**Mitigation:**
- Network planning: H₂ infrastructure at multiple airports along routes
- Dual-source H₂ supply: Fixed pipeline + mobile bowser for redundancy
- Inventory management: H₂ storage buffer at airports for short-term disruptions

### GPU Unavailable

**Scenario**: Ground power unit failure or unavailable at stand

**Options:**

1. **Aircraft APU (if equipped)**
   - Start APU for electrical power and air conditioning
   - Fuel consumption: ~ 50-100 kg jet fuel per hour (APU uses conventional fuel as backup)
   - Duration: Limited by APU fuel supply (separate tank, ~ 4 hours typical)

2. **Aircraft Batteries**
   - Essential systems only (lighting, avionics, fire detection)
   - Duration: 2-3 hours (battery capacity)
   - Limitation: No air conditioning, limited hotel services

3. **Alternative GPU**
   - Request GPU from adjacent stand or maintenance area
   - Delay: 10-30 minutes (depending on availability and response time)

**Impact:**
- Minor schedule delay (10-30 minutes)
- Increased operational cost (APU fuel burn)
- Passenger comfort: Reduced (if no air conditioning)

**Mitigation:**
- GPU redundancy at busy airports (spare GPUs available)
- APU as backup (if aircraft is so equipped)
- Procedural: Ground crew trained to request alternative GPU promptly

### Evacuation Infrastructure Impaired

**Scenario**: Evacuation slide deployment zone obstructed (e.g., GSE vehicle, debris) or slide malfunction

**Options:**

1. **Alternate Exits**
   - 16 total exits (12 Type A + 4 Type III overwing)
   - Regulatory requirement: 50% of exits available (8 exits minimum)
   - Capacity: Even with 50% blockage, 220 passengers evacuate in < 90 seconds (demonstrated)

2. **Mobile Stairs (Assisted Evacuation)**
   - Deploy mobile stairs to unobstructed doors
   - Time: +5-10 minutes vs. slide evacuation (acceptable for non-emergency or slow-developing situations)

3. **ARFF Assisted Evacuation**
   - ARFF platforms and ladders for high-level evacuations
   - Primarily for rescue of incapacitated passengers or crew

**Impact:**
- Evacuation time may increase (but still within safety margins)
- Potential for minor injuries (stairs vs. slides)

**Mitigation:**
- Stand design: Ensure evacuation zones are marked and kept clear (ICAO Annex 14 compliance)
- Ground crew vigilance: Pre-departure FOD walk to verify clear zones
- Redundant exits: 16 exits provide significant margin over minimum requirements

### Airport ARFF Capability Reduced

**Scenario**: Airport fire services temporarily reduced capability (e.g., vehicle maintenance, personnel shortage)

**Options:**

1. **Regulatory Minimum Enforcement**
   - ICAO Annex 14: Aerodrome category must match largest aircraft (BWB = Category 9)
   - If ARFF drops below category: Airport may restrict operations (no BWB departures/arrivals)

2. **Mutual Aid Agreements**
   - Local fire departments provide backup ARFF capability
   - Training: Local FD must be trained on aircraft firefighting (NFPA 1003)

3. **Operational Restrictions**
   - No H₂ refuelling operations (degraded fire response)
   - Aircraft must arrive with sufficient H₂ to depart without refuelling

**Impact:**
- Severe: Potential flight cancellations or diversions
- Schedule: Major disruptions until ARFF capability restored

**Mitigation:**
- Preventive maintenance: ARFF vehicles and equipment maintained with redundancy
- Training pipeline: Sufficient qualified ARFF personnel with cross-training
- Contingency planning: Mutual aid agreements in place before service degradation

## Emergency Scenario Response Procedures

### Scenario 1: H₂ Leak During Refuelling

**Immediate Actions (Automatic):**
1. H₂ leak detector alarm (< 1 second from detection)
2. Emergency shutoff valve closure on ground and aircraft sides (< 1 second)
3. Alarm transmitted to cockpit, ground crew, and airport operations center
4. Fire suppression system armed (automatic activation if fire detected)

**Ground Crew Response (Manual):**
1. Verify refuelling stopped (< 5 seconds)
2. Evacuate personnel from exclusion zone (10m radius) (< 30 seconds)
3. Notify airport operations center and ARFF (< 1 minute) - if not already automatic
4. Monitor leak level with portable detectors (ongoing)
5. If leak persists and increases: Initiate controlled venting or emergency defuelling (per procedure)

**ARFF Response:**
1. Dispatch upon alarm (< 1 minute)
2. Arrive at scene (< 3 minutes from alarm)
3. Establish safety perimeter (25m, upwind)
4. Monitor H₂ concentration (portable detectors)
5. Standby for fire suppression (water deluge if fire occurs)
6. All-clear after leak stopped and H₂ concentration < 0.1% LEL for 10 minutes

**Recovery:**
1. Inspect refuelling equipment and aircraft connector (damage assessment)
2. Leak repair or equipment replacement (may require aircraft repositioning)
3. Safety review: Incident investigation, lessons learned, procedure updates (if needed)

### Scenario 2: CO₂ Battery Thermal Runaway Warning

**Immediate Actions (Automatic):**
1. Temperature exceedance detected (> 55°C or > 2°C/min rise)
2. Charging stopped automatically (< 1 second)
3. Cooling system flow increased to maximum (within 5 seconds)
4. Alarm transmitted to cockpit, ground crew, and airport operations center

**Ground Crew Response (Manual):**
1. Verify charging stopped (< 5 seconds)
2. Monitor battery temperature (continuous)
3. If temperature continues to rise: Disconnect battery electrically and thermally (< 2 minutes)
4. If temperature stabilizes: Monitor for 10 minutes, if decreasing, resume charging at reduced rate (if time permits)
5. If temperature exceeds 60°C: Notify ARFF, prepare for possible fire

**ARFF Response (if notified):**
1. Dispatch upon notification (< 1 minute)
2. Arrive at scene (< 3 minutes)
3. Assess battery condition (thermal imaging)
4. If fire occurs: Dry powder or CO₂ suppression (avoid water on electrical fire)
5. If no fire: Standby until battery temperature returns to normal (< 40°C)

**Recovery:**
1. Battery module inspection (may require replacement if thermal event was severe)
2. Incident investigation: Determine root cause (charging profile, cell defect, cooling failure)
3. Procedure update: Modify charging parameters if necessary

### Scenario 3: Emergency Evacuation with Concurrent H₂ Operations

**Immediate Actions (Automatic + Crew):**
1. Emergency declared: Crew initiates evacuation (e.g., fire, severe turbulence on ground, security threat)
2. H₂ refuelling automatically stopped (if active) - interlock with evacuation initiation
3. Ground power maintained (for emergency lighting and communications)
4. ARFF automatically dispatched

**Ground Crew Response (Manual):**
1. H₂ bowser: Emergency disconnection (< 30 seconds), move away from aircraft (> 50m)
2. All GSE: Move clear of evacuation zones (< 1 minute)
3. Direct passengers away from aircraft to assembly points (ongoing)

**Cabin Crew Response:**
1. Initiate evacuation per CS-25.803 / FAR 25.803 procedures
2. All exits available (no exits blocked by H₂ operations - temporal separation ensures this)
3. Slides deployed, passengers evacuated (< 90 seconds)

**Coordination:**
- H₂ operations and evacuation are temporally separated by design (H₂ refuelling complete before boarding)
- If rare scenario occurs (e.g., emergency during disembarkation while H₂ refuelling), H₂ automatic stop and bowser retreat ensure safety

**Recovery:**
1. Passengers accounted for at assembly points (< 15 minutes post-evacuation)
2. Incident investigation: Determine cause of evacuation, any injuries, equipment performance
3. Aircraft inspection: Determine if aircraft can be re-entered or requires tow to maintenance area

## Resilience Metrics and Continuous Improvement

### Key Performance Indicators (KPIs)

**Safety KPIs:**
- **H₂ Leak Rate**: Target: < 1 event per 10,000 refuelling operations
- **Battery Thermal Events**: Target: < 1 event per 10,000 charging cycles
- **Ground Incidents**: Target: < 1 per 1,000 turnarounds (any GSE or infrastructure-related injury or damage)
- **Emergency Evacuation Readiness**: 100% of evacuation drills meet < 90 second target

**Operational Resilience KPIs:**
- **H₂ Infrastructure Availability**: Target: > 99.5% (downtime < 1.8 days per year per airport)
- **GPU Availability**: Target: > 99.9% (backup GPU or APU available)
- **On-Time Performance** (infrastructure-related delays): Target: < 2% of flights delayed > 15 minutes due to infrastructure issues

**Response and Recovery KPIs:**
- **ARFF Response Time**: Target: < 3 minutes to any point on aircraft (ICAO Annex 14 standard)
- **Infrastructure Restoration Time**: Target: < 4 hours for critical systems (H₂, GPU), < 24 hours for non-critical systems

### Continuous Improvement Process

**Data Collection:**
- Incident and near-miss reporting (voluntary and mandatory)
- Performance data from ground operations (turnaround times, refuelling durations, battery charging efficiency)
- Maintenance data (equipment reliability, failure modes)

**Analysis:**
- Monthly safety review meetings (operations, engineering, safety teams)
- Trend analysis (identify recurring issues or degrading performance)
- Root cause analysis for incidents (5-Why, Fishbone diagrams, FMEA)

**Action:**
- Design improvements (e.g., connector redesign if leak-prone, battery thermal management upgrade)
- Procedure updates (e.g., clarify ground crew coordination steps)
- Training enhancements (e.g., additional H₂ safety modules)

**Verification:**
- Monitor KPIs post-implementation (verify improvement)
- Periodic audits (internal and external, e.g., aviation authority, airport authority)
- Feedback loop to design teams for future aircraft or infrastructure upgrades

---

## Document Control

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT** – Subject to human review and approval.
- Human approver: _[to be completed]_.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: 2025-11-21

---
