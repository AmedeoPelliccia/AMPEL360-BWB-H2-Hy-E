# 85-00-11-002: Versioning and Tagging Model for ATA 85

## Purpose

This document defines the **versioning model and tagging conventions** for **ATA 85 – Infrastructure Interface Standards**, enabling systematic tracking, configuration management, and traceability of infrastructure interface baselines throughout the aircraft lifecycle.

---

## Scope

### In Scope

- Semantic versioning rules for ATA 85 interface standards
- Git tagging conventions for CD/CI integration
- Relationship between tags, baselines, and EIS packages
- Mapping to [DPP (Digital Product Passport)](../../../N-NEURAL_NETWORKS_USERS_TRACEABILITY/ATA_95-DIGITAL_PRODUCT_PASSPORT_NEURAL_NETWORKS/README.md) schema versions
- Compatibility rules across interface versions

### Out of Scope

- Aircraft-level versioning (covered in 00-00-11_EIS_VERSIONS_TAGS)
- Individual component version tracking (covered in [85-00-13_Subsystems_Components](../85-00-13_Subsystems_Components/README.md))
- Software versioning for on-board systems (covered in respective ATA 40 chapters)

---

## Versioning Principles

### 1. Semantic Versioning (SemVer)

ATA 85 interface standards follow **semantic versioning** principles adapted for aviation infrastructure:

```
MAJOR.MINOR.PATCH
```

- **MAJOR**: Incompatible interface changes requiring aircraft/infrastructure modifications
- **MINOR**: Backward-compatible feature additions (e.g., new optional connectors)
- **PATCH**: Backward-compatible bug fixes, clarifications, or documentation updates

**Example**: `v2.1.0`
- Major version 2: Significant interface redesign (e.g., H₂ connector change)
- Minor version 1: Added optional CO₂ battery charging interface
- Patch version 0: Initial release of this minor version

---

### 2. Version Lifecycle States

Each version progresses through defined states:

| State | Description | Tag Suffix |
|-------|-------------|------------|
| **DRAFT** | Under development, not released | `-draft` |
| **RELEASE_CANDIDATE** | Feature-complete, undergoing final validation | `-rc1`, `-rc2`, etc. |
| **RELEASED** | Approved for EIS, active in operations | None (standard tag) |
| **DEPRECATED** | Superseded by newer version, not recommended for new deployments | Marked in [85-00-11-A-103_Deprecated_Tags_Register.csv](./ASSETS/Tags/85-00-11-A-103_Deprecated_Tags_Register.csv) |
| **RETIRED** | No longer supported, must migrate to newer version | Marked in register |

---

## Git Tagging Conventions

### Tag Structure

Git tags for ATA 85 infrastructure releases follow this pattern:

```regex
v[0-9]+\.[0-9]+\.[0-9]+-85-[A-Z]+-[A-Z0-9]+
```

**Components**:
1. **`vX.Y.Z`**: Semantic version (e.g., `v2.1.0`)
2. **`-85-`**: Constant identifier for ATA 85
3. **`[A-Z]+`**: Airport Archetype Code (e.g., `ARCHA`, `ARCHB`, `ARCHC`)
4. **`[A-Z0-9]+`**: Configuration Variant (e.g., `H2STD`, `H2CO2`, `H2ONLY`)

### Tag Examples

| Tag | Interpretation |
|-----|----------------|
| `v02.01.00-85-ARCHA-H2STD` | Version 2.1.0 for Archetype A airports with Standard H₂ refuelling |
| `v02.01.00-85-ARCHB-H2CO2` | Version 2.1.0 for Archetype B airports with H₂ + CO₂ battery infra |
| `v03.00.00-85-ARCHC-H2ONLY` | Version 3.0.0 for Archetype C airports with H₂-only (no CO₂ battery) |

### Tag Creation Rules

1. **Uniqueness**: Each tag must be globally unique within the repository
2. **Immutability**: Once a tag is pushed, it MUST NOT be modified or deleted
3. **Traceability**: Each tag MUST have a corresponding entry in [85-00-11-A-101_Git_Tags_to_ATA85_Config_Map.csv](./ASSETS/Tags/85-00-11-A-101_Git_Tags_to_ATA85_Config_Map.csv)
4. **Approval**: Tags for RELEASED versions require CCB approval per [85-00-10_Certification](../85-00-10_Certification/README.md)

---

## Relationship Between Tags, Baselines, and EIS Packages

### Configuration Baseline

