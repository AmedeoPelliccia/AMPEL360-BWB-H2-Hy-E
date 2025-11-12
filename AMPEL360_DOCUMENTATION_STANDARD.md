# AMPEL360 Documentation Standard

**Version:** 1.3  
**Date:** 2025-11-12  
**Status:** ACTIVE

---

## 1. Purpose

This standard defines the **mandatory documentation structure** for the  
**AMPEL360-BWB-H₂-Hy-E** program.

All ATA chapters (`ATA_XX`) and systems documented in the repository  
**MUST** follow these rules to ensure:

- **Consistent documentation** across all domains  
- **Certification readiness** with complete traceability  
- Coverage of the **full lifecycle** (concept → in-service operation)  
- Compliance with **ATA iSpec 2200**, **S1000D**, and applicable aviation regulations  

---

## 2. Canonical Reference: ATA 95-00-00_GENERAL

The canonical reference for the documentation structure is:

```text
/OPT-IN_FRAMEWORK/N-NEURAL_NETWORKS_USERS_TRACEABILITY/
    ATA_95_NEURAL_NETWORKS/95-00-00_GENERAL/
````

ATA 95-00-00_GENERAL defines the pattern for:

* The **GENERAL layer** of an ATA chapter
* The **14 lifecycle areas**
* Naming and traceability style

**Rule:**
Every new `ATA_XX` chapter must follow this same organizational logic, adapted to its own technical domain.

---

## 3. Root Structure per ATA Chapter

Each ATA chapter in AMPEL360 is organized as:

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

### 3.1 GENERAL Layer Rules (`XX-00-00_GENERAL`)

* `XX-00-00_GENERAL/` is **mandatory** for every `ATA_XX`.
* The 14 subfolders `XX-00-01_…` to `XX-00-14_…` are **always required**.
* Each of them must contain at least a `README.md` describing:

  * The purpose of that area within this ATA chapter
  * The scope of content expected there
  * The status (`Pending`, `Draft`, `Active`, `Deprecated`)

This GENERAL layer defines **how the chapter is documented**, not the internal details of any specific system.

---

## 4. The 14 Lifecycle Areas as “Lenses”

The 14 lifecycle areas define the **coverage space** that documentation must address, but:

* They are materialized as **folders only** under `XX-00-00_GENERAL`.
* For concrete systems, they are **conceptual lenses**: each artefact is tagged against one or more lifecycle areas using metadata / indices.

### 4.1 Lifecycle Areas (Semantics)

1. **Overview** – description, purpose, scope, high-level architecture
2. **Safety** – FHA, FMEA, FTA, CCA, safety objectives and safety requirements
3. **Requirements** – functional / non-functional requirements + traceability
4. **Design** – architecture and detailed design, models, design decisions
5. **Interfaces** – interfaces, ICDs, protocols, data formats, timing
6. **Engineering** – engineering analysis, simulation, models, trade-offs
7. **V_AND_V** – verification & validation (plans, test cases, coverage)
8. **Prototyping** – prototypes, rigs, PoCs, experiments, lessons learned
9. **Production_Planning** – industrialization, ramp-up, supply chain, quality
10. **Certification** – regulatory mapping, MoC, evidence, certification plan
11. **Operations_Maintenance** – operation, maintenance, troubleshooting, SBs
12. **Assets_Management** – spares, tooling, datasets, versions, CM
13. **Subsystems_Components** – breakdown, component specs, integration
14. **Ops_Std_Sustain / Meta_Governance** – standards, CI/CD, metadata, sustainability

---

## 5. Per-System Breakdown: Free but Traceable

Each concrete system (`XX-20-01_*`, `XX-50-01_*`, `03-80-01_LH2_CRYO_REFUELER`, etc.):

* Is **NOT required** to replicate the `01_OVERVIEW`…`14_META_GOVERNANCE` folder structure.
* **MUST** be structured in a way that makes sense for how that system is:

  * conceived,
  * designed,
  * and evolved over time (increments, baselines, versions, blocks, etc.).

Examples of valid system-specific breakdowns:

```text
03-80-01_LH2_CRYO_REFUELER/
├── SYSTEM_ARCHITECTURE/
├── CONTROL_SOFTWARE/
├── HARDWARE_DESIGN/
├── TEST_RIGS/
├── FIELD_DATA/
└── CERTIFICATION_EVIDENCE/
```

or:

```text
95-10-00_FLIGHT_CONTROL_NN/
├── HIGH_LEVEL_DESIGN/
├── TRAINING_DATA/
├── MODELS/
├── RUNTIME_MONITORING/
└── SAFETY_CASE/
```

### 5.1 Mandatory: Lifecycle Metadata

Even though the folder trees are free:

* Every artefact (document, model, script, dataset, etc.) must carry metadata indicating:

  * `ata_code` – e.g. `03-80-01`
  * `lifecycle_area` – one or more of
    `[01_Overview, 02_Safety, …, 14_Ops_Std_Sustain]`

Example of YAML front-matter in a `.md` file:

```yaml
---
ata_code: "03-80-01"
lifecycle_area:
  - "02_Safety"
  - "07_V_AND_V"
