---
Title: "Document Structure & References — ATA 02 General"
Identifier: "AMPEL360-02-00-01-003A"
Version: "1.0.0"
Status: "Draft"
AccessLevel: "Internal"
Author: "AMPEL360 Documentation Team"
CreatedAt: "2025-11-13"
ModifiedAt: "2025-11-13"
Abstract: "Defines how ATA 02 documentation is structured within AMPEL360 and lists the authoritative references that govern content organization and formatting."
Keywords: ["Structure", "References", "Standards", "ATA 02", "Documentation"]
---

# Document Structure & References

This document describes how ATA 02 documentation is structured in AMPEL360, which standards it conforms to, and the rules for file metadata, naming, and cross-referencing.

## 1. Structure

### 1.1 General Layer (`02-00_GENERAL`)

The **General Layer** (`02-00_GENERAL`) is the root governance layer for ATA 02. It contains:

- **Governance & Policy**  
  - Documentation governance and ownership  
  - Change management and approval rules  

- **Safety & Compliance**  
  - Safety principles and constraints  
  - Regulatory alignment and certification basis (where applicable)  

- **Requirements & Lifecycle**  
  - High-level functional and non-functional requirements  
  - Lifecycle stages and maturity criteria  

- **EIS / Versioning Rules**  
  - Entry-into-service (EIS) policies  
  - Versioning, baselining, and release conventions for ATA 02 documents  

- **Services, Subsystems & Components Index**  
  - Index of services, subsystems, and components referenced from ATA 02  
  - Canonical identifiers and naming rules  

- **Operations Standards & Sustainability**  
  - Operational standards and constraints  
  - Sustainability and circularity principles applicable across all buckets  

> The General Layer defines the *rules and references* for the entire ATA 02 tree. Detailed lifecycle content and implementation details reside in the subordinate buckets, not here.

### 1.2 Root Buckets at Chapter Root

At the chapter root for ATA 02, the following **root buckets** are defined. Each bucket is a top-level folder and may contain its own substructure and deliverables.

- `02-10_Operations`  
  Operational concepts, procedures, use cases, and operating constraints.

- `02-20_Subsystems`  
  Subsystem breakdown, interfaces, and behavioral models.

- `02-30_Circularity`  
  Circularity, re-use, recycling, end-of-life strategies, and related metrics.

- `02-40_Software`  
  Software architecture, components, interfaces, and software-specific standards.

- `02-50_Structures`  
  Physical structures, layout, and structure-related constraints.

- `02-60_Storages`  
  Storage systems (energy, data, materials) and associated interfaces.

- `02-70_Propulsion`  
  Propulsion-related elements, performance envelopes, and constraints.

- `02-80_Energy`  
  Energy generation, distribution, conversion, and management models.

- `02-90_Tables_Schemas_Diagrams`  
  Shared tables, data schemas, canonical diagrams, and reference visual artefacts.

> Each bucket owns *its* detailed content. The General Layer only references and governs it.

## 2. Authoritative References

ATA 02 documentation in AMPEL360 is governed by the following references:

1. **ATA iSpec 2200**  
   - Basis for content structuring and ATA chapter/section numbering.  
   - Defines how technical content is categorized and referenced.

2. **S1000D**  
   - Basis for modular, data-module–oriented publishing.  
   - Influences how content is broken down into reusable units and managed across products/programs.

3. **AMPEL360 Documentation Standard v1.1**  
   - Internal standard defining:
     - Front-matter metadata schema  
     - File naming conventions  
     - Folder structure patterns  
     - Cross-linking and traceability rules  

4. **Program-Specific References (As Applicable)**  
   - Program or customer-specific documentation policies  
   - Additional regulatory or industry standards mandated by a program  
   - These must be explicitly listed in relevant program-level documents and cross-referenced from the ATA 02 General Layer where they impact structure or numbering.

## 3. Conformance

All ATA 02 documents **must** conform to the following:

### 3.1 Metadata Front-Matter

- Every file includes **metadata front-matter** at the top of the file.  
- At minimum, the front-matter must contain:
  - `Title`  
  - `Identifier`  
  - `Version`  
  - `Status`  
  - `AccessLevel`  
  - `Author`  
  - `CreatedAt`  
  - `ModifiedAt`  
  - `Abstract`  
- Additional fields may be defined in the AMPEL360 Documentation Standard v1.1 for specific document types.

### 3.2 Naming Rules

- File and folder names:
  - Must follow the **ATA chapter/section numbering** conventions derived from ATA iSpec 2200.  
  - Must follow the **AMPEL360 Documentation Standard v1.1** naming rules (including permitted characters, casing, and separators).  
- Identifiers such as `AMPEL360-02-XX-YY-ZZZ?` must be unique and traceable to their position in the hierarchy.

### 3.3 Cross-Linking and Content Location

- Cross-link **to subordinate folders** (i.e., from `02-00_GENERAL` to the relevant `02-10_…` / `02-20_…` buckets), rather than duplicating content.
- Do **not** duplicate lifecycle or implementation content inside the General Layer:
  - The General Layer may describe *what* content must exist and *where* it resides, but not re-embed that content.
- Shared artefacts (tables, schemas, diagrams) must be located under `02-90_Tables_Schemas_Diagrams` and referenced from other buckets, not copied.

### 3.4 Consistency and Traceability

- Any deviation from these rules must be:
  - Explicitly justified in a **Deviation or Waiver** record; and  
  - Linked from the impacted documents’ front-matter (e.g., in a `Deviations` or `Notes` field).
- Changes to structure or references must update:
  - This ATA 02 General document, and  
  - Any impacted cross-links or indices.

---

## 4. Change & Extension Guidelines (For Authors)

When extending ATA 02 documentation:

1. **Determine the correct bucket** based on the primary content type (operations, subsystem, software, etc.).  
2. **Create or update front-matter** using the canonical schema from AMPEL360 Documentation Standard v1.1.  
3. **Assign identifiers and filenames** that follow:
   - ATA iSpec 2200 numbering; and  
   - AMPEL360 naming rules.  
4. **Cross-link instead of duplicating**:
   - Reference existing tables, schemas, or diagrams in `02-90_…` where applicable.  
5. **Update indices**:
   - If you add a new service, subsystem, or component, update the relevant index in `02-00_GENERAL`.
