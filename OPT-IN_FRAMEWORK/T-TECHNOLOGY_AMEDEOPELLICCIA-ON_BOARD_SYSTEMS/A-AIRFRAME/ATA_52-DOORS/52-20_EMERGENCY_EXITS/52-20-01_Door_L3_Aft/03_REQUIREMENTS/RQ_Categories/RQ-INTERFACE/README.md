# RQ-INTERFACE - Interface Requirements

**Category:** RQ-INTERFACE  
**ID Range:** RQ-52-20-01-070 to RQ-52-20-01-091  
**Total Requirements:** 22  
**Priority:** High

## Requirements Summary Table

| Requirement_ID | Description | Interface_Type | Standard | Criticality | Verification | Status |
|---|---|---|---|---|---|---|
| RQ-52-20-01-070 | Fuselage_Structural_Interface | Mechanical | ATA_53 | Critical | FEA+Test | Defined |
| RQ-52-20-01-071 | Door_Frame_Mounting | Mechanical | AMPEL360 | Critical | Analysis | Defined |
| RQ-52-20-01-072 | Floor_Beam_Interface | Mechanical | ATA_53 | Critical | Test | Defined |
| RQ-52-20-01-073 | Electrical_Power_28VDC | Electrical | MIL-STD-704 | High | Test | Defined |
| RQ-52-20-01-074 | Emergency_Power_Bus | Electrical | ATA_24 | Critical | Demo | Defined |
| RQ-52-20-01-075 | ARINC_429_Data_Bus | Data | ARINC_429 | High | Test | Defined |
| RQ-52-20-01-076 | Latch_Striker_Interface | Mechanical | ATA_52 | Critical | Inspect | Defined |
| RQ-52-20-01-077 | Hinge_System_Interface | Mechanical | ATA_52 | Critical | Test | Defined |
| RQ-52-20-01-078 | Seal_Interface | Mechanical | ATA_52 | High | Test | Defined |
| RQ-52-20-01-079 | ECS_Interface | Environmental | ATA_21 | High | Analysis | Defined |
| RQ-52-20-01-080 | Drainage_Interface | Environmental | ATA_52 | Medium | Test | Defined |
| RQ-52-20-01-081 | Slide_Bustle_Interface | Mechanical | TSO-C69c | Critical | Demo | Defined |
| RQ-52-20-01-082 | Girt_Bar_Floor_Interface | Mechanical | TSO-C69c | Critical | Test | Defined |
| RQ-52-20-01-083 | Cockpit_Display_Interface | Data | ATA_31 | High | Demo | Defined |
| RQ-52-20-01-084 | Cabin_Crew_Panel | Operational | ATA_44 | High | Inspect | Defined |
| RQ-52-20-01-085 | Ground_Interface | Operational | Ground_Ops | Medium | Demo | Defined |
| RQ-52-20-01-086 | Lightning_Bonding | Electrical | CS_25.581 | Critical | Test | Defined |
| RQ-52-20-01-087 | EMI_Shielding | Electrical | DO-160G | High | Test | Defined |
| RQ-52-20-01-088 | Emergency_Lighting | Electrical | CS_25.812 | Critical | Test | Defined |
| RQ-52-20-01-089 | Escape_Path_Interface | Operational | CS_25.809 | Critical | Inspect | Defined |
| RQ-52-20-01-090 | CAOS_Data_Interface | Data | AMPEL360 | Medium | Test | Defined |
| RQ-52-20-01-091 | Sensor_Network | Data | AMPEL360 | Medium | Demo | Defined |

## Overview

This category contains all interface requirements for the Door L3 Aft Emergency Exit, including physical mounting, system connections, and data interfaces with aircraft systems.

## Interface Design Philosophy

All interfaces must:
- Be clearly defined and documented
- Have standardized connectors where possible
- Tolerate normal installation variations
- Be maintainable without special tools
- Have redundant paths for critical functions

## Key Requirements Summary

### Structural Interfaces (RQ-070 to RQ-072)
- **RQ-52-20-01-070**: Fuselage structural interface (frames 42-44)
  - Load transfer: 150% ultimate design loads
  - Interface: 12 attachment points minimum
  - FEA verification required
  
- **RQ-52-20-01-071**: Door frame mounting requirements
  - Uniform load distribution around perimeter
  - Loss of 2 points tolerable (redundancy)
  - Shims for adjustment: ±3mm
  
