# Microservices Architecture

## Purpose

This document defines the **microservices architecture** for the AMPEL360 **ATA 02 – Operations Information** ecosystem.

Its objectives are to:

- Describe the **architectural principles and patterns** governing microservice design and deployment.
- Define **service boundaries, domains and interaction patterns** across Flight Ops, Ground Ops, Energy, Propulsion, Analytics and NN-based services.
- Provide a **reference model** for implementing applications under `02-40_Software` (especially `02-40-01_Core_Applications`, `02-40-12_Backend_Services`, `02-40-31_Integration_Middleware`, `02-40-32_API_Management`).
- Support **safety, security, performance and lifecycle requirements**, including alignment with ATA 95 NN governance, DO-178C/DO-326A principles and DPP traceability.

This document is intentionally **technology-agnostic** (no binding to a specific vendor or platform) and focuses on the logical and structural aspects of the architecture.

---

## Scope

### In Scope

- The **backend microservices layer** implementing AMPEL360 operational capabilities, including but not limited to:
  - Flight operations services (FPL, performance, W&B, dispatch, weather).
  - Ground operations services (turnaround, GSE, slot/ATFM integration).
  - Energy and propulsion information services (battery, H₂, fuel cell, power budgets).
  - Data recording, analytics, NN/MLOps and digital twin services.
- **Integration and communication patterns**:
  - Synchronous APIs (REST/gRPC, GraphQL).
  - Asynchronous messaging and event streaming (Kafka or equivalent).
- **Cross-cutting concerns**:
  - Security, authentication/authorization.
  - Observability (logging, metrics, tracing).
  - Resilience, fault tolerance, back-pressure.
  - Configuration and service discovery.
- Relationships with:
  - Storage platforms (`02-60_Storages`).
  - Schemas, tables and diagrams (`02-90_Tables_Schemas_Diagrams`).
  - DevOps and lifecycle (`02-40-41_DevOps_Infrastructure`, `02-40-52_Lifecycle_Management`).

### Out of Scope

- Detailed **class-level implementation** or specific programming language frameworks.
- Detailed **deployment manifests** (Kubernetes, Helm, Terraform) – covered in `02-40-41` and `02-90-07`.
- Detailed **API specifications and payloads** – covered in `02-40-12_Backend_Services`, `02-40-32_API_Management`, `02-90-02_API_Specifications`.
- Detailed **NN model internals** and certification artefacts – covered under ATA 95 and related documentation (`ATA_95_NEURAL_NETWORKS`, `02-40-23_Predictive_Ops_Software`).

---

## Content Sections

1. Microservices Architecture Overview  
2. Service Taxonomy and Bounded Contexts  
3. Communication Patterns and API Design  
4. Cross-Cutting Concerns (Security, Observability, Resilience)  
5. Deployment, Environments and Lifecycle Governance  

---

## 1. Microservices Architecture Overview

### 1.1 Architectural Style

AMPEL360 adopts a **microservices-first** backend architecture with the following characteristics:

- **Domain-aligned services**: Each microservice encapsulates a **bounded context** (e.g. Flight Planning, Turnaround, Energy Budgeting, Predictive Ops).
- **Independent deployability**: Services can be deployed, scaled and upgraded independently, within the constraints of safety and certification requirements.
- **API-driven integration**: All communication (synchronous and asynchronous) occurs via **well-defined contracts** registered under `02-90-02_API_Specifications`.
- **Event-driven collaboration**: Operational events (flight status, turnaround updates, energy state changes, NN outputs) are propagated through **event streams** managed by `02-40-31_Integration_Middleware`.
- **Polyglot persistence**: Each service can own the storage pattern that best fits its needs (relational, time-series, object, key-value), with schemas catalogued in `02-90-01_Database_Schemas` and `02-60_Storages`.

### 1.2 Alignment with 02-40 Software Architecture Overview

This document refines the high-level view described in:

- `../02-40-00-001_Software_Architecture_Overview.md`
- `../02-40-00-002_Software_Integration_Map.md` (if present)

The microservices architecture is the **logical realization** of the following:

- **Core Applications (02-40-01)**: Portfolio of business capabilities mapped to services.
- **Backend Services (02-40-12)**: Concrete microservices implementing those capabilities.
- **Integration Middleware (02-40-31)**: Message bus/event streaming fabric connecting services.
- **API Management (02-40-32)**: Gateway, security, rate limiting and developer portal.

### 1.3 Design Principles

Core principles:

