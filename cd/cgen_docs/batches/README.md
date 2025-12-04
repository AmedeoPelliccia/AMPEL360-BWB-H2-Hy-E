# CGen Docs Batches

This directory contains the batch configuration files for CGen Docs Waves.

## Batch Files

| File | Description |
|------|-------------|
| `BATCH_ONBOARD_A.yaml` | T-ON_BOARD Systems - Wave A (Airframe, Aerodynamics, Cockpit) |
| `BATCH_ONBOARD_B.yaml` | T-ON_BOARD Systems - Wave B (Energy, Electronics, Propulsion) |
| `BATCH_INFRA_A.yaml` | I-INFRASTRUCTURES - Wave A |

## Batch Configuration Schema

```yaml
batch_id: BATCH_XXX           # Unique identifier
name: "Human-readable name"
description: |
  Multi-line description
frequency: "P3D"              # ISO 8601 duration (informational)
owner: "Owner name"

scope:                        # Directories to process
  - path: OPT-IN_FRAMEWORK/...
    patterns:
      - "**/*.md"
    exclude:
      - "**/00_INDEX.md"

targets:                      # Processing objectives
  - type: deepen_sections
    description: "..."
    priority: 1

context_sources:              # Additional context files
  - path: OPT-IN_FRAMEWORK/README.md
    role: "framework_overview"

ai_policy:                    # AI configuration
  model: "gpt-5.1-codex"
  max_tokens_per_doc: 6000
  temperature: 0.2
  require_human_review: true
  write_mode: "inplace"

output:                       # Output configuration
  update_sidecars: true
  log_to_jsonl: true
```

## Adding New Batches

1. Create a new YAML file following the schema above
2. Use a unique `batch_id` with format `BATCH_<DOMAIN>_<WAVE>`
3. Define the scope paths relative to repository root
4. Configure appropriate AI policy settings

---
