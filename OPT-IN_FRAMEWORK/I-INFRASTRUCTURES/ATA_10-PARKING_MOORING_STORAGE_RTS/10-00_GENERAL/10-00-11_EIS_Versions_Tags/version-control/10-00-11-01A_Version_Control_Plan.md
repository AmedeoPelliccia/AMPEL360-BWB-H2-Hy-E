# 10-00-11-01A: Version Control Plan

## Document Information
- **Document ID**: 10-00-11-01A
- **Title**: Version Control Plan
- **Version**: 1.0.0
- **Date**: 2025-12-11
- **Status**: DRAFT
- **Document Type**: version-plan

## Purpose

This document defines the version control plan for the AMPEL360-BWB-H2 aircraft Entry Into Service (EIS) program, establishing the framework for managing versions, baselines, and configurations throughout the aircraft development lifecycle.

## Scope

This plan covers:
- Version control methodology for all EIS-related documentation and artifacts
- Baseline management approach for aircraft configurations
- Configuration control processes for H2 and BWB-specific systems
- Change management procedures
- Traceability requirements

## Version Control Framework

### 1. Version Numbering Scheme

The program adopts **Semantic Versioning 2.0.0** (MAJOR.MINOR.PATCH) for all versioned items:

- **MAJOR**: Incompatible changes, major configuration updates, certification milestones
- **MINOR**: Backward-compatible functionality additions, design updates
- **PATCH**: Backward-compatible bug fixes, documentation corrections

**Format**: `MAJOR.MINOR.PATCH[-prerelease][+build]`

**Examples**:
- `0.1.0-alpha` - Alpha release
- `0.5.0-beta` - Beta release
- `1.0.0` - EIS release
- `1.1.0` - Post-EIS with new features
- `1.0.1` - Post-EIS with fixes

### 2. Document Version Scheme

All documents follow the pattern: `10-00-11-NNA_DESCRIPTION.md`

- `10` = ATA Chapter (Parking, Mooring, Storage & RTS)
- `00` = Section (GENERAL)
- `11` = Subsection (EIS_Versions_Tags)
- `NN` = Sequential number (01-99)
- `A` = Revision letter (A, B, C, ...)
- `DESCRIPTION` = Descriptive title in PascalCase

### 3. Baseline Types

The program maintains the following baseline types:

| Baseline | Acronym | Description | Milestone |
|----------|---------|-------------|-----------|
| Functional Baseline | FBL | System requirements baseline | PDR |
| Allocated Baseline | ABL | Design requirements baseline | CDR |
| Product Baseline | PBL | Production configuration baseline | TRR |
| H2 System Baseline | H2BL | H2-specific configuration | CDR/TRR |
| BWB Configuration Baseline | BWBBL | BWB-specific configuration | CDR/TRR |
| EIS Baseline | EISBL | Entry Into Service baseline | EIS |

## Configuration Management Approach

### 1. Configuration Items (CI)

All configuration items are:
- Uniquely identified with CI numbers
- Version controlled
- Tracked for effectivity (MSN, operator)
- Baselined at appropriate milestones

**CI Naming Convention**: `CI-10-[SUBSYSTEM]-[NUMBER]`

Example: `CI-10-PARK-001` (Parking System Configuration Item 001)

### 2. Change Control Process

1. **Change Request Initiation**
   - Stakeholder submits change request
   - Impact assessment performed
   - Classification (MAJOR/MINOR/PATCH)

2. **Change Review**
   - Technical review
   - Safety assessment
   - Certification impact analysis
   - H2/BWB specific considerations

3. **Change Approval**
   - Configuration Control Board (CCB) approval
   - Documentation updates
   - Version increment

4. **Implementation**
   - Changes implemented
   - Testing/verification
   - Baseline update

5. **Release**
   - Release notes generated
   - Stakeholder notification
   - Archive previous version

### 3. Baseline Management

**Baseline Establishment**:
- Baselines are established at key milestones (PDR, CDR, TRR, FAI, EIS)
- All CIs are frozen at baseline
- Changes require formal CCB approval

**Baseline Updates**:
- Emergency changes (safety-critical)
- Approved change packages
- Version increments follow semantic versioning

## Tool and Repository Strategy

### Primary Repository
- Git-based version control
- GitHub repository: `AmedeoPelliccia/AMPEL360-BWB-H2-Hy-E`
- Branch strategy: GitFlow (main, develop, feature, release, hotfix)

### Tagging Strategy
- Tags mark official releases and baselines
- Format: `v[VERSION]-[MILESTONE]`
- Examples: `v0.1.0-alpha`, `v1.0.0-EIS`, `v1.0.0-PDR-baseline`

### Documentation Management
- All documentation in Markdown (`.md`)
- Configuration data in CSV (`.csv`)
- Schemas in JSON Schema (`.schema.json`)
- Diagrams in SVG (`.svg`)

## H2 and BWB Specific Considerations

### H2 System Version Control
- H2 safety systems maintained in separate baseline (H2BL)
- Cryo system configurations tracked independently
- H2 vent and detection systems require separate approval
- Version compatibility matrix with aircraft versions

### BWB Configuration Version Control
- BWB structural configurations in separate baseline (BWBBL)
- Ground handling configurations tracked
- Clearance requirements versioned
- BWB-specific equipment compatibility tracked

## Traceability Requirements

All versioned items maintain traceability to:
- **Requirements**: System and subsystem requirements
- **Design**: Design documents and specifications
- **Tests**: Verification and validation artifacts
- **Certifications**: Certification artifacts and evidence
- **Changes**: Change requests and approvals

Traceability matrices are maintained in CSV format and updated with each baseline.

## Roles and Responsibilities

| Role | Responsibility |
|------|----------------|
| Configuration Manager | Overall CM process, baseline management |
| Document Controller | Document versioning, release management |
| CCB Chair | Change approval authority |
| System Engineers | Technical content, impact assessment |
| Safety Engineer | Safety assessment of changes |
| Certification Engineer | Certification impact analysis |

## Metrics and Reporting

Key metrics tracked:
- Number of baselines established
- Change requests processed per baseline
- Version release frequency
- Configuration item count
- Effectivity coverage

Reports generated:
- Monthly version status report
- Baseline status at each milestone
- Change summary reports
- Configuration audit reports

## Standards and References

This plan complies with:
- **ATA iSpec 2200**: Configuration Management
- **CM2**: Configuration Management Standards
- **Semantic Versioning 2.0.0**: https://semver.org/
- **SAE ARP4754A**: Development of Civil Aircraft and Systems
- **EASA Part 21**: Certification Procedures for Aircraft and Related Products
- **S1000D**: International Specification for Technical Publications

## Review and Update

This plan is reviewed:
- At each major milestone (PDR, CDR, TRR, FAI, EIS)
- Annually post-EIS
- When significant process changes occur

## Document Control

- **Author**: AMPEL360 Configuration Management Team
- **Reviewer**: [To be assigned]
- **Approver**: [To be assigned]
- **Next Review**: 2026-03-11
- **Revision History**:
  - Rev A (v1.0.0) - 2025-12-11 - Initial release

---

**END OF DOCUMENT**
