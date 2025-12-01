# 61-20-01_Electric_Motor — ATA 61 Subsystem

| Field              | Value                                  |
|--------------------|----------------------------------------|
| **Subsystem ID**   | 61-20-01_Electric_Motor                |
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

The **Electric Motor** subsystem defines the high-power electric machine used in each EDF (Electric Ducted Fan) propulsor of the AMPEL360 Q100 distributed propulsion system.

Each propulsor integrates a **4 MW electric motor** that converts electrical power into mechanical shaft power to drive the ducted fan.

---

## 2. Scope

This subsystem covers the **design, specification, integration, and lifecycle management** of the high-power electric motors used in the AMPEL360 Q100 distributed propulsion architecture, including:

- Motor electromagnetic and mechanical design
- Integration with the ducted fan and nacelle structures
- Electrical power and control interfaces
- Thermal management interfaces
- Reliability, maintainability, and certification aspects

Out of scope:

- Central energy generation (fuel cells, batteries – see ATA 24/ATA 80/ATA 28/ATA 49 as applicable)
- Global propulsion control laws (ATA 22 / ATA 40 / ATA 42)
- Wing/nacelle structural integration (ATA 57 / ATA 53)

---

## 3. Key Specifications

- **Power Rating:** 4 MW per motor (continuous nominal)
- **Quantity:** 4 motors total (4 × 4 MW EDF propulsors)
- **Configuration:** Direct-drive or high-stiffness coupling to ducted fan
- **Nominal Operating Regime:** High-torque, mid-RPM range (details in engineering models)
- **Cooling Interface:** Connected to `61-20-05_Cooling_Loop`
- **Health Monitoring:** Integrated temperature, vibration, and electrical signature sensors
- **Redundancy / Safety:** To be defined in Safety (61-00-02) and Engineering (61-00-06)

---

## 4. Contents of This Subsystem Folder

This folder should contain, at minimum:

- **Motor design specifications**  
  - Electromagnetic design data, mechanical envelope, materials
- **Performance characteristics**  
  - Torque–speed curves, efficiency maps, power-factor data
- **Electrical interface requirements**  
  - Voltage, current, frequency ranges; connector and harness specifications
- **Thermal management requirements**  
  - Heat rejection, coolant flow rates, allowable temperature ranges
- **Reliability and maintenance data**  
  - MTBF/MTBUR assumptions, inspection tasks, condition-based triggers
- **Certification evidence for motor systems**  
  - Test reports, analyses, MoC mapping (linked to 61-00-10_Certification)
- **Links to models and tables**  
  - References into `61-90_Tables_Schemas_Diagrams` for curves, schemas and SDS

---

## 5. Interfaces

### 5.1 Internal Subsystem Interfaces

- **61-20-02_Ducted_Fan**  
  - *Type:* Mechanical  
  - *Description:* Shaft/coupling interface between motor and fan; torque, speed, and vibration transfer.

- **61-20-04_Propulsor_Control_Unit (PCU)**  
  - *Type:* Electrical / Logical  
  - *Description:* Control commands, feedback signals, limits, and fault reporting between motor and PCU.

- **61-20-05_Cooling_Loop**  
  - *Type:* Thermal / Fluid  
  - *Description:* Coolant supply and return, temperature sensors, and allowable pressure/flow envelopes.

### 5.2 Cross-ATA Interfaces

- **ATA 24 – Electrical Power**  
  - Supply of electrical power (voltage, current, quality) to the motor drive chain.

- **ATA 72 – Engine / Propulsion Integration**  
  - Integration of the Electric Motor + EDF assembly into the overall propulsion system functional chain.

- **ATA 80 / ATA 28 / ATA 49 (as mapped by programme)**  
  - Upstream energy provisioning (fuel cells, batteries, auxiliary power, hydrogen systems), referenced but not owned here.

---

## 6. Status

- **Subsystem ID:** 61-20-01  
- **Lifecycle State:** Active / In Definition & Early Engineering  
- **Safety Criticality:** To be defined in 61-00-02_Safety  
- **Linked Requirements:** To be defined in 61-00-03_Requirements (REQ-61-20-01-XXX)

---

## 7. Document Control

- **Standard:** OPT-IN Framework v1.2  
- **Owner:** AMPEL360 Propulsion Team  
- **Generation:** Content may be partially generated with AI assistance (e.g. GitHub Copilot, ChatGPT API) under deterministic, version-controlled prompts.  
- **Approval:** Subject to human engineering review and configuration management, per chapter 61-00-11 and programme CC/CM rules.
