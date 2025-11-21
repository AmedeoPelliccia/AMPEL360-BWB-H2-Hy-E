# 02-40 – Software

## Purpose

This folder contains the complete software ecosystem for AMPEL360 BWB-H₂-Hy-E aircraft operations, including applications, services, calculation engines, interfaces, and AI/ML systems that support flight operations, dispatch, maintenance, and hydrogen fuel management.

---

## Scope

The 02-40 Software chapter encompasses:

- **Core Applications**: Foundational operational applications and microservices architecture
- **Electronic Flight Bag (EFB)**: iOS/iPadOS application for pilots with performance calculations, W&B, weather, and document viewing
- **Backend Services**: API gateway, authentication, data services, notification, analytics
- **Performance Calculator**: Takeoff, landing, and cruise performance calculations (DO-178C Level C)
- **Weight & Balance System**: CG calculations with H₂ fuel integration (DO-178C Level C)
- **Flight Planning Software**: Route optimization, H₂ fuel planning, weather integration
- **Dispatch Interface**: ACARS/SITA communication with aircraft
- **Weather Data Processor**: METAR/TAF/GRIB processing and graphical weather products
- **Data Recording Service**: Operational event logging and DPP integration
- **Analytics Engine**: Real-time and historical analytics, KPIs, dashboards
- **H₂ Operations Software**: Hydrogen refueling control and safety monitoring
- **Predictive Ops Software**: ML/AI for predictive maintenance and optimization

---

## Folder Organization

### Core Documentation (02-40-00-xxx)

- **[02-40-00-001_Software_Architecture_Overview.md](02-40-00-001_Software_Architecture_Overview.md)**: Overall software architecture, layers, domains, key systems, and design principles
- **[02-40-00-002_Software_Integration_Map.md](02-40-00-002_Software_Integration_Map.md)**: Integration map showing data flows, API dependencies, and communication patterns
- **[02-40-00-003_API_Catalog.yaml](02-40-00-003_API_Catalog.yaml)**: Machine-readable catalog of all APIs, services, endpoints, and message queues
- **[02-40-00-004_Software_Development_Standards.md](02-40-00-004_Software_Development_Standards.md)**: Coding standards, branching model, code review rules, and SDLC guidelines

### Subsystems

#### Core Platform (02-40-01 to 02-40-09)
- **[02-40-01_Core_Applications/](02-40-01_Core_Applications/)**: Core operational applications, microservices architecture, service mesh

#### Operational Systems (02-40-11 to 02-40-19)
- **[02-40-11_EFB_Software/](02-40-11_EFB_Software/)**: Electronic Flight Bag iOS application with performance, W&B, weather, and document modules
- **[02-40-12_Backend_Services/](02-40-12_Backend_Services/)**: API gateway, authentication, data services, notifications
- **[02-40-13_Performance_Calculator/](02-40-13_Performance_Calculator/)**: Flight performance calculation engine (DO-178C Level C)
- **[02-40-14_Weight_Balance_System/](02-40-14_Weight_Balance_System/)**: W&B calculations with H₂ fuel integration (DO-178C Level C)
- **[02-40-15_Flight_Planning_Software/](02-40-15_Flight_Planning_Software/)**: Route optimization and H₂ fuel planning
- **[02-40-16_Dispatch_Interface/](02-40-16_Dispatch_Interface/)**: ACARS/SITA integration for air-ground communication
- **[02-40-17_Weather_Data_Processor/](02-40-17_Weather_Data_Processor/)**: Meteorological data processing and distribution
- **[02-40-18_Data_Recording_Service/](02-40-18_Data_Recording_Service/)**: Operational event logging and DPP integration
- **[02-40-19_Analytics_Engine/](02-40-19_Analytics_Engine/)**: Real-time and batch analytics, KPIs, reporting

#### Specialized Systems (02-40-21 to 02-40-29)
- **[02-40-21_H2_Operations_Software/](02-40-21_H2_Operations_Software/)**: Hydrogen refueling control and safety monitoring
- **[02-40-23_Predictive_Ops_Software/](02-40-23_Predictive_Ops_Software/)**: ML pipeline for predictive maintenance and optimization

