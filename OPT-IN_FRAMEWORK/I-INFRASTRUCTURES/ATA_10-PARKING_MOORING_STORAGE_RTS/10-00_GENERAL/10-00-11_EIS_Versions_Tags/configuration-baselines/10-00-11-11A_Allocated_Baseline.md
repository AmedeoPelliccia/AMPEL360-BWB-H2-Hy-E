# 10-00-11-11A: Allocated Baseline

## Document Information
- **Document ID**: 10-00-11-11A
- **Title**: Allocated Baseline (ABL)
- **Version**: 1.0.0
- **Date**: 2025-12-11
- **Status**: DRAFT
- **Document Type**: baseline
- **Baseline Type**: ABL
- **Milestone**: CDR

## Purpose

This document establishes the Allocated Baseline (ABL) for the AMPEL360-BWB-H2 aircraft ATA 10 systems at the Critical Design Review (CDR) milestone. The ABL represents the approved detailed design configuration with all requirements allocated to design components and subsystems.

## Scope

The Allocated Baseline covers:
- Detailed design specifications for parking, mooring, and storage systems
- Component-level requirements allocation
- Interface specifications (internal and external)
- H2 system detailed design
- BWB configuration detailed design
- Design verification procedures

## Baseline Establishment

### Baseline Criteria

The ABL is established when:
- All detailed design documents are complete and approved
- Requirements are allocated to all design components
- Interface Control Documents (ICDs) are baselined
- Design Failure Mode and Effects Analysis (DFMEA) is complete
- CDR is successfully completed
- H2 and BWB detailed designs are approved
- CCB approves baseline freeze

### Baseline Date

- **Target CDR Date**: TBD (Month 42)
- **ABL Freeze Date**: TBD
- **CCB Approval**: [Pending]

## Design Architecture

### System Architecture

The ATA 10 system architecture consists of:

1. **Parking Position System**
   - Position marking subsystem
   - Clearance monitoring subsystem
   - BWB-specific guidance subsystem

2. **Mooring System**
   - Tiedown attachment subsystem
   - Load distribution subsystem
   - BWB structural interface subsystem

3. **Storage System**
   - Long-term preservation subsystem
   - H2 tank management subsystem
   - Environmental protection subsystem

4. **H2 Ground Safety System**
   - H2 detection and monitoring subsystem
   - Vent and dispersion subsystem
   - Emergency response subsystem

### Component Allocation

All FBL requirements are allocated to specific components and subsystems as documented in the design specifications.

## Configuration Items (Detailed)

| CI ID | Description | Version | Design Doc | Status |
|-------|-------------|---------|------------|--------|
| CI-10-PARK-001 | Parking Position System | 0.5.0 | DESIGN-10-PARK-001 | Detailed Design |
| CI-10-PARK-002 | BWB Clearance Monitoring | 0.5.0 | DESIGN-10-BWB-001 | Detailed Design |
| CI-10-MOOR-001 | Mooring System | 0.5.0 | DESIGN-10-MOOR-001 | Detailed Design |
| CI-10-MOOR-002 | BWB Tiedown Interface | 0.5.0 | DESIGN-10-BWB-002 | Detailed Design |
| CI-10-STOR-001 | Storage System | 0.5.0 | DESIGN-10-STOR-001 | Detailed Design |
| CI-10-H2-001 | H2 Ground Safety System | 0.5.0 | DESIGN-10-H2-001 | Detailed Design |
| CI-10-H2-002 | H2 Detection System | 0.5.0 | DESIGN-10-H2-002 | Detailed Design |
| CI-10-H2-003 | H2 Vent System | 0.5.0 | DESIGN-10-H2-003 | Detailed Design |
| CI-10-CRYO-001 | Cryo Management System | 0.5.0 | DESIGN-10-CRYO-001 | Detailed Design |

## Interface Baseline

### Internal Interfaces

- **PARK ↔ MOOR**: Position coordination interface
- **H2 ↔ CRYO**: Thermal management interface
- **H2 ↔ VENT**: Pressure management interface

### External Interfaces (Baselined ICDs)

| Interface | ICD Document | Version | Status |
|-----------|--------------|---------|--------|
| ATA 02 - Operations | ICD-10-ATA02 | v0.5.0 | Baselined |
| ATA 21 - Environmental | ICD-10-ATA21 | v0.5.0 | Baselined |
| ATA 28 - Fuel System | ICD-10-ATA28 | v0.5.0 | Baselined |
| Ground Control | ICD-10-GROUND | v0.5.0 | Baselined |
| H2 Infrastructure | ICD-10-H2-INFRA | v0.5.0 | Baselined |

## Requirements Allocation Summary

- **Total Requirements from FBL**: TBD
- **Allocated to Design**: TBD (100% target)
- **Derived Requirements**: TBD
- **Interface Requirements**: TBD

