# 23-97-10-001 — MMIP ⇄ AST-L Binding

**Document ID:** 23-97-10-001_MMIP_ASTL_Binding  
**Chapter:** ATA 23-97-10 CAPSULES  
**Version:** 0.1  
**Status:** DRAFT  

---

## 1. Purpose

Define how **MMIP Memory Capsules** carry **AST-L (Aerospace Semantic Technical Language)** content to ensure semantic interoperability across AMPEL360 systems.

---

## 2. AST-L in Capsule Content

MMIP capsules use the `content` field to store structured information. When carrying technical semantics, the content SHOULD contain valid AST-L statements.

### 2.1 Content Structure

```json
{
  "capsule_id": "cap_SHM_001",
  "type": "model_message",
  "scope": "session",
  "content": {
    "ast_l": {
      "statements": [
        {
          "subject": "STRINGER_F2",
          "predicate": "hasCondition",
          "object": "OVERLOAD_DETECTED",
          "confidence": 0.92
        }
      ],
      "version": "1.0"
    },
    "natural_language": "Overload condition detected on Stringer F2 with 92% confidence."
  },
  "provenance": { "...": "..." }
}
```

### 2.2 Validation Rules

- Capsules with `type: model_message` or `type: summary` SHOULD contain valid AST-L.
- Invalid AST-L MUST be logged and flagged.
- Safety-critical Context Packages MUST NOT contain unvalidated AST-L.

---

## 3. AST-L Statement Types

| Statement Type | Use Case |
|----------------|----------|
| Observation | Sensor readings, detected anomalies |
| Hypothesis | Agent reasoning, root cause analysis |
| Decision | Recommended actions, maintenance plans |
| Reference | Links to standards, procedures, or artifacts |

---

## 4. References

- [23-96 AST-L Specification](../../23-96_AST_L/) _(if exists)_
- [MMIP Capsule Schema](../23-97-90_SCHEMAS/capsule.json)
- [23-97-00-001 MMIP Overview](../23-97-00_GENERAL/23-97-00-001_MMIP_Overview.md)

---

## 5. Document Control

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT** – Subject to human review and approval.
- Human approver: _[to be completed]_.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: 2025-11-28.

---
