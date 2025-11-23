# NN-ECS Datasets Directory

This directory contains dataset cards and schema files for all datasets used in training and validation.

## Purpose

Dataset cards document the source, collection method, quality, and usage of training/validation/test datasets.

## File Naming Convention

- Dataset cards: `95-20-21-D-XXX_<Short_Dataset_Name>.md`
- Dataset schemas: `95-20-21-D-XXX_<Short_Dataset_Name>_schema.json` or `.csv`

## Example

```
95-20-21-D-001_ECS_Operational_Logs.md
95-20-21-D-001_ECS_Operational_Logs_schema.json
```

## Dataset Card Template

See `.github/instructions/95-20-21-nn-ecs.instructions.md` Section 4.4 for the dataset card template.

## Datasets to be Documented

1. D-001: ECS Operational Logs (10,000 flight hours)
2. D-002: Flight Test Data (2,000 hours)
3. D-003: Synthetic Cabin Environment Scenarios
4. D-004: Ground Test Data
5. D-005: Edge Case Collection

## Related Artifacts

- Model Cards: `../MODELS/`
- Training Runs: `../TRAINING_RUNS/`
- OD/ODD Specification: `../../DS-AI_CONFORMITY/95-20-21-A-102_NN-ECS_Operational_Domain_ODD_DS-AI-120.md`

---

**Last Updated**: 2025-11-23
