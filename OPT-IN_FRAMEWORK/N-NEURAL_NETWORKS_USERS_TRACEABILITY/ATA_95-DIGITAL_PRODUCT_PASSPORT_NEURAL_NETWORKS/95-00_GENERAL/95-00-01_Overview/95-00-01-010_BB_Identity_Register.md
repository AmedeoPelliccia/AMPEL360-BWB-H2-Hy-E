---
document_id: 95-00-01-010
title: Body+Brain Identity Register
subtitle: Scalable CCert/CVal Circuit + Fleet Register for Embedded-Intelligence Artifacts
version: 1.2
date: 2025-12-13
status: WORKING DRAFT
owner: AMPEL360 / ATA 95 Governance
classification: INTERNAL
primary_ata: "95"
related_ata: ["ALL"]
---

# Body+Brain Identity Register
## Scalable model for any embedded-intelligence artifact (Body + Brain) in a fleet

---

## 0. Executive intent (what this document *is*)
This is a single **master document** for the scalable lifecycle of any **Body+Brain** artifact in a fleet:
- **Body**: the physical instantiation (hardware / structure / installation / maintainability evidence)
- **Brain**: embedded digital intelligence (software loadables and/or ML/NN models + configs + monitors)

This document is simultaneously:
1) **A conceptual circuit** (CCert/CVal) for certifiable prediction vs operational truth, and  
2) **A register** listing Body+Brain artifacts across ATA chapters, to prevent loss of scope and evidence.

---

## 1. The canonical CCert/CVal circuit (the “truth loop”)
### 1.1 Circuit (normative)
> **AM → DV → DPP → OM → OAV → DT → AM′**

- **AM** (At-Rest Model): definition and descriptive knowledge (design + maintainability truth candidates)
- **DV** (Design Validation): evidence gate proving AM is internally coherent and meets intended constraints (lab/sim/test-rig)
- **DPP** (Digital Product Passport): the authoritative, versioned identity record of the artifact (Body and/or Brain)
- **OM** (Operational Mission): the operational manifestation that the DPP predicts (an “ontological mission” of behavior)
- **OAV** (On-Asset Validation): validation under real operational context (aircraft/asset uniqueness is decisive)
- **DT** (Digital Twin): accumulated operational truth, forming evidence continuity and learnable reality
- **AM′**: updated AM after change control (CCB), derived from DT truth without violating certification immutability

### 1.2 Epistemological axiom (frozen)
**AM defines DPP. DPP predicts OM. Only operational context (OAV) can validate empirical truth. DT accumulates truth. The loop updates AM under controlled change.**

This is “predicting the future” in a certifiable way:
- **Prediction** = DPP claims about expected operational behavior (OM)
- **Truth** = OAV measurements in the unique operational context
- **Verifiability** = DT evidence continuity + traceable gates DV/OAV + immutable records

### 1.3 Validation layers (explicit, as requested)
**DV (Design Validation) — validates by design**
- Purpose: prove the predictive model is coherent *before* the aircraft context exists.
- Typical: SIL/HIL, rig tests, simulation sweeps, requirements coverage, tool qualification evidence, safety argument structure.
- Output: DV artifacts that justify publishing/issuing a DPP state.

**OAV (On-Asset Validation) — validates by reality**
- Purpose: prove that the predicted OM claims hold in the real, unique operational context.
- Typical: flight test campaigns, in-service telemetry, anomaly data, drift monitoring, operational boundary checks.
- Output: OAV events that either confirm or falsify OM predictions; DT snapshots store the resulting truth.

> Practical rule: **DV is necessary to issue a DPP; OAV is necessary to confirm OM** (especially for ML/NN and operationally sensitive behaviors).

---

## 2. Governance: sovereignty + interfacing (no “parent/child” semantics)
### 2.1 Sovereignty rule
- **Body and Brain are independent sovereign artifacts** (each can be baselined, validated, and governed).
- They are **fully interfaced** through explicit contracts (ICDs, configs, interface schemas, traceability semantics).

### 2.2 ATA rule (your coupling)
- **Functional ownership remains in the functional ATA** (e.g., Flight Controls = ATA 27).
- **DPP governance for embedded intelligence is anchored in ATA 95** (passport truth is governed there).
- The register therefore distinguishes:
  - **Body ATA (functional/physical ownership)**  
  - **Brain ATA (functional ownership of executing logic)**  
  - **DPP governance** (implicitly ATA 95 for Brain; may also host Body DPP indices if you decide so)

### 2.3 ATA placement correction (frozen)
- **Cameras / recording / video** belong under **ATA 31 (Indicating/Recording Systems)** as the functional home for recording/indicating assets.
- ATA 33 remains **Lights** (not cameras).
- **Flight control intelligence** belongs functionally under **ATA 27** (not a generic “flightcontrol” namespace).

---

## 3. Glossary & acronyms (recap, certifiable meanings)
### 3.1 Core terms
- **Body+Brain Artifact**: any system where operational value depends on both physical instantiation (Body) and embedded logic (Brain).
- **AM (At-Rest Model)**: “descriptive + maintainability” model. Baseline definition of what the artifact is, what it claims, and how it is maintained.
- **DV (Design Validation)**: pre-operational proof gate for AM; validates the design’s internal truth claims.
- **DPP (Digital Product Passport)**: the authoritative identity record for an artifact version (metadata + evidence pointers + governance state).
- **OM (Operational Mission)**: the predicted operational manifestation (“ontogenesis” of future DT); what the artifact is expected to do in the fleet.
- **OAV (On-Asset Validation)**: operational validation in the unique asset context (aircraft/vehicle/ground unit). (Generic expansion acceptable: **On Asset Validation**.)
- **DT (Digital Twin)**: accumulated operational truth: telemetry + events + validated outcomes + evidence continuity.
- **CCert (Continuous Certification)**: continuous maintenance of certification evidence continuity through controlled updates and immutable truth records.
- **CVal (Continuous Validation)**: continuous validation of operational truth through OAV and DT feedback loops.

### 3.2 Evidence artifacts (examples)
- **Body evidence**: BOM, CMM, ICD, installation drawings, wiring routes, structural substantiation, maintainability procedures.
- **Brain evidence**: IMAGE, SBOM, configuration manifests, model files, runtime monitors, deployment records, training/eval datasets (if applicable).
- **Gate evidence**:
  - DV: test reports, coverage, simulation envelopes, tool qualification
  - OAV: campaign plan, telemetry capture, anomaly reports, operational compliance results

---

## 4. Identity scheme (register-level)
### 4.1 Register ID (BB-ID)
**Format:** `ATAxx-BB-###` (unique program-wide). Example: `27-BB-008`

### 4.2 Fields (minimum required to avoid “lost crystallization”)
Each entry SHALL eventually carry pointers (even if placeholder during early drafts):
- `am_ref` (baseline definition pointer)
- `dv_ref` (design validation gate pointer)
- `dpp_id` (ATA 95 passport pointer if Brain exists; Body DPP pointer if used)
- `image_id` (software loadable package id, if applicable)
- `sbom_ref` (if software exists)
- `bom_ref` (if physical assembly exists)
- `om_class` (what operational manifestation looks like)
- `oav_ref` (campaign/validation pointer)
- `dt_ref` (where truth is accumulated)

### 4.3 Authoritative storage (scalable)
- Authoritative register (machine-usable):  
  `ASSETS/95-00-01-010-A-001_BodyBrain_Identity_Register.csv`
- This document is the normative narrative + curated views.

Recommended CSV columns:
`bb_id,artifact_name,body_summary,brain_summary,body_ata,brain_ata,dal,brain_type,dpp_id,image_id,sbom_ref,bom_ref,am_ref,dv_ref,om_class,oav_ref,dt_ref,notes`

---

## 5. Register: curated views by ATA chapter (current snapshot)

### 5.1 O-ORGANIZATION (ATA 00–05)
#### ATA 00 — General
| ID | Artifact Name | Body | Brain | Body ATA | Brain ATA | DAL | Brain Type |
|---|---|---|---|---:|---:|---:|---|
| 00-BB-001 | Document Management Terminal | Display hardware, enclosure | DMS client software | 00 | 46 | E | HMI |
| 00-BB-002 | Configuration Control Workstation | Computing hardware | CCB workflow software | 00 | 46 | D | DATA |

#### ATA 01 — Maintenance Policy (Weight & Balance)
| ID | Artifact Name | Body | Brain | Body ATA | Brain ATA | DAL | Brain Type |
|---|---|---|---|---:|---:|---:|---|
| 01-BB-001 | Weight & Balance Computer | Computing unit, sensors | W&B calculation software | 01 | 42 | B | RT-CTRL |
| 01-BB-002 | Load Sheet Generation System | Interface hardware | Load optimization algorithm | 01 | 42 | C | ML-INF |

#### ATA 02 — Operations Information
| ID | Artifact Name | Body | Brain | Body ATA | Brain ATA | DAL | Brain Type |
|---|---|---|---|---:|---:|---:|---|
| 02-BB-001 | Electronic Flight Bag (EFB) | Tablet/display hardware | EFB applications suite | 02 | 46 | C | HMI |
| 02-BB-002 | Performance Calculator | EFB hardware | Takeoff/landing performance SW | 02 | 42 | B | RT-CTRL |

