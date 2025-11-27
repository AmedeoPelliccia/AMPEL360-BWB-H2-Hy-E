# 53-10-04-003 — ANCHORS CO2 LEAK

| Field | Value |
|-------|-------|
| **Document ID** | 53-10-04-003 |
| **Version** | 1.0 |
| **Date** | 2025-11-27 |
| **Status** | DRAFT |
| **Classification** | OPERATIONAL — EMERGENCY |

---

## 1. Purpose

This procedure defines the crew response to CO₂ release to cabin emergency.

## 2. ECAM/EICAS Message

**Message:** `ANCHORS CO2 LEAK`
**Level:** WARNING (Red)
**Trigger:** CO₂ detected in cabin above safe threshold

## 3. Emergency Procedure

| Step | Action | Notes |
|------|--------|-------|
| 1 | **CO2 ISOL VALVE — CLOSE** | Isolate source |
| 2 | **ANCHORS CO2 — OFF** | Stop capture |
| 3 | **ECS — MAX FLOW** | Dilute CO₂ |
| 4 | **Cabin CO₂ — MONITOR** | Must stay < 5000 ppm |
| 5 | If > 5000 ppm: **Crew O₂** | Protect crew |
| 6 | **Notify cabin** | Passenger awareness |

## 4. Memory Items

> **ANCHORS CO2 LEAK**
> 1. CO2 ISOL VALVE .......... CLOSE
> 2. ANCHORS CO2 ............. OFF
> 3. ECS ..................... MAX FLOW

## 5. CO₂ Thresholds

| Level | Concentration | Effect |
|-------|---------------|--------|
| Normal | < 1000 ppm | No effect |
| Elevated | 1000–2000 ppm | Slight discomfort |
| High | 2000–5000 ppm | Headache, drowsiness |
| Dangerous | > 5000 ppm | O₂ required, consider descent |

## 6. Cautions

⚠️ **High CO₂ can cause incapacitation without warning**
⚠️ **Prioritize crew protection — don O₂ early if in doubt**
⚠️ **ECS max flow will dilute CO₂ but takes time**

## 7. Related Documents

- [53-10-03-002_ANCHORS_CO2_SYS_FAULT.md](../53-10-03_Abnormal_Procedures/53-10-03-002_ANCHORS_CO2_SYS_FAULT.md) — System fault
- 53-30-00-02_H2_CO2_Safety_Provisions.md — Safety provisions

---

## Document Control

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT** – Subject to human review and approval.
- Human approver: _[to be completed]_.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: 2025-11-27.

---

*END OF DOCUMENT*
