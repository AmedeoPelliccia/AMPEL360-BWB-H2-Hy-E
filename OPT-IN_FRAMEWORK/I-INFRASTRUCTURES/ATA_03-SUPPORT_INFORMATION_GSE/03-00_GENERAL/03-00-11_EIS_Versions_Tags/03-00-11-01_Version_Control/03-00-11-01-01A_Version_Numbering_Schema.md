# 03-00-11-01-01A - Version Numbering Schema

## 1. Purpose

This document defines the version numbering schema for AMPEL360 BWB-H2-Hy-E aircraft and associated systems, ensuring consistent version identification throughout the product lifecycle from initial development through Entry Into Service (EIS) and beyond.

## 2. Scope

This specification covers:
- Semantic versioning principles for aircraft systems
- Version number structure and interpretation
- Version increment rules and triggers
- Integration with configuration management systems
- Applicability to hardware, software, and documentation

## 3. Applicable Documents

- **ATA 03-00-06**: Engineering
- **ATA 03-00-10**: Certification
- **Semantic Versioning 2.0.0** (https://semver.org/)
- **AS9100**: Quality Management Systems - Aerospace
- **MIL-HDBK-61A**: Configuration Management Guidance
- **ISO/IEC/IEEE 12207**: Systems and software engineering — Software life cycle processes

## 4. Description

### 4.1 Overview

The AMPEL360 project adopts a structured version numbering schema based on **Semantic Versioning** adapted for aerospace applications. The schema provides clear, unambiguous identification of configuration states and compatibility between systems.

### 4.2 Requirements

#### 4.2.1 Version Number Format

The standard version format is: **MAJOR.MINOR.PATCH[-LABEL]**

**Example:** `2.3.1-beta` or `1.0.0-EIS`

**Component Definitions:**

- **MAJOR**: Incremented for incompatible changes requiring recertification or major system modifications
- **MINOR**: Incremented for backward-compatible functionality additions or significant enhancements
- **PATCH**: Incremented for backward-compatible bug fixes, minor corrections, or documentation updates
- **LABEL** (optional): Pre-release or release status identifier (alpha, beta, RC, EIS, etc.)

#### 4.2.2 Version Increment Rules

| Change Type | MAJOR | MINOR | PATCH | Examples |
|-------------|-------|-------|-------|----------|
| Breaking change / Recertification required | +1 | Reset to 0 | Reset to 0 | Structural modification, new propulsion system |
| New feature / Compatible enhancement | - | +1 | Reset to 0 | Additional monitoring capability, improved algorithm |
| Bug fix / Minor correction | - | - | +1 | Documentation correction, software patch |

#### 4.2.3 Pre-Release Labels

Standard labels for development phases:

- **alpha**: Early development, internal testing
- **beta**: Feature-complete, under validation
- **RC** (Release Candidate): Final testing before release
- **PDR**: Post Preliminary Design Review
- **CDR**: Post Critical Design Review
- **EIS**: Entry Into Service baseline

### 4.3 Procedures

#### 4.3.1 Assigning Version Numbers

1. **Initial Version**: All new systems start at `0.1.0-alpha`
2. **Development Progression**: Increment MINOR and PATCH as features and fixes are added
3. **First Release**: Transition to `1.0.0` at EIS or initial operational capability
4. **Subsequent Updates**: Follow increment rules based on change impact

#### 4.3.2 Version Control Integration

- All version numbers must be tracked in the configuration management database
- Git tags must match official version numbers
- Version metadata must be embedded in:
  - Software builds
  - Hardware drawings
  - Documentation headers
  - System interface definitions

#### 4.3.3 Compatibility Assessment

When incrementing version numbers, assess:
- **Interface compatibility**: Can systems interact without modification?
- **Certification impact**: Is re-certification required?
- **Maintenance impact**: Can existing procedures be used?
- **Training impact**: Is operator/maintainer retraining required?

## 5. Version/Tag Registry

| Component | Current Version | Date | Description | Status |
|-----------|----------------|------|-------------|--------|
| BWB Airframe | 1.0.0-CDR | 2025-11-15 | Critical Design Review baseline | Active |
| H2 Propulsion System | 0.9.2-beta | 2025-12-01 | Pre-certification testing | In Development |
| Flight Control Software | 2.1.3 | 2025-10-20 | Post-EIS update with bug fixes | Released |
| Neural Network DPP | 1.0.0-EIS | 2025-09-15 | Entry Into Service version | Released |

## 6. Approval Requirements

- **Version Increment Proposal**: Prepared by System Engineer
- **Review**: Configuration Control Board (CCB)
- **Approval**: Chief Engineer or Program Manager
- **For MAJOR increments**: Additional approval from Certification Authority Representative

## 7. Cross-References

- **Related ATA Chapters**:
  - [ATA 03-00-06 Engineering](../../03-00-06_Engineering/)
  - [ATA 03-00-07 V&V](../../03-00-07_V_AND_V/)
  - [ATA 03-00-10 Certification](../../03-00-10_Certification/)
- **Parent Document**: [03-00-11_EIS_Versions_Tags](../)
- **Related Documents**:
  - [03-00-11-01-02A Version History Log](./03-00-11-01-02A_Version_History_Log.md)
  - [03-00-11-03-01A Tag Naming Convention](../03-00-11-03_Tagging_Standards/03-00-11-03-01A_Tag_Naming_Convention.md)

## 8. Revision History

| Rev | Date | Author | Description |
|-----|------|--------|-------------|
| A | 2025-12-07 | AMPEL360 Documentation WG | Initial release |

---

## Document Control

- **Generated with the assistance of AI (GitHub Copilot)**, prompted by **Amedeo Pelliccia**.
- **Status**: DRAFT – Subject to human review and approval.
- **Human approver**: _[to be completed]_.
- **Repository**: `AMPEL360-BWB-H2-Hy-E`
- **Last AI update**: 2025-12-07.

---
