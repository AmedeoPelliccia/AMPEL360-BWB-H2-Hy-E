# 10-00-11-13A: H2 System Baseline

## Document Information
- **Document ID**: 10-00-11-13A
- **Title**: H2 System Baseline
- **Version**: 1.0.0
- **Date**: 2025-12-11
- **Status**: DRAFT
- **Document Type**: baseline
- **Baseline Type**: H2BL
- **Milestone**: CDR
- **H2 Related**: true
- **Cryo Related**: true

## Purpose

This document establishes the H2 System Baseline (H2BL) for the AMPEL360-BWB-H2 aircraft, defining the approved configuration of all hydrogen fuel system components, safety systems, and cryogenic systems as they relate to parking, mooring, and storage operations.

## Scope

The H2 System Baseline covers:
- LH2 (Liquid Hydrogen) fuel tank configuration
- H2 safety systems for ground operations
- H2 venting system configuration
- Cryogenic system configuration
- H2 detection and monitoring systems
- H2 ground handling procedures
- Emergency response systems

## Baseline Establishment

### Baseline Criteria

The H2BL is established when:
- H2 fuel system design is complete and approved
- Safety analysis (FHA, PSSA) is completed for H2 systems
- H2 ground handling procedures are validated
- CDR for H2 systems is successfully completed
- Regulatory authority consultation complete
- CCB approves H2 baseline freeze

### Baseline Date

- **Target CDR Date**: TBD
- **H2BL Freeze Date**: TBD
- **CCB Approval**: [Pending]
- **Authority Consultation**: [In Progress]

## H2 Fuel System Configuration

### 1. LH2 Tank System

**Configuration**: 
- Tank Type: Cryogenic vacuum-insulated
- Capacity: TBD liters (LH2)
- Operating Pressure: TBD bar
- Operating Temperature: -253°C (20K)
- Tank Location: [Fuselage/Wing integration TBD]

**CI**: CI-10-H2-TANK-001 v1.0.0

**Ground Operational States**:
- Fueled (parking with H2)
- Defueled (storage without H2)
- Preservation (long-term storage)

### 2. Cryo Insulation System

**Configuration**:
- Insulation Type: Multi-layer vacuum insulation (MLVI)
- Thermal Performance: TBD W/K heat leak
- Vacuum Level: < 10^-4 mbar
- Monitoring: Vacuum pressure sensors

**CI**: CI-10-H2-INSUL-001 v1.0.0

**Parking/Storage Requirements**:
- Vacuum integrity check every 7 days
- Boil-off monitoring during parking
- Thermal protection during long-term storage

### 3. H2 Venting System

**Configuration**:
- Primary Vent: Atmospheric discharge above aircraft
- Emergency Vent: Rapid discharge capability
- Vent Height: TBD meters above ground
- Dispersion Zone: 25m radius (preliminary)

**CI**: CI-10-H2-VENT-001 v1.0.0

**Venting Scenarios**:
- Normal boil-off during parking
- Pressure relief during ground operations
- Emergency pressure release
- Tank defueling preparation

**Vent Rates**:
- Normal: TBD kg/hr
- Emergency: TBD kg/hr

## H2 Safety System Configuration

### 4. H2 Detection System

**Configuration**:
- Detection Method: Electrochemical H2 sensors
- Coverage Zones: Parking area, storage area, maintenance zones
- Sensor Locations: TBD (based on dispersion modeling)
- Alert Levels:
  - Level 1 (Caution): 1% H2 concentration (2500 ppm)
  - Level 2 (Warning): 2% H2 concentration (5000 ppm)
  - Level 3 (Danger): 4% H2 concentration (10000 ppm)

**CI**: CI-10-H2-DETECT-001 v1.0.0

**Integration**:
- Airport fire alarm system
- Ground crew notification system
- Aircraft cockpit warning system (when powered)

### 5. H2 Safety Zones

**Configuration**:
- **Zone 1 (Exclusion)**: 5m radius from vent outlet
  - No personnel, no ignition sources, no equipment
- **Zone 2 (Restricted)**: 15m radius from vent
  - Essential personnel only, no ignition sources
  - Intrinsically safe equipment only
- **Zone 3 (Controlled)**: 25m radius from vent
  - Controlled access, restricted ignition sources
  - Non-sparking tools required

**CI**: CI-10-H2-ZONES-001 v1.0.0

**Marking**: 
- Ground markings per airport standards
- Signage: "HYDROGEN AIRCRAFT - NO SMOKING - NO IGNITION SOURCES"

### 6. Emergency Response System

**Configuration**:
- Emergency Stop: Manual H2 system shutdown
- Fire Suppression: Dry chemical/foam capability
- Personnel Protection: H2-rated PPE availability
- Emergency Procedures: Posted at parking positions

**CI**: CI-10-H2-EMERG-001 v1.0.0

## Cryogenic System Configuration

### 7. Cryo Management System

**Configuration**:
- Temperature Monitoring: Cryogenic RTD sensors
- Pressure Monitoring: Cryogenic pressure transducers
- Thermal Control: Passive (insulation) + Active (cooling)
- Data Logging: Continuous during parking

**CI**: CI-10-CRYO-MGT-001 v1.0.0

**Parking Operations**:
- Pressure management: Auto-vent above TBD bar
- Temperature monitoring: Alert if > -250°C
- Boil-off calculation: Estimated parking duration

### 8. Cryo Valve Configuration

**Valves**:
- Tank Isolation Valve: Normally closed during parking
- Vent Valve: Automatic pressure relief
- Fill/Drain Valves: Locked closed during parking
- Emergency Shutoff: Manual quick-close

**CI**: CI-10-CRYO-VALVE-001 v1.0.0

