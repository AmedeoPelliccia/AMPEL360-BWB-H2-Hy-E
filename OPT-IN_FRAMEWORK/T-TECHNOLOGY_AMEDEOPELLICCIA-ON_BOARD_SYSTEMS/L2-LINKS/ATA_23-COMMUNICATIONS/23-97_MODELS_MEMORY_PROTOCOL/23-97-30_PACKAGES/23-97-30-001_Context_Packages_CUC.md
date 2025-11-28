# 23-97-30-001 — Context Packages ⇄ CUC

**Document ID:** 23-97-30-001_Context_Packages_CUC  
**Chapter:** ATA 23-97-30 PACKAGES  
**Version:** 0.1  
**Status:** DRAFT  

---

## 1. Purpose

Define how **MMIP Context Packages** relate to **CUC (Contextual Use Cases)** and reusable context bundles in AMPEL360.

---

## 2. Package Types

| Package Type | Description | Retention |
|--------------|-------------|-----------|
| `pkg_AIRCRAFT_ARCH` | Aircraft architecture context | long_term |
| `pkg_MISSION_<id>` | Mission-specific context | session |
| `pkg_ICA_CASE_<id>` | Investigation case bundle | long_term |
| `pkg_KNOWN_ISSUE_<code>` | Known issue patterns | long_term |
| `pkg_TRAINING_<topic>` | Training/onboarding context | long_term |

---

## 3. Package Creation

```
CREATE_CONTEXT_PACKAGE(
  name="ICA_CASE_123",
  capsule_refs=["cap_SHM_01", "cap_ICA_01", "cap_ICA_02"],
  policies={
    "visibility": ["all_models"],
    "export": "allow",
    "retention": "long_term"
  }
)
```

---

## 4. Package Application

On session start or agent switch:

```
APPLY_CONTEXT_PACKAGE(
  session_id="session_XYZ",
  package_id="pkg_AIRCRAFT_ARCH",
  mode="read_only"
)
```

This is automatically invoked on model/session shifts per MMIP default behaviour.

---

## 5. Document Control

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT** – Subject to human review and approval.
- Human approver: _[to be completed]_.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: 2025-11-28.

---
