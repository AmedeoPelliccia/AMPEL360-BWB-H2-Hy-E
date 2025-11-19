# 02-20-01_Digital_Ops_Platform — Core Digital Operations Platform

**Subsystem ID:** 02-20-01  
**Group:** [02-20_Subsystems](../README.md)  
**ATA Chapter:** [ATA_02-OPERATIONS_INFORMATION](../../README.md)  
**Axis:** I — Infrastructures  
**Status:** FRAMEWORK_DEFINED  

---

## 1. Purpose

The **Digital Ops Platform** is the **core backbone** for AMPEL360 digital
operations:

- Provides a **shared data and services layer** for all 02-20 subsystems  
- Normalises, stores and distributes **operational data** (flights, turnarounds,
  H₂ operations, performance, W&B, etc.)  
- Exposes **APIs, events and streams** to:
  - Onboard tools (EFB, W&B, performance)  
  - Ground systems (flight planning, dispatch, AOC)  
  - CAOS / AirCCC analytics and dashboards  
  - ATA 95 NN-based services  

It is not a user-facing app; it is the **platform under the apps**.

---

## 2. Scope

Included in this subsystem:

- **Data layer** for 02-20:
  - Storage of operational entities (flights, legs, sectors, turnarounds, events)
  - Time series and KPI history
  - Metadata, lineage and DPP hooks
- **Service layer**:
  - REST / gRPC / event streams for other 02-20 subsystems
  - Authentication, authorization, auditing
  - Schema registry and validation
- **Integration layer**:
  - Connectors to aircraft-side data (via ATA 42 / AOC gateways)
  - Connectors to ground-side systems (planning, dispatch, GSE)
  - Connectors to CAOS and ATA 95 inference endpoints
- **Observability**:
  - Logging, metrics and traces for platform and subsystems
  - Health dashboards feeding CAOS / AirCCC where appropriate

Out of scope:

- Detailed functional logic of consumer subsystems (EFB, W&B, performance, etc.)  
  → See their own `02-20-XX_…/README.md`  
- UI design for flight deck, dispatch or management  
  → Owned by each app subsystem (11, 13, 14, 15, 16, 19, 22…)  
- Internal CAOS microservice architecture  
  → See `/CAOS` documentation  

---

## 3. Position in the Architecture

The Digital Ops Platform sits **between**:

- **Subsystems in 02-20**  
  (`02-20-11`, `…12`, `…13`, `…14`, `…15`, `…16`, `…17`, `…18`, `…19`, `…21`, `…22`, `…23`)  
- And **external consumers / producers**:
  - Aircraft-side systems via ATA 42 / AOC interfaces  
  - Ground systems (planning, dispatch, GSE, maintenance)  
  - CAOS / AirCCC  
  - ATA 95 NN services  

Relations:

- Parent overview:  
  → [`../02-20-00-001_Subsystems_Overview.md`](../02-20-00-001_Subsystems_Overview.md)  
- Integration map:  
  → [`../02-20-00-002_Subsystems_Integration_Map.md`](../02-20-00-002_Subsystems_Integration_Map.md)  
- Cross-ATA dependencies:  
  → [`../02-20-00-003_Cross_ATA_Dependencies.csv`](../02-20-00-003_Cross_ATA_Dependencies.csv)  
- CAOS integration:  
  → [`../02-20-00-004_CAOS_Operations_Integration.md`](../02-20-00-004_CAOS_Operations_Integration.md)  

---

## 4. Internal Structure (Files & Folders)

Recommended structure for this subsystem:

- `02-20-01-001_Platform_Architecture.md`  
  - Logical and physical architecture  
  - Context diagram vs 02-20 subsystems and external systems  
  - High-level component model (ingest, storage, services, observability)

- `02-20-01-002_Data_Management.md`  
  - Data model concepts (Flight, Sector, Turnaround, H2_Op, Event, KPI, …)  
  - Retention, partitioning, multi-tenant aspects (if any)  
  - Data quality rules and validation flows  
  - DPP anchoring (how data sets and models are traced)

- `02-20-01-003_User_Interfaces.md`  
  - This subsystem has **no primary UI**, but:
    - Internal admin / monitoring consoles  
    - API documentation portals  
  - Links to UI-owning subsystems (EFB, Ops dashboards, CAOS console)

- `02-20-01-004_Integration_Layer.md`  
  - External interfaces and protocols:
    - To 02-20 subsystems (REST, events, DB views)  
    - To CAOS (batch/stream, feature export, KPI feeds)  
    - To aircraft / ATA 42 / AOC  
  - Security, authN/authZ and audit concepts

