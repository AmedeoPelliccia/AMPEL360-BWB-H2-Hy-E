# OPT-IN Framework — Top-Level Standard & Cross-ATA Bucket Schema

**Version:** 1.2
**Date:** 2025-11-17
**Status:** Active
**Owner:** AMPEL360 Documentation WG

---

## 1. Purpose

This document defines the **mandatory program documentation topology** for AMPEL360, unifying:

1. The **OPT-IN axes** (O, P, T, I, N) and their ATA mappings
2. The **canonical XX-00_GENERAL 14-folder lifecycle**
3. The **cross-ATA root buckets** (XX-10/20/30/40/50/60/70/80/90) present in every ATA chapter

This enforces **certification-grade traceability**, **consistent navigation**, and **CI validation**.

---

## 2. OPT-IN Axes (Top Level)

All AMPEL360 documentation is organized under the **OPT-IN Framework**, with five main axes:

```
OPT-IN_FRAMEWORK/
├── O-ORGANIZATION/
├── P-PROGRAM/
├── T-TECHNOLOGY_AMEDEOPELLICCIA-ON_BOARD_SYSTEMS/
│   ├── A-AIRFRAME/
│   ├── M-MECHANICS/
│   ├── E1-ENVIRONMENT/
│   ├── D-DATA/
│   ├── E2-ENERGY/
│   ├── O-OPERATING_SYSTEMS/
│   ├── P-PROPULSION/
│   ├── E3-ELECTRONICS/
│   ├── L1-LOGICS/
│   ├── L2-LINKS/
│   ├── I-INFORMATION_INTELLIGENCE_INTERFACES/
│   ├── C1-COCKPIT_CABIN_CARGO/
│   ├── C2-CIRCULAR_CRYOGENICS_SYSTEMS/
│   ├── I2-R_AND_D/
│   └── A2-AERODYNAMICS/
├── I-INFRASTRUCTURES/
└── N-NEURAL_NETWORKS_USERS_TRACEABILITY/
```

### 2.1 Representative ATA Mapping (Abridged)

#### O — Organization
Policies, limitations, and maintenance frameworks.
- **ATA 00**: General
- **ATA 01**: Maintenance Policy Information
- **ATA 04**: Airworthiness Limitations
- **ATA 05**: Time Limits / Maintenance Checks

#### P — Program
Geometry, handling, servicing, and physical operations.
- **ATA 06**: Dimensions and Areas
- **ATA 07**: Lifting and Shoring
- **ATA 08**: Leveling and Weighing
- **ATA 09**: Towing and Taxiing
- **ATA 12**: Servicing

#### T — Technology (On-Board Systems — AMEDEOPELLICCIA)

##### A-Airframe
- **ATA 20**: Standard Practices Airframe
- **ATA 50-57**: Cargo, Structures, Doors, Fuselage, Nacelles/Pylons, Stabilizers, Windows, Wings

##### M-Mechanics
- **ATA 27**: Flight Controls Actuation
- **ATA 29**: Hydraulic Power
- **ATA 32**: Landing Gear
- **ATA 36**: Pneumatic
- **ATA 37**: Vacuum/Waste Disposal
- **ATA 41**: Water Ballast

##### E1-Environment
- **ATA 21**: Air Conditioning/Pressurization
- **ATA 26**: Fire Protection
- **ATA 30**: Ice/Rain Protection
- **ATA 38**: Water/Waste

##### D-Data
- **ATA 31**: Indicating/Recording (Recording Function) — FDR/CVR

##### E2-Energy
- **ATA 24**: Electrical Power
- **ATA 47**: Inerting System
- **ATA 49**: Airborne Auxiliary Power
- **ATA 80**: Starting

##### O-Operating Systems
- **ATA 42**: IMA Governance (Operating systems, partitioning)

##### P-Propulsion
- **ATA 60-61**: Standard Practices Prop/Rotor, Propellers/Propulsors
- **ATA 70-79**: Engine, Fuel Control, Ignition, Air, Controls, Exhaust, Oil

##### E3-Electronics
- **ATA 34**: Navigation
- **ATA 39**: Electrical/Electronic Panels
- **ATA 42**: IMA Hardware Modules (CPM/IOM)

##### L1-Logics
- **ATA 22**: Autoflight
- **ATA 27**: Flight Controls (Control Laws/SW)
- **ATA 42**: IMA Hosted Applications (Partitions)

##### L2-Links
- **ATA 23**: Communications
- **ATA 42**: IMA Network Fabric (e.g., AFDX)
- **ATA 91**: Charts/Flight Operations

