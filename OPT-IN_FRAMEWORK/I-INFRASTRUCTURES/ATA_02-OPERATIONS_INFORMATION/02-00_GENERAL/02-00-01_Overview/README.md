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
Abstract: "Introduces ATA 02 Operations Information general layer, its scope and positioning within the OPT-IN I-axis, and links to safety, requirements, and certification content."
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

This overview orients contributors to **ATA 02 — Operations Information** and the **02-00 General** layer. It defines scope, applicability, and the organizing principles used across the chapter, aligned with the AMPEL360 **OPT-IN** framework (**I — Infrastructures**) and the canonical `XX-00_GENERAL` standard.

It is the canonical entry point into the ATA 02 General layer and should be referenced by all ATA 02 governance, safety, requirements, and certification documents.

## 2. Position in OPT-IN

- **Axis:** I — Infrastructures (airports, supply chains, facilities, operations)  
- **Chapter:** ATA 02 — Operations Information  
- **Role:** Provide the operational information backbone (ground/flight operations constraints, procedures, turnarounds, operational limits, and linkages to infrastructure and services) across the I-axis.

ATA 02 acts as the **operations-facing integration layer** between technical ATA chapters and infrastructure/airport realities, ensuring that cross-system operational constraints are visible and actionable.

## 3. Scope — What belongs under ATA 02

ATA 02 content focuses on operational information that:

- **Spans systems** and supports **safe, efficient operation**, including:
  - Turnaround and ground handling data  
  - Operating envelopes and limitations  
  - Environmental and airport constraints  
  - Handling and servicing rules  
  - Operational boundaries and conditions-of-use  
- **Integrates** information from multiple technical ATAs into coherent operations views:
  - Linkages to ATA 21/24/28/32/49/etc. for ops-relevant behavior  
  - Interfaces with services, infrastructure, and ground systems  

ATA 02 **does not**:

- Duplicate detailed technical design content (e.g., detailed schematics, internal logic, component-level design justifications).  
- Replace the owning technical ATA chapter for authoritative technical data.

Instead, ATA 02 **links to, indexes, and contextualizes** these technical sources for operations, making them usable by operations stakeholders (airlines, airports, maintenance, safety).

## 4. Relationship to the ATA 02 chapter structure

### 4.1 General Layer (`02-00_GENERAL`)

The **General** layer (`02-00_GENERAL`) owns:

- Governance and chapter-wide rules  
- Cross-ATA safety principles and references  
- Operations-related requirements and traceability views  
- Certification strategy and evidence mapping for ops content  
- Configuration, versioning, and change policies for ATA 02  
- Indices for services, subsystems, components, and standards  
- Sustainability and operations standards applicable across the chapter  

It defines **what must exist and how it is governed**, not the detailed implementation.

### 4.2 Root Buckets (chapter root)

The following **root buckets** exist at the ATA 02 chapter root:

- `02-10_Operations`  
- `02-20_Subsystems`  
- `02-30_Circularity`  
- `02-40_Software`  
- `02-50_Structures`  
- `02-60_Storages`  
- `02-70_Propulsion`  
- `02-80_Energy`  
- `02-90_Tables_Schemas_Diagrams`  

Each bucket is a **design- and content-driven tree** that:

- Owns detailed, reusable content (procedures, models, schemas, diagrams, etc.).  
- Is referenced by governance and lifecycle views in `02-00_GENERAL`.  
- May be reused or cross-referenced by other ATAs where appropriate.

### 4.3 Lifecycle views vs. buckets

- The **`02-00-01` to `02-00-14`** range provides **lifecycle-oriented views** (safety, requirements, design, interfaces, V&V, certification, etc.) within `02-00_GENERAL`.  
- The **root buckets** (`02-10_…` to `02-90_…`) provide **content repositories** that lifecycle views reference.

**Rule:**  
There is **no 01–14 lifecycle tree duplication inside buckets**. Buckets remain design/content-driven trees. Lifecycle perspectives are expressed in `02-00_GENERAL` and **link into** buckets.

## 5. Standards & compliance

ATA 02 General content must comply with:

- **ATA iSpec 2200**  
  - Governs ATA chapter/section numbering and technical content categorization.

- **S1000D**  
  - Governs modular, data-module–oriented structuring and reuse where applicable.

- **AMPEL360 Doc Standard v1.1**  
  - Governs:
    - Metadata front-matter schema  
    - File naming conventions and identifiers  
    - Folder hierarchy patterns  
    - Cross-linking and traceability rules across OPT-IN axes and ATAs  

Any additional program-specific or authority-specific standards must be listed in the relevant `02-00_GENERAL` governance documents and cross-referenced from here where they affect ATA 02 structure or obligations.

## 6. Quick links (workbench)

The following documents implement the `02-00_GENERAL` pattern for ATA 02:

- **Purpose & Scope**  
  → `./02-00-01-001A_Purpose_Scope.md`

- **Applicability Matrix**  
  → `./02-00-01-002A_Applicability_Matrix.md`

- **Document Structure & References**  
  → `./02-00-01-003A_Document_Structure_References.md`

- **Roles & Responsibilities**  
  → `./02-00-01-004A_Roles_Responsibilities.md`

- **Subordinate Chapters Index**  
  → `./02-00-01-005A_Subordinate_Chapters_Index.md`

These files together define how ATA 02 is governed, who is responsible for what, how content is organized, and how to navigate to subordinate lifecycle folders and root buckets.

---

## 7. Usage guidelines for contributors

When creating or updating ATA 02 content:

1. **Start here** to identify:
   - Whether your content belongs in `02-00_GENERAL` or in a root bucket.  
   - Which lifecycle view (safety, requirements, certification, etc.) applies.

2. **Follow the governance docs**:
   - Use the **Document Structure & References** and **Roles & Responsibilities** documents to apply the correct structure and approvals.

3. **Place detailed content in buckets**:
   - Put detailed operational procedures, models, schemas, or diagrams in the correct `02-10_…` to `02-90_…` bucket;  
   - Reference them from lifecycle documents rather than duplicating content.

4. **Maintain traceability**:
   - Ensure links to safety analyses, requirements, and certification evidence are maintained using the patterns defined in `02-00_GENERAL`.

---
