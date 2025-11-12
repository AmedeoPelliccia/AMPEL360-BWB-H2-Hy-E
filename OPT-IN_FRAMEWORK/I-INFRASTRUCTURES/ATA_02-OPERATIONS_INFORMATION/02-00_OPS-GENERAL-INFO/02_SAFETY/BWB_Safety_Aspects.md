# BWB Safety Aspects

**Document ID:** AMPEL360-02-10-00-SAF-BWB  
**Version:** 1.0.0  
**Date:** 2025-11-05  
**Status:** Released  
**Classification:** Safety Critical

## Introduction

The Blended Wing Body (BWB) configuration presents unique safety considerations compared to conventional tube-and-wing aircraft. This document addresses BWB-specific safety aspects, hazards, and mitigation strategies for the AMPEL360 aircraft.

## Configuration Overview

### BWB Characteristics

**Aerodynamic:**
- Entire fuselage generates lift
- Lower induced drag
- Efficient cruise performance
- Non-conventional handling characteristics

**Structural:**
- Load-bearing body structure
- Wide cabin cross-section
- Integrated wing-body
- Distributed passenger seating

**Operational:**
- Wide CG range
- Unique ground handling requirements
- Enhanced evacuation considerations
- Different failure modes than conventional

## Flight Safety Considerations

### Center of Gravity Management

**Challenge:**
- BWB configuration has wider permissible CG range
- CG position more sensitive to load distribution
- Fuel consumption affects CG more than conventional
- Passenger/cargo distribution critical

**Hazards:**
- CG outside limits: Loss of control, aerodynamic stall
- Rapid CG shift: Unexpected handling changes
- CG calculation error: Unknown aircraft state

**Mitigation:**

**Real-Time Monitoring (CAOS)**
- Continuous CG calculation based on:
  - Fuel quantity and distribution
  - Passenger count and seating
  - Cargo loading
  - System component status
- Update rate: 1 Hz (every second)
- Accuracy: ±0.1% MAC

**Alert System**
- **Caution (±2% MAC from limit):** Yellow alert, crew awareness
- **Warning (±1% MAC from limit):** Red alert, immediate action required
- **Prevention (at limit):** Automatic fuel transfer if available

**Operational Procedures**
- Pre-flight: Load planning with CG verification
- In-flight: Regular CG checks by crew
- Fuel management: Procedures to maintain CG within limits
- Passenger movement: Minimize during critical phases

**Training**
- Flight crew: CG management training (4 hours)
- Load planning: CG calculation procedures
- Dispatcher: Load planning tools and verification

**Monitoring**
- CAOS: Predictive CG calculation (fuel burn)
- Cross-check: Crew manual verification
- Recording: CG position logged throughout flight

### Handling Characteristics

**Differences from Conventional:**
- Pitch control: Elevon effectiveness varies with CG
- Roll control: Wide wing span requires coordination
- Yaw stability: Winglet design critical
- Stall characteristics: Different from tube-and-wing

**Safety Approach:**

**Flight Control System**
- Fly-by-wire: All control inputs processed
- Envelope protection: Prevents exceeding safe limits
- Redundancy: Quadruple flight control computers
- Degraded modes: Multiple levels of backup control laws

**Pilot Training**
- Type rating: BWB-specific training required
- Simulator: High-fidelity BWB handling simulation
- Unusual attitudes: Recovery training
- Degraded modes: Practice with limited controls
- Duration: 40 hours ground + 20 hours simulator

**Flight Envelope Protection**
- Angle of attack limiting
- Bank angle limiting (configurable)
- Load factor limiting (2.5g to -1.0g normal)
- Overspeed protection
- Underspeed protection (stall warning + stick pusher)

### Structural Safety

**Load Distribution:**
- Distributed lift across BWB planform
- Multiple load paths (redundancy)
- Damage tolerance designed in
- Composite construction with proven safety

**Design Philosophy:**
- **Fail-safe:** Structure can withstand single failure
- **Damage tolerant:** Detectable damage before critical
- **Safety factor:** 3× for static loads, 1.5× for ultimate
- **Fatigue life:** 120,000 flight cycles design goal

**Inspection:**
- Structural health monitoring: Fiber optic sensors
- CAOS integration: Anomaly detection
- Regular NDT: Per maintenance schedule
- Access panels: Provided for critical areas