##### I-Information/Intelligence/Interfaces
- **ATA 31**: Indicating/Recording (Indicating Function)
- **ATA 42**: IMA Core OS/APIs/Health Monitoring
- **ATA 45**: Onboard Maintenance Systems
- **ATA 46**: Information Systems/Datalink
- **ATA 77**: Engine Indicating
- **ATA 93**: Onboard Data Load/Configuration (reserved in ATA; used here)

##### C1-Cockpit/Cabin/Cargo
- **ATA 11**: Placards/Markings
- **ATA 15**: Aircrew Information
- **ATA 16**: Change of Role
- **ATA 25**: Equipment/Furnishings
- **ATA 33**: Lights
- **ATA 35**: Oxygen
- **ATA 44**: Cabin Systems

##### C2-Circular/Cryogenics
- **ATA 28**: Fuel (SAF & Cryogenic H₂)
- **ATA 47**: Inerting (link)
- **ATA 99**: Carbon Accounting (provisional)
- **ATA 100**: Circular Metrics (provisional)

##### I2-R&D/AI Integration
- **ATA 40**: Multisystem/AI Integration
- **ATA 42-55-00**: Powertrain/Energy Orchestration (provisional)
- **ATA 42-60-00**: Quantum-Inspired Orchestration (provisional)
- **ATA 48**: In-Flight Maintenance/AI-Enabled (reserved)
- **ATA 92**: Model-Based Maintenance (provisional)

##### A2-Aerodynamics
- **ATA 27**: Flight Controls (Aerodynamic Manipulation)

#### I — Infrastructures
Airports, hydrogen value chains, supply chains, ground facilities, operations.
- **ATA 02**: Operations Information
- **ATA 03**: Support Information/GSE
- **ATA 10**: Parking/Mooring/Storage/RTS
- **ATA 13**: Hardware and General Tools
- **ATA 85-90**: Infrastructure Interface Standards (reserved)
- **ATA 115**: Flight Simulator Systems
- **ATA 116**: Flight Simulator Cuing System

#### N — Neural Networks / Users / Traceability
Digital intelligence and Digital Product Passport.
- **ATA 95**: Digital Product Passport / Neural Networks
- **ATA 96**: Neural Network Training Data (provisional)
- **ATA 97**: Neural Network Models (provisional)
- **ATA 98**: Neural Network Runtime Monitoring (provisional)

---

## 3. Canonical General Layer (Mandatory)

**Every ATA_XX-DESCRIPTION must include the General layer with the full lifecycle:**

```
ATA_XX-DESCRIPTION/
└── XX-00_GENERAL/
    ├── XX-00-01_Overview/
    ├── XX-00-02_Safety/
    ├── XX-00-03_Requirements/
    ├── XX-00-04_Design/
    ├── XX-00-05_Interfaces/
    ├── XX-00-06_Engineering/
    ├── XX-00-07_V_AND_V/
    ├── XX-00-08_Prototyping/
    ├── XX-00-09_Production_Planning/
    ├── XX-00-10_Certification/
    ├── XX-00-11_EIS_Versions_Tags/
    ├── XX-00-12_Services/
    ├── XX-00-13_Subsystems_Components/
    └── XX-00-14_Ops_Std_Sustain/
```

### 3.1 A-LIVE-GP – 14-Folder Lifecycle Skeleton

The standard 14-folder structure used in all `XX-00-00_GENERAL` layers implements the:

**A-LIVE-GP — Aircraft Lifecycle Industrialization and Validation Executive General Plan**

A-LIVE-GP is the canonical lifecycle skeleton for every ATA chapter in the OPT-IN Framework.
It ensures that all systems, subsystems and interfaces are engineered, validated and industrialized under a consistent, certification-grade plan.

#### A-LIVE-GP Folder Mapping

Each `XX-00-00_GENERAL` chapter uses the following 14 folders to implement A-LIVE-GP:

1. **01_OVERVIEW**
   Program / chapter mission, scope, architecture context, stakeholders and governance.

2. **02_SAFETY**
   Safety objectives, FHA/PSSA allocation, risks, mitigations and safety governance.

3. **03_REQUIREMENTS**
   Structured requirements set (functional, performance, safety, regulatory) with IDs and traceability hooks.

4. **04_DESIGN**
   Logical and physical architecture, models, design decisions, trades and baselines.

5. **05_INTERFACES**
   Internal and external interfaces, ICDs, data contracts, infra standards (e.g. ATA 85), and change control.

6. **06_ENGINEERING**
   Detailed engineering work: analyses, simulations, dimensioning, models, calculations, algorithms.

7. **07_V_AND_V**
   Verification & Validation strategy, plans, procedures, coverage and results mapping to requirements.

8. **08_PROTOTYPING**
   Breadboards, rigs, mock-ups, PoCs, pilots, and digital/physical prototyping campaigns (ground + flight where applicable).

