# 61-20-05_Cooling_Loop — ATA 61 Subsystem

| Field              | Value                                  |
|--------------------|----------------------------------------|
| **Subsystem ID**   | 61-20-05_Cooling_Loop                  |
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

The **Cooling Loop** subsystem defines the thermal management architecture for the EDF (Electric Ducted Fan) propulsors.  
It manages heat dissipation from the high-power electric motors and power electronics through dedicated cooling circuits and, where applicable, interfaces to cryogenic systems.

---

## 2. Scope

This subsystem covers the **design, integration, and operation** of cooling systems serving propulsor components, including:

- Motor stator/rotor and bearing cooling
- PCU / power electronics thermal management
- Heat exchanger and pump selection and sizing
- Interfaces to aircraft thermal and cryogenic systems
- Thermal monitoring and control logic (hardware side)

Out of scope:

- Detailed motor design (see `61-20-01_Electric_Motor`)
- Detailed PCU electronics design (see `61-20-04_Propulsor_Control_Unit`)
- Global environmental control system architecture (ATA 21)
- Global hydrogen system architecture (ATA 28)

---

## 3. Cooling Configurations

The cooling loop may include one or more of the following configurations:

- **Liquid Cooling**  
  - Glycol–water or dielectric fluid loops  
  - Closed-loop circuits with pumps and heat exchangers

- **Oil Cooling**  
  - Motor bearing and winding cooling via oil circulation  
  - Oil-to-liquid or oil-to-air heat exchangers

- **Cryogenic Interface**  
  - LH₂ cold sink utilization for enhanced cooling (optional)  
  - Interface to hydrogen fuel system (ATA 28) for cold energy recovery

- **Air Cooling**  
  - Ram air for heat exchangers  
  - Nacelle-integrated air scoops and ducting

---

## 4. Contents of This Subsystem Folder

This folder should contain:

- **Cooling system architecture and schematics**  
  P&ID diagrams, block diagrams, and functional descriptions

- **Heat exchanger specifications**  
  Type, capacity, materials, and integration requirements

- **Pump and flow control specifications**  
  Pump types, flow rates, pressure heads, and control logic

- **Thermal analysis and simulation results**  
  CFD, lumped-parameter models, and transient thermal analyses

- **Interface definitions to cryogenic systems**  
  Coordination with ATA 28 for LH₂ cold sink utilization

---

## 5. Interfaces

### 5.1 Internal Subsystem Interfaces

- **61-20-01_Electric_Motor**  
  - *Type:* Thermal / Fluid  
  - *Description:* Primary heat source; coolant supply and return.

- **61-20-04_Propulsor_Control_Unit**  
  - *Type:* Thermal / Fluid  
  - *Description:* PCU cooling requirements and thermal interface.

- **61-80_Energy**  
  - *Type:* Thermal / Energy  
  - *Description:* Thermal energy exchange with aircraft energy systems.

### 5.2 Cross-ATA Interfaces

- **ATA 21 – Air Conditioning**  
  - Potential heat sink for propulsor cooling loops.

- **ATA 28 – Fuel System**  
  - Cryogenic interface for LH₂ cold energy recovery.

---

## 6. Status

- **Subsystem ID:** 61-20-05  
- **Lifecycle State:** Active / In Definition & Early Engineering  
- **Safety Criticality:** To be defined in `61-00-02_Safety`  
- **Linked Requirements:** To be defined in `61-00-03_Requirements` (REQ-61-20-05-XXX)

---

## 7. Document Control

- **Standard:** OPT-IN Framework v1.2  
- **Owner:** AMPEL360 Propulsion Team  
- **Generation:** Produced with AI assistance under deterministic, version-controlled prompts (GitHub Copilot / ChatGPT API).  
- **Approval:** Pending human review and configuration management per `61-00-11_EIS_Versions_Tags` and CC/CM rules.

---

*This folder is part of the `61-20_Subsystems` bucket under ATA 61 — Propellers/Propulsors.*