#### ATA 04 — Airworthiness Limitations
| ID | Artifact Name | Body | Brain | Body ATA | Brain ATA | DAL | Brain Type |
|---|---|---|---|---:|---:|---:|---|
| 04-BB-001 | Life-Limited Parts Tracker | RFID readers, antennas | LLP tracking database/logic | 04 | 45 | C | DATA |
| 04-BB-002 | Fatigue Monitoring System | Strain gauges, accelerometers | Fatigue accumulation algorithm | 04 | 95 | B | ML-INF |

#### ATA 05 — Time Limits/Maintenance Checks
| ID | Artifact Name | Body | Brain | Body ATA | Brain ATA | DAL | Brain Type |
|---|---|---|---|---:|---:|---:|---|
| 05-BB-001 | Maintenance Interval Computer | Interface unit | Interval optimization ML | 05 | 95 | C | ML-INF |
| 05-BB-002 | Task Card Display System | Rugged display | Task sequencing software | 05 | 46 | D | HMI |

---

### 5.2 P-PROGRAM (ATA 06–12)
#### ATA 06 — Dimensions & Areas
| ID | Artifact Name | Body | Brain | Body ATA | Brain ATA | DAL | Brain Type |
|---|---|---|---|---:|---:|---:|---|
| 06-BB-001 | 3D Scanning System | LiDAR/photogrammetry HW | Point cloud processing SW | 06 | 46 | E | DATA |
| 06-BB-002 | Digital Measurement System | Laser trackers | Dimensional analysis SW | 06 | 46 | D | DATA |

#### ATA 07 — Lifting & Shoring
| ID | Artifact Name | Body | Brain | Body ATA | Brain ATA | DAL | Brain Type |
|---|---|---|---|---:|---:|---:|---|
| 07-BB-001 | Smart Jack System | Hydraulic jacks, load cells | Load distribution controller | 07 | 42 | C | RT-CTRL |
| 07-BB-002 | Shoring Load Monitor | Load sensors, wireless TX | Overload warning system | 07 | 45 | C | MON |

#### ATA 08 — Leveling & Weighing
| ID | Artifact Name | Body | Brain | Body ATA | Brain ATA | DAL | Brain Type |
|---|---|---|---|---:|---:|---:|---|
| 08-BB-001 | Aircraft Weighing System | Load cells, platforms | Weight computation & CG calc | 08 | 42 | B | RT-CTRL |
| 08-BB-002 | Fuel Densitometer | Density sensor probe | Temperature compensation SW | 08 | 28 | C | RT-CTRL |

#### ATA 09 — Towing & Taxiing
| ID | Artifact Name | Body | Brain | Body ATA | Brain ATA | DAL | Brain Type |
|---|---|---|---|---:|---:|---:|---|
| 09-BB-001 | Electric Taxi System (E-Taxi) | Wheel motors, gearboxes | E-Taxi control unit | 09 | 42 | B | RT-CTRL |
| 09-BB-002 | Autonomous Taxi Guidance | Cameras, radar, LiDAR | Path planning ML system | 09 | 95 | B | ML-INF |
| 09-BB-003 | Tow Bar Load Monitor | Strain gauges | Overload protection SW | 09 | 45 | C | MON |

#### ATA 10 — Parking, Mooring, Storage, Return to Service
| ID | Artifact Name | Body | Brain | Body ATA | Brain ATA | DAL | Brain Type |
|---|---|---|---|---:|---:|---:|---|
| 10-BB-001 | Ground Power Interface Unit | Connectors, contactors | Power quality monitor | 10 | 24 | C | MON |
| 10-BB-002 | Storage Condition Monitor | Humidity/temp sensors | Corrosion prediction ML | 10 | 95 | D | ML-INF |

#### ATA 11 — Placards & Markings
| ID | Artifact Name | Body | Brain | Body ATA | Brain ATA | DAL | Brain Type |
|---|---|---|---|---:|---:|---:|---|
| 11-BB-001 | E-Ink Placard System | E-ink displays, mounting | Dynamic placard controller | 11 | 46 | D | HMI |
| 11-BB-002 | Emergency Exit Lighting | LED strips, batteries | Adaptive brightness controller | 11 | 33 | B | RT-CTRL |

#### ATA 12 — Servicing
| ID | Artifact Name | Body | Brain | Body ATA | Brain ATA | DAL | Brain Type |
|---|---|---|---|---:|---:|---:|---|
| 12-BB-001 | Fluid Service Panel | Valves, connectors, gauges | Service sequence controller | 12 | 45 | C | RT-CTRL |
| 12-BB-002 | Potable Water Fill Monitor | Flow sensors, level gauges | Fill optimization SW | 12 | 38 | D | RT-CTRL |
| 12-BB-003 | Waste Service Controller | Valves, vacuum pumps | Service cycle controller | 12 | 38 | D | RT-CTRL |

---

### 5.3 T-TECHNOLOGY: A-AIRFRAME (ATA 20, 50–57)
#### ATA 20 — Standard Practices — Airframe
| ID | Artifact Name | Body | Brain | Body ATA | Brain ATA | DAL | Brain Type |
|---|---|---|---|---:|---:|---:|---|
| 20-BB-001 | Smart Torque Wrench | Torque tool, encoder | Torque verification SW | 20 | 45 | D | DATA |
| 20-BB-002 | NDT Inspection System | UT/ET probes, scanner | Defect detection ML | 20 | 95 | C | ML-INF |
| 20-BB-003 | Composite Repair Heater | Heat blankets, thermocouples | Cure cycle controller | 20 | 45 | C | RT-CTRL |

#### ATA 50 — Cargo & Accessory Compartments
| ID | Artifact Name | Body | Brain | Body ATA | Brain ATA | DAL | Brain Type |
|---|---|---|---|---:|---:|---:|---|
| 50-BB-001 | Cargo Loading System | Rollers, PDUs, latches | Cargo distribution optimizer | 50 | 42 | C | ML-INF |
| 50-BB-002 | Cargo Smoke Detector | Photoelectric sensors | Multi-criteria fire detection | 50 | 26 | A | RT-CTRL |
| 50-BB-003 | ULD Position Sensor | Proximity sensors | Load manifest verification | 50 | 45 | C | DATA |

#### ATA 51 — Standard Practices & Structures — General
| ID | Artifact Name | Body | Brain | Body ATA | Brain ATA | DAL | Brain Type |
|---|---|---|---|---:|---:|---:|---|
| 51-BB-001 | Structural Health Monitoring Hub | Fiber optic sensors, strain gauges | SHM analysis processor | 51 | 95 | B | ML-INF |
| 51-BB-002 | Corrosion Detection System | Eddy current sensors | Corrosion progression ML | 51 | 95 | C | ML-INF |
| 51-BB-003 | Impact Detection Network | Piezoelectric sensors | Impact localization algorithm | 51 | 95 | B | ML-INF |

#### ATA 52 — Doors
| ID | Artifact Name | Body | Brain | Body ATA | Brain ATA | DAL | Brain Type |
|---|---|---|---|---:|---:|---:|---|
| 52-BB-001 | Passenger Door Actuator | Hydraulic/electric actuator | Door sequencing controller | 52 | 42 | A | RT-CTRL |
| 52-BB-002 | Door Warning System | Proximity sensors, switches | Door status logic / annunciation | 52 | 31 | A | RT-CTRL |
| 52-BB-003 | Emergency Exit Controller | Slide pack, actuators | Emergency deploy logic | 52 | 42 | A | RT-CTRL |
| 52-BB-004 | Cargo Door System | Actuators, locks, seals | Cargo door controller | 52 | 42 | A | RT-CTRL |

#### ATA 53 — Fuselage
| ID | Artifact Name | Body | Brain | Body ATA | Brain ATA | DAL | Brain Type |
|---|---|---|---|---:|---:|---:|---|
| 53-BB-001 | Fuselage SHM Array | Distributed fiber optic network | Strain pattern analyzer | 53 | 95 | B | ML-INF |
| 53-BB-002 | Pressurization Cycle Counter | Pressure sensors | Fatigue accumulation tracker | 53 | 45 | B | DATA |
| 53-BB-003 | BWB Center Body Monitor | Multi-axis strain gauges | Load path verification ML | 53 | 95 | B | ML-INF |

#### ATA 54 — Nacelles/Pylons
| ID | Artifact Name | Body | Brain | Body ATA | Brain ATA | DAL | Brain Type |
|---|---|---|---|---:|---:|---:|---|
| 54-BB-001 | Nacelle Vibration Monitor | Accelerometers | Vibration signature ML | 54 | 95 | B | ML-INF |
| 54-BB-002 | Thrust Reverser Actuator | Hydraulic actuators, locks | Reverser sequencer | 54 | 78 | A | RT-CTRL |
| 54-BB-003 | Nacelle Anti-Ice Controller | Bleed ducts, valves | Anti-ice demand logic | 54 | 30 | B | RT-CTRL |

#### ATA 55 — Stabilizers
| ID | Artifact Name | Body | Brain | Body ATA | Brain ATA | DAL | Brain Type |
|---|---|---|---|---:|---:|---:|---|
| 55-BB-001 | Horizontal Stabilizer Actuator | Ball screw, motor | Trim control computer | 55 | 27 | A | RT-CTRL |
| 55-BB-002 | Stabilizer Load Monitor | Strain gauges | Flutter prediction ML | 55 | 95 | A | ML-INF |
| 55-BB-003 | Vertical Stabilizer SHM | Fiber optic sensors | Fatigue monitoring | 55 | 95 | B | ML-INF |

