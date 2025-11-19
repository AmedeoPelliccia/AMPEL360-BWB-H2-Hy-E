# 95-10-00-01-003 Operations Taxonomy

## Document Information

- **Document ID**: 95-10-00-01-003
- **Title**: Operations Taxonomy for Neural Networks and DPP
- **Version**: 1.0
- **Date**: 2025-11-17
- **Status**: Active
- **Category**: META - Operations
- **ATA Chapter**: 95 - Digital Product Passport and Neural Networks

## Purpose

This document establishes a comprehensive taxonomy for categorizing, organizing, and referencing operational activities, documents, and artifacts related to Neural Network systems and the Digital Product Passport.

## Taxonomy Structure

### Level 1: Operational Domains

```
95-10_Operations
├── 00_META (Metadata and Cross-References)
├── 01_FLIGHT_OPERATIONS
├── 02_MAINTENANCE_OPERATIONS
├── 03_GROUND_OPERATIONS
├── 04_DATA_OPERATIONS
├── 05_AI_OPERATIONS_AND_MLOPS_IN_SERVICE
├── 06_SAFETY_CRITICAL_OPERATIONS
├── 07_ABNORMAL_AND_EMERGENCY_USE
├── 08_TRAINING_AND_SIMULATION_OPERATIONS
├── 09_FLEET_AND_AIRLINE_INTEGRATION
├── 10_OPERATIONS_MONITORING_AND_FEEDBACK
├── 11_DPP_IN_OPERATIONS
├── 12_SECURITY_AND_PRIVACY_IN_OPERATIONS
├── 13_ENVIRONMENTAL_AND_CIRCULARITY_OPS
└── 14_CONTINUOUS_IMPROVEMENT_AND_GOVERNANCE_IN_OPS
```

### Level 2: Document Types

Within each operational domain, documents are categorized by type:

#### A. Procedural Documents
- **Procedures**: Step-by-step instructions for operational tasks
- **Checklists**: Verification lists for critical operations
- **Workflows**: Process flows and decision trees
- **Guidelines**: Best practices and recommendations

#### B. Reference Documents
- **Overviews**: High-level descriptions and summaries
- **Use Cases**: Specific operational scenarios
- **Integration Specs**: Interface and integration details
- **Link Documents**: Cross-references to related materials

#### C. Technical Artifacts
- **Diagrams**: Visual representations (drawio, svg)
- **Data Specifications**: JSON/CSV schemas and templates
- **Dashboards**: Monitoring and reporting interfaces
- **Templates**: Reusable document and data templates

### Level 3: Operational Phases

Operations are further categorized by phase in the operational lifecycle:

```
Phase 0: Pre-Operations (Planning, Briefing, Setup)
Phase 1: Normal Operations (Standard procedures)
Phase 2: Abnormal Operations (Non-standard but managed)
Phase 3: Emergency Operations (Critical situations)
Phase 4: Post-Operations (Debrief, Data Capture, Analysis)
```

## Document Naming Convention

### Standard Format

All operational documents follow the ATA-style naming convention:

```
95-10-XX-YY-ZZZ_Description.ext
│  │  │  │  │   │             └─── File extension
│  │  │  │  │   └─────────────── Descriptive name (PascalCase with underscores)
│  │  │  │  └──────────────────── Sequential number (001-999)
│  │  │  └─────────────────────── Sub-category (00-99)
│  │  └────────────────────────── Category (00-14)
│  └───────────────────────────── Bucket (10 = Operations)
└──────────────────────────────── ATA Chapter (95)
```

### Examples

- `95-10-01-01-001_Flight_Ops_Use_of_NN_Systems.md` → Flight Operations, category 01, document 001
- `95-10-02-01-A-001_Maint_Op_Flowchart.drawio` → Maintenance Operations, ASSET 001
- `95-10-00-01-005_Operational_Roles_Registry.json` → META, registry in JSON format

### Asset Naming

Assets (diagrams, templates, data files) include an "A" suffix in the category:

```
95-10-XX-YY-A-ZZZ_Description.ext
             └─── "A" indicates ASSET
```

## Operational Categories

### 00_META - Metadata and Cross-References

