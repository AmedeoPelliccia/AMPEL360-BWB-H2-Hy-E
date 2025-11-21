# 85-00-05-002: Interface Categories Map

## 1. Introduction
This document categorizes the various interfaces defined within ATA 85-00-05 to facilitate navigation and management.

## 2. Category Map

| Category ID | Category Name | Description | Key Sub-System |
| :--- | :--- | :--- | :--- |
| **CAT-A** | **Airport Geometric** | Physical dimensions and clearances. | [Airport Interface](./AIRPORT_INTERFACE/README.md) |
| **CAT-H** | **Hydrogen Infrastructure** | Cryogenic and gaseous H2 handling. | [H2 Infrastructure](./H2_INFRASTRUCTURE_INTERFACE/README.md) |
| **CAT-C** | **CO2 & Battery** | CO2 canister and battery module handling. | [CO2 Battery Interface](./CO2_BATTERY_INTERFACE/README.md) |
| **CAT-G** | **Ground Services** | Conventional GSE (Water, Waste, Air). | [Ground Services](./GROUND_SERVICES_INTERFACE/README.md) |
| **CAT-P** | **Passenger & Crew** | Boarding bridges, stairs, and evacuation. | [Pax Boarding](./PAX_BOARDING_EVAC_INTERFACE/README.md) |
| **CAT-D** | **Digital & Data** | IT, AODB, and [A-CDM](https://www.eurocontrol.int/concept/airport-collaborative-decision-making) integration. | [Digital Infrastructure](./DIGITAL_INFRASTRUCTURE_INTERFACE/README.md) |
| **CAT-E** | **Energy & Power** | Electrical grid and microgrid connections. | [Energy Infrastructure](./ENERGY_INFRASTRUCTURE_INTERFACE/README.md) |

## 3. Interdependencies
*   **CAT-H** and **CAT-E** are closely linked for energy management.
*   **CAT-A** dictates the constraints for all physical service vehicles in **CAT-G**, **CAT-H**, and **CAT-C**.
*   **CAT-D** overlays all categories for monitoring and control.


---

## Document Control

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT** – Subject to human review and approval.
- Human approver: _[to be completed]_.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: 2025-11-21.

---
