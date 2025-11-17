# 95-90-00-004 — Tables and Schemas Taxonomy

## 1. Purpose

This document defines the **hierarchical taxonomy** for organizing all tables, schemas, and diagrams in the 95-90 bucket, ensuring consistent classification and discovery.

## 2. Taxonomy Structure

### 2.1 Top-Level Categories

```
Tables_Schemas_Diagrams/
├── META                    # Governance and metadata
├── TAXONOMIES              # Classification and mapping
├── DATA_SCHEMAS            # Entity and data models
├── INTERFACE_SCHEMAS       # API and message contracts
├── TRACEABILITY           # Requirements and V&V mappings
├── REGULATORY              # Compliance and standards
├── DIAGRAMS                # Visual representations
├── TEST_DATA               # Benchmarks and datasets
└── ATA_SPECIFIC            # Domain-specific schemas
```

### 2.2 Schema Types Taxonomy

```
Schema Types
├── Entity Schemas          # Represent domain objects
│   ├── Aircraft
│   ├── Flight
│   ├── Component
│   ├── Segment
│   └── Asset
├── Event Schemas           # Represent occurrences
│   ├── Telemetry Event
│   ├── Alert Event
│   ├── Maintenance Event
│   └── Audit Event
├── Time-Series Schemas     # Represent sequential data
│   ├── Sensor Data
│   ├── Performance Metrics
│   └── Energy Consumption
├── Interface Schemas       # API contracts
│   ├── REST API
│   ├── gRPC
│   ├── GraphQL
│   └── Message Bus
└── Aggregate Schemas       # Compositions
    ├── Flight Profile
    ├── Mission Data
    └── DPP Complete
```

### 2.3 Table Types Taxonomy

```
Table Types
├── Reference Tables        # Static lookup data
│   ├── ATA Chapter Codes
│   ├── Airport Codes
│   ├── Aircraft Types
│   └── Component Types
├── Mapping Tables          # Cross-references
│   ├── ATA to OPT-IN
│   ├── Requirement to Design
│   ├── Design to V&V
│   └── Standard to Requirement
├── Configuration Tables    # System settings
│   ├── IMA Partitions
│   ├── Bus Configuration
│   ├── Sensor Calibrations
│   └── Safety Thresholds
└── Traceability Tables     # Audit trails
    ├── Change History
    ├── Approval Records
    └── Compliance Evidence
```

### 2.4 Diagram Types Taxonomy

```
Diagram Types
├── Structural Diagrams     # Static architecture
│   ├── Component Diagrams
│   ├── Deployment Diagrams
│   ├── Class Diagrams
│   └── ER Diagrams
├── Behavioral Diagrams     # Dynamic behavior
│   ├── Sequence Diagrams
│   ├── State Machines
│   ├── Activity Diagrams
│   └── Flowcharts
├── Physical Diagrams       # Physical layout
│   ├── P&ID (Piping & Instrumentation)
│   ├── Wiring Diagrams
│   └── Layout Diagrams
└── Conceptual Diagrams     # High-level views
    ├── Context Diagrams
    ├── Architecture Overviews
    └── Mission Profiles
```

## 3. Classification Dimensions

### 3.1 By Domain

| Domain | Code | Description | Examples |
|--------|------|-------------|----------|
| Global | GLB | Cross-ATA, universal | Aircraft schema, Flight schema |
| ECS | ECS | Environmental Control System | ATA 21 sensors, control states |
| H₂ | H2 | Hydrogen fuel systems | ATA 28 tanks, safety sensors |
| IMA | IMA | Integrated Modular Avionics | ATA 42 partitions, AFDX VLs |
| Energy | ENR | Energy systems | ATA 80 energy balance, KPIs |

### 3.2 By Lifecycle Phase

| Phase | Code | Description |
|-------|------|-------------|
| Requirements | REQ | Requirements traceability |
| Design | DES | Design models and specs |
| Implementation | IMP | Implementation artifacts |
| Verification | VER | V&V data and results |
| Operation | OPS | Operational data models |
| Maintenance | MNT | Maintenance records |

