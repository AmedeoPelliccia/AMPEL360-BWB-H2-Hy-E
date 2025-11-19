# 95-20-21-A-003 — ECS NN Data Flow Diagram

**Subsystem**: 95-20-21 NN ECS (Environmental Control System Neural Networks)  
**ATA Chapters**: ATA 21 (Air Conditioning) · ATA 95 (Neural Networks)  
**Status**: WORKING  

---

## 1. Purpose and Scope

This document provides a **data-flow–centric view** of the ECS NN subsystem:

- How **runtime data** flows from sensors to NN models and back to ECS actuators.  
- How **logging & monitoring** feeds ATA 31 / ATA 45.  
- How **offline training data** is generated and used (digital twin, synthetic scenarios, flight data).  

It complements:

- `95-20-21-A-001_ECS_NN_System_Architecture.md` (structural view)  
- Model cards in `ASSETS/Model_Cards/95-20-21-A-1XX_*.yaml`  
- Safety & certification view in `95-20-21-009_Safety_and_Certification.md`  

---

## 2. Runtime Data Flow (Onboard)

### 2.1 Logical Data Flow (Mermaid)

```mermaid
flowchart LR
    %% 95-20-21 ECS NN – Runtime Data Flow

    subgraph SENSORS["ATA 21 Sensors & Inputs"]
        TZONE["Cabin T per zone\n(°C, 10 Hz)"]
        AQ["Air Quality Sensors\nCO₂, VOC, PM, RH (5–10 Hz)"]
        PDATA["Pressure & Diff P\n(hPa, 1–10 Hz)"]
        AIRFLOW["Airflow Rates\n(m³/min, 10 Hz)"]
        EXT["External T & Env\n(°C, 1 Hz)"]
        LOAD["Passenger Load\n(0.1 Hz)"]
        PHASE["Flight Phase\n(enum, 0.5 Hz)"]
    end

    subgraph FE["Feature Engineering & Preprocessing\n(95-20-21 NN ECS Partition)"]
        FE_NODE["Normalization · Windowing\nOutlier Filtering · Encoding"]
    end

    subgraph NN_ECS["95-20-21 NN ECS Models"]
        TEMP_NN["A-101\nCabin Temp Predictor"]
        AQ_NN["A-102\nAir Quality Monitor"]
        HVAC_OPT["A-103\nHVAC Optimizer"]
        HUM_NN["A-105\nHumidity Management"]
        CO2_OPT["A-107\nCO₂ Scrubbing Optimizer"]
    end

    subgraph ECS["ATA 21 ECS Controller + Actuators"]
        ECSCTL["Classical ECS Controller\n(PID / Logic / Schedules)"]
        ACT["ECS Actuators\nValves · Packs · Fans · Scrubbers"]
    end

    subgraph MON["Monitoring & Recording\n(ATA 31 / 45)"]
        LOGS["ECS NN Logs\nPredictions · Alerts · Setpoints\nHealth & Status"]
        HFM["Health / Fault Mgmt"]
    end

    %% Sensor data to FE
    TZONE --> FE_NODE
    AQ --> FE_NODE
    PDATA --> FE_NODE
    AIRFLOW --> FE_NODE
    EXT --> FE_NODE
    LOAD --> FE_NODE
    PHASE --> FE_NODE

    %% FE to NNs
    FE_NODE --> TEMP_NN
    FE_NODE --> AQ_NN
    FE_NODE --> HUM_NN
    FE_NODE --> CO2_OPT

    %% Chained inputs into HVAC optimizer
    TEMP_NN -->|"Zone T forecast\n(5 min horizon)"| HVAC_OPT
    AQ_NN -->|"AQI + alerts"| HVAC_OPT
    HUM_NN -->|"RH trends / targets"| HVAC_OPT
    CO2_OPT -->|"Scrubber duty\nrecommendations"| HVAC_OPT

    %% Optimizer to ECS controller
    HVAC_OPT -->|"Optimized setpoints\n(advisory, bounded)"| ECSCTL
    ECSCTL -->|"Validated commands"| ACT

    %% Logging & monitoring
    TEMP_NN --> LOGS
    AQ_NN --> LOGS
    HVAC_OPT --> LOGS
    HUM_NN --> LOGS
    CO2_OPT --> LOGS
    ECSCTL --> LOGS

    LOGS --> HFM
````

### 2.2 Key Data Contracts

Main data contracts between blocks:

* **Sensors → Preprocessing**

  * Numeric time series with timestamps, units (°C, %RH, ppm, µg/m³, hPa, m³/min).
  * Quality flags (OK / DEGRADED / FAIL).

* **Preprocessing → NN Models**

  * Fixed-length sliding windows (e.g. `shape = [batch, timesteps, features]`).
  * Encoded categorical variables (flight phase, modes).

* **NN Models → ECS Controller**

  * Bounded, unit-consistent recommendations:

    * Temperature targets (°C) per zone
    * Humidity targets (%RH)
    * CO₂ scrubber duty cycle / mode
    * HVAC power bands (kW range)
  * Confidence / quality indicators AND anomaly flags, when available.

* **NN Models & ECS Controller → Monitoring**

  * Raw predictions / recommendations
  * Final commands applied
  * NN health status, inference latency, failure counters

---

## 3. Offline Training & Data Lifecycle

### 3.1 Training Data Flow (High-Level)

```mermaid
flowchart TB
    %% 95-20-21 ECS NN – Training Data Flow

    subgraph SRC["Data Sources"]
        FLT["Flight Test Data\n(Real ECS Telemetry)"]
        RIG["Ground Rigs / Iron Bird\nECS Test Benches"]
        DTWIN["Digital Twin & Synthetic\n95-20-21-605_Digital_Twin_ECS_Scenarios.parquet"]
    end

    subgraph RAW["Raw Ingestion\n(95-20-21 Data)"]
        RAW_ECS["Raw ECS Logs\n(time series, events)"]
    end

    subgraph CUR["Curation & Labeling"]
        CURATE["Cleaning · Alignment\nUnit Checks · Outlier Removal"]
        LABEL["Labeling & Annotation\nComfort, AQI, Events"]
    end

    subgraph DS["Training Datasets\n(Data/Training_Datasets)"]
        DS_TEMP["95-20-21-601\nCabin_Temp_10k_Flights.parquet"]
        DS_AQ["95-20-21-602\nAir_Quality_Logs.parquet"]
        DS_HUM["95-20-21-603\nHumidity_Profiles.parquet"]
        DS_CO2["95-20-21-604\nCO2_Scrubber_Logs.parquet"]
    end

    subgraph TRAIN["Model Training\n(Offline ML Pipeline)"]
        TRAIN_TEMP["Train A-101\nTemp Predictor"]
        TRAIN_AQ["Train A-102\nAir Quality Monitor"]
        TRAIN_HVAC["Train A-103\nHVAC Optimizer"]
    end

    subgraph ART["Model Artifacts\n(Models/Trained + DPP)"]
        ONNX_TEMP["temp_predictor_v1.2.onnx"]
        ONNX_AQ["air_quality_monitor_v1.0.onnx"]
        CARD["Model Cards\n95-20-21-A-1XX_*.yaml"]
        DPP["DPP Entries\n(hashes, lineage, evidence)"]
    end

    SRC --> RAW_ECS
    RAW_ECS --> CURATE
    CURATE --> LABEL
    LABEL --> DS_TEMP
    LABEL --> DS_AQ
    LABEL --> DS_HUM
    LABEL --> DS_CO2

    DS_TEMP --> TRAIN_TEMP
    DS_AQ --> TRAIN_AQ
    DS_TEMP --> TRAIN_HVAC
    DS_AQ --> TRAIN_HVAC
    DS_HUM --> TRAIN_HVAC
    DS_CO2 --> TRAIN_HVAC

    TRAIN_TEMP --> ONNX_TEMP
    TRAIN_AQ --> ONNX_AQ
    TRAIN_TEMP --> CARD
    TRAIN_AQ --> CARD
    TRAIN_HVAC --> CARD

    ONNX_TEMP --> DPP
    ONNX_AQ --> DPP
    CARD --> DPP
