---
Title: "ATA 02 — 02-00-01 Overview"
Identifier: "AMPEL360-02-00-01_OVR"
Version: "1.0.0"
Status: "Draft"
AccessLevel: "Internal"
Author: "AMPEL360 Documentation Team"
CreatedAt: "2025-11-13"
ModifiedAt: "2025-11-13"
Scope: "Overview for ATA 02-00 General layer within I-INFRASTRUCTURES"
Abstract: "Introduces ATA 02 Operations Information general layer, scope, positioning within OPT-IN I-axis, and links to safety, requirements, and certification."
Keywords: ["ATA 02", "Operations Information", "General", "Overview", "OPT-IN", "I-Infrastructures"]
Compliance:
  - "ATA iSpec 2200"
  - "S1000D"
  - "AMPEL360 Doc Standard v1.1"
Links:
  ParentGeneral: "../"
  Siblings:
    - "../02-00-02_Safety/"
    - "../02-00-03_Requirements/"
    - "../02-00-04_Design/"
    - "../02-00-05_Interfaces/"
    - "../02-00-06_Engineering/"
    - "../02-00-07_V_AND_V/"
    - "../02-00-08_Prototyping/"
    - "../02-00-09_Production_Planning/"
    - "../02-00-10_Certification/"
    - "../02-00-11_EIS_Versions_Tags/"
    - "../02-00-12_Services/"
    - "../02-00-13_Subsystems_Components/"
    - "../02-00-14_Ops_Std_Sustain/"
  CrossATABuckets:
    - "../../02-10_Operations/"
    - "../../02-20_Subsystems/"
    - "../../02-30_Circularity/"
    - "../../02-40_Software/"
    - "../../02-50_Structures/"
    - "../../02-60_Storages/"
    - "../../02-70_Propulsion/"
    - "../../02-80_Energy/"
    - "../../02-90_Tables_Schemas_Diagrams/"
ChangeLog:
  - {version: "1.0.0", date: "2025-11-13", author: "AMPEL360 Documentation Team", change: "Initial creation"}
---

# 02-00-01 — Overview (ATA 02: Operations Information)

## 1. Purpose
This overview orients contributors to **ATA 02 — Operations Information** and the **02-00 General** layer. It defines scope, applicability, and the organizing principles used across the chapter, aligned with the AMPEL360 **OPT-IN** framework (I-INFRASTRUCTURES) and the canonical `XX-00_GENERAL` standard.

## 2. Position in OPT-IN
- **Axis:** I — Infrastructures (airports, supply chains, facilities, operations)
- **Chapter:** ATA 02 — Operations Information
- **Role:** Provide the operational information backbone (ground/flight operations constraints, procedures, turnarounds, operational limits, and linkages to infrastructure and services).

## 3. What belongs under ATA 02
- Operational information that **spans systems** and supports **safe, efficient operation**: turnaround data, operating envelopes, environmental/airport constraints, handling rules, servicing boundaries, and cross-references to more detailed ATA domains.
- Chapter **does not** duplicate technical design content—those remain in their technical ATA chapters; ATA 02 **links** and contextualizes them for operations.

## 4. How ATA 02 relates to the chapter structure
- The **General** layer (`02-00_GENERAL`) owns governance, safety, requirements, certification strategy, and configuration/change policies for the chapter.
- Root **buckets** present in ATA 02: `02-10_Operations`, `02-20_Subsystems`, `02-30_Circularity`, `02-40_Software`, `02-50_Structures`, `02-60_Storages`, `02-70_Propulsion`, `02-80_Energy`, `02-90_Tables_Schemas_Diagrams`.
- **No 01–14 lifecycle duplication** inside buckets. Buckets are design-driven trees referencing this General layer.

## 5. Related standards & compliance
- **ATA iSpec 2200** for content and numbering
- **S1000D** for modular publications
- **AMPEL360 Doc Standard v1.1** for mandatory structure and traceability

## 6. Quick links (workbench)
- Purpose & Scope → `./02-00-01-001A_Purpose_Scope.md`
- Applicability Matrix → `./02-00-01-002A_Applicability_Matrix.md`
- Document Structure & References → `./02-00-01-003A_Document_Structure_References.md`
- Roles & Responsibilities → `./02-00-01-004A_Roles_Responsibilities.md`
- Subordinate Chapters Index → `./02-00-01-005A_Subordinate_Chapters_Index.md`