---

## Key Features

### Safety-Critical Software
- **DO-178C Certification**: EFB performance module, W&B system, performance calculator
- **Rigorous Testing**: 100% MC/DC coverage for Level C software
- **Independent Verification**: Certified reviewers and QA processes

### Offline-First Architecture
- **EFB Offline Operation**: Full functionality without network connectivity
- **Data Synchronization**: Delta sync with conflict resolution
- **Cached Content**: Aeronautical database, weather, documents available offline

### BWB-Specific Features
- **Custom Aerodynamics**: BWB performance models and control authority
- **H₂ Fuel Integration**: Cryogenic hydrogen mass properties, boil-off management
- **Unique CG Envelope**: BWB-specific center of gravity limits

### AI/ML Integration
- **Predictive Maintenance**: ML-based component failure prediction
- **Route Optimization**: AI-enhanced flight planning
- **Performance Enhancement**: NN-assisted performance calculations with safety constraints
- **EU AI Act Compliance**: Risk assessment, transparency, human oversight

### Integration with CAOS
- **Real-Time Coordination**: Integration with [CAOS Framework](../../../CAOS/) for operational coordination
- **Event-Driven Architecture**: Kafka-based event streaming
- **Digital Product Passport**: Immutable audit trail via [ATA 95](../../../N-NEURAL_NETWORKS_USERS_TRACEABILITY/ATA_95-DIGITAL_PRODUCT_PASSPORT_NEURAL_NETWORKS/)

---

## Technology Stack

### Languages
- **Swift**: iOS EFB application
- **Python**: ML/NN pipelines, data processing, analytics
- **Go**: High-performance backend services
- **TypeScript/Node.js**: Web applications, integration services
- **C++**: Performance-critical calculations

### Infrastructure
- **Cloud**: AWS (primary), Azure (DR)
- **Containers**: Docker, Kubernetes (EKS)
- **Service Mesh**: Istio (mTLS, observability)
- **Databases**: PostgreSQL, MongoDB, InfluxDB, Redis
- **Message Brokers**: Apache Kafka, RabbitMQ

### ML/AI
- **Frameworks**: PyTorch, TensorFlow
- **Serving**: ONNX Runtime, TensorFlow Serving
- **Feature Store**: Feast
- **Monitoring**: Evidently AI, Prometheus

---

## Standards and Compliance