### 3.3 By Abstraction Level

| Level | Description | Examples |
|-------|-------------|----------|
| L0 - Physical | Hardware, sensors, actuators | Tank sizing, sensor maps |
| L1 - Logical | Data structures, interfaces | Schemas, API contracts |
| L2 - Conceptual | Requirements, taxonomies | Functional taxonomy, classifications |
| L3 - Meta | Governance, standards | Naming rules, versioning |

### 3.4 By Status

| Status | Description | Usage |
|--------|-------------|-------|
| DRAFT | Under development | Initial creation, review pending |
| FOR_REVIEW | Ready for review | Peer review in progress |
| APPROVED | Approved for use | Baseline, operational |
| DEPRECATED | Marked for removal | Use discouraged, migration available |
| ARCHIVED | No longer in use | Historical reference only |

## 4. Tagging Conventions

### 4.1 Metadata Tags

All schemas and tables should include metadata tags:

```json
{
  "metadata": {
    "id": "aircraft_schema",
    "type": "entity_schema",
    "domain": "GLB",
    "lifecycle_phase": "OPS",
    "abstraction_level": "L1",
    "status": "APPROVED",
    "version": "1.2.0",
    "tags": ["aircraft", "flight", "core", "dpp"]
  }
}
```

### 4.2 Search Keywords

Each document should include search keywords:
- **Primary domain**: Main classification
- **Secondary domains**: Related areas
- **Data types**: Types of data represented
- **Usage context**: Where it's used

## 5. Discovery and Navigation

### 5.1 Index Files

Each subdirectory maintains an index:
- **README.md**: Human-readable overview
- **INDEX.csv**: Machine-readable catalog
- **Registry entry**: In 95-90-00-006_Tables_Schemas_Registry.json

### 5.2 Cross-Reference Graph

The taxonomy supports a cross-reference graph:
```
Aircraft Schema (GLB)
├── Used by → Flight Schema
├── Referenced in → DPP Complete
├── Implements → RQ-95-00-03-001
└── Related to → H₂ Tank Schema (H2)
```

## 6. Extension Mechanism

### 6.1 Adding New Categories

To add a new top-level category:
1. Propose to Data Architecture WG
2. Document purpose and scope
3. Create subdirectory and README
4. Update this taxonomy document
5. Update registry and index files

### 6.2 Adding New Schema Types

To add a new schema type:
1. Identify parent category
2. Follow naming conventions
3. Document schema structure
4. Add examples
5. Register in taxonomy

## 7. Compliance

### 7.1 Mandatory Tags

All schemas must include:
- `type`: Schema type from taxonomy
- `domain`: Domain code
- `status`: Current status
- `version`: Semantic version

### 7.2 Validation

The taxonomy is enforced by:
- CI validation checks
- Schema validation tools
- Registry consistency checks

## 8. Cross-References

### 8.1 Related Documents
- [Usage Rules and Conventions](../95-90-00-002_Usage_Rules_and_Conventions.md)
- [Schema Registry](95-90-00-006_Tables_Schemas_Registry.json)
- [Naming and Versioning Rules](95-90-00-005_Naming_and_Versioning_Rules.md)

### 8.2 Related Standards
- **JSON Schema**: http://json-schema.org/
- **OPT-IN Framework**: [OPT-IN_FRAMEWORK_STANDARD.md](../../../../../OPT-IN_FRAMEWORK_STANDARD.md)
- **ATA iSpec 2200**: Industry standard for technical documentation

## 9. Status

- **Document ID**: 95-90-00-004
- **Version**: 1.0
- **Status**: ACTIVE
- **Last Updated**: 2025-11-17
- **Owner**: AMPEL360 Data Architecture WG

---

## Document Control

- **Standard**: OPT-IN Framework v1.2
- **ATA Chapter**: 95 (Digital Product Passport and Neural Networks)
- **Bucket**: 90_Tables_Schemas_Diagrams
