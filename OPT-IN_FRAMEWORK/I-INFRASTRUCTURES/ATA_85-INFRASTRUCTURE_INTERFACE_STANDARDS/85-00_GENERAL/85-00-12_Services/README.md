# 85-00-12_Services

## Purpose

This folder defines the **service, support and operational enablement model** for  
**ATA 85 – Infrastructure Interface Standards**, covering how the BWB aircraft and its  
interfaces with airport infrastructure, H₂ systems, CO₂ battery systems, GSE and  
passenger boarding/evacuation infrastructure are **supported in operation**.

It corresponds to **Stage 12 – Services** of the  
**A-LIVE-GP – Aircraft Lifecycle Industrialization and Validation Executive General Plan**  
for ATA 85.

---

## Scope

### In Scope

- Definition of the **service model** for infrastructure interfaces (ATA 85) in service:
  - Airport interface standards (power, data, gates, boarding bridges, evacuation flows)
  - H₂ production / storage / refuelling infrastructures
  - CO₂ battery ground infrastructure
  - GSE power and data interfaces

- **Operational support models**:
  - 1st/2nd/3rd line support responsibilities and escalation paths
  - Service desks and remote operations centers
  - Incident, problem and change management for ATA 85 interfaces

- **Service Level Agreements (SLAs) and OLAs**:
  - Service levels for infra availability, response and restoration times
  - Operating level agreements between airlines, airports, infra operators and OEMs

- **Training and enablement**:
  - Training paths for airport technical staff and service desks
  - Operational drills and rehearsals for H₂ / CO₂ / evacuation capabilities

- **Service performance and continuous improvement**:
  - KPI definitions, dashboards and monitoring
  - Feedback loop from field operations into design, production and EIS (Stages 04–11)
  - Integration with DPP and digital twin for infra-related service events

### Out of Scope

- Detailed certification artefacts (covered in **85-00-10_Certification**)
- EIS baseline definition and tagging (covered in **85-00-11_EIS_Versions_Tags**)
- Detailed aircraft operational procedures (covered in **ATA 02 – Operations Information**)

---

## Contents

### Core Documents

- `85-00-12-001_Service_Model_Infrastructure_Interfaces.md`  
  High-level service model for all ATA 85 interfaces:
  - Service boundaries and responsibilities
  - Customer journeys (airline, airport, infra operator)
  - Interaction with AMPEL360 program-level service model.

- `85-00-12-002_Operational_Support_Model.md`  
  Operational support structure:
  - L1/L2/L3 support definition
  - Escalation paths and response matrix
  - Interfaces with OEM, infra providers and airport operations centers.

- `85-00-12-003_SLA_and_OLA_Framework.md`  
  Framework for SLAs/OLAs:
  - Standard SLA template components
  - Service metrics (availability, response, resolution)
  - OLA examples for internal teams (engineering, operations, suppliers).

- `85-00-12-004_Spare_Parts_and_Logistics_Services.md`  
  Service support for physical infra elements:
  - Spare parts strategies for H₂ / CO₂ / GSE infra components
  - Logistics flows and stock locations
  - Service contracts with critical suppliers.

- `85-00-12-005_Training_and_Enablement_Services.md`  
  Training and enablement:
  - Training curriculum for airport technical teams
  - Certification and recurrent training
  - Drills and simulations (H₂ safety, evacuation, CO₂ battery incidents).

- `85-00-12-006_Remote_Monitoring_and_Support_Centers.md`  
  Remote services:
  - Remote monitoring center role and architecture
  - Interfaces with digital twin and ATA 02/99
  - Operating procedures for remote interventions and guidance.

- `85-00-12-007_Service_Performance_and_Continuous_Improvement.md`  
  Continuous improvement:
  - KPI framework for ATA 85 services
  - Field feedback collection and review cadence
  - Link to design, requirements and EIS updates (Stages 03, 04, 11).

---

## ASSETS

### `ASSETS/Playbooks/`

- `85-00-12-A-001_Service_Runbook_Template.md`  
  Generic runbook structure for service operations on ATA 85 interfaces.

- `85-00-12-A-002_Major_Incident_Playbook.md`  
  Playbook for managing major incidents (e.g. H₂ infra outage, CO₂ battery infra failure).

- `85-00-12-A-003_Change_Implementation_Playbook.md`  
  Standard change implementation flow for infra interface updates.

### `ASSETS/SLAs/`

- `85-00-12-A-101_SLA_Template_Airport_Interfaces.md`  
  SLA template for airport interface services (power, gates, boarding, evacuation).

- `85-00-12-A-102_SLA_Template_H2_CO2_Providers.md`  
  SLA template for hydrogen and CO₂ infra operators.

- `85-00-12-A-103_OLA_Internal_Teams_Template.md`  
  OLA template for internal roles (engineering, operations, digital twin, DPP).

### `ASSETS/Training/`

- `85-00-12-A-201_Airport_Technical_Training_Outline.pdf`  
- `85-00-12-A-202_Service_Desk_Training_Outline.pdf`  
- `85-00-12-A-203_E_Learning_Modules_Index.xlsx`  

Training materials and indexes for ATA 85 service enablement.

### `ASSETS/Monitoring/`

- `85-00-12-A-301_Service_KPI_Dashboard_Layout.svg`  
- `85-00-12-A-302_Service_KPI_Definitions.xlsx`  
- `85-00-12-A-303_Alerting_Rules_Template.yaml`  

Monitoring / alerting assets for services on infra interfaces.

### `ASSETS/DPP_Links/`

- `85-00-12-A-401_Service_Events_to_DPP_Map.csv`  
  Mapping between service events (tickets, incidents, changes) and DPP entries.

- `85-00-12-A-402_Service_Configuration_Anchors.json`  
  Anchors connecting service states to DPP/digital twin configuration.

---

## Lifecycle Position (A-LIVE-GP)

- **Lifecycle Stage**: 12 of 14 – **Services**  
- **Upstream Inputs**:
  - 85-00-09_Production_Planning  
  - 85-00-10_Certification  
  - 85-00-11_EIS_Versions_Tags  
- **Downstream Outputs**:
  - Feedback into **03_REQUIREMENTS** and **04_DESIGN** for infra interfaces
  - Input to **13_Subsystems_Components** and **14_Ops_Std_Sustain**
  - Input to **ATA 99 – Circularity & Sustainability** for service-related impacts.

---

## Status

- **Phase**: Service Operations & Support (A-LIVE-GP Stage 12)  
- **Maturity**: `DRAFT` (skeleton – content to be progressively populated)  
- **Last Updated**: 2025-11-21  

---

## Document Control

- **Standard**: OPT-IN Framework v1.1 (A-LIVE-GP, ATA 85 pattern)  
- **Folder Owner**: ATA 85 Service & Operations Lead  
- **Change Authority**: Infrastructure Interfaces CCB (I-CCB-85)  
- **Repository**: `AMPEL360-BWB-H2-Hy-E`
