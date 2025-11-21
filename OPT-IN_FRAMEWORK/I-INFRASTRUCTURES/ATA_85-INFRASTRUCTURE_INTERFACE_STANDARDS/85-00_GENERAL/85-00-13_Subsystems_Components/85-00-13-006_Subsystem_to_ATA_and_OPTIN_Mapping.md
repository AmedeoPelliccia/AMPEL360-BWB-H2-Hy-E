# 85-00-13-006: Subsystem to ATA and OPT-IN Mapping

## Document Information

- **Document ID**: 85-00-13-006
- **Title**: Subsystem to ATA and OPT-IN Mapping
- **Version**: 1.0
- **Status**: DRAFT
- **Date**: 2025-11-21

---

## 1. Introduction

This document provides comprehensive mapping between **ATA 85 subsystems** and both **ATA chapters** and **OPT-IN pillars**. This mapping enables cross-functional integration, traceability, and coordination across the AMPEL360 BWB aircraft lifecycle.

### 1.1 Purpose

The mapping serves to:

- **Identify cross-chapter dependencies** for integrated design and verification
- **Enable multi-pillar coordination** across OPT-IN framework dimensions
- **Support lifecycle planning** by linking subsystems to relevant processes
- **Facilitate impact analysis** when requirements or designs change
- **Enable holistic systems engineering** across organizational boundaries

### 1.2 Scope

This document maps:

- All ATA 85 subsystems to related ATA chapters (primary and secondary)
- All ATA 85 subsystems to OPT-IN pillars (I, N, O, P, T)
- Rationale for each mapping relationship
- Integration touchpoints and interfaces

---

## 2. ATA Chapter Overview

### 2.1 ATA Chapter System

The **Air Transport Association (ATA) Spec 100** provides a standardized chapter numbering system for aircraft technical documentation. Key ATA chapters relevant to infrastructure interfaces:

| ATA Chapter | Title | Relevance to ATA 85 |
|-------------|-------|---------------------|
| **02** | Limitations, Operations Information | Operational procedures, data requirements |
| **05** | Periodic Inspections | Maintenance intervals, inspection procedures |
| **10** | Parking, Mooring, Storage | Ground handling, tiedown interfaces |
| **12** | Servicing | Routine servicing, fluid replenishment |
| **21** | Environmental Control | Thermal interfaces, air conditioning |
| **24** | Electrical Power | Power generation, distribution, ground power |
| **28** | Fuel | H₂ fuel system integration |
| **32** | Landing Gear | Ground interface points, jacking |
| **45** | Diagnostics, Maintenance Systems | Data acquisition, health monitoring |
| **52** | Doors | Passenger, cargo, and service doors |
| **53** | Fuselage | Structure, interface mounting points |
| **80** | Starting | APU, engine starting systems |
| **85** | **Infrastructure Interface Standards** | **Primary chapter** |
| **95** | Digital Product Passport, Traceability | DPP, data management |
| **99** | Circularity, Carbon, Recycling | End-of-life, sustainability |

### 2.2 Mapping Notation

For each subsystem:
- **Primary ATA**: Main chapter for subsystem design and certification
- **Related ATA**: Supporting chapters with interface dependencies
- **Integration Level**: Depth of integration (High, Medium, Low)

---

## 3. OPT-IN Pillar Overview

### 3.1 OPT-IN Framework Pillars

The **OPT-IN Framework** organizes aircraft lifecycle elements into five pillars:

| Pillar | Focus | Description |
|--------|-------|-------------|
| **I – Infrastructures** | Physical/logical foundations | Facilities, equipment, interfaces, processes |
| **N – Neural Networks & Traceability** | AI, data, tracking | Machine learning, digital thread, DPP |
| **O – Organization** | People, processes, governance | Roles, procedures, quality, certification |
| **P – Program** | Project management | Planning, scheduling, milestones, resources |
| **T – Technology** | Technical systems | On-board systems, hardware, software |

### 3.2 Pillar Mapping Rationale

Each ATA 85 subsystem maps to one or more pillars based on:

- **I (Infrastructures)**: Always mapped (ATA 85 is infrastructure-focused)
- **N (Neural & Traceability)**: If subsystem has sensors, data collection, AI monitoring
- **O (Organization)**: If subsystem requires specific processes, training, certification
- **P (Program)**: If subsystem is on critical path or has program management implications
- **T (Technology)**: If subsystem interfaces with on-board systems (ATA 20-80)

