# 23-97-00-001 — MMIP Overview

**Document ID:** 23-97-00-001_MMIP_Overview  
**Chapter:** ATA 23-97 MODELS MEMORY PROTOCOL  
**Version:** 0.1  
**Status:** DRAFT  
**Owner:** C-COMMUNICATIONS / CAOS Architecture  

---

## 1. Purpose

This document introduces the **Models Memory Inheritance Protocol (MMIP)** as the
standard **memory substrate** for AMPEL360.

MMIP defines **what gets remembered**, **how it is structured**, and **how it is
inherited** across:

- Models (reasoning, code, vision, planning, control)
- Agents (CAOS SHM, ICA, MRO, etc.)
- Transports (FAirCCC/CFLF, MCP, internal buses)
- Surfaces (IETP, CAOS consoles, engineering tools)

Where:

- **AST-L** defines *how information is expressed* (technical language),
- **FAirCCC** defines *how information is transported* (channels, QoS),
- **MMIP** defines *how information is persisted and inherited as memory*.

---

## 2. Scope

MMIP in AMPEL360 covers:

- All **AI/ML-enabled subsystems** described under ATA 95 / ATA 23.
- All **CAOS agents** participating in Operations & Services decision loops.
- All **context flows** where previous state influences future reasoning.

Out of scope:

- Low-level signal transport (covered by FAirCCC / CFLF).
- Model-internal weights and training data (covered by 97-40-20_DP / 97-40-20_FL).

---

## 3. Conceptual Stack

```text
┌───────────────────────────────────────────────┐
│           23-97 MMIP (this chapter)          │
│      Memory Capsules / Threads / Packages    │
├───────────────────────────────────────────────┤
│           23-96 AST-L                        │
│      Technical semantic language             │
├───────────────────────────────────────────────┤
│           23-95 COMM_NN (FAirCCC)            │
│      Neural network communication protocols  │
└───────────────────────────────────────────────┘
```

- MMIP objects carry **AST-L statements** inside the `content` field.
- MMIP envelopes ride on **FAirCCC/CFLF channels** as payloads.

---

## 4. MMIP Core Objects in AMPEL360

| MMIP Concept | AMPEL360 Mapping |
|--------------|------------------|
| Memory Capsule | AST-L statement(s) + context + policy |
| Memory Thread | CAOS event chain / mission or operation storyline |
| Context Package | CUC-like bundle for reusable context |
| Memory Envelope | Gradient Envelope delivered to a model/agent |
| Provenance | DPP traceability + CAOS event metadata |
| Policies | 97-40-20 governance overlays |

---

## 5. Default Automatic Inheritance

MMIP implementations in AMPEL360 MUST automatically inherit relevant memory on 
model or session shifts by default. This ensures context continuity without 
requiring manual re-entry of information.

**Default behavior on model/session shift**:

1. The system MUST automatically invoke `INHERIT_CONTEXT` with the current thread and applicable context packages
2. The incoming model/session MUST receive the composed Memory Envelope
3. Context MUST NOT be reset unless explicitly requested by the user or policy

---

## 6. Validation Rules

- Capsules labelled as `model_message` or `summary` SHOULD contain **valid AST-L**
  statements; malformed AST-L MUST be logged and either corrected or isolated.
- AST-L violations MUST NOT silently propagate into Context Packages used for
  safety-critical decisions.

---

## 7. References

- [MMIP v0.1 Specification](../../../../../../mmip-standard/spec/mmip-v0.1.md)
- [MMIP Schemas](../../../../../../mmip-standard/schemas/)
- [23-97-60-010 MMIP ⇄ FAirCCC Integration](../23-97-60_INHERITANCE/23-97-60-010_MMIP_FAIRCCC_Integration.md)
- [23-97-70-010 MMIP ⇄ CAOS Agent Memory](../23-97-70_OPERATIONS/23-97-70-010_MMIP_CAOS_Agent_Memory.md)

---

## 8. Document Control

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT** – Subject to human review and approval.
- Human approver: _[to be completed]_.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: 2025-11-28.

---
