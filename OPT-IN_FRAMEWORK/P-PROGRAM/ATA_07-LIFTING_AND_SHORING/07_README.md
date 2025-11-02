# ATA 07: Lifting and Shoring

**PROGRAM CHAPTER STATUS:** ATA 07 establishes the procedures, equipment specifications, and safety requirements for lifting and supporting the AMPEL360 aircraft during maintenance operations. This chapter is critical for safe aircraft servicing, including landing gear maintenance, weight and balance operations, and major structural work.

## Scope and Structure
This chapter documents all aspects of aircraft lifting and shoring operations, including:
- **Jack Point Locations:** Certified locations for aircraft jacks
- **Jacking Procedures:** Step-by-step procedures for raising aircraft
- **Jack Specifications:** Equipment requirements and capacities
- **Shoring Requirements:** Support structures for extended maintenance
- **Safety Procedures:** Hazard mitigation and emergency response
- **Special Considerations:** Hydrogen system precautions, composite structure protection

## The 14-Folder Skeleton
Every 6-digit component within this chapter represents a formal lifting/shoring procedure or equipment specification. Each component is managed through the full lifecycle skeleton to ensure requirements traceability, design verification, procedure validation, and safety compliance.

## Regulatory Framework

### Certification Requirements
- **CS-25.1529:** Instructions for Continued Airworthiness (ICA)
- **FAA AC 43-13-1B:** Acceptable Methods, Techniques, and Practices - Aircraft Inspection and Repair
- **EASA Part-M.A.402:** Performance of Maintenance
- **SAE ARP1247:** Aircraft Jacking Points and Procedures
- **MIL-STD-882E:** System Safety (jacking hazard analysis)

### Industry Standards
- **ATA iSpec 2200 Chapter 07:** Standard jacking procedures format
- **SAE AS478:** Hydraulic Hand Jacks for Aircraft Maintenance
- **ISO 11228:** Ergonomics - Manual Handling
- **OSHA 1926.502:** Fall Protection Systems
- **NFPA 409:** Aircraft Hangars (hydrogen safety during maintenance)

## AMPEL360 Unique Characteristics

### 1. **Blended Wing Body (BWB) Structure**
The AMPEL360 has no conventional fuselage, creating unique lifting challenges:

**Structural Load Paths:**
- **Center Body:** Primary structure integrates wing box and passenger cabin
- **Wing Carry-Through:** Continuous spar structure (no discrete fuselage frame)
- **Distributed Loading:** Jack loads distributed across wider area than conventional aircraft
- **Composite Construction:** Carbon fiber structure requires special jack pad design

**Jacking Strategy:**
- **Three-Point Jacking:** One nose jack + two main jacks (conventional approach maintained)
- **Jack Point Selection:** Located at major structural hard points (landing gear attachment frames)
- **Load Distribution:** Jack pads designed for composite structure (larger contact area)

### 2. **Hydrogen System Safety**
Cryogenic LH₂ system presents unique hazards during jacking operations:

**Mandatory Pre-Jacking Requirements:**
1. **LH₂ Tank Depressurization:** Reduce tank pressure to ≤0.2 bar (near-atmospheric)
2. **Hydrogen Venting:** Vent residual H₂ to atmosphere via dedicated ground vent line
3. **Nitrogen Purge:** Purge all H₂ lines with GN₂ until O₂ content <2% (explosion prevention)
4. **Thermal Stabilization:** Allow structure to warm to ambient temperature (30 min minimum)
5. **Leak Check:** Verify no hydrogen leaks with portable H₂ detector (<10 ppm)

**Safety Zones During Jacking:**
- **Hot Work Prohibited:** No welding, grinding, or spark-producing activities within 15m
- **Smoking Prohibited:** 25m radius from aircraft
- **Portable H₂ Detectors:** Continuous monitoring (alarm set at 10% LEL - 400 ppm)
- **Fire Extinguishers:** CO₂ or dry chemical extinguishers staged at each jack point

**Structural Considerations:**
- Hydrogen tank support structure must not be compromised during jacking
- Tank thermal contraction/expansion must be accommodated (±10mm movement)
- Vacuum jacket integrity must be maintained (no excessive loading)

### 3. **Composite Structure Protection**
Carbon fiber composite airframe requires different handling than aluminum:

