# ATA 22 Auto Flight Interface

## Document Control

| Field | Value |
|-------|-------|
| **Document ID** | OFEC-97-40-40-IF22-001 |
| **Version** | 1.0 |
| **Status** | DRAFT |

---

## 1. Interface Overview

This document defines the interface between Envelope Analytics (97-40-40) and the Auto Flight system (ATA 22).

### 1.1 Purpose

The Auto Flight interface provides:
- Current flight phase information
- Autopilot mode and engagement status
- Target parameters for envelope prediction

---

## 2. Data Exchange

### 2.1 Auto Flight → Envelope Analytics

| Parameter | Type | Unit | Range | Rate | Usage |
|-----------|------|------|-------|------|-------|
| flight_phase | enum | - | 0-7 | 1 Hz | Phase-aware publishing |
| autopilot_engaged | bool | - | T/F | 1 Hz | Mode context |
| autothrottle_engaged | bool | - | T/F | 1 Hz | Speed control context |
| flight_director_mode | enum | - | See §2.1.1 | 1 Hz | Advisory context |
| target_speed | float32 | kts | 0-500 | 1 Hz | Predictive dynamics |
| target_altitude | float32 | ft | 0-50000 | 1 Hz | Predictive dynamics |
| target_heading | float32 | deg | 0-360 | 1 Hz | Trend analysis |

#### 2.1.1 Flight Director Modes

| Value | Mode | Description |
|-------|------|-------------|
| 0 | OFF | Flight director off |
| 1 | HDG | Heading select |
| 2 | NAV | Navigation mode |
| 3 | APP | Approach mode |
| 4 | GA | Go-around |
| 5 | ALT_HLD | Altitude hold |
| 6 | V/S | Vertical speed |
| 7 | FLCH | Flight level change |

### 2.2 Envelope Analytics → Auto Flight

| Parameter | Type | Description |
|-----------|------|-------------|
| envelope_advisory | enum | Current advisory level |
| margin_status | bitfield | Per-margin status flags |
| trend_direction | enum | IMPROVING/STABLE/DEGRADING |

---

## 3. Integration with Autopilot Protection

### 3.1 Relationship to Primary Protections

```
┌─────────────────────────────────────────────────┐
│           AUTO FLIGHT SYSTEM (ATA 22)           │
├─────────────────────────────────────────────────┤
│                                                 │
│  ┌──────────────────┐   ┌──────────────────┐   │
│  │  Primary Flight  │   │  Envelope        │   │
│  │  Protections     │   │  Analytics       │   │
│  │  (Safety-Critical)   │  (Advisory)      │   │
│  │                  │   │                  │   │
│  │  • Alpha Floor   │◄──│  • α Margin      │   │
│  │  • Speed Limit   │   │  • Speed Margin  │   │
│  │  • Bank Limit    │   │  • G-load Margin │   │
│  │  • G-limit       │   │  • Trend Data    │   │
│  └──────────────────┘   └──────────────────┘   │
│         │                       │              │
│         ▼                       ▼              │
│  Commands to                Telemetry to       │
│  Flight Controls            Ground             │
│                                                 │
└─────────────────────────────────────────────────┘
```

### 3.2 Independence

- Envelope Analytics operates **independently** from primary protections
- Primary protections are safety-critical (DAL A/B)
- Envelope Analytics is advisory (DAL D)
- No bidirectional control dependencies

---

## 4. Message Format

### 4.1 Auto Flight Status Message

```json
{
  "source": "ATA22_AUTOFLIGHT",
  "timestamp": "2025-11-28T12:00:00.000Z",
  "flight_phase": 4,
  "autopilot": {
    "engaged": true,
    "mode": "NAV"
  },
  "autothrottle": {
    "engaged": true,
    "mode": "SPEED"
  },
  "targets": {
    "speed_kts": 280,
    "altitude_ft": 35000,
    "heading_deg": 270
  }
}
```

---

## Document Control

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT** – Subject to human review and approval.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: _2025-11-28_.
