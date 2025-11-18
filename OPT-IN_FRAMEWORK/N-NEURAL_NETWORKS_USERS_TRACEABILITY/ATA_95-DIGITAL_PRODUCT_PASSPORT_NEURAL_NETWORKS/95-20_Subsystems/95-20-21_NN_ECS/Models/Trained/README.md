# Trained Models Directory

This directory contains the official trained ONNX models for the AMPEL360 BWB H₂ Hy-E Environmental Control System neural networks.

## Air Quality Monitor v1.0

**File**: `air_quality_monitor_v1.0.onnx`  
**Model ID**: 95-20-21-A-102  
**Version**: 1.0  
**Status**: WORKING

### Model Properties

- **Size**: 4.0 MB
- **Parameters**: 1,026,117 (all trainable)
- **SHA256**: `bb03e479d77c729a22058a53bee62b149b4f090fe7675ab3b42e403d24edd2d4`
- **ONNX Opset**: 17
- **Framework**: PyTorch → ONNX

### Architecture

```
Input (sensor_window) 
  ↓ [batch, seq_len, 16]
1D CNN (64/128/256 filters)
  ↓ 
Bi-directional LSTM (2 layers, 256 units)
  ↓
Dense layers (128 → 64 → 5)
  ↓
Output (aqi_logits) [batch, 5] - 5-class AQI classification
```

### Input/Output Specification

**Input**:
- Name: `sensor_window`
- Shape: `[batch_size, seq_len, 16]`
- Type: `float32`
- Dynamic axes: `batch_size`, `seq_len`
- Features (16):
  - CO₂ concentration (ppm)
  - Humidity (% RH)
  - VOC level (ppb)
  - PM2.5 (μg/m³)
  - PM10 (μg/m³)
  - Temperature (°C)
  - ... (10 additional sensor readings)

**Output**:
- Name: `aqi_logits`
- Shape: `[batch_size, 5]`
- Type: `float32`
- Classes:
  1. Excellent (AQI 1)
  2. Good (AQI 2)
  3. Moderate (AQI 3)
  4. Poor (AQI 4)
  5. Hazardous (AQI 5)

### Usage

#### Inspect the Model

```bash
cd ../Source
python3 inspect_air_quality_onnx.py
```

#### Regenerate the Model

```bash
cd ../Source
python3 export_air_quality_onnx.py
```

#### Load in ONNX Runtime (Python)

```python
import onnxruntime as ort
import numpy as np

# Load model
session = ort.InferenceSession("air_quality_monitor_v1.0.onnx")

# Prepare input (example: batch_size=1, seq_len=60, features=16)
sensor_data = np.random.randn(1, 60, 16).astype(np.float32)

# Run inference
outputs = session.run(None, {"sensor_window": sensor_data})
logits = outputs[0]

# Apply softmax to get probabilities
import scipy.special
probabilities = scipy.special.softmax(logits, axis=1)
predicted_class = np.argmax(probabilities, axis=1)[0] + 1  # AQI 1-5
```

### Metadata

The ONNX model includes embedded metadata accessible via `onnx.load()`:

- `model_id`: 95-20-21-A-102
- `version`: 1.0
- `component`: 95-20-21-003_Air_Quality_Monitor
- `dal_level`: C
- `certification`: DO-178C
- `owner`: AMPEL360 ML Engineering Team
- `ai_assistance`: GitHub Copilot; prompted by Amedeo Pelliccia

### References

- **Component Specification**: [95-20-21-003_Air_Quality_Monitor.md](../../95-20-21-003_Air_Quality_Monitor.md)
- **Model Card**: [95-20-21-A-102_Air_Quality_Monitor_v1.0.yaml](../../ASSETS/Model_Cards/95-20-21-A-102_Air_Quality_Monitor_v1.0.yaml)
- **Training Config**: [training_config_air_quality.yaml](../Configs/training_config_air_quality.yaml)
- **Source Code**: [air_quality_monitor_v1.0.py](../Source/air_quality_monitor_v1.0.py)

### Safety & Certification

- **DAL Level**: C (Hazardous)
- **Certification Standard**: [DO-178C](https://www.rtca.org/product/do-178c/)
- **Failure Condition**: Undetected poor air quality could affect passenger health
- **Mitigation**: Redundant sensors + direct sensor readouts to crew

For detailed safety analysis, see [95-20-21-009_Safety_and_Certification.md](../../95-20-21-009_Safety_and_Certification.md)

---

## Document Control

- **Status**: WORKING
- **Last Updated**: 2025-11-17
- **AI Assistance**: Generated with GitHub Copilot, prompted by Amedeo Pelliccia
- **Repository**: AMPEL360-BWB-H2-Hy-E
- **Approver**: _[to be completed]_
