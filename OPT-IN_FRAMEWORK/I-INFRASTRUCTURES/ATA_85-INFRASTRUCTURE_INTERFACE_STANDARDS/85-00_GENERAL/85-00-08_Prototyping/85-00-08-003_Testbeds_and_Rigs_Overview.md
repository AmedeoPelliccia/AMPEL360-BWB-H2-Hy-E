# 85-00-08-003 Testbeds and Rigs Overview

## 1. Purpose

This document provides an overview of physical testbeds, rigs, and mockups used to validate infrastructure interfaces for the AMPEL360 BWB aircraft with H2 propulsion and CO₂ battery systems.

## 2. Scope

Covers:
- **Testbeds**: Permanent or semi-permanent facilities for controlled testing
- **Rigs**: Portable or specialized equipment for specific interface validation
- **Mockups**: Physical replicas for human factors, clearance, and procedural testing

## 3. Testbed Categories

### 3.1 H2 Infrastructure Testbeds
Purpose: Validate liquid hydrogen (LH2) refueling interfaces, safety systems, and cryogenic handling.

**Key Facilities**:
- **LH2 Refueling Rig**: Full-scale connector compatibility per [ISO 19880-3](https://www.iso.org/standard/62359.html)
- **Cryogenic Handling Testbed**: Thermal management, leak detection, emergency shutdown
- **Safety Zone Validation**: Distance and ventilation requirements per [ISO/TR 15916](https://www.iso.org/standard/29316.html)

**Location Options**:
- Partner facility (e.g., hydrogen production site)
- Dedicated test site with safety clearances
- Aircraft ground test facility (post-integration)

**Documentation**: See [H2_INFRASTRUCTURE_INTERFACE](./H2_INFRASTRUCTURE_INTERFACE/README.md)

### 3.2 CO₂ Battery Interface Testbeds
Purpose: Validate closed-loop CO₂ battery ground exchange and buffer management.

**Key Facilities**:
- **CO₂ Battery Dock Rig**: Mechanical coupling, leak-tight seals, thermal management
- **Buffer Exchange Testbed**: Rapid exchange of CO₂ buffer tanks, pressure equalization
- **Closed-Loop Validation**: End-to-end CO₂ capture, storage, and reintegration

**Location Options**:
- Laboratory mockup (early phase)
- Airport apron test site (pilot deployment)
- Integrated aircraft ground test (final validation)

**Documentation**: See [CO2_BATTERY_INTERFACE](./CO2_BATTERY_INTERFACE/README.md)

### 3.3 Airport Interface Testbeds
Purpose: Validate apron operations, gate turnaround, and BWB-specific clearances.

**Key Facilities**:
- **Gate Mockup**: Full-scale boarding bridge alignment and door clearance
- **Apron Operations Rig**: Taxiway/stand navigation, wingtip clearances, camera sightlines
- **Turnaround Simulation**: Coordinated GSE positioning, timing, and workflows

**Location Options**:
- Airport partner facility (e.g., test gate at partner hub)
- Aircraft manufacturer test facility
- Virtual mockup + on-site validation

**Documentation**: See [AIRPORT_INTERFACE](./AIRPORT_INTERFACE/README.md)

### 3.4 Ground Services Equipment (GSE) Testbeds
Purpose: Validate multi-GSE integration, smart scheduling, and automated coordination.

**Key Facilities**:
- **Multi-GSE Hub**: Simultaneous power, cooling, de-icing, lavatory, and cargo GSE
- **Smart Scheduling Pilot**: Automated GSE dispatch and conflict resolution
- **Interface Compatibility Rig**: Electrical, pneumatic, and data interface validation

**Location Options**:
- Ground handling provider facility
- Airport apron test site
- Virtual coordination via digital twin

**Documentation**: See [GROUND_SERVICES_INTERFACE](./GROUND_SERVICES_INTERFACE/README.md)

### 3.5 Passenger Boarding/Evacuation Mockups
Purpose: Validate boarding flow, evacuation pathways, and human factors for BWB configuration.

**Key Facilities**:
- **Boarding Flow Mockup**: Full-scale cabin section, door alignment, passenger flow timing
- **Evacuation Pathway Mockup**: Emergency exit accessibility, slide deployment, evacuation timing per [CS-25.803](https://www.easa.europa.eu/en/document-library/certification-specifications/cs-25-large-aeroplanes)
- **Human Factors Lab**: Passenger and crew usability studies

**Location Options**:
- Aircraft manufacturer facility
- Certification test facility
- Partner airport for operational trials

**Documentation**: See [PAX_BOARDING_EVAC_INTERFACE](./PAX_BOARDING_EVAC_INTERFACE/README.md)

### 3.6 Digital Twin Testbeds
Purpose: Hardware-in-the-loop (HIL) and software-in-the-loop (SIL) validation of infrastructure interfaces.

**Key Facilities**:
- **Interface Digital Twin**: Virtual representation of airport, GSE, and aircraft ground interfaces
- **HIL Rig**: Real control systems interacting with simulated environment
- **Scenario Library**: Pre-defined test cases (nominal, off-nominal, emergency)

**Location Options**:
- On-premise compute cluster
- Cloud-based simulation platform
- Hybrid (local HIL rig + cloud digital twin)

**Documentation**: See [DIGITAL_TWIN_PROTOTYPES](./DIGITAL_TWIN_PROTOTYPES/README.md)

## 4. Rig Design Principles

### 4.1 Safety First
- Fail-safe mechanical and software interlocks
- Emergency stop accessible from all positions
- Personnel training and PPE requirements
- Incident reporting and continuous improvement

### 4.2 Modularity and Reusability
- Modular components for multiple test configurations
- Portable rigs for field trials
- Digital twin integration for hybrid testing

### 4.3 Instrumentation and Data Collection
- Sensor coverage: pressure, temperature, flow, force, position
- High-frequency data logging for transient events
- Video/photo documentation for qualitative analysis
- Data feeds to digital twin for calibration

### 4.4 Regulatory Compliance
- Testbeds designed to demonstrate compliance with [CS-25](https://www.easa.europa.eu/en/document-library/certification-specifications/cs-25-large-aeroplanes), [DO-160G](https://standards.sae.org/do160g/) (environmental), and [NFPA 2](https://www.nfpa.org/codes-and-standards/all-codes-and-standards/list-of-codes-and-standards/detail?code=2) (hydrogen safety)
- Certification authority observation and approval
- Traceability to [85-00-10 Certification](../85-00-10_Certification/README.md)

## 5. Rig Inventory and Status

For a consolidated register of all prototypes and testbeds, see:
- [85-00-08-MASTER-001 Prototype Inventory](./MASTER/85-00-08-MASTER-001_Prototype_Inventory.md)
- [Prototype Register (Excel)](./MASTER/ASSETS/REGISTERS/85-00-08-A-001_Prototype_Register.xlsx)

## 6. Traceability

Links to:
- [85-00-08-001 Prototyping Strategy](./85-00-08-001_Prototyping_Strategy.md) – Overall strategy
- [85-00-07 V&V](../85-00-07_V_AND_V/README.md) – V&V test planning
- [85-00-06 Engineering](../85-00-06_Engineering/README.md) – Detailed engineering designs for rigs

---

## Document Control

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT** – Subject to human review and approval.
- Human approver: _[to be completed]_.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: 2025-11-21.

---