9. **09_PRODUCTION_PLANNING**
   Industrialization, supply chain, producibility, process design, production tooling and ramp-up planning.

10. **10_CERTIFICATION**
    Certification basis, means of compliance, evidence structure (DO-178C, DO-254, DO-160, CS-25, etc.) and authority interactions.

11. **11_EIS_VERSIONS_TAGS**
    Entry-Into-Service strategy, versioning model, tags, release notes, in-service modifications and configuration records.

12. **12_SERVICES**
    In-service support: operations support, maintenance program hooks, digital services, customer services integration.

13. **13_SUBSYSTEMS_COMPONENTS**
    Breakdown of subsystems and components under the chapter, with allocation to responsible teams and cross-ATA links.

14. **14_OPS_STD_SUSTAIN**
    Operations standards, procedures, performance standards and sustainability/circularity hooks (integration with ATA 02/99).

### 3.2 Source Pattern
- **Source**: ATA 95-00-00_GENERAL (canonical template)
- **Purpose**: This folder owns governance, requirements, safety, certification, config/change management for the chapter

### 3.3 Lifecycle Folder Descriptions

1. **XX-00-01_Overview**: ATA domain description and global architecture
2. **XX-00-02_Safety**: Safety framework and analysis methods
3. **XX-00-03_Requirements**: Requirements framework and traceability
4. **XX-00-04_Design**: Reference architectures and design patterns
5. **XX-00-05_Interfaces**: General interface rules and ICD templates
6. **XX-00-06_Engineering**: Approach to analysis, models, and simulation
7. **XX-00-07_V_AND_V**: Global verification & validation strategy
8. **XX-00-08_Prototyping**: Prototyping and experimentation policy
9. **XX-00-09_Production_Planning**: Industrialization / deployment strategy
10. **XX-00-10_Certification**: Certification strategy and MoC catalog
11. **XX-00-11_EIS_Versions_Tags**: EIS, versions, CM, and change control
12. **XX-00-12_Services**: In-service MRO and service models
13. **XX-00-13_Subsystems_Components**: Subsystems, components, and PNR/source management
14. **XX-00-14_Ops_Std_Sustain**: Operational standards, governance, circularity

---

## 4. Cross-ATA Root Buckets (Mandatory in Every Chapter)

**Present in every ATA_XX-DESCRIPTION root (even if N/A):**

```
ATA_XX-DESCRIPTION/
├── XX-00_GENERAL/              # (14 lifecycle folders as above)
├── XX-10_Operations/           # Ops use, turnarounds, procedures
├── XX-20_Subsystems/           # Functional subsystems (design-driven)
├── XX-30_Circularity/          # Sustainability, LCA, reuse/recycle, DPP links
├── XX-40_Software/             # SW, control logic, diagnostics, ML/NN
├── XX-50_Structures/           # Frames, housings, mounts, structural routes
├── XX-60_Storages/             # Tanks, reservoirs, accumulators, cryo vessels
├── XX-70_Propulsion/           # Propulsive interfaces/couplings (if any)
├── XX-80_Energy/               # Electrical/thermal energy interactions
└── XX-90_Tables_Schemas_Diagrams/  # Tables, data dicts, catalogs, SDS/training
```

### 4.1 Bucket Descriptions

#### XX-10_Operations
- Operational use cases
- Turnaround procedures
- Line maintenance operations
- Operational limitations

#### XX-20_Subsystems
- Functional subsystems (design-driven)
- Internal structure is free-form
- Must be navigable and traceable

#### XX-30_Circularity
- Sustainability metrics
- Life Cycle Assessment (LCA)
- Reuse/recycle strategies
- Digital Product Passport links
- Carbon accounting

#### XX-40_Software
- Software components
- Control logic
- Diagnostic algorithms
- Machine Learning / Neural Network models
- Runtime monitoring

#### XX-50_Structures
- Frames and housings
- Mounting structures
- Structural routes
- GSE structural elements

#### XX-60_Storages
- Tanks and reservoirs
- Accumulators
- Cryogenic vessels
- Storage interfaces

#### XX-70_Propulsion
- Propulsive interfaces
- Propulsion couplings
- Engine attachments (if applicable)

#### XX-80_Energy
- Electrical energy interactions
- Thermal energy management
- Power distribution interfaces
- Energy storage interfaces

#### XX-90_Tables_Schemas_Diagrams
- Data tables
- Data dictionaries
- System catalogs
- Schemas (XML, JSON, etc.)
- System Data Sheets (SDS)
- Training materials

---

## 5. Definitions (One-Liners)