**Material**: Stainless steel 316L (cryogenic rated)
**Seals**: PTFE (cryogenic rated)

### 9. Cryo Sensor Configuration

**Sensors**:
- Tank Pressure: 0-10 bar range, ±0.1% accuracy
- Tank Temperature: -260°C to +20°C, ±1°C accuracy
- Vacuum Pressure: 10^-6 to 1 mbar range
- Liquid Level: Capacitance-based, ±2% accuracy

**CI**: CI-10-CRYO-SENS-001 v1.0.0

## Ground Handling Procedures

### 10. Parking with H2 Fuel

**Procedure**: PROC-10-H2-PARK-001 v1.0.0

**Steps**:
1. Position aircraft in H2-rated parking spot
2. Activate H2 detection system
3. Verify safety zone clear
4. Connect ground monitoring (if available)
5. Post signage and barriers
6. Monitor tank pressure and boil-off
7. Maximum parking duration: 12 hours with fuel

### 11. H2 Tank Defueling for Storage

**Procedure**: PROC-10-H2-DEFUEL-001 v1.0.0

**Steps**:
1. Connect defueling equipment
2. Verify vent system operational
3. Transfer LH2 to ground storage
4. Purge tank with inert gas (GN2)
5. Verify < 100 ppm H2 concentration
6. Close and lock all valves
7. Tag "DEFUELED - SAFE FOR STORAGE"

### 12. Long-Term Storage (H2 Tank Preservation)

**Procedure**: PROC-10-H2-PRESERVE-001 v1.0.0

**Requirements**:
- Tank must be defueled and purged
- Vacuum insulation maintained
- Desiccant installed in vent lines
- Inspection every 30 days
- Temperature monitoring continuous

## Compatibility and Effectivity

### Aircraft Version Compatibility

| Aircraft Version | H2 System Baseline | Notes |
|------------------|-------------------|-------|
| v0.5.0-beta | H2BL v0.5.0 | Development testing |
| v1.0.0-EIS | H2BL v1.0.0 | Entry Into Service |

### Operator Effectivity

H2 System Baseline applies to:
- All H2-equipped aircraft (MSN: TBD)
- Airports with H2 infrastructure
- Operators with H2 handling certification

## Verification and Testing

### Ground Test Requirements

- **GT-H2-001**: H2 leak detection system functionality
- **GT-H2-002**: Vent system capacity and dispersion
- **GT-H2-003**: Emergency shutdown response time
- **GT-H2-004**: Cryo system thermal performance
- **GT-H2-005**: Parking procedure validation

Test Plan: `10-00-07_V_AND_V/H2-Ground-Test-Plan.md`

## Safety and Certification

### Safety Assessment

- **FHA**: Functional Hazard Assessment complete
- **PSSA**: Preliminary System Safety Assessment complete
- **FMEA**: Failure Modes and Effects Analysis in progress

Safety Document: `10-00-02_Safety/H2-Safety-Assessment.md`

### Hazards Addressed

- H-10-H2-001: H2 ignition during parking (Severity: Catastrophic)
- H-10-H2-002: Cryogenic exposure to personnel (Severity: Major)
- H-10-H2-003: Uncontrolled H2 release (Severity: Hazardous)
- H-10-H2-004: Cryo system vacuum loss (Severity: Minor)

### Certification Requirements

- **CS-25.1309**: H2 fuel system safety
- **CS-25.981**: Fuel tank explosion prevention (adapted for H2)
- **EASA SC-H2**: Special Condition for Hydrogen Fuel Systems (anticipated)

## Change Control

### Change Authority

- **Pre-H2BL Freeze**: H2 System Engineer + Safety Engineer approval
- **Post-H2BL Freeze**: CCB approval + Authority consultation

### Restricted Changes

The following require regulatory authority approval:
- H2 safety zone dimensions
- Vent system configuration
- Detection system alert levels
- Emergency procedures

## Known Limitations and Open Issues

### Open Issues

1. **H2-OI-001**: Vent dispersion modeling validation pending
2. **H2-OI-002**: Airport H2 infrastructure interface standards TBD
3. **H2-OI-003**: Long-term cryo performance data collection ongoing
4. **H2-OI-004**: H2 detection sensor placement optimization in progress

### Assumptions

- Airport H2 safety infrastructure available at EIS
- H2 fuel quality per ISO 14687
- Ground crew H2 training completed before EIS

## Standards and References

### H2 Standards
- **ISO 14687**: Hydrogen fuel quality
- **SAE J2719**: Hydrogen fuel quality for fuel cell vehicles
- **NFPA 2**: Hydrogen Technologies Code
- **ISO/TS 19880-1**: Gaseous hydrogen fueling stations

### Cryogenic Standards
- **ASME BPVC Section VIII**: Pressure vessels
- **ISO 21013**: Cryogenic vessels
- **NFPA 55**: Compressed Gases and Cryogenic Fluids

### Aviation Standards
- **CS-25**: Certification Specifications for Large Aeroplanes
- **SAE ARP4754A**: Development of Civil Aircraft
- **DO-178C**: Software (for H2 monitoring systems)

## Related Documents

- 10-00-11-10A: Functional Baseline
- 10-00-11-11A: Allocated Baseline
- 10-00-11-12A: Product Baseline
- 10-00-11-14A: BWB Config Baseline
- 10-00-11-43A: H2 System CI
- 10-00-11-44A: Cryo System CI
- 10-00-11-62A: H2 System Change History

## Document Control

- **Author**: AMPEL360 H2 Systems Engineering Team
- **Reviewer**: [To be assigned]
- **Approver**: [To be assigned]
- **Next Review**: At TRR
- **Revision History**:
  - Rev A (v1.0.0) - 2025-12-11 - Initial H2 System Baseline for CDR

---

**END OF DOCUMENT**
