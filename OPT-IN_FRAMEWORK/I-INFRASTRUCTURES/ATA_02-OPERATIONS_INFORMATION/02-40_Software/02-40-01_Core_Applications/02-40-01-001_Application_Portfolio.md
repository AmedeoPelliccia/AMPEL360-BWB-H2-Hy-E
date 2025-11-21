# Application Portfolio

## Purpose

This document provides a structured overview of the **core application portfolio** that supports the AMPEL360 **ATA 02 – Operations Information** environment.

Its objectives are to:

- Identify the **main application families** within scope of `02-40-01_Core_Applications`.
- Describe how each family contributes to **flight operations, ground operations, energy, propulsion, and analytics** workflows.
- Provide an **entry point** into the detailed application-level documentation under `02-40-xx` (EFB, backend services, performance calculator, analytics, etc.).
- Support **architectural decisions, safety/criticality classification, lifecycle planning, and DevOps alignment**.
- Enable **traceability** between applications, data stores (02-60), schemas (02-90), and NN-based components (02-40-23 / ATA 95).

This document is written at **portfolio level** and is not intended to capture low-level implementation details.

---

## Scope

### In Scope

The Application Portfolio covers:

- All **core applications** represented under `02-40_Software`, with a focus on:
  - `02-40-01_Core_Applications` (this document)
  - EFB applications (`02-40-11`)
  - Backend services (`02-40-12`)
  - Performance and W&B engines (`02-40-13`, `02-40-14`)
  - Flight planning software (`02-40-15`)
  - Dispatch, weather, data recording, analytics, predictive ops, and integration middleware (`02-40-16` to `02-40-23`, `02-40-31`, `02-40-32`)
- Logical description of:
  - **Application domains** (Flight Ops, Ground Ops, Energy, Propulsion, Predictive Ops, DPP).
  - **Application tiers** (EFB/front-ends, web portals, backend microservices, batch/analytics jobs, NN/MLOps components).
  - **Operational criticality** (safety-critical vs business-critical vs supporting).
- High-level **relationships** to:
  - Storage and data platforms (02-60).
  - Tables, schemas and diagrams (02-90).
  - Energy and propulsion operations (02-70, 02-80).
  - NN and AI components (ATA 95; 02-40-23, 02-20-23).

### Out of Scope

The following are explicitly out of scope for this document:

- Detailed **class/module-level design** of any single application.
- Full specification of **APIs, schemas or message formats** (see 02-40-12, 02-40-32, 02-90-02).
- Detailed **CI/CD pipeline configuration** and infrastructure-as-code (see 02-40-41, 02-90-07).
- Detailed **test cases, coverage metrics and verification artefacts** (see 02-40-42, 02-90-12).

These details are captured in the respective subsystem documents and code repositories referenced from this portfolio.

---

## Content Sections

### Section 1 – Portfolio Overview and Taxonomy

This section provides a **high-level taxonomy** of the AMPEL360 application landscape as seen from ATA 02.

#### 1.1 Portfolio Views

The portfolio can be analysed through several complementary views:

1. **Domain View**  
   Grouping applications by primary operational domain:
   - **Flight Operations**: flight planning, dispatch, W&B, performance calculators, EFB apps.
   - **Ground Operations**: turnaround & GSE management, slot/ATFM integration, weather ingestion, dispatch tooling.
   - **Energy & Propulsion**: battery, fuel cell, electrical power, propulsion performance, energy optimisation.
   - **Data & Analytics**: data recording, analytics engine, monitoring and observability.
   - **Predictive & NN-based**: predictive operations, anomaly detection, maintenance and health monitoring models.
   - **Integration & Governance**: middleware, API management, DevOps, lifecycle management, documentation.

