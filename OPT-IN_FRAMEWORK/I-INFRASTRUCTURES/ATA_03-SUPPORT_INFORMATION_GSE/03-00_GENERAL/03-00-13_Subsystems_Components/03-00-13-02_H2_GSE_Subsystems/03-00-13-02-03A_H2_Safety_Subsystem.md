---
Title: "H₂ Safety Subsystem — ATA 03 Support Information GSE"
Identifier: "AMPEL360-03-00-13-02-03A"
Version: "1.0.0"
Status: "Draft"
AccessLevel: "Internal"
Author: "AMPEL360 Documentation Team"
ResponsibleOrg: "I-INFRASTRUCTURES Chapter Authority"
Language: "en"
CreatedAt: "2025-12-07"
ModifiedAt: "2025-12-07"
Abstract: "Detailed specifications for the Hydrogen Safety Subsystem monitoring and protecting against hydrogen hazards during GSE operations for the AMPEL360 BWB H₂ Hy-E aircraft."
Keywords: ["ATA 03","GSE","Hydrogen Safety","Leak Detection","Fire Suppression","Ground Support"]
Compliance:
  - "ATA iSpec 2200"
  - "SAE AS6968"
  - "ISO 19880-8"
  - "NFPA 2"
Links:
  Parent: "../"
  Siblings:
    - "03-00-13-02-01A_LH2_Storage_Subsystem.md"
    - "03-00-13-02-02A_LH2_Transfer_Subsystem.md"
    - "03-00-13-02-04A_Cryogenic_Control_Subsystem.md"
ChangeLog:
  - { version: "1.0.0", date: "2025-12-07", author: "AMPEL360 Documentation Team", change: "Initial H₂ safety subsystem specification" }
---

# H₂ Safety Subsystem — ATA 03 Support Information GSE

## 1. Purpose

This document specifies the **Hydrogen Safety Subsystem** for ground support equipment serving the AMPEL360 BWB H₂ Hy-E aircraft. The subsystem provides continuous monitoring, detection, alarming, and automated response to hydrogen-related hazards including leaks, fires, overpressure, and unauthorized access during refueling and maintenance operations.

## 2. Scope

### 2.1 Coverage

The H₂ Safety Subsystem encompasses:

1. **Hydrogen Leak Detectors**
   - Fixed point detectors (0-4% H₂ by volume)
   - Portable detectors for personnel
   - Detection sensitivity: 0.1% H₂ (1000 ppm)
   - Response time: < 1 second

2. **Emergency Vent System**
   - Automated emergency venting
   - Vent stack with flame arrestor
   - Dispersion modeling and monitoring
   - Capacity: 500 kg/hour

3. **Grounding Equipment**
   - Static grounding cables and clamps
   - Ground resistance monitoring
   - Requirement: < 0.1 Ω (aircraft to ground)
   - Continuous verification during operations

4. **Safety Interlock System**
   - Programmable safety relay (Category 3, SIL 2)
   - Emergency stop circuits
   - Zone control and access management
   - Integration with all H₂ GSE subsystems

5. **Fire Detection System**
   - UV/IR flame detectors
   - Heat detectors
   - Manual pull stations
   - Integration with airport fire alarm

### 2.2 Out of Scope

- Fire suppression system hardware (covered under [03-00-13-07-02A](../03-00-13-07_GSE_Safety_Subsystems/03-00-13-07-02A_Fire_Suppression_Subsystem.md))
- Aircraft-mounted safety systems
- General airport safety systems (unless integrated with GSE)

## 3. Applicable Documents