- `ASSETS/`  
  - `02-20-01-A-001_Platform_Architecture.drawio`  
  - `02-20-01-A-002_Platform_Architecture.svg`  
  - `02-20-01-A-003_Data_Flow_Diagram.svg`  

---

## 5. External Interfaces

### 5.1 Towards 02-20 Subsystems

The platform exposes:

- **Data access APIs**:
  - Flight, sector, turnaround, H₂ ops, events, KPIs
- **Event streams**:
  - Operational events to be consumed (e.g. by 02-20-23 Predictive Ops NN)
- **Schema registry**:
  - Canonical schemas referenced by `../02-90_Tables_Schemas_Diagrams/`

Primary consumers:

- `02-20-11_Electronic_Flight_Bag/`  
- `02-20-12_Weight_Balance_Computer/`  
- `02-20-13_Performance_Computer/`  
- `02-20-14_Ground_Ops_Management/`  
- `02-20-15_Flight_Planning_Integration/`  
- `02-20-16_Dispatch_System_Integration/`  
- `02-20-17_Weather_Information_System/`  
- `02-20-18_Operational_Data_Recording/`  
- `02-20-19_Crew_Resource_Management/`  
- `02-20-21_H2_Operations_Management/`  
- `02-20-22_Passenger_Experience_Management/`  
- `02-20-23_Predictive_Operations_NN/`  

### 5.2 Towards CAOS / AirCCC

See also:  
→ [`../02-20-00-004_CAOS_Operations_Integration.md`](../02-20-00-004_CAOS_Operations_Integration.md)  

The platform:

- Publishes:
  - Operational events, KPIs, context for CAOS use cases  
  - Curated data sets (via 02-20-18) for analytics and model training
- Receives:
  - CAOS alerts and advisories  
  - Analytics outputs and KPIs to redistribute to apps  

### 5.3 Towards ATA 95 (Neural Networks)

The platform is **not** the place where NNs are defined; that belongs to ATA 95.

However, it:

- Hosts or proxies **inference endpoints** backed by ATA 95 models  
- Logs **model usage, inputs and outputs** for traceability  
- Provides **feature stores** or data views used by models in:
  - `02-20-13`, `02-20-17`, `02-20-19`, `02-20-23`  

NN governance, assurance and traceability are documented in ATA 95; 02-20-01
only exposes and observes the runtime.

---

## 6. Data Management & DPP

Data-related governance should reference:

- `../02-90_Tables_Schemas_Diagrams/` for schemas and table definitions  
- ATA 95 DPP material for **model-centric traceability**  

Key principles:

- All ops data has **clear ownership** (which subsystem, which ATA reference).  
- Data artifacts can be **referenced from DPP entries** (hashes, anchors).  
- Data lifecycle is aligned with:
  - Safety & cert (minimum retention)  
  - Privacy & regulatory constraints  
  - Fleet analytics needs  

---

## 7. Security, Safety & Authority

The Digital Ops Platform must:

- Enforce **strong security**:
  - AuthN/AuthZ, encryption in transit/at rest, auditing  
- Respect **safety and certification** boundaries:
  - It may aggregate, transform and provide data and advisory outputs  
  - It must not **directly command safety-critical systems**  
- Align with:
  - `../02-00-00_GENERAL/02-00-02_SAFETY/`  
  - Relevant cyber-security guidance (e.g. DO-326A/ED-202A when applicable)  

Final operational authority always remains with:

- Flight crew (in flight)  
- Airline operations / dispatch (ground & network)  

---

## 8. Conventions

- File names: `02-20-01-XXX_Description.md` (XXX = 001, 002, 003, …)  
- Diagrams: stored under `ASSETS/`, with IDs `02-20-01-A-XXX_*.ext`  
- Every document under this subsystem should include:
  - **Scope**  
  - **Interfaces & Data**  
  - **Relation to CAOS / ATA 95** (if applicable)  
  - **Assumptions & Limitations**  

---

## 9. Document Control

> **Originator:** AI prompted by Amedeo Pelliccia  
> **Toolchain:** GitHub, MCP Doc Control, AMPEL360 OPT-IN Guidelines  
> **Subsystem:** 02-20-01 Digital Ops Platform

| Version | Date       | Author / Team                          | Changes                                      |
|---------|------------|-----------------------------------------|----------------------------------------------|
| 0.1     | YYYY-MM-DD | AMPEL360 Digital Operations & CAOS WG  | Initial Digital Ops Platform README skeleton |