2. **Tier View**  
   Grouping by where and how applications run:
   - **Onboard / Edge**:
     - EFB applications (`02-40-11`)
     - Edge storage/processing components (`02-60-09`)
   - **Ground / Cloud**:
     - Backend services and APIs (`02-40-12`, `02-40-31`, `02-40-32`)
     - Analytics and predictive engines (`02-40-19`, `02-40-23`)
     - Digital twin and energy/propulsion monitoring (`02-70-10`, `02-80-14`)
   - **Hybrid**:
     - Applications that coordinate onboard and ground components (e.g. flight planning, performance, energy management).

3. **Criticality View**  
   Classification by operational and safety impact:
   - **Safety-critical**: functions that may be subject to DO-178C/DO-326A or equivalent (e.g. certain performance/W&B, power limits, health monitoring outputs used for safety decisions).
   - **Mission-critical**: functions with high operational impact (e.g. flight planning, dispatch, energy scheduling) but not directly safety-critical.
   - **Business-critical / Supporting**: dashboards, analytics, documentation tooling that support decision-making but are not directly safety- or mission-critical.

A full criticality mapping per application family is initiated in Section 2 and refined in downstream artefacts (e.g. `02-40-42-007_DO_178C_Verification.md`).

#### 1.2 Relationship to 02-40 Software Architecture

The **Software Architecture Overview** (`02-40-00-001`) defines the **technical architecture patterns** (microservices, event-driven flows, data lake, feature store, etc.).  

This portfolio document:

- Uses that architecture as a **backdrop**, but is organised by **application capability** rather than by infrastructure or pattern.
- Provides a **catalogue of “what exists”** (or is planned) in terms of applications that realise the technical architecture.
- Establishes **traceability** between applications and:
  - Their underlying **APIs** (`02-40-00-003`, `02-40-12`, `02-40-32`).
  - Their **data stores** (02-60).
  - Their **schemas and diagrams** (02-90).

#### 1.3 Relationship to Other OPT-IN Axes

While this document sits under the **I – Infrastructures** axis, application capabilities may:

- Consume **T – Training / NN artefacts** (e.g. 02-40-23 Predictive Ops software).
- Support **O – Operations** and **P – Product** axes (e.g. EFB apps used by crew, performance tools for flight preparation).
- Engage with **N – Neural Networks & DPP** components for traceability and digital product passports.

Formal cross-axis mapping is maintained elsewhere but referenced from this portfolio for navigation.

---

### Section 2 – Core Application Catalogue

This section lists the **main application families** under 02-40 and provides a portfolio-level summary. Detailed descriptions are in the corresponding subsystem documents (`02-40-xx-00x_*.md`).

#### 2.1 Portfolio Summary Table

The table below summarises the **key application families** in scope. It is intentionally high-level and will be elaborated as the architecture matures.

