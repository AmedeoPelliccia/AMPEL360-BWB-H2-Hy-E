# 85-80-01-001 Primary Distribution 33kV

## Document Information

- **Document ID**: 85-80-01-001
- **Title**: Primary Distribution 33kV System Standards
- **Version**: 1.0
- **Status**: DRAFT
- **Date**: 2025-11-22

## Purpose

This document establishes standards and specifications for 33kV primary electrical distribution systems at airport facilities supporting AMPEL360 BWB-H2-Hy-E aircraft operations.

## Scope

Defines requirements for:

- 33kV primary distribution network topology
- Switchgear and protection equipment
- Transformer substations (33kV/11kV)
- Cable specifications and routing
- System protection and fault management
- Monitoring and control systems

## System Architecture

### Network Configuration

The 33kV primary distribution system shall employ a ring main configuration to provide redundancy and reliability:

- **Ring Main Units (RMUs)** at strategic locations
- **Normally Open Points (NOPs)** for sectionalizing
- **Automatic Transfer Schemes** for fault isolation
- **Dual Feed** to critical substations

### Voltage Regulation

- **Nominal Voltage**: 33kV ±10%
- **Operating Range**: 30.5kV to 36.5kV
- **Voltage Drop Limit**: Maximum 5% under full load
- **Power Factor**: Minimum 0.95 lagging

## Equipment Standards

### Switchgear

#### Ring Main Units (RMUs)