#### ATA 56 — Windows
| ID | Artifact Name | Body | Brain | Body ATA | Brain ATA | DAL | Brain Type |
|---|---|---|---|---:|---:|---:|---|
| 56-BB-001 | Cockpit Window Heating | Heating elements, sensors | Anti-ice/defogging controller | 56 | 30 | B | RT-CTRL |
| 56-BB-002 | Electrochromic Window System | EC glass panels | Tint control processor | 56 | 44 | D | RT-CTRL |
| 56-BB-003 | Window Crack Detection | Acoustic emission sensors | Crack propagation ML | 56 | 95 | B | ML-INF |

#### ATA 57 — Wings
| ID | Artifact Name | Body | Brain | Body ATA | Brain ATA | DAL | Brain Type |
|---|---|---|---|---:|---:|---:|---|
| 57-BB-001 | Wing SHM Network | Fiber optic sensor array | Wing load analyzer | 57 | 95 | A | ML-INF |
| 57-BB-002 | Winglet Load Monitor | Strain gauges | Fatigue accumulation | 57 | 95 | B | ML-INF |
| 57-BB-003 | Wing Fold Actuator (if applicable) | Hydraulic/electric actuators | Fold sequence controller | 57 | 42 | A | RT-CTRL |
| 57-BB-004 | Fuel Tank Inerting Monitor | O₂ sensors | Inerting effectiveness tracker | 57 | 47 | B | MON |

---

### 5.4 T-TECHNOLOGY: M-MECHANICS (ATA 27, 29, 32, 36, 37, 41)
#### ATA 27 — Flight Controls
| ID | Artifact Name | Body | Brain | Body ATA | Brain ATA | DAL | Brain Type |
|---|---|---|---|---:|---:|---:|---|
| 27-BB-001 | Primary Flight Control Computer (PFCC) | Computing hardware, I/O | Flight control laws | 27 | 27 | A | GUID |
| 27-BB-002 | Elevator Actuator (EHA) | Electro-hydrostatic actuator | Position control loop | 27 | 27 | A | RT-CTRL |
| 27-BB-003 | Aileron Actuator | Servo actuator | Position/rate control | 27 | 27 | A | RT-CTRL |
| 27-BB-004 | Rudder Actuator | Tandem actuator | Yaw damper/control | 27 | 27 | A | RT-CTRL |
| 27-BB-005 | Spoiler Actuator Array | Individual actuators | Spoiler mixer logic | 27 | 27 | A | RT-CTRL |
| 27-BB-006 | Flap/Slat Control Unit | Motors, gearboxes, sensors | High-lift control computer | 27 | 27 | A | RT-CTRL |
| 27-BB-007 | Fly-By-Wire Sensor Suite | LVDT, RVDT, accelerometers | Sensor fusion/voting | 27 | 27 | A | RT-CTRL |
| 27-BB-008 | Active Gust Alleviation System | Control surfaces, sensors | Gust load alleviation ML | 27 | 95 | A | ML-INF |
| 27-BB-009 | Envelope Protection Computer | Processing unit | Flight envelope limiter | 27 | 27 | A | GUID |
| 27-BB-010 | Stick/Yoke Force Feedback | Motors, force sensors | Feel simulation SW | 27 | 27 | B | RT-CTRL |

#### ATA 29 — Hydraulic Power
| ID | Artifact Name | Body | Brain | Body ATA | Brain ATA | DAL | Brain Type |
|---|---|---|---|---:|---:|---:|---|
| 29-BB-001 | Engine-Driven Pump | Variable displacement pump | Demand-based pressure control | 29 | 42 | B | RT-CTRL |
| 29-BB-002 | Electric Motor Pump (EMP) | Motor, pump, reservoir | EMP controller | 29 | 42 | B | RT-CTRL |
| 29-BB-003 | Power Transfer Unit (PTU) | Bi-directional pump | PTU engagement logic | 29 | 42 | B | RT-CTRL |
| 29-BB-004 | Hydraulic Fluid Monitor | Contamination sensor | Fluid health predictor ML | 29 | 95 | C | ML-INF |
| 29-BB-005 | Accumulator Precharge Monitor | Pressure/temp sensors | Precharge verification | 29 | 45 | C | MON |

#### ATA 32 — Landing Gear
| ID | Artifact Name | Body | Brain | Body ATA | Brain ATA | DAL | Brain Type |
|---|---|---|---|---:|---:|---:|---|
| 32-BB-001 | Brake System Control Unit (BSCU) | Brake assemblies, valves | Antiskid/autobrake SW | 32 | 32 | A | RT-CTRL |
| 32-BB-002 | Landing Gear Control Unit (LGCU) | Actuators, uplocks, doors | Extension/retraction logic | 32 | 42 | A | RT-CTRL |
| 32-BB-003 | Nose Wheel Steering | Steering actuator | NWS control computer | 32 | 32 | B | RT-CTRL |
| 32-BB-004 | Weight-on-Wheels Sensor | Proximity/oleo sensors | Air/ground logic | 32 | 42 | A | RT-CTRL |
| 32-BB-005 | Tire Pressure Monitoring System | Pressure sensors, wireless TX | TPMS controller | 32 | 45 | C | MON |
| 32-BB-006 | Brake Temperature Monitor | Thermocouples | Brake cooling predictor | 32 | 45 | C | MON |
| 32-BB-007 | Electric Brake Actuator | Electromechanical actuators | E-brake controller | 32 | 32 | A | RT-CTRL |
| 32-BB-008 | Gear Vibration Monitor | Accelerometers | Shimmy detection ML | 32 | 95 | B | ML-INF |

#### ATA 36 — Pneumatic
| ID | Artifact Name | Body | Brain | Body ATA | Brain ATA | DAL | Brain Type |
|---|---|---|---|---:|---:|---:|---|
| 36-BB-001 | Bleed Air Controller | Valves, ducts, sensors | Bleed management computer | 36 | 42 | B | RT-CTRL |
| 36-BB-002 | Precooler System | Heat exchanger, valve | Precooler control | 36 | 36 | B | RT-CTRL |
| 36-BB-003 | High Pressure Shut-Off Valve | HP valve | Overpressure protection | 36 | 36 | B | RT-CTRL |
| 36-BB-004 | Bleed Leak Detection | Thermocouples, loops | Leak detection logic | 36 | 26 | A | MON |

#### ATA 37 — Vacuum
| ID | Artifact Name | Body | Brain | Body ATA | Brain ATA | DAL | Brain Type |
|---|---|---|---|---:|---:|---:|---|
| 37-BB-001 | Vacuum Pump System | Dry vacuum pump | Pump health monitor | 37 | 45 | D | MON |
| 37-BB-002 | Vacuum Waste System | Vacuum generator, valves | Waste service controller | 37 | 38 | D | RT-CTRL |

#### ATA 41 — Water Ballast
| ID | Artifact Name | Body | Brain | Body ATA | Brain ATA | DAL | Brain Type |
|---|---|---|---|---:|---:|---:|---|
| 41-BB-001 | CG Trim Tank System | Tanks, pumps, valves | Fuel/ballast transfer controller | 41 | 28 | B | RT-CTRL |
| 41-BB-002 | CG Optimization Computer | Interface unit | CG optimization ML | 41 | 95 | B | ML-INF |

---

### 5.5 T-TECHNOLOGY: E1-ENVIRONMENT (ATA 21, 26, 30, 38)
#### ATA 21 — Air Conditioning
| ID | Artifact Name | Body | Brain | Body ATA | Brain ATA | DAL | Brain Type |
|---|---|---|---|---:|---:|---:|---|
| 21-BB-001 | Pack Controller | Air cycle machine, valves | Pack control computer | 21 | 42 | B | RT-CTRL |
| 21-BB-002 | Cabin Pressure Controller | Outflow valve, sensors | Pressurization control computer | 21 | 21 | A | RT-CTRL |
| 21-BB-003 | Zone Temperature Controller | Mix valves, sensors | Zone control logic | 21 | 44 | C | RT-CTRL |
| 21-BB-004 | Air Quality Sensor | VOC, CO₂, particulate sensors | Air quality monitor ML | 21 | 95 | C | ML-INF |
| 21-BB-005 | Recirculation Fan | Fan motor, filter | Fan speed controller | 21 | 21 | C | RT-CTRL |
| 21-BB-006 | Electric Compressor (E-ECS) | Electric compressor unit | Variable speed controller | 21 | 42 | B | RT-CTRL |
| 21-BB-007 | Humidity Controller | Humidifier, sensors | Humidity optimization | 21 | 44 | D | RT-CTRL |

