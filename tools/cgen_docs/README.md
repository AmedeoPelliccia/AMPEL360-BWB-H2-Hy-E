# CGen Docs Waves - Tools

This directory contains the Python implementation of the CGen Docs Waves system.

## Structure

```text
tools/cgen_docs/
├── __init__.py          # Package init
├── run_batch.py         # Main entry point
├── utils/               # Utility modules
│   ├── __init__.py
│   ├── ai.py            # AI model integration
│   ├── context.py       # Context loading
│   ├── diff.py          # File diff and writing
│   └── metadata.py      # Logging and metadata
└── prompts/             # Prompt templates
    ├── __init__.py
    └── deepen_evolve.py # Main prompt templates
```

## Usage

```bash
# Run a batch
python tools/cgen_docs/run_batch.py --batch-id BATCH_ONBOARD_A

# Dry run
python tools/cgen_docs/run_batch.py --batch-id BATCH_ONBOARD_A --dry-run

# Verbose
python tools/cgen_docs/run_batch.py --batch-id BATCH_ONBOARD_A --verbose
```

## Dependencies

- Python 3.11+
- pyyaml
- openai (optional, for AI processing)

## Environment Variables

| Variable | Description |
|----------|-------------|
| `OPENAI_API_KEY` | OpenAI API key for AI processing |

## Components

### run_batch.py

Main entry point that:
1. Loads batch configuration
2. Collects documents from scope
3. Processes each document through AI
4. Writes changes and metadata

### utils/context.py

Loads and assembles context for AI prompts:
- Global AMPEL360 context
- Document-specific context
- Related documents

### utils/ai.py

Handles AI model integration:
- API client management
- Prompt execution with retries
- Response parsing

### utils/diff.py

Manages file operations:
- Writing changes
- Sidecar metadata generation
- Backup creation

### utils/metadata.py

Logging and reporting:
- JSONL wave logs
- Wave reports
- Statistics generation

### prompts/deepen_evolve.py

Contains prompt templates:
- Main Deepen & Evolve prompt
- Sidecar metadata prompt
- Prompt composition logic

---

## Document Control

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT** – Subject to human review and approval.
- Human approver: _[to be completed]_.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: 2025-12-04.

---
