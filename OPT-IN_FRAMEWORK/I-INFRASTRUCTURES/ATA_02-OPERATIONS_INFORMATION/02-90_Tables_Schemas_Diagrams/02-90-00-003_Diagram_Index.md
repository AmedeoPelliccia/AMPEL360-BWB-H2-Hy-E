# 02-90-00-003: Diagram Index

## 1. Purpose

This document provides a comprehensive index of all key diagrams referenced under ATA 02-90, including system diagrams, data flow diagrams, network topologies, and UI mockups.

## 2. Diagram Categories

### 2.1 Entity-Relationship Diagrams (ERD)

| ID | File Name | Description | Related Schemas | Status |
|----|-----------|-------------|-----------------|--------|
| ERD-001 | [02-90-01-A-201_Operations_ERD.svg](./02-90-01_Database_Schemas/ASSETS/ERD/02-90-01-A-202_Operations_ERD.svg) | Core operational tables and relationships | Flight Operations, Performance | Active |
| ERD-001-SRC | [02-90-01-A-201_Operations_ERD.drawio](./02-90-01_Database_Schemas/ASSETS/ERD/02-90-01-A-201_Operations_ERD.drawio) | Draw.io source for Operations ERD | - | Active |
| ERD-002 | [02-90-01-A-203_Data_Relationships.pdf](./02-90-01_Database_Schemas/ASSETS/ERD/02-90-01-A-203_Data_Relationships.pdf) | Detailed relationship documentation | All schemas | Active |

### 2.2 System Architecture Diagrams (C4 Model)

| ID | File Name | Description | C4 Level | Status |
|----|-----------|-------------|----------|--------|
| ARCH-001 | [02-90-04-A-002_System_Context.svg](./02-90-04_System_Architecture_Diagrams/ASSETS/Architecture/02-90-04-A-002_System_Context.svg) | High-level system context | Context | Active |
| ARCH-001-SRC | [02-90-04-A-001_System_Context.drawio](./02-90-04_System_Architecture_Diagrams/ASSETS/Architecture/02-90-04-A-001_System_Context.drawio) | Draw.io source | Context | Active |
| ARCH-002 | [02-90-04-A-003_Container_Diagram.svg](./02-90-04_System_Architecture_Diagrams/ASSETS/Architecture/02-90-04-A-003_Container_Diagram.svg) | Services, databases, external systems | Container | Active |
| ARCH-003 | [02-90-04-A-004_Component_Diagram.svg](./02-90-04_System_Architecture_Diagrams/ASSETS/Architecture/02-90-04-A-004_Component_Diagram.svg) | Core services with dependencies | Component | Active |
| ARCH-004 | [02-90-04-A-005_Deployment_Diagram.svg](./02-90-04_System_Architecture_Diagrams/ASSETS/Architecture/02-90-04-A-005_Deployment_Diagram.svg) | Infrastructure deployment (cloud/edge) | Deployment | Active |

### 2.3 Data Flow Diagrams

| ID | File Name | Description | Related Systems | Status |
|----|-----------|-------------|-----------------|--------|
| FLOW-001 | [02-90-04-A-101_Operations_Data_Flow.svg](./02-90-04_System_Architecture_Diagrams/ASSETS/Data_Flow/02-90-04-A-101_Operations_Data_Flow.svg) | Flight operations data ingestion to analytics | [02-20 Subsystems](../02-20_Subsystems/README.md), [02-40 Software](../02-40_Software/README.md) | Active |
| FLOW-002 | [02-90-04-A-102_Energy_Data_Flow.svg](./02-90-04_System_Architecture_Diagrams/ASSETS/Data_Flow/02-90-04-A-102_Energy_Data_Flow.svg) | Energy sensors to storage to dashboards | [02-80 Energy](../02-80_Energy/README.md) | Active |
| FLOW-003 | [02-90-04-A-103_Propulsion_Data_Flow.svg](./02-90-04_System_Architecture_Diagrams/ASSETS/Data_Flow/02-90-04-A-103_Propulsion_Data_Flow.svg) | Propulsion telemetry data flows | [02-70 Propulsion](../02-70_Propulsion/README.md) | Active |
| FLOW-004 | [02-90-04-A-104_End_to_End_Flow.svg](./02-90-04_System_Architecture_Diagrams/ASSETS/Data_Flow/02-90-04-A-104_End_to_End_Flow.svg) | Aircraft/ground to decision-support | All systems | Active |

