# NN-ECS Models Directory

This directory contains model cards and configuration files for all neural network models in the ECS subsystem.

## Purpose

Model cards document the specifications, training approach, performance, and limitations of each trained model.

## File Naming Convention

- Model cards: `95-20-21-M-XXX_<Short_Model_Name>.md`
- Model configurations: `95-20-21-M-XXX_<Short_Model_Name>_config.yaml` or `.json`

## Example

```
95-20-21-M-001_ECS_Cabin_Temp_Model.md
95-20-21-M-001_ECS_Cabin_Temp_Model_config.yaml
```

## Model Card Template

See `.github/instructions/95-20-21-nn-ecs.instructions.md` Section 4.4 for the model card template.

## Models to be Documented

1. M-001: Cabin Temperature Predictor
2. M-002: Air Quality Monitor
3. M-003: HVAC Optimizer
4. M-004: Pressure Control NN
5. M-005: Humidity Management
6. M-006: CO₂ Scrubbing Optimizer

## Related Artifacts

- Training Runs: `../TRAINING_RUNS/`
- Datasets: `../DATASETS/`
- Verification Evidence: `../../10_CERTIFICATION/ASSETS/Reports/`

---

**Last Updated**: 2025-11-23
