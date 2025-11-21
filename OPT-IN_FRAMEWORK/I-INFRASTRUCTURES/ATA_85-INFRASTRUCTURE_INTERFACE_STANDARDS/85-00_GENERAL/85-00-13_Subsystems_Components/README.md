# 85-00-13_Subsystems_Components

## Purpose

This folder defines the **subsystem and component view** of  
**[ATA 85 – Infrastructure Interface Standards](https://www.easa.europa.eu/en/document-library/certification-specifications)**, providing the canonical register of:

- All **infrastructure-related subsystems** for the AMPEL360 BWB (H₂, CO₂ battery, airport, GSE, PAX boarding/evac)
- Their **physical and logical components**
- The **interface hardware** that connects aircraft, airport, and energy infrastructures
- The linkage of these elements to **DPP**, **digital twin**, and other OPT-IN axes.

It corresponds to **Stage 13 – Subsystems & Components** of the  
**A-LIVE-GP – Aircraft Lifecycle Industrialization and Validation Executive General Plan** for ATA 85.

---

## Scope

### In Scope

- Master register of ATA 85 **subsystems** and their associated components
- Subsystem breakdowns for:
  - H₂ infrastructure interfaces
  - CO₂ battery infrastructure interfaces
  - Airport infrastructure (gates, power, data, boarding bridges)
  - GSE and ground services interfaces
  - Passenger boarding and evacuation interfaces
- Definition of:
  - Component families, coding and identification rules
  - Interface hardware catalog (connectors, manifolds, hoses, couplers, sensors)
  - Configurable packages/kits linking multiple components (e.g. "H₂ Gate Kit", "CO₂ Service Kit")
- Mapping of subsystems/components to:
  - ATA chapters and OPT-IN pillars
  - DPP entries (ATA 95 / ATA 99)
  - Digital twin models for infrastructure interfaces.

### Out of Scope

- Detailed interface **behavioural requirements** (covered in [85-00-03_Requirements](../85-00-03_Requirements/README.md))
- Detailed **geometrical/installation design** (covered in [85-00-04_Design](../85-00-04_Design/README.md))
- Verification, certification and services content (Stages 07–12).

---

## Contents

### Core Documents

- [85-00-13-001_Subsystems_Components_Overview.md](./85-00-13-001_Subsystems_Components_Overview.md)  
  High-level explanation of the ATA 85 subsystem/component model, how this register is structured, and its role in A-LIVE-GP.

- [85-00-13-002_Subsystem_Master_Register.md](./85-00-13-002_Subsystem_Master_Register.md)  
  Narrative description of the subsystem master register:
  - Subsystem naming conventions
  - Classification by domain (H₂, CO₂, Airport, GSE, PAX)
  - Links to MASTER registry artefacts.

- [85-00-13-003_Component_Taxonomy_and_Coding.md](./85-00-13-003_Component_Taxonomy_and_Coding.md)  
  Component taxonomy and coding rules:
  - Component family codes
  - Identification rules (labels, tagging, QR/NFC, DPP IDs)
  - Relationship to ATA/IPC conventions.

- [85-00-13-004_Interface_Hardware_Catalog.md](./85-00-13-004_Interface_Hardware_Catalog.md)  
  Catalog of all physical interface hardware:
  - H₂ and CO₂ connectors and manifolds
  - Power and data connectors at airport/GSE interfaces
  - PAX boarding/evac hardware relevant to ATA 85.

- [85-00-13-005_Configurable_Packages_and_Kits.md](./85-00-13-005_Configurable_Packages_and_Kits.md)  
  Definition of configurable packages:
  - Standard infra kits per airport category
  - Aircraft-configuration-driven infra kits
  - Mapping to BOMs in `ASSETS/BOMs/`.

- [85-00-13-006_Subsystem_to_ATA_and_OPTIN_Mapping.md](./85-00-13-006_Subsystem_to_ATA_and_OPTIN_Mapping.md)  
  Mapping table linking each subsystem to:
  - ATA chapter(s) (02, 21, 28, 32, 85, 95, 99…)
  - OPT-IN pillars (I, N, O, P, T)
  - Upstream design and downstream operations.

- [85-00-13-007_DPP_and_Digital_Twin_Links.md](./85-00-13-007_DPP_and_Digital_Twin_Links.md)  
  How subsystems/components connect to:
  - DPP schemas and anchors (ATA 95 / 02-90-13)
  - Digital twin instances for infra interfaces
  - Traceability to manufacturing, maintenance and circularity.

---

## Subsystem Families

### [MASTER/](./MASTER/)

**Global, aircraft-level registry layer** for ATA 85:

- `85-00-13-M-001_Master_Subsystem_List.csv`  
  One line per subsystem, with ID, domain, ATA mapping, lifecycle status.

- `85-00-13-M-002_Master_Component_List.csv`  
  Normalized view of components across all subsystems.

- `85-00-13-M-003_Interface_Point_Register.csv`  
  Register of interface points (physical and logical) between aircraft and infra.

- `85-00-13-M-004_Subsystem_Configurable_Units.xlsx`  
  Grouping into configuration units / kits.

### [H2_INFRASTRUCTURE/](./H2_INFRASTRUCTURE/)

Subsystem and component registers focused on **hydrogen infrastructure interfaces**:

- `85-00-13-H2-001_H2_Infrastructure_Subsystems_Index.md`  
- `85-00-13-H2-002_H2_Infrastructure_Components_Index.md`  
- `ASSETS/BOMs`, `ASSETS/Diagrams`, `ASSETS/DPP_Links` for H₂-specific content.

### [CO2_BATTERY_INTERFACE/](./CO2_BATTERY_INTERFACE/)

Subsystem/component breakdown for **CO₂ battery infrastructure**:

- `85-00-13-CO2-001_CO2_Battery_Subsystems_Index.md`  
- `85-00-13-CO2-002_CO2_Battery_Components_Index.md`

### [AIRPORT_INTERFACE/](./AIRPORT_INTERFACE/)

Subsystems and components for **airport infra interfaces**:

- `85-00-13-AI-001_Airport_Interface_Subsystems_Index.md`  
- `85-00-13-AI-002_Airport_Interface_Components_Index.md`

### [GROUND_SERVICES_INTERFACE/](./GROUND_SERVICES_INTERFACE/)

Subsystem/component breakdown for **GSE & ground services** (power carts, H₂/CO₂ service units, etc.).

### [PAX_BOARDING_EVAC_INTERFACE/](./PAX_BOARDING_EVAC_INTERFACE/)

Subsystems/components for **passenger boarding and evacuation** interfaces where ATA 85 infra standards are relevant.

Each of these follows the same pattern:  
`*_Subsystems_Index.md` + `*_Components_Index.md` + `ASSETS/` for BOMs, diagrams and DPP links.

---

## ASSETS

Central, cross-domain assets for ATA 85 subsystems/components:

- [ASSETS/Registries/](./ASSETS/Registries/) – curated views of master lists
- [ASSETS/BOMs/](./ASSETS/BOMs/) – domain BOMs for infra interfaces
- [ASSETS/Diagrams/](./ASSETS/Diagrams/) – subsystem/component diagrams and hierarchy views
- [ASSETS/DPP_Links/](./ASSETS/DPP_Links/) – mapping to DPP anchors and digital twin instances.

---

## Lifecycle Position (A-LIVE-GP)

- **Lifecycle Stage**: 13 of 14 – **Subsystems & Components**  
- **Upstream Inputs**:
  - [85-00-03_Requirements](../85-00-03_Requirements/README.md)
  - [85-00-04_Design](../85-00-04_Design/README.md)
  - [85-00-06_Engineering](../85-00-06_Engineering/README.md)
  - [85-00-09_Production_Planning](../85-00-09_Production_Planning/README.md)
- **Downstream Outputs**:
  - [85-00-14_Ops_Std_Sustain](../85-00-14_Ops_Std_Sustain/README.md) (standard operations, sustainment, circularity)
  - ATA 99 (circularity, carbon, recycling strategies)
  - DPP and digital twin operational views.

---

## Status

- **Phase**: Subsystem & Component Register Definition (A-LIVE-GP Stage 13)  
- **Maturity**: `DRAFT` – Structural skeleton, content to be progressively populated  
- **Last Updated**: 2025-11-21  

---

## Document Control

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT** – Subject to human review and approval.
- Human approver: _[to be completed]_.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: _2025-11-21_.
- **Standard**: OPT-IN Framework v1.1 (A-LIVE-GP, ATA 85 pattern)  
- **Folder Owner**: ATA 85 Subsystems & Components Lead  
- **Change Authority**: Infrastructure Interfaces CCB (I-CCB-85)

---