1. **Single Responsibility per Service**  
   - Each service owns a **coherent business capability** (e.g. `TurnaroundOrchestrator`, `EnergyBudgetService`, `PerformanceCalculatorService`).
   - Avoid “god services” that aggregate unrelated domains.

2. **Autonomous Data Ownership**  
   - Each service owns its **data model** and storage and exposes data via APIs or domain events.
   - Cross-service data access occurs via **APIs/events** rather than direct database access.

3. **Explicit Contracts**  
   - All service interfaces are defined and versioned via:
     - OpenAPI / GraphQL / AsyncAPI artefacts (`02-90-02`).
     - Protobuf/JSON schemas for internal messages (`02-90-03_Data_Exchange_Formats`).

4. **Resilience by Design**  
   - Use:
     - Timeouts, retries and circuit breakers.
     - Bulkheads and fallback handlers.
     - Idempotent operations for message re-processing.

5. **Security by Default**  
   - All service calls authenticated and authorised via:
     - API gateway, identity provider, mutual TLS (as applicable).
   - Sensitive data encrypted at rest and in transit, aligned with `02-40-43_Security_Compliance` and `02-60-12_Storage_Security`.

6. **Observability and Traceability**  
   - Every service emits structured logs, metrics and traces per `02-40-44_Monitoring_Observability`.
   - Correlation IDs used across services to trace end-to-end flows (e.g. per flight or turnaround ID).

7. **Safety-Aware Segregation**  
   - Safety-critical functions are segregated:
     - Separate deployment domains.
     - Limited dependencies on non-critical services.
     - Clear fallbacks to deterministic behaviour when NN/analytics components are unavailable (ATA 95 expectations).

---

## 2. Service Taxonomy and Bounded Contexts

### 2.1 Domain-Based Service Groups

The following table outlines key **microservice groups** and their primary bounded contexts (indicative, non-exhaustive):

| Domain               | Example Services (Logical)                     | Source Folder(s)                         |
| -------------------- | ---------------------------------------------- | ---------------------------------------- |
| Flight Planning      | `FlightPlanService`, `RouteOptimizerService`   | `02-40-15_Flight_Planning_Software`      |
| Performance & W&B    | `PerfCalcService`, `WBService`                 | `02-40-13`, `02-40-14`                   |
| Dispatch & Messaging | `DispatchInterfaceService`, `AcarsGateway`     | `02-40-16_Dispatch_Interface`            |
| Weather              | `WeatherIngestionService`, `WeatherQueryAPI`   | `02-40-17_Weather_Data_Processor`        |
| Data Recording       | `OpsEventRecorder`, `TimeSeriesIngestor`       | `02-40-18_Data_Recording_Service`        |
| Analytics            | `OpsAnalyticsService`, `ReportingService`      | `02-40-19_Analytics_Engine`              |
| H₂ Operations        | `H2RefuelingCoordinator`, `H2SafetyMonitor`    | `02-40-21_H2_Operations_Software`        |
| Predictive Ops (NN)  | `DelayPredictorAPI`, `TurnaroundRiskScorer`    | `02-40-23_Predictive_Ops_Software`       |
| Integration          | `EventRouter`, `TransformationService`         | `02-40-31_Integration_Middleware`        |
| API Management       | `APIGateway`, `DeveloperPortal`                | `02-40-32_API_Management`                |
| DevOps/Platform      | `CIOrchestrator`, `DeploymentOrchestrator`     | `02-40-41_DevOps_Infrastructure`         |
| Security             | `AuthService`, `PolicyEnforcer`                | `02-40-43_Security_Compliance`           |
| Observability        | `LogAggregator`, `MetricsCollector`, `Tracer`  | `02-40-44_Monitoring_Observability`      |

These logical services may map to one or more **deployable microservice instances** depending on performance, safety, and organisational constraints.

### 2.2 Bounded Contexts and Data Ownership

Each service group defines its own **bounded context**, including:

- Domain model (entities, value objects, aggregates).
- Local persistence (schemas in `02-90-01`, storage in `02-60`).
- Business rules and invariants.

Example:

- `FlightPlanService`:
  - Owns `FlightPlan`, `Route`, `Alternate`, `FuelPlan` entities.
  - Uses PostgreSQL schemas (e.g. `02-90-01-A-002_Performance_Data_Schema.sql`) and object storage for attachments (e.g. `02-60-03_Object_Storage`).
  - Publishes events like `FPL.CREATED`, `FPL.UPDATED`, `FPL.CANCELLED`.

- `TurnaroundOrchestrator`:
  - Owns `Turnaround`, `GSEAllocation`, `TaskStatus`.
  - Uses time-series storage for status ticks (e.g. `02-60-02_Time_Series_Storage`).
  - Publishes `TURNAROUND.STATUS_UPDATED`, `GSE.ALLOCATION_CHANGED`.

