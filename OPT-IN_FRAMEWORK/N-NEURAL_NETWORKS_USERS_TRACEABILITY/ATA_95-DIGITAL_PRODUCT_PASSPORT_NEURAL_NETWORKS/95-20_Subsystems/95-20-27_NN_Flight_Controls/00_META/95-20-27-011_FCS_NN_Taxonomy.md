# 95-20-27-011 — FCS NN Taxonomy

**Document ID:** 95-20-27-011  
**Version:** 1.0  
**Date:** 2025-11-17  
**Status:** Active

---

## 1. Purpose

This document defines the taxonomy and classification scheme for the FCS_NN subsystem, providing a structured framework for organizing and referencing neural network models, components, and artifacts.

---

## 2. Subsystem Classification

### 2.1 ATA Chapter Mapping

```yaml
subsystem:
  id: "95-20-27"
  name: "NN_Flight_Controls"
  parent_ata: "ATA-27"
  parent_ata_name: "Flight Controls"
  cross_ata_dependencies:
    - "ATA-42": "Integrated Modular Avionics"
    - "ATA-53": "Fuselage / Structures"
    - "ATA-57": "Wings"
    - "ATA-70": "Propulsion"
  criticality: "DAL-A"
  safety_impact: "Catastrophic"
```

### 2.2 OPT-IN Framework Position

```
OPT-IN_FRAMEWORK/
└── N-NEURAL_NETWORKS_USERS_TRACEABILITY/
    └── ATA_95-DIGITAL_PRODUCT_PASSPORT_NEURAL_NETWORKS/
        └── 95-20_Subsystems/
            └── 95-20-27_NN_Flight_Controls/     ← This subsystem
```

---

## 3. Model Taxonomy

### 3.1 Model Classification Hierarchy

```
FCS_NN Models
├── Predictive Models
│   ├── Aerodynamic Predictor (PINN)
│   └── Gust Predictor (LSTM)
│
├── Control Models
│   ├── Control Surface Optimizer (PPO/RL)
│   ├── Flight Path Stabilization (MPC+NN)
│   └── Trim Optimizer (FNN+Online Learning)
│
└── Safety Models
    ├── Envelope Protection (Ensemble)
    └── Fault Detection & Isolation (Autoencoder)
```

### 3.2 Model Naming Convention

**Format**: `<Component>_<Type>_v<Major>.<Minor>.<Patch>`

**Examples**:
- `aero_predictor_v2.1.0`
- `control_surface_optimizer_v1.4.2`
- `gust_load_alleviation_v1.3.1`

**Version Semantics**:
- **Major**: Breaking changes, requires re-certification
- **Minor**: New features, backward compatible
- **Patch**: Bug fixes, performance improvements

---

## 4. Component Taxonomy

### 4.1 Component Types

| Type | Code | Description | Examples |
|------|------|-------------|----------|
| **Neural Network Model** | NN | Trained model for inference | Aero Predictor, Control Optimizer |
| **Data Pipeline** | DP | Data preprocessing and feature engineering | Sensor fusion, normalization |
| **Inference Engine** | IE | Runtime execution environment | ONNX Runtime, TensorRT |
| **Monitor** | MON | Health and performance monitoring | Latency tracker, anomaly detector |
| **Fallback Logic** | FB | Backup control laws | Conventional FCS, lookup tables |
| **Interface Adapter** | IA | Data translation and protocol conversion | ARINC 429 adapter, AFDX adapter |

### 4.2 Component Naming Convention

**Format**: `<Type>_<Function>_<Version>`

**Examples**:
- `NN_AeroPredictor_v2.1`
- `DP_SensorFusion_v1.0`
- `IE_ONNXRuntime_v1.12`
- `MON_LatencyTracker_v1.0`
- `FB_ConventionalFCS_v3.2`
- `IA_ARINC429Adapter_v1.1`

---

## 5. Asset Taxonomy

### 5.1 Asset Categories

```
ASSETS/
├── Architecture/           [ARCH]  System architecture diagrams and data flows
├── Model_Cards/           [MCARD] Model metadata and performance specifications
├── Performance_Data/      [PERF]  Benchmark results and performance metrics
├── Test_Data/             [TEST]  Validation and verification test results
├── Interface_Specs/       [IFACE] Interface definitions and protocols
└── Certification/         [CERT]  Certification evidence and compliance documents
```

### 5.2 Asset Naming Convention

**Format**: `95-20-27-A-<Category><Sequence>_<Description>_<Version>.<Extension>`

