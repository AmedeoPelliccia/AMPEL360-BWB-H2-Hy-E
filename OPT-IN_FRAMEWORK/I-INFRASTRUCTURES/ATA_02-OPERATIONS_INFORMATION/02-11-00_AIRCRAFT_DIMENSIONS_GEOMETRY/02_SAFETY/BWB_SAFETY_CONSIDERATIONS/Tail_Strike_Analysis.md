# Tail Strike Analysis

**Document ID:** AMPEL360-02-11-00-SAF-032  
**Version:** 1.0.0

## Overview

Tail strike is the contact of the aircraft's tail or aft fuselage with the runway or taxiway surface. For the AMPEL360 BWB, the unique geometry presents specific considerations for tail strike prevention and analysis.

## BWB Tail Strike Characteristics

### Geometric Configuration

**Aft Body Design:**
- No traditional tail (BWB configuration)
- Aft fuselage tapers to vertical stabilizers
- Lowest aft point: STA 34m, 2.5m above ground (static, MTOW)
- Critical structure: Vertical stabilizer bases

**Strike Points:**
- Primary: Aft fuselage belly panel (STA 32-34m)
- Secondary: Vertical stabilizer attachments
- Tertiary: Aft equipment bay doors/panels

### Clearance Margins

**Static Conditions (Level, MTOW):**
- Aft clearance: 2.5m ± 0.1m
- Margin above minimum: +0.5m
- Critical attitude: 10° pitch up (clearance→0.5m minimum)

**Dynamic Conditions:**
- Takeoff rotation: Maximum 12° pitch angle (BWB-specific limit)
- Landing flare: Maximum 10° pitch angle
- Taxi: Normal ±2° pitch (clearance adequate)

## Tail Strike Scenarios

### Takeoff

**Rotation Phase:**
- Typical rotation rate: 3-5°/sec
- Target rotation angle: 8-10°
- Maximum safe angle: 12° (tail strike protection)
- Over-rotation risk: Training emphasis

**Risk Factors:**
- Aft CG loading
- High gross weight
- Excessive rotation rate
- Pilot technique error
- Runway slope (uphill departure)

**Prevention:**
- Target pitch attitude display
- CAOS pitch limit alerting
- Standard rotation rate training
- Aft CG limitations (loading manual)

### Landing

**Flare Phase:**
- Normal landing attitude: 6-8° pitch
- Maximum safe attitude: 10° pitch
- Deep landing/hard flare: Risk scenario
- Bounce recovery: Risk scenario

**Risk Factors:**
- High sink rate at touchdown
- Late flare initiation
- Excessive flare (deep landing)
- Bounce with pitch-up recovery
- Runway slope (upslope landing)

**Prevention:**
- Standard approach and landing procedures
- Pitch limit awareness (training)
- Bounce recovery technique (pitch control)
- CAOS pitch alert system

### Ground Operations

**Taxi:**
- Normal pitch variation: ±2° (adequate clearance)
- Abrupt braking: Pitch-down tendency (not tail strike)
- Rough surfaces: Pitch excursions monitored by CAOS

**Towing:**
- Nose gear attachment: No abnormal pitch
- Proper tow bar angle: Critical
- Tow vehicle coordination: Standard procedures

## BWB-Specific Considerations

### Pitch Attitude Limits

**Compared to Conventional Aircraft:**
- Conventional: 15-18° typical limit
- AMPEL360 BWB: 12° takeoff, 10° landing
- **More restrictive due to aft geometry**

**Operational Impact:**
- Enhanced pilot training emphasis
- Pitch limit awareness critical
- CAOS pitch alert system essential
- Standard procedures must be followed

### Load Distribution Effects

**CG Range:**
- Forward CG: Increased pitch authority required (rotation)
- Aft CG: Reduced tail clearance margin (critical)
- CG limits: Defined in loading manual
- Loadmaster/dispatcher awareness critical

**Weight Effects:**
- MTOW: Minimum clearance (2.5m aft)
- MLW: Improved clearance (~2.6m)
- Fuel burn: Clearance improves in flight

### Structural Design

**Tail Strike Protection:**
- Aft fuselage: Reinforced skin panels
- Strike detection system: Sensors installed (CAOS integration)
- Damage tolerance: Analysis performed
- Inspection requirements: Post-strike procedure defined

## Prevention Systems

### CAOS Pitch Monitoring

**Functions:**
- Real-time pitch angle calculation
- Pitch rate monitoring
- Tailstrike clearance computation
- Crew alerting system integration