- **RQ-52-20-01-072**: Floor beam interface (lower sill)
  - Evacuation loads + panic loads
  - Slide girt bar load transfer
  - Vertical + horizontal components

### Electrical Interfaces (RQ-073 to RQ-075)
- **RQ-52-20-01-073**: Primary power 28VDC
  - Voltage: 22-29V nominal 28V
  - Current: 15A peak, 2A standby
  - Protection: 20A circuit breaker
  - Connector: MS3102A-20-15P
  
- **RQ-52-20-01-074**: Emergency power bus
  - Source: Essential bus
  - Duration: 30 minutes minimum
  - Load shed protected
  - Automatic switchover
  
- **RQ-52-20-01-075**: ARINC 429 data bus
  - Speed: 12.5 kbps (low speed)
  - Channels: 2 (Tx/Rx)
  - Labels: Per ATA 52 allocation
  - Protocol: ARINC 429 Mark 33

### Mechanical Interfaces (RQ-076 to RQ-078)
- **RQ-52-20-01-076**: Latch striker interface
  - Count: 8 minimum engagement points
  - Adjustment: ±3mm (rigging tolerance)
  - Material: Titanium 6Al-4V
  - Surface hardness: RC 35-40
  
- **RQ-52-20-01-077**: Hinge system interface
  - Type: Translating arc motion
  - Lubrication: Sealed bearings (lifetime)
  - Life: 20,000 cycles minimum
  - Load capacity: 200% design loads
  
- **RQ-52-20-01-078**: Pressure seal interface
  - Type: Dual seal system (primary + backup)
  - Compression: 30% nominal deflection
  - Surface finish: 32 Ra maximum
  - Seal material: Silicone rubber

### Environmental Interfaces (RQ-079 to RQ-080)
- **RQ-52-20-01-079**: ECS (cabin environment) interface
  - Pressure: 0-8.6 psi differential
  - Temperature: -20°C to +50°C cabin
  - Humidity: 5-95% RH
  - Condensation management required
  
- **RQ-52-20-01-080**: Drainage interface
  - Channels: Door and frame integrated
  - Flow capacity: 1 liter/minute minimum
  - Freeze protection: Heated if required
  - Overboard discharge path

### Slide System Interfaces (RQ-081 to RQ-082)
- **RQ-52-20-01-081**: Slide bustle interface
  - Location: Lower door interior
  - Release: Automatic on door opening (armed)
  - Manual backup: RED handle accessible
  - Pack weight: 35 kg supported
  
- **RQ-52-20-01-082**: Girt bar floor interface
  - Type: Quick-release fittings
  - Strength: 30,000 lbf minimum
  - Shear disconnect: Ditching scenario
  - Visual inspection provisions

### Operational Interfaces (RQ-083 to RQ-085)
- **RQ-52-20-01-083**: Cockpit display interface
  - Display system: EICAS/ECAM
  - Status: Door position, armed state
  - Warnings: Unsafe conditions (takeoff with door armed)
  - Format: ATA 52 standard symbology
  
- **RQ-52-20-01-084**: Cabin crew panel interface
  - Local indicators: Armed, pressure, faults
  - Location: Adjacent to door (visible from aisle)
  - Visibility: Day and night conditions
  - Test function: Built-in test (BIT)
  
- **RQ-52-20-01-085**: Ground interface
  - External controls: Door open/close from outside
  - Ground power: Compatible with GPU
  - Tools: Standard aircraft tools only
  - Safety interlocks: Ground handling mode

### Lightning/EMI Protection (RQ-086 to RQ-087)
- **RQ-52-20-01-086**: Lightning bonding
  - Electrical resistance: <3 milliohms
  - Current capacity: 200kA waveform A
  - Bond path: Dual redundant
  - Test: Per DO-160G Section 17
  
- **RQ-52-20-01-087**: EMI shielding
  - Standard: DO-160G Category M
  - Shielding effectiveness: 60dB minimum
  - Grounding: Single point to airframe
  - Cable shielding: 360° termination

### Emergency Interfaces (RQ-088 to RQ-089)
- **RQ-52-20-01-088**: Emergency lighting interface
  - Illumination: Per CS 25.812
  - Power: Independent battery backup
  - Duration: 10 minutes minimum
  - Activation: Automatic on door opening
  
