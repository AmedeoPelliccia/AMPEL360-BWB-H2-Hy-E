# 02-40-11-001 — EFB App Architecture

## Purpose

This document defines the **end-to-end architecture** of the AMPEL360 **Electronic Flight Bag (EFB) application**, implemented primarily for iOS/iPadOS devices used by flight crew and, where applicable, ground/maintenance personnel.

It aims to:

- Describe the **high-level architecture and layering** of the EFB app.
- Define **module boundaries** (Performance, W&B, Weather, Documentation Viewer, etc.) and their responsibilities.
- Explain how the EFB app integrates with **backend services**, **onboard systems**, and **data storages** defined under `02-40_Software`, `02-60_Storages`, and `02-90_Tables_Schemas_Diagrams`.
- Capture **non-functional requirements** relevant to:
  - Offline operation and synchronization.
  - Security, integrity and device hardening.
  - Performance, usability, and operational robustness.
- Provide a **reference baseline** for detailed design documents:
  - `02-40-11-002_iOS_Application_Design.md`
  - `02-40-11-003_Offline_Data_Sync.md`
  - `02-40-11-004_Performance_Module.md`
  - `02-40-11-005_Weight_Balance_Module.md`
  - `02-40-11-006_Weather_Display_Module.md`
  - `02-40-11-007_Document_Viewer.md`
  - `02-40-11-008_User_Interface_Guidelines.md`

---

## Scope

### In Scope

- Logical architecture of the **EFB front-end application**, including:
  - UI and navigation structure (high-level).
  - Domain modules (performance, W&B, weather, documentation, etc.).
  - Data, sync and caching strategies for online/offline operation.
- Interactions with:
  - **Backend microservices** (`02-40-12_Backend_Services`, `02-40-31_Integration_Middleware`, `02-40-32_API_Management`).
  - **Storage systems** (`02-60_Storages`: document storage, time-series, model storage as relevant).
  - **Analytics and logging** (`02-40-19_Analytics_Engine`, `02-40-44_Monitoring_Observability`).
- High-level **security** aspects related to:
  - Authentication/authorization.
  - Data-at-rest and data-in-transit protection on EFB devices.
  - Device management (MDM/EMM) preconditions.

### Out of Scope

- Low-level **iOS implementation details** (class diagrams, specific frameworks, code-level decisions) – these are described in `02-40-11-002_iOS_Application_Design.md`.
- Detailed **UI specification** (layouts, pixel-level design) – covered in:
  - `02-40-11-008_User_Interface_Guidelines.md`
  - UI assets under `ASSETS/UI_Designs`.
- Detailed **performance algorithms** and **W&B formulas** – covered in:
  - `../02-40-13_Performance_Calculator/`
  - `../02-40-14_Weight_Balance_System/`
- Detailed **backend architecture** – covered in:
  - `../02-40-12_Backend_Services/`
  - `../02-40-31_Integration_Middleware/`
  - `../02-40-32_API_Management/`
- Certification artefacts (DO-178C evidence, test reports) – see:
  - `02-40-11-009_DO_178C_Evidence.md`
  - `02-40-11-010_Testing_Strategy.md`
  - Certification schemas in `02-90-12_Certification_Documentation_Schemas/`.

---

## 1. Architecture Overview

### 1.1 Logical Layering

The EFB application follows a **multi-layered architecture**:

1. **Presentation Layer (UI/UX)**
   - SwiftUI / UIKit screens and navigation flows.
   - UI state management (view models).
   - Application-specific design system consistent with AMPEL360 branding (`02-90-10_User_Interface_Specifications`).

2. **Domain Layer (Business Logic)**
   - Modules:
     - Performance (takeoff, landing, climb, cruise).
     - Weight & Balance (W&B).
     - Weather visualization (METAR/TAF, graphical weather).
     - Documentation viewer (OM, MEL, AMM extracts, ATAs).
     - Checklists and procedures (where applicable).
   - Domain models, validation rules, and computation orchestration.

3. **Data & Integration Layer**
   - API clients (REST/GraphQL) for backend services (`02-40-12_Backend_Services`).
   - Offline caches and synchronization engine (`02-40-11-003_Offline_Data_Sync.md`).
   - Local databases (e.g. SQLite/Core Data) and file stores (e.g. PDFs, manuals).
   - Serialization/deserialization using schemas from `02-90-01` and `02-90-02`.

4. **Platform & Infrastructure Layer**
   - Secure storage (keychain, protected containers).
   - Logging, analytics and telemetry clients.
   - Connectivity monitoring and environment configuration.
   - Integration with MDM/EMM, certificate stores and OS-level security features.

