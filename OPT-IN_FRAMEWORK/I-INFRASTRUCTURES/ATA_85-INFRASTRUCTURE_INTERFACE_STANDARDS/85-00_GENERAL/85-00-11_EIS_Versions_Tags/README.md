# 85-00-11_EIS_Versions_Tags

## Purpose

This folder defines the **Entry Into Service (EIS), versioning and tagging framework** for  
**ATA 85 – Infrastructure Interface Standards**, with focus on:

- Interfaces between the BWB aircraft and **airport infrastructure**
- **Hydrogen (H₂)** production, storage and refuelling interfaces
- **CO₂ battery** infrastructure interfaces
- **Ground services (GSE)** power and data interfaces
- **Passenger boarding and evacuation** infrastructure interfaces

It corresponds to **Stage 11 – EIS / Versions / Tags** of the  
**A-LIVE-GP – Aircraft Lifecycle Industrialization and Validation Executive General Plan** for ATA 85.

---

## Scope

### In Scope

- EIS strategy for ATA 85 interface standards (by airport archetype, region, maturity)
- Versioning model and tagging conventions for infrastructure interface baselines
- Definition and management of **ATA 85 configuration baselines** for EIS
- EIS package structure for:
  - Airport infra archetypes (A, B, C…)
  - H₂ / CO₂ infra configurations
  - GSE / power / data configurations
  - PAX boarding/evac infrastructure configurations
- Mapping between **Git tags / CD releases** and ATA 85 EIS baselines
- Linkage to **digital twin** and **DPP** (Digital Product Passport) states

### Out of Scope

- Detailed certification logic (covered in [85-00-10_Certification](../85-00-10_Certification/README.md))
- Detailed operational procedures (covered in [85-00-12_Services](../85-00-12_Services/README.md) and [ATA 02](../../../ATA_02-OPERATIONS_INFORMATION/README.md))
- Full aircraft-wide EIS governance (covered in 00-00-11_EIS_Versions_Tags)

---

## Contents

### Core Documents

- `85-00-11-001_EIS_Strategy_Infrastructure_Interfaces.md`  
  High-level EIS strategy for ATA 85:
  - Phasing per airport archetype
  - Dependencies on infrastructure readiness (H₂, CO₂, GSE, PAX flows)
  - Coordination with airline and airport operators.

- `85-00-11-002_Versioning_and_Tagging_Model.md`  
  Definition of the versioning model for ATA 85:
  - Semantic versioning rules for interface standards
  - Tagging conventions (Git tags, CD release labels)
  - Relationship between **tags**, **baselines** and **EIS packages**.

- `85-00-11-003_Interface_Configuration_Baselines.md`  
  Rules for defining and controlling ATA 85 baselines:
  - Baseline identification and naming
  - Baseline content (requirements, design, ICDs, test evidence pointers)
  - Baseline freeze and change rules.

- `85-00-11-004_Airport_Archetype_EIS_Packages.md`  
  Definition of EIS package structure per airport archetype:
  - Minimum infra for A/B/C category airports
  - Variants (H₂ only, H₂ + CO₂ battery infra, etc.)
  - EIS dependencies and readiness criteria per archetype.

- `85-00-11-005_H2_CO2_GSE_EIS_Packages.md`  
  Aggregated EIS packages for:
  - Hydrogen refuelling systems
  - CO₂ battery ground infra
  - GSE power/data interface packs.

- `85-00-11-006_Change_Log_and_Lifecycle_History.md`  
  High-level change log:
  - Introduced/retired EIS packages
  - Baseline transitions over time
  - Major impacting changes to airport infra requirements.

- `85-00-11-007_Digital_Twin_and_DPP_Linkage.md`  
  How EIS versions are mapped to:
  - Infrastructure digital twin states
  - DPP records for infra components
  - CD release artifacts and GenCCC baselines.

---

## ASSETS

### `ASSETS/Baselines/`

- `85-00-11-A-001_Interface_Baseline_Register.xlsx`  
  Master list of ATA 85 baselines with IDs, scope, status, validity dates.

- `85-00-11-A-002_Airport_Archetype_Baselines.xlsx`  
  Mapping of airport archetypes (A/B/C…) to baseline IDs.

- `85-00-11-A-003_EIS_Config_Snapshot_Template.xlsx`  
  Template to capture a frozen EIS configuration snapshot for a specific airline/airport pair.

### `ASSETS/Tags/`

- `85-00-11-A-101_Git_Tags_to_ATA85_Config_Map.csv`  
  Table linking Git tags (e.g. `v02.85.00`) to ATA 85 baselines and EIS packages.

- `85-00-11-A-102_EIS_Package_Tags.yaml`  
  Semantic tagging of EIS packages (airport category, H₂ infra level, CO₂ battery presence, etc.).

- `85-00-11-A-103_Deprecated_Tags_Register.csv`  
  Register of deprecated tags and their replacements.

### `ASSETS/EIS_Packages/`

- `85-00-11-A-201_EIS_Package_Template.md`  
  Template for describing an ATA 85 EIS package (scope, content, dependencies, constraints).

- `85-00-11-A-202_EIS_Readiness_Checklist.xlsx`  
  Checklist to confirm that infra + documentation + training are ready for EIS.

