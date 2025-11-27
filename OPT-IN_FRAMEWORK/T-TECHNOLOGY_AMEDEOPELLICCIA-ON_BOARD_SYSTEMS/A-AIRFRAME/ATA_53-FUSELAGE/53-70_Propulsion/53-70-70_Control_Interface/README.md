# 53-70-70 Control Interface

| Field | Value |
|-------|-------|
| **Document ID** | 53-70-70 |
| **Version** | 1.0 |
| **Date** | 2025-11-27 |
| **Status** | DRAFT |
| **Classification** | TECHNICAL |
| **ATA Chapter** | 53-70 |

---

## Purpose

This section documents the control interface between ANCHORS systems and propulsion controllers.

## Scope

The Control Interface section covers:

- Control interface design
- Mode coordination logic
- Message dictionary for control communications
- Interface control documents for ATA 76

## Contents

### Planned Documents

| Document ID | Title | Status |
|-------------|-------|--------|
| [53-70-70-01_Control_Interface_Design.md](./53-70-70-01_Control_Interface_Design.md) | Control Interface Design | PLANNED |
| [53-70-70-02_Mode_Coordination.md](./53-70-70-02_Mode_Coordination.md) | Mode Coordination | PLANNED |
| [53-70-70-03_Message_Dictionary.md](./53-70-70-03_Message_Dictionary.md) | Message Dictionary | PLANNED |
| [53-70-70-04_ICD_76-001_Control.md](./53-70-70-04_ICD_76-001_Control.md) | ICD 76-001 Control | PLANNED |

## Control Messages Summary

| Message | Direction | Protocol | Rate |
|---------|-----------|----------|------|
| POWER_DEMAND | ANCHORS → Prop | AFDX | 10 Hz |
| POWER_AVAILABLE | Prop → ANCHORS | AFDX | 10 Hz |
| REGEN_REQUEST | ANCHORS → Prop | AFDX | 10 Hz |
| REGEN_STATUS | Prop → ANCHORS | AFDX | 10 Hz |
| THERMAL_STATUS | Prop → ANCHORS | CAN | 1 Hz |
| FAULT_STATUS | Both | AFDX | 10 Hz |

## Cross-References

- [53-70 Propulsion README](../README.md) - Parent overview
- [53-40 Software](../../53-40_Software/) - Control software
- [ATA 76 Controls](../../../../../../P-PROPULSION/) - Engine controls

---

## Document Control

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT** – Subject to human review and approval.
- Human approver: _[to be completed]_.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: 2025-11-27

---
