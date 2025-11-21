# 02-90-04: System Architecture Diagrams

## Purpose

This folder aggregates key architecture and data flow diagrams for the AMPEL360 operations ecosystem, following the [C4 model](https://c4model.com/) and industry best practices.

## Scope

System architecture documentation includes:

- **Architecture Diagrams**: System context, containers, components, deployment (C4 model)
- **Data Flow Diagrams**: End-to-end data movement across systems
- **Integration Diagrams**: Cross-ATA and external system integrations
- **Sequence Diagrams**: Interaction flows for key use cases

All diagrams are **non-proprietary** and suitable for public collaboration.

## Diagram Categories

### 1. Architecture Diagrams (C4 Model)

Following the [C4 model](https://c4model.com/) for software architecture visualization:

| Level | Diagram | Description | Audience |
|-------|---------|-------------|----------|
| **Context** | [System Context](./ASSETS/Architecture/02-90-04-A-002_System_Context.svg) | High-level system and external actors | All stakeholders |
| **Container** | [Container Diagram](./ASSETS/Architecture/02-90-04-A-003_Container_Diagram.svg) | Services, databases, external systems | Architects, developers |
| **Component** | [Component Diagram](./ASSETS/Architecture/02-90-04-A-004_Component_Diagram.svg) | Internal service components | Developers |
| **Deployment** | [Deployment Diagram](./ASSETS/Architecture/02-90-04-A-005_Deployment_Diagram.svg) | Infrastructure and runtime | DevOps, infrastructure |

### 2. Data Flow Diagrams

End-to-end data movement:

- **[Operations Data Flow](./ASSETS/Data_Flow/02-90-04-A-101_Operations_Data_Flow.svg)**: Flight ops ingestion → storage → analytics
- **[Energy Data Flow](./ASSETS/Data_Flow/02-90-04-A-102_Energy_Data_Flow.svg)**: Sensor data → monitoring → dashboards
- **[Propulsion Data Flow](./ASSETS/Data_Flow/02-90-04-A-103_Propulsion_Data_Flow.svg)**: Engine telemetry flows
- **[End-to-End Flow](./ASSETS/Data_Flow/02-90-04-A-104_End_to_End_Flow.svg)**: Aircraft/ground → decision support

### 3. Integration Diagrams

System integration patterns:

- **[Cross-ATA Integration](./ASSETS/Integration/02-90-04-A-201_Cross_ATA_Integration.svg)**: ATA 02, 70, 80, 95, 99 data and service flows
- **[Cloud/Edge Architecture](./ASSETS/Integration/02-90-04-A-202_Cloud_Edge_Architecture.svg)**: Workload distribution
- **[External Systems](./ASSETS/Integration/02-90-04-A-203_External_Systems.svg)**: AOC, ANSP, airport connections

### 4. Sequence Diagrams

Interaction flows for key scenarios:

- **[Flight Planning](./ASSETS/Sequence/02-90-04-A-301_Flight_Planning_Sequence.svg)**: Flight planning workflow
- **[Performance Calculation](./ASSETS/Sequence/02-90-04-A-302_Performance_Calc_Sequence.svg)**: Performance calc request/response
- **[Emergency Response](./ASSETS/Sequence/02-90-04-A-303_Emergency_Response_Sequence.svg)**: Emergency data flows

## Diagram Standards

### Format and Tooling

| Format | Purpose | Tool | Export |
|--------|---------|------|--------|
| **.drawio** | Editable source | [Draw.io](https://app.diagrams.net/) | .drawio |
| **.svg** | Web embedding | Draw.io export | .svg |
| **.pdf** | Printable docs | Draw.io export | .pdf |
| **.png** | Presentations | Draw.io export | .png |

### Style Guide

#### Color Palette

- **Primary Blue** (#0078D4): Core AMPEL360 systems
- **Green** (#107C10): Operational/healthy states
- **Orange** (#D83B01): External systems/interfaces
- **Yellow** (#FFB900): Warnings/attention
- **Red** (#E81123): Errors/critical states
- **Gray** (#8A8886): Infrastructure/support

#### Typography

- **Titles**: Arial Bold, 18pt
- **Headers**: Arial Bold, 14pt
- **Body**: Arial Regular, 11pt
- **Labels**: Arial Regular, 9pt

#### Shapes

- **Systems/Services**: Rounded rectangles
- **Databases**: Cylinders
- **External Entities**: Rectangles with thick border
- **Processes**: Circles/ovals
- **Data Flows**: Arrows with labels

### Naming Conventions

- **Source**: `02-90-04-A-NNN_Description.drawio`
- **Export SVG**: `02-90-04-A-NNN_Description.svg` (same NNN or NNN+1)
- **Export PDF**: `02-90-04-A-NNN_Description.pdf`

## C4 Model Levels Explained

### Level 1: System Context

**Purpose**: Big picture view of the system and its environment

**Shows**:
- The software system (AMPEL360 Operations)
- Users and external systems
- High-level relationships

**Audience**: Everyone (executives, managers, technical staff)

### Level 2: Container

**Purpose**: Decompose the system into containers (applications, databases, etc.)

**Shows**:
- Web applications, mobile apps
- Backend services
- Databases, message queues
- Technology choices

**Audience**: Architects, developers, operations

### Level 3: Component

**Purpose**: Decompose each container into components

**Shows**:
- Internal modules/components
- Responsibilities
- Implementation technology

**Audience**: Developers, architects

### Level 4: Code (Not Included)

**Purpose**: Zoom into individual components (UML class diagrams, etc.)

**Note**: Code-level diagrams are maintained in source code repositories, not in 02-90.

## Diagram Lifecycle

### Creation

1. **Identify need**: New system, major change, documentation gap
2. **Select template**: Use existing diagram as starting point
3. **Create source**: Edit in Draw.io
4. **Export formats**: Generate SVG, PDF as needed
5. **Commit together**: Source (.drawio) and exports in same commit

### Maintenance

1. **Trigger**: Architecture change, system update, feedback
2. **Update source**: Modify .drawio file
3. **Regenerate exports**: Update SVG, PDF
4. **Review**: Peer review for accuracy
5. **Version**: Update diagram version number

### Review Process

- [ ] Title and version clearly visible
- [ ] Legend included (if custom symbols)
- [ ] All connections labeled
- [ ] External references documented
- [ ] Date and author visible
- [ ] Consistent with other diagrams
- [ ] Accessible colors (colorblind-friendly)

## Usage Guidelines

### For Stakeholders

1. **Start with Context**: Understand the big picture
2. **Drill down**: Move to Container, then Component as needed
3. **Follow references**: Use hyperlinks to related docs
4. **Provide feedback**: Report outdated or unclear diagrams

### For Developers

1. **Consult before building**: Review architecture first
2. **Update when changing**: Keep diagrams current with code
3. **Use in code reviews**: Reference architecture in discussions
4. **Link from code**: Add diagram links in README files

### For Operations

1. **Understand deployment**: Review deployment diagrams
2. **Troubleshoot with flows**: Use data flow diagrams for debugging
3. **Plan capacity**: Use architecture for scaling decisions

## Cross-References

- [02-90-00-003 Diagram Index](../02-90-00-003_Diagram_Index.md) – Complete diagram catalog
- [02-90-01 Database Schemas](../02-90-01_Database_Schemas/README.md) – Data models
- [02-90-02 API Specifications](../02-90-02_API_Specifications/README.md) – Service contracts
- [02-40 Software](../../02-40_Software/README.md) – Application components
- [C4 Model](https://c4model.com/) – Architecture visualization framework
- [UML](https://www.uml.org/) – Unified Modeling Language

---

## Document Control

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT** – Subject to human review and approval.
- Human approver: _[to be completed]_.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: _2025-11-21_.

---