### 1.2 High-Level Data Flow (Conceptual)

```text
+----------------------------+      +----------------------------------------+
|        Flight Crew         |      |            Ground / Backend           |
| (EFB App: iPad / Tablet)   |      | (Ops, Dispatch, Performance, NN, etc) |
+----------------------------+      +----------------------------------------+
           |                                           ^
           | 1. User interaction                       |
           v                                           |
+----------------------------+                        |
|      Presentation Layer    |                        |
| (Views, ViewModels, Nav)   |                        |
+-------------+--------------+                        |
              | 2. Domain requests                    |
              v                                       |
+----------------------------+                        |
|        Domain Layer        |                        |
| (Perf, W&B, WX, Docs)      |                        |
+-------------+--------------+                        |
              | 3. Data & sync calls                  |
              v                                       |
+----------------------------+    4. API / Sync       |
|   Data & Integration Layer |------------------------+
| (API Clients, Cache, Sync) |   (via API Gateway,   |
+-------------+--------------+    Message Bus, etc.)  |
              | 5. Local storage                      |
              v                                       |
+----------------------------+
| Platform & Infrastructure  |
| (Local DB, Files, Security)|
+----------------------------+
````

---

## 2. Functional Modules and Responsibilities

The EFB app is structured into **functional modules** aligned with operational domains.

### 2.1 Performance Module

* Defined in detail in `02-40-11-004_Performance_Module.md`.
* Responsibilities:

  * Provide **takeoff, landing, climb and cruise performance** calculations for AMPEL360 BWB H₂ Hy-E variants.
  * Interface with:

    * Performance calculator backend (`../02-40-13_Performance_Calculator/`).
    * Aircraft configuration and performance tables (`02-90-05_Reference_Tables`).
  * Support:

    * Offline computation using onboard models/lookup tables.
    * Online refinement using backend-calculated data where connectivity is available.
  * Handle **what-if scenarios** (alternate runway, changed contamination, temperature, wind).

### 2.2 Weight & Balance (W&B) Module

* Defined in `02-40-11-005_Weight_Balance_Module.md`.
* Responsibilities:

  * Editable load sheet (passengers, cargo, fuel) and resulting **CG envelope**.
  * Integration with:

    * W&B core engine (`../02-40-14_Weight_Balance_System/`).
    * Aircraft configuration data (`02-90-05-A-101_Weight_Balance_Config.yaml`).
  * Provide:

    * Visual CG envelope and margins.
    * Export of final load sheet to backend / operational systems (dispatch, ground handling).

### 2.3 Weather Display Module

* Defined in `02-40-11-006_Weather_Display_Module.md`.
* Responsibilities:

  * Display METAR/TAF and other relevant meteorological data.
  * Integrate with:

    * Weather data processor backend (`../02-40-17_Weather_Data_Processor/`).
    * Weather schemas (`02-90-03_Data_Exchange_Formats`, `02-90-01_A-103_Weather_Data_Schema.json`).
  * Provide:

    * Textual and graphical weather views.
    * Basic filtering by route, alternates, time horizon.

### 2.4 Documentation Viewer

* Defined in `02-40-11-007_Document_Viewer.md`.
* Responsibilities:

  * Provide **searchable access to manuals and operational documents**:

    * OM-A/B, QRH, MEL, CDL, operational bulletins, etc.
  * Integrate with document storage and metadata:

    * `02-60-07_Document_Storage/`.
    * `02-90-07_Configuration_Manifests` for repository structure where applicable.
  * Support:

    * Offline document availability.
    * Incremental updates (deltas) distributed from ground.

### 2.5 Shared Utilities

* Common components used by all modules:

  * Flight selection and context (active flight, departure/arrival, alternates).
  * Crew identity and role (captain, FO, instructor).
  * Theme and locale settings.
  * Connectivity status and sync indicators.

---

## 3. Application Layers in Detail

### 3.1 Presentation Layer

* Technologies:

  * SwiftUI (preferred) and/or UIKit where required.
* Patterns:

  * MVVM or similar state management pattern:

    * Views consume observable view models.
    * View models orchestrate domain layer use cases.
* Navigation:

  * Root home/dashboard view.
  * Module-specific navigation stacks:

    * Performance
    * W&B
    * Weather
    * Documentation
    * Settings & Sync

Key requirements:

* Clear indication of:

  * Online vs offline state.
  * Data staleness (e.g. “Weather data: 15 min old”).
  * Sync status and completeness of dataset (performance, manuals, etc.).
* Consistent **UX patterns** across modules, guided by:

  * `02-40-11-008_User_Interface_Guidelines.md`.
  * Design tokens and components from `02-90-10_User_Interface_Specifications`.

### 3.2 Domain Layer

* Encapsulates **use cases / interactors**, such as:

  * “Compute takeoff performance for active flight and selected runway.”
  * “Recalculate W&B after passenger reassignment.”
  * “Retrieve and cache weather for current route.”
  * “Open document section for specific ATA / DMC code.”
* Domain objects:

  * `FlightContext`, `AircraftVariant`, `RunwayCondition`, `LoadSheet`, `WeatherSnapshot`, etc.
* Rules:

  * No direct UI or OS dependencies.
  * Only depends on:

    * Domain interfaces for repositories and services.
    * Pure business logic and validation libraries.

### 3.3 Data & Integration Layer

Responsibilities:

* **API Clients**:

  * REST/GraphQL clients for:

    * Flight Planning services (`../02-40-15_Flight_Planning_Software/`).
    * Weather data (`../02-40-17_Weather_Data_Processor/`).
    * Performance calculator and W&B backend (where applicable).
    * Ops & Analytics services (`../02-40-18_Data_Recording_Service/`, `../02-40-19_Analytics_Engine/`).
  * Contracts aligned with `02-90-02_API_Specifications`.

* **Local Storage**:

  * Cached datasets:

    * Performance tables / models relevant to current variant and base.
    * W&B configurations.
    * Manuals and documentation.
    * Weather snapshots and route information.
  * Use of:

    * SQLite/Core Data for structured data.
    * Local file storage for PDFs/attachments.
    * Secure storage (Keychain) for secrets and tokens.

* **Synchronization Engine**:

  * Detailed in `02-40-11-003_Offline_Data_Sync.md`.
  * Tasks:

    * Pull updated datasets from backend (delta updates).
    * Resolve conflicts and partial downloads.
    * Maintain sync logs for audit and troubleshooting.

### 3.4 Platform & Infrastructure Layer

* Device capabilities:

  * Network reachability and QoS.
  * Secure storage and key management.
* Integration points:

  * MDM/EMM profiles for:

    * App distribution and revocation.
    * Device encryption and jailbreak detection (where applicable).
  * Logging and telemetry clients feeding:

    * `../02-40-44_Monitoring_Observability/`.
    * `../02-40-19_Analytics_Engine/`.

---

## 4. Data Flows and Integration

### 4.1 Pre-Flight Data Sync Flow

Typical pre-flight sync (on ground, connected):

1. User opens EFB app in **pre-flight** phase.
2. App validates:

   * Device registration and crew identity.
   * Validity of local datasets (performance, manuals, weather).
3. Sync engine:

   * Fetches:

     * Latest manuals and bulletins.
     * Updated performance and W&B data for assigned aircraft.
     * Route and FPL from Flight Planning backend.
     * Weather data (METAR/TAF, SIGMET, etc.).
4. Modules consume updated datasets to provide:

   * Performance computations.
   * W&B computation and CG verification.
   * Weather overlay for route.

### 4.2 In-Flight Operation (Offline-first)

* EFB is expected to operate primarily **offline** in flight:

  * All essential datasets (performance, W&B, documentation for assigned aircraft and route) must be available locally.
* Any **in-flight connectivity** (if present) is treated as:

  * Optional enhancement for:

    * Updated weather.
    * Updated NOTAMs or operational messages.
    * Telemetry backhaul.

### 4.3 Post-Flight Data Upload

* After landing and once connectivity is restored:

  * App can upload:

    * Logs of performance/W&B calculations used.
    * Crew actions (e.g., manual overrides, what-if scenarios executed).
    * App usage telemetry (for UX and performance improvement).
  * Data is routed via:

    * API Gateway (`../02-40-32_API_Management/`).
    * Integration Middleware (`../02-40-31_Integration_Middleware/`).
    * Stored in:

      * Operational data recording (`../02-40-18_Data_Recording_Service/`).
      * Analytics and ML training datasets (`../02-40-19_Analytics_Engine/`, `02-90-06_ML_Training_Datasets`).

---

## 5. Security and Compliance

### 5.1 Security Objectives

* Maintain **confidentiality**, **integrity** and **availability** of operational data on EFB devices.
* Enforce strict **access control** and **identity verification**.
* Support **regulatory and certification** requirements (e.g., DO-326A for airborne information security, where applicable).

### 5.2 Key Mechanisms

* **Authentication & Authorization**:

  * Integration with identity provider (IdP) via secure protocols (e.g. OAuth2/OIDC).
  * Role-based access control (RBAC) for:

    * Crew roles (captain, FO).
    * Additional roles (instructor, examiner, maintenance).
* **Data Protection**:

  * Full device encryption, enforced through MDM policies.
  * In-app:

    * Keychain for sensitive tokens and credentials.
    * Encrypted local storage for operational datasets, where feasible.
* **Secure Communications**:

  * TLS 1.2+ for all network communication.
  * Certificate pinning and/or mutual TLS where mandated by security architecture (`../02-40-43_Security_Compliance/`).
* **Hardening**:

  * Jailbreak/root detection mechanisms (where supported).
  * Restricted debugging/logging in production builds.

### 5.3 Auditability and Traceability

* All critical operations (e.g., performance calculation used for takeoff, W&B approval) should:

  * Generate local logs.
  * Be synchronized to backend logs under:

    * `../02-40-18_Data_Recording_Service/`.
    * Certification-related schemas (`02-90-12`).
* Logs should be traceable by:

  * Flight ID, aircraft registration, crew ID, and EFB device ID.
  * Version of performance/W&B algorithms and datasets used.

---

## 6. Performance, Reliability, and UX Considerations

### 6.1 Performance Targets

* **Startup time**: within defined threshold for operational readiness (target specified in `02-40-11-010_Testing_Strategy.md`).
* **Computation latency**:

  * Local performance/W&B calculations should return in **sub-second** times for typical scenarios.
* **Responsiveness**:

  * UI should remain responsive during sync operations (background tasks, progress indicators).

### 6.2 Reliability and Error Handling

* **Graceful degradation**:

  * If certain non-critical datasets are missing or outdated, EFB must:

    * Clearly indicate affected features.
    * Allow safe operation for remaining capabilities.
* **Error classification**:

  * User-facing messages vs. detailed technical logs.
* **Recovery flows**:

  * Clear user guidance when:

    * Sync fails.
    * Required datasets are missing for a specific operation (e.g. attempting performance calc for aircraft/airport combination not downloaded).

### 6.3 Usability

* Designed for:

  * **High workload environments** (e.g., pre-flight, taxi).
  * Use with gloves or in turbulent conditions (touch targets, contrast).
* UX guidelines:

  * High contrast and readability.
  * Minimal steps for critical workflows (e.g. final performance check).
  * Clear indicators of **finality** (e.g., “Performance data APPROVED for Flight XYZ”).

---

## 7. Extensibility and Configuration

### 7.1 Modular Feature Flags

* Ability to **enable/disable modules** per:

  * Operator contract.
  * Certification status of specific features (e.g., new NN-based advisory).
* Centralized configuration:

  * Retrieved from backend configuration service or manifest (`02-90-07_Configuration_Manifests`).

### 7.2 Multi-Operator Support

* Architecture must allow:

  * Custom branding and minor workflow variations per operator.
  * Separation of operator-specific settings and content, under appropriate namespaces and storage segregation.

---

## References

* [02-40-11 EFB Software README](README.md)
* [02-40-00-001 Software Architecture Overview](../02-40-00-001_Software_Architecture_Overview.md)
* [02-40-00-004 Software Development Standards](../02-40-00-004_Software_Development_Standards.md)

Related:

* `02-40-11-002_iOS_Application_Design.md`
* `02-40-11-003_Offline_Data_Sync.md`
* `02-40-11-004_Performance_Module.md`
* `02-40-11-005_Weight_Balance_Module.md`
* `02-40-11-006_Weather_Display_Module.md`
* `02-40-11-007_Document_Viewer.md`
* `02-40-11-008_User_Interface_Guidelines.md`
* `../02-40-12_Backend_Services/README.md`
* `../02-40-31_Integration_Middleware/README.md`
* `../02-40-32_API_Management/README.md`
* `../../02-60_Storages/README.md`
* `../../02-90_Tables_Schemas_Diagrams/README.md`

---

## Document Control

* **Generated with the assistance of AI (GitHub Copilot / ChatGPT), prompted by Amedeo Pelliccia**.
* **Status**: DRAFT – Initial EFB app architecture baseline; detailed refinement pending.
* **Human approver**: *[to be completed]*.
* **Repository**: `AMPEL360-BWB-H2-Hy-E`
* **Last AI update**: *2025-11-21*.

---

**End of Document**

```
::contentReference[oaicite:0]{index=0}
```
