# 10-00-11_EIS_Versions_Tags

## Purpose

This directory manages **Entry Into Service (EIS) versions, configuration baselines, and change control** for the AMPEL360-BWB-H2 aircraft ATA 10 (Parking, Mooring, Storage & RTS) systems. It provides comprehensive version management, baseline control, and configuration management throughout the aircraft development lifecycle from concept through EIS and post-delivery support.

## Scope

This folder is part of the **10-00_GENERAL** layer, which provides governance and lifecycle management for ATA Chapter 10.

### What's Included

- **Version Control**: Version control plans, policies, and semantic versioning guidelines
- **Configuration Baselines**: Functional, Allocated, Product, H2 System, and BWB Configuration baselines
- **EIS Milestones**: Roadmap and baseline snapshots at PDR, CDR, TRR, FAI, and EIS
- **Release Tags**: Release management, version registers, and release notes
- **Configuration Items**: CI registers and tracking for parking, mooring, H2, and BWB systems
- **Effectivity Management**: MSN effectivity, H2 configuration effectivity, operator effectivity
- **Change History**: Master change log, design changes, H2 changes, certification changes
- **Templates**: Reusable templates for baselines, releases, change logs, and CI registers

## Version Control Methodology

### Semantic Versioning (SemVer 2.0.0)

The program uses **Semantic Versioning** for all software, systems, and configurations:

**Format**: `MAJOR.MINOR.PATCH[-PRERELEASE][+BUILD]`

- **MAJOR**: Incompatible changes, breaking changes, major milestones
- **MINOR**: Backward-compatible functionality additions
- **PATCH**: Backward-compatible bug fixes

**Development Progression**:
```
0.1.0-alpha → 0.3.0 (PDR) → 0.5.0-beta (CDR) → 0.9.0-rc (TRR) → 1.0.0 (EIS)
```

**Production Versions**:
- `1.0.0` - Entry Into Service (EIS)
- `1.x.0` - Post-EIS enhancements
- `2.0.0+` - Major updates requiring certification amendments

### Document Versioning

All documents follow the naming pattern: **`10-00-11-NNA_DESCRIPTION.md`**

- `10` = ATA Chapter (Parking, Mooring, Storage & RTS)
- `00` = Section (GENERAL)
- `11` = Subsection (EIS_Versions_Tags)
- `NN` = Sequential number (01-99)
- `A` = Revision letter (A, B, C, ...)
- `DESCRIPTION` = Descriptive title in PascalCase with underscores

**Example**: `10-00-11-01A_Version_Control_Plan.md`

## Baseline Management Approach

### Baseline Types

The program maintains six baseline types aligned with engineering milestones:

| Baseline | Acronym | Milestone | Version Target | Document |
|----------|---------|-----------|----------------|----------|
| Functional Baseline | FBL | PDR | v0.3.0 | 10-00-11-10A |
| Allocated Baseline | ABL | CDR | v0.5.0 | 10-00-11-11A |
| Product Baseline | PBL | TRR | v0.9.0 | 10-00-11-12A |
| H2 System Baseline | H2BL | CDR/TRR | v0.5.0+ | 10-00-11-13A |
| BWB Configuration Baseline | BWBBL | CDR/TRR | v0.5.0+ | 10-00-11-14A |
| EIS Baseline | EISBL | EIS | v1.0.0 | 10-00-11-25A |

### Baseline Establishment

Baselines are frozen at key milestones after:
1. All requirements/design elements are defined and approved
2. Safety assessment is complete
3. Traceability is established
4. Milestone review (PDR/CDR/TRR/FAI/EIS) is successfully completed
5. Configuration Control Board (CCB) approves freeze

### Baseline Change Control

- **Pre-freeze**: System engineer approval
- **Post-freeze**: CCB approval required
- **Emergency changes**: Safety-critical changes permitted with post-approval review

## Directory Structure

