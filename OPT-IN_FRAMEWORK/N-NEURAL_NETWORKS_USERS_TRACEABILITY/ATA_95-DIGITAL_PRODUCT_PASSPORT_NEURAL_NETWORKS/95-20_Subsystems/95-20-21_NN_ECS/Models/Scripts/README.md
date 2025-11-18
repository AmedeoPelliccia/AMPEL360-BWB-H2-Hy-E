# Model Scripts

This directory contains scripts for managing, inspecting, testing, and deploying the cabin temperature predictor ONNX model.

## 📁 Scripts Overview

### 1. `inspect_onnx_model.py`

**Purpose**: Comprehensive ONNX model inspection and validation

**Usage**:
```bash
python3 inspect_onnx_model.py <model_path>
```

**Example**:
```bash
python3 inspect_onnx_model.py ../Trained/temp_predictor_v1.2.onnx
```

**Features**:
- Validates ONNX format compliance
- Extracts and displays metadata
- Analyzes model architecture (nodes, operations, parameters)
- Computes file integrity hashes (SHA-256, MD5)
- Tests runtime inference with ONNX Runtime
- Measures inference latency
- Generates JSON inspection report

**Output**:
- Console output with detailed model information
- JSON report: `<model_name>_inspection_report.json`

---

### 2. `test_onnx_model.py`

**Purpose**: Comprehensive test suite for ONNX model validation

**Usage**:
```bash
python3 test_onnx_model.py <model_path>
```

**Example**:
```bash
python3 test_onnx_model.py ../Trained/temp_predictor_v1.2.onnx
```

**Test Suite** (6 tests):

1. **Input Validation** - Validates correct and incorrect input shapes
2. **Output Range Validation** - Ensures predictions are physically realistic
3. **Physical Consistency** - Tests physics-based behavior and stability
4. **Inference Latency** - Benchmarks performance (requirement: <10ms)
5. **Numerical Stability** - Checks for determinism and NaN/Inf values
6. **Batch Processing** - Tests various batch sizes (1, 2, 4, 8)

**Exit Codes**:
- `0`: All tests passed
- `1`: One or more tests failed

---

### 3. `deploy_to_ima.py`

**Purpose**: Deploy ONNX model to IMA Neural Partition with verification

**Usage**:
```bash
python3 deploy_to_ima.py <model_path> [aircraft_serial]
```

**Example**:
```bash
python3 deploy_to_ima.py ../Trained/temp_predictor_v1.2.onnx AMPEL360-Q100-001
```

**Deployment Pipeline** (5 steps):

1. **Verify Integrity** - Compute and verify SHA-256 hash
2. **Copy to IMA Staging** - Stage model for deployment
3. **Load to ARINC 653 Partition** - Load into target partition
4. **Run Built-In Test (BIT)** - Validate operational status
5. **Log to DPP** - Record deployment in Digital Product Passport

**Output**:
- Console output with deployment status
- Deployment log JSON: `deployment_log_<timestamp>.json`
- Blockchain anchor (simulated)

---

### 4. `generate_simple_onnx.py`

**Purpose**: Generate ONNX model from Keras architecture

**Usage**:
```bash
python3 generate_simple_onnx.py
```

**Features**:
- Builds LSTM-based Keras model
- Performs quick training with synthetic data
- Exports to ONNX format (opset 17)
- Adds metadata (model_id, version, certification info)
- Computes and displays SHA-256 hash

**Output**:
- ONNX model file: `../Trained/temp_predictor_v1.2.onnx`
- Model information (size, hash, architecture)

---

### 5. `generate_onnx_model.py`

**Purpose**: Alternative model generation script (requires source module import)

**Note**: This script imports from the Source directory and may have dependency issues. Use `generate_simple_onnx.py` as the primary generation script.

---

## 🔧 Requirements

### Python Version
- Python 3.8 or higher

### Dependencies
```bash
pip install onnx onnxruntime numpy tensorflow tf2onnx
```

### Specific Versions (tested):
- `onnx>=1.17.0`
- `onnxruntime>=1.23.0`
- `numpy>=2.3.0`
- `tensorflow>=2.20.0`
- `tf2onnx>=1.16.0`

---

## 📊 Typical Workflow

### 1. Generate Model (if needed)
```bash
python3 generate_simple_onnx.py
```

### 2. Inspect Model
```bash
python3 inspect_onnx_model.py ../Trained/temp_predictor_v1.2.onnx
```

### 3. Test Model
```bash
python3 test_onnx_model.py ../Trained/temp_predictor_v1.2.onnx
```

### 4. Deploy Model
```bash
python3 deploy_to_ima.py ../Trained/temp_predictor_v1.2.onnx AMPEL360-Q100-001
```

---

## 🔐 Security & Verification

All scripts include security features:

- **Hash Verification**: SHA-256 and MD5 checksums
- **Digital Signatures**: GPG signature verification (production)
- **Blockchain Anchoring**: DPP integration for provenance
- **Audit Logging**: All operations logged with timestamps

---

## 📝 Model Metadata

Each script interacts with model metadata:

```yaml
model_id: "95-20-21-A-101"
version: "1.2"
created_by: "Amedeo Pelliccia"
framework: "TensorFlow 2.20"
opset: "17"
dal_level: "DAL C"
certification: "DO-178C"
```

---

## 🚨 Troubleshooting

### Common Issues

**1. Import Errors**
```bash
# Install missing dependencies
pip install onnx onnxruntime
```

**2. TensorFlow Compatibility**
```bash
# Ensure compatible versions
pip install 'tensorflow>=2.14' 'tf2onnx>=1.16'
```

**3. ONNX Runtime Errors**
```bash
# Reinstall ONNX Runtime
pip uninstall onnxruntime
pip install onnxruntime
```

**4. Model Not Found**
```bash
# Check path
ls -l ../Trained/temp_predictor_v1.2.onnx
```

---

## 📚 References

- **Model Card**: [95-20-21-A-101_Temp_Predictor_v1.2.yaml](../../ASSETS/Model_Cards/95-20-21-A-101_Temp_Predictor_v1.2.yaml)
- **Model README**: [../Trained/README.md](../Trained/README.md)
- **Component Spec**: [../../95-20-21-002_Cabin_Temp_Predictor.md](../../95-20-21-002_Cabin_Temp_Predictor.md)
- **ONNX Documentation**: https://onnx.ai/
- **ONNX Runtime**: https://onnxruntime.ai/

---

## 📞 Support

- **Owner**: AMPEL360 ML Engineering Team
- **Email**: ml-engineering@ampel360.aero
- **Issue Tracker**: GitHub Issues

---

## Document Control

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **PRODUCTION** – Subject to human review and approval.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: _2025-11-17_.

---
