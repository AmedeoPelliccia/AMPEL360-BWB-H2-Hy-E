# 95-40-00-002 Software Architecture and Scope

**ATA Chapter:** 95 – Digital Product Passport Neural Networks  
**Section:** 95-40 – Software  
**Document ID:** 95-40-00-002  
**Version:** 1.0  
**Date:** 2025-11-17  
**Status:** ACTIVE

---

## 1. Purpose

This document defines the software architecture, design patterns, and scope boundaries for all software components within ATA 95. It provides the architectural blueprint that guides software development, integration, and deployment decisions.

---

## 2. Architectural Overview

### 2.1 System Context

The AMPEL360 software architecture supports three primary operational contexts:

1. **Ground Operations:** Cloud-based training, analytics, and DPP management
2. **Onboard Operations:** Embedded real-time inference and safety monitoring
3. **Development Operations:** Tools, pipelines, and testing infrastructure

### 2.2 Architectural Viewpoints

We use the following architectural viewpoints per ISO/IEC 42010:

- **Functional View:** Capabilities and features
- **Information View:** Data models and flows
- **Deployment View:** Runtime topology and infrastructure
- **Development View:** Code organization and build structure
- **Operational View:** Monitoring, maintenance, and support

---

## 3. Architectural Patterns

### 3.1 Microservices Architecture (Ground)

**Pattern:** Domain-driven microservices with API gateways

**Characteristics:**
- Independent deployment and scaling
- Service mesh for inter-service communication
- Event-driven integration where appropriate
- Centralized logging and distributed tracing

**Technology Stack:**
- Kubernetes for orchestration
- Istio or Linkerd for service mesh
- Kafka for event streaming
- PostgreSQL, Redis for persistence

### 3.2 Partitioned Architecture (Embedded)

**Pattern:** ARINC 653 time and space partitioning

**Characteristics:**
- Safety-critical partition isolation
- Deterministic scheduling
- Limited inter-partition communication
- Certified runtime environment

**Technology Stack:**
- ARINC 653 APEX API
- VxWorks 653 or PikeOS
- ARINC 664 (AFDX) for network communication
- DO-178C Level A/B certified code

### 3.3 Pipeline Architecture (MLOps)

**Pattern:** Directed acyclic graph (DAG) pipelines

**Characteristics:**
- Reproducible, versioned workflows
- Parallel execution where possible
- Checkpointing and failure recovery
- Artifact tracking and lineage

**Technology Stack:**
- Apache Airflow or Kubeflow Pipelines
- MLflow for experiment tracking
- DVC for data versioning
- Feature stores (Feast, Tecton)

---

## 4. Component Architecture

### 4.1 Layered Component Model

```
┌─────────────────────────────────────────────────────────┐
│                   Application Layer                      │
│  NN Models, DPP Services, Business Logic, User Interfaces│
├─────────────────────────────────────────────────────────┤
│                     API Layer                            │
│     REST APIs, gRPC Services, GraphQL, Event Streams     │
├─────────────────────────────────────────────────────────┤
│                   Platform Layer                         │
│  Orchestration, Resource Mgmt, Service Discovery, Config │
├─────────────────────────────────────────────────────────┤
│                 Infrastructure Layer                     │
│    Compute, Storage, Network, Security, Observability    │
└─────────────────────────────────────────────────────────┘
```

### 4.2 Component Catalog

See [00_META/95-40-00-006_Software_Components_Registry.json](00_META/95-40-00-006_Software_Components_Registry.json) for the complete component catalog.

---

## 5. Data Architecture

### 5.1 Data Flows

**Training Pipeline:**
```
Raw Data → Feature Engineering → Feature Store → Training → Model Registry
```

**Inference Pipeline:**
```
Input → Pre-processing → Model Serving → Post-processing → Output
```

**DPP Pipeline:**
```
Event → Off-Chain Processing → Smart Contract → Blockchain → Query API
```

### 5.2 Data Stores

| Store Type | Technology | Purpose | Location |
|------------|------------|---------|----------|
| Relational | PostgreSQL | Structured metadata, configurations | Ground |
| Time-Series | InfluxDB, Prometheus | Metrics, telemetry | Ground |
| Object Storage | S3, MinIO | Models, datasets, artifacts | Ground |
| Cache | Redis | Session state, feature cache | Ground/Edge |
| Blockchain | Hyperledger Fabric | Immutable DPP records | Ground |
| Embedded DB | SQLite, FlatBuffers | Onboard cached data | Embedded |

---

## 6. Security Architecture

### 6.1 Security Principles

- **Zero Trust:** No implicit trust, verify every access
- **Defense in Depth:** Multiple layers of security controls
- **Least Privilege:** Minimum necessary permissions
- **Privacy by Design:** Data protection built-in from the start

### 6.2 Security Controls

| Layer | Controls |
|-------|----------|
| Network | Firewalls, VPNs, mTLS, network segmentation |
| Application | OAuth2/OIDC, RBAC, input validation, CSRF protection |
| Data | Encryption at rest (AES-256), in transit (TLS 1.3) |
| Infrastructure | IAM, secrets management, hardened containers |
| Audit | Comprehensive logging, SIEM integration, tamper-proof logs |

