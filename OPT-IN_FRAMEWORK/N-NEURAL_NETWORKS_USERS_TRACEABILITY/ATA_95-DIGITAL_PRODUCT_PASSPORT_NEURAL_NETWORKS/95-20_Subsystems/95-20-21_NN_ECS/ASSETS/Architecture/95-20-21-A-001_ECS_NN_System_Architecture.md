
# 95-20-21-A-001 — ECS Neural Networks System Architecture  
**Subsystem**: 95-20-21 – Environmental Control System (ECS) Neural Networks  
**Document Type**: System Architecture (ARCH)  
**Status**: WORKING  
**Version**: 1.0  
**Last Updated**: 2025-11-18  

---

## 1. Overview

This document defines the **system-level architecture** of the Neural Networks supporting the **Environmental Control System (ECS)** within the AMPEL360 BWB H₂ Hy-E aircraft.  
It provides interfaces, data flows, safety boundaries, IMA allocations, and integration with ATA 21.

The ECS NN suite includes:

| Model ID | Component | Version |
|---------|-----------|---------|
| 95-20-21-A-101 | Cabin Temperature Predictor | v1.2 |
| 95-20-21-A-102 | Air Quality Monitor | v1.0 |
| 95-20-21-A-103 | HVAC Optimizer | v2.1 |
| 95-20-21-A-104 | Pressure Control NN | v1.3 |
| 95-20-21-A-105 | Humidity Management NN | v1.1 |
| 95-20-21-A-106 | CO₂ Scrubbing Optimizer | v1.0 |

These networks collectively support predictive, adaptive, and energy-efficient ECS control.

---

## 2. High-Level Architecture (Mermaid Diagram)