### Certification Standards
- **[DO-178C](https://www.rtca.org/content/standards-guidance-materials)**: Software Considerations in Airborne Systems
- **[DO-278A](https://www.rtca.org/content/standards-guidance-materials)**: CNS/ATM Systems Software Integrity Assurance
- **[DO-254](https://www.rtca.org/content/standards-guidance-materials)**: Airborne Electronic Hardware Design Assurance

### Aviation Standards
- **[EASA CS-25](https://www.easa.europa.eu/en/document-library/certification-specifications/cs-25-large-aeroplanes)**: Certification Specifications for Large Aeroplanes
- **[CS-25.1309](https://www.easa.europa.eu/en/document-library/certification-specifications/cs-25-large-aeroplanes)**: Equipment, Systems, and Installations
- **[FAA Part 21](https://www.ecfr.gov/current/title-14/chapter-I/subchapter-C/part-21)**: Certification Procedures for Products

### AI/ML Standards
- **[EU AI Act](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:52021PC0206)**: Regulation on Artificial Intelligence
- **MLOps Best Practices**: Model versioning, monitoring, governance

### Communication Standards
- **ARINC 618**: ACARS protocol standards
- **ARINC 429/664**: Avionics data buses
- **ICAO Standards**: Aeronautical information exchange (AIXM)

---

## Integration Points

### On-Board Systems (T-TECHNOLOGY)
- **[ATA 28 – H₂ Fuel System](../../../T-TECHNOLOGY_AMEDEOPELLICCIA-ON_BOARD_SYSTEMS/C2-CIRCULAR_CRYOGENICS_SYSTEMS/ATA_28-FUEL_SAF_CRYOGENIC_H2/)**: Fuel quantity, temperature, pressure
- **[ATA 31 – Indicating/Recording](../../../T-TECHNOLOGY_AMEDEOPELLICCIA-ON_BOARD_SYSTEMS/D-DATA/ATA_31-INDICATING_RECORDING_RECORDING_FUNCTION/)**: Flight data recorder events
- **[ATA 34 – Navigation](../../../T-TECHNOLOGY_AMEDEOPELLICCIA-ON_BOARD_SYSTEMS/E3-ELECTRONICS/ATA_34-NAVIGATION/)**: GPS position, navigation aids
- **[ATA 45 – Onboard Maintenance](../../../T-TECHNOLOGY_AMEDEOPELLICCIA-ON_BOARD_SYSTEMS/I-INFORMATION_INTELLIGENCE_INTERFACES/ATA_45-ONBOARD_MAINTENANCE_SYSTEMS/)**: Maintenance messages, fault codes

### Ground Systems (I-INFRASTRUCTURES)
- **[ATA 02 – Other Subsystems](../)**: Operations, subsystems, circularity
- **[ATA 03 – GSE](../../ATA_03-SUPPORT_INFORMATION_GSE/)**: Ground support equipment coordination

### Digital Intelligence (N-NEURAL_NETWORKS)
- **[ATA 95 – Digital Product Passport](../../../N-NEURAL_NETWORKS_USERS_TRACEABILITY/ATA_95-DIGITAL_PRODUCT_PASSPORT_NEURAL_NETWORKS/)**: Event anchoring, traceability, blockchain

---

## Development Workflow

1. **Requirements**: Captured in issue tracking, linked to high-level requirements
2. **Design**: Architecture decisions in ADRs, diagrams in ASSETS folders
3. **Implementation**: Following [coding standards](02-40-00-004_Software_Development_Standards.md)
4. **Testing**: Unit, integration, E2E tests with appropriate coverage
5. **Certification Review**: Independent verification for safety-critical code
6. **Deployment**: CI/CD with automated testing and security scanning
7. **Monitoring**: Production observability with Prometheus and Grafana

---

## Status

- **Bucket**: 40_Software
- **Status**: Active
- **Applicability**: ATA 02 Operations Information
- **Last Updated**: 2025-11-21
- **Owner**: AMPEL360 Software Architecture Team

---

## Quick Links

### Documentation
- [Software Architecture Overview](02-40-00-001_Software_Architecture_Overview.md)
- [Software Integration Map](02-40-00-002_Software_Integration_Map.md)
- [API Catalog](02-40-00-003_API_Catalog.yaml)
- [Development Standards](02-40-00-004_Software_Development_Standards.md)

### Key Subsystems
- [EFB Software](02-40-11_EFB_Software/)
- [Backend Services](02-40-12_Backend_Services/)
- [Performance Calculator](02-40-13_Performance_Calculator/)
- [Weight & Balance System](02-40-14_Weight_Balance_System/)

### External References
- [CAOS Framework](../../../CAOS/)
- [ATA 95 Digital Product Passport](../../../N-NEURAL_NETWORKS_USERS_TRACEABILITY/ATA_95-DIGITAL_PRODUCT_PASSPORT_NEURAL_NETWORKS/)
- [AMPEL360 Documentation Standard](../../../../AMPEL360_DOCUMENTATION_STANDARD.md)

---

## Document Control

- **Generated with the assistance of AI (GitHub Copilot), prompted by Amedeo Pelliccia**.
- **Status**: DRAFT – Subject to human review and approval.
- **Human approver**: _[to be completed]_.
- **Repository**: `AMPEL360-BWB-H2-Hy-E`
- **Last AI update**: _2025-11-21_.
- **Standard**: OPT-IN Framework v1.1
- **Owner**: AMPEL360 Documentation WG

---

**End of Document**