**Category Codes**:
- **0xx**: Architecture diagrams (00x: system, 01x: data flow, 02x: integration)
- **1xx**: Model Cards (101-199: one per model)
- **2xx**: Performance Data (201-299: various metrics)
- **3xx**: Test Data (301-399: various test types)
- **4xx**: Interface Specs (401-499: various interfaces)
- **5xx**: Certification (501-599: various evidence)

**Examples**:
- `95-20-27-A-001_FCS_NN_System_Architecture.drawio`
- `95-20-27-A-002_FCS_NN_System_Architecture.svg`
- `95-20-27-A-101_Aero_Predictor_v2.1.yaml`
- `95-20-27-A-201_Tracking_Performance_Results.xlsx`
- `95-20-27-A-301_Ground_Rig_Test_Results.csv`
- `95-20-27-A-401_ATA_27_FCS_Interface_Spec.yaml`
- `95-20-27-A-501_DO_178C_Evidence_Package.pdf`

---

## 6. Data Taxonomy

### 6.1 Data Categories

```
Data/
├── Training_Datasets/     [TRAIN]  Data used for model training
├── Validation_Datasets/   [VAL]    Data used for model validation
└── Synthetic_Data/        [SYN]    Simulated or generated data
```

### 6.2 Data Naming Convention

**Format**: `95-20-27-<Category><Sequence>_<Description>.<Extension>`

**Category Codes**:
- **6xx**: Data files (601-650: training, 651-680: validation, 681-699: synthetic)

**Examples**:
- `95-20-27-601_CFD_Aero_Surface_Coeffs.parquet`
- `95-20-27-602_Control_Law_Flight_Data.parquet`
- `95-20-27-603_Gust_and_Turbulence_FlightLogs.parquet`
- `95-20-27-604_FCS_Validation_Flights_2025.parquet`
- `95-20-27-605_Digital_Twin_FCS_Scenarios.parquet`

---

## 7. Test Taxonomy

### 7.1 Test Levels

```
Tests/
├── Unit_Tests/            [UT]    Individual component tests
├── Integration_Tests/     [IT]    Component interaction tests
└── HIL_Tests/             [HIL]   Hardware-in-the-loop system tests
```

### 7.2 Test Naming Convention

**Format**: `test_<ComponentUnderTest>_<TestType>.py`

**Examples**:
- `test_aero_predictor_accuracy.py`
- `test_control_surface_optimizer_latency.py`
- `test_gust_load_alleviation_robustness.py`
- `test_ata_27_fcs_loop_integration.py`
- `test_ata_42_partition_interface.py`

### 7.3 Test Scenario Files

**Format**: `95-20-27-<Sequence>_<Scenario>_<Type>.yaml`

**Examples**:
- `95-20-27-701_HIL_Test_Scenarios.yaml`
- `95-20-27-702_Edge_Case_Scenarios.yaml`
- `95-20-27-703_Failure_Mode_Scenarios.yaml`

---

## 8. Documentation Taxonomy

### 8.1 Document Types

| Type | Code | Description | Examples |
|------|------|-------------|----------|
| **Technical Specification** | SPEC | Detailed technical design | Component specs (001-010) |
| **Operations Manual** | OPS | Flight crew procedures | 95-20-27-801 |
| **Maintenance Manual** | MAINT | Maintenance procedures | 95-20-27-802 |
| **Troubleshooting Guide** | TRBL | Fault diagnosis | 95-20-27-803 |
| **Training Material** | TRAIN | Crew/tech training | Crew_Training_Guide.pdf |

### 8.2 Document Naming Convention

**Format**: `95-20-27-<Sequence>_<Title>.md` or `.pdf`

**Sequence Ranges**:
- **001-099**: Component technical specifications
- **800-899**: Operational and maintenance documentation

**Examples**:
- `95-20-27-001_FCS_NN_Overview.md`
- `95-20-27-801_FCS_NN_Operations_Manual.md`
- `95-20-27-802_FCS_NN_Maintenance_Procedures.md`
- `95-20-27-803_FCS_NN_Troubleshooting_Guide.md`

---

## 9. Code Taxonomy

### 9.1 Code Organization

```
Models/
├── Source/                 [SRC]   Source code for models
│   ├── <model_name>.py            Individual model implementations
│   └── training_scripts/          Training pipeline scripts
├── Trained/               [TRAIN]  Trained model artifacts
│   ├── <model_name>.onnx          ONNX format for deployment
│   └── checkpoints/               Training checkpoints
└── Configs/               [CFG]    Configuration files
    └── <config_name>.yaml         Training and deployment configs
```

