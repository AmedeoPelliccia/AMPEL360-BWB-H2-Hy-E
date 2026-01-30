# 85-80-01-002 Secondary Distribution 11kV

## Document Information

- **Document ID**: 85-80-01-002
- **Title**: Secondary Distribution 11kV System Standards
- **Version**: 1.0
- **Status**: DRAFT
- **Date**: 2025-11-22

## Purpose

This document establishes standards for 11kV secondary electrical distribution systems serving airport operational areas, including terminal buildings, apron areas, and support facilities for AMPEL360 aircraft operations.

## Scope

Covers:

- 11kV distribution network architecture
- Switchgear and protection systems
- 11kV/400V distribution transformers
- Cable systems and installation
- Load management and monitoring
- Integration with primary distribution (33kV)

## System Architecture

### Network Topology

The 11kV distribution network shall be configured as:

- **Radial System** with sectionalizing capability
- **Loop Feed** for critical loads
- **Tie Points** between feeders for flexibility
- **Dedicated Feeders** for high-priority loads (H2 production, aircraft charging)

### Voltage Characteristics

- **Nominal Voltage**: 11kV ±5%
- **Operating Range**: 10.45kV to 11.55kV
- **Voltage Drop Limit**: Maximum 3% from substation to end-use
- **Power Factor**: Minimum 0.95 (capacitor banks where required)

## Equipment Standards

### Switchgear

#### 11kV Metal-Clad Switchgear

