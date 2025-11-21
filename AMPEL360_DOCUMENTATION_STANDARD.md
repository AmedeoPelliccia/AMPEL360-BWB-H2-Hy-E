# AMPEL360 Documentation & OPT-IN Structure Standard

**Version:** 1.5  
**Date:** 2025-11-13  
**Status:** ACTIVE

> **Note**: This document provides a comprehensive overview of the OPT-IN Framework.
> For the complete mandatory standard including cross-ATA buckets and CI validation,
> see [OPT-IN_FRAMEWORK_STANDARD.md](OPT-IN_FRAMEWORK_STANDARD.md)

---

## 1. OPT-IN Framework Top-Level Structure

All documentation in the AMPEL360 program is organized under the **OPT-IN Framework**, with five main axes:

```text
OPT-IN_FRAMEWORK/
├── O-ORGANIZATION/
├── P-PROGRAM/
├── T-TECHNOLOGY/        # AMEDEOPELLICCIA taxonomy – on-board systems
├── I-INFRASTRUCTURES/   # Airports, H2 value chains, supply chains, facilities, operations
└── N-NEURAL_NETWORKS_USERS_TRACEABILITY/
````

Each axis is mapped to specific ATA chapters as follows.

---

### 1.1 O – ORGANIZATION

Policies, limitations, and maintenance frameworks.

```text
O-ORGANIZATION/
├── ATA_00_GENERAL/
├── ATA_01_MAINTENANCE_POLICY_INFORMATION/
├── ATA_04_AIRWORTHINESS_LIMITATIONS/
└── ATA_05_TIME_LIMITS_MAINTENANCE_CHECKS/
```

---

### 1.2 P – PROGRAM

Geometry, handling, servicing, and physical operations of the aircraft.

```text
P-PROGRAM/
├── ATA_06_DIMENSIONS_AND_AREAS/
├── ATA_07_LIFTING_AND_SHORING/
├── ATA_08_LEVELING_AND_WEIGHING/
├── ATA_09_TOWING_AND_TAXIING/
└── ATA_12_SERVICING/
```

---

### 1.3 T – TECHNOLOGY (On-Board Systems – AMEDEOPELLICCIA)

On-board systems are structured using the A-M-E-D-E-O-P-E-L-I-C-C-I₂-A₂ taxonomy.

```text
T-TECHNOLOGY/
├── A-AIRFRAME/
│   ├── ATA_20_STANDARD_PRACTICES_AIRFRAME/
│   ├── ATA_50_CARGO_ACCESSORY_COMPARTMENTS/
│   ├── ATA_51_STANDARD_PRACTICES_STRUCTURES_GENERAL/
│   ├── ATA_52_DOORS/
│   ├── ATA_53_FUSELAGE/
│   ├── ATA_54_NACELLES_PYLONS/
│   ├── ATA_55_STABILIZERS/
│   ├── ATA_56_WINDOWS/
│   └── ATA_57_WINGS/
│
├── M-MECHANICS/
│   ├── ATA_27_FLIGHT_CONTROLS_ACTUATION/
│   ├── ATA_29_HYDRAULIC_POWER/
│   ├── ATA_32_LANDING_GEAR/
│   ├── ATA_36_PNEUMATIC/
│   ├── ATA_37_VACUUM_WASTE_DISPOSAL/
│   └── ATA_41_WATER_BALLAST/
│
├── E1-ENVIRONMENT/
│   ├── ATA_21_AIR_CONDITIONING_PRESSURIZATION/
│   ├── ATA_26_FIRE_PROTECTION/
│   ├── ATA_30_ICE_RAIN_PROTECTION/
│   └── ATA_38_WATER_WASTE/
│
├── D-DATA/
│   └── ATA_31_INDICATING_RECORDING_RECORDING_FUNCTION/   # FDR/CVR
│
├── E2-ENERGY/
│   ├── ATA_24_ELECTRICAL_POWER/
│   ├── ATA_47_INERTING_SYSTEM/
│   ├── ATA_49_AIRBORNE_AUXILIARY_POWER/
│   └── ATA_80_STARTING/
│
├── O-OPERATING_SYSTEMS/
│   └── ATA_42_IMA_GOVERNANCE/                            # Operating systems, partitioning
│
├── P-PROPULSION/
│   ├── ATA_60_STANDARD_PRACTICES_PROP_ROTOR/
│   ├── ATA_61_PROPELLERS_PROPULSORS/
│   ├── ATA_70_STANDARD_PRACTICES_ENGINE/
│   ├── ATA_71_POWER_PLANT/
│   ├── ATA_72_ENGINE/
│   ├── ATA_73_ENGINE_FUEL_CONTROL/
│   ├── ATA_74_IGNITION/
│   ├── ATA_75_AIR/
│   ├── ATA_76_ENGINE_CONTROLS/
│   ├── ATA_78_EXHAUST/
│   └── ATA_79_OIL/
│
├── E3-ELECTRONICS/
│   ├── ATA_34_NAVIGATION/
│   ├── ATA_39_ELECTRICAL_ELECTRONIC_PANELS/
│   └── ATA_42_IMA_HARDWARE_MODULES/                       # CPM/IOM
│
├── L1-LOGICS/
│   ├── ATA_22_AUTOFLIGHT/
│   ├── ATA_27_FLIGHT_CONTROLS_CONTROL_LAWS_SW/
│   └── ATA_42_IMA_HOSTED_APPLICATIONS/                    # Partitions
│
├── L2-LINKS/
│   ├── ATA_23_COMMUNICATIONS/
│   ├── ATA_42_IMA_NETWORK_FABRIC/                         # e.g. AFDX
│   └── ATA_91_CHARTS_FLIGHT_OPERATIONS/
│
├── I-INFORMATION_INTELLIGENCE_INTERFACES/
│   ├── ATA_31_INDICATING_RECORDING_INDICATING_FUNCTION/
│   ├── ATA_42_IMA_CORE_OS_APIS_HEALTH_MONITORING/
│   ├── ATA_45_ONBOARD_MAINTENANCE_SYSTEMS/
│   ├── ATA_46_INFORMATION_SYSTEMS_DATALINK/
│   ├── ATA_77_ENGINE_INDICATING/
│   └── ATA_93_ONBOARD_DATA_LOAD_CONFIGURATION/            # Reserved in ATA; used here
│
├── C1-COCKPIT_CABIN_CARGO/
│   ├── ATA_11_PLACARDS_MARKINGS/
│   ├── ATA_15_AIRCREW_INFORMATION/
│   ├── ATA_16_CHANGE_OF_ROLE/
│   ├── ATA_25_EQUIPMENT_FURNISHINGS/
│   ├── ATA_33_LIGHTS/
│   ├── ATA_35_OXYGEN/
│   └── ATA_44_CABIN_SYSTEMS/
│
├── C2-CIRCULAR_CRYOGENICS_SYSTEMS/
│   ├── ATA_28_FUEL_SAF_CRYOGENIC_H2/
│   └── ATA_21-80-00_CO2_CAPTURE_PROCESSING_PROV/
│
├── I2-I_PLUS_D/
│   ├── ATA_40_MULTISYSTEM_AI_INTEGRATION/
│   ├── ATA_42-55-00_POWERTRAIN_ENERGY_ORCHESTRATION_PROV/
│   ├── ATA_42-60-00_QUANTUM_INSPIRED_ORCHESTRATION_PROV/
│   ├── ATA_48_IN_FLIGHT_MAINTENANCE_AI_ENABLED_RESERVED/
│   └── ATA_92_MODEL_BASED_MAINTENANCE_PROV/
│
└── A2-AERODYNAMICS/
    └── ATA_27_FLIGHT_CONTROLS_AERODYNAMIC_MANIPULATION/