## Ground Operations Safety

### Ground Handling

**Challenges:**
- Wide wingspan (non-standard)
- Low ground clearance areas
- Unique towing requirements
- Unconventional access points

**Towing and Pushback:**
- **Tow bar:** BWB-specific design required
- **Attachment point:** Reinforced nose gear
- **Clearance:** Ground personnel awareness training
- **Procedure:** Step-by-step in Ground Ops Manual
- **Communication:** Tow crew + flight deck continuous

**Ground Clearance:**
- **Critical areas:** Wing tips, tail, aft fuselage
- **Marking:** Visual indicators for clearance limits
- **Equipment:** BWB-compatible ground support equipment
- **Lighting:** Enhanced for night operations
- **Training:** Ground crew BWB-specific (4 hours)

**Parking and Mooring:**
- **Gate requirements:** Wider wingspan considerations
- **Tie-down points:** 8 points (vs 3 conventional)
- **Chocks:** Main and nose gear
- **Weather limits:** High wind procedures
- **Lightning protection:** Grounding when parked

### Refueling Safety

**H₂ Refueling (BWB-specific considerations):**
- **Connection location:** Designed for ground crew access
- **Safety zone:** 50m radius enforced
- **Passenger restriction:** Not aboard during refueling
- **Vent location:** Above BWB profile, safe dispersion
- **Emergency shutdown:** Accessible from ground and flight deck

**Ground Electrical:**
- **GPU connection:** Standard location marked
- **Bonding:** Verified before H₂ refueling
- **Power limits:** Ground power capacity adequate

## Cabin Safety

### Evacuation

**Challenges:**
- Wide cabin (not conventional aisle configuration)
- Distributed seating across BWB planform
- Exit spacing different from conventional
- Passenger flow patterns unique

**Exit Configuration:**
- **Type A exits:** 4 (forward and aft sides)
  - Capacity: 110 persons/minute each
  - Dual-lane slides
- **Type III exits:** 8 (distributed along perimeter)
  - Capacity: 55 persons/minute each
  - Single-lane slides
- **Total capacity:** 880 persons/minute (regulatory: 220 in 90 sec = 147/min)

**Demonstrated Evacuation:**
- **Test conditions:** Full aircraft, 50% passengers >50 years, lighting off
- **Result:** 75 seconds (target <90 seconds)
- **Margin:** 15 seconds (20% safety margin)
- **Certification:** Meets CS-25.803 requirements

**Evacuation Procedures:**
- **Crew positioning:** Strategic for BWB layout
- **Passenger briefing:** BWB-specific (exits may be unfamiliar)
- **Lighting:** Enhanced for wide cabin
  - Floor path lighting: Photoluminescent strips
  - Exit signs: High-visibility LED
  - Emergency lighting: 15 minutes battery backup
- **Commands:** Clear and loud (PA + crew voices)

### Fire Safety

**Detection:**
- **Smoke detectors:** Optimally placed for BWB cabin volume
- **Lavatory detectors:** All lavatories
- **Cargo detectors:** All cargo compartments
- **Ceiling-mounted:** Coverage per zone analysis

**Suppression:**
- **Handheld extinguishers:**
  - 6 Halon (electrical, H₂)
  - 4 Water (cabin Class A fires)
  - Distributed: Accessible from any cabin location
- **Cargo suppression:** Automatic Halon system

**Containment:**
- **Fireproof barriers:** Between compartments
- **Cabin materials:** Fire-resistant per CS-25.853
- **Waste bin suppression:** Automatic in lavatories
- **Oxygen shutoff:** Crew-activated passenger oxygen shutoff

### Seating and Restraints

**BWB Seating:**
- **Orientation:** Some seats side-facing (optimized for BWB layout)
- **Certification:** 16g forward, 4g side per CS-25.562
- **Restraints:** 3-point harness (lap + shoulder)
- **Spacing:** Adequate for evacuation

**Child Restraints:**
- **Compatibility:** Standard child seats compatible
- **Labeling:** Approved child seat types posted
- **Procedure:** Flight attendant verifies installation

## Emergency Systems (BWB-specific)

### Emergency Lighting

