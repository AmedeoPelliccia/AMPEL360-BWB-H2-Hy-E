# 95-90-00-001 — Tables, Schemas, Diagrams Overview

## 1. Purpose

This document provides an overview of the **Tables, Schemas, and Diagrams** structure within ATA 95 (Digital Product Passport and Neural Networks). This cross-ATA bucket consolidates all data models, schemas, taxonomies, traceability tables, and diagrams used across the DPP and NN systems.

## 2. Scope

The 95-90 bucket encompasses:

- **Global reference taxonomies**: Functional classifications, ATA/OPT-IN mappings, and labeling schemes
- **Global data schemas**: Common entities (aircraft, flight, segment), time-series, events, and evidence records
- **Global interface schemas**: REST/gRPC contracts, message bus topics, and file exchange formats
- **Global traceability tables**: Requirements-to-design, design-to-V&V mappings, and DPP traceability views
- **Regulatory and standards tables**: EASA/FAA AI requirements, DO-178/DO-330/DO-331 mappings, EU AI Act compliance
- **Diagram library and styles**: Notation guides, symbol libraries, abstraction levels, and viewpoint catalogs
- **Test data and benchmark tables**: Benchmark scenarios, dataset splits, KPI definitions
- **ATA-specific tables**: ECS (ATA 21), H₂ (ATA 28), IMA (ATA 42), Energy (ATA 80)

## 3. Organization

```
95-90_Tables_Schemas_Diagrams/
├── 00_META/                                              # Metadata, taxonomy, and governance
├── 95-90-01_Global_Reference_Taxonomies/                # Functional taxonomies and mappings
├── 95-90-02_Global_Data_Schemas/                        # Common entity and telemetry schemas
├── 95-90-03_Global_Interface_Schemas/                   # API and message schemas
├── 95-90-04_Global_Traceability_Tables/                 # Requirements and V&V traceability
├── 95-90-05_Regulatory_and_Standards_Tables/            # Compliance mappings
├── 95-90-06_Diagram_Library_and_Styles/                 # Diagram standards and templates
├── 95-90-07_Test_Data_and_Benchmark_Tables/             # Test scenarios and datasets
├── 95-90-21_ECS_Tables_Schemas_Diagrams/                # ATA 21 – ECS specific
├── 95-90-28_H2_and_Fuel_Tables_Schemas_Diagrams/        # ATA 28 – H₂ specific
├── 95-90-42_IMA_and_Avionics_Tables_Schemas_Diagrams/   # ATA 42 – IMA specific
└── 95-90-80_Energy_Tables_Schemas_Diagrams/             # ATA 80 – Energy specific
```

## 4. Key Principles

### 4.1 Single Source of Truth
All schemas, taxonomies, and tables are maintained in this bucket as the authoritative source. Other ATA chapters reference these definitions.

### 4.2 Versioning
All schemas and tables follow semantic versioning (e.g., `v1.0`, `v1.1`, `v2.0`) and maintain backward compatibility where possible.

### 4.3 Traceability
Every schema and table links to:
- Requirements (95-00-03)
- Design documents (95-00-04)
- Interfaces (95-00-05)
- V&V artifacts (95-00-07)

### 4.4 Cross-ATA Integration
Tables and schemas in this bucket support integration across ATA chapters, particularly:
- **95-20**: Subsystems (references schemas)
- **95-30**: Methods & Algorithms (uses data models)
- **95-40**: Software (implements interfaces)
- **95-50**: Hardware (hardware schemas)
- **95-60**: Storage (storage schemas)
- **95-80**: Energy (energy models)

## 5. Usage Guidelines

### 5.1 Creating New Schemas
1. Follow naming conventions (see 95-90-00-002)
2. Register in 95-90-00-006_Tables_Schemas_Registry.json
3. Document in appropriate subdirectory README
4. Add ASSETS files in JSON/CSV/drawio format
5. Link to requirements and design docs

### 5.2 Updating Existing Schemas
1. Increment version number
2. Document changes in schema file header
3. Update registry with new version
4. Maintain backward compatibility or document breaking changes
5. Update dependent systems

### 5.3 Creating Diagrams
1. Use templates from 95-90-06_Diagram_Library_and_Styles
2. Follow notation and style guide
3. Export to .drawio and .svg/.png formats
4. Document diagram purpose and context

## 6. Cross-References

### 6.1 Internal Links
- **Meta**: [00_META/](00_META/)
- **Taxonomies**: [95-90-01_Global_Reference_Taxonomies/](95-90-01_Global_Reference_Taxonomies/)
- **Data Schemas**: [95-90-02_Global_Data_Schemas/](95-90-02_Global_Data_Schemas/)
- **Interface Schemas**: [95-90-03_Global_Interface_Schemas/](95-90-03_Global_Interface_Schemas/)
- **Traceability**: [95-90-04_Global_Traceability_Tables/](95-90-04_Global_Traceability_Tables/)
- **Regulatory**: [95-90-05_Regulatory_and_Standards_Tables/](95-90-05_Regulatory_and_Standards_Tables/)
- **Diagrams**: [95-90-06_Diagram_Library_and_Styles/](95-90-06_Diagram_Library_and_Styles/)
- **Test Data**: [95-90-07_Test_Data_and_Benchmark_Tables/](95-90-07_Test_Data_and_Benchmark_Tables/)

### 6.2 External Links
- **Requirements**: [95-00-03_Requirements/](../95-00_GENERAL/95-00-03_Requirements/)
- **Design**: [95-00-04_Design/](../95-00_GENERAL/95-00-04_Design/)
- **Interfaces**: [95-00-05_Interfaces/](../95-00_GENERAL/95-00-05_Interfaces/)
- **V&V**: [95-00-07_Verification_Validation/](../95-00_GENERAL/95-00-07_Verification_Validation/)
- **Software**: [95-40_Software/](../95-40_Software/)
- **Storage**: [95-60_Storage/](../95-60_Storage/)

## 7. Maintenance

### 7.1 Ownership
- **Owner**: AMPEL360 Data Architecture WG
- **Reviewers**: Systems Engineering, Software, Certification teams
- **Approval**: Chief Architect, Certification Manager

### 7.2 Review Cycle
- **Quarterly**: Review schema versions and registry
- **As-needed**: When new requirements or systems are added
- **Pre-release**: Comprehensive review before major releases

## 8. Status

- **Document ID**: 95-90-00-001
- **Version**: 1.0
- **Status**: ACTIVE
- **Last Updated**: 2025-11-17
- **Owner**: AMPEL360 Data Architecture WG

---

## Document Control

- **Standard**: OPT-IN Framework v1.2
- **ATA Chapter**: 95 (Digital Product Passport and Neural Networks)
- **Bucket**: 90_Tables_Schemas_Diagrams
