# 61-20-03_Blade_System — ATA 61 Subsystem

| Field              | Value                                  |
|--------------------|----------------------------------------|
| **Subsystem ID**   | 61-20-03_Blade_System                  |
| **ATA Chapter**    | 61 – Propellers / Propulsors           |
| **Axis / Bucket**  | P-PROPULSION / 61-20_Subsystems        |
| **Programme**      | AMPEL360 BWB H₂ Hy-E Q100              |
| **Status**         | Active                                 |
| **Version**        | 1.0                                    |
| **Last Updated**   | 2025-12-01                             |
| **Owner**          | AMPEL360 Propulsion Team               |
| **Standard**       | OPT-IN Framework v1.2                  |

---

## 1. Purpose

The **Blade System** subsystem defines the detailed design, materials, and aerodynamic profiling of the fan blades used in the EDF (Electric Ducted Fan) propulsors of the AMPEL360 Q100.

It ensures that blade geometry, structure, materials, and manufacturability meet performance, safety, and sustainability targets.

---

## 2. Scope

This subsystem addresses the **blade-level design and lifecycle**, including:

- Airfoil selection and aerodynamic optimization
- Composite materials and layup design
- Structural sizing and analysis (stress, fatigue, vibration)
- Manufacturing processes and tolerances
- FOD (Foreign Object Damage) and containment considerations
- Sustainability and recyclability of blade materials

Out of scope:

- Full rotor/stator aerodynamic integration (see `61-20-02_Ducted_Fan`)
- Motor design (see `61-20-01_Electric_Motor`)
- Global maintenance programme authoring (ATA 05 – referenced, not owned)

---

## 3. Key Aspects

- **Airfoil Profiles**  
  Optimized for cruise efficiency at Mach 0.78 and appropriate off-design performance.

- **Materials**  
  Advanced composite systems (CFRP or hybrid stacks) targeting weight reduction, stiffness, and damage tolerance.

- **Manufacturing**  
  Automated fiber placement (AFP), resin transfer molding (RTM), or hybrid processes depending on blade geometry and programme requirements.

- **Containment**  
  Design for blade-off containment in accordance with [CS-E 810](https://www.easa.europa.eu/document-library/certification-specifications/cs-e-amendment-6) or equivalent requirements.

---

## 4. Contents of This Subsystem Folder

This folder should contain:

- **Blade geometry definitions**  
  Airfoil coordinates, twist distribution, chord distribution (CSV, YAML, or SVG format)

- **Material specifications and layup schedules**  
  Composite ply tables, material properties, stacking sequences

- **Structural analysis reports**  
  Stress, fatigue, vibration, bird strike, and containment analyses

- **Manufacturing process specifications**  
  Process parameters, quality control requirements, tolerances

- **FOD tolerance analysis**  
  Impact resistance, damage propagation, and repair limits

---

## 5. Interfaces

### 5.1 Internal Subsystem Interfaces

- **61-20-02_Ducted_Fan**  
  - *Type:* Mechanical / Design  
  - *Description:* Integration with rotor hub, blade attachment, and aerodynamic integration.

- **61-50_Structures**  
  - *Type:* Structural  
  - *Description:* Load paths to nacelle, blade containment structure.

### 5.2 Cross-ATA Interfaces

- **61-30_ANCHORS**  
  - Sustainability and recyclability of blade materials; LCA data for blade production and end-of-life.

- **ATA 05 – Maintenance**  
  - Maintenance and inspection procedures, blade replacement intervals, and repair schemes.

---

## 6. Status

- **Subsystem ID:** 61-20-03  
- **Lifecycle State:** Active / In Definition & Early Engineering  
- **Safety Criticality:** To be defined in `61-00-02_Safety`  
- **Linked Requirements:** To be defined in `61-00-03_Requirements` (REQ-61-20-03-XXX)

---

## 7. Document Control

- **Standard:** OPT-IN Framework v1.2  
- **Owner:** AMPEL360 Propulsion Team  
- **Generation:** Produced with AI assistance under deterministic, version-controlled prompts (GitHub Copilot / ChatGPT API).  
- **Approval:** Pending human review and configuration management per `61-00-11_EIS_Versions_Tags` and CC/CM rules.

---

*This folder is part of the `61-20_Subsystems` bucket under ATA 61 — Propellers/Propulsors.*