### 2.4 Integration Diagrams

| ID | File Name | Description | Related ATAs | Status |
|----|-----------|-------------|--------------|--------|
| INT-001 | [02-90-04-A-201_Cross_ATA_Integration.svg](./02-90-04_System_Architecture_Diagrams/ASSETS/Integration/02-90-04-A-201_Cross_ATA_Integration.svg) | Cross-ATA data and service integration | ATA 02, 70, 80, 95, 99 | Active |
| INT-002 | [02-90-04-A-202_Cloud_Edge_Architecture.svg](./02-90-04_System_Architecture_Diagrams/ASSETS/Integration/02-90-04-A-202_Cloud_Edge_Architecture.svg) | Cloud/edge workload partitioning | Infrastructure | Active |
| INT-003 | [02-90-04-A-203_External_Systems.svg](./02-90-04_System_Architecture_Diagrams/ASSETS/Integration/02-90-04-A-203_External_Systems.svg) | Connections to AOC, ANSP, airports | External | Active |

### 2.5 Sequence Diagrams

| ID | File Name | Description | Use Case | Status |
|----|-----------|-------------|----------|--------|
| SEQ-001 | [02-90-04-A-301_Flight_Planning_Sequence.svg](./02-90-04_System_Architecture_Diagrams/ASSETS/Sequence/02-90-04-A-301_Flight_Planning_Sequence.svg) | Flight planning workflow | [02-40-15](../02-40_Software/02-40-15_Flight_Planning_Software/README.md) | Active |
| SEQ-002 | [02-90-04-A-302_Performance_Calc_Sequence.svg](./02-90-04_System_Architecture_Diagrams/ASSETS/Sequence/02-90-04-A-302_Performance_Calc_Sequence.svg) | Performance calculation cycle | [02-40-13](../02-40_Software/02-40-13_Performance_Calculator/README.md) | Active |
| SEQ-003 | [02-90-04-A-303_Emergency_Response_Sequence.svg](./02-90-04_System_Architecture_Diagrams/ASSETS/Sequence/02-90-04-A-303_Emergency_Response_Sequence.svg) | Emergency response data flows | Emergency systems | Active |

### 2.6 Network Topology Diagrams

| ID | File Name | Description | Network Type | Status |
|----|-----------|-------------|--------------|--------|
| NET-001 | [02-90-03-A-003_Network_Topology.svg](./02-90-03_Data_Exchange_Formats/ASSETS/AFDX/02-90-03-A-003_Network_Topology.svg) | AFDX network topology | Avionics | Active |
| NET-002 | [02-90-09 Network Diagrams](./02-90-09_Wiring_Data_Network_Diagrams/README.md) | Physical and logical network wiring | Infrastructure | Planned |

## 3. Diagram Format Standards

### 3.1 Supported Formats