```
10-00-11_EIS_Versions_Tags/
├── README.md (this file)
├── 00_INDEX.md
├── eis-metadata.schema.json
│
├── version-control/ (01-09)
│   ├── 10-00-11-01A_Version_Control_Plan.md
│   ├── 10-00-11-02A_Versioning_Policy.md
│   ├── 10-00-11-03A_Semantic_Versioning.md
│   └── 10-00-11-04A_Change_Log_Policy.md
│
├── configuration-baselines/ (10-19)
│   ├── 10-00-11-10A_Functional_Baseline.md (FBL - PDR)
│   ├── 10-00-11-11A_Allocated_Baseline.md (ABL - CDR)
│   ├── 10-00-11-12A_Product_Baseline.md (PBL - TRR)
│   ├── 10-00-11-13A_H2_System_Baseline.md (H2BL)
│   └── 10-00-11-14A_BWB_Config_Baseline.md (BWBBL)
│
├── eis-milestones/ (20-29)
│   ├── 10-00-11-20A_EIS_Roadmap.md
│   ├── 10-00-11-21A_PDR_Baseline.md
│   ├── 10-00-11-22A_CDR_Baseline.md
│   ├── 10-00-11-23A_TRR_Baseline.md
│   ├── 10-00-11-24A_FAI_Baseline.md
│   └── 10-00-11-25A_EIS_Baseline.md
│
├── release-tags/ (30-39)
│   ├── 10-00-11-30A_Release_Tag_Register.md
│   ├── 10-00-11-31A_v0.1.0_Alpha_Release.md
│   ├── 10-00-11-32A_v0.5.0_Beta_Release.md
│   ├── 10-00-11-33A_v1.0.0_EIS_Release.md
│   └── 10-00-11-34A_Release_Notes_Template.md
│
├── configuration-items/ (40-49)
│   ├── 10-00-11-40A_CI_Register.md
│   ├── 10-00-11-41A_Parking_System_CI.md
│   ├── 10-00-11-42A_Mooring_System_CI.md
│   ├── 10-00-11-43A_H2_System_CI.md
│   └── 10-00-11-44A_Cryo_System_CI.md
│
├── effectivity/ (50-59)
│   ├── 10-00-11-50A_Effectivity_Management.md
│   ├── 10-00-11-51A_MSN_Effectivity.md
│   ├── 10-00-11-52A_H2_Config_Effectivity.md
│   └── 10-00-11-53A_Operator_Effectivity.md
│
├── change-history/ (60-69)
│   ├── 10-00-11-60A_Master_Change_Log.md
│   ├── 10-00-11-61A_Design_Change_History.md
│   ├── 10-00-11-62A_H2_System_Change_History.md
│   └── 10-00-11-63A_Certification_Change_History.md
│
└── eis-templates/
    ├── baseline-template.md
    ├── release-notes-template.md
    ├── change-log-template.md
    └── ci-register-template.md
```

## Naming Conventions by Folder

| Folder | Number Range | Purpose | Example |
|--------|--------------|---------|---------|
| version-control | 01-09 | Version control policies and plans | 10-00-11-01A |
| configuration-baselines | 10-19 | Engineering baselines | 10-00-11-10A |
| eis-milestones | 20-29 | Milestone baselines | 10-00-11-20A |
| release-tags | 30-39 | Release management | 10-00-11-30A |
| configuration-items | 40-49 | CI tracking | 10-00-11-40A |
| effectivity | 50-59 | Effectivity management | 10-00-11-50A |
| change-history | 60-69 | Change logs | 10-00-11-60A |

## H2 and BWB Specific Baselines

### H2 System Baseline (10-00-11-13A)

Dedicated baseline for hydrogen fuel systems covering:
- LH2 tank configuration and capacity
- H2 safety systems (detection, venting, emergency response)
- Cryogenic insulation and thermal management
- H2 ground handling procedures and safety zones
- Cryo valve and sensor configurations
- H2-specific parking and storage requirements

**Key Features**:
- Safety zone definitions (5m/15m/25m exclusion/restricted/controlled)
- H2 detection alert levels (1%/2%/4% concentration)
- Cryo system thermal performance specifications
- Ground handling procedures (parking, defueling, preservation)

### BWB Configuration Baseline (10-00-11-14A)

Dedicated baseline for Blended Wing Body configuration:
- BWB airframe structural configuration
- Ground handling point locations for BWB geometry
- Clearance requirements for wide wingspan
- Center-of-gravity considerations for parking
- BWB-specific ground support equipment compatibility