A **baseline** is a frozen snapshot of:
- ATA 85 requirements (from [85-00-03_Requirements](../85-00-03_Requirements/README.md))
- Interface Control Documents (ICDs) (from [85-00-05_Interfaces](../85-00-05_Interfaces/README.md))
- Design specifications (from [85-00-04_Design](../85-00-04_Design/README.md))
- V&V evidence (from [85-00-07_V_AND_V](../85-00-07_V_AND_V/README.md))
- Certification artifacts (from [85-00-10_Certification](../85-00-10_Certification/README.md))

**Baseline Naming**: `BL-85-00-11-XXX` (e.g., `BL-85-00-11-004`)

---

### EIS Package

An **EIS package** is a deployment-ready bundle containing:
- Baseline reference
- Airport archetype specifications
- Configuration variant (H₂/CO₂/GSE options)
- Installation/validation procedures
- Training materials
- Rollback plans

**Package Naming**: `PKG-85-ARCH-X-YYY` (e.g., `PKG-85-ARCH-A-001`)

---

### Mapping Flow

```
Git Tag → Baseline → EIS Package → Airport Deployment
```

1. **Git Tag** created upon approval of a release
2. **Baseline** frozen and registered in [85-00-11-A-001_Interface_Baseline_Register.xlsx](./ASSETS/Baselines/85-00-11-A-001_Interface_Baseline_Register.xlsx)
3. **EIS Package** assembled per [85-00-11-A-201_EIS_Package_Template.md](./ASSETS/EIS_Packages/85-00-11-A-201_EIS_Package_Template.md)
4. **Airport Deployment** executed per [85-00-11-001_EIS_Strategy_Infrastructure_Interfaces.md](./85-00-11-001_EIS_Strategy_Infrastructure_Interfaces.md)

---

## CSV Mapping for GenCCC/CGen Automation

### File: `85-00-11-A-101_Git_Tags_to_ATA85_Config_Map.csv`

This CSV file is the **"Rosetta Stone"** for automation tools (**GenCCC** and **CGen**), enabling automatic linking of CD releases to ATA 85 configurations.

#### Column Definitions

| Column Header | Description | Example Value |
|---------------|-------------|---------------|
| **GIT_TAG** | Exact Git tag string (Primary Key) | `v02.01.00-85-ARCHA-H2STD` |
| **ATA85_BASELINE_ID** | Frozen baseline identifier | `BL-85-00-11-004` |
| **EIS_PACKAGE_REF** | EIS package reference | `PKG-85-ARCH-A-001` |
| **DPP_SCHEMA_VER** | [DPP](../../../N-NEURAL_NETWORKS_USERS_TRACEABILITY/ATA_95-DIGITAL_PRODUCT_PASSPORT_NEURAL_NETWORKS/README.md) schema version | `v1.4` |
| **COMPATIBILITY_MASK** | Regex for compatible aircraft software versions | `^v04\.0[0-9]\..*` |
| **RELEASE_DATE** | ISO 8601 date (YYYY-MM-DD) | `2025-11-21` |
| **STATUS** | Current status (RELEASED, DEPRECATED, RETIRED) | `RELEASED` |
| **NOTES** | Optional human-readable notes | `Initial EIS for FRA airport` |

#### Example CSV Content

```csv
GIT_TAG,ATA85_BASELINE_ID,EIS_PACKAGE_REF,DPP_SCHEMA_VER,COMPATIBILITY_MASK,RELEASE_DATE,STATUS,NOTES
v02.01.00-85-ARCHA-H2STD,BL-85-00-11-004,PKG-85-ARCH-A-001,v1.4,^v04\.0[0-9]\..*,2025-11-21,RELEASED,Initial EIS for FRA airport
v02.01.00-85-ARCHB-H2STD,BL-85-00-11-005,PKG-85-ARCH-B-001,v1.4,^v04\.0[0-9]\..*,2025-12-15,RELEASED,Initial EIS for MUC airport
v02.02.00-85-ARCHA-H2CO2,BL-85-00-11-006,PKG-85-ARCH-A-002,v1.5,^v04\.1[0-9]\..*,2026-03-01,RELEASED,Added CO2 battery interface
```

---

### Automation Logic

When **CGen** (Continuous Generation tool) detects a new Git tag matching the pattern:

1. **Parse tag**: Extract version, archetype, variant
2. **Lookup CSV**: Find corresponding row in `85-00-11-A-101_Git_Tags_to_ATA85_Config_Map.csv`
3. **Retrieve metadata**:
   - `ATA85_BASELINE_ID`: Links to frozen baseline documentation
   - `EIS_PACKAGE_REF`: Links to deployment package
   - `DPP_SCHEMA_VER`: Ensures DPP compatibility
   - `COMPATIBILITY_MASK`: Validates aircraft software compatibility
4. **Stamp artifacts**: All release artifacts tagged with:
   - Git tag
   - Baseline ID
   - DPP schema version
   - ISO 8601 timestamp
