# 23-97-80-001 — MMIP Reference Implementation Link

**Document ID:** 23-97-80-001_MMIP_Reference_Implementation_Link  
**Chapter:** ATA 23-97-80 REFERENCE_IMPL  
**Version:** 0.1  
**Status:** DRAFT  

---

## 1. Purpose

This document provides links to the MMIP reference implementation for use within AMPEL360.

---

## 2. Reference Implementation Location

The MMIP reference implementation is maintained in the repository at:

```
mmip-standard/reference_impl/
├── __init__.py
└── mmip_protocol.py
```

### Python Module

The reference implementation provides:

- **Enums**: `CapsuleType`, `Scope`, `ExportPolicy`, `RetentionPolicy`, `ProducerType`, `ApplyMode`, `LinkType`
- **Data Classes**: `Capsule`, `Envelope`, `Thread`, `ContextPackage`, `Provenance`, etc.
- **Abstract Protocol**: `MMIPProtocol` base class with all required operations
- **Compliance Checker**: `check_compliance_level()` function

### Example Usage

```python
from mmip_protocol import Capsule, CapsuleType, Scope, Provenance
from datetime import datetime

# Create a capsule
capsule = Capsule(
    capsule_id="cap_CAOS_SHM_001",
    capsule_type=CapsuleType.MODEL_MESSAGE,
    scope=Scope.SESSION,
    content={"ast_l": "ANOMALY detected in STRINGER F2"},
    provenance=Provenance(
        timestamp=datetime.now(),
        creator_id="CAOS_SHM",
        creator_type=ProducerType.AGENT
    )
)
```

---

## 3. Schema Files

JSON Schemas for validation are available at:

- [capsule.json](../23-97-90_SCHEMAS/capsule.json) — Memory Capsule schema
- [envelope.json](../23-97-90_SCHEMAS/envelope.json) — Memory Envelope schema

Original schemas are maintained at:

- [mmip-standard/schemas/capsule.json](../../../../../../mmip-standard/schemas/capsule.json)
- [mmip-standard/schemas/envelope.json](../../../../../../mmip-standard/schemas/envelope.json)

---

## 4. Integration with CAOS

For CAOS agent integration, see:

- [23-97-70-010 MMIP ⇄ CAOS Agent Memory](../23-97-70_OPERATIONS/23-97-70-010_MMIP_CAOS_Agent_Memory.md)

---

## 5. Document Control

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT** – Subject to human review and approval.
- Human approver: _[to be completed]_.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: 2025-11-28.

---