- **RQ-52-20-01-089**: Escape path interface
  - Clear width: 20 inches minimum
  - Height: Floor to exit sill
  - Marking: Photoluminescent strips
  - Obstacles: None in egress path

### CAOS Interfaces (RQ-090 to RQ-091)
- **RQ-52-20-01-090**: CAOS data interface
  - Protocol: Ethernet 1Gbps
  - Data rate: 100Hz for critical parameters
  - Security: Encrypted (AES-256)
  - Isolation: Cannot affect door operation
  
- **RQ-52-20-01-091**: Sensor network interface
  - Sensors: 24 minimum (position, load, temp)
  - Sampling: 1kHz maximum rate
  - Bus: CAN bus or equivalent
  - Diagnostics: Built-in self-test

## Interface Control Documents (ICDs)

| ICD Number | Title | Interfaces | Status |
|------------|-------|------------|--------|
| ICD-52-20-01-001 | Electrical Interfaces | RQ-073 to RQ-075 | Released |
| ICD-52-20-01-002 | Structural Interfaces | RQ-070 to RQ-072 | Released |
| ICD-52-20-01-003 | Data Bus Interfaces | RQ-075, RQ-090 | Draft |
| ICD-52-20-01-004 | Slide System Interfaces | RQ-081 to RQ-082 | Released |

## Interface Verification Matrix

| Interface Type | Verification Method | Test Equipment |
|----------------|---------------------|----------------|
| Structural | Static load test | Load frames, strain gauges |
| Electrical | Functional test | Power supplies, oscilloscope |
| Data | Protocol analysis | Bus analyzer, simulator |
| Mechanical | Fit check | Coordinate measuring machine |
| EMI/Lightning | Environmental test | Anechoic chamber, HIRF lab |

## Physical Interface Locations

### Door Frame Perimeter
- **Top**: 4 attachment points + seal groove
- **Sides**: 3 attachment points each + hinges
- **Bottom**: 2 attachment points + girt bar fittings

### Internal Connections
- **Upper Right**: Electrical connector panel
- **Upper Left**: Emergency lighting connection
- **Lower Right**: CAOS sensor cluster
- **Lower Left**: Slide pack mounting bracket

## Electrical Connector Schedule

| Connector | Type | Pins | Function |
|-----------|------|------|----------|
| J1 | MS3102A-20-15P | 15 | Primary power + discretes |
| J2 | MS3102A-14-12S | 12 | ARINC 429 + backup power |
| J3 | MS3102A-10-6P | 6 | Emergency lighting |
| J4 | RJ45 | 8 | Ethernet (CAOS) |

## Interface Tolerances

### Mechanical
- **Position**: ±3mm in all axes
- **Angle**: ±0.5 degrees
- **Gap**: 2-5mm (seal compression dependent)

### Electrical
- **Voltage**: ±10% of nominal
- **Frequency**: ±0.1% (data clocks)
- **Resistance**: <100 mΩ (power), <3 mΩ (bonding)

### Environmental
- **Temperature**: ±5°C calibration accuracy
- **Pressure**: ±0.1 psi measurement
- **Humidity**: ±5% RH

## Interface Testing Requirements

### Factory Acceptance Test (FAT)
- All interfaces verified to specifications
- Functional tests with simulators
- Environmental conditioning
- EMI/EMC baseline testing

### Site Acceptance Test (SAT)
- Final installation verification
- End-to-end system tests
- Aircraft integration checks
- Flight control system interface validation

## Interface Change Control

Changes to any interface require:
1. Engineering Change Request (ECR)
2. Impact analysis on both sides of interface
3. ICD update and revision
4. Coordinated implementation schedule
5. Re-verification testing

## Common Interface Issues

| Issue | Cause | Resolution |
|-------|-------|------------|
| Pin/connector damage | Improper mating | Use alignment pins, train personnel |
| Seal leakage | Surface finish | Improve surface prep, tighter tolerance |
| EMI coupling | Poor shielding | Add ferrites, improve bonding |
| Data errors | Noise/crosstalk | Separate signal paths, shielded cables |

## Related Documents

- **04_DESIGN**: Interface mechanical drawings
- **05_INTERFACES**: Detailed ICD documents
- **06_ENGINEERING**: Interface analysis reports
- **07_V_AND_V**: Interface test procedures

---

**Document Control**  
**Version:** 1.0  
**Date:** 2025-11-04  
**Status:** Released  
**Approved by:** Chief Integration Engineer