Allocation traceability: `10-90_Tables_Schemas_Diagrams/requirements-allocation.csv`

## Design Verification

### Verification Methods by Component

| Component | Analysis | Test | Inspection | Demo | Total |
|-----------|----------|------|------------|------|-------|
| Parking System | 3 | 5 | 2 | 1 | 11 |
| Mooring System | 4 | 6 | 3 | 2 | 15 |
| Storage System | 2 | 4 | 3 | 1 | 10 |
| H2 Safety System | 5 | 8 | 2 | 3 | 18 |
| BWB Interface | 3 | 4 | 2 | 1 | 10 |

Design Verification Plan: `10-00-07_V_AND_V/Design-Verification-Plan-ABL.md`

## Safety Assessment Update

### Design Failure Modes

DFMEA completed with findings:
- **DFMEA-10-001**: Parking position sensor failure
- **DFMEA-10-002**: Mooring attachment point failure
- **DFMEA-10-003**: H2 detector failure (single point)
- **DFMEA-10-004**: Cryo insulation degradation

Mitigation incorporated into design.

### Safety Requirements Allocation

All safety requirements from FBL allocated to design components with mitigation measures.

Safety Document: `10-00-02_Safety/Design-Safety-Assessment-ABL.md`

## H2 System Detailed Design

See dedicated H2 System Baseline: 10-00-11-13A

**Key H2 Design Elements**:
- LH2 tank interface design
- H2 vent system detailed design (flow rates, dispersion)
- H2 detection system placement and coverage
- Emergency shutdown system design
- Safety zone implementation design

## BWB Configuration Detailed Design

See dedicated BWB Configuration Baseline: 10-00-11-14A

**Key BWB Design Elements**:
- Ground handling point locations and load paths
- Clearance monitoring sensor placement
- Parking position marking for wide wingspan
- Tiedown attachment design for BWB structure

## Manufacturing Considerations

### Design for Manufacturing (DFM)

- Component standardization where possible
- Ease of assembly and installation
- Special tooling requirements identified
- H2-compatible materials specified
- BWB-specific manufacturing constraints addressed

### Supplier Baseline

Key suppliers selected and baselined:
- Parking system sensors: [Supplier TBD]
- Mooring equipment: [Supplier TBD]
- H2 detection sensors: [Supplier TBD]
- Cryo insulation: [Supplier TBD]

## Change Control

### Change Authority

- **Pre-ABL Freeze**: Design Engineer + System Engineer approval
- **Post-ABL Freeze**: CCB approval required

### Change Impact Types

Changes assessed for impact on:
- Requirements allocation
- Interface compatibility
- Safety assessment
- Verification plan
- Manufacturing
- H2 certification
- BWB certification

## Known Issues and Risks

### Open Design Issues

1. **ABL-OI-001**: H2 vent dispersion analysis refinement ongoing
2. **ABL-OI-002**: BWB ground handling point load verification pending
3. **ABL-OI-003**: Cryo system thermal performance margin analysis in progress
4. **ABL-OI-004**: Parking sensor redundancy architecture under review

### Design Risks

| Risk ID | Description | Severity | Mitigation |
|---------|-------------|----------|------------|
| ABL-R-001 | H2 sensor placement optimization | Medium | Additional CFD analysis |
| ABL-R-002 | BWB mooring load concentration | Medium | FEA validation testing |
| ABL-R-003 | Cryo insulation long-term degradation | Low | Material testing program |

## Standards Compliance

Design complies with:
- **CS-25**: Large Aircraft Certification Specifications
- **SAE ARP4754A**: Development of Civil Aircraft
- **ISO 14687**: Hydrogen fuel quality
- **NFPA 2**: Hydrogen Technologies Code
- **ASME BPVC**: Pressure Vessels (for cryo systems)

## Related Documents

- 10-00-11-10A: Functional Baseline (predecessor)
- 10-00-11-12A: Product Baseline (successor)
- 10-00-11-13A: H2 System Baseline
- 10-00-11-14A: BWB Config Baseline
- 10-00-11-22A: CDR Baseline (milestone snapshot)
- Design Specifications (various DESIGN-10-XXX documents)

## Approval Record

- **Prepared By**: [System Engineering]
- **Design Review**: [Pending]
- **Safety Review**: [Pending]
- **CCB Approval**: [Pending]
- **CDR Approval**: [Pending]

## Document Control

- **Author**: AMPEL360 Systems Engineering Team
- **Reviewer**: [To be assigned]
- **Approver**: [To be assigned]
- **Next Review**: At TRR
- **Revision History**:
  - Rev A (v1.0.0) - 2025-12-11 - Initial ABL document for CDR

---

**END OF DOCUMENT**
