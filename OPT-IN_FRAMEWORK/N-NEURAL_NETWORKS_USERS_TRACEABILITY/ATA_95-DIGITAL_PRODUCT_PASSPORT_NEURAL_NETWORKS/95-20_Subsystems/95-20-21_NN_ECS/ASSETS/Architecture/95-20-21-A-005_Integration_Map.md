
# 95-20-21-A-005 — ECS NN Integration Map

**Subsystem**: 95-20-21 NN ECS (Environmental Control System Neural Networks)  
**ATA Chapters**: ATA 21 (Air Conditioning) · ATA 95 (Neural Networks)  
**Status**: WORKING  

---

## 1. Purpose and Scope

This document provides a **system-level integration map** of the ECS Neural Network
subsystem (95-20-21 NN ECS) with:

- ATA 21 – Environmental Control System (sensors, actuators, controller)  
- Other NN subsystems under **95-20-XX** (e.g. Flight Controls, Fuel System, Recording)  
- Monitoring, recording and maintenance systems (ATA 31 / ATA 45)  
- The **ATA 95 Digital Product Passport (DPP)** and certification / V&V artefacts  

It complements:

- `95-20-21-A-001_ECS_NN_System_Architecture.md` (internal ECS NN structure)  
- `95-20-21-A-003_ECS_NN_Data_Flow_Diagram.md` (detailed data flows)  

---

## 2. High-Level Integration Map (Mermaid)