| App Family ID | Folder / Reference                            | Domain            | Criticality (Initial)    | Primary Users                           | Key Interfaces / Dependencies                                       |
| ------------- | --------------------------------------------- | ----------------- | ------------------------ | --------------------------------------- | -------------------------------------------------------------------- |
| APP-EFB-CORE  | `02-40-11_EFB_Software`                       | Flight Ops        | Mission-critical         | Flight crew                             | Performance calculator (02-40-13), W&B (02-40-14), Weather (02-40-17), Doc storage (02-60-07) |
| APP-BE-OPS    | `02-40-12_Backend_Services`                   | Cross-domain      | Mission-critical         | Dispatch, OCC, Ops engineering          | API Gateway (02-40-12), Storage (02-60), APIs (02-40-32, 02-90-02)   |
| APP-PERF      | `02-40-13_Performance_Calculator`             | Flight Ops        | Safety-critical (parts)  | Performance engineers, Flight crew      | Flight planning SW (02-40-15), Propulsion data (02-70-03), Tables (02-90-05) |
| APP-WB        | `02-40-14_Weight_Balance_System`              | Flight Ops        | Safety-critical          | Load control, Dispatch, Flight crew     | Aircraft config tables (02-90-05), Edge storage (02-60-09), EFB (02-40-11) |
| APP-FPL       | `02-40-15_Flight_Planning_Software`           | Flight Ops        | Mission-critical         | Dispatch, OCC                           | Weather processor (02-40-17), Propulsion/Energy data (02-70, 02-80), Slots/ATFM (02-20-15) |
| APP-DISP      | `02-40-16_Dispatch_Interface`                 | Flight Ops        | Mission-critical         | Dispatch, OCC                           | ACARS/SITA schemas (02-90-11), Backend services (02-40-12)          |
| APP-WX        | `02-40-17_Weather_Data_Processor`             | Flight & Ground   | Business-critical        | Flight planning, EFB, OCC               | External weather feeds, Time series storage (02-60-02), UI specs (02-90-10) |
| APP-ODR       | `02-40-18_Data_Recording_Service`             | Data & Analytics  | Mission-critical (post)  | Safety/occurrence investigators, Analytics | ATA 31 / FDR integration, Storage (02-60-02/06), DPP (02-60-08, 02-90-13) |
| APP-ANALYTICS | `02-40-19_Analytics_Engine`                   | Data & Analytics  | Business-critical        | Ops analysts, Engineering, Management   | Data storage (02-60), ML datasets (02-90-06), Dashboards (02-40-44) |
| APP-H2-OPS    | `02-40-21_H2_Operations_Software`             | Energy & Ground   | Mission-critical         | Ground Ops, Energy Ops, Safety          | H₂ infrastructure data (02-70-01, 02-80-04), DPP links (02-30-06, 02-90-13) |
| APP-PRED-OPS  | `02-40-23_Predictive_Ops_Software`            | Predictive & NN   | Mission/Business-critical| OCC, Dispatch, Ground Ops               | NN governance (ATA 95), Feature store (02-60-08, 02-90-06), Ops data (02-40-18) |
| APP-MW        | `02-40-31_Integration_Middleware`             | Integration       | Mission-critical         | All domains via APIs/events             | Message bus (Kafka, etc.), Async APIs (02-90-02), K8s/IaC (02-40-41, 02-90-07) |
| APP-API-MGMT  | `02-40-32_API_Management`                     | Integration       | Supporting / Business    | Platform, API owners, developers        | API catalog (02-40-00-003), OpenAPI specs (02-90-02), IAM (02-60-12) |
| APP-DEVOPS    | `02-40-41_DevOps_Infrastructure`              | Governance        | Supporting               | DevOps, Engineering                     | CI/CD workflows, Kubernetes/Terraform manifests (02-90-07)          |
| APP-QA        | `02-40-42_Testing_QA`                         | Governance        | Cross-cutting            | QA, Certification, Safety               | Test artefact schemas (02-90-12), Reports, Coverage dashboards      |
| APP-SEC       | `02-40-43_Security_Compliance`                | Governance        | Mission-critical (sec)   | Security, Compliance, Engineering       | IAM and encryption configs (02-60-12), Security policies, audit trails |
| APP-OBS       | `02-40-44_Monitoring_Observability`           | Governance        | Supporting               | Ops, SRE, DevOps                        | Metrics/logs/traces storage (02-60), dashboard configs (02-90-04)   |
| APP-DOCS      | `02-40-51_Documentation`                      | Governance        | Supporting               | All technical stakeholders              | ADRs, C4 models, references to 02-90 diagrams and schemas           |
| APP-LIFECYCLE | `02-40-52_Lifecycle_Management`               | Governance        | Supporting               | Product owners, Release managers        | Versioning strategy, release notes, roadmap; aligns with Git repos  |

This table is a **starting point**. Each entry is expected to be refined with:

- A unique **application identifier**.
- A link to the **authoritative documentation** and **code repository**.
- A more precise **safety and security classification**, validated with Safety, Certification and Security teams.

#### 2.2 Domain-Specific Subsections (Narrative Overview)

Below is a narrative summary of the most important domains.

##### 2.2.1 Flight Operations Applications

Key elements:

- **EFB Software (02-40-11)**  
  Provides pilot-facing functionality for performance calculations, W&B, weather visualisation and document viewing. Typically runs on certified tablets with offline capabilities and synchronises with backend services when connectivity is available.

