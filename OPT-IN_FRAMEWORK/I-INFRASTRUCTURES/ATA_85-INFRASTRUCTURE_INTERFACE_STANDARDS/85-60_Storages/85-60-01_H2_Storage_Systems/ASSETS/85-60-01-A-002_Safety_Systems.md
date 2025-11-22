# 85-60-01-A-002 — Safety Systems for H2 Storage

## Document Metadata

```yaml
asset_id: "85-60-01-A-002"
title: "Safety Systems for H2 Storage"
parent_system: "85-60-01 H2 Storage Systems"
category: "Safety Documentation"
status: "DRAFT"
version: "1.0"
last_updated: "2025-11-22"
```

## Purpose

This asset document provides comprehensive safety system specifications, safety instrumented functions, and emergency response procedures for hydrogen storage systems.

## Safety Instrumented System (SIS) Architecture

### SIS Rating

**Safety Integrity Level (SIL):** SIL 3 per [IEC 61508](https://www.iec.ch/functionalsafety/)

**Design Basis:**
- Catastrophic consequence prevention (fire, explosion, toxic release)
- Required risk reduction: >1000x (SIL 3)
- Architecture: 2oo3 (Two-out-of-Three) voting for critical sensors

### SIS Components

#### H2 Detection System

**Sensor Type:** Catalytic bead or electrochemical H2 sensors

**Locations:**
- Near LH2 tank vents (minimum 4 sensors)
- Near GH2 vessel manifolds (minimum 4 sensors per bank)
- Compressor area (minimum 4 sensors)
- Vaporizer area (minimum 2 sensors)
- Transfer line low points (minimum 2 sensors)

**Alarm Setpoints:**
- **Low Alarm:** 0.2% H2 by volume (5% LEL) — Warning only
- **High Alarm:** 0.4% H2 by volume (10% LEL) — Action required
- **Emergency Shutdown (ESD):** 0.8% H2 by volume (20% LEL) — Automatic shutdown

**Response Time:** <3 seconds from detection to alarm/action

**Voting Logic:** 2oo3 for ESD function (any 2 of 3 sensors in zone trigger shutdown)

#### Pressure Monitoring

**Pressure Transmitters:**
- LH2 tanks: 0-20 bar range, ±0.5% accuracy
- GH2 cascade vessels: 0-600 bar range, ±0.5% accuracy
- Compressor stages: Appropriate range per stage, ±0.5% accuracy

**Alarm Setpoints:**
- **High Pressure Alarm:** 95% of design pressure — Warning
- **High-High Pressure:** 98% of design pressure — Action required (reduce pressure)

**ESD Triggers:**
- LH2tank over-pressure (>design pressure)
- GH2 vessel over-pressure (>design pressure)
- Compressor discharge high pressure (>design pressure downstream equipment)

**Safety Actions:**
- Close isolation valves
- Stop compressor
- PRV should relieve pressure (if ESD fails to control)

#### Temperature Monitoring

**RTD Locations:**
- LH2 tank (liquid space, vapor space)
- Vaporizer outlet (ensure complete vaporization)
- Compressor interstage and discharge (prevent overheating)
- Ambient temperature (AAV performance monitoring)

**Alarm Setpoints:**
- **Vaporizer Low Outlet Temperature:** <-100°C — Incomplete vaporization (liquid carryover hazard)
- **Compressor High Temperature:** >100°C (or per manufacturer spec) — Overheating risk

**ESD Triggers:**
- Vaporizer outlet temperature <-150°C (liquid carryover to compressor — damage risk)
- Compressor temperature >150°C (fire or explosion risk)

#### Fire Detection

**Detector Types:**
- UV/IR flame detectors (detect hydrogen flame, which is nearly invisible)
- Thermal imaging cameras (detect heat signature)
- Heat detectors (rate-of-rise or fixed temperature)

**Coverage:**
- LH2 tank area (minimum 4 detectors for full coverage)
- GH2 vessel area (minimum 4 detectors)
- Compressor building (minimum 2 detectors)

**Alarm Response:**
- Immediate audible and visual alarm
- Notify ARFF (Airport Rescue and Fire Fighting)
- Activate water deluge system (cool vessels, not extinguish H2 fire)

**ESD Trigger:**
- Fire detected in H2 storage area → Close isolation valves, stop compressor, activate deluge

## Emergency Shutdown (ESD) System

### ESD Levels

#### ESD Level 1 — Controlled Shutdown

**Triggers:**
- High pressure alarm (not critical)
- Low H2 alarm (0.2-0.4% by volume)
- Minor equipment fault (e.g., compressor vibration alarm)

**Actions:**
1. Reduce system load (slow down or pause refueling)
2. Notify operators (investigate and correct)
3. Log event

#### ESD Level 2 — Rapid Shutdown

**Triggers:**
- High-high pressure (98% design pressure)
- High H2 alarm (0.4-0.8% by volume)
- Equipment fault requiring immediate attention (e.g., compressor high temperature)

**Actions:**
1. Stop compressor
2. Close non-critical isolation valves
3. Maintain safe conditions (do not depressurize vessels unnecessarily)
4. Notify operations and maintenance
5. Log event and conduct investigation

#### ESD Level 3 — Emergency Shutdown (Full ESD)

**Triggers:**
- H2 concentration >0.8% by volume (20% LEL)
- Fire detection
- Critical equipment failure (e.g., vessel rupture, major leak)
- Manual ESD button activation

**Actions:**
1. **Immediate (<1 second):**
   - Close all isolation valves (LH2 supply, GH2 transfer, refueling hoses)
   - Stop all pumps and compressors
   - Isolate electrical power to non-essential equipment

2. **Within 5 seconds:**
   - Activate water deluge system (if fire detected)
   - Sound evacuation alarm (audible and visual)
   - Notify ARFF and operations center

3. **Within 1 minute:**
   - Verify all personnel evacuated (check in at designated assembly area)
   - ARFF establishes safety perimeter (minimum 100m, 300m if fire)
   - Assess situation (safe approach only after H2 dispersed)

### ESD Logic

**Architecture:** Redundant PLCs (Primary and Backup)

**Logic:** 1oo2D (One-out-of-Two with Diagnostics)
- Either PLC can initiate ESD
- Continuous diagnostics detect PLC failures
- Manual ESD buttons hardwired (bypass PLCs for ultimate reliability)

**Valve Actuation:** Fail-safe design
- Spring-return pneumatic actuators (close on air loss)
- Dual solenoid valves (energize to open, de-energize to close)
- Manual override (for maintenance and testing)

## Fire Protection System

### Water Deluge System

**Purpose:** Cool H2 vessels during fire (prevent BLEVE — Boiling Liquid Expanding Vapor Explosion)

**Design:** Open nozzles (no sprinklers), activated by fire detection or manual

**Coverage:**
- LH2 tanks: 360° coverage, minimum 10 L/min/m² of tank surface area
- GH2 vessels: 360° coverage, minimum 5 L/min/m² of vessel surface area

**Water Supply:**
- Dedicated fire water tank (minimum 2 hours supply at design flow rate)
- Backup: Municipal water supply (if sufficient pressure and flow)
- Pumps: Electric (primary) and diesel (backup, auto-start on power failure)

**Activation:**
- Automatic: Fire detection in zone → Activate deluge valve for that zone
- Manual: Deluge valve control stations at safe locations (minimum 50m from H2 storage)

### Foam System (LH2 Spills)

**Purpose:** Cover LH2 spills to reduce vaporization rate (foam acts as insulation)

**Foam Type:** Alcohol-resistant foam (AFFF or protein-based)

**Application:**
- Mobile foam units (trailer-mounted, operated by ARFF)
- Fixed monitors (if spill containment area designed)

**Limitation:** Foam is not effective for extinguishing H2 fires (H2 flame temperature >2000°C, foam breaks down)

### Fire Extinguishers

**Type:** Class D (for metal fires) or Class ABC (general purpose)

**Not for H2 Fires:** Do not attempt to extinguish H2 fires with portable extinguishers (allow to burn unless leak can be stopped)

**Use:** Incipient fires in surrounding equipment or materials (not H2 itself)

## Grounding and Bonding

### Purpose

Dissipate static electricity to prevent ignition of H2-air mixture.

### Requirements

**Tank Grounding:**
- All H2 storage vessels bonded to ground grid
- Ground resistance: <10 ohms (measure annually)
- Ground grid: Bare copper conductor, buried 0.6-1m depth, encircling storage area

**Transfer Hose Bonding:**
- All transfer hoses include bonding wire (connects tanker truck or refueling equipment to storage tank)
- Bonding wire: Minimum 6 AWG (10 mm²) copper
- Verify bonding connection before transfer (resistance <1 ohm)

**Personnel Grounding:**
- Conductive footwear and flooring in H2 storage and refueling areas
- Static dissipative mats at work stations

## Emergency Response Procedures

### LH2 Spill (No Fire)

1. **Activate ESD** (close all valves, stop pumps)
2. **Evacuate personnel** (upwind, minimum 100m)
3. **Notify ARFF** (provide spill location and estimated quantity)
4. **Establish safety perimeter** (minimum 100m, no ignition sources)
5. **Monitor H2 concentration** (ARFF or trained personnel with portable detectors)
6. **Allow LH2 to vaporize naturally** (do not attempt to contain — LH2 vaporizes rapidly)
7. **Apply foam** (if trained and safe to approach — reduces vaporization rate)
8. **Re-entry** (safe only after H2 concentration <0.1% by volume, confirmed by monitoring)

### H2 Fire

**Do NOT extinguish H2 fire unless leak can be stopped (re-ignition hazard from continued H2 release)**

1. **Activate ESD** (attempt to stop H2 flow to fire)
2. **Evacuate all personnel** (minimum 300m)
3. **Notify ARFF** (provide fire location and approximate H2 quantity)
4. **Establish safety perimeter** (minimum 300m)
5. **Activate water deluge** (cool adjacent vessels, not extinguish fire)
6. **Defensive operations only** (ARFF protects exposures, allows H2 to burn off)
7. **If jet fire** (from pressurized leak):
   - Jet flame can extend 10-50 meters
   - Nearly invisible (extremely dangerous)
   - Do not approach (radiant heat and flame contact hazard)
8. **After fire self-extinguishes** (H2 exhausted):
   - Cool down area with water spray (prevent re-ignition from hot surfaces)
   - Inspect vessels for damage (ARFF thermal imaging or visual inspection)
   - Do not re-pressurize or return to service until inspection complete

### Vessel BLEVE (Catastrophic Failure)

**BLEVE Risk:** If vessel exposed to fire and pressure relief inadequate, vessel can rupture catastrophically.

**Pre-BLEVE Indicators:**
- Increasing tank pressure despite PRV operation
- Audible change in PRV discharge (from vapor to liquid, indicating boiling inside vessel)
- Thermal imaging shows hot spots on vessel (loss of insulation or internal boiling)

**ARFF Actions:**
- Recognize BLEVE risk (train on indicators)
- Withdraw to safe distance (minimum 500m)
- Evacuate all personnel (no heroic measures)
- Allow event to occur (if BLEVE happens, shrapnel can travel >300m, fireball can extend >100m)

**Post-BLEVE:**
- Account for all personnel (search and rescue if safe)
- Establish exclusion zone (minimum 500m, or per incident commander)
- Investigate debris field (document for investigation)

## Training Requirements

### Operations Personnel

**H2 Safety Fundamentals** (8 hours):
- H2 properties and hazards
- Flammability and explosion risks
- Leak detection and response
- PPE (personal protective equipment) requirements

**Storage System Operation** (16 hours):
- Normal operations (filling, vaporization, compression, dispensing)
- Alarm response (interpretation and corrective actions)
- Emergency shutdown procedures (ESD activation and verification)

**Emergency Response** (8 hours with ARFF):
- H2 leak and fire scenarios (tabletop and live exercises)
- Coordination with ARFF
- Evacuation procedures

**Recurrent Training:** Annual (8 hours, focus on lessons learned and procedure updates)

### ARFF (Airport Rescue and Fire Fighting)

**H2 Incident Response** (16 hours):
- H2 fire behavior (jet fires, pool fires, vapor cloud explosions)
- Detection (H2 flames nearly invisible, use thermal imaging)
- Tactics (defensive operations, cool exposures, let H2 burn)
- BLEVE recognition and withdrawal criteria

**Live Fire Training** (recommended annually):
- Controlled H2 fire exercises (small scale for safety)
- Thermal imaging practice (detecting invisible flames)
- Water deluge system operation

## Maintenance and Testing

### H2 Detection System

**Monthly:**
- Bump test (expose sensors to known H2 concentration, verify alarm)
- Check alarm annunciation (audible and visual)

**Quarterly:**
- Full calibration (adjust sensor output to match reference gas)
- Test alarm setpoints (verify correct thresholds)

**Annual:**
- Replace sensors (or per manufacturer recommendation, typically 2-5 year life)
- Full system functional test (simulate H2 leak, verify ESD activation)

### Fire Detection System

**Monthly:**
- Test flame detectors (simulate flame with test lamp)
- Check camera operation (if thermal imaging)

**Quarterly:**
- Full system functional test (verify alarm transmission and deluge activation — no water release)

**Annual:**
- Flow test deluge system (full water flow, verify coverage and flow rates)

### ESD System

**Monthly:**
- Stroke test automated valves (partial stroke, verify movement)
- Test manual ESD buttons (simulate, do not actuate)

**Quarterly:**
- Full ESD test (coordinate with operations, secure system, actuate ESD, verify all functions)
- Test PLC redundancy (disconnect primary PLC, verify backup takes over)

**Annual:**
- Full system validation (inspect all wiring, test all interlocks, document results)

## Document Control

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT** – Subject to human review and approval.
- Human approver: _[to be completed]_.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: 2025-11-22

---

*Reference: [85-60-01 H2 Storage Systems README](../README.md)*
