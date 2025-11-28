# MMIP — Models Memory Inheritance Protocol

**Version:** 0.1  
**Status:** Draft Standard  
**Date:** 2025-11-28

## Overview

The **Models Memory Inheritance Protocol (MMIP)** defines a vendor-agnostic, transport-agnostic standard for representing, storing, sharing, inheriting, redacting, and exporting **memory capsules** between generative AI models, tools, and agentic workflows.

MMIP enables continuity of context across:

- **Model switches** (e.g., reasoning → code → image)
- **Tool calls**
- **Agent pipelines**
- **Playground or IDE sessions**

...without requiring users to manually re-enter context.

MMIP also provides **user-level control**: browsing, managing, grouping, redacting, exporting, and injecting context as **Context Packages**.

## Repository Structure

```text
mmip-standard/
├── README.md                    # This file (introduction)
├── spec/
│   └── mmip-v0.1.md             # Full standard specification
├── schemas/
│   ├── capsule.json             # Memory Capsule JSON Schema (Annex A.1)
│   └── envelope.json            # Memory Envelope JSON Schema (Annex A.2)
├── assets/
│   └── diagrams/
│       └── README.md            # Architecture diagrams (Annex D)
└── reference_impl/
    └── mmip_protocol.py         # Reference Python API skeleton
```

## Quick Start

### 1. Read the Specification

The complete specification is in [`spec/mmip-v0.1.md`](./spec/mmip-v0.1.md).

### 2. Validate Your Implementation

Use the JSON Schemas in the `schemas/` directory to validate your capsules and envelopes:

```python
import json
import jsonschema

# Load schemas
with open("schemas/capsule.json") as f:
    capsule_schema = json.load(f)
with open("schemas/envelope.json") as f:
    envelope_schema = json.load(f)

# Validate a capsule
capsule = {
    "capsule_id": "cap_001",
    "type": "user_message",
    "scope": "session",
    "content": {"text": "Hello, world!"},
    "provenance": {"timestamp": "2025-11-28T12:00:00Z"}
}
jsonschema.validate(capsule, capsule_schema)
```

### 3. Implement the Protocol

Use the reference implementation skeleton in `reference_impl/mmip_protocol.py` as a starting point.

## Key Concepts

| Concept | Description |
|---------|-------------|
| **Memory Capsule** | Atomic unit of memory containing content, metadata, scopes, and policies |
| **Memory Thread** | A chain or DAG of capsules representing a persistent contextual sequence |
| **Context Package** | A named, user-definable bundle of capsules and summaries, portable across sessions and models |
| **Memory Envelope** | The subset of memory delivered to a model/tool for a single call |

## Compliance Levels

MMIP defines three compliance tiers:

| Level | Name | Description |
|-------|------|-------------|
| **Level 1** | Basic | Supports capsules, threads, and envelopes |
| **Level 2** | User-Controlled Memory | Adds packages, export, redaction, and user-facing operations |
| **Level 3** | Full Agentic Interoperability | Implements inheritance, summarization, lineage, integrity, and cross-model portability |

## Integration

MMIP is designed to work with:

- **LLMs, VLMs, code models, tool agents**
- **Playgrounds, IDEs, Copilot-like systems**
- **Model context servers** (e.g., MCP-based)
- **Multi-agent, multi-model AI stacks**

## Related Projects

- [`mcp-pr-memory`](../mcp-pr-memory/) — A prototype MCP server for indexing PRs/commits

## License

See [LICENSE](../LICENSE) for license information.

---

## Document Control

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT** – Subject to human review and approval.
- Human approver: _[to be completed]_.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: 2025-11-28.

---
