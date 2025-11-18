# [95-00-13-01-001](95-00-13-01-001.md): Functional Subsystems Overview

## Document Information
- **Document ID**: [95-00-13-01-001](95-00-13-01-001.md)
- **Title**: Functional Subsystems Overview
- **Version**: 1.0
- **Status**: Active
- **Last Updated**: 2025-11-17

## Purpose

This document provides a comprehensive overview of the functional subsystems of the AMPEL360 BWB H₂ Hy-E aircraft, organized by their primary mission capabilities.

## Definition

**Functional Subsystems** are groups of components organized around specific aircraft functions or capabilities, independent of their physical implementation (hardware, software, or hybrid).

## Key Functional Subsystems

### 1. Flight Control Subsystem
**Primary Function**: Maintain aircraft attitude, trajectory, and stability

**Components**:
- Primary flight control laws
- Autopilot functions
- Fly-by-wire processing
- Control surface management
- Stability augmentation

**Interfaces**:
- Control surfaces (ailerons, elevators, rudder)
- Pilot inputs (sidestick, pedals)
- Navigation subsystem
- Air data system

**Criticality**: DAL-A (Safety Critical)

**ATA Chapters**: ATA-22, ATA-27

### 2. Navigation Subsystem
**Primary Function**: Determine aircraft position, velocity, and attitude

**Components**:
- GNSS receivers and processing
- Inertial navigation (INS/IMU)
- Sensor fusion algorithms
- Position estimation
- Velocity computation

**Interfaces**:
- GNSS satellites
- Inertial sensors
- Air data system
- Flight management system

**Criticality**: DAL-A (Safety Critical)

**ATA Chapters**: ATA-34

### 3. Communication Subsystem
**Primary Function**: Enable voice and data communication

**Components**:
- VHF voice communication
- Data link (VDL, CPDLC)
- Satcom interface
- Internal communication (intercom)
- Emergency locator transmitter

**Interfaces**:
- Ground stations
- Air traffic control
- Flight crew
- Other aircraft (ADS-B)

**Criticality**: DAL-B (Essential)

**ATA Chapters**: ATA-23

### 4. Power Management Subsystem
**Primary Function**: Generate, distribute, and manage electrical power

**Components**:
- H₂ fuel cell power generation
- Battery backup systems
- Power distribution units
- Voltage regulation
- Load management

**Interfaces**:
- All electrical loads
- Fuel cell system
- Battery systems
- Thermal management

**Criticality**: DAL-B (Essential)

**ATA Chapters**: ATA-24

### 5. Mission Management Subsystem
**Primary Function**: Plan and coordinate mission execution

**Components**:
- Flight planning
- Route optimization
- Fuel management
- Performance monitoring
- Mission reconfiguration

**Interfaces**:
- Flight crew
- Navigation subsystem
- Power management
- Communication subsystem

**Criticality**: DAL-C (Important)

**ATA Chapters**: ATA-22, ATA-28

### 6. Environmental Control Subsystem
**Primary Function**: Maintain cabin and equipment environment

**Components**:
- Cabin pressurization
- Temperature control
- Humidity management
- Air circulation
- Equipment cooling

**Interfaces**:
- Pneumatic system
- Air conditioning packs
- Bleed air sources
- Equipment bays

**Criticality**: DAL-C (Important)

**ATA Chapters**: ATA-21

### 7. Fuel System Subsystem
**Primary Function**: Store and deliver H₂ fuel to fuel cells

**Components**:
- H₂ storage tanks
- Fuel delivery system
- Tank pressure management
- Fuel quantity indication
- Leak detection

**Interfaces**:
- Fuel cells
- Fueling interface
- Monitoring systems
- Vent system

**Criticality**: DAL-B (Essential)

**ATA Chapters**: ATA-28

### 8. Display & Crew Interface Subsystem
**Primary Function**: Present information to crew and accept inputs

**Components**:
- Primary flight displays (PFD)
- Navigation displays (ND)
- Engine/system displays (EICAS)
- Control panels
- Warning/caution systems

**Interfaces**:
- All monitored subsystems
- Flight crew
- Flight control subsystem
- Mission management

**Criticality**: DAL-B (Essential)

**ATA Chapters**: ATA-31

### 9. Data Recording Subsystem
**Primary Function**: Record flight data and cockpit voice

**Components**:
- Flight data recorder (FDR)
- Cockpit voice recorder (CVR)
- Quick access recorder (QAR)
- Data acquisition units
- Crash-protected memory

**Interfaces**:
- All monitored subsystems
- Cockpit audio
- Data buses
- Maintenance system

**Criticality**: DAL-C (Important)

**ATA Chapters**: ATA-31

### 10. Health Monitoring Subsystem
**Primary Function**: Monitor system health and predict failures

**Components**:
- Central maintenance system (CMS)
- Health and usage monitoring
- Built-in test equipment (BITE)
- Prognostics algorithms
- Alert generation

**Interfaces**:
- All monitored subsystems
- Display subsystem
- Data recording subsystem
- Ground maintenance

**Criticality**: DAL-D (Standard)

**ATA Chapters**: ATA-45

## Functional Decomposition Principles

### Allocation Criteria
1. **Primary Function**: Single, clear mission capability
2. **Independence**: Minimal coupling with other subsystems
3. **Testability**: Can be verified independently
4. **Certification**: Aligned with certification requirements

### Interface Management
- Well-defined functional interfaces
- Standard data exchange formats
- Timing and performance requirements
- Error handling and recovery

### Mode-Based Organization
Subsystems operate differently in various flight modes:
- Ground operations
- Taxi
- Takeoff
- Climb
- Cruise
- Descent
- Approach
- Landing
- Emergency modes

## Subsystem Interactions

### Critical Paths
1. **Primary Flight Path**: Sensors → Navigation → Flight Control → Actuators
2. **Power Path**: Fuel → Fuel Cells → Power Distribution → Loads
3. **Crew Interface Path**: Subsystems → Data Processing → Displays → Crew

### Data Flows
- Real-time control loops (100+ Hz)
- Monitoring data (1-10 Hz)
- Configuration data (on-demand)
- Diagnostic data (event-driven)

## Traceability

### To Requirements
See: [95-00-13-01-005_Links_to_95-00-03_Requirements.md](95-00-13-01-005_Links_to_95-00-03_Requirements.md)

### To ATA Systems
See: [ASSETS/95-00-13-01-A-002_Subsystems_Allocation_Table.csv](ASSETS/95-00-13-01-A-002_Subsystems_Allocation_Table.csv)

### To Operational Modes
See: [95-00-13-01-004_Modes_and_Operational_Contexts](95-00-13-01-004_Modes_and_Operational_Contexts.md).md

## Related Documents

- [95-00-13-01-002](95-00-13-01-002.md): Functional Decomposition Rules
- [95-00-13-01-003](95-00-13-01-003.md): Functional Subsystems List
- [95-00-13-00-003](../00_META/95-00-13-00-003.md): Subsystems Taxonomy
- [95-00-03](../../95-00-03_*/): Requirements Documentation
- [95-00-05](../../95-00-05_*/): Interfaces Documentation

## Revision History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | 2025-11-17 | AMPEL360 Documentation WG | Initial release |
