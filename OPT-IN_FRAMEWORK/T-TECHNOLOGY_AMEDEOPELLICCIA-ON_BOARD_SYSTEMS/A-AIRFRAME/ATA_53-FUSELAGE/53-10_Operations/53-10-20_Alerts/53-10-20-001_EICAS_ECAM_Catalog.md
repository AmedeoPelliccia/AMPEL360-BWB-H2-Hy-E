# 53-10-20-001 — EICAS/ECAM Catalog

| Field | Value |
|-------|-------|
| **Document ID** | 53-10-20-001 |
| **Version** | 1.0 |
| **Date** | 2025-11-27 |
| **Status** | DRAFT |
| **Classification** | OPERATIONAL |

---

## 1. Purpose

This document catalogs all EICAS/ECAM messages for ANCHORS systems.

## 2. Scope

Applicable to all ANCHORS-related crew alerts.

## 3. Message Catalog

| Level | Message | Condition | Action |
|-------|---------|-----------|--------|
| **WARNING** | ANCHORS BATT FIRE | Thermal runaway detected | [Emergency proc](../53-10-04_Emergency_Procedures/53-10-04-001_ANCHORS_BATT_FIRE.md) |
| **WARNING** | ANCHORS CO2 LEAK | CO₂ in cabin > limit | [Emergency proc](../53-10-04_Emergency_Procedures/53-10-04-003_ANCHORS_CO2_LEAK.md) |
| **CAUTION** | ANCHORS BATT TEMP HI | Pack > 50°C | [Abnormal proc](../53-10-03_Abnormal_Procedures/53-10-03-001_ANCHORS_BATT_TEMP_HI.md) |
| **CAUTION** | ANCHORS BATT ISOL | Pack isolated | Reduced capacity |
| **CAUTION** | ANCHORS CO2 SYS FAULT | Capture system fault | [Abnormal proc](../53-10-03_Abnormal_Procedures/53-10-03-002_ANCHORS_CO2_SYS_FAULT.md) |
| **CAUTION** | ANCHORS BAY PRESS LOW | Bay pressure loss | [Abnormal proc](../53-10-04_Emergency_Procedures/53-10-04-002_ANCHORS_BAY_PRESS_LOW.md) |
| **ADVISORY** | ANCHORS CART FULL | Cartridge > 90% | Plan swap |
| **ADVISORY** | ANCHORS BATT LOW | SoC < 20% | Monitor |
| **ADVISORY** | ANCHORS DPP SYNC | Offline > 24 hr | Ground sync |
| **ADVISORY** | ANCHORS HARVEST LOW | Generation < 1 kW | Normal (night) |
| **ADVISORY** | ANCHORS DEGRADED | System in degraded mode | Monitor |
| **STATUS** | ANCHORS STBY | System in standby | — |
| **STATUS** | ANCHORS ECO | Economy mode active | — |

## 4. Alert Logic

```mermaid
flowchart TB
    subgraph SENSORS["SENSOR INPUTS"]
        S1["Battery Temp"]
        S2["Battery SoC"]
        S3["CO₂ Sensors"]
        S4["Pressure"]
        S5["Smoke Detect"]
    end
    
    subgraph LOGIC["ALERT LOGIC (53-30-95)"]
        L1["Threshold<br/>Comparison"]
        L2["Trend<br/>Analysis"]
        L3["Multi-Sensor<br/>Voting"]
    end
    
    subgraph ALERTS["ALERT GENERATION"]
        A1["WARNING<br/>(Red)"]
        A2["CAUTION<br/>(Amber)"]
        A3["ADVISORY<br/>(Blue/White)"]
    end
    
    subgraph DISPLAY["CREW DISPLAY"]
        D1["EICAS/ECAM"]
        D2["Master Warning"]
        D3["Aural Alert"]
    end
    
    S1 & S2 & S3 & S4 & S5 --> L1 & L2 & L3
    L1 & L2 & L3 --> A1 & A2 & A3
    A1 --> D1 & D2 & D3
    A2 --> D1 & D2
    A3 --> D1
    
    style SENSORS fill:#e3f2fd,stroke:#1565c0
    style LOGIC fill:#fff9c4,stroke:#f9a825
    style ALERTS fill:#ffcdd2,stroke:#c62828
    style DISPLAY fill:#c8e6c9,stroke:#2e7d32
```

## 5. Related Documents

- [53-10-21-001_ANCHORS_System_Page.md](../53-10-21_Displays/53-10-21-001_ANCHORS_System_Page.md) — System page display
- [53-10-22-001_ANCHORS_Panel_Operations.md](../53-10-22_Controls/53-10-22-001_ANCHORS_Panel_Operations.md) — Panel operations

---

## Document Control

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT** – Subject to human review and approval.
- Human approver: _[to be completed]_.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: 2025-11-27.

---

*END OF DOCUMENT*