```mermaid
flowchart LR
    %% ECS Neural Network System Architecture

    subgraph ATA21["ATA 21 – Environmental Control System"]
        TEMP["Temperature Sensors\n(6 zones, 10 Hz)"]
        AIRQ["Air Quality Sensors\n(CO₂, VOC, PM2.5, Humidity, 5 Hz)"]
        PRESS["Cabin Pressure Sensors\n(5 Hz)"]
        HUM["Humidity Sensors\n(5 Hz)"]
        FLOW["Airflow Sensors\n(10 Hz)"]
        ACT["ECS Actuators\n(Valves, Fans, Packs)"]
    end

    subgraph IMA["IMA Platform\n(ARINC 653 Partition\n95-20-21 ECS-NN)"]
        TEMP_PRED["Cabin Temp Predictor\n95-20-21-A-101"]
        AIR_MON["Air Quality Monitor\n95-20-21-A-102"]
        HVAC_OPT["HVAC Optimizer\n95-20-21-A-103"]
        PRESS_CTL["Pressure Control NN\n95-20-21-A-104"]
        HUM_CTL["Humidity Controller NN\n95-20-21-A-105"]
        CO2_OPT["CO₂ Scrubbing Optimizer\n95-20-21-A-106"]
    end

    subgraph MON["Safety / Monitoring Layer"]
        VVM["V&V Runtime Monitors\n(Range checks, drift detection)"]
        FAIL["Fallback Logic\n(Classical ECS Control Laws)"]
    end

    %% Sensor flows to models
    TEMP --> TEMP_PRED
    AIRQ --> AIR_MON
    PRESS --> PRESS_CTL
    HUM --> HUM_CTL
    FLOW --> HVAC_OPT
    AIRQ --> CO2_OPT

    %% Outputs to ATA 21 actuator layer
    TEMP_PRED --> HVAC_OPT
    AIR_MON --> HVAC_OPT
    HUM_CTL --> HVAC_OPT
    CO2_OPT --> HVAC_OPT

    HVAC_OPT --> ACT

    %% Safety monitoring
    TEMP_PRED -.-> VVM
    AIR_MON -.-> VVM
    PRESS_CTL -.-> VVM
    HUM_CTL -.-> VVM
    CO2_OPT -.-> VVM

    VVM -. violation .-> FAIL
    FAIL --> ACT
````

---

## 3. Functional Decomposition

### 3.1. Temperature Management

* Predicts 5-minute cabin temperature profile (6 zones).
* Provides anticipatory input to HVAC optimizer.

### 3.2. Air Quality Management

* Monitors CO₂, PM2.5, VOC, humidity.
* Flags anomalies and triggers ventilation / scrubbing logic.

### 3.3. Pressure Control

* Predicts pressure trends influenced by altitude / sealed volume.
* Supports smoother transitions and energy savings.

### 3.4. Humidity Management

* Predicts humidity drift based on load factor + ECS cycle.
* Helps reduce condensation and improve comfort.

### 3.5. CO₂ Scrubbing Optimization

* Determines optimal scrubber cycle timing and intensity.
* Reduces energy draw.

---

## 4. Data Interfaces

### 4.1. Inputs

| Source               | Type       | Rate   |
| -------------------- | ---------- | ------ |
| Temp sensors         | float32[6] | 10 Hz  |
| Air quality sensors  | float32[5] | 5 Hz   |
| Pressure sensors     | float32    | 5 Hz   |
| Humidity             | float32    | 5 Hz   |
| Airflow              | float32    | 10 Hz  |
| FMS flight phase     | enum       | 0.5 Hz |
| Passenger load       | int16      | 0.1 Hz |
| External temperature | float32    | 1 Hz   |

### 4.2. Outputs

| Component              | Output                                  |
| ---------------------- | --------------------------------------- |
| Temp Predictor         | 6-zone temp forecast                    |
| Air Quality Monitor    | AQI 1-5, CO₂ estimate, contaminant flag |
| Pressure NN            | Predicted cabin pressure                |
| Humidity NN            | Target humidity band                    |
| CO₂ Scrubber Optimizer | Scrubbing duty cycle                    |
| HVAC Optimizer         | Final actuator commands                 |

---

## 5. IMA Partition Allocation (ARINC 653)

| Partition            | Role                                               | Resources                       |
| -------------------- | -------------------------------------------------- | ------------------------------- |
| 95-20-21 ECS-NN      | Inference, pre-processing, consistency checks      | 1 CPU core, 200 MB RAM          |
| 95-20-99 NN-Support  | Shared NN utilities (quantization, explainability) | 0.3 CPU core                    |
| 21-30-00 ECS Control | Safety fallback system                             | 1 CPU core, highest criticality |

---

## 6. Safety Boundaries

### Safety Measures (per EASA SC-AI + DO-178C):

* **DAL C** components with runtime monitoring.
* Fallback to **deterministic classical ECS controllers**.
* Health checks: NAN/INF detection, range checks, inference timeout.
* Cross-NN sanity checks (e.g., pressure vs altitude).
* Drift monitoring (input & output).

---

## 7. Digital Product Passport (ATA 95)

Each model includes:

* Model card (ASSETS/Model_Cards/)
* ONNX artifact
* SHA-256 provenance hash
* Training dataset lineage
* Certification evidence mapping
* Synthetic data generation flows

---

## 8. Files in This Directory

| File                                             | Description                            |
| ------------------------------------------------ | -------------------------------------- |
| **95-20-21-A-001_ECS_NN_System_Architecture.md** | Main architecture document (this file) |
| `ECS_NN_Architecture_Diagram.pdf`                | To be created (graphical architecture) |
| `ECS_Data_Flow.mmd`                              | Mermaid source for diagrams            |
| `ECS_Interfaces.yaml`                            | Machine-readable interface definitions |

---

## 9. Document Control

* **Version**: 1.0
* **Status**: WORKING
* **Author**: AMPEL360 ECS Neural Systems Team
* **AI Assistance**:

  * GitHub Copilot
  * ChatGPT (prompted by **Amedeo Pelliccia**)
* **Requires Approval By**: Chief Engineer – AI Systems

---


