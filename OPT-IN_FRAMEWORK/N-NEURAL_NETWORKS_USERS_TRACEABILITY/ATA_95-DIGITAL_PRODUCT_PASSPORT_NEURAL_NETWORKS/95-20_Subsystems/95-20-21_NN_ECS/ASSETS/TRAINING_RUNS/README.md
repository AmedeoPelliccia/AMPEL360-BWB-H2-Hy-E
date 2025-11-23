# NN-ECS Training Runs Directory

This directory contains records of all training runs for model traceability and reproducibility.

## Purpose

Training run records document the exact configuration, data, code version, and results of each training execution.

## File Naming Convention

- Training run records: `95-20-21-T-XXX_<Run_Name>.md` or `.json`

## Example

```
95-20-21-T-001_Baseline_Training_Run.json
95-20-21-T-002_Hyperparameter_Sweep_Run_5.json
```

## Training Run Record Template

See `.github/instructions/95-20-21-nn-ecs.instructions.md` Section 4.4 for the training run record format.

## Required Fields

```json
{
  "training_run_id": "95-20-21-T-XXX",
  "model_id": "95-20-21-M-XXX",
  "dataset_ids": ["95-20-21-D-XXX"],
  "git_commit": "<commit_hash>",
  "framework": "pytorch|tensorflow|...",
  "hyperparameters": {...},
  "metrics": {...},
  "seed": 1234,
  "training_date": "YYYY-MM-DD",
  "notes": "..."
}
```

## Related Artifacts

- Model Cards: `../MODELS/`
- Dataset Cards: `../DATASETS/`
- Learning Assurance: `../../DS-AI_CONFORMITY/95-20-21-A-106_NN-ECS_Learning_Assurance_DS-AI-150.md`

---

**Last Updated**: 2025-11-23
