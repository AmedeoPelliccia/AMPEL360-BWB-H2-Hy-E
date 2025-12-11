# Index: I-INFRASTRUCTURES/ATA_10-PARKING_MOORING_STORAGE_RTS/10-00_GENERAL/10-00-11_EIS_Versions_Tags

> **Last Update:** 2025-12-11
> **Status:** Expanded structure with version control, baselines, milestones, releases, and change management

## 📂 Directory Contents

### 📄 Core Files

- **README.md** - Comprehensive overview of EIS version management, baselines, and configuration control
- **eis-metadata.schema.json** - JSON Schema for EIS metadata standardization

---

## 📁 Subdirectories

### 1. version-control/ (Documents 01-09)

Version control policies, plans, and guidelines:

- **10-00-11-01A_Version_Control_Plan.md** - Overall version control plan and framework
- **10-00-11-02A_Versioning_Policy.md** - Versioning policies and governance rules
- **10-00-11-03A_Semantic_Versioning.md** - Semantic versioning (SemVer 2.0.0) guidelines
- **10-00-11-04A_Change_Log_Policy.md** - Change log requirements and standards

### 2. configuration-baselines/ (Documents 10-19)

Engineering baselines established at major milestones:

- **10-00-11-10A_Functional_Baseline.md** - Functional Baseline (FBL) at PDR
- **10-00-11-11A_Allocated_Baseline.md** - Allocated Baseline (ABL) at CDR
- **10-00-11-12A_Product_Baseline.md** - Product Baseline (PBL) at TRR
- **10-00-11-13A_H2_System_Baseline.md** - H2 System Baseline (H2BL) - LH2 fuel and cryo systems
- **10-00-11-14A_BWB_Config_Baseline.md** - BWB Configuration Baseline (BWBBL) - Blended Wing Body specific

### 3. eis-milestones/ (Documents 20-29)

EIS roadmap and milestone baseline snapshots:

- **10-00-11-20A_EIS_Roadmap.md** - Overall EIS roadmap with phases, milestones, and timeline
- **10-00-11-21A_PDR_Baseline.md** - Preliminary Design Review baseline snapshot
- **10-00-11-22A_CDR_Baseline.md** - Critical Design Review baseline snapshot
- **10-00-11-23A_TRR_Baseline.md** - Test Readiness Review baseline snapshot
- **10-00-11-24A_FAI_Baseline.md** - First Article Inspection baseline snapshot
- **10-00-11-25A_EIS_Baseline.md** - Entry Into Service baseline (Type Certificate)

### 4. release-tags/ (Documents 30-39)

Release management, version tags, and release notes:

- **10-00-11-30A_Release_Tag_Register.md** - Master register of all releases and tags
- **10-00-11-31A_v0.1.0_Alpha_Release.md** - Alpha release (v0.1.0) details
- **10-00-11-32A_v0.5.0_Beta_Release.md** - Beta release (v0.5.0) at CDR
- **10-00-11-33A_v1.0.0_EIS_Release.md** - EIS release (v1.0.0) - Type Certificate baseline
- **10-00-11-34A_Release_Notes_Template.md** - Template for release notes

### 5. configuration-items/ (Documents 40-49)

Configuration Item (CI) registers and tracking:

- **10-00-11-40A_CI_Register.md** - Master CI register for all ATA 10 systems
- **10-00-11-41A_Parking_System_CI.md** - Parking system configuration items
- **10-00-11-42A_Mooring_System_CI.md** - Mooring system configuration items
- **10-00-11-43A_H2_System_CI.md** - H2 fuel system configuration items (safety, venting, detection)
- **10-00-11-44A_Cryo_System_CI.md** - Cryogenic system configuration items (tanks, insulation, valves)

### 6. effectivity/ (Documents 50-59)

Effectivity management for configurations and changes:

- **10-00-11-50A_Effectivity_Management.md** - Overall effectivity management approach
- **10-00-11-51A_MSN_Effectivity.md** - Manufacturing Serial Number (MSN) effectivity tracking
- **10-00-11-52A_H2_Config_Effectivity.md** - H2 configuration effectivity (H2-equipped vs. non-H2)
- **10-00-11-53A_Operator_Effectivity.md** - Operator-specific configuration effectivity

### 7. change-history/ (Documents 60-69)

Change logs and history tracking:

- **10-00-11-60A_Master_Change_Log.md** - Master change log for entire ATA 10 system
- **10-00-11-61A_Design_Change_History.md** - Design change history and evolution
- **10-00-11-62A_H2_System_Change_History.md** - H2 system-specific change history
- **10-00-11-63A_Certification_Change_History.md** - Certification-affecting changes log

### 8. eis-templates/

Reusable templates for consistency:

- **baseline-template.md** - Standard template for baseline documents
- **release-notes-template.md** - Standard template for release notes
- **change-log-template.md** - Standard template for change logs (Keep a Changelog format)
- **ci-register-template.md** - Standard template for CI registers

---

## 📊 Quick Reference

### Version Numbering Scheme

- **Semantic Versioning**: MAJOR.MINOR.PATCH
- **Development**: 0.x.y (pre-EIS)
- **Production**: 1.x.y (post-EIS)
- **Document IDs**: 10-00-11-NNA_DESCRIPTION

### Baseline Progression

| Milestone | Version | Baseline | Document |
|-----------|---------|----------|----------|
| PDR | v0.3.0 | FBL | 10-00-11-10A, 10-00-11-21A |
| CDR | v0.5.0 | ABL, H2BL, BWBBL | 10-00-11-11A, 10-00-11-13A, 10-00-11-14A, 10-00-11-22A |
| TRR | v0.9.0 | PBL | 10-00-11-12A, 10-00-11-23A |
| FAI | v1.0.0-rc | FAI Baseline | 10-00-11-24A |
| EIS | v1.0.0 | EIS Baseline | 10-00-11-25A |

### Configuration Item Families

- **CI-10-PARK-XXX**: Parking systems
- **CI-10-MOOR-XXX**: Mooring systems
- **CI-10-STOR-XXX**: Storage systems
- **CI-10-H2-XXX**: H2 fuel and safety systems
- **CI-10-CRYO-XXX**: Cryogenic systems
- **CI-10-BWB-XXX**: BWB-specific systems

---

## 🔗 Related Documentation

- **10-00-02_Safety**: Safety assessments referenced in baselines
- **10-00-03_Requirements**: Requirements baselined in FBL
- **10-00-04_Design**: Design artifacts baselined in ABL/PBL
- **10-00-10_Certification**: Type Certificate and certification evidence
- **10-90_Tables_Schemas_Diagrams**: Traceability matrices

---

## 📌 Document Status Legend

- **DRAFT**: Under development
- **IN_REVIEW**: Under review
- **APPROVED**: Approved, not yet released
- **RELEASED**: Official release, under configuration control
- **SUPERSEDED**: Replaced by newer version
- **OBSOLETE**: No longer valid

---

**Last Updated**: 2025-12-11  
**Maintained By**: AMPEL360 Configuration Management Team