- `85-00-11-A-203_Reversibility_Rollback_Plan_Template.md`  
  Template for roll-back plans if an EIS deployment must be reverted.

### `ASSETS/Reports/`

- `85-00-11-A-301_EIS_Release_Notes_Template.md`  
  Standard shape for internal/external release notes per EIS drop.

- `85-00-11-A-302_EIS_KPI_Dashboard.xlsx`  
  KPI dashboard: infra readiness, adoption rate per airport, incidents, deviations.

- `85-00-11-A-303_Field_Feedback_Summary_Template.md`  
  Template for consolidating feedback from airports/airlines on ATA 85 interfaces.

---

## CD/Git Tag Mapping Convention

To enable **GenCCC** and **CGen** to auto-link specific CD releases to the ATA 85 configurations, the following convention is used in `85-00-11-A-101_Git_Tags_to_ATA85_Config_Map.csv`.

### Git Tag Syntax

Git tags for ATA 85 infrastructure releases MUST follow this regex pattern:

```regex
v[0-9]+.[0-9]+.[0-9]+-85-[A-Z]+-[A-Z0-9]+
```

**Breakdown:**
1. **`vX.Y.Z`**: Semantic Version of the Interface Standard (e.g., `v2.1.0`).
2. **`-85-`**: Constant identifier for ATA 85.
3. **`[A-Z]+`**: Airport Archetype Code (e.g., `ARCHA`, `ARCHB`).
4. **`[A-Z0-9]+`**: Configuration Variant (e.g., `H2STD`, `H2CO2`).

**Example Tag:** `v02.01.00-85-ARCHA-H2STD`  
*(Interpretation: Version 2.1.0 of ATA 85 standards for Archetype A airports with Standard H₂ fueling interfaces.)*

### CSV Structure (`85-00-11-A-101`)

The CSV file is the "Rosetta Stone" for the automation tools.

| Column Header | Description | Example Value |
| :--- | :--- | :--- |
| **GIT_TAG** | Exact Git tag string (Key) | `v02.01.00-85-ARCHA-H2STD` |
| **ATA85_BASELINE_ID** | The frozen Doc Baseline ID | `BL-85-00-11-004` |
| **EIS_PACKAGE_REF** | Link to the specific EIS pack | `PKG-85-ARCH-A-001` |
| **DPP_SCHEMA_VER** | Digital Product Passport schema version | `v1.4` |
| **COMPATIBILITY_MASK** | Regex for compatible aircraft soft | `^v04\.0[0-9]\..*` |
| **RELEASE_DATE** | ISO 8601 Date | `2025-11-21` |

### Automation Logic

When CGen detects a new Git Tag matching the pattern:
1. It parses the tag.
2. It looks up the row in `85-00-11-A-101`.
3. It retrieves the `EIS_PACKAGE_REF`.
4. It stamps the release artifacts with the correct `ATA85_BASELINE_ID`.

---

## Lifecycle Position (A-LIVE-GP)

- **Lifecycle Stage**: 11 of 14 – **EIS / Versions / Tags**
- **Upstream Inputs**:
  - [85-00-09_Production_Planning](../85-00-09_Production_Planning/README.md) (industrialization of infrastructures)
  - [85-00-10_Certification](../85-00-10_Certification/README.md) (approved interfaces and constraints)
- **Downstream Outputs**:
  - Feeds [85-00-12_Services](../85-00-12_Services/README.md) (support & service models per EIS package)
  - Feeds **00-00-11_EIS_VERSIONS_TAGS** (program-level EIS status)
  - Inputs to **ATA 99** for circularity and sustainability tracking of infra components.

---

## Status

- **Phase**: EIS / Release Management (A-LIVE-GP Stage 11)  
- **Maturity**: `DRAFT` (skeleton – content to be progressively populated)  
- **Last Updated**: 2025-11-21  

---

## Related Folders

Part of the canonical 14-folder lifecycle:
1. [Overview](../85-00-01_Overview/README.md) → 2. [Safety](../85-00-02_Safety/README.md) → 3. [Requirements](../85-00-03_Requirements/README.md) → 4. [Design](../85-00-04_Design/README.md) → 5. [Interfaces](../85-00-05_Interfaces/README.md) → 6. [Engineering](../85-00-06_Engineering/README.md) → 7. [V&V](../85-00-07_V_AND_V/README.md) → 8. [Prototyping](../85-00-08_Prototyping/README.md) → 9. [Production Planning](../85-00-09_Production_Planning/README.md) → 10. [Certification](../85-00-10_Certification/README.md) → **11. EIS/Versions/Tags** → 12. [Services](../85-00-12_Services/README.md) → 13. [Subsystems/Components](../85-00-13_Subsystems_Components/README.md) → 14. [Ops/Std/Sustain](../85-00-14_Ops_Std_Sustain/README.md)

---

## Document Control

- **Standard**: OPT-IN Framework v1.1 (A-LIVE-GP, ATA 85 pattern)  
- **Folder Owner**: ATA 85 EIS & Configuration Lead  
- **Change Authority**: Infrastructure Interfaces CCB (I-CCB-85)  
- **Repository**: `AMPEL360-BWB-H2-Hy-E`
- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT** – Subject to human review and approval.
- Human approver: *[to be completed]*.
- Last AI update: *2025-11-21*.