**Purpose**: Organizational and navigational documents

**Subcategories**:
- `00-01`: Taxonomy and classification
- `00-02`: Traceability matrices
- `00-03`: Registries and catalogs
- `00-04`: Cross-reference documents
- `00-05`: Integration hooks (CAOS, DPP)

### 01_FLIGHT_OPERATIONS - Flight Operations

**Purpose**: Documents for flight crew and flight-related operations

**Subcategories**:
- `01-01`: Normal flight procedures with NN systems
- `01-02`: Abnormal flight procedures
- `01-03`: Emergency flight procedures
- `01-04`: Flight crew responsibilities
- `01-05`: Links to FCOM/FCTM/OM

### 02_MAINTENANCE_OPERATIONS - Maintenance Operations

**Purpose**: Documents for maintenance personnel and maintenance activities

**Subcategories**:
- `02-01`: Predictive maintenance procedures
- `02-02`: Component health monitoring
- `02-03`: Integration with ATA 05/45
- `02-04`: Maintenance tasks and intervals
- `02-05`: Maintenance data feedback

### 03_GROUND_OPERATIONS - Ground Operations

**Purpose**: Documents for ground handling and turnaround operations

**Subcategories**:
- `03-01`: Turnaround procedures
- `03-02`: Ramp operations
- `03-03`: Ground safety with NN
- `03-04`: GSE integration
- `03-05`: Ground data capture

### 04_DATA_OPERATIONS - Data Operations

**Purpose**: Documents for data management and operations

**Subcategories**:
- `04-01`: Data strategy and flows
- `04-02`: Data quality monitoring
- `04-03`: Data retention policies
- `04-04`: Data engineering links
- `04-05`: Data governance

### 05_AI_OPERATIONS_AND_MLOPS_IN_SERVICE - AI/MLOps

**Purpose**: Documents for AI model deployment and operations

**Subcategories**:
- `05-01`: Model deployment procedures
- `05-02`: Runtime configuration
- `05-03`: Operational rules for updates
- `05-04`: Model monitoring
- `05-05`: MLOps integration

### 06_SAFETY_CRITICAL_OPERATIONS - Safety-Critical Operations

**Purpose**: Documents for safety-critical operational procedures

**Subcategories**:
- `06-01`: Safety boundaries and criteria
- `06-02`: Safety monitors
- `06-03`: Override procedures
- `06-04`: Safety roles and accountability
- `06-05`: Safety integration

### 07_ABNORMAL_AND_EMERGENCY_USE - Abnormal/Emergency Operations

**Purpose**: Documents for non-normal and emergency situations

**Subcategories**:
- `07-01`: Abnormal use cases
- `07-02`: Emergency procedures with NN
- `07-03`: Fallback to conventional systems
- `07-04`: Event recording and analysis
- `07-05`: Links to QRH and safety tests

### 08_TRAINING_AND_SIMULATION_OPERATIONS - Training

**Purpose**: Documents for training programs and simulation

**Subcategories**:
- `08-01`: Training programs and curricula
- `08-02`: Simulator use of NN models
- `08-03`: Training scenarios
- `08-04`: Competence assessment
- `08-05`: Training integration

### 09_FLEET_AND_AIRLINE_INTEGRATION - Fleet/Airline Integration

**Purpose**: Documents for airline and fleet-specific operations

**Subcategories**:
- `09-01`: Airline integration strategy
- `09-02`: Fleet management use cases
- `09-03`: Operator-specific profiles
- `09-04`: Operational agreements/SLAs
- `09-05`: Fleet integration

### 10_OPERATIONS_MONITORING_AND_FEEDBACK - Monitoring

**Purpose**: Documents for operational monitoring and feedback

**Subcategories**:
- `10-01`: Monitoring strategy and KPIs
- `10-02`: Dashboards and reporting
- `10-03`: Feedback channels
- `10-04`: Incident feedback to engineering
- `10-05`: Continuous improvement

### 11_DPP_IN_OPERATIONS - DPP Operations

**Purpose**: Documents for DPP use in day-to-day operations

**Subcategories**:
- `11-01`: DPP operational access
- `11-02`: DPP views and interfaces
- `11-03`: DPP update procedures
- `11-04`: DPP data flows
- `11-05`: DPP integration

