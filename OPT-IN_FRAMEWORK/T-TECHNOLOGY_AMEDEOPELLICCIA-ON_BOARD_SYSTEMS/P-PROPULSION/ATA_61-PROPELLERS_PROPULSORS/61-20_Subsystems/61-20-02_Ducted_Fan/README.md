# 61-20-02_Ducted_Fan — ATA 61 Subsystem

| Field              | Value                                  |
|--------------------|----------------------------------------|
| **Subsystem ID**   | 61-20-02_Ducted_Fan                    |
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

The **Ducted Fan** subsystem defines the aerodynamic thrust-producing module of each EDF (Electric Ducted Fan) propulsor.  
It comprises the **rotating fan**, **stator vanes**, and the **nacelle duct** that guides and accelerates airflow to generate thrust from the mechanical power delivered by the electric motor.

---

## 2. Scope

This subsystem covers the **aerodynamic, acoustic, and structural design** of the ducted fan assembly, including:

- Fan rotor design (blade count, twist, chord distribution)
- Stator vane geometry and flow-straightening design
- Nacelle duct aerodynamics and airflow management
- Spinner and inlet cone integration
- Mechanical integration with the electric motor
- Performance maps across the propulsion envelope

Excluded:

- Motor electromagnetic design (see `61-20-01_Electric_Motor`)
- Propulsor-level control loops (see `61-20-04_Propulsor_Control_Unit`)
- Full nacelle external structure (mostly ATA 57 + ATA 53 integration)

---

## 3. Key Components

- **Fan Rotor** — Rotating blade assembly generating primary airflow  
- **Stator Vanes** — Fixed vanes straightening the exit flow for improved efficiency  
- **Nacelle Duct** — Internal annular duct shaping the inlet/outlet flow and reducing losses  
- **Spinner** — Nose cone that reduces inlet turbulence and drag  

---

## 4. Contents of This Subsystem Folder

This folder should contain:

- **Aerodynamic design specifications**  
  Blade geometry, twist distribution, CFD summaries

- **Rotor/stator blade geometry**  
  Non-binary CAD sources (SVG, STEP if needed), coordinate tables

- **Nacelle integration drawings**  
  Internal duct profile, clearances, mounting points

- **Performance maps**  
  - Thrust vs. flight speed  
  - Efficiency vs. RPM  
  - Pressure ratio curves  
  Stored in `61-90_Tables_Schemas_Diagrams` as CSV/YAML/SVG

- **Acoustic characteristics**  
  Noise spectra, harmonics, tonal components, mitigation strategies

---

## 5. Interfaces

### 5.1 Internal Subsystem Interfaces

- **61-20-01_Electric_Motor**  
  - *Type:* Mechanical  
  - *Description:* Shaft and torque transfer + rotational speed interface.

- **61-20-03_Blade_System**  
  - *Type:* Mechanical / Design  
  - *Description:* Blade geometry libraries, materials, manufacturability rules.

- **61-50_Structures**  
  - *Type:* Structural  
  - *Description:* Nacelle frame, mounts, vibration paths, loads and stiffness constraints.

### 5.2 Cross-ATA Interfaces

- **ATA 71 – Power Plant**  
  - Propulsion group integration, installation standards, and nacelle-level certification hooks.

- **ATA 72 – Engine / Propulsion System**  
  - Integration of ducted fan aerodynamic output within the global propulsion chain.

- **ATA 57 – Wings / Nacelle Integration**  
  - Structural mounting (if applicable to wing station). *(Referenced but documented under ATA 57.)*

---

## 6. Status

- **Subsystem ID:** 61-20-02  
- **Lifecycle State:** Active / In Definition & Early Engineering  
- **Safety Criticality:** To be defined in `61-00-02_Safety`  
- **Linked Requirements:** To be defined in `61-00-03_Requirements` (REQ-61-20-02-XXX)

---

## 7. Document Control

- **Standard:** OPT-IN Framework v1.2  
- **Owner:** AMPEL360 Propulsion Team  
- **Generation:** Produced with AI assistance under deterministic, version-controlled prompts (GitHub Copilot / ChatGPT API).  
- **Approval:** Pending human review and configuration management per `61-00-11_EIS_Versions_Tags` and CC/CM rules.

---

*This folder is part of the `61-20_Subsystems` bucket under ATA 61 — Propellers/Propulsors.*