#### ATA 26 — Fire Protection
| ID | Artifact Name | Body | Brain | Body ATA | Brain ATA | DAL | Brain Type |
|---|---|---|---|---:|---:|---:|---|
| 26-BB-001 | Engine Fire Detection Loop | Sensing elements | Fire detection controller | 26 | 26 | A | RT-CTRL |
| 26-BB-002 | APU Fire Detection | Sensing elements | APU fire controller | 26 | 26 | A | RT-CTRL |
| 26-BB-003 | Cargo Fire Detection | Multi-spectrum sensors | Cargo fire logic | 26 | 26 | A | RT-CTRL |
| 26-BB-004 | Fire Extinguishing System | Bottles, squibs, lines | Discharge sequencer | 26 | 26 | A | RT-CTRL |
| 26-BB-005 | Lavatory Smoke Detector | Photoelectric sensor | Smoke detection logic | 26 | 26 | B | RT-CTRL |
| 26-BB-006 | Battery Fire Suppression | Containment, suppression | Battery thermal runaway logic | 26 | 24 | A | RT-CTRL |
| 26-BB-007 | H₂ Leak Detection System | H₂ sensors array | Hydrogen leak ML | 26 | 95 | A | ML-INF |

#### ATA 30 — Ice & Rain Protection
| ID | Artifact Name | Body | Brain | Body ATA | Brain ATA | DAL | Brain Type |
|---|---|---|---|---:|---:|---:|---|
| 30-BB-001 | Wing Anti-Ice Controller | Bleed valves, ducts | Anti-ice demand logic | 30 | 42 | B | RT-CTRL |
| 30-BB-002 | Engine Inlet Anti-Ice | Bleed valves | Engine AI controller | 30 | 73 | B | RT-CTRL |
| 30-BB-003 | Windshield Wiper | Motor, blade assembly | Wiper controller | 30 | 30 | D | RT-CTRL |
| 30-BB-004 | Probe Heat Controller | Heating elements | Probe heat logic | 30 | 34 | A | RT-CTRL |
| 30-BB-005 | Ice Detection System | Magnetostrictive probe | Ice accretion estimator | 30 | 42 | B | RT-CTRL |
| 30-BB-006 | Electrothermal De-Ice | Heating mats | Cyclic heating controller | 30 | 42 | B | RT-CTRL |

#### ATA 38 — Water/Waste
| ID | Artifact Name | Body | Brain | Body ATA | Brain ATA | DAL | Brain Type |
|---|---|---|---|---:|---:|---:|---|
| 38-BB-001 | Potable Water System | Tank, pumps, heater | Water system controller | 38 | 38 | D | RT-CTRL |
| 38-BB-002 | Waste Tank System | Vacuum waste tank | Waste level monitor | 38 | 38 | D | MON |
| 38-BB-003 | Water Heater | Electric heater | Temperature controller | 38 | 38 | D | RT-CTRL |
| 38-BB-004 | Gray Water System | Collection tank, drain | Gray water controller | 38 | 38 | D | RT-CTRL |

---

### 5.6 T-TECHNOLOGY: D-DATA (ATA 31)
#### ATA 31 — Indicating/Recording Systems
| ID | Artifact Name | Body | Brain | Body ATA | Brain ATA | DAL | Brain Type |
|---|---|---|---|---:|---:|---:|---|
| 31-BB-001 | Primary Flight Display (PFD) | LCD/AMLCD display | PFD rendering SW | 31 | 42 | A | HMI |
| 31-BB-002 | Navigation Display (ND) | LCD display | ND rendering SW | 31 | 42 | A | HMI |
| 31-BB-003 | Engine Indication (EICAS/ECAM) | Display unit | Engine indication SW | 31 | 42 | A | HMI |
| 31-BB-004 | Flight Data Recorder (FDR) | Crash-protected memory | FDR acquisition SW | 31 | 31 | A | DATA |
| 31-BB-005 | Cockpit Voice Recorder (CVR) | Crash-protected memory | CVR acquisition SW | 31 | 31 | A | DATA |
| 31-BB-006 | Quick Access Recorder (QAR) | Removable memory | QAR acquisition SW | 31 | 31 | C | DATA |
| 31-BB-007 | Flight Warning Computer (FWC) | Computing unit | Alert prioritization SW | 31 | 42 | A | RT-CTRL |
| 31-BB-008 | Head-Up Display (HUD) | Combiner glass, projector | HUD symbology SW | 31 | 42 | A | HMI |
| 31-BB-009 | Enhanced Vision System (EVS) | IR camera, display | EVS processing SW | 31 | 34 | B | ML-INF |
| 31-BB-010 | Synthetic Vision System (SVS) | Display integration | Terrain database/rendering | 31 | 34 | C | HMI |
| 31-BB-011 | Standby Instruments | Independent display | Standby processing | 31 | 31 | A | HMI |
| 31-BB-012 | Video Surveillance System | Cameras, DVR | Video management SW | 31 | 46 | D | DATA |
| 31-BB-013 | Tail Camera | External camera | Video streaming SW | 31 | 46 | E | DATA |
| 31-BB-014 | Data Concentrator Unit (DCU) | Signal conditioning | Data acquisition SW | 31 | 42 | B | DATA |

---

### 5.7 T-TECHNOLOGY: E2-ENERGY (ATA 24, 47, 49, 80)
#### ATA 24 — Electrical Power
| ID | Artifact Name | Body | Brain | Body ATA | Brain ATA | DAL | Brain Type |
|---|---|---|---|---:|---:|---:|---|
| 24-BB-001 | Integrated Drive Generator (IDG) | Generator, CSD | Generator Control Unit (GCU) | 24 | 24 | B | RT-CTRL |
| 24-BB-002 | Variable Frequency Generator | Direct-drive generator | VF generator controller | 24 | 24 | B | RT-CTRL |
| 24-BB-003 | Transformer Rectifier Unit (TRU) | Transformer, rectifiers | TRU controller | 24 | 24 | B | RT-CTRL |
| 24-BB-004 | Bus Power Control Unit (BPCU) | Contactors, sensors | Power distribution logic | 24 | 24 | A | RT-CTRL |
| 24-BB-005 | Emergency Generator | Ram air turbine (RAT) | RAT deployment controller | 24 | 24 | A | RT-CTRL |
| 24-BB-006 | Battery Charger | Charging electronics | Battery management SW | 24 | 24 | B | RT-CTRL |
| 24-BB-007 | Main Battery | Li-ion/Ni-Cd cells | Battery monitoring unit (BMU) | 24 | 24 | A | MON |
| 24-BB-008 | Solid State Power Controller | SSPC modules | Load management SW | 24 | 24 | B | RT-CTRL |
| 24-BB-009 | High Voltage DC System (±270V) | HVDC buses, converters | HVDC controller | 24 | 24 | B | RT-CTRL |
| 24-BB-010 | Fuel Cell Power Unit | PEM fuel cell stack | Fuel cell controller | 24 | 80 | A | RT-CTRL |
| 24-BB-011 | Power Electronics Bay | Inverters, converters | Power conversion SW | 24 | 42 | B | RT-CTRL |
| 24-BB-012 | Electrical Load Management | Load sensing | Load shedding algorithm | 24 | 42 | B | RT-CTRL |

#### ATA 47 — Nitrogen Generation/Inerting
| ID | Artifact Name | Body | Brain | Body ATA | Brain ATA | DAL | Brain Type |
|---|---|---|---|---:|---:|---:|---|
| 47-BB-001 | OBIGGS | Air separation module | OBIGGS controller | 47 | 47 | B | RT-CTRL |
| 47-BB-002 | NEA Distribution | Valves, manifolds | Distribution controller | 47 | 47 | C | RT-CTRL |
| 47-BB-003 | Tank Ullage Monitor | O₂ sensors | Inerting effectiveness tracker | 47 | 45 | B | MON |

#### ATA 49 — Auxiliary Power Unit
| ID | Artifact Name | Body | Brain | Body ATA | Brain ATA | DAL | Brain Type |
|---|---|---|---|---:|---:|---:|---|
| 49-BB-001 | APU Engine | Gas turbine | APU Electronic Control (APUEC) | 49 | 49 | B | RT-CTRL |
| 49-BB-002 | APU Generator | AC generator | APU GCU | 49 | 24 | B | RT-CTRL |
| 49-BB-003 | APU Bleed System | Bleed valve, ducting | APU bleed controller | 49 | 36 | B | RT-CTRL |
| 49-BB-004 | APU Inlet Door | Actuator, door | Door sequencer | 49 | 49 | C | RT-CTRL |
| 49-BB-005 | APU Health Monitor | Vibration, temp sensors | APU trending ML | 49 | 95 | C | ML-INF |

#### ATA 80 — Starting / New Energy Systems
| ID | Artifact Name | Body | Brain | Body ATA | Brain ATA | DAL | Brain Type |
|---|---|---|---|---:|---:|---:|---|
| 80-BB-001 | Air Turbine Starter | Pneumatic starter | Start sequencer | 80 | 73 | B | RT-CTRL |
| 80-BB-002 | Electric Starter Generator | Motor/generator | Start/generate controller | 80 | 73 | B | RT-CTRL |
| 80-BB-003 | Ground Power Starter | Electrical interface | Ground start logic | 80 | 24 | C | RT-CTRL |
| 80-BB-004 | H₂ Fuel Cell System (Main) | High-power PEM stack | Fuel cell management system | 80 | 95 | A | RT-CTRL |
| 80-BB-005 | Battery Energy Storage System | High-voltage battery pack | BESS management controller | 80 | 24 | A | RT-CTRL |
| 80-BB-006 | Supercapacitor Array | Ultracapacitor modules | Energy buffer controller | 80 | 24 | B | RT-CTRL |
| 80-BB-007 | DC-DC Converter (High Power) | Power electronics | Voltage regulation SW | 80 | 24 | B | RT-CTRL |
| 80-BB-008 | Thermal Management (Energy) | Cooling loops, pumps | Thermal control algorithm | 80 | 95 | B | ML-INF |

