# 10-00-11-25A: EIS Baseline

## Document Information
- **Document ID**: 10-00-11-25A
- **Title**: EIS Baseline (Entry Into Service)
- **Version**: 1.0.0
- **Date**: 2025-12-11
- **Status**: DRAFT
- **Document Type**: baseline
- **Baseline Type**: EISBL
- **Milestone**: EIS
- **Aircraft Version**: v1.0.0

## Purpose

This document establishes the **Entry Into Service (EIS) Baseline** for the AMPEL360-BWB-H2 aircraft ATA 10 (Parking, Mooring, Storage & RTS) systems. The EIS Baseline represents the production configuration approved by the Type Certificate and marks the aircraft ready for commercial operation.

## Scope

The EIS Baseline encompasses:
- Final production configuration of all ATA 10 systems
- Type Certificate Data Sheet (TCDS) referenced configuration
- All approved configuration items for initial deliveries
- H2 system certified configuration
- BWB configuration certified design
- Approved operational procedures and limitations
- Service Bulletin baseline

## Baseline Establishment

### EIS Criteria

The EIS Baseline is established when:
- **Type Certificate issued** by EASA/FAA
- **Production Certificate issued** 
- All certification findings closed
- Flight testing successfully completed
- FAI (First Article Inspection) approved
- Initial operator training completed
- Approved Maintenance Program in place
- Flight Manual approved
- Minimum Essential Equipment List (MEL) approved
- **CCB approval** of EIS baseline freeze

### Milestone Dates

- **FAI Completion**: [Month 72 - TBD]
- **Type Certificate Issue**: [Month 78 - TBD]
- **EIS Date**: [Month 78 - TBD]
- **EIS Baseline Freeze**: [TBD]
- **First Delivery**: [TBD]

## Type Certificate Configuration

### TCDS Reference

- **Type Certificate Number**: [EASA.A.XXX or TBD]
- **TCDS Issue**: [Issue number]
- **TCDS Date**: [Date]
- **Applicant**: AMPEL360 Aircraft GmbH

### Model Designation

- **Model**: AMPEL360-BWB-H2
- **Variant**: [Production variant identifier]
- **Configuration**: BWB (Blended Wing Body) with LH2 fuel

## Production Configuration Items

### Baseline CI Register

All CIs at EIS baseline v1.0.0:

| CI ID | Description | Version | TCDS Ref | Notes |
|-------|-------------|---------|----------|-------|
| CI-10-PARK-001 | Parking Position System | 1.0.0 | ATA 10-10 | Production standard |
| CI-10-PARK-002 | BWB Clearance Monitoring | 1.0.0 | ATA 10-10 | BWB-specific |
| CI-10-MOOR-001 | Mooring System | 1.0.0 | ATA 10-20 | Production standard |
| CI-10-MOOR-002 | BWB Tiedown Interface | 1.0.0 | ATA 10-20 | BWB-specific |
| CI-10-STOR-001 | Storage System | 1.0.0 | ATA 10-30 | Production standard |
| CI-10-H2-001 | H2 Ground Safety System | 1.0.0 | ATA 10-40 | H2-equipped aircraft |
| CI-10-H2-002 | H2 Detection System | 1.0.0 | ATA 10-40 | H2-equipped aircraft |
| CI-10-H2-003 | H2 Vent System | 1.0.0 | ATA 10-40 | H2-equipped aircraft |
| CI-10-CRYO-001 | Cryo Management System | 1.0.0 | ATA 10-40 | H2-equipped aircraft |
| CI-10-CRYO-002 | Cryo Valve Assembly | 1.0.0 | ATA 10-40 | H2-equipped aircraft |
| CI-10-BWB-001 | BWB Ground Handling System | 1.0.0 | ATA 10-50 | BWB-specific |

Complete CI Register: `10-00-11-40A_CI_Register.md`

## H2 System EIS Configuration

### H2 Certified Configuration

**LH2 Fuel System** (per 10-00-11-13A H2 System Baseline v1.0.0):
- Tank capacity: [TBD] liters LH2
- Operating pressure: [TBD] bar
- Operating temperature: -253°C
- Vent system: Certified per CS-25.XXX (Special Condition)
- Detection system: Triple redundant, certified per CS-25.1309

**Safety Zones** (Certified):
- Zone 1 (Exclusion): 5m radius from vent
- Zone 2 (Restricted): 15m radius
- Zone 3 (Controlled): 25m radius

**Operational Limitations**:
- Maximum parking duration with LH2: 12 hours
- Minimum separation from ignition sources: 25m
- H2 concentration alert levels: 1%, 2%, 4%
- Ground crew H2 certification required

## BWB Configuration EIS

### BWB Certified Design

**BWB Configuration** (per 10-00-11-14A BWB Config Baseline v1.0.0):
- Wingspan: [TBD] meters
- Parking position width: [TBD] meters
- Ground handling points: [Number] locations
- Clearance requirements: Documented in AFM
- Center-of-gravity range: [TBD]