### 9.2 Code File Naming Convention

**Source Code**: `<model_name>_v<version>.py`

**Examples**:
- `aero_predictor_v2.1.py`
- `control_surface_optimizer_v1.4.py`
- `gust_load_alleviation_v1.3.py`

**Trained Models**: `<model_name>_v<version>.onnx`

**Examples**:
- `aero_predictor_v2.1.onnx`
- `control_surface_optimizer_v1.4.onnx`

**Configs**: `<purpose>_config_<model>.yaml`

**Examples**:
- `training_config_aero.yaml`
- `deployment_config_fcs.yaml`

---

## 10. Interface Taxonomy

### 10.1 Interface Types

| Type | Code | Description |
|------|------|-------------|
| **Sensor Input** | SI | Data from aircraft sensors |
| **Control Output** | CO | Commands to actuators |
| **Inter-Model** | IM | Data exchange between NN models |
| **External System** | ES | Integration with ATA 27, 42, etc. |
| **Monitoring** | MON | Health and performance data |

### 10.2 Interface Naming Convention

**Format**: `<Type>_<Source>_to_<Destination>`

**Examples**:
- `SI_AirData_to_AeroPredictor`
- `CO_ControlOptimizer_to_FCC`
- `IM_AeroPredictor_to_ControlOptimizer`
- `ES_FCS_NN_to_ATA27`
- `MON_FCS_NN_to_EICAS`

---

## 11. Traceability Taxonomy

### 11.1 Requirement Types

| Type | Prefix | Description |
|------|--------|-------------|
| **Functional Requirement** | FR | What the system must do |
| **Non-Functional Requirement** | NFR | Quality attributes (performance, safety) |
| **Interface Requirement** | IR | Data exchange specifications |
| **Certification Requirement** | CR | Regulatory compliance |

### 11.2 Requirement Naming Convention

**Format**: `<Type>-FCS-<Sequence>`

**Examples**:
- `FR-FCS-001`: Real-time aerodynamic predictions <10ms
- `NFR-FCS-002`: Deterministic inference on IMA partition
- `IR-FCS-003`: ARINC 429 air data input
- `CR-FCS-004`: DO-178C Level A compliance

### 11.3 Traceability Matrix

**File**: `00_META/95-20-27-012_FCS_NN_Traceability_Map.csv`

**Columns**:
- Requirement ID
- Component ID
- Model ID
- Test Case ID(s)
- Verification Method
- Status

---

## 12. Version Control Taxonomy

### 12.1 Branch Naming

**Format**: `<type>/<scope>/<description>`

**Types**:
- `feature/`: New feature development
- `bugfix/`: Bug fixes
- `hotfix/`: Critical production fixes
- `release/`: Release preparation
- `experiment/`: Experimental work

**Examples**:
- `feature/fcs_nn/aero-predictor-v2.2`
- `bugfix/fcs_nn/envelope-protection-edge-case`
- `release/fcs_nn/v1.0.0`

### 12.2 Commit Message Format

**Format**: `<type>(<scope>): <subject>`

**Types**: `feat`, `fix`, `docs`, `test`, `refactor`, `chore`

**Examples**:
- `feat(aero_predictor): add icing condition adaptation`
- `fix(control_optimizer): correct actuator rate limiting`
- `docs(safety): update certification evidence`
- `test(gla): add turbulence edge cases`

### 12.3 Tag Naming

**Format**: `v<major>.<minor>.<patch>[-<pre-release>]`

**Examples**:
- `v1.0.0`: Major release
- `v1.1.0`: Minor feature release
- `v1.1.1`: Patch release
- `v2.0.0-beta.1`: Pre-release

---

## 13. References

- [95-20-27-001_FCS_NN_Overview.md](../95-20-27-001_FCS_NN_Overview.md)
- [95-20-27-012_FCS_NN_Traceability_Map.csv](95-20-27-012_FCS_NN_Traceability_Map.csv)
- [95-20-27-013_FCS_NN_Assets_Registry.json](95-20-27-013_FCS_NN_Assets_Registry.json)
- [AMPEL360_DOCUMENTATION_STANDARD.md](../../../../../../AMPEL360_DOCUMENTATION_STANDARD.md)
- [AMPEL360_ASSETS_STANDARD.md](../../../../../../AMPEL360_ASSETS_STANDARD.md)

---

## Document Control

- **Owner**: AMPEL360 FCS_NN Architecture Team
- **Version**: 1.0
- **Status**: Active
- **Classification**: Technical Reference
- **Last Updated**: 2025-11-17
