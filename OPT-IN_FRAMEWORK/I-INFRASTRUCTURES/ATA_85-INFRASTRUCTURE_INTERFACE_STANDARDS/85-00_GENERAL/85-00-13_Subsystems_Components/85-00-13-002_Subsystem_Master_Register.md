# 85-00-13-002: Subsystem Master Register

## Document Information

- **Document ID**: 85-00-13-002
- **Title**: Subsystem Master Register
- **Version**: 1.0
- **Status**: DRAFT
- **Date**: 2025-11-21

---

## 1. Introduction

This document describes the **Subsystem Master Register** for ATA 85 Infrastructure Interface Standards. The register provides the authoritative source for all infrastructure-related subsystems in the AMPEL360 BWB aircraft, defining their identification, classification, and relationships.

### 1.1 Purpose

The Subsystem Master Register:

- Provides a **single source of truth** for all ATA 85 subsystems
- Establishes **naming conventions** and identification schemes
- Defines **domain classification** (H₂, CO₂, Airport, GSE, PAX)
- Documents **relationships** between subsystems and other ATA chapters
- Links subsystems to **OPT-IN pillars** (I, N, O, P, T)
- Enables **traceability** to requirements, design, and verification

### 1.2 Scope

This register covers:

- All infrastructure interface subsystems at the aircraft-ground boundary
- Subsystems for energy transfer (H₂, CO₂, electrical, thermal)
- Subsystems for data and communication interfaces
- Subsystems for passenger and cargo handling interfaces
- Integration points with airport and ground service equipment

---

## 2. Subsystem Naming Conventions

### 2.1 Subsystem ID Format

Each subsystem has a unique identifier following this pattern:

```
85-<DOMAIN>-<CATEGORY>-<SEQUENCE>
```

Where:
- **85** = ATA chapter (Infrastructure Interface Standards)
- **DOMAIN** = Two or three-letter domain code (see Section 2.2)
- **CATEGORY** = Functional category within domain (see Section 2.3)
- **SEQUENCE** = Three-digit sequence number (001-999)

**Examples**:
- `85-H2-FUEL-001` – H₂ Fueling Interface Subsystem
- `85-CO2-CHRG-001` – CO₂ Battery Charging Interface Subsystem
- `85-APT-PWR-001` – Airport Gate Power Interface Subsystem
- `85-GSE-DATA-001` – GSE Data Communications Subsystem
- `85-PAX-BRDG-001` – Passenger Boarding Bridge Interface Subsystem

### 2.2 Domain Codes

| Domain Code | Domain Name | Description |
|-------------|-------------|-------------|
| H2 | Hydrogen Infrastructure | H₂ fueling, venting, safety interfaces |
| CO2 | CO₂ Battery Infrastructure | CO₂ battery charging, thermal management |
| APT | Airport Infrastructure | Gate power, data, utilities |
| GSE | Ground Services Equipment | Mobile GSE interfaces |
| PAX | Passenger Boarding/Evac | Passenger interface systems |

### 2.3 Category Codes

Common category codes used across domains:

| Category | Description | Typical Use |
|----------|-------------|-------------|
| FUEL | Fueling/Refueling | H₂ fuel transfer |
| VENT | Venting | H₂ boil-off, pressure relief |
| CHRG | Charging | CO₂ battery charging |
| THRM | Thermal Management | Cooling/heating interfaces |
| PWR | Electrical Power | Ground power connections |
| DATA | Data Communications | Network, telemetry, diagnostics |
| BRDG | Boarding Bridge | Passenger loading bridges |
| EVAC | Evacuation | Emergency egress interfaces |
| SFTY | Safety Systems | Interlocks, monitoring, alarms |

---

## 3. Domain Classifications

### 3.1 H₂ Infrastructure (H2)

Subsystems for hydrogen fuel interfaces:

| Subsystem ID | Name | Description |
|--------------|------|-------------|
| 85-H2-FUEL-001 | H₂ Fueling Interface | Primary H₂ refueling receptacle and control |
| 85-H2-VENT-001 | H₂ Vent Interface | Boil-off and pressure relief venting |
| 85-H2-SFTY-001 | H₂ Safety Monitoring | Leak detection, fire suppression interfaces |
| 85-H2-PURGE-001 | H₂ Purge Interface | Pre/post-flight purge connections |

See [H2_INFRASTRUCTURE/85-00-13-H2-001_H2_Infrastructure_Subsystems_Index.md](./H2_INFRASTRUCTURE/85-00-13-H2-001_H2_Infrastructure_Subsystems_Index.md) for complete listing.

### 3.2 CO₂ Battery Infrastructure (CO2)

Subsystems for CO₂ battery interfaces:

| Subsystem ID | Name | Description |
|--------------|------|-------------|
| 85-CO2-CHRG-001 | CO₂ Battery Charging Interface | High-power DC charging connection |
| 85-CO2-THRM-001 | CO₂ Battery Thermal Interface | Cooling system ground connections |
| 85-CO2-DATA-001 | CO₂ Battery Data Interface | BMS communication and diagnostics |
| 85-CO2-SFTY-001 | CO₂ Battery Safety Interface | Emergency shutdown, monitoring |

See [CO2_BATTERY_INTERFACE/85-00-13-CO2-001_CO2_Battery_Subsystems_Index.md](./CO2_BATTERY_INTERFACE/85-00-13-CO2-001_CO2_Battery_Subsystems_Index.md) for complete listing.

### 3.3 Airport Infrastructure (APT)

Subsystems for airport facility interfaces:

| Subsystem ID | Name | Description |
|--------------|------|-------------|
| 85-APT-PWR-001 | Airport Gate Power Interface | 400Hz/DC ground power connection |
| 85-APT-DATA-001 | Airport Data Interface | WiFi, fiber, network connections |
| 85-APT-BRDG-001 | Boarding Bridge Interface | Physical docking, environmental seal |
| 85-APT-UTIL-001 | Airport Utilities Interface | Water, waste, pneumatics |

See [AIRPORT_INTERFACE/85-00-13-AI-001_Airport_Interface_Subsystems_Index.md](./AIRPORT_INTERFACE/85-00-13-AI-001_Airport_Interface_Subsystems_Index.md) for complete listing.

### 3.4 Ground Services Equipment (GSE)

Subsystems for mobile GSE interfaces:

| Subsystem ID | Name | Description |
|--------------|------|-------------|
| 85-GSE-PWR-001 | GSE Power Interface | Mobile power cart connections |
| 85-GSE-FUEL-001 | GSE H₂ Fueling Interface | Mobile H₂ fueling unit connection |
| 85-GSE-DATA-001 | GSE Data Interface | Diagnostics, maintenance data exchange |
| 85-GSE-LIFT-001 | GSE Lifting Interface | Jacking, towing attachment points |

See [GROUND_SERVICES_INTERFACE/85-00-13-GSE-001_GSE_Interface_Subsystems_Index.md](./GROUND_SERVICES_INTERFACE/85-00-13-GSE-001_GSE_Interface_Subsystems_Index.md) for complete listing.

### 3.5 Passenger Boarding/Evacuation (PAX)

Subsystems for passenger interface systems:

| Subsystem ID | Name | Description |
|--------------|------|-------------|
| 85-PAX-BRDG-001 | Passenger Boarding Bridge Interface | Bridge docking hardware |
| 85-PAX-EVAC-001 | Emergency Evacuation Interface | Slide deployment interfaces |
| 85-PAX-DOOR-001 | Passenger Door Interface | Door operation, safety interlocks |

See [PAX_BOARDING_EVAC_INTERFACE/85-00-13-PAX-001_Pax_Boarding_Evac_Subsystems_Index.md](./PAX_BOARDING_EVAC_INTERFACE/85-00-13-PAX-001_Pax_Boarding_Evac_Subsystems_Index.md) for complete listing.

---

## 4. Master Registry Artifacts

### 4.1 Master Subsystem List

The authoritative subsystem register is maintained in:

**[MASTER/85-00-13-M-001_Master_Subsystem_List.csv](./MASTER/85-00-13-M-001_Master_Subsystem_List.csv)**

This CSV file contains one record per subsystem with the following fields:

| Field | Description | Example |
|-------|-------------|---------|
| Subsystem_ID | Unique identifier | 85-H2-FUEL-001 |
| Subsystem_Name | Full name | H₂ Fueling Interface Subsystem |
| Domain | Domain classification | H2 |
| Category | Functional category | FUEL |
| Description | Brief description | Primary H₂ refueling receptacle and control system |
| ATA_Chapters | Related ATA chapters | 28, 85 |
| OPTIN_Pillars | Related OPT-IN pillars | I, T |
| Lifecycle_Status | Current status | Active, Prototype, Retired |
| Owner | Responsible engineer/team | Infrastructure Systems Team |
| Version | Current version | 1.2 |
| Last_Updated | Last modification date | 2025-11-21 |

### 4.2 Interface Point Register

Physical and logical interface points are catalogued in:

**[MASTER/85-00-13-M-003_Interface_Point_Register.csv](./MASTER/85-00-13-M-003_Interface_Point_Register.csv)**

This register documents:
- Physical connectors and receptacles
- Logical data interfaces (protocols, ports)
- Mechanical attachment points
- Thermal interface points
- Safety interlocks and sensors

### 4.3 Configurable Units

Subsystem groupings and kits are defined in:

**[MASTER/85-00-13-M-004_Subsystem_Configurable_Units.xlsx](./MASTER/85-00-13-M-004_Subsystem_Configurable_Units.xlsx)**

This allows for:
- Standard configuration packages per airport type
- Aircraft variant-specific subsystem sets
- Optional vs. mandatory subsystem identification
- Kit-level BOMs and procurement packages

---

## 5. Integration with ATA Chapters

### 5.1 Multi-Chapter Subsystems

Many ATA 85 subsystems have relationships with other ATA chapters:

| Subsystem | Primary ATA | Related ATA Chapters | Rationale |
|-----------|-------------|----------------------|-----------|
| 85-H2-FUEL-001 | 85 | 28 (Fuel) | Fuel system integration |
| 85-CO2-THRM-001 | 85 | 21 (Environmental) | Thermal management |
| 85-APT-PWR-001 | 85 | 24 (Electrical) | Power systems |
| 85-GSE-DATA-001 | 85 | 45 (Diagnostics), 02 (Operations) | Data and diagnostics |

See [85-00-13-006_Subsystem_to_ATA_and_OPTIN_Mapping.md](./85-00-13-006_Subsystem_to_ATA_and_OPTIN_Mapping.md) for complete mapping.

### 5.2 OPT-IN Pillar Mapping

Each subsystem maps to one or more OPT-IN pillars:

- **I (Infrastructures)** – All ATA 85 subsystems
- **N (Neural Networks & Traceability)** – Subsystems with sensors, AI monitoring
- **O (Organization)** – Subsystems requiring specific processes/certification
- **P (Program)** – Subsystems on critical path for development
- **T (Technology)** – Subsystems with on-board system integration

---

## 6. Lifecycle Tracking

### 6.1 Subsystem Status Values

Each subsystem has a lifecycle status:

| Status | Description | Typical Activities |
|--------|-------------|-------------------|
| Concept | Initial definition | Requirements capture |
| Design | Detailed design in progress | CAD models, ICDs |
| Prototype | Physical prototype exists | Testing, validation |
| Active | In production/service | Manufacturing, installation |
| Modified | Design change in progress | Engineering change order |
| Retired | No longer used | Superseded by new design |
| Archived | Historical record only | Documentation retention |

### 6.2 Version Control

Subsystem definitions use semantic versioning:
- **Major** version: Significant design change affecting interfaces
- **Minor** version: Design refinement, backward compatible
- **Patch** version: Documentation corrections, no design change

Example: Version 2.3.1
- Major = 2 (second generation design)
- Minor = 3 (third refinement)
- Patch = 1 (first documentation update)

---

## 7. Usage and Maintenance

### 7.1 Adding New Subsystems

To add a new subsystem:

1. Define subsystem scope and boundaries
2. Assign unique Subsystem_ID following naming convention
3. Add entry to Master Subsystem List (M-001)
4. Create detailed subsystem documentation in appropriate domain folder
5. Update interface point register (M-003)
6. Link to related requirements, design docs, and DPP entries
7. Submit to I-CCB-85 for approval

### 7.2 Modifying Existing Subsystems

To modify a subsystem:

1. Create engineering change proposal (ECP)
2. Assess impact on interfaces, components, verification
3. Update Master Subsystem List with new version
4. Update related documentation and artifacts
5. Submit ECP to I-CCB-85 for approval
6. Update DPP records for affected components

### 7.3 Review and Audit

- **Quarterly review**: Check for obsolete or missing subsystems
- **Annual audit**: Reconcile with as-built aircraft configuration
- **Change-driven review**: When major requirements or design changes occur

---

## 8. References

### 8.1 Internal References

- [85-00-13-001_Subsystems_Components_Overview.md](./85-00-13-001_Subsystems_Components_Overview.md)
- [85-00-13-003_Component_Taxonomy_and_Coding.md](./85-00-13-003_Component_Taxonomy_and_Coding.md)
- [85-00-13-006_Subsystem_to_ATA_and_OPTIN_Mapping.md](./85-00-13-006_Subsystem_to_ATA_and_OPTIN_Mapping.md)
- [MASTER/README.md](./MASTER/README.md)

### 8.2 External Standards

- **[EASA CS-25](https://www.easa.europa.eu/en/document-library/certification-specifications/cs-25-large-aeroplanes)** – Certification Specifications for Large Aeroplanes
- **[ATA iSpec 2200](https://www.ata.org/)** – Information Standards for Aviation Maintenance
- **[ISO 81346](https://www.iso.org/standard/50086.html)** – Industrial systems, installations and equipment and industrial products — Structuring principles and reference designations

---

## Document Control

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT** – Subject to human review and approval.
- Human approver: _[to be completed]_.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: _2025-11-21_.

---