- **Performance Calculator (02-40-13)** and **W&B System (02-40-14)**  
  Provide computational engines that may be:
  - Embedded in EFB clients.
  - Exposed as backend services (e.g. via `02-40-12` APIs).
  - Integrated with flight planning tools for route and fuel optimisation.

- **Flight Planning Software (02-40-15)** and **Dispatch Interface (02-40-16)**  
  Implement flight plan generation, optimisation and communication with external networks (ACARS, SITA), interacting closely with:
  - Weather processor (02-40-17).
  - Energy/propulsion information (02-70, 02-80).
  - Predictive Ops components (02-40-23, 02-20-23).

##### 2.2.2 Ground Operations & Energy Applications

- **Weather Data Processor (02-40-17)**  
  Normalises METAR, TAF and graphical weather feeds into standard schemas for use by:
  - Flight planning.
  - EFB and cockpit displays.
  - Predictive Ops and analytics.

- **Data Recording Service (02-40-18)**  
  Captures operational events, time series and logs, integrating with ATA 31/FDR and feeding:
  - Analytics engine (02-40-19).
  - ML datasets (02-90-06).
  - DPP and traceability systems (02-60-08, 02-90-13).

- **H₂ Operations Software (02-40-21)** and **Energy-related Apps (02-80-xx)**  
  Provide the operational interface for:
  - Ground H₂ refuelling procedures.
  - Energy budget management and optimisation.
  - Monitoring of battery and fuel cell systems, including health and degradation.

##### 2.2.3 Analytics, Predictive and NN-Enabled Applications

- **Analytics Engine (02-40-19)**  
  Supports:
  - Batch and real-time analytics.
  - Dashboards and reports for fleet, performance, energy and operations.

- **Predictive Ops Software (02-40-23)**  
  Implements MLOps pipelines, model training and serving for:
  - Delay prediction.
  - GSE allocation and turnaround risk.
  - Energy and propulsion optimisation.

It is governed by ATA 95 principles and uses:

- **ML Model Storage** (02-60-08).
- **Training datasets and feature definitions** (02-90-06).
- **DPP data structures** (02-90-13).

##### 2.2.4 Integration, API Management and Governance Applications

- **Integration Middleware (02-40-31)** and **API Management (02-40-32)**  
  Provide the backbone for:
  - Message-based integration between subsystems.
  - API exposure, security controls, rate limiting, and documentation.

- **DevOps Infrastructure (02-40-41)**, **Testing & QA (02-40-42)**, **Security & Compliance (02-40-43)**, **Monitoring & Observability (02-40-44)**  
  Are cross-cutting, enabling consistent lifecycle management and operational reliability across all application families.

- **Documentation (02-40-51)** and **Lifecycle Management (02-40-52)**  
  Provide:
  - Documentation standards, ADRs, architecture diagrams.
  - Release, versioning and end-of-life policies that apply to the entire portfolio.

---

### Section 3 – Lifecycle, Criticality and Governance

This section summarises **how the application portfolio is managed over time**, and how criticality is handled at portfolio level.

#### 3.1 Lifecycle States

Applications in the portfolio are managed through a common set of lifecycle states:

- **PLANNED**  
  - Business or technical need identified.  
  - High-level description exists in this Portfolio document and/or in roadmap artefacts (`02-40-52-A-201_Software_Roadmap.md`).  

- **IN DESIGN / DEVELOPMENT**  
  - Architecture documented under the relevant `02-40-xx` folder.  
  - Initial schemas and APIs registered in `02-90-xx`.  
  - CI/CD pipelines configured (`02-40-41`).  

- **OPERATIONAL**  
  - Deployed and in active use in one or more environments (test, staging, production).  
  - Monitored via observability stack (`02-40-44`).  
  - Covered by security, QA and compliance processes (`02-40-42`, `02-40-43`, `02-90-12`).  

- **DEPRECATED / RETIRED**  
  - Replaced or no longer needed.  
  - Kept for historical reference and traceability.  
  - Marked in portfolio table and lifecycle records (`02-40-52-005_End_of_Life_Policy.md`).  

