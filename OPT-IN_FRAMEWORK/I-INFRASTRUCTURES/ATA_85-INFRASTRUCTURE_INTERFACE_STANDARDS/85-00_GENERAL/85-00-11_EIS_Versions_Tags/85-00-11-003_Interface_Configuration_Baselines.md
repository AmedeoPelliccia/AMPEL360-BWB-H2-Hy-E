# 85-00-11-003: Interface Configuration Baselines

## Purpose

This document defines the **rules and procedures** for creating, controlling, and managing **configuration baselines** for ATA 85 infrastructure interfaces, ensuring systematic configuration management and traceability throughout the aircraft lifecycle.

---

## Scope

### In Scope

- Baseline identification and naming conventions
- Baseline content definition (requirements, design, ICDs, test evidence)
- Baseline freeze and approval processes
- Baseline change control procedures
- Traceability to [DPP (Digital Product Passport)](../../../N-NEURAL_NETWORKS_USERS_TRACEABILITY/ATA_95-DIGITAL_PRODUCT_PASSPORT_NEURAL_NETWORKS/README.md) and Git tags

### Out of Scope

- Detailed interface specifications (covered in [85-00-05_Interfaces](../85-00-05_Interfaces/README.md))
- Test procedures (covered in [85-00-07_V_AND_V](../85-00-07_V_AND_V/README.md))
- Certification processes (covered in [85-00-10_Certification](../85-00-10_Certification/README.md))

---

## Baseline Definition

### What is a Configuration Baseline?

A **configuration baseline** is a formally approved, frozen snapshot of:
- Requirements documents
- Design specifications
- Interface Control Documents (ICDs)
- V&V evidence and test reports
- Certification artifacts
- Associated software/firmware versions (if applicable)

**Purpose**: Provides a stable reference point for EIS deployment, change management, and traceability.

---

## Baseline Naming Convention

### Format

```
BL-85-00-11-XXX
```

**Components**:
- **BL**: Baseline identifier
- **85**: ATA chapter (Infrastructure)
- **00-11**: Lifecycle stage (EIS/Versions/Tags)
- **XXX**: Sequential baseline number (001, 002, 003, etc.)

### Examples

| Baseline ID | Description |
|-------------|-------------|
| `BL-85-00-11-001` | Initial baseline for Archetype A airports, H₂ standard configuration |
| `BL-85-00-11-002` | Enhanced baseline with CO₂ battery interface |
| `BL-85-00-11-003` | Regional variant for North American airports |

---

## Baseline Content

### Mandatory Components

Each baseline MUST include:

1. **Requirements Traceability Matrix (RTM)**
   - Links to [85-00-03_Requirements](../85-00-03_Requirements/README.md)
   - Coverage: Functional, performance, safety, regulatory requirements

2. **Interface Control Documents (ICDs)**
   - Links to [85-00-05_Interfaces](../85-00-05_Interfaces/README.md)
   - Coverage: H₂ refuelling, CO₂ battery, GSE, PAX boarding/evac

3. **Design Documentation**
   - Links to [85-00-04_Design](../85-00-04_Design/README.md)
   - Coverage: Physical interfaces, electrical interfaces, data interfaces

4. **V&V Evidence Package**
   - Links to [85-00-07_V_AND_V](../85-00-07_V_AND_V/README.md)
   - Coverage: Test reports, simulation results, validation certificates

