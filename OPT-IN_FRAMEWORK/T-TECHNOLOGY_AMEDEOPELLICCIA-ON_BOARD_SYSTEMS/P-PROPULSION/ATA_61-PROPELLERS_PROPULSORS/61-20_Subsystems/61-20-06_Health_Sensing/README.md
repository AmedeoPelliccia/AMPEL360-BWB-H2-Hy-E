# 61-20-06_Health_Sensing — ATA 61 Subsystem

| Field              | Value                                  |
|--------------------|----------------------------------------|
| **Subsystem ID**   | 61-20-06_Health_Sensing                |
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

The **Health Sensing** subsystem provides real-time monitoring of EDF (Electric Ducted Fan) propulsor health using vibration, strain, temperature, and electromagnetic sensors.

It enables **condition monitoring, predictive maintenance, and fault detection** for the AMPEL360 Q100 propulsion system.

---

## 2. Scope

This subsystem covers the **sensing hardware and data acquisition chain** used to monitor:

- Electric motor health
- Ducted fan rotor/stator and blade health
- Structural loads in the nacelle and mounts
- Thermal states of motors, bearings, and cooling circuits
- Electromagnetic signatures indicative of motor or PCU degradation

Out of scope:

- Core control loops of the PCU (see `61-20-04_Propulsor_Control_Unit`)
- Global diagnostic algorithms and ML models (primarily documented under `61-40_Software` and ATA 95)
- Central maintenance server implementation (ATA 45)

---

## 3. Sensor Types

- **Vibration Sensors**  
  Accelerometers placed on motor housings, nacelle structures, and selected structural points to detect rotor imbalance, bearing wear, and structural anomalies.

- **Strain Gauges**  
  Gauges on blades and structural members to monitor loads, fatigue accumulation, and compare against design limits.

- **Temperature Sensors**  
  Thermocouples or RTDs monitoring motor windings, bearings, cooling fluid inlet/outlet, and nacelle skin temperatures.

- **EM Sensors**  
  Electromagnetic field monitoring (e.g. current signature analysis, flux sensors) for early detection of motor or PCU degradation.

---

## 4. Contents of This Subsystem Folder

This folder should contain:

- **Sensor specifications and selection criteria**  
  Types, ranges, accuracy, environmental ratings

- **Sensor placement diagrams**  
  Locations on motor, fan, nacelle, and structural members

- **Data acquisition architecture**  
  Signal conditioning, sampling rates, data buses, and interfaces to PCU and aircraft systems

- **Health monitoring algorithms**  
  (See also `61-40_Software`) Thresholds, trending, anomaly detection, and fault isolation logic

- **Predictive maintenance integration**  
  Data flow to ATA 45 / ATA 95 for maintenance planning and Digital Product Passport logging

---

## 5. Interfaces

### 5.1 Internal Subsystem Interfaces

- **61-20-01_Electric_Motor**  
  - *Type:* Electrical / Data  
  - *Description:* Motor health sensing; temperature, vibration, and EM signals.

- **61-20-02_Ducted_Fan**  
  - *Type:* Mechanical / Data  
  - *Description:* Fan vibration and blade health monitoring.

- **61-20-04_Propulsor_Control_Unit**  
  - *Type:* Electrical / Data  
  - *Description:* Sensor data interface; fault reporting to PCU.

- **61-40_Software**  
  - *Type:* Logical / Data  
  - *Description:* Health monitoring and ML diagnostics algorithms.

### 5.2 Cross-ATA Interfaces

- **ATA 45 – Central Maintenance System**  
  - Integration for maintenance alerts, fault logging, and work package generation.

- **ATA 95 – Digital Product Passport**  
  - Data logging for component lifecycle tracking and circularity metrics.

---

## 6. Status

- **Subsystem ID:** 61-20-06  
- **Lifecycle State:** Active / In Definition & Early Engineering  
- **Safety Criticality:** To be defined in `61-00-02_Safety`  
- **Linked Requirements:** To be defined in `61-00-03_Requirements` (REQ-61-20-06-XXX)

---

## 7. Document Control

- **Standard:** OPT-IN Framework v1.2  
- **Owner:** AMPEL360 Propulsion Team  
- **Generation:** Produced with AI assistance under deterministic, version-controlled prompts (GitHub Copilot / ChatGPT API).  
- **Approval:** Pending human review and configuration management per `61-00-11_EIS_Versions_Tags` and CC/CM rules.

---

*This folder is part of the `61-20_Subsystems` bucket under ATA 61 — Propellers/Propulsors.*