**BWB-Specific Equipment**:
- Wing clearance monitoring system
- Ground handling guidance system
- Special tiedown equipment for BWB structure

## Approved Operational Procedures

### Standard Procedures (Certified)

- **PROC-10-PARK-001 v1.0.0**: Standard Parking Procedure
- **PROC-10-MOOR-001 v1.0.0**: Mooring Procedure
- **PROC-10-STOR-001 v1.0.0**: Long-Term Storage Procedure
- **PROC-10-H2-PARK-001 v1.0.0**: Parking with H2 Fuel
- **PROC-10-H2-DEFUEL-001 v1.0.0**: H2 Defueling for Storage
- **PROC-10-H2-PRESERVE-001 v1.0.0**: H2 Tank Preservation
- **PROC-10-BWB-PARK-001 v1.0.0**: BWB Parking Procedure

All procedures approved in Aircraft Flight Manual (AFM) and Maintenance Manual (AMM).

## Effectivity

### Initial Effectivity

**MSN Effectivity**: MSN-001 and subsequent (all production aircraft)

**H2 Configuration**: 
- Standard for all AMPEL360-BWB-H2 aircraft
- Retrofit package not available (factory installation only)

**BWB Configuration**:
- Standard for all AMPEL360-BWB-H2 aircraft
- No conventional configuration variant

### Operator Effectivity

Approved for operation by:
- Operators with H2 handling certification
- Airports with H2 ground infrastructure
- Ground crew with H2 safety training

## Certification Evidence

### Compliance Demonstration

All ATA 10 requirements demonstrated compliant with:
- **CS-25**: Large Aeroplane Certification Specifications
- **CS-25.XXX (SC-H2)**: Special Condition for Hydrogen Fuel Systems
- **CS-25.XXX (SC-BWB)**: Special Condition for BWB Configuration

### Test Evidence

- Ground tests: Complete (all pass)
- Flight tests: Complete (all pass)
- Safety testing: Complete (all hazards mitigated)
- H2 system tests: Complete (certified)
- BWB handling tests: Complete (certified)

Evidence Package: `10-00-10_Certification/Certification-Evidence-Package.md`

## Service Bulletin Baseline

### Initial Service Bulletins at EIS

| SB Number | Description | Compliance | Effectivity |
|-----------|-------------|------------|-------------|
| SB-10-001 | [TBD] | Optional | All MSN |
| [Others TBD] | | | |

Service Bulletins tracked in: `10-00-12_Services/Service-Bulletin-Register.md`

## Known Limitations

### Operational Limitations

1. **H2 Parking**: Maximum 12 hours with fuel on board
2. **H2 Infrastructure**: Requires airport H2 capability
3. **BWB Parking**: Requires wide parking positions (>Xm width)
4. **Ground Crew**: H2 training certification mandatory

### Environmental Limitations

- Maximum wind for mooring: 65 knots
- Temperature range for LH2 operations: [TBD to TBD]°C
- Altitude limitations: Per AFM

All limitations documented in Aircraft Flight Manual.

## Post-EIS Change Control

### Change Authority

- **All changes** require CCB approval
- **Safety-related changes** require authority coordination
- **Service Bulletins** follow SB process
- **Airworthiness Directives** mandatory compliance

### Version Progression Post-EIS

- **v1.0.x**: Bug fixes, corrections (PATCH)
- **v1.x.0**: Enhancements, improvements (MINOR)
- **v2.0.0+**: Major changes, certification amendments (MAJOR)

## Standards and References

### Certification Standards

- **CS-25**: EASA Certification Specifications for Large Aeroplanes
- **Part 25**: FAA Airworthiness Standards
- **CS-25.XXX (SC-H2)**: Special Condition - Hydrogen Fuel Systems
- **CS-25.XXX (SC-BWB)**: Special Condition - Blended Wing Body

### Configuration Management

- **ATA iSpec 2200**: Configuration Management
- **S1000D**: Technical Publications
- **ATA 10**: Parking, Mooring, Storage, and Return to Service

### Related Baselines

- 10-00-11-10A: Functional Baseline (FBL)
- 10-00-11-11A: Allocated Baseline (ABL)
- 10-00-11-12A: Product Baseline (PBL)
- 10-00-11-13A: H2 System Baseline (H2BL)
- 10-00-11-14A: BWB Config Baseline (BWBBL)
- 10-00-11-24A: FAI Baseline

### Release Documentation

- 10-00-11-33A: v1.0.0 EIS Release
- 10-00-11-60A: Master Change Log

## Approval Record

- **Type Certificate**: [EASA.A.XXX - Pending]
- **Production Certificate**: [PC-XXX - Pending]
- **CCB Approval**: [Pending]
- **EIS Approval**: [Pending]
- **First Delivery Authorization**: [Pending]

## Document Control

- **Author**: AMPEL360 Certification Team
- **Reviewer**: [To be assigned]
- **Approver**: Head of Certification
- **Next Review**: Annually post-EIS
- **Revision History**:
  - Rev A (v1.0.0) - 2025-12-11 - Initial EIS Baseline document

---

**END OF DOCUMENT**