5. **Certification Artifacts**
   - Links to [85-00-10_Certification](../85-00-10_Certification/README.md)
   - Coverage: Type certificate data, compliance statements per [CS-25](https://www.easa.europa.eu/en/document-library/certification-specifications/cs-25-amendment-27) / [FAR-25](https://www.ecfr.gov/current/title-14/chapter-I/subchapter-C/part-25)

6. **DPP Schema Reference**
   - Links to [ATA 95 DPP](../../../N-NEURAL_NETWORKS_USERS_TRACEABILITY/ATA_95-DIGITAL_PRODUCT_PASSPORT_NEURAL_NETWORKS/README.md)
   - Coverage: Schema version, blockchain anchor references

7. **Git Tag Reference**
   - Tag(s) associated with this baseline (per [85-00-11-002_Versioning_and_Tagging_Model.md](./85-00-11-002_Versioning_and_Tagging_Model.md))

---

## Baseline Lifecycle

### 1. Baseline Creation (DRAFT)

**Trigger**: Completion of design, V&V, and pre-certification activities

**Activities**:
- Assemble baseline content from upstream lifecycle stages
- Perform internal consistency checks
- Draft baseline documentation per [85-00-11-A-001_Interface_Baseline_Register.xlsx](./ASSETS/Baselines/85-00-11-A-001_Interface_Baseline_Register.xlsx)

**Approval**: ATA 85 Configuration Lead

---

### 2. Baseline Review (UNDER_REVIEW)

**Trigger**: DRAFT baseline complete and consistent

**Activities**:
- CCB (Configuration Control Board) review
- Stakeholder feedback (airlines, airports, suppliers)
- Regulatory pre-coordination (EASA, FAA)

**Approval**: CCB consensus

---

### 3. Baseline Freeze (FROZEN)

**Trigger**: CCB approval and all review comments resolved

**Activities**:
- Freeze all baseline content (no further changes without CCB approval)
- Create Git tag per [85-00-11-002_Versioning_and_Tagging_Model.md](./85-00-11-002_Versioning_and_Tagging_Model.md)
- Register in [85-00-11-A-001_Interface_Baseline_Register.xlsx](./ASSETS/Baselines/85-00-11-A-001_Interface_Baseline_Register.xlsx)
- Anchor in [DPP](../../../N-NEURAL_NETWORKS_USERS_TRACEABILITY/ATA_95-DIGITAL_PRODUCT_PASSPORT_NEURAL_NETWORKS/README.md)

**Approval**: CCB Chair + Certification Authority liaison

---

### 4. Baseline Release (RELEASED)

**Trigger**: Certification approval and readiness for EIS

**Activities**:
- Publish EIS package per [85-00-11-A-201_EIS_Package_Template.md](./ASSETS/EIS_Packages/85-00-11-A-201_EIS_Package_Template.md)
- Notify operators per [85-00-11-A-301_EIS_Release_Notes_Template.md](./ASSETS/Reports/85-00-11-A-301_EIS_Release_Notes_Template.md)
- Enable for airport deployments

**Approval**: Program leadership + regulatory authorities

---

### 5. Baseline Superseded (SUPERSEDED)

**Trigger**: Newer baseline released that replaces this one

**Activities**:
- Mark as SUPERSEDED in register
- Maintain for 24+ months per deprecation policy ([85-00-11-002](./85-00-11-002_Versioning_and_Tagging_Model.md))
- Plan migration for operators

**Approval**: ATA 85 Configuration Lead

---

### 6. Baseline Retired (RETIRED)

**Trigger**: End of support period (24+ months post-supersession)

**Activities**:
- Remove from active baselines
- Archive for historical/audit purposes
- Ensure all operators migrated to newer baseline

**Approval**: CCB Chair

---

## Baseline Change Control

### Minor Changes (PATCH-level)

**Examples**: Documentation clarifications, typo fixes, non-functional updates

**Process**:
1. Propose change via change request (CR)
2. Impact analysis by ATA 85 Configuration Lead
3. Approval by Configuration Lead (no CCB required)
4. Update baseline documentation
5. Increment PATCH version (e.g., v2.1.0 → v2.1.1)
6. Log in [85-00-11-006_Change_Log_and_Lifecycle_History.md](./85-00-11-006_Change_Log_and_Lifecycle_History.md)

---

### Moderate Changes (MINOR-level)

**Examples**: Addition of optional interfaces, performance improvements, backward-compatible enhancements

**Process**:
1. Propose change via change request (CR)
2. Impact analysis by ATA 85 Configuration Lead + Engineering
3. CCB review (notification, not full approval)
4. Update baseline documentation
5. Increment MINOR version (e.g., v2.1.0 → v2.2.0)
6. Log in [85-00-11-006_Change_Log_and_Lifecycle_History.md](./85-00-11-006_Change_Log_and_Lifecycle_History.md)

---

### Major Changes (MAJOR-level)

**Examples**: Interface redesign, safety-critical changes, incompatible updates

**Process**:
1. Propose change via change request (CR)
2. Full impact analysis (safety, certification, operators, airports)
3. CCB formal review and approval
4. Regulatory coordination (EASA, FAA)
5. Create new baseline (e.g., `BL-85-00-11-010`)
6. Increment MAJOR version (e.g., v2.1.0 → v3.0.0)
7. Log in [85-00-11-006_Change_Log_and_Lifecycle_History.md](./85-00-11-006_Change_Log_and_Lifecycle_History.md)
8. Notify all operators, plan migration

---

## Baseline Traceability

### Upstream Traceability

Each baseline traces back to:
- **Requirements** ([85-00-03](../85-00-03_Requirements/README.md))
- **Design** ([85-00-04](../85-00-04_Design/README.md))
- **Interfaces** ([85-00-05](../85-00-05_Interfaces/README.md))
- **V&V** ([85-00-07](../85-00-07_V_AND_V/README.md))
- **Certification** ([85-00-10](../85-00-10_Certification/README.md))

### Downstream Traceability

Each baseline is used by:
- **EIS Packages** ([85-00-11-004](./85-00-11-004_Airport_Archetype_EIS_Packages.md), [85-00-11-005](./85-00-11-005_H2_CO2_GSE_EIS_Packages.md))
- **Airport Deployments** (per [85-00-11-001](./85-00-11-001_EIS_Strategy_Infrastructure_Interfaces.md))
- **Services** ([85-00-12](../85-00-12_Services/README.md))
- **Operational Monitoring** ([ATA 98](../../../N-NEURAL_NETWORKS_USERS_TRACEABILITY/ATA_98-NEURAL_NETWORK_RUNTIME_MONITORING/README.md))

### Horizontal Traceability

Each baseline links to:
- **Git Tag** (per [85-00-11-002](./85-00-11-002_Versioning_and_Tagging_Model.md))
- **DPP Entry** ([ATA 95](../../../N-NEURAL_NETWORKS_USERS_TRACEABILITY/ATA_95-DIGITAL_PRODUCT_PASSPORT_NEURAL_NETWORKS/README.md))
- **CD Release Artifacts** (GenCCC/CGen automation)

---

## Baseline Variants

### Geographic Variants

- **EU**: European regulations ([EASA CS-25](https://www.easa.europa.eu/en/document-library/certification-specifications/cs-25-amendment-27))
- **US**: North American regulations ([FAA FAR-25](https://www.ecfr.gov/current/title-14/chapter-I/subchapter-C/part-25))
- **APAC**: Asia-Pacific regulations (CAAC, CASA, etc.)

**Management**: Separate baseline IDs or variant suffixes (e.g., `BL-85-00-11-001-EU`, `BL-85-00-11-001-US`)

---

### Configuration Variants

- **H₂ Standard**: Standard H₂ refuelling interfaces
- **H₂ + CO₂**: H₂ refuelling + CO₂ battery charging
- **H₂ Only**: H₂ refuelling without CO₂ battery (for aircraft without CO₂ systems)

**Management**: Captured in `CONFIGURATION_VARIANT` field of [85-00-11-A-001_Interface_Baseline_Register.xlsx](./ASSETS/Baselines/85-00-11-A-001_Interface_Baseline_Register.xlsx)

---

## Baseline Snapshot Template

For airport-specific deployments, use [85-00-11-A-003_EIS_Config_Snapshot_Template.xlsx](./ASSETS/Baselines/85-00-11-A-003_EIS_Config_Snapshot_Template.xlsx) to capture:
- Airport ID (ICAO code)
- Airline operator
- Baseline ID applied
- Configuration variant
- Installation date
- Validation status
- Contact information

---

## References

- [ISO 10007:2017 – Quality management — Guidelines for configuration management](https://www.iso.org/standard/70400.html)
- [EASA Part 21 – Certification of Aircraft and Related Products](https://www.easa.europa.eu/en/document-library/regulations/commission-regulation-eu-no-7482012)
- [DO-178C – Software Considerations in Airborne Systems and Equipment Certification](https://www.rtca.org/content/standards-guidance-materials)
- [85-00-03_Requirements](../85-00-03_Requirements/README.md)
- [85-00-04_Design](../85-00-04_Design/README.md)
- [85-00-05_Interfaces](../85-00-05_Interfaces/README.md)
- [85-00-07_V_AND_V](../85-00-07_V_AND_V/README.md)
- [85-00-10_Certification](../85-00-10_Certification/README.md)
- [85-00-11-002_Versioning_and_Tagging_Model.md](./85-00-11-002_Versioning_and_Tagging_Model.md)
- [ATA 95 – Digital Product Passport](../../../N-NEURAL_NETWORKS_USERS_TRACEABILITY/ATA_95-DIGITAL_PRODUCT_PASSPORT_NEURAL_NETWORKS/README.md)

---

## Document Control

- **Standard**: OPT-IN Framework v1.1 (A-LIVE-GP, ATA 85 pattern)
- **Document ID**: 85-00-11-003
- **Version**: 1.0 (DRAFT)
- **Last Updated**: 2025-11-21
- **Next Review**: 2026-02-21
- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT** – Subject to human review and approval.
- Human approver: *[to be completed]*.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: *2025-11-21*.
