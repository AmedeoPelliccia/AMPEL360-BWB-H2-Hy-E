# 02-40-01 – Core Applications

## Purpose

This folder contains documentation and assets for the core operational applications that form the foundation of the AMPEL360 operations software platform. These applications support essential flight operations, crew management, dispatch coordination, and integration with the CAOS (Coordinated Aerospace Operations System) framework.

---

## Scope

The Core Applications subsystem includes:

- **Application Portfolio Management**: Catalog of all core operational applications
- **Microservices Architecture**: Design and implementation of service-oriented architecture
- **Service Mesh Implementation**: Inter-service communication, security, and observability
- **Application Security**: Authentication, authorization, and security controls

---

## Folder Organization

### Documentation Files

- **[02-40-01-001_Application_Portfolio.md](02-40-01-001_Application_Portfolio.md)**: Complete list and description of core applications, their owners, criticality levels, and main responsibilities
- **[02-40-01-002_Microservices_Architecture.md](02-40-01-002_Microservices_Architecture.md)**: Detailed microservices architecture including bounded contexts, services, deployment units, and communication patterns
- **[02-40-01-003_Service_Mesh_Implementation.md](02-40-01-003_Service_Mesh_Implementation.md)**: Service mesh design covering mTLS, traffic policies, resilience patterns, and observability
- **[02-40-01-004_Application_Security.md](02-40-01-004_Application_Security.md)**: Application-level security controls including authentication, authorization, input validation, secrets management, and hardening

### ASSETS Folder

The **[ASSETS/](ASSETS/)** folder contains design artifacts organized according to the [AMPEL360 ASSETS Standard](../../../../AMPEL360_ASSETS_STANDARD.md):

- **DIAGRAMS/**: Architecture diagrams (02-40-01-A-001, 02-40-01-A-002)
- **DRAWINGS/**: Technical drawings and diagrams
- **MODELS/**: Logical/system models
- **DATA/**: Configuration data and lookup tables
- **TEMPLATES/**: Document templates
- **EXPORTS/**: Rendered outputs (SVG, PNG, PDF) for documentation embedding

Key assets include:
- **02-40-01-A-001_Application_Architecture.drawio**: Source diagram for core application architecture
- **02-40-01-A-002_Application_Architecture.svg**: Exported architecture diagram
- **02-40-01-A-003_Service_Dependencies.svg**: Service dependency and call graph visualization
- **02-40-01-A-004_Deployment_Topology.svg**: Deployment topology across environments and regions

---

## Relationship to CAOS Framework

The Core Applications integrate with the [CAOS (Coordinated Aerospace Operations System)](../../../../CAOS/) framework, providing:

- **Operational Coordination**: Real-time coordination between flight operations, crew, maintenance, and ground services
- **Data Integration**: Unified data access across operational domains
- **Event Processing**: Event-driven architecture for operational event handling
- **System Orchestration**: Orchestration of complex operational workflows

See the [CAOS documentation](../../../../CAOS/README.md) for details on the integration architecture.

---

## Integration Points

### Internal Integrations (02-40 Subsystems)

- **[02-40-12 Backend Services](../02-40-12_Backend_Services/)**: API gateway, authentication, data services
- **[02-40-18 Data Recording Service](../02-40-18_Data_Recording_Service/)**: Operational event logging
- **[02-40-19 Analytics Engine](../02-40-19_Analytics_Engine/)**: Real-time and batch analytics

### Cross-ATA Integrations

- **[ATA 31 – Indicating/Recording](../../../../T-TECHNOLOGY_AMEDEOPELLICCIA-ON_BOARD_SYSTEMS/D-DATA/ATA_31-INDICATING_RECORDING_RECORDING_FUNCTION/)**: Flight data recorder integration
- **[ATA 45 – Onboard Maintenance Systems](../../../../T-TECHNOLOGY_AMEDEOPELLICCIA-ON_BOARD_SYSTEMS/I-INFORMATION_INTELLIGENCE_INTERFACES/ATA_45-ONBOARD_MAINTENANCE_SYSTEMS/)**: Maintenance messaging and fault reporting
- **[ATA 95 – Digital Product Passport](../../../../N-NEURAL_NETWORKS_USERS_TRACEABILITY/ATA_95-DIGITAL_PRODUCT_PASSPORT_NEURAL_NETWORKS/)**: Operational event traceability

---

## Technology Stack

- **Backend Services**: Go, Python, Node.js/TypeScript
- **Container Runtime**: Docker
- **Orchestration**: Kubernetes (EKS)
- **Service Mesh**: Istio
- **Databases**: PostgreSQL, MongoDB, Redis
- **Message Broker**: Apache Kafka, RabbitMQ
- **Monitoring**: Prometheus, Grafana, Jaeger

---

## Standards and Compliance

- **Coding Standards**: See [02-40-00-004 Software Development Standards](../02-40-00-004_Software_Development_Standards.md)
- **API Standards**: OpenAPI 3.0 specifications
- **Security Standards**: OAuth2, JWT, mTLS
- **Observability**: OpenTelemetry for distributed tracing

---

## Development Workflow

1. **Requirements**: Captured in issue tracking system, linked to this documentation
2. **Design**: Architectural decisions documented in ADRs, diagrams in ASSETS/
3. **Implementation**: Following language-specific coding standards
4. **Testing**: Unit, integration, and E2E tests (see testing strategy in development standards)
5. **Deployment**: CI/CD pipeline with automated testing and security scanning
6. **Monitoring**: Production monitoring with Prometheus and Grafana

---

## Status

- **Implementation**: In Progress
- **Last Updated**: 2025-11-21
- **Owner**: AMPEL360 Platform Team

---

## References

### Internal Documentation
- [02-40-00-001 Software Architecture Overview](../02-40-00-001_Software_Architecture_Overview.md)
- [02-40-00-002 Software Integration Map](../02-40-00-002_Software_Integration_Map.md)
- [02-40-00-004 Software Development Standards](../02-40-00-004_Software_Development_Standards.md)
- [CAOS Framework](../../../../CAOS/README.md)

### External Standards
- [Twelve-Factor App Methodology](https://12factor.net/)
- [Microservices Patterns](https://microservices.io/patterns/index.html)
- [Istio Service Mesh](https://istio.io/latest/docs/)

---

## Document Control

- **Generated with the assistance of AI (GitHub Copilot), prompted by Amedeo Pelliccia**.
- **Status**: DRAFT – Subject to human review and approval.
- **Human approver**: _[to be completed]_.
- **Repository**: `AMPEL360-BWB-H2-Hy-E`
- **Last AI update**: _2025-11-21_.

---

**End of Document**