- **Type**: Air-insulated or SF6 gas-insulated
- **Rated Voltage**: 12kV
- **Rated Current**: 630A to 1250A
- **Breaking Capacity**: 25kA for 1 second
- **Bus bar System**: Copper, rated for full fault current
- **Standards**: [IEC 62271-200](https://www.iec.ch/)

#### Circuit Breakers

- **Type**: Vacuum circuit breakers (VCB)
- **Operating Mechanism**: Spring-charged or motor-driven
- **Number of Operations**: Minimum 10,000 mechanical, 100 at rated current
- **Standards**: [IEC 62271-100](https://www.iec.ch/)

### Transformers

#### 11kV/400V Distribution Transformers

- **Type**: Cast resin (dry-type) or oil-immersed
- **Power Rating**: 500 kVA to 2500 kVA typical
- **Vector Group**: Dyn11
- **Impedance**: 4% to 6%
- **Efficiency**: Minimum 98% at 50% load, 98.5% at full load
- **Temperature Rise**: Class F insulation, Class B rise
- **Standards**: [IEC 60076](https://www.iec.ch/)

#### Transformer Selection Criteria

| Application                  | Rating     | Type       | Location          |
|------------------------------|------------|------------|-------------------|
| Terminal Building            | 1000-2500  | Cast Resin | Indoor            |
| Apron Ground Power           | 1000-1600  | Cast Resin | Outdoor Enclosure |
| H2 Production Facility       | 1600-2500  | Oil/Resin  | Dedicated Subst.  |
| Maintenance Hangars          | 1000-1600  | Cast Resin | Indoor            |
| General Loads                | 500-1000   | Cast Resin | Indoor/Outdoor    |

## Cable Specifications

### 11kV XLPE Cables

- **Conductor**: Stranded aluminum or copper
- **Insulation**: XLPE (Cross-Linked Polyethylene)
- **Screen**: Copper wire or tape screen
- **Sheath**: PVC or LSZH
- **Current Rating**: Based on IEC 60502-2
- **Standards**: [IEC 60502-2](https://www.iec.ch/)

### Cable Installation

- **Direct Buried**: Minimum depth 1.0m, with warning tape
- **Duct Banks**: HDPE or PVC ducts, concrete encased where required
- **Cable Trays**: Fire-rated trays in buildings
- **Separation**: Minimum 300mm from LV cables, 500mm from communication cables
- **Details**: See [85-80-01-005 Cable Routing Standards](./85-80-01-005_Cable_Routing_Standards.md)

## Protection Systems

### Protection Scheme

#### Feeder Protection

1. **Instantaneous Overcurrent (ANSI 50)**
   - Pickup: 8-10 x rated current
   - Time Delay: 0.1 seconds

2. **Time Overcurrent (ANSI 51)**
   - Pickup: 1.3 x rated current
   - Curve: IEC Standard Inverse (SI)

3. **Earth Fault Protection (ANSI 51N)**
   - Pickup: 20% of phase fault setting
   - Curve: IEC Very Inverse (VI)

4. **Undervoltage Protection (ANSI 27)**
   - Pickup: 80% of nominal voltage
   - Time Delay: 2 seconds

#### Transformer Protection

- **Differential Protection (ANSI 87T)**: For transformers ≥1000 kVA
- **Buchholz Relay**: For oil-immersed transformers
- **Thermal Overload (ANSI 49)**: Based on winding temperature
- **HV/LV Overcurrent Backup**: Time-graded with upstream protection

### Protection Coordination

- **Discrimination Time**: 0.3 seconds minimum between devices
- **Coordination Study**: Required for all new installations and modifications
- **Documentation**: See [85-80-01-A-003_Protection_Settings.csv](./ASSETS/85-80-01-A-003_Protection_Settings.csv)

## Load Management

### Load Categories

#### Priority 1 - Critical Loads

- Air traffic control systems
- Emergency lighting and fire protection
- H2 production safety systems
- Critical communication systems
- **Backup**: Must have dual feed or emergency generation

#### Priority 2 - Essential Loads

- Aircraft ground power supply
- Apron lighting
- Terminal HVAC (reduced capacity acceptable)
- Security systems
- **Backup**: Single feed with fast transfer to backup

#### Priority 3 - Non-Essential Loads

- General building services
- Retail areas
- Administrative offices
- **Backup**: Not required

### Load Shedding

Automatic load shedding shall be implemented based on:

- Overload conditions
- Loss of primary supply
- Emergency situations
- **Sequence**: Priority 3 → Priority 2 (partial) → Priority 1 (never shed)

## Power Quality

### Harmonic Management

- **Total Harmonic Distortion (THD)**: Maximum 5% voltage, 8% current
- **Individual Harmonics**: Per [IEEE 519](https://standards.ieee.org/)
- **Mitigation**: Harmonic filters where necessary (H2 electrolyzers, large VFDs)

### Voltage Regulation

- **Automatic Voltage Regulators**: On key feeders to maintain ±2.5%
- **Capacitor Banks**: For power factor correction (target 0.98)
- **Control**: Integrated with SCADA for real-time adjustment

## SCADA and Monitoring

### Remote Monitoring

- **Voltage and Current**: Real-time per feeder
- **Power and Energy**: Active, reactive, and apparent
- **Power Factor**: Continuous monitoring
- **Alarms**: Fault conditions, equipment status, abnormal operation

### Communication

- **Protocol**: IEC 61850 or Modbus TCP/IP
- **Network**: Redundant fiber optic backbone
- **Integration**: See [85-80-06-001 SCADA Architecture](../85-80-06_Energy_Management_Systems/85-80-06-001_SCADA_Architecture.md)

## Safety and Earthing

### Earthing System

- **System Type**: TN-S (separate neutral and earth)
- **Earth Electrode**: Copper rod or grid
- **Earth Resistance**: Maximum 1 ohm at distribution substations
- **Bonding**: All metallic structures and cable screens

### Arc Flash Protection

- **Arc Flash Study**: Mandatory for all 11kV installations
- **PPE Category**: Based on incident energy (typically Category 2-3)
- **Arc Flash Labels**: Required at all switchgear access points
- **Standards**: [IEEE 1584](https://standards.ieee.org/)

## Maintenance

### Preventive Maintenance Schedule

| Equipment                 | Inspection      | Testing         | Major Service   |
|---------------------------|-----------------|-----------------|-----------------|
| Switchgear                | Monthly         | Annual          | 5 years         |
| Circuit Breakers          | Quarterly       | Annual          | 3 years         |
| Transformers (Dry)        | Quarterly       | Biennial        | 10 years        |
| Transformers (Oil)        | Monthly         | Annual + Oil    | 5 years         |
| Protection Relays         | Quarterly       | Annual          | N/A (electronic)|
| Cables                    | Visual/Thermal  | 5 years (PD)    | As needed       |

### Condition Monitoring

- **Switchgear Temperature**: Continuous monitoring at critical connections
- **Transformer Monitoring**: Temperature, load, and oil quality (oil-filled)
- **Partial Discharge**: Online monitoring for critical feeders

## Documentation

### Required Design Documents

- Single-line diagrams (see [85-80-01-A-001](./ASSETS/85-80-01-A-001_Single_Line_Diagrams.svg))
- Cable schedules and routing plans
- Load flow analysis results (see [85-80-01-A-002](./ASSETS/85-80-01-A-002_Load_Flow_Analysis.csv))
- Protection coordination study (see [85-80-01-A-003](./ASSETS/85-80-01-A-003_Protection_Settings.csv))
- Substation layouts (see [85-80-01-004](./85-80-01-004_Substation_Design.md))

### Operational Documents

- Operating procedures (normal and emergency)
- Switching schedules
- Lockout/tagout procedures
- Emergency response plans

## Standards and Compliance

### International Standards

- [IEC 62271-200](https://www.iec.ch/) - AC metal-enclosed switchgear and controlgear
- [IEC 60076](https://www.iec.ch/) - Power transformers
- [IEC 60502-2](https://www.iec.ch/) - Power cables with extruded insulation for rated voltages from 6 kV to 30 kV
- [IEC 61850](https://www.iec.ch/) - Communication networks and systems for power utility automation
- [IEEE 519](https://standards.ieee.org/) - Harmonic Control in Electrical Power Systems

### Regional Compliance

- European Union: EN standards, Low Voltage Directive
- North America: NFPA 70 (NEC), IEEE standards
- Local: Airport authority electrical codes

## Cross-References

- **85-80-01-001** - Primary Distribution 33kV (upstream supply)
- **85-80-01-003** - Low Voltage Distribution 400V (downstream loads)
- **85-80-01-004** - Substation Design (physical infrastructure)
- **85-80-01-005** - Cable Routing Standards (installation details)
- **85-80-06** - Energy Management Systems (monitoring and control)

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
