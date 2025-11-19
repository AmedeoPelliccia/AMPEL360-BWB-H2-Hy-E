# 95-90-01-001 — Global Taxonomies Overview

## 1. Purpose

This document provides an overview of the **global reference taxonomies** used across the AMPEL360 BWB H₂ Hy-E program for classifying and organizing Neural Network (NN) and Digital Product Passport (DPP) systems.

## 2. Taxonomy Hierarchy

### 2.1 Top-Level Classification

```
AMPEL360 Taxonomies
├── Functional Taxonomy          # System functions and capabilities
├── Structural Taxonomy          # Physical and logical organization
├── Process Taxonomy             # Workflows and procedures
├── Data Taxonomy                # Data types and relationships
└── Lifecycle Taxonomy           # Development and operational phases
```

### 2.2 Functional Taxonomy

Classifies systems by their function:

```
Functional Classes
├── Perception                   # Sensors, data acquisition
│   ├── Vision Systems
│   ├── LIDAR/Radar
│   ├── Environmental Sensors
│   └── Instrumentation
├── Processing                   # Data analysis and computation
│   ├── Neural Networks
│   ├── Classical Algorithms
│   ├── Edge Computing
│   └── Cloud Processing
├── Decision                     # Control and decision-making
│   ├── Autonomous Control
│   ├── Advisory Systems
│   ├── Fault Detection
│   └── Optimization
├── Actuation                    # Physical actions
│   ├── Flight Controls
│   ├── Propulsion Control
│   ├── System Management
│   └── Energy Management
└── Communication               # Data exchange
    ├── Internal Buses
    ├── External Networks
    ├── Human Interface
    └── Ground Systems
```

## 3. ATA to OPT-IN Mapping

### 3.1 Mapping Structure

The taxonomy maps ATA chapters to OPT-IN framework axes:

| ATA Chapter | System | OPT-IN Axis | Category |
|-------------|--------|-------------|----------|
| 21 | Air Conditioning | T (E1-Environment) | ECS |
| 28 | Fuel (H₂) | T (P-Propulsion) | H₂ Fuel |
| 42 | IMA | T (O-Operating Systems) | Avionics |
| 80 | Starting/Energy | T (E2-Energy) | Energy |
| 95 | DPP/NN | N (Neural Networks) | Digital Twin |

### 3.2 Cross-ATA Integration Points

Key integration points where multiple ATAs converge:

1. **Energy Management** (ATA 24, 28, 80)
   - Electrical power distribution
   - H₂ fuel cell output
   - Energy storage and conversion

2. **Environmental Control** (ATA 21, 26, 30)
   - Cabin pressurization
   - Fire protection
   - Ice/rain protection

3. **Digital Systems** (ATA 42, 45, 95)
   - IMA platform
   - Central maintenance system
   - DPP and neural networks

## 4. Classification Schemes

### 4.1 Criticality Classification

| Level | Description | Examples | Certification |
|-------|-------------|----------|---------------|
| DAL-A | Catastrophic | Primary flight controls | DO-178C Level A |
| DAL-B | Hazardous | Engine control | DO-178C Level B |
| DAL-C | Major | Navigation systems | DO-178C Level C |
| DAL-D | Minor | Passenger entertainment | DO-178C Level D |
| DAL-E | No effect | Non-safety systems | No certification |

### 4.2 AI/ML Classification

Specific to neural network systems:

| ML Type | Description | Certification Approach |
|---------|-------------|------------------------|
| Supervised Learning | Labeled training data | EASA AI Roadmap 2.0 |
| Unsupervised Learning | Pattern discovery | Enhanced scrutiny required |
| Reinforcement Learning | Reward-based training | Special conditions |
| Transfer Learning | Pre-trained models | Source model verification |

## 5. Labels and Tags

### 5.1 Standard Labels

All entities should be tagged with:

```yaml
labels:
  ata_chapter: "95"
  optin_axis: "N"
  criticality: "DAL-C"
  ai_ml_type: "supervised_learning"
  lifecycle_phase: "design"
  status: "active"
  owner_team: "data_architecture_wg"
```

### 5.2 Searchable Keywords

Standardized keywords for discovery:

- **Domain**: `aircraft`, `propulsion`, `avionics`, `energy`, `environment`
- **Technology**: `h2`, `fuel_cell`, `neural_network`, `ima`, `digital_twin`
- **Function**: `perception`, `processing`, `decision`, `actuation`, `communication`
- **Data**: `telemetry`, `event`, `schema`, `model`, `diagram`

## 6. Taxonomy Governance

### 6.1 Change Management

Taxonomy changes follow this process:
1. Proposal submitted to Data Architecture WG
2. Impact analysis performed
3. Stakeholder review
4. Approval by Chief Architect
5. Update all affected documents
6. Communicate changes

### 6.2 Version Control

Taxonomy versioning:
- **Major version**: Breaking changes to classification
- **Minor version**: New categories added
- **Patch version**: Clarifications and corrections

Current version: **v1.0.0**

## 7. Related Documents

### 7.1 Internal References
- [Functional Taxonomy Details](95-90-01-002_Functional_Taxonomy_for_NN_and_DPP.md)
- [ATA/OPT-IN Mapping Tables](95-90-01-003_ATA_and_OPTIN_Mapping_Tables.md)
- [Labels and Classification Schemes](95-90-01-004_Labels_and_Classification_Schemes.md)

### 7.2 Asset Files
- [Functional Taxonomy Table](ASSETS/95-90-01-A-001_Functional_Taxonomy_Table.csv)
- [ATA/OPT-IN Mapping Table](ASSETS/95-90-01-A-002_ATA_OPTIN_Mapping_Table.csv)
- [Classification Schema](ASSETS/95-90-01-A-003_Classification_Schema.json)
- [Taxonomy Diagram](ASSETS/95-90-01-A-004_Taxonomy_Diagram.drawio)

### 7.3 External References
- **OPT-IN Framework Standard**: [OPT-IN_FRAMEWORK_STANDARD.md](../../../../../../OPT-IN_FRAMEWORK_STANDARD.md)
- **ATA iSpec 2200**: Industry standard for technical documentation
- **EASA AI Roadmap 2.0**: AI/ML certification guidance

## 8. Status

- **Document ID**: 95-90-01-001
- **Version**: 1.0
- **Status**: ACTIVE
- **Last Updated**: 2025-11-17
- **Owner**: AMPEL360 Data Architecture WG

---

## Document Control

- **Standard**: OPT-IN Framework v1.2
- **ATA Chapter**: 95 (Digital Product Passport and Neural Networks)
- **Bucket**: 90_Tables_Schemas_Diagrams
- **Section**: 01_Global_Reference_Taxonomies