**Enhanced for BWB:**
- **Coverage:** Wider cabin requires more units
- **Uniformity:** Even lighting across wide cabin
- **Floor path:** All aisles to all exits
- **Exit marking:** Clearly visible from all cabin positions

### Life Rafts

**Quantity and Distribution:**
- **8 rafts:** 50-person capacity each (total 400)
- **Location:** Distributed optimally for BWB cabin
  - 2 forward
  - 4 mid-cabin (port and starboard)
  - 2 aft
- **Accessibility:** Crew access without passenger obstruction
- **Deployment:** Manual, crew-initiated

### Emergency Equipment Access

**Strategic Distribution:**
- **Fire extinguishers:** Maximum 25 ft from any cabin point
- **First aid kits:** 4 stations, distributed
- **Oxygen (portable):** 6 bottles, accessible
- **AED:** 2 units, forward and aft

## Ditching Considerations

### BWB Ditching Characteristics

**Advantages:**
- **Buoyancy:** Wide body provides inherent flotation
- **Stability:** Anticipated to float level (analysis + test)
- **Duration:** Estimated 10+ minutes floating time
- **Access:** Multiple exits above waterline (predicted)

**Certification:**
- **Analysis:** CS-25.801 ditching analysis conducted
- **Testing:** Model testing completed
- **Procedures:** Ditching checklist developed

**Procedures:**
- **Preparation time:** Maximize preparation if ditching anticipated
- **Landing technique:** Specific for BWB (detailed in QRH)
- **Post-ditching:** Immediate evacuation to rafts
- **Crew coordination:** Specific crew responsibilities

## Regulatory Compliance

### BWB-Specific Certification

**EASA Special Conditions:**
- **SC-BWB-001:** Handling characteristics unique to BWB
- **SC-BWB-002:** Evacuation demonstration (wide cabin)
- **SC-BWB-003:** Structural loads (distributed lift)
- **SC-BWB-004:** Flight deck visibility (unconventional)

**FAA Special Conditions:**
- Equivalent to EASA
- Bilateral acceptance
- Additional FAA testing if required

### Standard Requirements (applied to BWB):
- **CS-25.803:** Emergency evacuation
- **CS-25.807:** Emergency exits
- **CS-25.853:** Compartment interiors (fire)
- **CS-25.1309:** Equipment, systems, installations
- All CS-25 requirements met or exceeded

## Training Requirements

### Flight Crew

**BWB Type Rating (required):**
- Ground school: 40 hours
  - BWB aerodynamics (8 hours)
  - Flight controls (8 hours)
  - CG management (4 hours)
  - Systems (12 hours)
  - Emergency procedures (8 hours)
- Simulator: 20 hours
  - Normal operations (10 hours)
  - Abnormal/emergency (10 hours)
- Check ride: Type rating examination

**Recurrent (annual):**
- Ground: 4 hours (BWB-specific refresh)
- Simulator: 8 hours (includes BWB emergencies)

### Cabin Crew

**BWB-Specific Training (initial):**
- Cabin layout and evacuation (4 hours)
- BWB exits and equipment (2 hours)
- Demonstration: Evacuation drill

**Recurrent (annual):**
- BWB evacuation procedures (2 hours)
- Hands-on: Annual evacuation demonstration

### Ground Crew

**BWB Ground Handling (initial):**
- Configuration overview (2 hours)
- Towing and pushback (2 hours)
- Clearances and markings (2 hours)
- Practical: Towing exercise

**Recurrent (annual):**
- Refresher (2 hours)

## Continuous Improvement

### Operational Feedback

**Data Collection:**
- Flight crew reports (BWB-specific issues)
- Cabin crew reports (evacuation, passenger issues)
- Maintenance reports (access, procedures)
- CAOS data analysis (CG management, anomalies)

**Analysis:**
- Monthly: Trend analysis
- Quarterly: Safety review
- Annually: Full BWB safety review

**Actions:**
- Procedure updates as needed
- Training enhancements
- Design improvements (if feasible)
- Documentation updates

---

**Document Owner:** Chief Engineer - BWB Integration  
**Next Review Date:** 2026-05-05  
**Configuration Control:** Git SHA-256: [hash]  
**Classification:** Safety Critical - Unclassified