**Jack Pad Design:**
- **Contact Area:** 400 cm² minimum (vs. 200 cm² for metal aircraft)
- **Material:** Aluminum alloy with neoprene rubber face (Shore A 60 durometer)
- **Load Distribution:** Prevents point loading that could cause composite delamination
- **Inspection:** Visual check for damage before each use

**Composite Surface Protection:**
- **Protective Sheeting:** Lay down rubber mats under jack stands
- **Edge Protection:** Foam padding on jack stand edges (prevent accidental contact)
- **FOD Control:** Absolute prohibition on dropping tools/equipment on composite surfaces

### 4. **Upper-Surface Propulsors**
Twin propulsors mounted above BWB center body affect jacking operations:

**Clearance Requirements:**
- **Vertical Clearance:** 4.5m minimum ceiling height required (propulsor top to hangar ceiling)
- **Work Platform Access:** Elevated platforms needed for propulsor maintenance (when jacked)
- **Propulsor Rotation:** Blades must be secured (prevent rotation during jacking)

**Safety Precautions:**
- Propulsors must be electrically isolated (high-voltage disconnect)
- Fuel cell system must be shut down and purged
- Rotational locks installed on propulsor shafts

### 5. **Wide Center Body Geometry**
BWB center body width (22.5m) requires special considerations:

**Jack Positioning:**
- **Main Jack Lateral Spacing:** 15.6m (main landing gear track width)
- **Jack Stability:** Wide stance provides excellent stability (vs. narrow-body aircraft)
- **Floor Loading:** Hangar floor must support distributed load (jack point loads + aircraft weight)

**Advantages:**
- Lower center of gravity (more stable when jacked)
- Reduced roll instability compared to conventional aircraft
- Easier access to center body components when jacked

## Jack Point Specifications

### Primary Jack Points

| Jack Point | Location (BRS) | Capacity | Type |
|------------|----------------|----------|------|
| **Nose Jack** | FS 6,500 / BL 0 / WL 2,800 | 200 kN | Axial |
| **Main Jack (Left)** | FS 23,800 / BL -7,800 / WL 3,200 | 550 kN | Axial |
| **Main Jack (Right)** | FS 23,800 / BL +7,800 / WL 3,200 | 550 kN | Axial |

**Total Jacking Capacity Required:** 1,300 kN (133 metric tons) - supports MTOW 120,000 kg with safety factor

### Secondary Jack Points (Contingency)

| Jack Point | Location (BRS) | Capacity | Usage |
|------------|----------------|----------|-------|
| **Auxiliary Nose** | FS 4,500 / BL 0 / WL 2,600 | 150 kN | Emergency/recovery |
| **Wing Root (Left)** | FS 20,000 / BL -10,000 / WL 4,000 | 300 kN | Wing change |
| **Wing Root (Right)** | FS 20,000 / BL +10,000 / WL 4,000 | 300 kN | Wing change |

## Jacking Procedures Overview

### Standard Three-Point Jacking Sequence

1. **Pre-Jacking Preparation (2 hours):**
   - Aircraft positioned on level surface (±0.5° max slope)
   - Parking brake set, wheel chocks installed
   - LH₂ system depressurized and purged (H₂ safety protocol)
   - Electrical power off, hydraulic pressure relieved
   - Landing gear safety pins installed

2. **Jack Setup (1 hour):**
   - Position jacks at certified jack points (verify location with jack pad adapters)
   - Install jack pads (torque bolts to 150 Nm)
   - Verify jack alignment (plumb within 2°)
   - Connect jack synchronization system (hydraulic manifold)

3. **Initial Lift (30 minutes):**
   - Raise aircraft 50mm (verify all jacks lifting evenly)
   - Stop and inspect: check jack stability, look for structural distress
   - Install safety stands (minimum 2 stands, positioned at shoring points)

4. **Full Jacking (30 minutes):**
   - Raise aircraft to required height (typically 500mm wheel clearance)
   - Landing gear extended: jack to 800mm wheel clearance
   - Final height verification and leveling check (±0.1° tolerance)

5. **Securing (30 minutes):**
   - Install additional safety stands (minimum 4 total for extended maintenance)
   - Install landing gear retraction locks (if gear being cycled)
   - Post warning placards: "AIRCRAFT ON JACKS - DO NOT ENTER"

