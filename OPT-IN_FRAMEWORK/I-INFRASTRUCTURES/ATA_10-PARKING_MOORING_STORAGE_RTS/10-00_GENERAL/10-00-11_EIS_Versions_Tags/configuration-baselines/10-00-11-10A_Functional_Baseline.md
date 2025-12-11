# 10-00-11-10A: Functional Baseline

## Document Information
- **Document ID**: 10-00-11-10A
- **Title**: Functional Baseline (FBL)
- **Version**: 1.0.0
- **Date**: 2025-12-11
- **Status**: DRAFT
- **Document Type**: baseline
- **Baseline Type**: FBL
- **Milestone**: PDR

## Purpose

This document establishes the Functional Baseline (FBL) for the AMPEL360-BWB-H2 aircraft ATA 10 (Parking, Mooring, Storage & RTS) systems. The FBL captures the agreed-upon system requirements and functional specifications at the Preliminary Design Review (PDR) milestone.

## Scope

The Functional Baseline covers:
- System-level requirements for parking, mooring, and storage
- Functional requirements for ground handling
- H2 system functional requirements for ground operations
- BWB-specific functional requirements
- Interface requirements with ground support equipment
- Safety functional requirements

## Baseline Establishment

### Baseline Criteria

The FBL is considered established when:
- All system requirements are defined and approved
- Requirements traceability to stakeholder needs is complete
- Preliminary safety assessment is approved
- PDR is successfully completed
- CCB approves baseline freeze

### Baseline Date

- **Target PDR Date**: TBD
- **FBL Freeze Date**: TBD
- **CCB Approval**: [Pending]

## Functional Requirements Summary

### 1. Parking System Requirements

**REQ-10-PARK-F-001**: The system SHALL provide safe parking positions for BWB aircraft configuration.

**REQ-10-PARK-F-002**: The system SHALL accommodate H2-fueled aircraft with appropriate clearance zones.

**REQ-10-PARK-F-003**: The system SHALL support parking durations from 30 minutes to 72 hours.

**REQ-10-PARK-F-004**: The system SHALL provide parking position marking compatible with BWB wingspan.

**REQ-10-PARK-F-005**: The system SHALL integrate with airport ground control systems.

### 2. Mooring System Requirements

**REQ-10-MOOR-F-001**: The system SHALL provide mooring capability for wind speeds up to 65 knots.

**REQ-10-MOOR-F-002**: The system SHALL accommodate BWB structural attachment points.

**REQ-10-MOOR-F-003**: The system SHALL support both nose and wing mooring configurations.

**REQ-10-MOOR-F-004**: The system SHALL be compatible with standard tiedown equipment.

### 3. Storage System Requirements

**REQ-10-STOR-F-001**: The system SHALL support long-term storage (> 30 days).

**REQ-10-STOR-F-002**: The system SHALL provide H2 tank preservation procedures.

**REQ-10-STOR-F-003**: The system SHALL maintain cryogenic system integrity during storage.

**REQ-10-STOR-F-004**: The system SHALL include environmental protection for BWB surfaces.

### 4. H2 System Ground Operational Requirements

**REQ-10-H2-F-001**: The system SHALL provide safe H2 venting during ground operations.

**REQ-10-H2-F-002**: The system SHALL monitor H2 concentration in parking/storage areas.

**REQ-10-H2-F-003**: The system SHALL maintain minimum separation distances from ignition sources.

**REQ-10-H2-F-004**: The system SHALL integrate with airport H2 safety systems.

**REQ-10-H2-F-005**: The system SHALL support H2 tank pressure management during extended parking.

### 5. BWB-Specific Requirements

**REQ-10-BWB-F-001**: The system SHALL accommodate BWB wing clearance requirements.

**REQ-10-BWB-F-002**: The system SHALL provide ground handling points accessible for BWB configuration.

**REQ-10-BWB-F-003**: The system SHALL support BWB center-of-gravity positioning during parking.

### 6. Safety Functional Requirements

**REQ-10-SAFE-F-001**: The system SHALL prevent unauthorized aircraft movement when parked.

**REQ-10-SAFE-F-002**: The system SHALL provide emergency shutdown capability for H2 systems.

**REQ-10-SAFE-F-003**: The system SHALL alert personnel of H2 hazard zones.

**REQ-10-SAFE-F-004**: The system SHALL support fail-safe mooring under structural failure.

## Requirements Traceability

All functional requirements trace to:
- **Stakeholder Needs**: Operator requirements, regulatory requirements
- **System Specifications**: ATA 10 system specifications
- **Safety Requirements**: Safety assessment findings
- **H2 Requirements**: H2 safety standards and regulations
- **BWB Requirements**: BWB design constraints