```mermaid
flowchart TB
    %% 95-20-21 ECS NN – Integration Map

    subgraph ATA21["ATA 21 – Environmental Control System"]
        A21_SENS["Sensors\nT, RH, CO₂, VOC, PM, P, Airflow"]
        A21_CTRL["Classical ECS Controller"]
        A21_ACT["Actuators\nValves, Packs, Fans, Scrubbers"]
    end

    subgraph NN_ECS["95-20-21 NN ECS"]
        A101["A-101\nCabin Temp Predictor"]
        A102["A-102\nAir Quality Monitor"]
        A103["A-103\nHVAC Optimizer"]
        A105["A-105\nHumidity Management"]
        A107["A-107\nCO₂ Scrubbing Optimizer"]
    end

    subgraph NN_FC["95-20-27 NN Flight Controls"]
        A27_FC["95-20-27\nFlight Control NNs\n(loads, envelopes, profiles)"]
    end

    subgraph NN_FUEL["95-20-28 NN Fuel System"]
        A28_FUEL["95-20-28\nFuel NNs\n(mission state, energy mgmt)"]
    end

    subgraph NN_REC["95-20-31 NN Recording Systems"]
        A31_REC["95-20-31\nRecording NNs\n(CVR/FDR, ECS traces)"]
    end

    subgraph MON["ATA 31 / 45 – Monitoring & Maintenance"]
        A31_LOG["Recording & Trend Monitoring"]
        A45_CMS["Central Maintenance\nFaults & Messages"]
    end

    subgraph DPP["ATA 95 – Digital Product Passport"]
        DPP_ECS["DPP Entries\nECS NN Models & Hashes"]
    end

    %% Primary integration: ATA 21 <-> NN ECS
    A21_SENS -->|"Telemetry\n(time series)"| NN_ECS
    A101 -->|"Forecasted T(zones)"| A103
    A102 -->|"AQI + alerts"| A103
    A105 -->|"RH targets/trends"| A103
    A107 -->|"Scrubber duty recs"| A103
    A103 -->|"Optimized setpoints\n(advisory, bounded)"| A21_CTRL
    A21_CTRL --> A21_ACT

    %% Cross-ATA NN integrations
    A27_FC -->|"Flight phase,\nload & envelope context"| NN_ECS
    A28_FUEL -->|"Mission state,\nenergy budget info"| NN_ECS

    %% Monitoring & recording
    NN_ECS -->|"Predictions · Alerts · Setpoints"| A31_LOG
    A21_CTRL -->|"Commands & modes"| A31_LOG
    A31_LOG --> A45_CMS

    %% DPP integration
    NN_ECS -->|"Model cards · ONNX hashes\nV&V evidence refs"| DPP_ECS
    DPP_ECS -->|"Traceability links"| A31_LOG
````

---

## 3. Integration Points (By Domain)

### 3.1 ATA 21 – ECS

| Direction         | From                 | To                    | Type                         | Notes                              |
| ----------------- | -------------------- | --------------------- | ---------------------------- | ---------------------------------- |
| Input to NN ECS   | ATA 21 sensors       | 95-20-21 NN ECS       | Telemetry (T, RH, CO₂, etc.) | Main feature inputs, 5–10 Hz       |
| Advisory to ECS   | A-103 HVAC Optimizer | ECS Controller        | Setpoints, power bands       | Bounded, subject to safety logic   |
| Monitoring & logs | ECS Controller       | ATA 31 / NN Recording | Commands, modes              | For trend analysis and diagnostics |

### 3.2 Other NN Subsystems (95-20-XX)

| Partner Subsystem             | Typical Exchange                                          | Purpose                                                                     |
| ----------------------------- | --------------------------------------------------------- | --------------------------------------------------------------------------- |
| 95-20-27 NN Flight Controls   | Flight phase, flight profile class, load / envelope flags | Context for ECS optimization (e.g. expected turbulence, phases)             |
| 95-20-28 NN Fuel System       | Mission state, energy budget, tank temps (if exposed)     | Coherent energy management between ECS loads and propulsion/fuel strategies |
| 95-20-31 NN Recording Systems | Recorded ECS NN inputs/outputs, health metrics            | Post-flight analysis, incident investigation, ML retraining data            |

---

## 4. Cross-Chapter Traceability (ATA 95 / DPP)

The following artefacts must reference each other to maintain **end-to-end traceability**:

* **Model Cards** (`ASSETS/Model_Cards/95-20-21-A-1XX_*.yaml`)

  * Fields `interfaces.inputs` and `interfaces.outputs` must:

    * Refer to ATA 21 signals by name and units.
    * Document any dependencies on 95-20-27, 95-20-28, 95-20-31 signals.

* **ONNX Artefacts** (`Models/Trained/*.onnx`)

  * Inspected by scripts like:

    * `Models/Scripts/inspect_onnx_model.py`
    * `Models/Scripts/test_onnx_model.py`
  * Hashes recorded in:

    * Model cards (`dpp_integration.model_hash`)
    * DPP entries (`ATA_95_NEURAL_NETWORKS/...`)

* **Recording & Monitoring** (`95-20-31_NN_Recording_Systems`)

  * Must be able to reconstruct:

    * Which ECS NN versions were active for a given flight.
    * What inputs, outputs and health status they had at key times.

* **Certification & Safety** (`95-20-21-009_Safety_and_Certification.md`)

  * Integration map should be referenced as:

    * The **authoritative source** of integration assumptions.
    * Basis for hazard analysis interfaces (e.g. ECS ↔ NNs ↔ Recording).

---

## 5. Integration Constraints and Rules

To keep the ECS NN subsystem **certification-aligned and governable**, the following integration rules apply:

1. **Advisory Role to ECS Controller**
   ECS NN components (especially A-103 HVAC Optimizer) provide **advisory setpoints**, not direct actuator commands. The classical ECS controller remains the **authoritative control function**.

2. **Bounded and Validated Outputs**
   All NN outputs that influence ECS behaviour must:

   * Respect pre-defined **safe envelopes and rate limits**.
   * Be discarded or downgraded if:

     * Confidence is low, or
     * Inputs are out-of-distribution / invalid.

3. **Deterministic Fallback**
   Loss of NN ECS partition, model failure or anomaly detection must trigger:

   * Fallback to pre-defined deterministic ECS modes and schedules.
   * Proper logging and fault signalling towards ATA 31 / ATA 45.

4. **Version Awareness in Recording Systems**
   95-20-31 NN Recording Systems must:

   * Record which **ECS NN versions (model_id, version)** are in use.
   * Associate events / anomalies with NN configurations (for later analysis or retraining).

5. **DPP as Single Pane of Glass**
   The ATA 95 DPP layer should be able to answer:

   * “Which ECS NN model was deployed on aircraft X at time Y?”
   * “Which external subsystems (95-20-27, 95-20-28, 95-20-31) did it depend on?”

---

## 6. Document Control

* **Document ID**: 95-20-21-A-005_ECS_NN_Integration_Map
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
  This document was drafted with AI assistance for integration mapping and diagram
  generation. Content is subject to human review, validation, and approval under the
  AMPEL360 document control process before being used for certification or regulatory
  submissions.

```