**Alerts:**
- **Amber:** Approaching pitch limit (10° takeoff, 9° landing)
- **Red:** Pitch limit exceeded (12° takeoff, 10° landing)
- **Caution:** Excessive pitch rate (>6°/sec)

**Display:**
- Primary flight display (PFD) pitch ladder
- CAS messages
- Aural alert (pitch limit)

### Tail Strike Protection System (TSPS)

**Detection:**
- Aft fuselage contact sensors (pressure switches)
- Accelerometers (sudden deceleration signature)
- CAOS pitch attitude correlation

**Indication:**
- Immediate crew warning (CAS message, aural)
- TSPS light (flight deck)
- Maintenance message generation

**Post-Strike Actions:**
- Aircraft inspection mandatory before next flight
- Maintenance notification automatic
- Data recording for analysis

## Operational Procedures

### Takeoff Procedures

**Standard Rotation:**
1. Vr (rotation speed): As calculated (typically 140-150 kt)
2. Rotation rate: 3°/sec target
3. Target pitch attitude: 10° (hold, not exceed)
4. Lift-off: Natural, at target attitude
5. Initial climb: Maintain pitch ≤10° until gear retracted

**Monitoring:**
- Pilot Flying (PF): Pitch attitude control
- Pilot Monitoring (PM): Pitch attitude verification, callouts
- CAOS: Continuous monitoring, alert generation

**Callouts:**
- "Rotate" (at Vr)
- "10 degrees" (target pitch reached)
- "Positive rate" (climb established)
- "Gear up"

### Landing Procedures

**Approach:**
- Stabilized approach: Standard (speed, sink rate, configuration)
- Approach attitude: 3-5° pitch

**Flare:**
1. Flare initiation: 20-30 feet AGL
2. Gradual pitch increase: 2-3°/sec maximum
3. Target touchdown attitude: 7-8° pitch
4. Maximum attitude: 10° (do not exceed)

**Touchdown:**
- Main gear first (normal)
- Nose gear follows (controlled descent)
- Pitch control maintained throughout

**Bounce Recovery:**
- If bounce occurs: Do not pull back excessively
- Maximum pitch: 10° (tail strike protection)
- Go-around: If excessive bounce

### Post-Strike Procedures

**Crew Actions:**
1. TSPS warning: Note and acknowledge
2. Complete flight normally (if safe)
3. Notify maintenance immediately upon landing
4. Aircraft parked for inspection
5. Complete incident report

**Maintenance Actions:**
1. Visual inspection (aft fuselage, sensors)
2. Structural assessment (per maintenance manual)
3. TSPS data download and analysis
4. Damage documentation (photos, measurements)
5. Repair as required (per SRM)
6. Airworthiness determination before next flight

## Training Requirements

### Flight Crew

**Initial Training:**
- BWB pitch limitations (2 hours ground school)
- Tail strike prevention (1 hour)
- CAOS pitch monitoring system (1 hour)
- Simulator training: Rotation/landing technique (4 hours)

**Emphasis Areas:**
- Standard rotation rate (3°/sec)
- Target pitch attitudes (10° takeoff, 7-8° landing)
- Pitch limit recognition
- Bounce recovery technique (pitch control)

**Recurrent Training:**
- Annual refresher (1 hour)
- Simulator: Rotation and landing (2 hours annually)
- Incident case studies
- Procedure updates

### Maintenance Personnel

**Training:**
- TSPS system operation
- Post-strike inspection procedures
- Damage assessment criteria
- Repair procedures (per SRM)

## Analysis and Improvement

### Incident Analysis

**Data Sources:**
- TSPS activation records
- Flight data recorder (FDR)
- CAOS system logs
- Crew reports

**Analysis:**
- Flight conditions (weight, CG, runway, weather)
- Crew actions (rotation rate, pitch attitude)
- System performance (CAOS alerts)
- Contributing factors

**Corrective Actions:**
- Training enhancements
- Procedure modifications
- System improvements
- Communication to fleet

### Predictive Analysis

**Monitoring:**
- Pitch attitude trends (fleet data)
- CAOS alert frequency
- Training effectiveness
- Procedure compliance

**Risk Assessment:**
- High-risk conditions identification
- Preventive measures implementation
- Continuous improvement

---

**Document Control:**
- Revision Date: 2025-11-06
- Next Review: 2026-05-06
- Approval: Chief Pilot, Chief Engineer