Formal lifecycle tracking is expected to be captured in:

- The **Lifecycle Management** subsystem (`02-40-52`).
- Version control and release notes (`Release_Notes/`, `Changelog`).
- DPP entries for software (`02-90-13_Software_DPP_Schema`).

#### 3.2 Criticality and Safety Classification

At portfolio level, applications are classified by **criticality**:

- **Safety-critical**  
  - Applications whose failure could directly or indirectly affect flight safety (e.g. certain performance calculator functions, W&B computations, thrust limit calculations).
  - Likely subject to **DO-178C / DO-326A** processes and additional assurance requirements.
  - Strong coupling to ATA 95 where NN-based components participate in safety-related functions.

- **Mission-critical**  
  - Applications that are essential to operations, but not directly safety-critical (e.g. flight planning, dispatch interface, energy scheduling).
  - Require high availability, robust failure modes and clear fallbacks, but may not require full DO-178C compliance.

- **Business-critical / Supporting**  
  - Tools that support analytics, reporting, documentation, and governance (e.g. analytics dashboards, documentation generators).
  - Lower operational risk but important for efficiency, decision support and compliance reporting.

The **detailed per-application classification** will be:

- Maintained in the relevant subsystem documentation (e.g. `02-40-13-001_Calculator_Architecture.md`, `02-40-42-007_DO_178C_Verification.md`).
- Linked from this portfolio to ensure a **single consolidated view**.

#### 3.3 Governance and Traceability

Governance for the application portfolio includes:

- **Architecture Governance**  
  - Alignment with 02-40 Software Architecture Overview and architecture decision records (ADRs).
  - Use of standard patterns defined in `02-40-00-002_Software_Integration_Map.md` and `02-40-31_Integration_Middleware`.

- **Documentation Governance**  
  - Compliance with documentation standards (`02-40-51-001_Documentation_Standards.md`).  
  - Mandatory cross-references to relevant schemata, tables, and diagrams under 02-90.

- **Configuration & Change Management**  
  - Version control strategy (`02-40-52-002_Version_Control_Strategy.md`).  
  - Change and release management processes (`02-40-52-001_Release_Management.md`).

- **NN & DPP Traceability (where applicable)**  
  - For applications integrating NN/ML, adherence to ATA 95 and DPP structures:
    - Model definitions and artefacts stored under 02-60-08 and 02-90-06.
    - DPP schemas and blockchain anchors (`02-90-13_DPP_Data_Structures`).
  - Clear linkage between:
    - Application-level decisions.
    - Upstream data, models, and NN components.
    - Downstream operational and safety outcomes.

This portfolio document is expected to evolve as governance processes mature and as new applications are added or reclassified.

---

## References

- [Parent README](README.md)  
- [02-40-00-001 Software Architecture Overview](../02-40-00-001_Software_Architecture_Overview.md)  
- [02-40-00-004 Software Development Standards](../02-40-00-004_Software_Development_Standards.md)  
- Related subsystems (non-exhaustive):
  - `../02-40-11_EFB_Software/README.md`
  - `../02-40-12_Backend_Services/README.md`
  - `../02-40-13_Performance_Calculator/README.md`
  - `../02-40-14_Weight_Balance_System/README.md`
  - `../02-40-15_Flight_Planning_Software/README.md`
  - `../02-40-23_Predictive_Ops_Software/README.md`
  - `../../02-60_Storages/README.md`
  - `../../02-90_Tables_Schemas_Diagrams/README.md`

---

## Document Control

- **Generated with the assistance of AI (GitHub Copilot / ChatGPT), prompted by Amedeo Pelliccia**.  
- **Status**: DRAFT – Initial complete portfolio overview; subject to human review and enrichment.  
- **Human approver**: _[to be completed]_.  
- **Repository**: `AMPEL360-BWB-H2-Hy-E`  
- **Last AI update**: _2025-11-21_.  

---

**End of Document**
```