---

### 5.8 T-TECHNOLOGY: O-OPERATING SYSTEMS (ATA 42)
#### ATA 42 — Integrated Modular Avionics
| ID | Artifact Name | Body | Brain | Body ATA | Brain ATA | DAL | Brain Type |
|---|---|---|---|---:|---:|---:|---|
| 42-BB-001 | Common Computing Resource (CCR) | IMA cabinet, modules | ARINC 653 RTOS/platform | 42 | 42 | A | RT-CTRL |
| 42-BB-002 | Core Processing Module (CPM) | Processing blade | Partition management SW | 42 | 42 | A | RT-CTRL |
| 42-BB-003 | Input/Output Module (IOM) | I/O blade, interfaces | I/O driver stack | 42 | 42 | B | RT-CTRL |
| 42-BB-004 | Network Switch Module | AFDX switch | Network management SW | 42 | 42 | A | COMM |
| 42-BB-005 | Graphics Processing Module | GPU blade | Display rendering engine | 42 | 42 | B | HMI |
| 42-BB-006 | Remote Data Concentrator | Signal conditioning | RDC acquisition SW | 42 | 42 | B | DATA |
| 42-BB-007 | Cabinet Cooling System | Fans, cold plates | Thermal management | 42 | 21 | C | MON |
| 42-BB-008 | Power Supply Module | DC-DC converters | Power sequencing SW | 42 | 24 | B | RT-CTRL |
| 42-BB-009 | Health Monitoring Function | Built-in test circuits | BITE/diagnostic SW | 42 | 45 | B | DIAG |
| 42-BB-010 | Application Hosting Platform | Virtualization layer | Application container runtime | 42 | 42 | var | RT-CTRL |

---

### 5.9 T-TECHNOLOGY: P-PROPULSION (ATA 60–61, 70–79)
#### ATA 60–61 — Standard Practices — Propulsion
| ID | Artifact Name | Body | Brain | Body ATA | Brain ATA | DAL | Brain Type |
|---|---|---|---|---:|---:|---:|---|
| 60-BB-001 | Borescope Inspection System | Fiber optic probe | Image analysis ML | 60 | 95 | C | ML-INF |
| 60-BB-002 | Propulsion Test Stand | Load cells, sensors | Test automation SW | 60 | 45 | C | DATA |

#### ATA 70 — Standard Practices — Engine
| ID | Artifact Name | Body | Brain | Body ATA | Brain ATA | DAL | Brain Type |
|---|---|---|---|---:|---:|---:|---|
| 70-BB-001 | Engine Trend Monitor | Interface unit | Engine trending ML | 70 | 95 | B | ML-INF |
| 70-BB-002 | Maintenance Predictor | Edge computing | Predictive maintenance ML | 70 | 95 | C | ML-INF |

#### ATA 71 — Power Plant — General
| ID | Artifact Name | Body | Brain | Body ATA | Brain ATA | DAL | Brain Type |
|---|---|---|---|---:|---:|---:|---|
| 71-BB-001 | Electric Propulsion Motor | High-power electric motor | Motor controller (inverter) | 71 | 42 | A | RT-CTRL |
| 71-BB-002 | Hydrogen Turbine Engine | Modified gas turbine | FADEC (H₂ variant) | 71 | 73 | A | RT-CTRL |
| 71-BB-003 | Hybrid Propulsion Manager | Interface unit | Hybrid power optimizer | 71 | 95 | A | ML-INF |

#### ATA 72 — Engine — Turbine/Turboprop
| ID | Artifact Name | Body | Brain | Body ATA | Brain ATA | DAL | Brain Type |
|---|---|---|---|---:|---:|---:|---|
| 72-BB-001 | High Pressure Compressor | Blades, disks, case | Performance monitor | 72 | 95 | B | MON |
| 72-BB-002 | Combustion Chamber | Liner, fuel nozzles | Combustion dynamics ML | 72 | 95 | B | ML-INF |
| 72-BB-003 | High Pressure Turbine | Blades, nozzles | Thermal model predictor | 72 | 95 | B | ML-INF |
| 72-BB-004 | Low Pressure Turbine | Blades, disks | LPT health monitor | 72 | 95 | C | MON |

#### ATA 73 — Engine Fuel & Control
| ID | Artifact Name | Body | Brain | Body ATA | Brain ATA | DAL | Brain Type |
|---|---|---|---|---:|---:|---:|---|
| 73-BB-001 | FADEC | Hydromechanical unit, EEC | FADEC software | 73 | 73 | A | RT-CTRL |
| 73-BB-002 | Fuel Metering Unit | Metering valve, actuator | Fuel flow control | 73 | 73 | A | RT-CTRL |
| 73-BB-003 | Engine Fuel Pump | HP/LP pumps | Pump controller | 73 | 73 | B | RT-CTRL |
| 73-BB-004 | Variable Stator Vane Actuator | Actuator ring | VSV position control | 73 | 73 | B | RT-CTRL |
| 73-BB-005 | Variable Bleed Valve | Bleed valve | VBV controller | 73 | 73 | B | RT-CTRL |
| 73-BB-006 | H₂ Fuel Metering System | Cryogenic metering valve | H₂ flow controller | 73 | 95 | A | RT-CTRL |
| 73-BB-007 | Active Clearance Control | Thermal system | ACC controller | 73 | 73 | B | RT-CTRL |

#### ATA 74 — Engine Ignition
| ID | Artifact Name | Body | Brain | Body ATA | Brain ATA | DAL | Brain Type |
|---|---|---|---|---:|---:|---:|---|
| 74-BB-001 | Ignition Exciter | High-energy ignition unit | Ignition sequencer | 74 | 73 | B | RT-CTRL |
| 74-BB-002 | Spark Plug/Igniter | Igniter plug | Ignition health monitor | 74 | 45 | C | MON |

#### ATA 75 — Engine Air
| ID | Artifact Name | Body | Brain | Body ATA | Brain ATA | DAL | Brain Type |
|---|---|---|---|---:|---:|---:|---|
| 75-BB-001 | Engine Bleed System | Bleed valves, ducts | Bleed controller | 75 | 36 | B | RT-CTRL |
| 75-BB-002 | Anti-Ice Valve | Butterfly valve | Anti-ice demand logic | 75 | 30 | B | RT-CTRL |

#### ATA 76 — Engine Controls
| ID | Artifact Name | Body | Brain | Body ATA | Brain ATA | DAL | Brain Type |
|---|---|---|---|---:|---:|---:|---|
| 76-BB-001 | Thrust Management Computer | Computing unit | Autothrottle/TOGA logic | 76 | 22 | A | RT-CTRL |
| 76-BB-002 | Thrust Lever Assembly | FADEC interface, resolvers | Thrust lever position sensing | 76 | 73 | A | RT-CTRL |
| 76-BB-003 | Engine Vibration Monitor | Accelerometers | Vibration signature ML | 76 | 95 | B | ML-INF |

#### ATA 77 — Engine Indicating
| ID | Artifact Name | Body | Brain | Body ATA | Brain ATA | DAL | Brain Type |
|---|---|---|---|---:|---:|---:|---|
| 77-BB-001 | N1/N2 Speed Sensor | Magnetic pickup | Speed processing | 77 | 31 | A | DATA |
| 77-BB-002 | EGT/ITT Probe | Thermocouple harness | Temperature averaging | 77 | 31 | A | DATA |
| 77-BB-003 | Engine Pressure Sensor | Pressure transducers | Pressure processing | 77 | 31 | B | DATA |
| 77-BB-004 | Fuel Flow Transmitter | Turbine flowmeter | Flow computation | 77 | 31 | B | DATA |
| 77-BB-005 | Oil Pressure/Temp Sensor | Pressure/temp transducers | Oil system indicating | 77 | 79 | B | DATA |

#### ATA 78 — Engine Exhaust
| ID | Artifact Name | Body | Brain | Body ATA | Brain ATA | DAL | Brain Type |
|---|---|---|---|---:|---:|---:|---|
| 78-BB-001 | Thrust Reverser Actuation | Hydraulic/electric actuators | Reverser controller | 78 | 54 | A | RT-CTRL |
| 78-BB-002 | Variable Area Nozzle | Actuated nozzle flaps | Nozzle position controller | 78 | 73 | B | RT-CTRL |
| 78-BB-003 | Exhaust Gas Temperature Array | Thermocouple ring | EGT spread analyzer | 78 | 77 | B | DATA |

#### ATA 79 — Engine Oil
| ID | Artifact Name | Body | Brain | Body ATA | Brain ATA | DAL | Brain Type |
|---|---|---|---|---:|---:|---:|---|
| 79-BB-001 | Oil Pump | Gerotor/gear pump | Oil system controller | 79 | 73 | B | RT-CTRL |
| 79-BB-002 | Oil Cooler | Air/fuel oil cooler | Cooling flow controller | 79 | 79 | C | RT-CTRL |
| 79-BB-003 | Oil Filter (Main) | Filter element, bypass | Filter delta-P monitor | 79 | 45 | C | MON |
| 79-BB-004 | Chip Detector | Magnetic plug | Debris analysis ML | 79 | 95 | B | ML-INF |
| 79-BB-005 | Oil Quantity Indicator | Level sensor | Oil consumption tracker | 79 | 45 | C | MON |

