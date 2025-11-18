# Model Scripts

This directory contains utility scripts for model inspection, testing, and deployment.

## Available Scripts

### inspect_onnx_model.py

Inspects ONNX model files and generates detailed reports.

```bash
python inspect_onnx_model.py --model ../Trained/fuel_quantity_estimator_v1.0.onnx
```

**Features:**
- Model architecture visualization
- Input/output tensor shapes and types
- Parameter count and memory usage
- Operator analysis

### test_onnx_model_fuel.py

Tests ONNX fuel system models with sample data.

```bash
python test_onnx_model_fuel.py --model ../Trained/fuel_quantity_estimator_v1.0.onnx --test-data ../../Data/Test/
```

**Features:**
- Inference time benchmarking
- Accuracy validation
- Range checking
- Performance profiling

### deploy_to_ima_fuel.py

Deploys trained models to the IMA platform.

```bash
python deploy_to_ima_fuel.py --model ../Trained/fuel_quantity_estimator_v1.0.onnx --target ima-partition-3
```

**Features:**
- Model verification before deployment
- IMA partition compatibility checking
- Deployment logging and rollback
- Health check after deployment

## Usage Guidelines

### Model Inspection

Before deploying any model, always inspect it:

```bash
python inspect_onnx_model.py --model <model_path>
```

### Testing

Run comprehensive tests before production deployment:

```bash
python test_onnx_model_fuel.py --model <model_path> --test-data <test_data_path> --verbose
```

### Deployment

Deploy to IMA only after successful testing:

```bash
python deploy_to_ima_fuel.py --model <model_path> --target <ima_partition> --dry-run  # First do dry run
python deploy_to_ima_fuel.py --model <model_path> --target <ima_partition>  # Then actual deployment
```

## Reusable Scripts

Scripts in this directory can be parameterized and reused for different fuel system models. They follow the same pattern established in the ECS subsystem ([95-20-21](../../95-20-21_NN_ECS/Models/Scripts/)).

## Document Control

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT** – Subject to human review and approval.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: _2025-11-18_.