---

## 4. H₂ Infrastructure Subsystem Mapping

### 4.1 H₂ Fueling Interface Subsystem

**Subsystem ID**: `85-H2-FUEL-001`

| Mapping Type | Value | Integration Level | Rationale |
|--------------|-------|-------------------|-----------|
| **Primary ATA** | 85 | High | Core infrastructure interface |
| **Related ATA** | 28 (Fuel) | High | Integrates with aircraft H₂ fuel system |
| | 24 (Electrical) | Medium | Electrical bonding, power for controls |
| | 45 (Diagnostics) | Medium | Fueling status, diagnostics data |
| | 02 (Operations) | Low | Operational procedures, limitations |
| **OPT-IN Pillars** | I (Infrastructures) | Primary | Physical interface hardware |
| | T (Technology) | High | Interfaces with ATA 28 fuel system |
| | N (Neural & Trace) | Medium | Fueling telemetry, DPP tracking |
| | O (Organization) | Medium | Fueling procedures, training |
| | P (Program) | Low | Standard schedule, not critical path |

**Key Interfaces**:
- ATA 28: H₂ fuel tank fill/vent lines
- ATA 24: Bonding, receptacle heater power
- ATA 45: Fueling status to aircraft CMMS

### 4.2 H₂ Vent Interface Subsystem

**Subsystem ID**: `85-H2-VENT-001`

| Mapping Type | Value | Integration Level | Rationale |
|--------------|-------|-------------------|-----------|
| **Primary ATA** | 85 | High | Core infrastructure interface |
| **Related ATA** | 28 (Fuel) | High | H₂ boil-off, pressure relief |
| | 26 (Fire Protection) | High | Vent fire suppression integration |
| | 21 (Environmental) | Medium | Vent gas dispersion, safety zones |
| **OPT-IN Pillars** | I (Infrastructures) | Primary | Vent hardware, piping |
| | T (Technology) | High | ATA 28 vent system integration |
| | N (Neural & Trace) | Medium | Vent flow monitoring |
| | O (Organization) | High | Safety procedures, exclusion zones |

### 4.3 H₂ Safety Monitoring Subsystem

**Subsystem ID**: `85-H2-SFTY-001`

| Mapping Type | Value | Integration Level | Rationale |
|--------------|-------|-------------------|-----------|
| **Primary ATA** | 85 | High | Infrastructure safety interface |
| **Related ATA** | 26 (Fire Protection) | High | Fire/smoke detection, suppression |
| | 28 (Fuel) | Medium | Fuel system safety interlocks |
| | 45 (Diagnostics) | High | Real-time safety monitoring data |
| | 31 (Instruments) | Medium | Display of safety status |
| **OPT-IN Pillars** | I (Infrastructures) | Primary | Safety sensors, interlocks |
| | N (Neural & Trace) | High | AI-driven anomaly detection |
| | T (Technology) | High | Interfaces with aircraft safety systems |
| | O (Organization) | High | Safety procedures, emergency response |
| | P (Program) | Medium | Safety-critical, certification impact |

---

## 5. CO₂ Battery Interface Subsystem Mapping

### 5.1 CO₂ Battery Charging Interface

**Subsystem ID**: `85-CO2-CHRG-001`

| Mapping Type | Value | Integration Level | Rationale |
|--------------|-------|-------------------|-----------|
| **Primary ATA** | 85 | High | Infrastructure charging interface |
| **Related ATA** | 24 (Electrical) | High | Integrates with aircraft electrical system |
| | 80 (Starting) | Medium | Provides energy for engine starting |
| | 45 (Diagnostics) | High | Charging status, battery health data |
| | 26 (Fire Protection) | Medium | Battery thermal runaway protection |
| **OPT-IN Pillars** | I (Infrastructures) | Primary | Charging receptacle, cabling |
| | T (Technology) | High | Battery management system (BMS) |
| | N (Neural & Trace) | High | Predictive charging, battery analytics |
| | O (Organization) | Medium | Charging procedures, safety |

### 5.2 CO₂ Battery Thermal Interface

**Subsystem ID**: `85-CO2-THRM-001`