---

### 5.10 T-TECHNOLOGY: E3-ELECTRONICS (ATA 34, 39)
#### ATA 34 — Navigation
| ID | Artifact Name | Body | Brain | Body ATA | Brain ATA | DAL | Brain Type |
|---|---|---|---|---:|---:|---:|---|
| 34-BB-001 | Inertial Reference System (IRS) | RLGs, accelerometers | IRS navigation SW | 34 | 34 | A | NAV |
| 34-BB-002 | Air Data Computer (ADC) | Pitot/static probes | Air data algorithm | 34 | 34 | A | NAV |
| 34-BB-003 | GPS Receiver | Antenna, receiver | GPS processing | 34 | 34 | B | NAV |
| 34-BB-004 | Radio Altimeter | Antenna, transceiver | RA processing SW | 34 | 34 | A | NAV |
| 34-BB-005 | Weather Radar | Flat panel antenna | WXR processing/display | 34 | 34 | B | NAV |
| 34-BB-006 | TCAS/ACAS | Directional antennas | Collision avoidance SW | 34 | 34 | A | NAV |
| 34-BB-007 | TAWS/EGPWS | Terrain database | Terrain avoidance SW | 34 | 34 | A | NAV |
| 34-BB-008 | ADS-B Transponder | Mode-S transponder | ADS-B processing | 34 | 23 | B | COMM |
| 34-BB-009 | DME | DME transceiver | Distance processing | 34 | 34 | C | NAV |
| 34-BB-010 | VOR Receiver | VOR antenna, receiver | VOR processing | 34 | 34 | C | NAV |
| 34-BB-011 | ILS Receiver | LOC/GS | ILS processing | 34 | 34 | A | NAV |
| 34-BB-012 | MLS/GLS Receiver | MLS/GLS receiver | Precision approach SW | 34 | 34 | A | NAV |
| 34-BB-013 | AHRS | MEMS sensors | Attitude computation | 34 | 34 | B | NAV |
| 34-BB-014 | Terrain Database | Storage media | Database management | 34 | 46 | C | DATA |

#### ATA 39 — Electrical Wiring/Panels
| ID | Artifact Name | Body | Brain | Body ATA | Brain ATA | DAL | Brain Type |
|---|---|---|---|---:|---:|---:|---|
| 39-BB-001 | Smart Wire System | Sensing wires | Arc fault detection | 39 | 24 | B | MON |
| 39-BB-002 | Electronic Circuit Breaker Panel | SSPC array | Load management SW | 39 | 24 | B | RT-CTRL |
| 39-BB-003 | Wiring Health Monitor | TDR system | Wiring degradation ML | 39 | 95 | C | ML-INF |

---

### 5.11 T-TECHNOLOGY: L1-LOGICS (ATA 22)
#### ATA 22 — Auto Flight
| ID | Artifact Name | Body | Brain | Body ATA | Brain ATA | DAL | Brain Type |
|---|---|---|---|---:|---:|---:|---|
| 22-BB-001 | Flight Management Computer (FMC) | Computing unit | FMS application SW | 22 | 22 | B | NAV |
| 22-BB-002 | Autopilot Computer | Computing unit | AP control laws | 22 | 22 | A | GUID |
| 22-BB-003 | Flight Director | Display integration | FD guidance logic | 22 | 31 | B | GUID |
| 22-BB-004 | Autothrottle Computer | Thrust computation | A/T control laws | 22 | 76 | A | GUID |
| 22-BB-005 | Autoland System | Multi-sensor fusion | CAT III autoland SW | 22 | 22 | A | GUID |
| 22-BB-006 | Performance Database | Storage | Navigation database | 22 | 46 | C | DATA |
| 22-BB-007 | Trajectory Optimization | Computing function | 4D trajectory optimizer | 22 | 95 | B | ML-INF |

---

### 5.12 T-TECHNOLOGY: L2-LINKS (ATA 23, 91)
#### ATA 23 — Communications
| ID | Artifact Name | Body | Brain | Body ATA | Brain ATA | DAL | Brain Type |
|---|---|---|---|---:|---:|---:|---|
| 23-BB-001 | VHF Radio | Transceiver, antenna | VHF controller | 23 | 23 | B | COMM |
| 23-BB-002 | HF Radio | Transceiver, coupler | HF controller | 23 | 23 | C | COMM |
| 23-BB-003 | SATCOM System | Antenna, SDU | SATCOM controller | 23 | 23 | C | COMM |
| 23-BB-004 | ACARS/CMU | Data link unit | ACARS handler | 23 | 23 | C | COMM |
| 23-BB-005 | Audio Management Unit | Audio switching | Intercom/PA SW | 23 | 44 | C | COMM |
| 23-BB-006 | Emergency Locator Transmitter | ELT beacon | ELT controller | 23 | 23 | A | COMM |
| 23-BB-007 | Cabin Wireless Access Point | WiFi AP | WiFi/IFE gateway | 23 | 44 | E | COMM |
| 23-BB-008 | Cockpit Printer | Thermal printer | Print controller | 23 | 46 | D | HMI |
| 23-BB-009 | AeroMACS/4G-5G Link | Cellular modem | Broadband datalink SW | 23 | 46 | C | COMM |

#### ATA 91 — Charts
| ID | Artifact Name | Body | Brain | Body ATA | Brain ATA | DAL | Brain Type |
|---|---|---|---|---:|---:|---:|---|
| 91-BB-001 | Electronic Charts System | Display integration | Chart rendering SW | 91 | 46 | C | HMI |
| 91-BB-002 | Chart Update System | Data loader | Chart DB mgmt | 91 | 46 | C | DATA |

---

### 5.13 T-TECHNOLOGY: I-INFORMATION/INTERFACES (ATA 45, 46, 93)
#### ATA 45 — Central Maintenance System
| ID | Artifact Name | Body | Brain | Body ATA | Brain ATA | DAL | Brain Type |
|---|---|---|---|---:|---:|---:|---|
| 45-BB-001 | Central Maintenance Computer (CMC) | Computing unit | CMCS application | 45 | 45 | C | DIAG |
| 45-BB-002 | On-Board Data Loader | Data interface | Software loading SW | 45 | 45 | C | DATA |
| 45-BB-003 | Maintenance Access Terminal | Rugged laptop | MAT application | 45 | 45 | D | HMI |
| 45-BB-004 | Fleet Data Gateway | Cellular/satcom modem | Fleet comm SW | 45 | 23 | C | COMM |
| 45-BB-005 | Predictive Maintenance Engine | Edge computing | Predictive ML models | 45 | 95 | C | ML-INF |
| 45-BB-006 | Fault Correlation Engine | Computing function | Fault tree logic | 45 | 95 | C | ML-INF |

#### ATA 46 — Information Systems
| ID | Artifact Name | Body | Brain | Body ATA | Brain ATA | DAL | Brain Type |
|---|---|---|---|---:|---:|---:|---|
| 46-BB-001 | Onboard Information System | Server hardware | OIS platform SW | 46 | 46 | C | DATA |
| 46-BB-002 | Electronic Flight Bag Server | Server/storage | EFB hosting platform | 46 | 46 | C | DATA |
| 46-BB-003 | Aircraft Interface Device | Gateway hardware | AID protocol SW | 46 | 46 | C | COMM |
| 46-BB-004 | Crew Information System | Display/server | CIS application | 46 | 46 | D | HMI |
| 46-BB-005 | Operations Data Store | Storage unit | Data management SW | 46 | 46 | D | DATA |
| 46-BB-006 | Cybersecurity Gateway | Firewall hardware | Security monitoring SW | 46 | 46 | B | MON |

#### ATA 93 — Cabin Systems Network (Reserved)
| ID | Artifact Name | Body | Brain | Body ATA | Brain ATA | DAL | Brain Type |
|---|---|---|---|---:|---:|---:|---|
| 93-BB-001 | Cabin Network Server | Server hardware | Cabin network OS | 93 | 44 | D | COMM |
| 93-BB-002 | Passenger Service Unit (PSU) | PSU module | PSU controller | 93 | 44 | D | RT-CTRL |

---

### 5.14 T-TECHNOLOGY: C-CABIN/COCKPIT/CARGO (ATA 15, 16, 25, 33, 35, 44)
#### ATA 15 — External Training Aids (Reserved)
| ID | Artifact Name | Body | Brain | Body ATA | Brain ATA | DAL | Brain Type |
|---|---|---|---|---:|---:|---:|---|
| 15-BB-001 | Full Flight Simulator Interface | FFS HW integration | Simulator I/O controller | 15 | 46 | E | DATA |