```

### 3.2 Traceability Hooks

Every step above should be traceable via:

* **Dataset IDs** (`95-20-21-60X_*`) in:

  * Model cards (`training.dataset.*`)
  * Training configs (`Models/Configs/*.yaml`)

* **Model artefact hashes** (e.g. SHA-256) stored in:

  * Inspection reports (e.g. `*_inspection_report.json`)
  * DPP fields (`dpp_integration.model_hash` in model cards)

* **Training runs**:

  * Logged in CI/CD or MLOps pipeline (run ID + git commit).

---

## 4. Safety, Boundaries, and Fallback (Data Perspective)

From a data perspective, the following safety measures apply:

* **Input validation & sanitization**:

  * Range checks, unit consistency, sensor status flags.
  * Drop or flag obviously corrupted samples before feeding NNs.

* **Output bounding and plausibility checks**:

  * NN outputs are checked against safe envelopes and rate-of-change limits.
  * Out-of-bounds or low-confidence recommendations are discarded and replaced by:

    * Classical ECS controller defaults
    * Safe fallback schedules.

* **Data isolation & privacy**:

  * ECS NN logs contain no PII; only technical telemetry.
  * Logs are stored and offloaded according to safety and certification requirements.

---

## 5. Document Control

* **Document ID**: 95-20-21-A-003_ECS_NN_Data_Flow_Diagram
* **Version**: 1.0
* **Status**: WORKING
* **Location**: `ASSETS/Architecture/` under `95-20-21_NN_ECS`
* **Last Updated**: 2025-11-19

**AI Assistance & Authorship**

* **AI Tools Used**:

  * GitHub Copilot
  * ChatGPT
* **Prompted by**: **Amedeo Pelliccia**
* **Note**:
  This document was drafted with AI assistance for data-flow mapping and diagram
  generation. Content is subject to human review, validation, and approval under the
  AMPEL360 document control process before being used for certification or regulatory
  submissions.

```