6. **Lowering (1 hour):**
   - Remove safety stands (leave minimum 2 until aircraft on wheels)
   - Lower aircraft slowly and evenly (check for unusual noises/movement)
   - When wheels contact ground, continue lowering to compress struts normally
   - Remove jacks, jack pads, safety pins
   - Perform post-jacking inspection

**Total Time:** ~5.5 hours (for routine jacking with experienced crew)

## Safety Requirements

### Personnel Qualifications
- **Jack Operator:** Must be certified on aircraft type and jack equipment (40-hour course)
- **Supervisor:** Must hold Type Rating or equivalent maintenance authorization
- **Minimum Crew:** 4 personnel (1 supervisor + 3 operators)

### Personal Protective Equipment (PPE)
- **Mandatory:** Safety shoes (steel toe), safety glasses, hearing protection
- **Recommended:** Hard hat (overhead work), high-visibility vest
- **Hydrogen Work:** FR (flame-resistant) coveralls, leather gloves, face shield

### Emergency Procedures

**Jack Failure Scenario:**
1. Immediately stop all jacking operations
2. Activate emergency lowering system (if equipped)
3. Evacuate personnel from under aircraft
4. Stabilize aircraft with emergency shoring (pre-positioned cribbing)
5. Investigate failure cause before resuming

**Hydrogen Leak Scenario:**
1. Portable H₂ detector alarm (>400 ppm)
2. Immediately evacuate hangar (personnel to muster point 50m upwind)
3. Activate emergency ventilation (exhaust fans)
4. Notify emergency response team
5. Do not re-enter until H₂ level <10 ppm (confirmed by emergency responders)

## Equipment Specifications

### Hydraulic Jacks
- **Type:** Tripod hydraulic jacks (stable, self-supporting)
- **Capacity:** 600 kN (60 metric tons) minimum per jack
- **Lift Range:** 500-1,200mm
- **Safety Features:** Mechanical load-holding device (independent of hydraulic pressure)
- **Synchronization:** Hydraulic manifold ensures all jacks lift at same rate

**Approved Jacks (Pre-Qualified List):**
- Tronair 02-7870-0000 (60-ton tripod jack)
- Hydraulics International HJ-60 (60-ton jack)
- Malabar 9001 (heavy-duty aircraft jack)

### Jack Pads (Aircraft Interface)
- **Part Number:** AMPEL-07-JP-001 (nose), AMPEL-07-JP-002 (main)
- **Material:** Aluminum 7075-T6 alloy with bonded rubber face
- **Dimensions:** 200mm diameter × 50mm thick
- **Attachment:** 4× M12 bolts (torque 150 Nm)
- **Inspection Interval:** Visual inspection before each use, NDT every 500 jacking cycles

### Safety Stands (Shoring)
- **Type:** Adjustable tripod stands with locking pins
- **Capacity:** 300 kN (30 metric tons) per stand
- **Height Range:** 400-1,000mm
- **Quantity Required:** Minimum 4 stands for routine jacking, 8 stands for extended maintenance

### Leveling Equipment
- **Digital Inclinometer:** ±0.05° accuracy (wireless, mounted on aircraft during jacking)
- **Spirit Levels:** Backup verification (2× 600mm precision levels)
- **Laser Alignment System:** Optional (for precision leveling during weighing operations)

## Integration with Other Chapters

### Data Flows
```
ATA 07 (Lifting/Shoring)
    ↓ Jack Point Locations → ATA 06 (Dimensions), ATA 51 (Structures)
    ↓ Safety Procedures → ATA 12 (Servicing), ATA 20 (Standard Practices)
    ↓ H2 Safety Protocol → ATA 28 (Fuel System)
    ↓ Weight Condition → ATA 08 (Weighing)
    ↓ Equipment Specs → ATA 13 (Hardware/Tools)
```

### Cross-References
- **ATA 06-10:** Overall Dimensions (jack point coordinates)
- **ATA 08-10:** Weighing Procedures (jacking for weighing operations)
- **ATA 09-10:** Towing (aircraft must be lowered for towing)
- **ATA 12:** Servicing (some servicing requires jacked aircraft)
- **ATA 20:** Standard Practices - Airframe (composite handling)
- **ATA 28-00:** LH₂ System Safety (purging procedures)
- **ATA 32:** Landing Gear (gear retraction during maintenance)
- **ATA 51-10:** Structural Access (jacking for structural inspection)