#### ATA 16 — Ground Support Equipment
| ID | Artifact Name | Body | Brain | Body ATA | Brain ATA | DAL | Brain Type |
|---|---|---|---|---:|---:|---:|---|
| 16-BB-001 | Tow Tractor (Smart) | Electric/diesel tractor | Autonomous towing SW | 16 | 09 | D | ML-INF |
| 16-BB-002 | Ground Power Unit | GPU hardware | Power quality controller | 16 | 24 | D | RT-CTRL |
| 16-BB-003 | Air Start Unit | Pneumatic cart | ASU controller | 16 | 80 | D | RT-CTRL |
| 16-BB-004 | H₂ Refueling Vehicle | Cryogenic tanker | H₂ transfer controller | 16 | 28 | B | RT-CTRL |

#### ATA 25 — Equipment/Furnishings
| ID | Artifact Name | Body | Brain | Body ATA | Brain ATA | DAL | Brain Type |
|---|---|---|---|---:|---:|---:|---|
| 25-BB-001 | Galley System | Ovens, chillers | Galley management SW | 25 | 44 | D | RT-CTRL |
| 25-BB-002 | Lavatory System | Fixtures, vacuum system | Lavatory controller | 25 | 38 | D | RT-CTRL |
| 25-BB-003 | Passenger Seat (Premium) | Seat structure, actuators | Seat control unit | 25 | 44 | D | RT-CTRL |
| 25-BB-004 | Crew Rest Compartment | Bunk, environment | CRCC environment controller | 25 | 21 | D | RT-CTRL |
| 25-BB-005 | Stowage Bin (Motorized) | Bin mechanism | Bin controller | 25 | 44 | D | RT-CTRL |

#### ATA 33 — Lights
| ID | Artifact Name | Body | Brain | Body ATA | Brain ATA | DAL | Brain Type |
|---|---|---|---|---:|---:|---:|---|
| 33-BB-001 | Landing Light | LED assembly | Light controller | 33 | 33 | C | RT-CTRL |
| 33-BB-002 | Taxi Light | LED assembly | Light controller | 33 | 33 | D | RT-CTRL |
| 33-BB-003 | Navigation Lights | LED assembly | Position light controller | 33 | 33 | B | RT-CTRL |
| 33-BB-004 | Anti-Collision Beacon | Strobe assembly | Beacon controller | 33 | 33 | B | RT-CTRL |
| 33-BB-005 | Wing Inspection Light | LED assembly | Light controller | 33 | 33 | D | RT-CTRL |
| 33-BB-006 | Logo Light | LED assembly | Light controller | 33 | 33 | E | RT-CTRL |
| 33-BB-007 | Cabin Lighting System | LED strips, zones | Cabin lighting controller | 33 | 44 | D | RT-CTRL |
| 33-BB-008 | Emergency Lighting | LED strips, batteries | Emergency light controller | 33 | 33 | A | RT-CTRL |
| 33-BB-009 | Cockpit Lighting | Panel backlighting | Cockpit light controller | 33 | 33 | D | RT-CTRL |

#### ATA 35 — Oxygen
| ID | Artifact Name | Body | Brain | Body ATA | Brain ATA | DAL | Brain Type |
|---|---|---|---|---:|---:|---:|---|
| 35-BB-001 | Crew Oxygen System | Cylinders, masks, regulators | Oxygen system controller | 35 | 35 | A | RT-CTRL |
| 35-BB-002 | Passenger Oxygen (Chemical) | Chem generators, masks | PAX O₂ deploy controller | 35 | 35 | A | RT-CTRL |
| 35-BB-003 | Passenger Oxygen (Gaseous) | Cylinders, masks | Gaseous O₂ controller | 35 | 35 | A | RT-CTRL |
| 35-BB-004 | Therapeutic Oxygen | Portable outlets | Therapeutic O₂ controller | 35 | 35 | C | RT-CTRL |
| 35-BB-005 | Oxygen Concentration Monitor | O₂ sensors | Cabin O₂ monitor | 35 | 21 | B | MON |

#### ATA 44 — Cabin Systems
| ID | Artifact Name | Body | Brain | Body ATA | Brain ATA | DAL | Brain Type |
|---|---|---|---|---:|---:|---:|---|
| 44-BB-001 | Cabin Management System (CMS) | Computing hardware | CMS application | 44 | 44 | D | RT-CTRL |
| 44-BB-002 | In-Flight Entertainment (IFE) | Seat screens, servers | IFE platform SW | 44 | 44 | E | HMI |
| 44-BB-003 | Cabin Interphone | Handsets, speakers | Interphone controller | 44 | 23 | C | COMM |
| 44-BB-004 | Passenger Address System | Speakers, amplifiers | PA controller | 44 | 23 | B | COMM |
| 44-BB-005 | Flight Attendant Panel (FAP) | Touch panel | FAP application | 44 | 44 | D | HMI |
| 44-BB-006 | Call System | Buttons, lights | Call controller | 44 | 44 | D | HMI |
| 44-BB-007 | Mood Lighting Controller | RGB LEDs | Ambient light SW | 44 | 33 | E | RT-CTRL |
| 44-BB-008 | Cabin Pressure Display | PAX display | Altitude/info display SW | 44 | 31 | D | HMI |

---

### 5.15 T-TECHNOLOGY: C2-CIRCULAR/CRYOGENICS (ATA 28, 99, 100)
#### ATA 28 — Fuel (Including H₂ & SAF)
| ID | Artifact Name | Body | Brain | Body ATA | Brain ATA | DAL | Brain Type |
|---|---|---|---|---:|---:|---:|---|
| 28-BB-001 | Fuel Quantity Computer | Capacitance probes | Fuel quantity SW | 28 | 28 | B | RT-CTRL |
| 28-BB-002 | Fuel Control/Management | Pumps, valves, manifolds | Fuel management computer | 28 | 28 | A | RT-CTRL |
| 28-BB-003 | Refuel/Defuel Panel | Valves, gauges | Refuel controller | 28 | 28 | C | RT-CTRL |
| 28-BB-004 | Fuel Transfer System | Pumps, valves | CG optimization controller | 28 | 41 | B | RT-CTRL |
| 28-BB-005 | Fuel Temperature Monitor | Temp sensors | Low temp warning | 28 | 28 | B | MON |
| 28-BB-006 | Water Contamination Sensor | Water-in-fuel sensor | Contamination alert | 28 | 45 | C | MON |
| 28-BB-007 | LH₂ Tank System | Cryogenic tank, insulation | LH₂ tank management | 28 | 95 | A | RT-CTRL |
| 28-BB-008 | LH₂ Feed System | Cryogenic pumps, valves | LH₂ feed controller | 28 | 95 | A | RT-CTRL |
| 28-BB-009 | LH₂ Boil-Off Management | Vent valves, heaters | Boil-off controller | 28 | 95 | B | RT-CTRL |
| 28-BB-010 | H₂ Gasification System | Heat exchangers | Vaporization controller | 28 | 95 | A | RT-CTRL |
| 28-BB-011 | SAF Blend Monitor | Composition sensor | Blend verification SW | 28 | 95 | C | MON |

#### ATA 99 — Carbon/Emissions Accounting (Reserved)
| ID | Artifact Name | Body | Brain | Body ATA | Brain ATA | DAL | Brain Type |
|---|---|---|---|---:|---:|---:|---|
| 99-BB-001 | Emissions Monitoring Unit | Flow sensors, interface | Emissions calculation SW | 99 | 95 | D | DATA |
| 99-BB-002 | Carbon Accounting System | Computing function | Carbon credit tracker | 99 | 95 | E | DATA |
| 99-BB-003 | Flight Efficiency Optimizer | Interface unit | Fuel burn optimization ML | 99 | 95 | C | ML-INF |

#### ATA 100 — Circular Economy Metrics (Reserved)
| ID | Artifact Name | Body | Brain | Body ATA | Brain ATA | DAL | Brain Type |
|---|---|---|---|---:|---:|---:|---|
| 100-BB-001 | Part Lifecycle Tracker | RFID infrastructure | Lifecycle tracking SW | 100 | 95 | D | DATA |
| 100-BB-002 | Recyclability Assessor | Material database | End-of-life optimizer | 100 | 95 | E | ML-INF |
| 100-BB-003 | DPP Generator | Computing function | Digital passport creator | 100 | 95 | D | DATA |

---

### 5.16 T-TECHNOLOGY: I2-R&D / AI INTEGRATION (ATA 40, 48, 92)
#### ATA 40 — Multisystem
| ID | Artifact Name | Body | Brain | Body ATA | Brain ATA | DAL | Brain Type |
|---|---|---|---|---:|---:|---:|---|
| 40-BB-001 | Integrated Vehicle Health Mgmt | Distributed sensors | IVHM central processor | 40 | 95 | B | ML-INF |
| 40-BB-002 | Prognostics Engine | Computing function | Remaining life predictor ML | 40 | 95 | B | ML-INF |
| 40-BB-003 | System Integration Test Rig | HIL hardware | Test automation SW | 40 | 45 | D | DATA |
| 40-BB-004 | Cross-System Optimizer | Computing function | Multi-system efficiency ML | 40 | 95 | B | ML-INF |

#### ATA 48 — Future Systems (Reserved)
| ID | Artifact Name | Body | Brain | Body ATA | Brain ATA | DAL | Brain Type |
|---|---|---|---|---:|---:|---:|---|
| 48-BB-001 | Urban Air Mobility Interface | eVTOL integration HW | UAM coordination SW | 48 | 95 | B | COMM |
| 48-BB-002 | Autonomous Operation Module | Sensor fusion HW | Autonomous flight SW | 48 | 95 | A | ML-INF |