status: "Active"
---
```

This way:

* The **system** can evolve with whatever structure engineering needs.
* The **standard** still guarantees lifecycle coverage 01–14 through metadata.

---

## 6. ATA Code “Law of Origin” (20 / 40 / 50 / 70–80 / 90)

**AMPEL360 Law of Origin:**

* **20-xx → SYSTEMS** (functional / operational)
* **40-xx → PROGRAMMING / LOGIC / SW / NN / algorithms**
* **50-xx → STRUCTURES** (physical / airframe / structural GSE)
* **70-xx / 80-xx → PROPULSION / ENERGY**
* **90-xx → SCHEMAS / META / CATALOGS / TRAINING / SDS**

### 6.1 Application per Chapter

For each `ATA_XX` chapter:

* `XX-20-YY_*` → functional systems of that domain
* `XX-40-YY_*` → logic, software, algorithms, NN specific to that domain
* `XX-50-YY_*` → associated structures
* `XX-70-YY_*` / `XX-80-YY_*` → propulsion / energy systems
* `XX-90-YY_*` → catalogs, tables, training, SDS, registries, schemas

Blocks **10, 30, 60** are considered **reserved** and may only be used when:

* required by the standard ATA numbering,
* explicitly requested by an authority, or
* supported by a **documented** AMPEL360 program decision.

---

## 7. Minimum Content Requirements

### 7.1 In `XX-00-00_GENERAL/`

Each folder `XX-00-01_…` to `XX-00-14_…` must contain:

* A `README.md` with at least:

  * Purpose of that area in this ATA chapter
  * Scope of the content
  * Status (`Pending`, `Draft`, `Active`, `Deprecated`)
  * Key internal/external references

### 7.2 In Systems (`XX-20-YY_*`, `XX-50-YY_*`, etc.)

Each system must have at least:

* A `README.md` at system root
* An index file (`INDEX.meta.yaml` or equivalent)
* Metadata on key artefacts specifying `ata_code` and `lifecycle_area`

There is **no fixed requirement** on subfolder names, as long as:

* The structure is navigable and understandable
* Lifecycle coverage via metadata is possible (01–14)
* The structure makes sense for the way the system is conceived, designed and evolves

---

## 8. Integration with OPT-IN and CAOS

* Each `ATA_XX` chapter is mapped to one or more **OPT-IN axes** (O, P, T, I, N).
* ATA 95 and CAOS-related systems must:

  * Document DPP, Service Twin, federated learning integration in Overview/Design/Engineering.
  * Capture AI/ML requirements and evidence in Safety/Requirements/V&V/Certification/Assets/Meta.

**CAOS** appears primarily in:

* `Overview` – CAOS concept and role in the system
* `Engineering` – models, algorithms, simulations
* `V_AND_V` – performance, robustness and monitoring tests
* `Operations_Maintenance` – CAOS in service
* `Assets_Management` – models, datasets, services and versions

---

## 9. Implementation Checklist

For a new `ATA_XX`:

* [ ] Create `ATA_XX-SYSTEM_NAME/`.
* [ ] Create `XX-00-00_GENERAL/` with subfolders `XX-00-01_…` to `XX-00-14_…`.
* [ ] Add `README.md` to each folder in `XX-00-00_GENERAL/`.
* [ ] Create the root buckets:

  * `XX-20-00_Systems/`
  * `XX-40-00_Programming_Algorithms/`
  * `XX-50-00_Structures/`
  * `XX-70-00_Propulsion/`
  * `XX-90-00_Tables_Schemas_Diagrams/`
* [ ] For each new system (`XX-20-YY_*`, `XX-40-YY_*`, etc.), design a folder breakdown that fits its nature.
* [ ] Ensure artefacts include `ata_code` and `lifecycle_area` metadata.
* [ ] Check consistency against `ATA_95_NEURAL_NETWORKS/95-00-00_GENERAL`.

---

## 10. Document Control

| Version | Date       | Author                  | Changes                                                              |
| ------- | ---------- | ----------------------- | -------------------------------------------------------------------- |
| 1.3     | 2025-11-12 | AMPEL360 Documentation  | GENERAL layer fixed (14 areas), per-system breakdown free + metadata |
| 1.2     | 2025-11-12 | AMPEL360 Documentation  | Added XX-20/40/50/70/90 root buckets per ATA chapter                 |
| 1.1     | 2025-11-12 | AMPEL360 Implementation | Formalized XX-00-00_GENERAL                                          |
| 1.0     | 2025-11-12 | AMPEL360 Implementation | Initial documentation standard                                       |

---

## 11. Contact

* **Responsible team:** AMPEL360 Program Documentation Team
* **Channel:** GitHub Issues (label `documentation-standard`)

*This standard is mandatory for all documentation in the AMPEL360-BWB-H₂-Hy-E program.*

```