| Mapping Type | Value | Integration Level | Rationale |
|--------------|-------|-------------------|-----------|
| **Primary ATA** | 85 | High | Thermal interface hardware |
| **Related ATA** | 21 (Environmental) | High | Battery cooling system integration |
| | 24 (Electrical) | Medium | Coolant pump power |
| | 30 (Ice & Rain) | Low | Cold-weather thermal management |
| **OPT-IN Pillars** | I (Infrastructures) | Primary | Thermal coupling hardware |
| | T (Technology) | High | Thermal management system |
| | N (Neural & Trace) | Medium | Thermal performance monitoring |

### 5.3 CO₂ Battery Data Interface

**Subsystem ID**: `85-CO2-DATA-001`

| Mapping Type | Value | Integration Level | Rationale |
|--------------|-------|-------------------|-----------|
| **Primary ATA** | 85 | High | Data interface hardware |
| **Related ATA** | 45 (Diagnostics) | High | BMS data to ground systems |
| | 02 (Operations) | Medium | Operational data, flight planning |
| | 95 (DPP, Traceability) | High | DPP data exchange |
| **OPT-IN Pillars** | I (Infrastructures) | Primary | Data connectors, protocols |
| | N (Neural & Trace) | High | Data analytics, AI predictions |
| | T (Technology) | High | BMS, data acquisition systems |

---

## 6. Airport Infrastructure Subsystem Mapping

### 6.1 Airport Gate Power Interface

**Subsystem ID**: `85-APT-PWR-001`

| Mapping Type | Value | Integration Level | Rationale |
|--------------|-------|-------------------|-----------|
| **Primary ATA** | 85 | High | Ground power interface |
| **Related ATA** | 24 (Electrical) | High | Aircraft electrical system |
| | 33 (Lights) | Medium | External lighting during ground ops |
| | 21 (Environmental) | Medium | Air conditioning during ground ops |
| **OPT-IN Pillars** | I (Infrastructures) | Primary | Power receptacles, cabling |
| | T (Technology) | High | Power distribution, conversion |
| | O (Organization) | Low | Standard procedures |

### 6.2 Airport Data Interface

**Subsystem ID**: `85-APT-DATA-001`

| Mapping Type | Value | Integration Level | Rationale |
|--------------|-------|-------------------|-----------|
| **Primary ATA** | 85 | High | Data communication interface |
| **Related ATA** | 45 (Diagnostics) | High | Maintenance data upload/download |
| | 02 (Operations) | High | Flight planning, weather, ops data |
| | 95 (DPP, Traceability) | High | DPP synchronization |
| | 46 (Information Systems) | High | Aircraft information systems |
| **OPT-IN Pillars** | I (Infrastructures) | Primary | Data connectors, network hardware |
| | N (Neural & Trace) | High | Data exchange, cloud sync |
| | T (Technology) | High | Onboard data systems |
| | O (Organization) | Medium | Data security, access control |

### 6.3 Boarding Bridge Interface

**Subsystem ID**: `85-APT-BRDG-001`

| Mapping Type | Value | Integration Level | Rationale |
|--------------|-------|-------------------|-----------|
| **Primary ATA** | 85 | High | Physical docking interface |
| **Related ATA** | 52 (Doors) | High | Passenger door operation |
| | 21 (Environmental) | Medium | Environmental seal (pressurization) |
| | 53 (Fuselage) | Medium | Structural mounting, loads |
| **OPT-IN Pillars** | I (Infrastructures) | Primary | Docking hardware, seals |
| | T (Technology) | Medium | Door interlocks, sensors |
| | O (Organization) | High | Passenger safety, procedures |

---

## 7. Ground Services Equipment (GSE) Subsystem Mapping

### 7.1 GSE Power Interface

**Subsystem ID**: `85-GSE-PWR-001`

| Mapping Type | Value | Integration Level | Rationale |
|--------------|-------|-------------------|-----------|
| **Primary ATA** | 85 | High | Mobile ground power interface |
| **Related ATA** | 24 (Electrical) | High | Aircraft electrical system |
| | 12 (Servicing) | Low | Routine servicing procedures |
| **OPT-IN Pillars** | I (Infrastructures) | Primary | Power receptacles |
| | T (Technology) | Medium | Power management |

### 7.2 GSE H₂ Fueling Interface

**Subsystem ID**: `85-GSE-FUEL-001`

