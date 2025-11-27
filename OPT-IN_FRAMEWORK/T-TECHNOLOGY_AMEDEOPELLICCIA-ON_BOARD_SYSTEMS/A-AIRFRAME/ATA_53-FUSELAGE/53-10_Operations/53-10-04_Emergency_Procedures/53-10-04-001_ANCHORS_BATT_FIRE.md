# 53-10-04-001 — ANCHORS BATT FIRE

| Field | Value |
|-------|-------|
| **Document ID** | 53-10-04-001 |
| **Version** | 1.0 |
| **Date** | 2025-11-27 |
| **Status** | DRAFT |
| **Classification** | OPERATIONAL — EMERGENCY |

---

## 1. Purpose

This procedure defines the crew response to ANCHORS battery thermal runaway (fire) emergency.

## 2. ECAM/EICAS Message

**Message:** `ANCHORS BATT FIRE`
**Level:** WARNING (Red)
**Trigger:** Thermal runaway detected in battery pack

## 3. Emergency Procedure

| Step | Action | Notes |
|------|--------|-------|
| 1 | **ANCHORS MASTER — OFF** | Immediate isolation |
| 2 | **ANCHORS FIRE AGENT — DISCH** | If equipped |
| 3 | **Smoke/fumes — Crew O₂** | Protect crew |
| 4 | **Packs — Vent overboard** | Auto-activates |
| 5 | **Consider diversion** | Per SOP |
| 6 | **Notify cabin crew** | Prepare passengers |
| 7 | **Land ASAP** | Do not delay |

## 4. Memory Items

> **ANCHORS BATT FIRE**
> 1. ANCHORS MASTER .......... OFF
> 2. ANCHORS FIRE AGENT ...... DISCH (if equipped)
> 3. Crew O₂ ................ ON (if smoke/fumes)

## 5. Decision Factors

- Aircraft position relative to suitable airports
- Rate of temperature rise
- Smoke/fumes in cabin or cockpit
- Passenger count and special needs

## 6. Cautions

⚠️ **Do not attempt reset once thermal runaway confirmed**
⚠️ **Battery fire may propagate; monitor adjacent packs**
⚠️ **Prepare cabin for possible emergency landing**

## 7. Related Documents

- [53-10-03-001_ANCHORS_BATT_TEMP_HI.md](../53-10-03_Abnormal_Procedures/53-10-03-001_ANCHORS_BATT_TEMP_HI.md) — High temp caution
- 53-30-00-02_Thermal_Runaway_Mitigation.md — Design mitigations

---

## Document Control

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT** – Subject to human review and approval.
- Human approver: _[to be completed]_.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: 2025-11-27.

---

*END OF DOCUMENT*
