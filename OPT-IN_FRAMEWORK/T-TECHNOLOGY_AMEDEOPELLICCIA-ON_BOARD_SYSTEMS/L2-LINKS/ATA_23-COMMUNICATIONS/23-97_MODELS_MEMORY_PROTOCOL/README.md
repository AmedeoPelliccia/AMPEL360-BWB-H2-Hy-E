# ATA 23-97 — Models Memory Protocol (MMIP)

**Chapter:** ATA 23-97 MODELS_MEMORY_PROTOCOL  
**Version:** 0.1  
**Status:** DRAFT  
**Parent:** ATA 23 COMMUNICATIONS (L2-LINKS)

---

## Overview

This chapter defines the **Models Memory Inheritance Protocol (MMIP)** integration within the AMPEL360 program, providing the standard memory substrate for AI/ML-enabled systems.

MMIP defines **what gets remembered**, **how it is structured**, and **how it is inherited** across:

- Models (reasoning, code, vision, planning, control)
- Agents (CAOS SHM, ICA, MRO, etc.)
- Transports (FAirCCC/CFLF, MCP, internal buses)
- Surfaces (IETP, CAOS consoles, engineering tools)

## Relationship to Other Standards

| Standard | Role |
|----------|------|
| **AST-L** (23-96) | Defines *how information is expressed* (technical language) |
| **FAirCCC** (23-95) | Defines *how information is transported* (channels, QoS) |
| **MMIP** (23-97) | Defines *how information is persisted and inherited as memory* |

## Directory Structure

```
23-97_MODELS_MEMORY_PROTOCOL/
├── README.md                          # This file
├── 23-97-00_GENERAL/
│   ├── 23-97-00-001_MMIP_Overview.md
│   └── 23-97-00-002_MMIP_AMPEL360_Context.md
├── 23-97-10_CAPSULES/
│   └── 23-97-10-001_MMIP_ASTL_Binding.md
├── 23-97-20_THREADS/
│   └── 23-97-20-001_MMIP_Threads_CAOS_Events.md
├── 23-97-30_PACKAGES/
│   └── 23-97-30-001_Context_Packages_CUC.md
├── 23-97-40_ENVELOPES/
│   └── 23-97-40-001_Gradient_Envelopes_Mapping.md
├── 23-97-50_POLICIES/
│   └── 23-97-50-001_MMIP_Policies_97-40-20_Link.md
├── 23-97-60_INHERITANCE/
│   └── 23-97-60-010_MMIP_FAIRCCC_Integration.md
├── 23-97-70_OPERATIONS/
│   └── 23-97-70-010_MMIP_CAOS_Agent_Memory.md
├── 23-97-80_REFERENCE_IMPL/
│   └── 23-97-80-001_MMIP_Reference_Implementation_Link.md
└── 23-97-90_SCHEMAS/
    ├── capsule.json
    └── envelope.json
```

## Key Documents

| Document | Description |
|----------|-------------|
| [23-97-00-001_MMIP_Overview](./23-97-00_GENERAL/23-97-00-001_MMIP_Overview.md) | Introduction to MMIP in AMPEL360 |
| [23-97-60-010_MMIP_FAIRCCC_Integration](./23-97-60_INHERITANCE/23-97-60-010_MMIP_FAIRCCC_Integration.md) | MMIP ↔ FAirCCC transport binding |
| [23-97-70-010_MMIP_CAOS_Agent_Memory](./23-97-70_OPERATIONS/23-97-70-010_MMIP_CAOS_Agent_Memory.md) | MMIP ↔ CAOS agent memory binding |

## Related References

- [MMIP Specification (mmip-standard/)](../../../../../mmip-standard/) — Core MMIP v0.1 specification
- [ATA 95 Digital Product Passport](../../../../N-NEURAL_NETWORKS_USERS_TRACEABILITY/ATA_95-DIGITAL_PRODUCT_PASSPORT_NEURAL_NETWORKS/) — DPP integration
- [CAOS Architecture](../../../../../CAOS/) — CAOS agent system

---

## Document Control

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT** – Subject to human review and approval.
- Human approver: _[to be completed]_.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: 2025-11-28.

---