| Format | Use Case | Editing Tool | Export Format |
|--------|----------|--------------|---------------|
| Draw.io | Editable diagrams | [Draw.io](https://app.diagrams.net/) | .drawio, .svg, .png, .pdf |
| SVG | Web embedding | Vector graphics editors | .svg |
| PDF | Printable documentation | Various | .pdf |
| PNG | Raster images | Image editors | .png |

### 3.2 Naming Conventions

Diagram files follow the pattern:
- **Source files**: `02-90-XX-A-NNN_Description.drawio`
- **Exported SVG**: `02-90-XX-A-NNN_Description.svg` (same NNN + 1 for export)
- **Exported PDF**: `02-90-XX-A-NNN_Description.pdf`

### 3.3 Version Control

- **Source files** (.drawio) are version-controlled in Git
- **Exported formats** are regenerated on source changes
- **Change log** maintained in diagram metadata or adjacent README

### 3.4 Style Guidelines

#### Colors
- **Primary**: #0078D4 (Blue) – Core systems
- **Secondary**: #107C10 (Green) – Operational systems
- **Accent**: #D83B01 (Orange) – External systems
- **Warning**: #FFB900 (Yellow) – Alerts and cautions
- **Error**: #E81123 (Red) – Errors and failures
- **Neutral**: #8A8886 (Gray) – Infrastructure

#### Fonts
- **Title**: Arial Bold, 18pt
- **Headers**: Arial Bold, 14pt
- **Body**: Arial Regular, 11pt
- **Labels**: Arial Regular, 9pt

#### Shapes
- **Systems**: Rounded rectangles
- **Data stores**: Cylinders
- **External entities**: Rectangles with thick border
- **Processes**: Circles/ovals
- **Data flows**: Arrows with labels

## 4. Diagram Maintenance

### 4.1 Update Triggers

Diagrams must be updated when:

1. **System architecture changes**: New services, databases, integrations
2. **Data model changes**: Schema modifications affecting relationships
3. **API changes**: New endpoints or contract modifications
4. **Network changes**: Topology or protocol changes

### 4.2 Review Process

1. **Author** updates source file (.drawio)
2. **Author** exports to SVG/PDF
3. **Peer review** for accuracy and clarity
4. **Architecture review** for significant changes
5. **Commit** source and exported files together

### 4.3 Validation Checklist

- [ ] Diagram title and version clearly visible
- [ ] Legend included if using custom symbols
- [ ] All connections labeled with data types/protocols
- [ ] External references documented
- [ ] Date and author information included
- [ ] Consistent with other diagrams in same category
- [ ] Accessible color scheme (color-blind friendly)

## 5. Cross-References

### 5.1 Related Documentation

- [02-90-00-001 Tables Schemas Overview](./02-90-00-001_Tables_Schemas_Overview.md)
- [02-90-00-004 Schema Version Control](./02-90-00-004_Schema_Version_Control.md)
- [02-90-01 Database Schemas](./02-90-01_Database_Schemas/README.md)
- [02-90-04 System Architecture Diagrams](./02-90-04_System_Architecture_Diagrams/README.md)

### 5.2 External Standards

- [C4 Model](https://c4model.com/) – Software architecture diagrams
- [UML](https://www.uml.org/) – Unified Modeling Language
- [ArchiMate](https://www.opengroup.org/archimate-forum) – Enterprise architecture modeling
- [ISO/IEC/IEEE 42010](https://www.iso.org/standard/50508.html) – Systems and software engineering — Architecture description

## 6. Usage Guidelines

### 6.1 For Diagram Consumers

1. **Check version**: Ensure diagram is current
2. **Review legend**: Understand symbols and conventions
3. **Follow references**: Use hyperlinks to related documents
4. **Provide feedback**: Report inaccuracies or improvements

### 6.2 For Diagram Authors

1. **Use templates**: Start from existing diagrams when possible
2. **Follow standards**: Apply color scheme and style guidelines
3. **Document assumptions**: Note any simplifications or abstractions
4. **Link to sources**: Reference schemas, APIs, or systems depicted
5. **Export consistently**: Generate all required formats

## 7. Diagram Repository Structure

```
02-90_Tables_Schemas_Diagrams/
├── 02-90-01_Database_Schemas/ASSETS/ERD/
│   ├── *.drawio (source files)
│   ├── *.svg (exported diagrams)
│   └── *.pdf (printable versions)
├── 02-90-04_System_Architecture_Diagrams/ASSETS/
│   ├── Architecture/ (C4 model diagrams)
│   ├── Data_Flow/ (data flow diagrams)
│   ├── Integration/ (integration diagrams)
│   └── Sequence/ (sequence diagrams)
└── 02-90-09_Wiring_Data_Network_Diagrams/ASSETS/
    └── (network topology diagrams)
```

---

## Document Control

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT** – Subject to human review and approval.
- Human approver: _[to be completed]_.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: _2025-11-21_.

---