- **00 General** — General ATA information, audience-based instructions, regulations, governance, standards, configuration & change management.
- **10 Operations** — Operational use, turnaround, ground/flight ops specifics for the ATA domain.
- **20 Subsystems** — Functional systems of the domain; main engineering artefacts live here.
- **30 Circularity** — Sustainability, repairability, reuse/recycle, LCA, carbon accounting.
- **40 Software** — Embedded apps, controllers, diagnostics, analytics, ML/NN for the domain.
- **50 Structures** — Frames, housings, supports, structural routes.
- **60 Storages** — Tanks, reservoirs, accumulators, cryogenic storages (H₂, oils, etc.).
- **70 Propulsion** — Propulsive interface items/couplings (when applicable).
- **80 Energy** — Electrical/thermal energy conversion, distribution, interfaces.
- **90 Schemas** — Data schemas, tables, catalogs, drawing indexes, SDS, training.

---

## 6. Example — ATA 79 (OIL)

```
ATA_79-OIL/
├── 79-00_GENERAL/                    # 14 lifecycle folders (mandatory)
│   ├── 79-00-01_Overview/
│   ├── 79-00-02_Safety/
│   ├── 79-00-03_Requirements/
│   ├── 79-00-04_Design/
│   ├── 79-00-05_Interfaces/
│   ├── 79-00-06_Engineering/
│   ├── 79-00-07_V_AND_V/
│   ├── 79-00-08_Prototyping/
│   ├── 79-00-09_Production_Planning/
│   ├── 79-00-10_Certification/
│   ├── 79-00-11_EIS_Versions_Tags/
│   ├── 79-00-12_Services/
│   ├── 79-00-13_Subsystems_Components/
│   └── 79-00-14_Ops_Std_Sustain/
├── 79-10_Operations/
│   └── 79-10-01_Service_Turnaround_Lubes/
├── 79-20_Subsystems/
│   ├── 79-20-01_Engine_Oil_System/
│   └── 79-20-02_Oil_Condition_Monitoring/
├── 79-30_Circularity/
│   └── 79-30-01_Waste_Oil_Recovery_LCA/
├── 79-40_Software/
│   └── 79-40-01_Oil_Controller_SW/
├── 79-50_Structures/
│   └── 79-50-01_Oil_Tank_Mounts/
├── 79-60_Storages/
│   └── 79-60-01_Oil_Tank_Aft/
├── 79-70_Propulsion/                 # if applicable
├── 79-80_Energy/                     # if applicable
└── 79-90_Tables_Schemas_Diagrams/
    └── 79-90-01_Fluid_Specs_Tables/
```

---

## 7. Rules (Concise)

1. **All chapters include XX-00_GENERAL with all 14 lifecycle folders.**
2. **Buckets 10/20/30/40/50/60/70/80/90 are present in every chapter.**
   - If N/A, keep a `README.md` stating "Not Applicable" and why
   - Do **not** remove the bucket
3. **No 01–14 lifecycle duplication inside buckets.**
   - Bucket internals are design-driven
4. **Naming for bucket items**: `XX-YY-ZZ_DESCRIPTION`
   - XX = ATA chapter (e.g., 95)
   - YY = Bucket number (10, 20, 30, 40, 50, 60, 70, 80, or 90)
   - ZZ = Sequential number within bucket (00, 01, 02, etc.)

---

## 8. CI Validation

The repository includes automated validation to enforce this structure:

- **Script**: `tools/ci/optin_structure_validator.py`
- **Workflow**: `.github/workflows/optin-structure-check.yml`
- **Checks**:
  - Presence of XX-00_GENERAL with all 14 lifecycle folders
  - Presence of all 9 cross-ATA buckets (10/20/30/40/50/60/70/80/90)
  - README.md in each lifecycle folder and bucket
  - Proper naming conventions

---

## 9. Summary

The OPT-IN Framework provides:

1. **Consistency**: Same structure across all ATA chapters
2. **Traceability**: Clear lifecycle stages and cross-cutting concerns
3. **Flexibility**: Design-driven internal structure within buckets
4. **Certification-Ready**: Built-in compliance with regulatory expectations
5. **CI Enforcement**: Automated validation ensures conformance

---

## 10. Document Control

| Version | Date       | Author                      | Changes                                               |
|---------|------------|-----------------------------|-------------------------------------------------------|
| 1.2     | 2025-11-17 | AMPEL360 Documentation WG   | Added concise definitions & ATA 79 example            |
| 1.1     | 2025-11-13 | AMPEL360 Documentation WG   | Initial definition of OPT-IN Framework standard       |
| 1.0     | 2025-11-12 | AMPEL360 Documentation WG   | Draft specification                                   |

---

**ATA 95 (Neural Networks / DPP / Users / Traceability) serves as the canonical template for all GENERAL-layer documentation.**
