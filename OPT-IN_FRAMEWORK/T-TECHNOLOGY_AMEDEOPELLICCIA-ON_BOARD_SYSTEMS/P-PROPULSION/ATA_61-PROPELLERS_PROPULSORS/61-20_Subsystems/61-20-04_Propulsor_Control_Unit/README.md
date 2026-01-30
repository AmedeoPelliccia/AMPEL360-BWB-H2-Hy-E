# 61-20-04_Propulsor_Control_Unit — ATA 61 Subsystem

| Field              | Value                                  |
|--------------------|----------------------------------------|
| **Subsystem ID**   | 61-20-04_Propulsor_Control_Unit        |
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

The **Propulsor Control Unit (PCU)** subsystem defines the power electronics and control hardware responsible for driving and protecting the electric motor of each EDF (Electric Ducted Fan) propulsor.

The PCU manages power delivery, motor speed/torque regulation, protection functions, and communication with aircraft-level control systems.

---

## 2. Scope

This subsystem covers the **hardware design, architecture, and integration** of the propulsor control electronics for the AMPEL360 Q100 EDF propulsion system, including:

- Power electronics for high-power motor drive (inverter / converter stages)
- Control and protection circuitry
- Signal conditioning for sensors and commands
- Communication interfaces with flight control and energy systems
- Environmental and EMC robustness

Out of scope:

- Detailed motor electromagnetic design (see `61-20-01_Electric_Motor`)
- High-level control laws and software (primarily owned under `61-40_Software`)
- Global propulsion management logic (ATA 22 / ATA 40 / ATA 42)

---

## 3. Key Functions

- **Power Control**  
  - Motor speed and torque regulation  
  - Modulation strategy (e.g. PWM / space-vector)  
  - Power ramping and derating logic

- **Protection**  
  - Overcurrent, overvoltage, undervoltage protection  
  - Thermal protection and derating  
  - Fault detection and isolation

- **Monitoring**  
  - Real-time motor parameter monitoring (current, voltage, temperature)  
  - Health status reporting to aircraft systems

- **Communication**  
  - Interface to aircraft flight control systems  
  - Data exchange with energy management and health monitoring systems

---

## 4. Contents of This Subsystem Folder

This folder should contain:

- **PCU hardware architecture specifications**  
  Block diagrams, functional descriptions, redundancy concepts

- **Power electronics design**  
  Inverter topology, switching devices, gate drivers, DC link design

- **Control and protection circuitry**  
  Signal conditioning, analog/digital interfaces, protection logic

- **EMI/EMC compliance documentation**  
  Test reports, design measures, compliance to [DO-160](https://www.rtca.org/content/standards-guidance-materials) Section 21/22

- **Environmental qualification**  
  [DO-160](https://www.rtca.org/content/standards-guidance-materials) environmental categories, test plans and results

---

## 5. Interfaces

### 5.1 Internal Subsystem Interfaces

- **61-20-01_Electric_Motor**  
  - *Type:* Electrical / Logical  
  - *Description:* Motor control signals, feedback, and fault reporting.

- **61-20-06_Health_Sensing**  
  - *Type:* Electrical / Data  
  - *Description:* Sensor inputs for motor and propulsor health monitoring.

- **61-40_Software**  
  - *Type:* Logical / Data  
  - *Description:* Control software executed by PCU; software/hardware interface specification.

### 5.2 Cross-ATA Interfaces

- **ATA 24 – Electrical Power**  
  - Supply of electrical power (DC bus) to the PCU.

- **ATA 76 – Engine Controls**  
  - Integration with aircraft-level engine control and thrust management.

---

## 6. Status

- **Subsystem ID:** 61-20-04  
- **Lifecycle State:** Active / In Definition & Early Engineering  
- **Safety Criticality:** To be defined in `61-00-02_Safety`  
- **Linked Requirements:** To be defined in `61-00-03_Requirements` (REQ-61-20-04-XXX)

---

## 7. Document Control

- **Standard:** OPT-IN Framework v1.2  
- **Owner:** AMPEL360 Propulsion Team  
- **Generation:** Produced with AI assistance under deterministic, version-controlled prompts (GitHub Copilot / ChatGPT API).  
- **Approval:** Pending human review and configuration management per `61-00-11_EIS_Versions_Tags` and CC/CM rules.

---

*This folder is part of the `61-20_Subsystems` bucket under ATA 61 — Propellers/Propulsors.*
