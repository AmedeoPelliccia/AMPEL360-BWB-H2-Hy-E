# Q100-61-TYPE-DIAG — Diagram Type Definition

## Overview

Diagrams (DIAG) are simplified graphical representations that show system relationships, data flow, logic, or organization at a higher level of abstraction than schematics.

## Purpose

- Provide system overview
- Show functional relationships
- Document data/signal flow
- Support system understanding
- Aid troubleshooting

## Types of Diagrams

| Subtype | Description | Use Case |
|---------|-------------|----------|
| Block Diagram | Functional blocks with connections | System architecture |
| Flow Diagram | Process or data flow | Control logic, data processing |
| Wiring Diagram | Physical wire routing | Installation reference |
| Context Diagram | System boundaries and interfaces | System definition |
| State Diagram | System states and transitions | Control behavior |

## Naming Convention

```
Q100-61-DIAG-[SYSTEM]-[SUBTYPE]-[SEQ].svg
```

Examples:
- `Q100-61-DIAG-FPS-BLK-001.svg` (System block diagram)
- `Q100-61-DIAG-EMD-FLOW-001.svg` (Control flow diagram)
- `Q100-61-DIAG-OFP-STATE-001.svg` (Pitch control states)

## Required Content

### Block Diagrams

| Element | Required | Notes |
|---------|:--------:|-------|
| Functional blocks | ✓ | Named, bounded |
| Connections | ✓ | Lines with labels |
| Signal direction | ✓ | Arrows |
| Interface boundaries | ✓ | System edges |
| Legend | As needed | Non-standard symbols |

### Flow Diagrams

| Element | Required | Notes |
|---------|:--------:|-------|
| Process steps | ✓ | In sequence |
| Decision points | ✓ | With conditions |
| Flow direction | ✓ | Arrows |
| Start/end points | ✓ | Clearly marked |
| Data stores | As needed | Databases, files |

### Context Diagrams

| Element | Required | Notes |
|---------|:--------:|-------|
| System boundary | ✓ | Clear delineation |
| External entities | ✓ | All interfaces |
| Data flows | ✓ | Labeled |
| Trust boundaries | As needed | Security context |

## Layout Guidelines

1. Top-to-bottom or left-to-right flow
2. Group related elements
3. Use consistent shapes
4. Minimize crossing lines
5. Include legend for symbols

## Abstraction Level

Diagrams should:
- Hide implementation details
- Show logical relationships
- Be understandable without reference to detail drawings
- Focus on "what" not "how"

## Related Drawing Types

| Type | Relationship |
|------|--------------|
| SCH | Detailed implementation |
| DRW | Physical implementation |
| ICD | Interface details |

## Examples of Use

- Propulsion system block diagram
- Power distribution architecture
- Control system flow
- Data acquisition system
- Emergency shutdown logic

## Standard Symbols

For consistency, use:
- Rectangles for processes/blocks
- Diamonds for decisions
- Ovals for start/end
- Arrows for flow direction
- Cylinders for data stores

---

## Document Control

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT** – Subject to human review and approval.
- Human approver: _[to be completed]_.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: _2025-12-04_.

---
