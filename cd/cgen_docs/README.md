# CGen Docs Waves

This directory contains the configuration and infrastructure for the **CGen Docs Waves** system - an AI-assisted documentation improvement pipeline for AMPEL360 BWB H2 Hy-E.

## Overview

CGen Docs Waves extends the mechanical CGen (tables, indexes, traceability) into a **cognitive documentation evolution system** that:

* Reads large blocks of the repository
* Understands them in AMPEL360 context
* Detects gaps and inconsistencies
* Proposes deep evolutions on a scheduled basis (every 3 days by default)

## Directory Structure

```text
cd/cgen_docs/
├── batches/           # Batch configuration files (YAML)
│   ├── BATCH_ONBOARD_A.yaml
│   ├── BATCH_ONBOARD_B.yaml
│   └── BATCH_INFRA_A.yaml
├── cache/             # Processing cache
│   ├── summaries/     # Document summaries
│   └── embeddings/    # Vector embeddings (future)
├── logs/              # Wave execution logs (JSONL)
└── README.md          # This file
```

## Batches

Each batch defines a scope of documents to process:

| Batch ID | Name | Scope |
|----------|------|-------|
| `BATCH_ONBOARD_A` | T-ON_BOARD Systems – Wave A | Airframe, Aerodynamics, Cockpit/Cabin/Cargo |
| `BATCH_ONBOARD_B` | T-ON_BOARD Systems – Wave B | Energy, Electronics, Propulsion |
| `BATCH_INFRA_A` | I-INFRASTRUCTURES – Wave A | All infrastructure systems |

## How It Works

1. **Scheduled Execution**: GitHub Actions runs every 3 days
2. **Batch Selection**: Rotates through batches based on day of year
3. **Document Processing**: Each document is analyzed with AI assistance
4. **Changes Applied**: Improvements written back to documents
5. **PR Created**: Changes submitted as a pull request for human review

## Key Principles

* **CGen proposes, humans dispose** - All changes require human review
* **Traceability** - Every change is logged with AI metadata
* **Certification-friendly** - Wording suitable for aerospace certification
* **Incremental** - Evolves documentation over time, not all at once

## Running Manually

```bash
# Run a specific batch
python tools/cgen_docs/run_batch.py --batch-id BATCH_ONBOARD_A

# Dry run (no changes)
python tools/cgen_docs/run_batch.py --batch-id BATCH_ONBOARD_A --dry-run

# Verbose output
python tools/cgen_docs/run_batch.py --batch-id BATCH_ONBOARD_A --verbose
```

## Related Documentation

* [GenCCC gpt-5.1-codex Partitioned SW Development](../../../OPT-IN_FRAMEWORK/T-TECHNOLOGY_AMEDEOPELLICCIA-ON_BOARD_SYSTEMS/L1-LOGICS/ATA_42-IMA_GOVERNANCE/42-00-20_GENCCC_SW_CONFIG/42-00-20-001_GenCCC_gpt5_Partitioned_SW_Development.md)
* [CGen CI/CD Guide](../../../CGEN_CI_CD_GUIDE.md)

---

## Document Control

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT** – Subject to human review and approval.
- Human approver: _[to be completed]_.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: 2025-12-04.

---