#### ATA 92 — Electrical Installation (Reserved)
| ID | Artifact Name | Body | Brain | Body ATA | Brain ATA | DAL | Brain Type |
|---|---|---|---|---:|---:|---:|---|
| 92-BB-001 | Electrical Load Analyzer | Current sensors | Load analysis SW | 92 | 24 | C | MON |
| 92-BB-002 | Power Quality Monitor | Voltage/freq sensors | Power quality ML | 92 | 95 | C | ML-INF |

---

### 5.17 T-TECHNOLOGY: A2-AERODYNAMICS (within ATA 27 devices)
#### ATA 27 — Aerodynamic Devices (advanced)
| ID | Artifact Name | Body | Brain | Body ATA | Brain ATA | DAL | Brain Type |
|---|---|---|---|---:|---:|---:|---|
| 27-BB-011 | Active Flow Control | Synthetic jet actuators | AFC controller | 27 | 95 | B | ML-INF |
| 27-BB-012 | Morphing Wing Element | Shape-memory actuators | Morphing controller | 27 | 95 | B | ML-INF |
| 27-BB-013 | Drag Reduction System | Riblet actuators | Drag optimization ML | 27 | 95 | C | ML-INF |

---

### 5.18 I-INFRASTRUCTURES (ATA 03, 13, 85–90, 115–116)
#### ATA 03 — Minimum Equipment (MMEL/MEL)
| ID | Artifact Name | Body | Brain | Body ATA | Brain ATA | DAL | Brain Type |
|---|---|---|---|---:|---:|---:|---|
| 03-BB-001 | MEL Compliance Checker | EFB integration | MEL logic engine | 03 | 02 | C | DIAG |
| 03-BB-002 | Dispatch Deviation Guide | Computing function | DDG application | 03 | 45 | C | DIAG |

#### ATA 13 — Extended Range Operations (ETOPS/EDTO)
| ID | Artifact Name | Body | Brain | Body ATA | Brain ATA | DAL | Brain Type |
|---|---|---|---|---:|---:|---:|---|
| 13-BB-001 | ETOPS Monitor | Status interface | ETOPS compliance tracker | 13 | 45 | B | MON |
| 13-BB-002 | Diversion Airport Calculator | Navigation interface | Equal-time point optimizer | 13 | 22 | B | NAV |

#### ATA 85–90 — Infrastructure Systems (Reserved)
| ID | Artifact Name | Body | Brain | Body ATA | Brain ATA | DAL | Brain Type |
|---|---|---|---|---:|---:|---:|---|
| 85-BB-001 | Airport Interface System | Ground comm hardware | Airport datalink SW | 85 | 23 | D | COMM |
| 86-BB-001 | H₂ Supply Chain Tracker | Interface unit | H₂ provenance blockchain | 86 | 95 | D | DATA |
| 87-BB-001 | MRO Facility Interface | Workshop equipment | MRO workflow SW | 87 | 45 | D | DATA |
| 88-BB-001 | Flight Operations Center Link | Satcom/cellular | FOC comm SW | 88 | 23 | C | COMM |

#### ATA 115–116 — Ground Infrastructure (Reserved)
| ID | Artifact Name | Body | Brain | Body ATA | Brain ATA | DAL | Brain Type |
|---|---|---|---|---:|---:|---:|---|
| 115-BB-001 | H₂ Refueling Station | Cryogenic infrastructure | Refueling automation SW | 115 | 28 | B | RT-CTRL |
| 116-BB-001 | Battery Swap Station | HV equipment | Battery swap controller | 116 | 24 | B | RT-CTRL |

---

### 5.19 N-NEURAL NETWORKS / DPP / TRACEABILITY (ATA 95–98)
#### ATA 95 — Neural Networks & AI Governance
| ID | Artifact Name | Body | Brain | Body ATA | Brain ATA | DAL | Brain Type |
|---|---|---|---|---:|---:|---:|---|
| 95-BB-001 | AI Inference Engine | Edge computing module | Inference runtime | 95 | 95 | var | ML-INF |
| 95-BB-002 | ML Model Repository | Storage hardware | Model version control SW | 95 | 95 | C | DATA |
| 95-BB-003 | Training Data Pipeline | Data infrastructure | Data curation SW | 95 | 95 | D | DATA |
| 95-BB-004 | Model Validation Rig | Test hardware | V&V automation SW | 95 | 95 | B | ML-INF |
| 95-BB-005 | Explainability Engine | Computing function | XAI algorithms | 95 | 95 | B | ML-INF |
| 95-BB-006 | Drift Detection Monitor | Runtime monitoring | Drift detection ML | 95 | 95 | B | MON |
| 95-BB-007 | Federated Learning Hub | Distributed computing | FL orchestrator | 95 | 95 | C | ML-TRAIN |
| 95-BB-008 | Reinforcement Learning Module | Simulation interface | RL training SW | 95 | 95 | B | ML-TRAIN |

#### ATA 96 — Digital Product Passport (reserved chapter)
| ID | Artifact Name | Body | Brain | Body ATA | Brain ATA | DAL | Brain Type |
|---|---|---|---|---:|---:|---:|---|
| 96-BB-001 | DPP Generation Engine | Computing function | DPP creation SW | 96 | 95 | C | DATA |
| 96-BB-002 | DPP Validation Service | Interface unit | DPP verification SW | 96 | 95 | B | DATA |
| 96-BB-003 | Provenance Ledger | Distributed storage | Blockchain/DLT SW | 96 | 95 | C | DATA |
| 96-BB-004 | Component Identity Manager | RFID/NFC readers | Identity tracking SW | 96 | 95 | C | DATA |

#### ATA 97 — Telemetry & Time-Series (reserved chapter)
| ID | Artifact Name | Body | Brain | Body ATA | Brain ATA | DAL | Brain Type |
|---|---|---|---|---:|---:|---:|---|
| 97-BB-001 | Telemetry Acquisition Unit | Data concentrators | Telemetry acquisition SW | 97 | 31 | B | DATA |
| 97-BB-002 | Time-Series Database | Storage infrastructure | TSDB management SW | 97 | 46 | C | DATA |
| 97-BB-003 | Anomaly Detection Service | Computing function | Anomaly detection ML | 97 | 95 | B | ML-INF |
| 97-BB-004 | Data Quality Monitor | Interface function | DQ validation SW | 97 | 95 | C | MON |

#### ATA 98 — CCert/CVal Operations (reserved chapter)
| ID | Artifact Name | Body | Brain | Body ATA | Brain ATA | DAL | Brain Type |
|---|---|---|---|---:|---:|---:|---|
| 98-BB-001 | Continuous Certification Engine | Computing function | CCert workflow SW | 98 | 95 | B | DATA |
| 98-BB-002 | Validation Campaign Manager | Interface unit | CVal automation SW | 98 | 95 | B | DATA |
| 98-BB-003 | Evidence Package Generator | Computing function | Evidence compilation SW | 98 | 95 | C | DATA |
| 98-BB-004 | Regulatory Interface | Communication gateway | Authority submission SW | 98 | 95 | C | COMM |

---

## 6. Summary statistics (AUTO-DERIVED; do not hand-edit)
These figures SHALL be derived from `95-00-01-010-A-001_BodyBrain_Identity_Register.csv` by CI.

**Recommended generated views:**
- Count by ATA chapter
- Count by Brain Type
- Count by DAL
- Coverage by “pointer set completeness” (AM/DV/DPP/OM/OAV/DT present)

---

## 7. Usage rules (how to use this register)
1. **System design**: ensure every Body+Brain artifact has explicit Body/Brain split and interface contracts.
2. **DPP creation**: no Brain enters service without an ATA 95 DPP pointer and an OM class.
3. **V&V planning**: DAL drives evidence depth; DV is required before DPP issuance; OAV required for OM truth.
4. **Operations**: OM is the ontological mission description; OAV validates it on asset.
5. **CCert/CVal**: the loop is closed only when DT truth updates AM′ under change control.

**Gate rule (hard):**  
If an entry has no named OAV gate, it is not yet an operationally verifiable predictive claim.

---

## 8. Workflow note (your PR question)
Yes: workflows added/modified in a PR typically execute on:
- subsequent commits to the PR, and/or
- manual `workflow_dispatch`, if enabled.

Security note: treat `pull_request_target` as privileged; use only when explicitly required.

---

## 9. Related ATA 95 foundational documents (where the “database skeleton” lives)
This register is conceptually backed by ATA 95-90 schemas:
- `95-90-02-002_Common_Entity_Schemas.md`
- `95-90-02-003_TimeSeries_and_Telemetry_Schemas.md`
- `95-90-02-006_CCert_CVal_Database_Schema.md`
- `95-90-02-008_Common_Relationship_Semantics.md`

---

## 10. Document control
| Version | Date | Author | Changes |
|---:|---|---|---|
| 1.0 | 2025-12-13 | AMPEL360/ATA 95 WG | Initial comprehensive catalog (content population) |
| 1.1 | 2025-12-13 | AMPEL360/ATA 95 WG | Sovereignty + interfacing semantics; DV/OAV separation |
| 1.2 | 2025-12-13 | AMPEL360/ATA 95 WG | Complete master doc: circuit + glossary + register + ATA placement rules |

---