### 6.3 Threat Model

Documented in [95-40-06_Security_and_Privacy_Software](95-40-06_Security_and_Privacy_Software/).

---

## 7. Integration Architecture

### 7.1 Internal Integration

**Service-to-Service:**
- Synchronous: REST, gRPC
- Asynchronous: Event streaming (Kafka)
- Batch: File transfer, object storage

**Embedded Integration:**
- ARINC 653 APEX API for inter-partition communication
- ARINC 664 AFDX for network communication
- ARINC 429 for legacy avionics integration

### 7.2 External Integration

**Cloud Providers:**
- AWS, Azure, GCP for managed services
- Multi-cloud abstractions for portability

**Third-Party Systems:**
- MES (Manufacturing Execution Systems)
- ERP (Enterprise Resource Planning)
- Regulatory portals

**Standards Compliance:**
- ATA iSpec 2200
- S1000D for technical publications
- ACMS for onboard data export

---

## 8. Scalability and Performance

### 8.1 Scalability Strategy

**Horizontal Scaling:**
- Stateless services scale elastically
- Database read replicas for query load
- CDN for static assets

**Vertical Scaling:**
- GPU acceleration for model training and inference
- High-memory instances for large feature stores

**Partitioning:**
- Database sharding by tenant/aircraft
- Data lake partitioning by date/type

### 8.2 Performance Targets

| Service Type | Target Latency (p95) | Target Throughput |
|--------------|---------------------|-------------------|
| Online Inference | < 50ms | 1000 req/sec |
| Batch Inference | N/A | 100k predictions/min |
| API Queries | < 200ms | 500 req/sec |
| Blockchain Writes | < 5s (finality) | 100 tx/sec |
| Embedded Inference | < 10ms | 100 Hz |

See [95-40-02-004_Latency_and_Throughput_Constraints.md](95-40-02_Model_Serving_and_APIs/95-40-02-004_Latency_and_Throughput_Constraints.md) for detailed performance requirements.

---

## 9. Availability and Resilience

### 9.1 Availability Targets

| Service Tier | Availability SLA | Max Downtime/Year |
|--------------|------------------|-------------------|
| Critical (Production Inference) | 99.99% | 52 minutes |
| High (DPP Services) | 99.9% | 8.76 hours |
| Standard (Dev Tools) | 99.5% | 1.83 days |

### 9.2 Resilience Patterns

- **Circuit Breakers:** Prevent cascading failures
- **Bulkheads:** Isolate resource pools
- **Retry with Backoff:** Handle transient failures
- **Fallback:** Graceful degradation to backup systems
- **Health Checks:** Proactive failure detection

---

## 10. Software Boundaries and Scope

### 10.1 In-Scope

- All software directly implementing NN and DPP functionality
- Runtime platforms and infrastructure code
- Development tools and CI/CD pipelines
- Testing and simulation software
- Monitoring and observability stack

### 10.2 Out-of-Scope

- Operating system kernels (vendor-provided)
- Third-party commercial off-the-shelf (COTS) software
- Hardware firmware (unless NN/DPP-specific)
- General-purpose IT infrastructure (e.g., corporate network)

### 10.3 Interface Boundaries

Clearly defined interfaces to:
- Other ATA chapters (especially ATA 42 IMA)
- External vendors and suppliers
- Regulatory and certification authorities
- Cloud service providers

---

## 11. Technology Governance

### 11.1 Technology Radar

We maintain a technology radar categorizing technologies as:
- **Adopt:** Proven, production-ready
- **Trial:** Promising, pilot projects
- **Assess:** Watching, not yet committed
- **Hold:** Avoid for new projects

### 11.2 Approved Technologies

See [00_META/95-40-00-004_Software_Taxonomy.md](00_META/95-40-00-004_Software_Taxonomy.md) for the complete list of approved technologies.

---

## 12. Evolution and Migration

### 12.1 Architectural Evolution

- Quarterly architecture review board meetings
- Technology refresh cycles (3-5 years)
- Incremental migration strategies
- Backward compatibility maintenance

### 12.2 Legacy System Integration

- Adapter pattern for legacy interfaces
- Strangler fig pattern for gradual replacement
- API versioning for smooth transitions

---

## 13. References

### 13.1 Standards and Frameworks

- ISO/IEC 42010 (Systems and software engineering — Architecture description)
- DO-178C (Software Considerations in Airborne Systems and Equipment Certification)
- TOGAF (The Open Group Architecture Framework)
- 12-Factor App methodology

### 13.2 Related Documents

- [95-40-00-001 Software Overview](95-40-00-001_Software_Overview.md)
- [95-40-00-004 Software Taxonomy](00_META/95-40-00-004_Software_Taxonomy.md)
- [95-40-01-002 Runtime Architecture](95-40-01_Platform_and_Runtime/95-40-01-002_Runtime_Architecture.md)

---

## 14. Document Control

- **Owner:** Chief Software Architect
- **Approver:** Technical Director
- **Review Cycle:** Semi-annually
- **Next Review:** 2026-05-17

---

**END OF DOCUMENT**