### 12_SECURITY_AND_PRIVACY_IN_OPERATIONS - Security/Privacy

**Purpose**: Documents for operational security and privacy

**Subcategories**:
- `12-01`: Security policies
- `12-02`: Access control in operations
- `12-03`: Sensitive data handling
- `12-04`: Incident response
- `12-05`: Security integration

### 13_ENVIRONMENTAL_AND_CIRCULARITY_OPS - Environmental

**Purpose**: Documents for environmental and circularity operations

**Subcategories**:
- `13-01`: Environmental operational policy
- `13-02`: Carbon/energy/noise impact
- `13-03`: Circularity practices
- `13-04`: ESG reporting
- `13-05`: Sustainability integration

### 14_CONTINUOUS_IMPROVEMENT_AND_GOVERNANCE_IN_OPS - Governance

**Purpose**: Documents for operational governance and improvement

**Subcategories**:
- `14-01`: Governance frameworks
- `14-02`: Review committees and cadence
- `14-03`: Requirements linkage
- `14-04`: Change management
- `14-05`: Maturity assessments

## Tag System

### Primary Tags

Documents may be tagged with multiple classifiers:

#### Operational Phase Tags
- `#phase-0-pre`: Pre-operations
- `#phase-1-normal`: Normal operations
- `#phase-2-abnormal`: Abnormal operations
- `#phase-3-emergency`: Emergency operations
- `#phase-4-post`: Post-operations

#### Actor Tags
- `#actor-flight-crew`: Flight crew
- `#actor-maintenance`: Maintenance personnel
- `#actor-ground-ops`: Ground operations
- `#actor-occ`: Operations control center
- `#actor-data-ops`: Data operations team
- `#actor-mlops`: AI/MLOps team

#### System Tags
- `#system-nn`: Neural Network systems
- `#system-dpp`: Digital Product Passport
- `#system-caos`: CAOS integration
- `#system-aircraft`: Aircraft systems (ATA chapters)

#### Regulatory Tags
- `#reg-easa`: EASA requirements
- `#reg-faa`: FAA requirements
- `#reg-eu-ai-act`: EU AI Act compliance
- `#reg-gdpr`: GDPR compliance

## Cross-Reference Conventions

### Internal Cross-References

References to other 95-10 documents:
```
See: 95-10-XX-YY-ZZZ for [topic]
```

### External Cross-References

References to other ATA chapters or documents:
```
Ref: ATA XX-YY-ZZ [Title]
Ref: 95-00-XX [Title] (Other 95-00 buckets)
```

### Links to Manuals

References to operational manuals:
```
FCOM: [Section] - [Title]
FCTM: [Section] - [Title]
OM-A/OM-B: [Section] - [Title]
QRH: [Section] - [Title]
```

## Document Status Indicators

| Status      | Meaning                                    | Symbol |
|-------------|---------------------------------------------|--------|
| Draft       | Work in progress, not approved              | 📝     |
| Review      | Under review by stakeholders                | 🔍     |
| Active      | Approved and in operational use             | ✅     |
| Superseded  | Replaced by newer version                   | 🔄     |
| Archived    | No longer in use, kept for reference        | 📦     |
| Restricted  | Access restricted to specific roles         | 🔒     |

## Version Control

All operational documents follow semantic versioning:

```
Major.Minor.Patch
  │     │     └──── Bug fixes, typos, clarifications
  │     └────────── New content, significant updates
  └──────────────── Major restructuring or policy changes
```

## References

- ATA iSpec 2200: Numbering and Naming Conventions
- S1000D: Data Module Numbering
- AMPEL360_DOCUMENTATION_STANDARD.md
- 95-10-00-01-001: Operations Overview
- 95-10-00-01-002: Operational Scope and Actors

## Version History

| Version | Date       | Author              | Changes                |
|---------|------------|---------------------|------------------------|
| 1.0     | 2025-11-17 | AMPEL360 Ops Team   | Initial taxonomy       |

---

**Classification**: Internal Use  
**Owner**: AMPEL360 Operations Working Group  
**Next Review**: 2026-02-17