5. **Generate release notes**: Auto-populate template from [85-00-11-A-301_EIS_Release_Notes_Template.md](./ASSETS/Reports/85-00-11-A-301_EIS_Release_Notes_Template.md)
6. **Update DPP**: Record infrastructure interface version in [ATA 95 DPP](../../../N-NEURAL_NETWORKS_USERS_TRACEABILITY/ATA_95-DIGITAL_PRODUCT_PASSPORT_NEURAL_NETWORKS/README.md)

---

## Version Compatibility Rules

### Backward Compatibility

- **PATCH updates**: Always backward-compatible
- **MINOR updates**: Backward-compatible; may add optional features
- **MAJOR updates**: May break backward compatibility; require migration plan

### Forward Compatibility

- Not guaranteed across MAJOR versions
- MINOR/PATCH updates should be forward-compatible where feasible

### Compatibility Matrix

Maintained in [85-00-11-A-002_Airport_Archetype_Baselines.xlsx](./ASSETS/Baselines/85-00-11-A-002_Airport_Archetype_Baselines.xlsx), showing which aircraft software versions are compatible with which infrastructure interface versions.

---

## DPP Schema Versioning

Each ATA 85 interface version is associated with a [DPP schema version](../../../N-NEURAL_NETWORKS_USERS_TRACEABILITY/ATA_95-DIGITAL_PRODUCT_PASSPORT_NEURAL_NETWORKS/README.md):

- **DPP v1.x**: Initial DPP implementation, basic interface metadata
- **DPP v2.x**: Enhanced traceability, blockchain anchoring
- **DPP v3.x**: AI-driven predictive maintenance integration

**Mapping**: Defined in `DPP_SCHEMA_VER` column of CSV map

---

## Deprecation and Retirement Policy

### Deprecation

- Triggered when a newer MAJOR version is released
- Deprecated versions remain supported for **minimum 24 months**
- Operators notified via [85-00-11-A-301_EIS_Release_Notes_Template.md](./ASSETS/Reports/85-00-11-A-301_EIS_Release_Notes_Template.md)
- Tagged in [85-00-11-A-103_Deprecated_Tags_Register.csv](./ASSETS/Tags/85-00-11-A-103_Deprecated_Tags_Register.csv)

### Retirement

- Occurs after deprecation period (minimum 24 months)
- All operators must migrate to newer version
- Retired versions removed from active support
- Historical records maintained per [DO-178C traceability requirements](https://www.rtca.org/content/standards-guidance-materials)

---

## Change Control

### Minor/Patch Updates

- Approved by **ATA 85 Configuration Lead**
- Documented in [85-00-11-006_Change_Log_and_Lifecycle_History.md](./85-00-11-006_Change_Log_and_Lifecycle_History.md)
- CCB notification (information only)

### Major Updates

- Require **CCB (Configuration Control Board)** approval
- Full impact analysis per [85-00-03_Requirements](../85-00-03_Requirements/README.md)
- Certification review per [85-00-10_Certification](../85-00-10_Certification/README.md)
- Operator coordination per [85-00-11-001_EIS_Strategy_Infrastructure_Interfaces.md](./85-00-11-001_EIS_Strategy_Infrastructure_Interfaces.md)

---

## References

- [Semantic Versioning 2.0.0](https://semver.org/)
- [DO-178C – Software Considerations in Airborne Systems and Equipment Certification](https://www.rtca.org/content/standards-guidance-materials)
- [EASA Part 21 – Certification of Aircraft and Related Products](https://www.easa.europa.eu/en/document-library/regulations/commission-regulation-eu-no-7482012)
- [85-00-03_Requirements](../85-00-03_Requirements/README.md)
- [85-00-05_Interfaces](../85-00-05_Interfaces/README.md)
- [85-00-10_Certification](../85-00-10_Certification/README.md)
- [85-00-11-003_Interface_Configuration_Baselines.md](./85-00-11-003_Interface_Configuration_Baselines.md)
- [ATA 95 – Digital Product Passport](../../../N-NEURAL_NETWORKS_USERS_TRACEABILITY/ATA_95-DIGITAL_PRODUCT_PASSPORT_NEURAL_NETWORKS/README.md)

---

## Document Control

- **Standard**: OPT-IN Framework v1.1 (A-LIVE-GP, ATA 85 pattern)
- **Document ID**: 85-00-11-002
- **Version**: 1.0 (DRAFT)
- **Last Updated**: 2025-11-21
- **Next Review**: 2026-02-21
- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT** – Subject to human review and approval.
- Human approver: *[to be completed]*.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: *2025-11-21*.
