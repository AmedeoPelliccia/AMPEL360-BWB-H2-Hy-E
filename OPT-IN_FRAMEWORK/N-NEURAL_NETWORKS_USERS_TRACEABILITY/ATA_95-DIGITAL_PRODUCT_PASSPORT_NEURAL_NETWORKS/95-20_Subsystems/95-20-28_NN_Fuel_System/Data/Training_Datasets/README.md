# 95-20-28 — Fuel System NN Training Datasets

This folder contains the **primary training datasets** for the neural network
functions under **95-20-28 NN Fuel System**, supporting ATA 28.

Typical NN functions include:

- Fuel quantity estimation and cross-checking
- Leak / abnormal consumption detection
- Fuel transfer optimization and balancing
- Fuel temperature prediction and conditioning

> **Note:** Synthetic / digital-twin scenarios are stored under  
> `Data/Synthetic_Data/` and referenced separately in model configs and V&V docs.

---

## 1. Dataset Inventory

| ID                        | File Name                                            | Purpose                              | Used By (Examples)                               |
|---------------------------|------------------------------------------------------|--------------------------------------|--------------------------------------------------|
| 95-20-28-601              | `95-20-28-601_Fuel_Quantity_Sensor_Logs.parquet`    | Fuel quantity estimation / cross-checking | 95-20-28-A-101 Fuel Quantity Estimator     |
| 95-20-28-602              | `95-20-28-602_Fuel_Transfer_Events.parquet`         | Fuel transfer planning & optimization     | 95-20-28-A-103 Fuel Transfer Optimizer      |
| 95-20-28-603 (optional)   | `95-20-28-603_Fuel_Temp_And_Conditions.parquet`     | Fuel temperature prediction & conditioning | 95-20-28-A-104 Fuel Temperature Predictor |
| 95-20-28-604 (optional)   | `95-20-28-604_Fuel_Leaks_And_AbnormalUsage.parquet` | Leak / abnormal consumption detection     | 95-20-28-A-102 Leak Detection Monitor      |

Adjust / prune the list above according to the datasets you actually commit.

---

## 2. Expected Schema (Examples)

### 2.1 95-20-28-601 — Fuel Quantity Sensor Logs

Typical columns:

- `flight_id`
- `timestamp`
- `tank_id`  
- `fuel_quantity_kg`
- `fuel_quantity_raw_units` (if applicable)
- `pitch_deg`, `roll_deg`, `yaw_deg`
- `altitude_ft`
- `mach`
- `engine_thrust_mode`
- `sensor_status` (OK / DEGRADED / FAIL)
- `label_true_quantity_kg` (if ground-truth available from calibration / refuelling)

Used primarily for:

- Training and validating **Fuel Quantity Estimator** NNs  
- Calibrating against ground-truth measurements and reference instruments.

---

### 2.2 95-20-28-602 — Fuel Transfer Events

Typical columns:

- `flight_id`
- `event_id`
- `timestamp`
- `source_tank_id`
- `destination_tank_id`
- `commanded_transfer_rate_kg_per_min`
- `actual_transfer_rate_kg_per_min`
- `delta_quantity_source_kg`
- `delta_quantity_dest_kg`
- `valve_state` (OPEN / CLOSED / FAILED)
- `transfer_result` (SUCCESS / PARTIAL / FAIL)
- `imbalance_before_kg` / `imbalance_after_kg`
- `label_optimality_score` (0–1) or discrete class

Used for:

- Training **Fuel Transfer Optimizer** NNs  
- Evaluating balancing strategies and failure behaviours.

---

## 3. Usage in Model Configs

Each NN training config in `Models/Configs/` should reference these datasets
explicitly. Example:

```yaml
data:
  dataset_id: "95-20-28-601_Fuel_Quantity_Sensor_Logs"
  train_path: "Data/Training_Dataset/95-20-28-601_Fuel_Quantity_Sensor_Logs.parquet"
  format: "parquet"
  val_split: 0.1
  test_split: 0.1
  shuffle: true
````

Synthetic / digital-twin datasets are referenced separately as:

```yaml
synthetic_scenarios:
  - id: "95-20-28-605_Digital_Twin_Fuel_Scenarios"
    path: "Data/Synthetic_Data/95-20-28-605_Digital_Twin_Fuel_Scenarios.parquet"
    usage:
      - "robustness_testing"
      - "edge_case_evaluation"
```

---

## 4. Data Governance & Traceability

* **Owner:** AMPEL360 ML Engineering Team
* **Primary ATA Chapters:** ATA 28 Fuel System, ATA 95 Neural Networks
* **Linkage:**

  * Fuel NN specs under `95-20-28-0XX_*.md`
  * Model cards under `ASSETS/Model_Cards/95-20-28-A-1XX_*.yaml`
  * Safety & certification under `95-20-28-008_Safety_and_Certification.md`

Each dataset should have:

* A clear **provenance description** (source: flight test, rig, digital twin, etc.)
* Versioning / regeneration strategy (if synthetic / simulated)
* Hash and size recorded in the relevant model cards and/or DPP entries.

---

## 5. AI Assistance & Document Control

This README has been drafted with AI assistance (GitHub Copilot / ChatGPT),
**prompted by Amedeo Pelliccia**, and is subject to human review and formal
approval under the AMPEL360 document control process.

```