```

---

### 1.4 I – INFRASTRUCTURES

Airports, hydrogen value chains, supply chains, ground facilities, operations.

```text
I-INFRASTRUCTURES/
├── ATA_02_OPERATIONS_INFORMATION/
├── ATA_03_SUPPORT_INFORMATION_GSE/
├── ATA_10_PARKING_MOORING_STORAGE_RTS/
├── ATA_13_HARDWARE_AND_GENERAL_TOOLS/
├── ATA_85-90_INFRASTRUCTURE_INTERFACE_STANDARDS_RESERVED/
├── ATA_115_FLIGHT_SIMULATOR_SYSTEMS/
└── ATA_116_FLIGHT_SIMULATOR_CUING_SYSTEM/
```

---

### 1.5 N – NEURAL NETWORKS, USERS, TRACEABILITY

Digital intelligence and Digital Product Passport.

```text
N-NEURAL_NETWORKS_USERS_TRACEABILITY/
└── ATA_95_DIGITAL_PRODUCT_PASSPORT_NEURAL_NETWORKS/
```

ATA 95 (Neural Networks / DPP / Users / Traceability) is also the **canonical template** for GENERAL-layer documentation (`XX-00-00_GENERAL`).

---

## 2. Standard Root Structure per ATA Chapter

Every ATA chapter (`ATA_XX-…`) in the AMPEL360 repo **MUST** follow the same top-level pattern:

```text
ATA_XX-SYSTEM_NAME/
├── XX-00-00_GENERAL/
│   ├── XX-00-01_Overview/               # ATA domain description and global architecture
│   ├── XX-00-02_Safety/                 # Safety framework and analysis methods
│   ├── XX-00-03_Requirements/           # Requirements framework and traceability
│   ├── XX-00-04_Design/                 # Reference architectures and design patterns
│   ├── XX-00-05_Interfaces/             # General interface rules and ICD templates
│   ├── XX-00-06_Engineering/            # Approach to analysis, models and simulation
│   ├── XX-00-07_V_AND_V/                # Global verification & validation strategy
│   ├── XX-00-08_Prototyping/            # Prototyping and experimentation policy
│   ├── XX-00-09_Production_Planning/    # Industrialization / deployment strategy
│   ├── XX-00-10_Certification/          # Certification strategy and MoC catalog
│   ├── XX-00-11_EIS_Versions_Tags/      # EIS, versions, CM and change control
│   ├── XX-00-12_Services/               # In-service MRO and service models
│   ├── XX-00-13_Subsystems_Components/  # Subsystems, components and PNR/source management
│   └── XX-00-14_Ops_Std_Sustain/        # Operational standards, governance, circularity
│
├── XX-20-00_Systems/                    # Functional systems (origin block 20)
├── XX-40-00_Programming_Algorithms/     # SW, logic, NN, algorithms
├── XX-50-00_Structures/                 # Physical structures / airframe / structural GSE
├── XX-70-00_Propulsion/                 # Propulsion / energy (70/80 as applicable)
└── XX-90-00_Tables_Schemas_Diagrams/    # Tables, catalogs, schemas, SDS, training, meta
```

### 2.1 GENERAL Layer

* `XX-00-00_GENERAL/` is **mandatory** for every `ATA_XX`.
* The 14 subfolders `XX-00-01_…` to `XX-00-14_…` are **mandatory**.
* Each must contain at least a `README.md` stating:

  * Scope of the area (Overview, Safety, Requirements, …)
  * How it applies to this ATA chapter
  * Status (`Pending`, `Draft`, `Active`, `Deprecated`)

#### A-LIVE-GP – 14-Folder Lifecycle Skeleton

The standard 14-folder structure used in all `XX-00-00_GENERAL` layers implements the:

**A-LIVE-GP — Aircraft Lifecycle Industrialization and Validation Executive General Plan**

A-LIVE-GP is the canonical lifecycle skeleton for every ATA chapter in the OPT-IN Framework.
It ensures that all systems, subsystems and interfaces are engineered, validated and industrialized under a consistent, certification-grade plan.

##### A-LIVE-GP Folder Mapping

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

### 2.2 Origin Blocks: 20 / 40 / 50 / 70 / 90

The following “origin blocks” are used consistently:

* `XX-20-00_Systems/` → **functional systems** of that ATA domain
* `XX-40-00_Programming_Algorithms/` → **software, logic, NN, algorithms**
* `XX-50-00_Structures/` → **physical structures / supports / airframe / GSE frames**
* `XX-70-00_Propulsion/` → **propulsion & energy** (mapped to 70/80 family as needed)
* `XX-90-00_Tables_Schemas_Diagrams/` → **catalogs, tables, schemas, SDS, training, meta**

Concrete systems live under these origin directories as `XX-20-YY_*`, `XX-40-YY_*`, etc., with their own internal structure (see next section).

---

## 3. Per-System Breakdown (Design-Driven)

Each system under `XX-20-00_…`, `XX-40-00_…`, `XX-50-00_…`, `XX-70-00_…`, `XX-90-00_…`:

* **Does not** have to implement the 01…14 folders.
* **Must** be structured according to how that system is:

  * conceived,
  * designed,
  * implemented,
  * and evolved in time.

Examples:

```text
03-80-01_LH2_CRYO_REFUELER/
├── SYSTEM_ARCHITECTURE/
├── CONTROL_SOFTWARE/
├── HARDWARE_DESIGN/
├── TEST_RIGS/
├── FIELD_DATA/
└── CERTIFICATION_EVIDENCE/
```

```text
95-10-00_FLIGHT_CONTROL_NN/
├── HIGH_LEVEL_DESIGN/
├── TRAINING_DATA/
├── MODELS/
├── RUNTIME_MONITORING/
└── SAFETY_CASE/
```

The structure is **free**, as long as:

* It is navigable and understandable.
* Artefacts can be traced to lifecycle areas and requirements.

(You can enforce lifecycle linkage via metadata, RTMs, or index files – as you already defined in your UTCS/DET layer.)

---

## 4. Summary of Rules

1. **OPT-IN Framework** is the top-level organization: O, P, T, I, N.
2. Every ATA domain sits under one of those axes exactly as mapped above.
3. Every `ATA_XX-SYSTEM_NAME/` **must** have:

   * `XX-00-00_GENERAL/` with all 14 GENERAL subfolders.
   * The origin buckets `XX-20-00_…`, `XX-40-00_…`, `XX-50-00_…`, `XX-70-00_…`, `XX-90-00_…` as applicable.
4. Concrete systems live under `XX-20/40/50/70/90` and are **designed-driven** in their internal folder breakdown.
5. ATA 95 acts as the **canonical template** for GENERAL (`XX-00-00_GENERAL`), and is the reference when in doubt.

---

## 5. Document Control

| Version | Date       | Author                  | Changes                                                           |
| ------- | ---------- | ----------------------- | ----------------------------------------------------------------- |
| 1.5     | 2025-11-13 | AMPEL360 Documentation  | Added reference to OPT-IN_FRAMEWORK_STANDARD.md                   |
| 1.4     | 2025-11-12 | AMPEL360 Documentation  | Integrated full OPT-IN/ATA mapping + canonical ATA_XX root layout |
| 1.3     | 2025-11-12 | AMPEL360 Documentation  | Fixed GENERAL layer, per-system breakdown free + metadata concept |
| 1.2     | 2025-11-12 | AMPEL360 Documentation  | Added XX-20/40/50/70/90 root buckets per ATA chapter              |
| 1.1     | 2025-11-12 | AMPEL360 Implementation | Formalized XX-00-00_GENERAL                                       |
| 1.0     | 2025-11-12 | AMPEL360 Implementation | Initial documentation standard                                    |