**Key Features**:
- Wingspan clearance management (up to 80m)
- Unique ground handling points for wing-body blend design
- Parking position marking for BWB footprint
- Tiedown configurations for BWB structure

## EIS Milestones Overview

The program progresses through these major milestones:

1. **PDR (Preliminary Design Review)** - Month 24
   - Baseline: Functional Baseline (FBL)
   - Version: v0.3.0
   - Focus: Requirements validated, preliminary design approved

2. **CDR (Critical Design Review)** - Month 42
   - Baselines: Allocated Baseline (ABL), H2 System Baseline (H2BL), BWB Config Baseline (BWBBL)
   - Version: v0.5.0-beta
   - Focus: Detailed design complete, interfaces defined

3. **TRR (Test Readiness Review)** - Month 54
   - Baseline: Product Baseline (PBL)
   - Version: v0.9.0-rc
   - Focus: Integration complete, ready for testing

4. **FAI (First Article Inspection)** - Month 72
   - Baseline: FAI Baseline
   - Version: v1.0.0-rc.1
   - Focus: Certification testing complete, authority inspection

5. **EIS (Entry Into Service)** - Month 78
   - Baseline: EIS Baseline (EISBL)
   - Version: v1.0.0
   - Focus: Type Certificate issued, first delivery

## Configuration Items (CI) Management

All configuration items are:
- **Uniquely identified**: CI-10-[SUBSYSTEM]-[NUMBER]
- **Version controlled**: Using semantic versioning
- **Baselined**: At appropriate milestones
- **Effectivity tracked**: By MSN, operator, configuration variant

**Example CIs**:
- `CI-10-PARK-001`: Parking Position System
- `CI-10-H2-VENT-001`: H2 Venting System
- `CI-10-BWB-001`: BWB Ground Handling System

## Metadata Schema

All EIS documents and artifacts conform to `eis-metadata.schema.json`, which defines:
- Document identification and versioning
- Baseline type and milestone association
- H2/Cryo/BWB relationship flags
- Configuration item tracking
- Change summary and approval status
- Revision history

## Standards and References

This directory implements configuration management per:

### Standards
- **ATA iSpec 2200**: Configuration Management for Aviation
- **CM2**: Configuration Management Standards
- **Semantic Versioning 2.0.0**: https://semver.org/
- **SAE ARP4754A**: Development of Civil Aircraft and Systems
- **EASA Part 21**: Certification Procedures (Configuration Control)
- **S1000D**: International Specification for Technical Publications
- **ISO 10007**: Quality Management - Configuration Management

### H2-Specific Standards
- **ISO 14687**: Hydrogen fuel quality
- **NFPA 2**: Hydrogen Technologies Code
- **SAE J2719**: Hydrogen fuel quality for fuel cells

### Aviation Standards
- **CS-25**: Certification Specifications for Large Aeroplanes
- **DO-178C**: Software Considerations in Airborne Systems (for H2 monitoring software)

## Status

- **Phase**: EIS Versions Tags
- **Lifecycle Position**: 11 of 14
- **Status**: Active - Expanded structure implemented
- **Last Updated**: 2025-12-11

## Related Folders

Part of the canonical 14-folder lifecycle:
1. Overview → 2. Safety → 3. Requirements → 4. Design → 5. Interfaces → 6. Engineering → 7. V&V → 8. Prototyping → 9. Production Planning → 10. Certification → **11. EIS/Versions/Tags** → 12. Services → 13. Subsystems/Components → 14. Ops/Std/Sustain

### Key Cross-References

- **10-00-02_Safety**: Safety assessments referenced in baselines
- **10-00-03_Requirements**: Requirements traceability to baselines
- **10-00-04_Design**: Design artifacts baselined at CDR
- **10-00-07_V_AND_V**: Verification evidence for baselines
- **10-00-10_Certification**: Certification artifacts and Type Certificate
- **10-90_Tables_Schemas_Diagrams**: Traceability matrices and schemas

## Document Control

- **Standard**: OPT-IN Framework v1.1 (ATA 95 canonical template)
- **Owner**: AMPEL360 Configuration Management Team
- **Approved By**: [To be assigned]
- **Version**: 2.0.0
- **Last Updated**: 2025-12-11
- **Next Review**: At PDR milestone

---

**END OF DOCUMENT**
