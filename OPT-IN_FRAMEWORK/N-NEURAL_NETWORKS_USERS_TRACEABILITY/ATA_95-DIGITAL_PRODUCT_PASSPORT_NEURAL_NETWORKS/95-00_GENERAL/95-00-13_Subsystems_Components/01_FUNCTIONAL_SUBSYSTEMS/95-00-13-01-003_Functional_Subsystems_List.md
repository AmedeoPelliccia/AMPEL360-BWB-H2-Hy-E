# 95-00-13-01-003: Functional Subsystems List

## Document Information
- **Document ID**: 95-00-13-01-003
- **Title**: Functional Subsystems List
- **Version**: 1.0
- **Status**: Active
- **Last Updated**: 2025-11-17

## Functional Subsystems Catalog

| ID | Name | Primary Function | Criticality | ATA Ch | Status |
|----|------|------------------|-------------|---------|--------|
| FS-001 | Flight Control | Aircraft attitude & trajectory control | DAL-A | 22,27 | Active |
| FS-002 | Navigation | Position, velocity determination | DAL-A | 34 | Active |
| FS-003 | Communication | Voice & data communication | DAL-B | 23 | Active |
| FS-004 | Power Management | Electrical power generation & distribution | DAL-B | 24 | Active |
| FS-005 | Mission Management | Mission planning & execution | DAL-C | 22,28 | Active |
| FS-006 | Environmental Control | Cabin & equipment environment | DAL-C | 21 | Active |
| FS-007 | Fuel System | H₂ fuel storage & delivery | DAL-B | 28 | Active |
| FS-008 | Display & Crew Interface | Information presentation & input | DAL-B | 31 | Active |
| FS-009 | Data Recording | Flight data & voice recording | DAL-C | 31 | Active |
| FS-010 | Health Monitoring | System health & diagnostics | DAL-D | 45 | Active |
| FS-011 | Landing Gear Control | Landing gear extension/retraction | DAL-B | 32 | Active |
| FS-012 | Ice & Rain Protection | Anti-icing & de-icing | DAL-C | 30 | Active |
| FS-013 | Fire Protection | Fire detection & suppression | DAL-B | 26 | Active |
| FS-014 | Lighting | Interior & exterior lighting | DAL-D | 33 | Active |
| FS-015 | Oxygen System | Emergency oxygen supply | DAL-B | 35 | Active |

## Detailed Subsystem Descriptions

### FS-001: Flight Control Subsystem
- **Primary Function**: Maintain aircraft attitude, trajectory, and stability
- **Key Capabilities**: Pitch, roll, yaw control; stability augmentation; autopilot
- **Interfaces**: Control surfaces, pilot inputs, navigation data
- **Implementation**: Fly-by-wire control laws, redundant computers

### FS-002: Navigation Subsystem
- **Primary Function**: Determine aircraft position, velocity, and attitude
- **Key Capabilities**: GNSS processing, inertial navigation, sensor fusion
- **Interfaces**: GNSS receivers, IMU, air data system
- **Implementation**: Multi-sensor fusion algorithms, Kalman filtering

### FS-003: Communication Subsystem
- **Primary Function**: Enable voice and data communication
- **Key Capabilities**: VHF voice, data link, satcom, ADS-B
- **Interfaces**: Cockpit, ATC, ground stations, other aircraft
- **Implementation**: Digital radios, data link processors

### FS-004: Power Management Subsystem
- **Primary Function**: Generate, distribute, and manage electrical power
- **Key Capabilities**: H₂ fuel cell generation, distribution, load management
- **Interfaces**: All electrical loads, fuel cells, batteries
- **Implementation**: Power distribution units, smart load management

### FS-005: Mission Management Subsystem
- **Primary Function**: Plan and coordinate mission execution
- **Key Capabilities**: Flight planning, optimization, fuel management
- **Interfaces**: Crew, navigation, power, communication systems
- **Implementation**: Mission planning algorithms, optimization engines

## Cross-Reference Matrix

See: ASSETS/95-00-13-01-A-002_Subsystems_Allocation_Table.csv for detailed allocations.

## Related Documents

- 95-00-13-01-001: Functional Subsystems Overview
- 95-00-13-01-004: Modes and Operational Contexts
- 95-00-13-00-003: Subsystems Taxonomy

## Revision History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | 2025-11-17 | AMPEL360 Documentation WG | Initial release |
