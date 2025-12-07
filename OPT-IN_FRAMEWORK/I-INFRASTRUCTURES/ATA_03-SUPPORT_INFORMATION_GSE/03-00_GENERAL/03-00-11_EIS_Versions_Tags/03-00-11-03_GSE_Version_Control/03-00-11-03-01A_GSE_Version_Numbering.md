# 03-00-11-03-01A - GSE Version Numbering

## Document Information
- **Document ID**: 03-00-11-03-01A
- **Title**: GSE Version Numbering System
- **Version**: A
- **Status**: Draft
- **Last Updated**: 2025-12-07

## 1. Purpose

This document defines the version numbering system for Ground Support Equipment, establishing consistent methods for identifying and tracking GSE versions, modifications, and configurations throughout their lifecycle.

## 2. Scope

This document covers:
- Version numbering scheme and conventions
- Application to different GSE types
- Version change triggers and criteria
- Documentation and communication requirements
- Integration with configuration management

## 3. Applicable Documents

- [ISO 10007](https://www.iso.org/standard/70400.html) (Configuration Management)
- [IEEE 828](https://standards.ieee.org/standard/828-2012.html) (Configuration Management in Systems and Software Engineering)
- [ATA iSpec 2200](https://www.ataspec.org/) (Information Standards for Aviation Maintenance)
- Related: [03-00-11-03-02A GSE Configuration Baseline](./03-00-11-03-02A_GSE_Configuration_Baseline.md)
- Related: [03-00-11-03-03A GSE Change Control](./03-00-11-03-03A_GSE_Change_Control.md)

## 4. EIS/Versioning Requirements

### 4.1 Overview

A systematic version numbering scheme enables clear identification of GSE configuration state, tracking of changes over time, and communication of equipment capabilities and compatibility. The scheme must be scalable, intuitive, and integrated with configuration management processes.

**Version Numbering Principles:**
- Clear and unambiguous identification
- Hierarchical structure (major/minor/patch)
- Compatibility indication
- Change significance reflection
- Auditability and traceability

### 4.2 Version/Tag Specifications

| Parameter | Specification | Notes |
|-----------|---------------|-------|
| Numbering Scheme | Major.Minor.Patch | Semantic versioning adapted |
| Format | X.Y.Z | X, Y, Z are non-negative integers |
| Initial Version | 1.0.0 | First production release |
| Documentation Standard | Version control database | Centralized repository |

### 4.3 Tracking Methods

**Version Tracking:**
- Configuration management database
- Version history log
- Release documentation
- Fleet registry integration (ref: [03-00-11-05-01A](../03-00-11-05_GSE_Fleet_Management/03-00-11-05-01A_GSE_Fleet_Registry.md))
- Drawing and document control (ref: [03-00-11-08 Documentation Control](../03-00-11-08_GSE_Documentation_Control/))

## 5. Implementation Plan

### GSE Version Numbering Scheme

#### Format: MAJOR.MINOR.PATCH (X.Y.Z)

**MAJOR Version (X):**
- Incremented for significant design changes
- Not backward compatible with previous major versions
- Requires recertification or requalification
- Changes functional capabilities significantly

**Examples:**
- New propulsion system or major system redesign
- Change in safety certification level
- Incompatible interface changes
- Major capacity or capability change

**MINOR Version (Y):**
- Incremented for moderate enhancements or modifications
- Generally backward compatible
- May require operational procedure updates
- Adds or modifies functionality

**Examples:**
- New optional features or capabilities
- Performance improvements
- Enhanced monitoring or diagnostics
- Upgraded components (drop-in replacements)

**PATCH Version (Z):**
- Incremented for minor modifications and corrections
- Fully backward compatible
- No functional impact (or minimal)
- Bug fixes, corrections, minor improvements

**Examples:**
- Software bug fixes
- Documentation corrections
- Minor component replacements (like-for-like)
- Cosmetic or labeling changes

### Version Numbering Rules

#### Rule 1: Version Format
```
GSE-MODEL-X.Y.Z[-MODIFIER]

Where:
- GSE-MODEL = Equipment model designation (e.g., LH2-RF-001)
- X.Y.Z = Version numbers
- MODIFIER = Optional build or configuration identifier
```

**Examples:**
```
LH2-RF-001-1.0.0           (Initial release)
LH2-RF-001-1.1.0           (Minor enhancement)
LH2-RF-001-1.1.1           (Bug fix)
LH2-RF-001-2.0.0           (Major redesign)
LH2-RF-001-2.0.0-PROTO     (Prototype build)
```

#### Rule 2: Version Increment Triggers

**MAJOR (X) Increment When:**
- Fundamental design change
- Interface compatibility break
- Certification basis change
- Operational mode change (manual → automated)
- Capacity change >25%
- Safety classification change

**MINOR (Y) Increment When:**
- New feature or capability addition
- Significant component upgrade
- Performance enhancement >10%
- Operational procedure change
- Software/firmware major update
- Optional equipment addition

**PATCH (Z) Increment When:**
- Bug fix or correction
- Like-for-like component replacement
- Documentation update only
- Minor software/firmware update
- Cosmetic change
- Labeling or marking change

#### Rule 3: Version Reset Rules
- When X increments, Y and Z reset to 0 (e.g., 1.5.3 → 2.0.0)
- When Y increments, Z resets to 0 (e.g., 1.5.3 → 1.6.0)
- Z increments independently (e.g., 1.5.3 → 1.5.4)

#### Rule 4: Pre-Release Identifiers
For equipment in development or testing:

```
X.Y.Z-ALPHA    (Early development)
X.Y.Z-BETA     (Beta testing)
X.Y.Z-RC.N     (Release candidate, N = number)
X.Y.Z-PROTO    (Prototype)
X.Y.Z-TEST     (Test configuration)
```

**Examples:**
```
LH2-RF-001-2.0.0-ALPHA
LH2-RF-001-2.0.0-BETA
LH2-RF-001-2.0.0-RC.1
LH2-RF-001-2.0.0          (Final release)
```

### Application to Different GSE Types

#### Mobile Equipment (Vehicles, Tractors, Loaders)
- Version applied to complete vehicle assembly
- Sub-system versions tracked separately in BOM
- Major version change may require driver retraining

#### Static Equipment (Storage, Dispensing Systems)
- Version applied to complete system
- Modular components may have independent versions
- Site-specific configurations tracked separately

#### Software/Firmware
- Follows software versioning conventions
- Tracked independently but correlated with hardware version
- Compatibility matrix maintained

#### Tooling and Test Equipment
- Version applied to complete tool or test set
- Calibration separate from version control
- Verification and validation version-specific

### Version Documentation Requirements

#### Version Release Package
Each version release must include:

1. **Version Release Notes:**
   - Version number and date
   - Summary of changes from previous version
   - Known issues and limitations
   - Compatibility information
   - Migration/upgrade instructions (if applicable)

2. **Technical Documentation:**
   - Updated operation manuals (ref: [03-00-11-08-02A](../03-00-11-08_GSE_Documentation_Control/03-00-11-08-02A_GSE_Manual_Revisions.md))
   - Updated maintenance procedures
   - Updated drawings (ref: [03-00-11-08-03A](../03-00-11-08_GSE_Documentation_Control/03-00-11-08-03A_GSE_Drawing_Control.md))
   - Parts list / BOM
   - Software documentation (if applicable)

3. **Configuration Records:**
   - Configuration item list
   - Change request references
   - Verification/test results
   - Certification status

4. **Traceability:**
   - Change history (ref: [03-00-11-03-04A](./03-00-11-03-04A_GSE_Version_History.md))
   - Requirements traceability
   - Approval signatures
   - Effectivity planning

### Version Communication and Marking

#### Physical Marking
GSE equipment must be physically marked with:
- Model designation
- Version number (X.Y.Z)
- Serial number
- Date of manufacture
- Configuration baseline identifier

**Marking Location:**
- Primary data plate (permanent)
- Secondary locations as required
- Software/firmware version in diagnostics menu

#### Digital Identification
- Version recorded in fleet registry (ref: [03-00-11-05-01A](../03-00-11-05_GSE_Fleet_Management/03-00-11-05-01A_GSE_Fleet_Registry.md))
- RFID or QR code encoding (ref: [03-00-11-04 Tagging System](../03-00-11-04_GSE_Tagging_System/))
- Configuration management database
- Maintenance tracking system

### Version Compatibility Management

#### Compatibility Matrix
Maintain compatibility information:
- Aircraft interface compatibility
- Ground infrastructure compatibility
- Software/firmware compatibility
- Spare parts compatibility
- Training/qualification compatibility

#### Backward Compatibility
- Minor versions should maintain backward compatibility
- Incompatibilities documented and communicated
- Migration paths defined for major versions
- Obsolescence planning (ref: [03-00-11-06-03A](../03-00-11-06_GSE_Upgrade_Management/03-00-11-06-03A_GSE_Obsolescence_Management.md))

## 6. Cross-References

- **Related ATA Chapters**: 
  - ATA 03-10 (GSE Operations)
  - ATA 03-30 (GSE Maintenance)
- **Parent Document**: [03-00-11 EIS Versions Tags](../)
- **Related Version Control**: 
  - [03-00-11-03-02A GSE Configuration Baseline](./03-00-11-03-02A_GSE_Configuration_Baseline.md)
  - [03-00-11-03-03A GSE Change Control](./03-00-11-03-03A_GSE_Change_Control.md)
  - [03-00-11-03-04A GSE Version History](./03-00-11-03-04A_GSE_Version_History.md)
- **Fleet Management**: [03-00-11-05 GSE Fleet Management](../03-00-11-05_GSE_Fleet_Management/)
- **Documentation Control**: [03-00-11-08 GSE Documentation Control](../03-00-11-08_GSE_Documentation_Control/)

## 7. Revision History

| Rev | Date | Author | Description |
|-----|------|--------|-------------|
| A | 2025-12-07 | AMPEL360 Documentation WG | Initial release |

---

## Document Control

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT** – Subject to human review and approval.
- Human approver: _[to be completed]_.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: 2025-12-07.

---