| Standard | Application | Link |
|----------|-------------|------|
| **[SAE AS6968](https://www.sae.org/standards/content/as6968/)** | Hydrogen Aircraft Refueling | Safety requirements |
| **[ISO 19880-8](https://www.iso.org/standard/71940.html)** | Gaseous Hydrogen Fueling Stations | Safety system design |
| **[NFPA 2](https://www.nfpa.org/codes-and-standards/all-codes-and-standards/list-of-codes-and-standards/detail?code=2)** | Hydrogen Technologies Code | Safety requirements |
| **[IEC 61508](https://www.iec.ch/functionalsafety/)** | Functional Safety | Safety integrity levels |
| **[ISO 13849-1](https://www.iso.org/standard/69883.html)** | Safety of Machinery | Safety-related control systems |

## 4. Subsystem Description

### 4.1 Overview

The H₂ Safety Subsystem provides multiple layers of protection against hydrogen hazards. It continuously monitors for leaks, provides automated emergency response, ensures proper grounding, enforces safety interlocks, and detects fires. The system is designed to fail-safe, with redundant sensors and automatic shutdown capabilities.

```
┌──────────────────────────────────────────────────────────────┐
│              H₂ Safety Subsystem Architecture                 │
├──────────────────────────────────────────────────────────────┤
│                                                                │
│  ┌────────────────────────────────────────────────────────┐  │
│  │              Leak Detection Network                     │  │
│  │  - Fixed H₂ sensors (n=12): Storage, Transfer, Aircraft│  │
│  │  - Portable H₂ detectors (n=4): Personnel-carried      │  │
│  │  - Detection Range: 0-4% H₂ by volume                  │  │
│  │  - Alarm Threshold: 0.1% H₂ (1000 ppm)                 │  │
│  │  - Trip Threshold: 1.0% H₂ (10,000 ppm, 25% LEL)       │  │
│  └────────────────────────────────────────────────────────┘  │
│                         │                                     │
│                         ▼                                     │
│  ┌────────────────────────────────────────────────────────┐  │
│  │        Safety Interlock System (SIS)                   │  │
│  │  - Programmable Safety Relay (Pilz PNOZ multi)         │  │
│  │  - Category 3, PLd, SIL 2 per IEC 61508                │  │
│  │  - Inputs: Leak detectors, E-stops, zone sensors       │  │
│  │  - Outputs: Valve shutdowns, pump stops, alarms        │  │
│  └────────────────────────────────────────────────────────┘  │
│                         │                                     │
│                         ▼                                     │
│  ┌────────────────────────────────────────────────────────┐  │
│  │          Emergency Response Actions                     │  │
│  │                                                          │  │
│  │  Leak Detected (>0.1% H₂):                             │  │
│  │    → Alarm (visual + audible)                          │  │
│  │    → Notify operators                                  │  │
│  │                                                          │  │
│  │  High Leak (>1.0% H₂):                                 │  │
│  │    → Close all H₂ valves                               │  │
│  │    → Stop all H₂ pumps                                 │  │
│  │    → Activate emergency vent                           │  │
│  │    → Notify fire department                            │  │
│  │    → Evacuate exclusion zone                           │  │
│  │                                                          │  │
│  │  Fire Detected:                                        │  │
│  │    → Emergency shutdown all H₂ systems                 │  │
│  │    → Activate fire suppression (if automatic)          │  │
│  │    → Notify fire department                            │  │
│  │    → Evacuate site                                     │  │
│  └────────────────────────────────────────────────────────┘  │
│                                                                │
│  ┌────────────────────────────────────────────────────────┐  │
│  │              Grounding System                           │  │
│  │  - Aircraft-to-ground cable: 50 mm² copper             │  │
│  │  - Ground clamp: Aircraft structure                    │  │
│  │  - Ground resistance monitor: < 0.1 Ω verified         │  │
│  │  - Continuous monitoring during operations             │  │
│  └────────────────────────────────────────────────────────┘  │
│                                                                │
│  ┌────────────────────────────────────────────────────────┐  │
│  │         Fire Detection System                           │  │
│  │  - UV/IR flame detectors (n=6): Refueling zone         │  │
│  │  - Heat detectors (n=8): Storage, transfer areas       │  │
│  │  - Manual pull stations (n=4): Strategic locations     │  │
│  │  - Integration with airport fire alarm system          │  │
│  └────────────────────────────────────────────────────────┘  │
│                                                                │
└──────────────────────────────────────────────────────────────┘
```

### 4.2 Specifications

#### 4.2.1 Hydrogen Leak Detectors

**Fixed Point Detectors** (12 units total):

| Location | Quantity | Alarm Setpoint | Trip Setpoint | Part Number |
|----------|----------|----------------|---------------|-------------|
| Storage tank area | 4 | 0.1% H₂ | 1.0% H₂ | GSE-H2-03-001-A |
| Transfer pump area | 2 | 0.1% H₂ | 1.0% H₂ | GSE-H2-03-001-A |
| Transfer hose routing | 4 | 0.1% H₂ | 1.0% H₂ | GSE-H2-03-001-A |
| Aircraft connection | 2 | 0.1% H₂ | 1.0% H₂ | GSE-H2-03-001-A |

**Detector Specifications**:
- **Detection Range**: 0-4% H₂ by volume (0-40,000 ppm)
- **Sensitivity**: 0.05% H₂ (500 ppm) minimum detectable
- **Response Time**: < 1 second (T90)
- **Accuracy**: ±10% of reading
- **Operating Temperature**: -40°C to +60°C
- **Output**: 4-20 mA analog + relay contacts
- **Communication**: Modbus RTU
- **Certification**: ATEX Zone 1, IECEx
- **Calibration**: Every 6 months
- **Expected Life**: 5 years (sensor element)

**Portable Detectors** (4 units):
- Carried by personnel during operations
- Similar specifications to fixed detectors
- Battery-powered, 12-hour runtime
- Man-down alarm function

#### 4.2.2 Emergency Vent System

| Parameter | Specification | Notes |
|-----------|---------------|-------|
| **Vent Capacity** | 500 kg/hour | Entire storage tank in 20-30 hours |
| **Vent Line Size** | DN 200 (8 inches) | From storage to vent stack |
| **Vent Stack Height** | 10 meters above ground | Per dispersion modeling |
| **Flame Arrestor** | Integrated in stack | Prevent flashback |
| **Actuation** | Automatic (on high leak or overpressure) | Also manual override |
| **Control Valve** | Fail-open pneumatic valve | Loss of air = vent opens |
| **Discharge Location** | Vertical, open-ended | Upward dispersion |
| **Ignition Source Control** | 10m radius exclusion zone around vent | No ignition sources |

#### 4.2.3 Grounding Equipment

| Parameter | Specification | Notes |
|-----------|---------------|-------|
| **Grounding Cable** | 50 mm² bare copper | Flexible, 10m length |
| **Ground Clamp** | Stainless steel, spring-loaded | Aircraft structure attachment |
| **Ground Lug** | Copper, bolted to ground grid | < 1 Ω grid resistance |
| **Resistance Requirement** | < 0.1 Ω (aircraft to earth) | Measured before each refueling |
| **Resistance Monitor** | Continuous monitoring during ops | Alarm if > 0.15 Ω |
| **Resistance Meter** | Handheld, 4-wire Kelvin method | Verification tool |

#### 4.2.4 Safety Interlock System

| Parameter | Specification | Notes |
|-----------|---------------|-------|
| **Safety Relay** | Pilz PNOZ multi 2 | Configurable safety relay |
| **Safety Category** | Category 3 per ISO 13849-1 | Performance Level d (PLd) |
| **Safety Integrity Level** | SIL 2 per IEC 61508 | For critical functions |
| **Inputs** | 32 digital, 8 analog | Expandable |
| **Outputs** | 16 digital (safety-rated) | Solid-state or relay |
| **Reaction Time** | < 50 ms | From input to output change |
| **Self-Test** | Continuous | Automatic fault detection |
| **Programming** | PAScal (graphical) | User-friendly |

**Interlock Functions**:

| Interlock | Inputs | Outputs | Function |
|-----------|--------|---------|----------|
| **Refueling Permit** | All prerequisites met | Enable H₂ flow valves | AND logic of all conditions |
| **Emergency Stop** | E-stop buttons (4), leak detectors | Shutdown all H₂ systems | OR logic, latching |
| **Zone Control** | Motion sensors, access control | Prevent operations if personnel in zone | Continuous check |
| **Grounding Check** | Ground resistance monitor | Prevent H₂ flow if not grounded | Fail-safe |
| **Fire Alarm** | Fire detectors | Emergency shutdown, activate suppression | Immediate response |

#### 4.2.5 Fire Detection System

**UV/IR Flame Detectors** (6 units):

| Parameter | Specification | Notes |
|-----------|---------------|-------|
| **Detection Method** | UV + IR (dual spectrum) | Reduce false alarms |
| **Detection Range** | 0-30 meters (depending on fire size) | Wide coverage |
| **Field of View** | 90° cone | Strategic placement for overlap |
| **Response Time** | < 5 seconds | From flame appearance to alarm |
| **False Alarm Immunity** | High (welding, sunlight, lightning) | Dual-spectrum advantage |
| **Operating Temperature** | -40°C to +75°C | Outdoor rated |
| **Certification** | ATEX, FM, UL | Explosion-proof |

**Heat Detectors** (8 units):

| Parameter | Specification | Notes |
|-----------|---------------|-------|
| **Type** | Rate-of-rise + fixed temperature | Dual mode |
| **Fixed Temperature** | 68°C (155°F) | Alarm threshold |
| **Rate-of-Rise** | 8°C/minute | Rapid temperature increase |
| **Operating Range** | -40°C to +100°C | Wide range |

**Manual Pull Stations** (4 units):
- Located at strategic egress points
- Red, weather-proof enclosures
- Break-glass operation
- Connects to fire alarm control panel

### 4.3 Part Number Information

| Component | Part Number | Description | Supplier | Interchangeability |
|-----------|-------------|-------------|----------|-------------------|
| Fixed H₂ Detector | GSE-H2-03-001-A | 0-4% H₂, 4-20 mA, Modbus | Dräger | Polytron 8000 series |
| Portable H₂ Detector | GSE-H2-03-002-A | 0-4% H₂, battery, man-down alarm | MSA Safety | ALTAIR 5X H2 |
| Safety Relay System | GSE-H2-03-003-A | PNOZ multi 2, Cat 3, SIL 2 | Pilz | PNOZ multi 2 |
| Emergency Vent Valve | GSE-H2-03-004-A | DN 200, fail-open, pneumatic | Samson AG | Type 3241 |
| Grounding Cable Assy | GSE-H2-03-005-A | 50 mm² copper, 10m, clamps | Custom | N/A |
| Ground Resistance Monitor | GSE-H2-03-006-A | Continuous, 0.01-10 Ω, alarm | Megger | MOM2 |
| UV/IR Flame Detector | GSE-H2-03-007-A | Dual spectrum, 0-30m, ATEX | Det-Tronics | X3301 |
| Heat Detector | GSE-H2-03-008-A | Rate-of-rise + fixed temp | System Sensor | 5602 |
| Manual Pull Station | GSE-H2-03-009-A | Weatherproof, break-glass | Edwards | 270-SPO |

See [03-00-13-03_GSE_Part_Number_Registry](../03-00-13-03_GSE_Part_Number_Registry/) for complete PNR.

## 5. Spare Parts Information

### 5.1 Critical Spare Parts

| Part Number | Description | Criticality | Lead Time | Min Stock |
|-------------|-------------|-------------|-----------|-----------|
| GSE-H2-03-001-A | Fixed H₂ Detector | **Critical** | 8 weeks | 2 units |
| GSE-H2-03-002-A | Portable H₂ Detector | **Critical** | 4 weeks | 1 unit |
| GSE-H2-03-003-A | Safety Relay System | **Critical** | 10 weeks | 1 unit |
| GSE-H2-03-004-A | Emergency Vent Valve | **Critical** | 12 weeks | 1 unit |
| GSE-H2-03-007-A | UV/IR Flame Detector | **Essential** | 6 weeks | 1 unit |
| GSE-H2-03-010-A | H₂ Sensor Element | **Essential** | 4 weeks | 4 elements |
| GSE-H2-03-011-A | E-Stop Button | **Standard** | 2 weeks | 2 units |

See [03-00-13-04_GSE_Spare_Parts_Management](../03-00-13-04_GSE_Spare_Parts_Management/) for complete spare parts strategy.

## 6. Safety Zones and Access Control

### 6.1 Zone Definitions

| Zone | Radius from H₂ Connection | Access | Monitoring |
|------|---------------------------|--------|------------|
| **Exclusion Zone** | 0-10 meters | Essential personnel only, PPE required | Motion sensors, access log |
| **Restricted Zone** | 10-25 meters | Authorized personnel, safety briefing | Visual supervision |
| **Monitored Zone** | 25-50 meters | General airport personnel, awareness | H₂ detectors, cameras |

### 6.2 Personnel Protective Equipment (PPE)

Required for Exclusion Zone entry:
- Fire-resistant clothing (Nomex or equivalent)
- Safety glasses with side shields
- Steel-toed safety boots
- Portable H₂ detector (personal)
- Two-way radio for communication

## 7. Operational Procedures

### 7.1 Pre-Operational Safety Checks

| Check | Procedure | Accept Criteria | Frequency |
|-------|-----------|-----------------|-----------|
| **H₂ Detector Function Test** | Bump test with calibration gas | Alarm activates at 0.1% H₂ | Daily, before operations |
| **Grounding Verification** | Measure aircraft-to-ground resistance | < 0.1 Ω | Before each refueling |
| **E-Stop Function Test** | Press E-stop, verify all shutdowns | All H₂ systems de-energized | Weekly |
| **Fire Detector Test** | Use test lamp (UV/IR) or heat source | Alarm activates within 5 seconds | Monthly |
| **Emergency Vent Test** | Stroke valve (no actual venting) | Valve opens/closes smoothly | Quarterly |

### 7.2 Emergency Response Procedures

#### 7.2.1 Hydrogen Leak Response

1. **Alarm Activation**: Audible and visual alarms, HMI displays leak location
2. **Immediate Actions**:
   - Do NOT activate E-stop unless leak is severe (> 1% H₂) — this may create spark
   - Evacuate non-essential personnel from exclusion zone
   - Eliminate ignition sources (no vehicles, no electrical switching)
3. **If leak < 1% H₂**:
   - Investigate source with portable detector
   - Attempt to isolate leak (close manual valves if safe)
   - Ventilate area naturally (do not use fans — spark risk)
   - Monitor until H₂ concentration < 0.05%
4. **If leak ≥ 1% H₂** (automatic system response):
   - All H₂ valves close automatically
   - All H₂ pumps stop automatically
   - Emergency vent activates (if overpressure)
   - Fire department notified automatically
   - Evacuate all personnel to safe distance (> 100m)
5. **After leak resolved**:
   - Purge all H₂ systems with GN₂
   - Repair leak source
   - Re-test before return to service

#### 7.2.2 Fire Response

1. **Fire Detected**: Automatic or manual alarm activation
2. **Automatic System Actions**:
   - Emergency shutdown all H₂ systems
   - Activate fire suppression (if automatic system installed)
   - Notify fire department (automatic call)
3. **Personnel Actions**:
   - Evacuate all personnel immediately
   - Do NOT attempt to fight hydrogen fire unless trained
   - Establish exclusion perimeter (minimum 100m)
   - Allow hydrogen to burn if safe (better than explosive cloud)
4. **Fire Department Actions**:
   - Approach from upwind
   - Cool surrounding equipment with water spray
   - Do NOT extinguish hydrogen fire unless fuel source can be stopped
5. **After fire extinguished**:
   - Investigate cause
   - Assess damage
   - Repair/replace damaged components
   - Test all safety systems before return to service

## 8. Maintenance Requirements

### 8.1 Routine Inspections

| Inspection | Frequency | Procedure |
|------------|-----------|-----------|
| Visual inspection of detectors | Weekly | Check for physical damage, obstructions |
| H₂ detector bump test | Daily (before ops) | Expose to 1% H₂ gas, verify alarm |
| H₂ detector calibration | Every 6 months | Full 2-point calibration (0%, 2% H₂) |
| Safety relay function test | Monthly | Simulate alarm conditions, verify shutdowns |
| Grounding equipment inspection | Monthly | Check cable, clamps for damage, corrosion |
| Fire detector function test | Monthly | Use test equipment per manufacturer |
| Manual pull station test | Quarterly | Activate station, verify alarm |

### 8.2 Preventive Maintenance

| Task | Frequency | Estimated Duration |
|------|-----------|-------------------|
| Replace H₂ sensor elements | 5 years (or per manufacturer) | 1 hour per sensor |
| Safety relay system upgrade (firmware) | As released | 2 hours |
| Fire detector cleaning | Annually | 30 minutes per detector |
| Emergency vent valve overhaul | 5 years | Send to OEM |
| Grounding cable replacement | As needed (if damaged) | 1 hour |

## 9. Cross-References

### 9.1 Related ATA Chapters

- [ATA 02 — Operations Information](../../../../../ATA_02-OPERATIONS_INFORMATION/) — Emergency procedures
- [ATA 85 — Infrastructure Interface Standards](../../../../../ATA_85-INFRASTRUCTURE_INTERFACE_STANDARDS/) — Airport safety systems

### 9.2 Related Documents

- [03-00-13-01-01A_GSE_Subsystem_Overview](../03-00-13-01_GSE_Subsystem_Architecture/03-00-13-01-01A_GSE_Subsystem_Overview.md)
- [03-00-13-02-01A_LH2_Storage_Subsystem](./03-00-13-02-01A_LH2_Storage_Subsystem.md)
- [03-00-13-02-02A_LH2_Transfer_Subsystem](./03-00-13-02-02A_LH2_Transfer_Subsystem.md)
- [03-00-13-02-04A_Cryogenic_Control_Subsystem](./03-00-13-02-04A_Cryogenic_Control_Subsystem.md)
- [03-00-13-07_GSE_Safety_Subsystems](../03-00-13-07_GSE_Safety_Subsystems/) — Additional safety subsystems
- [03-00-02_Safety](../../03-00-02_Safety/) — Safety assessments

### 9.3 Parent Document

- [03-00-13_Subsystems_Components](../) — Top-level subsystems directory

## 10. Revision History

| Rev | Date | Author | Description |
|-----|------|--------|-------------|
| A | 2025-12-07 | AMPEL360 Documentation Team | Initial release |

---

## Document Control

- **Document ID**: 03-00-13-02-03A
- **Version**: 1.0.0
- **Status**: DRAFT — Subject to human review and approval
- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**
- **Human approver**: _[to be completed]_
- **Repository**: `AMPEL360-BWB-H2-Hy-E`
- **Last AI update**: 2025-12-07
- **Classification**: Internal Use
- **Owner**: AMPEL360 Ground Support Equipment WG

---
