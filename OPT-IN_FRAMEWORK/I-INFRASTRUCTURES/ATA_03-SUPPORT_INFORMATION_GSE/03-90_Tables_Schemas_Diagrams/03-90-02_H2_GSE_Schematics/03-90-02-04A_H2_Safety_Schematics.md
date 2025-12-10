# 03-90-02-04A - H2 Safety Schematics

## 1. Purpose

This document establishes standards for safety system schematics specific to hydrogen Ground Support Equipment, covering detection, protection, emergency shutdown, and response systems critical for safe hydrogen operations.

## 2. Scope

This specification covers safety schematics for:
- Hydrogen gas detection systems
- Fire detection and suppression systems
- Emergency shutdown (ESD) systems
- Overpressure protection and relief
- Ventilation and dilution systems
- Emergency response and evacuation
- Safety interlocks and permissives

## 3. Applicable Documents

- [NFPA 2](https://www.nfpa.org/codes-and-standards/all-codes-and-standards/list-of-codes-and-standards/detail?code=2) - Hydrogen Technologies Code
- [ISO 22734](https://www.iso.org/standard/62177.html) - Hydrogen Generators Using Water Electrolysis - Safety
- [IEC 60079](https://www.iec.ch/) - Explosive Atmospheres Standards
- [ISO/TR 15916](https://www.iso.org/standard/29316.html) - Basic Considerations for Safety of Hydrogen Systems
- [CGA G-5.5](https://www.cganet.com/) - Hydrogen Vent Systems
- [EN 60079-10-1](https://www.en-standard.eu/) - Classification of Areas - Explosive Gas Atmospheres
- [ISA 84](https://www.isa.org/standards-and-publications/isa-standards/isa-standards-committees/isa84) - Safety Instrumented Systems

## 4. Documentation Description

### 4.1 Overview

H2 safety schematics provide critical information for:
- Safety system design and verification
- Installation and commissioning
- Operational safety procedures
- Emergency response planning
- Regulatory compliance and audits
- Training of operations and safety personnel

Safety is the paramount concern for all hydrogen systems.

### 4.2 Format and Structure

| Element | Format | Standard |
|---------|--------|----------|
| Safety Functions | Red borders/highlights | Industry practice |
| Interlock Logic | Ladder logic or function blocks | ISA-5.1, IEC 61131-3 |
| Detection Zones | Shaded areas on layout | Hazardous area classification |
| Alarm Hierarchy | Priority levels (critical, high, low) | ISA 18.2 |
| SIL Ratings | Safety Integrity Level notation | IEC 61508, ISA 84 |

### 4.3 Content Requirements

#### 4.3.1 Hydrogen Gas Detection System

**Detection Technology:**

| Detector Type | Principle | Range | Response Time | Application |
|---------------|-----------|-------|---------------|-------------|
| Catalytic Bead | Combustion | 0-100% LEL | < 30 sec | General area |
| Electrochemical | Oxidation | 0-1000 ppm | < 15 sec | Enclosed spaces |
| Thermal Conductivity | Heat transfer | 0-100% vol | < 5 sec | High concentration |
| Optical (IR) | Absorption | 0-100% LEL | < 3 sec | Open areas |

**H2 Flammability:**
- Lower Explosive Limit (LEL): 4% vol in air
- Upper Explosive Limit (UEL): 75% vol in air
- Most sensitive range: 18-59% vol (stoichiometric ~29%)

**Detector Placement Strategy:**

**Zone Classification:**
- **Zone 0**: H2 present continuously or long periods
- **Zone 1**: H2 likely during normal operations
- **Zone 2**: H2 not likely, or only briefly

**Placement Guidelines:**
| Location | Height | Spacing | Qty |
|----------|--------|---------|-----|
| LH2 Storage | High (H2 rises) & low (cold gas sink) | 7.5m max | Per zone |
| Transfer Areas | High & mid-level | 5m max | Per zone |
| Indoor Spaces | High near vents | 10m max | Per room |
| Leak-Prone Areas | Flanges, valves, connections | 1m radius | Each major |

**Alarm Setpoints:**
- **Low Alarm**: 10% LEL (0.4% vol H2)
- **High Alarm**: 25% LEL (1.0% vol H2)
- **Evacuation**: 40% LEL (1.6% vol H2)

**Detector Wiring:**
- Intrinsically safe (IS) circuits for Zone 0, 1
- Addressable or zoned system
- Fault monitoring (open circuit, short circuit, detector failure)

#### 4.3.2 Fire Detection System

**Detection Methods:**

| Type | Principle | Coverage | Response Time |
|------|-----------|----------|---------------|
| UV/IR Flame | Radiation spectrum | Line-of-sight | < 5 sec |
| Heat (Rate-of-Rise) | Thermal | Area | 30-60 sec |
| Heat (Fixed Temp) | Thermal threshold | Area | 60-120 sec |
| Linear Heat | Fiber optic or cable | Linear runs | 10-30 sec |

**H2 Fire Characteristics:**
- Nearly invisible flame (daytime)
- Low radiant heat
- High flame temperature (~2000°C)
- UV detection preferred

**Fire Detector Placement:**
- Along piping runs (linear heat detection)
- Equipment areas (UV/IR detectors)
- High fire risk zones (transfer, dispensing)
- Overlapping coverage for redundancy

**Fire Detection Logic:**
- Single detector activation → Investigation alarm
- Two detectors in zone → Fire alarm
- Manual pull stations → Immediate fire alarm

#### 4.3.3 Emergency Shutdown (ESD) System

**ESD Architecture:**

**Safety Integrity Level (SIL):**
- SIL 2 minimum for H2 systems per risk assessment
- SIL 3 for large scale storage and aircraft fueling

**ESD Levels:**

| Level | Trigger | Action | Response Time |
|-------|---------|--------|---------------|
| ESD-1 | Process upset | Controlled shutdown | 30-60 sec |
| ESD-2 | High H2 detection (25% LEL) | Section isolation | 5-10 sec |
| ESD-3 | Fire or critical alarm | Full system shutdown | < 3 sec |
| ESD-Manual | Manual activation (E-stop) | Full system shutdown | < 3 sec |

**ESD Actions:**

**Automatic Actions:**
1. Close all Emergency Shutoff Valves (ESV/XV)
2. Stop all transfer pumps and compressors
3. Depressurize piping (vent to safe location)
4. De-energize electrical equipment (in hazardous zones)
5. Activate ventilation (if enclosed areas)
6. Activate fire suppression (if fire detected)
7. Sound alarms and activate beacons
8. Notify control room and emergency contacts

**ESV Valve Specifications:**
- Type: Ball or plug valve, fail-safe closed
- Actuation: Pneumatic (spring return) or solenoid
- Closure time: < 3 seconds
- Position indication: Limit switches
- Manual override: Lockable in closed position

**ESD Logic Diagram:**
```
[H2 Detector > 25% LEL] OR [Fire Detected] OR [E-Stop Pressed]
    ↓
[ESD Controller Activated (2oo3 voting)]
    ↓
[Close ESV-001, ESV-002, ESV-003...] AND [Stop Pumps] AND [Vent System]
    ↓
[Activate Alarms and Beacons]
```

#### 4.3.4 Overpressure Protection

**Relief Valve Hierarchy:**

| Device | Type | Set Pressure | Capacity | Discharge |
|--------|------|--------------|----------|-----------|
| Primary PRV | Spring-loaded | 100% design P | 100% required | Vent stack |
| Secondary PRV | Spring-loaded | 105% design P | 100% required | Vent stack |
| Rupture Disk | Burst disk | 110% design P | 150% required | Vent stack |

**Relief Sizing Basis:**
- **Fire scenario**: External fire exposure
- **Blocked outlet**: No flow exit scenario
- **Runaway pressure build**: Vaporizer failure
- **Thermal expansion**: Trapped liquid scenario

**Vent Stack Requirements:**
- Height per dispersion modeling (typically > 5m above structures)
- Diameter per flow capacity (minimize backpressure)
- No ignition sources within 3m radius
- Lightning protection
- Visual/audible alarm on venting

**Relief Discharge Collection:**
- Route to safe location (away from equipment, buildings)
- Consider H2 buoyancy (rises rapidly)
- Ensure adequate dispersion
- Monitor discharge (pressure or flow sensor)

#### 4.3.5 Ventilation and Dilution Systems

**Ventilation Requirements:**

**Enclosed Spaces:**
- Minimum 4 air changes per hour (ACH) normal
- 12 ACH when H2 detected > 10% LEL
- Exhaust at high points (H2 accumulation)
- Interlocked with H2 detection system
- Backup power for fans

**Outdoor/Semi-Enclosed:**
- Natural ventilation preferred
- Mechanical ventilation if natural inadequate
- Prevent dead zones where H2 can accumulate

**Ventilation Interlock:**
```
IF [H2 > 10% LEL] THEN [Activate High-Speed Ventilation]
IF [H2 > 40% LEL] THEN [Activate ESD] AND [Evacuate Area]
IF [Ventilation Failure] THEN [Alarm] AND [Suspend H2 Operations]
```

#### 4.3.6 Safety Interlocks and Permissives

**Transfer Operation Interlocks:**

**Pre-Transfer Checks (Permissives):**
- [ ] All manual valves in correct position
- [ ] Receiver tank has capacity
- [ ] H2 detection system operational
- [ ] Fire detection system operational
- [ ] Emergency shutdown tested
- [ ] Personnel clear of area
- [ ] Weather conditions acceptable (wind, lightning)

**During Transfer Interlocks:**
- IF [High H2 detected] THEN [Stop Transfer] + [ESD-2]
- IF [Fire detected] THEN [Stop Transfer] + [ESD-3]
- IF [Overfill detected] THEN [Stop Transfer]
- IF [Pressure excursion] THEN [Stop Transfer]
- IF [Communication lost] THEN [Stop Transfer]

**Lockout/Tagout (LOTO):**
- Electrical isolation points shown
- Mechanical isolation (valve lockout) points
- Energy dissipation (depressurization, drainage)
- Stored energy warnings (pressure, vacuum, cold)

#### 4.3.7 Personal Safety Systems

**Safety Showers and Eyewash:**
- Location per ANSI Z358.1 (within 10 seconds travel)
- Freeze-protected (if outdoor)
- Marked with signs
- Weekly activation test

**Emergency Breathing Apparatus:**
- Self-Contained Breathing Apparatus (SCBA) stations
- Quantity based on personnel count
- Maintenance and inspection schedule

**Fire Extinguishers:**
- Class D (suitable for H2 fires)
- Location per NFPA 10
- Inspection tags current

**Safety Signage:**
- "Hydrogen - No Smoking - No Open Flames"
- "Cryogenic Hazard - Cold Burns"
- "High Pressure"
- "Authorized Personnel Only"
- Emergency contact information

#### 4.3.8 Emergency Response Schematic

**Evacuation Routes:**
- Primary and secondary routes
- Assembly points (upwind locations)
- Evacuation alarm (distinct from fire alarm)

**Emergency Shutdown Stations:**
- E-stop button locations
- Manual valve closure locations
- Communication points (phone, radio)

**Emergency Response Equipment:**
- Foam/water monitors for cooling
- Thermal imaging cameras (H2 flame invisible)
- Portable H2 detectors
- Emergency lighting

**Emergency Communication:**
- Direct line to control room
- Radio channels
- Public address (PA) system
- Emergency notification system (ENS)

**Fire Brigade Interface:**
- Fire department pre-plan
- Hydrant and water supply locations
- Emergency responder training
- Access for emergency vehicles

### 4.4 Safety Instrumented Function (SIF) Documentation

For each SIF, document:

| Attribute | Example |
|-----------|---------|
| SIF ID | SIF-001 |
| Description | ESD on high H2 detection |
| SIL Target | SIL 2 |
| Sensors | 3× H2 detectors (2oo3 voting) |
| Logic Solver | Safety PLC |
| Final Elements | 4× ESV valves |
| Proof Test Interval | 12 months |
| Spurious Trip Rate | < 0.1 per year |

### 4.5 Safety Documentation Requirements

All safety schematics must include:

- **Safety Data Sheets (SDS)**: For hydrogen and other hazardous materials
- **Hazard and Operability (HAZOP) Study**: Results and recommendations
- **Layer of Protection Analysis (LOPA)**: Risk reduction measures
- **Safety Integrity Level (SIL) Verification**: Calculations and proof
- **Pre-Startup Safety Review (PSSR)**: Checklist and sign-off
- **Emergency Response Plan (ERP)**: Procedures and contact list

## 5. Cross-References

- Related ATA Chapters: ATA 12 (Servicing), ATA 26 (Fire Protection)
- Parent Document: [03-90_Tables_Schemas_Diagrams](../README.md)
- Related Documents:
  - [03-90-02-01A LH2 System Schematics](./03-90-02-01A_LH2_System_Schematics.md)
  - [03-90-02-03A Cryogenic Flow Diagrams](./03-90-02-03A_Cryogenic_Flow_Diagrams.md)
  - [03-90-05-01A LH2 Fueling PFD](../03-90-05_Process_Flow_Diagrams/03-90-05-01A_LH2_Fueling_PFD.md)
  - [03-90-10 Operations](../../03-10_Operations/README.md)

## 6. Revision History

| Rev | Date | Author | Description |
|-----|------|--------|-------------|
| A | 2025-12-08 | AMPEL360 H2 Safety Engineering | Initial release |

---

## Document Control

- **Generated with the assistance of AI** (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- **Status**: DRAFT – Subject to human review and approval.
- **Human approver**: _[to be completed]_.
- **Repository**: `AMPEL360-BWB-H2-Hy-E`
- **Last AI update**: 2025-12-08.

---