### 2.3 Safety-Critical vs Non-Critical Segregation

Where services implement **safety-related functions** (e.g. performance limits, W&B, certain NN-assisted recommendations), the architecture introduces:

- **Separated trust zones**:
  - Critical zone: services with stricter safety and cybersecurity requirements.
  - Non-critical zone: analytics, dashboards, planning tools, etc.
- **Controlled interfaces**:
  - Data flowing into critical zone constrained to validated channels.
  - Outputs from non-critical services treated as **advisory** in critical systems, with deterministic backups available.

This segregation is documented in:

- Safety and certification artefacts (`02-40-42-007_DO_178C_Verification.md`, ATA 95 artefacts).
- Network and deployment diagrams (`02-90-04_System_Architecture_Diagrams`).

---

## 3. Communication Patterns and API Design

### 3.1 Synchronous vs Asynchronous Communication

The architecture combines:

1. **Synchronous APIs** (REST/gRPC/GraphQL):
   - Used for:
     - Querying current state (e.g. “get flight plan”, “get weather snapshot”).
     - User-driven operations requiring immediate feedback (EFB, portals, OCC tools).
   - Described in:
     - OpenAPI / GraphQL specs under `02-90-02_API_Specifications`.
     - Managed and exposed via `02-40-32_API_Management`.

2. **Asynchronous Messaging / Event Streaming**:
   - Used for:
     - Publishing domain events (e.g. flight state, turnaround status, energy consumption ticks).
     - Broadcasting NN predictions and recommendations.
     - Decoupling producers and consumers.
   - Described in:
     - AsyncAPI specifications (`02-90-02-003_AsyncAPI_Event_Schemas.md`).
     - Kafka/MQTT topics definitions (`02-90-02-A-201_Kafka_Topics_Spec.yaml`, `02-90-03` Protobuf schemas).

Guideline:

- Prefer **asynchronous events** for **state changes and alerts**.
- Use **synchronous calls** for **commands and on-demand queries**.

### 3.2 API Versioning and Compatibility

Key rules:

- All public APIs are **versioned** (e.g. `/api/v1/flight-plans`).
- Breaking changes require:
  - New major version (e.g. v2).
  - Parallel support period defined in lifecycle policies (`02-40-52-001_Release_Management.md`).
- Schema changes are:
  - Documented via `02-90-02` specs and `02-90-00-004_Schema_Version_Control.md`.
  - Communicated via release notes and API documentation (`02-40-32-005_API_Documentation.md`).

### 3.3 Idempotency and Reliability

For operations executed via HTTP or messaging:

- **Idempotent methods** (GET, PUT, DELETE) must not change system state when retried.
- Non-idempotent operations (e.g. POST) should use:
  - Correlation IDs or idempotency keys to safely handle retries.
  - Exactly-once or at-least-once semantics, with idempotent consumers on the event stream.

Patterns such as **outbox** and **saga** are used for long-running, cross-service transactions (e.g. coordinating flight plan changes, turnaround updates, energy budgets).

### 3.4 Event Naming and Contract Governance

- Event types follow a consistent naming convention, e.g.:
  - `FPL.CREATED`, `FPL.UPDATED`, `TURNAROUND.STATUS_UPDATED`, `ENERGY.BUDGET_CHANGED`, `NN.PREDICTION.ISSUED`.
- Event payloads:
  - Use schemas stored under `02-90-03_Data_Exchange_Formats` and `02-90-06_ML_Training_Datasets` where applicable.
  - Include **metadata** (timestamp, source system, correlation ID, trace ID, model version for NN outputs).

`02-40-31_Integration_Middleware` is responsible for:

- Validating events against schemas.
- Routing events to appropriate topics/queues.
- Handling dead-letter queues and re-processing.

---

## 4. Cross-Cutting Concerns (Security, Observability, Resilience)

### 4.1 Security and Compliance

Microservices must comply with:

- `02-40-43_Security_Compliance` (security architecture, authentication/authorization, encryption).
- `02-60-12_Storage_Security` (encryption at rest, key management).
- Regulatory and certification requirements documented in:
  - `02-90-12_Certification_Documentation_Schemas`.
  - Security policies under `Security_Policies/`.

Key patterns:

- **Zero-trust approach** within the cluster:
  - Mutual TLS for service-to-service calls.
  - Service identities managed by the platform (e.g. SPIFFE/SPIRE) where applicable.