## Special Procedures

### Landing Gear Retraction Test (On Jacks)
**Procedure:** AMM 07-20-00-710-001

1. Aircraft jacked to 800mm wheel clearance (full gear extension)
2. Landing gear safety pins removed
3. Hydraulic pressure applied (3,000 psi)
4. Retract landing gear (verify proper sequencing and lock indication)
5. Visual inspection of gear bay (no hydraulic leaks, proper door operation)
6. Extend landing gear (verify down-and-locked indication)
7. Reinstall safety pins before lowering aircraft

**Safety Critical:** Aircraft must be on minimum 4 safety stands during gear retraction

### Wing Change (Major Structural Work)
**Procedure:** AMM 07-40-00-400-001

1. Aircraft jacked at three primary points
2. Wing root jack points engaged (secondary jacks)
3. Wing attach bolts progressively removed
4. Wing lowered onto dedicated shipping fixture
5. Replacement wing raised into position
6. Attach bolts installed and torqued per structural manual

**Special Tools Required:**
- Wing alignment jig (P/N AMPEL-07-WJ-001)
- Wing shipping fixture (P/N AMPEL-07-WSF-001)
- Hydraulic wing lift table (capacity: 8,000 kg)

### Hydrogen Tank Removal (On Jacks)
**Procedure:** AMM 07-50-00-400-001

1. LH₂ tank completely drained and purged (GN₂)
2. Aircraft jacked to 600mm wheel clearance
3. Belly fairing panels removed (ATA 53)
4. Tank support attachments disconnected
5. Tank lowered using specialized lifting fixture (P/N AMPEL-07-TL-001)
6. Tank removed through belly opening

**Critical Safety:** H₂ detector continuously monitoring throughout procedure

## Quality Assurance

### Pre-Jacking Inspection Checklist
- [ ] Jack equipment inspected (hydraulic leaks, mechanical integrity)
- [ ] Jack pads inspected (no cracks, rubber face intact)
- [ ] Hangar floor level (±0.5° verified with spirit level)
- [ ] Aircraft weight within jacking limits (verify actual weight)
- [ ] LH₂ system depressurized and purged (H₂ detector confirms <10 ppm)
- [ ] Landing gear safety pins installed
- [ ] Wheel chocks installed
- [ ] Emergency equipment staged (shoring cribbing, fire extinguishers)

### During Jacking Monitoring
- **Visual Inspection:** Continuous monitoring of jack stability during lift
- **Height Verification:** All jacks rising evenly (±10mm tolerance)
- **Structural Check:** No unusual noises, no visible distress in airframe
- **Level Check:** Aircraft attitude within ±0.5° of level

### Post-Jacking Inspection
- [ ] Landing gear visual inspection (no damage during gear cycling)
- [ ] Jack point inspection (no cracks or deformation)
- [ ] Hydraulic system check (no leaks introduced during maintenance)
- [ ] Functional checks completed (as applicable to maintenance performed)
- [ ] Aircraft logbook entry: "Aircraft jacked per AMM 07-XX-XX. Post-jacking inspection completed. No discrepancies noted."

## Document Hierarchy
```
ATA 07 (This Chapter)
├── Jacking and Shoring Manual (JSM)
├── Jack Point Identification Drawing
├── Jacking Procedure (AMM Section 07)
├── Jack Equipment Specification
├── Safety Risk Assessment (Jacking Operations)
├── Hydrogen Safety Protocol (Jacking Supplement)
├── Personnel Training Curriculum
└── Emergency Response Procedures
```

## Revision Control
Changes to ATA 07 procedures require:
1. **Engineering Analysis:** Stress analysis if jack point locations change
2. **Safety Assessment:** Update hazard analysis for procedure changes
3. **Regulatory Approval:** EASA/FAA review if affects type design
4. **Operator Training:** Personnel requalification for major procedure changes
5. **Service Bulletin:** Formal notification to all operators

## Future Enhancements
- **Automated Jacking System:** Synchronized electric jacks with load cells (eliminates manual manifold)
- **AR Guidance System:** Augmented reality overlay showing jack point locations
- **Real-Time Monitoring:** Load cells + inclinometers streaming to tablet (operator awareness)
- **Predictive Maintenance:** Jack equipment health monitoring (hydraulic fluid analysis, structural NDT)