| Mapping Type | Value | Integration Level | Rationale |
|--------------|-------|-------------------|-----------|
| **Primary ATA** | 85 | High | Mobile H₂ fueling interface |
| **Related ATA** | 28 (Fuel) | High | H₂ fuel system |
| | 26 (Fire Protection) | High | Safety interlocks |
| | 12 (Servicing) | High | Fueling procedures |
| **OPT-IN Pillars** | I (Infrastructures) | Primary | Fueling hardware |
| | T (Technology) | High | Fuel system controls |
| | O (Organization) | High | Safety procedures, training |
| | P (Program) | Medium | GSE procurement, standards |

### 7.3 GSE Data Interface

**Subsystem ID**: `85-GSE-DATA-001`

| Mapping Type | Value | Integration Level | Rationale |
|--------------|-------|-------------------|-----------|
| **Primary ATA** | 85 | High | Maintenance data interface |
| **Related ATA** | 45 (Diagnostics) | High | Fault data download |
| | 05 (Inspections) | Medium | Inspection data recording |
| | 02 (Operations) | Low | Operational reports |
| **OPT-IN Pillars** | I (Infrastructures) | Primary | Data ports, protocols |
| | N (Neural & Trace) | High | Data analytics, predictive maintenance |
| | T (Technology) | High | Aircraft data systems |

---

## 8. Passenger Boarding/Evacuation Subsystem Mapping

### 8.1 Passenger Boarding Bridge Interface

**Subsystem ID**: `85-PAX-BRDG-001`

| Mapping Type | Value | Integration Level | Rationale |
|--------------|-------|-------------------|-----------|
| **Primary ATA** | 85 | High | Bridge docking interface |
| **Related ATA** | 52 (Doors) | High | Passenger door integration |
| | 25 (Cabin Equipment) | Low | Cabin environment continuity |
| **OPT-IN Pillars** | I (Infrastructures) | Primary | Docking hardware |
| | O (Organization) | High | Passenger safety, procedures |
| | T (Technology) | Low | Door sensors, interlocks |

### 8.2 Emergency Evacuation Interface

**Subsystem ID**: `85-PAX-EVAC-001`

| Mapping Type | Value | Integration Level | Rationale |
|--------------|-------|-------------------|-----------|
| **Primary ATA** | 85 | High | Evacuation slide interface |
| **Related ATA** | 52 (Doors) | High | Door operation, slide deployment |
| | 25 (Cabin Equipment) | High | Emergency equipment |
| | 26 (Fire Protection) | Medium | Emergency evacuation coordination |
| **OPT-IN Pillars** | I (Infrastructures) | Primary | Slide deployment hardware |
| | O (Organization) | High | Emergency procedures, training |
| | T (Technology) | High | Automatic slide deployment |
| | P (Program) | High | Safety-critical certification |

---

## 9. Cross-Chapter Integration Matrix

### 9.1 ATA 85 to Related ATA Chapters

Summary of subsystem counts by related ATA chapter:

| Related ATA | # Subsystems | Integration Intensity | Key Touchpoints |
|-------------|--------------|----------------------|-----------------|
| **24 (Electrical)** | 8 | High | Power interfaces, bonding, controls |
| **28 (Fuel)** | 4 | High | H₂ fuel system integration |
| **45 (Diagnostics)** | 9 | High | Data exchange, monitoring |
| **52 (Doors)** | 3 | High | Door operations, interlocks |
| **26 (Fire Protection)** | 5 | Medium-High | Safety systems, fire suppression |
| **21 (Environmental)** | 4 | Medium | Thermal, environmental seals |
| **02 (Operations)** | 7 | Medium | Procedures, limitations, data |
| **95 (DPP, Trace)** | All | High | DPP linkage for all subsystems |
| **99 (Circularity)** | All | Medium | End-of-life, recycling |

### 9.2 Interface Control Documents (ICDs)

For high-integration touchpoints, Interface Control Documents (ICDs) define:

- Mechanical interfaces (connectors, mounting)
- Electrical interfaces (power, signals)
- Data interfaces (protocols, messages)
- Functional interfaces (sequences, timing)
- Safety interfaces (interlocks, monitoring)

ICDs maintained in: [85-00-05_Interfaces](../85-00-05_Interfaces/README.md)

---

## 10. OPT-IN Multi-Pillar Integration

### 10.1 Subsystem OPT-IN Coverage

Summary of subsystem mappings by OPT-IN pillar:

| OPT-IN Pillar | # Subsystems | Typical Involvement |
|---------------|--------------|---------------------|
| **I (Infrastructures)** | All (100%) | Primary pillar for all ATA 85 subsystems |
| **T (Technology)** | 14 (~88%) | Subsystems with on-board system integration |
| **N (Neural & Trace)** | 11 (~69%) | Subsystems with sensors, data, AI |
| **O (Organization)** | 9 (~56%) | Subsystems requiring special procedures/training |
| **P (Program)** | 4 (~25%) | Safety-critical or schedule-critical subsystems |

### 10.2 Example: Multi-Pillar Coordination Scenario

**Scenario**: Implementing H₂ Fueling Interface Subsystem (85-H2-FUEL-001)

| Pillar | Activities | Stakeholders |
|--------|-----------|--------------|
| **I** | Hardware design, installation, testing | Infrastructure engineering team |
| **N** | DPP schema, fueling telemetry, AI monitoring | Data management, AI/ML team |
| **O** | Fueling procedures, training, certification | Operations, training, quality |
| **P** | Schedule, resource allocation, milestones | Program management office (PMO) |
| **T** | ATA 28 fuel system integration, software | On-board systems engineering |

**Integration Touchpoints**:
- I ↔ T: Mechanical/electrical interfaces (ICD)
- I ↔ N: Sensor data to DPP, AI models
- O ↔ I: Procedures documented, training developed
- P ↔ All: Schedule coordination, milestone tracking

---

## 11. Traceability and Impact Analysis

### 11.1 Requirements Traceability

Each subsystem traces to:
- **System requirements** (in [85-00-03_Requirements](../85-00-03_Requirements/README.md))
- **Design specifications** (in [85-00-04_Design](../85-00-04_Design/README.md))
- **Verification plans** (in [85-00-07_V_AND_V](../85-00-07_V_AND_V/README.md))
- **Certification basis** (in [85-00-10_Certification](../85-00-10_Certification/README.md))

### 11.2 Change Impact Analysis

When a subsystem changes, impact analysis considers:

1. **Direct ATA chapter impacts**: Related chapters requiring coordination
2. **Cross-pillar impacts**: OPT-IN pillars affected by change
3. **Interface impacts**: ICDs requiring updates
4. **DPP impacts**: DPP schema or data flow changes
5. **Certification impacts**: Certification basis amendments

**Example**: Change to H₂ Fueling Receptacle (85-RCPT-H2F-001-A)

| Impact Area | Description | Action Required |
|-------------|-------------|-----------------|
| ATA 28 | Fuel system interface | Update ICD, test plan |
| ATA 24 | Bonding design | Review bonding adequacy |
| ATA 95 | Component DPP | Update DPP schema |
| Pillar T | On-board software | Verify compatibility |
| Pillar N | Fueling telemetry | Update data models |
| Pillar O | Fueling procedure | Revise procedures, retrain |

---

## 12. Governance and Maintenance

### 12.1 Mapping Ownership

- **Mapping Owner**: ATA 85 Systems Engineering Lead
- **Review Frequency**: Quarterly
- **Update Triggers**: New subsystem, subsystem change, ATA chapter update, OPT-IN evolution

### 12.2 Change Control

Changes to mappings require:
1. Engineering change proposal (ECP)
2. Cross-functional review (affected ATA chapters, OPT-IN pillars)
3. Configuration Control Board (CCB) approval
4. Documentation updates (this document + related artifacts)
5. Stakeholder notification

---

## 13. References

### 13.1 Internal References

- [85-00-13-001_Subsystems_Components_Overview.md](./85-00-13-001_Subsystems_Components_Overview.md)
- [85-00-13-002_Subsystem_Master_Register.md](./85-00-13-002_Subsystem_Master_Register.md)
- [85-00-03_Requirements](../85-00-03_Requirements/README.md)
- [85-00-04_Design](../85-00-04_Design/README.md)
- [85-00-05_Interfaces](../85-00-05_Interfaces/README.md)

### 13.2 External Standards

- **[ATA iSpec 2200](https://www.ata.org/)** – ATA chapter numbering and documentation standards
- **[SAE ARP4754A](https://www.sae.org/)** – Guidelines for Development of Civil Aircraft and Systems
- **[ISO/IEC 15288](https://www.iso.org/standard/63711.html)** – Systems and software engineering — System life cycle processes

---

## Document Control

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT** – Subject to human review and approval.
- Human approver: _[to be completed]_.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: _2025-11-21_.

---