- **OAuth2/OIDC/JWT** for user-facing APIs.
- **Fine-grained authorization** enforced at:
  - API gateway level (coarse-grained).
  - Service level for domain-specific rules (fine-grained).

### 4.2 Observability

Per `02-40-44_Monitoring_Observability`:

- Every microservice must:
  - Emit structured logs with correlation IDs.
  - Expose metrics (e.g. Prometheus format) for:
    - Latency, throughput, error rates.
    - Domain-specific KPIs (e.g. number of flight plans, delay prediction calls).
  - Support distributed tracing (e.g. OpenTelemetry), propagating trace context across API and message boundaries.

Dashboards and alerts:

- Configured under `Dashboards/` and `Alerts/` in `02-40-44` and `02-60-13_Storage_Monitoring`.
- Must cover:
  - Service health (SLOs/SLIs).
  - Capacity patterns.
  - Error trends and anomalies.

### 4.3 Resilience and Fault Tolerance

Mandatory resilience mechanisms:

- **Timeouts** for all remote calls (no unbounded waits).
- **Retries with backoff** for transient failures.
- **Circuit breakers** to prevent cascading failures.
- **Bulkheads** to isolate failures per dependency where justified.

Fallback strategies:

- For NN-based services:
  - When predictions are unavailable or low-confidence, fall back to **deterministic rule-based logic** with clear indication to the user (per ATA 95 expectations).
- For external dependencies (e.g. third-party weather providers):
  - Multi-provider strategies where possible.
  - Graceful degradation (e.g. using last known good data with validity annotations).

---

## 5. Deployment, Environments and Lifecycle Governance

### 5.1 Deployment Model

Microservices are deployed on a **container-orchestrated platform** (e.g. Kubernetes), as described in:

- `02-40-41_DevOps_Infrastructure`
- `02-90-07_Configuration_Manifests` (Kubernetes, Helm, Terraform manifests)

Key characteristics:

- **Environment separation**:
  - DEV, TEST, STAGING, PROD at a minimum.
  - Possibly additional pre-certification or “safety validation” environments for critical services.

- **Deployment patterns**:
  - Rolling updates or blue/green deployments.
  - Canary releases for selected services (typically non-safety-critical).

### 5.2 CI/CD and Quality Gates

CI/CD pipelines (see `02-40-41-002_CI_CD_Pipeline.md`) enforce:

- Automated build, test and security scanning.
- Deployment to non-production environments.
- Promotion rules to production based on:
  - Test suite results (aligned with `02-40-42_Testing_QA`).
  - Code coverage and static analysis.
  - Security checks and compliance gates.

For safety-critical or regulated services:

- Additional manual reviews and approvals are expected.
- Traceable links to verification evidence (`02-90-12_Certification_Documentation_Schemas`).

### 5.3 Versioning, Rollback and Decommissioning

Lifecycle practices (see `02-40-52_Lifecycle_Management`) include:

- **Semantic versioning** for services and APIs.
- **Release notes** and **changelogs**:
  - Documented in `Release_Notes/` and `Changelog` artefacts under `02-40-52`.
- **Rollback strategies**:
  - Ability to revert to previous stable versions with minimal downtime.
- **Decommissioning**:
  - Controlled retirement of services with:
    - Migration of data to successor services.
    - Update of clients to new endpoints.
    - Update of DPP entries and documentation to reflect retirement.

---

## References

- [Parent README](README.md)  
- [02-40-00-001 Software Architecture Overview](../02-40-00-001_Software_Architecture_Overview.md)  
- [02-40-00-004 Software Development Standards](../02-40-00-004_Software_Development_Standards.md)  

Related:

- `../02-40-01_Core_Applications/02-40-01-001_Application_Portfolio.md`  
- `../02-40-12_Backend_Services/README.md`  
- `../02-40-31_Integration_Middleware/README.md`  
- `../02-40-32_API_Management/README.md`  
- `../02-40-41_DevOps_Infrastructure/README.md`  
- `../02-40-44_Monitoring_Observability/README.md`  
- `../../02-60_Storages/README.md`  
- `../../02-90_Tables_Schemas_Diagrams/README.md`  
- ATA 95 NN & DPP artefacts as applicable.

---

## Document Control

- **Generated with the assistance of AI (GitHub Copilot / ChatGPT), prompted by Amedeo Pelliccia**.  
- **Status**: DRAFT – Initial microservices architecture description; subject to human review and refinement.  
- **Human approver**: _[to be completed]_.  
- **Repository**: `AMPEL360-BWB-H2-Hy-E`  
- **Last AI update**: _2025-11-21_.  

---

**End of Document**
```