- **Type**: SF6 gas-insulated or air-insulated
- **Rated Voltage**: 36kV
- **Rated Current**: 630A minimum
- **Breaking Capacity**: 20kA for 3 seconds
- **Standards**: [IEC 62271-200](https://www.iec.ch/), [IEC 62271-100](https://www.iec.ch/)

#### Protection Relays

- **Type**: Numerical multifunction relays
- **Functions**: Overcurrent, earth fault, directional, distance protection
- **Communication**: IEC 61850 compliant
- **Standards**: [IEC 60255](https://www.iec.ch/)

### Transformers

#### 33/11kV Power Transformers

- **Type**: Oil-immersed or dry-type (environment dependent)
- **Power Rating**: 5 MVA to 20 MVA
- **Vector Group**: Dyn11 (star-delta with neutral)
- **Cooling**: ONAN/ONAF for oil-type
- **Efficiency**: Minimum 98.5% at full load
- **Standards**: [IEC 60076](https://www.iec.ch/)

#### Voltage Regulation

- **On-Load Tap Changer (OLTC)**: ±10% in 17 steps (±1.25% per step)
- **Automatic Voltage Control**: Integrated with SCADA
- **Control Strategy**: Maintain 11kV ±2.5%

## Cable Specifications

### High Voltage Cables

- **Type**: XLPE (Cross-Linked Polyethylene) insulated
- **Conductor**: Stranded aluminum or copper
- **Screen**: Copper wire screen with semiconducting layers
- **Sheath**: PVC or LSZH (Low Smoke Zero Halogen)
- **Standards**: [IEC 60502](https://www.iec.ch/)

### Cable Sizing Criteria

- **Current Carrying Capacity**: Based on ambient temperature 40°C, burial depth, and grouping
- **Short Circuit Rating**: Minimum 1 second at 20kA
- **Voltage Drop**: Maximum 2% under normal conditions
- **Installation**: Direct buried, duct banks, or cable trays per 85-80-01-005

## Protection and Control

### Protection Philosophy

1. **Primary Protection**: Main protection at each RMU
   - Instantaneous overcurrent (50)
   - Time-delayed overcurrent (51)
   - Earth fault protection (50N/51N)
   - Directional protection (67) where applicable

2. **Backup Protection**: Remote backup at upstream substations
   - Time-graded overcurrent
   - Distance protection for long feeders

3. **Auto-Reclosing**: 
   - Single-shot auto-reclose for transient faults
   - Lockout after unsuccessful reclose

### Coordination

- **Discrimination Time**: Minimum 0.3 seconds between protection stages
- **Coordination Study**: Required for all protection devices (see 85-80-01-A-003)
- **Software Tools**: ETAP, CAPE, or equivalent

## System Monitoring

### SCADA Integration

- **Protocol**: IEC 61850 or DNP3
- **Data Points**: Voltage, current, power, energy, status indications
- **Remote Control**: Circuit breaker open/close commands
- **Alarms**: Fault detection, equipment status, abnormal conditions
- **Integration**: See [85-80-06 Energy Management Systems](../85-80-06_Energy_Management_Systems/README.md)

### Power Quality Monitoring

- **Harmonic Analysis**: THD monitoring at critical points
- **Voltage Sags/Swells**: Event recording
- **Frequency**: Continuous monitoring
- **Standards**: [IEEE 1159](https://standards.ieee.org/), [IEC 61000-4-30](https://www.iec.ch/)

## Safety Requirements

### Earthing and Bonding

- **Earth Electrode System**: Grid earthing system
- **Earth Resistance**: Maximum 1 ohm at main substations
- **Equipotential Bonding**: All metallic structures bonded
- **Standards**: [IEEE 80](https://standards.ieee.org/) - Guide for Safety in AC Substation Grounding

### Arc Flash Protection

- **Arc Flash Study**: Required for all 33kV installations
- **Personal Protective Equipment (PPE)**: Based on incident energy calculations
- **Arc Flash Labels**: At all access points
- **Standards**: [IEEE 1584](https://standards.ieee.org/) - Guide for Performing Arc Flash Hazard Calculations

### Access Control

- **Restricted Access**: 33kV equipment in secured enclosures
- **Interlocking**: Mechanical and electrical interlocks on switchgear
- **Signage**: Warning signs and safety labels per local regulations

## Maintenance Requirements

### Routine Inspections

- **Visual Inspection**: Monthly
- **Thermographic Survey**: Quarterly for connections and terminations
- **Protection Relay Testing**: Annual
- **Switchgear Maintenance**: Biennial
- **Transformer Oil Analysis**: Annual for oil-filled transformers

### Condition Monitoring

- **Partial Discharge Monitoring**: For cables and switchgear (where applicable)
- **Dissolved Gas Analysis (DGA)**: For oil-filled transformers
- **Temperature Monitoring**: Continuous for transformers and cables

## Documentation Requirements

### Design Documentation

- Single-line diagrams (see 85-80-01-A-001)
- Protection settings and coordination study (see 85-80-01-A-003)
- Cable schedules and routing drawings
- Load flow analysis (see 85-80-01-A-002)
- Short circuit calculations

### As-Built Documentation

- Updated drawings reflecting actual installation
- Test reports (commissioning, protection relay, insulation)
- Equipment certificates and warranties
- Operation and maintenance manuals

## Compliance and Standards

### Primary Standards

- [IEC 62271](https://www.iec.ch/) - High-voltage switchgear and controlgear
- [IEC 60076](https://www.iec.ch/) - Power transformers
- [IEC 60502](https://www.iec.ch/) - Power cables with extruded insulation
- [IEC 61850](https://www.iec.ch/) - Communication networks and systems for power utility automation
- [IEEE 141 (Red Book)](https://standards.ieee.org/) - Electrical Power Distribution for Industrial Plants

### Regional Standards

- Europe: EN standards aligned with IEC
- North America: IEEE, ANSI, NFPA 70 (NEC)
- Local airport authority standards and regulations

## Cross-References

- **85-80-01-002** - Secondary Distribution 11kV (downstream systems)
- **85-80-01-004** - Substation Design (physical layout and civil works)
- **85-80-01-005** - Cable Routing Standards (installation methods)
- **85-80-06-001** - SCADA Architecture (monitoring and control)
- **85-80-07** - Emergency Power (integration with backup systems)

## Revision History

| Version | Date       | Author               | Changes                  |
|---------|------------|----------------------|--------------------------|
| 1.0     | 2025-11-22 | AMPEL360 Doc Team    | Initial release          |

## Document Control

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT** – Subject to human review and approval.
- Human approver: _[to be completed]_.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: _2025-11-22_.

---