Traceability matrix maintained in: `10-90_Tables_Schemas_Diagrams/requirements-traceability.csv`

## Baseline Configuration Items

The following Configuration Items are included in FBL:

| CI ID | Description | Version | Status |
|-------|-------------|---------|--------|
| CI-10-PARK-001 | Parking Position System | 0.1.0 | Defined |
| CI-10-MOOR-001 | Mooring System | 0.1.0 | Defined |
| CI-10-STOR-001 | Storage System | 0.1.0 | Defined |
| CI-10-H2-001 | H2 Ground Safety System | 0.1.0 | Defined |
| CI-10-BWB-001 | BWB Ground Handling System | 0.1.0 | Defined |

## Interface Baseline

### External Interfaces

- **ATA 02**: Flight Operations (parking procedures)
- **ATA 21**: Air Conditioning (H2 vent integration)
- **ATA 28**: Fuel System (H2 tank interfaces)
- **Ground Systems**: Airport ground control, H2 safety systems

Interface Control Documents (ICDs) baseline:
- ICD-10-ATA02: v0.1.0
- ICD-10-ATA21: v0.1.0
- ICD-10-ATA28: v0.1.0
- ICD-10-GROUND: v0.1.0

## Safety Baseline

### Preliminary Hazard Analysis (PHA)

PHA completed with findings:
- H-10-001: H2 ignition during parking (Severity: Catastrophic)
- H-10-002: BWB structural damage from mooring (Severity: Hazardous)
- H-10-003: Cryogenic exposure during maintenance (Severity: Major)

Safety assessment document: `10-00-02_Safety/PHA-ATA10-Rev0.md`

### Safety Requirements

All safety functional requirements identified and baselined.

## Verification Approach

Verification methods for functional requirements:

| Method | Description | Count |
|--------|-------------|-------|
| Analysis | Mathematical/logical analysis | 8 |
| Test | Physical testing | 12 |
| Inspection | Visual/physical inspection | 6 |
| Demonstration | Operational demonstration | 4 |

Verification Plan: `10-00-07_V_AND_V/Verification-Plan-FBL.md`

## Baseline Change Control

### Change Authority

- **Pre-FBL Freeze**: System Engineer approval
- **Post-FBL Freeze**: CCB approval required

### Change Impact Assessment

All changes after FBL freeze require:
- Requirements impact analysis
- Safety impact assessment
- Interface impact review
- Schedule and cost impact

### Emergency Changes

Emergency changes for safety issues:
- Immediate implementation permitted
- Post-implementation CCB review within 5 working days
- Documentation update within 10 working days

## H2 System Baseline Notes

H2 system functional requirements are preliminary and subject to:
- Detailed safety analysis completion
- Regulatory authority consultation
- H2 infrastructure availability assessment

H2 baseline will be further refined at CDR with separate H2 System Baseline (10-00-11-13A).

## BWB Configuration Baseline Notes

BWB-specific requirements based on:
- BWB preliminary design (Wing-body blend configuration)
- Ground clearance analysis
- Center-of-gravity envelope

BWB baseline will be refined at CDR with separate BWB Configuration Baseline (10-00-11-14A).

## Assumptions and Constraints

### Assumptions
- Airport H2 infrastructure available at EIS
- BWB configuration finalized before CDR
- Ground support equipment compatible with BWB

### Constraints
- H2 safety zone: Minimum 25m from ignition sources
- BWB wingspan: Maximum 80m
- Parking duration with active H2: Maximum 12 hours

## References

### Standards
- **CS-25**: Certification Specifications for Large Aeroplanes
- **SAE ARP4754A**: Development of Civil Aircraft and Systems
- **ISO 14687**: Hydrogen fuel quality
- **NFPA 2**: Hydrogen Technologies Code

### Related Documents
- 10-00-03_Requirements: System Requirements Specification
- 10-00-02_Safety: Preliminary Safety Assessment
- 10-00-11-11A: Allocated Baseline
- 10-00-11-13A: H2 System Baseline
- 10-00-11-14A: BWB Config Baseline

## Approval Record

- **Prepared By**: [System Engineering]
- **Technical Review**: [Pending]
- **Safety Review**: [Pending]
- **CCB Approval**: [Pending]
- **PDR Approval**: [Pending]

## Document Control

- **Author**: AMPEL360 Systems Engineering Team
- **Reviewer**: [To be assigned]
- **Approver**: [To be assigned]
- **Next Review**: At CDR
- **Revision History**:
  - Rev A (v1.0.0) - 2025-12-11 - Initial FBL document for PDR

---

**END OF DOCUMENT**
