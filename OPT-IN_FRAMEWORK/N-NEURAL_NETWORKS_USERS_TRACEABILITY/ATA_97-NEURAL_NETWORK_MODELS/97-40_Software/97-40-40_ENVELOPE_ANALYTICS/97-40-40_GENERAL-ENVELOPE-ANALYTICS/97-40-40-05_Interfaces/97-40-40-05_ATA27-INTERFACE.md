# ATA 27 Flight Controls Interface

## Document Control

| Field | Value |
|-------|-------|
| **Document ID** | OFEC-97-40-40-IF27-001 |
| **Version** | 1.0 |
| **Status** | DRAFT |

---

## 1. Interface Overview

This document defines the interface between Envelope Analytics (97-40-40) and Flight Controls (ATA 27).

### 1.1 Purpose

The Flight Controls interface provides:
- Control surface positions for load analysis
- Configuration state (flaps, slats, gear)
- Load factor measurements
- Stall warning status

---

## 2. Data Exchange

### 2.1 Flight Controls → Envelope Analytics

| Parameter | Type | Unit | Range | Rate | Usage |
|-----------|------|------|-------|------|-------|
| flap_position | float32 | deg | 0-40 | 10 Hz | Config envelope |
| slat_position | float32 | deg | 0-25 | 10 Hz | Config envelope |
| gear_position | enum | - | UP/DOWN/TRANS | 1 Hz | Speed limits |
| speedbrake_deployed | bool | - | T/F | 10 Hz | Drag awareness |
| load_factor_z | float32 | g | -3 to +5 | 50 Hz | G-load margin |
| load_factor_y | float32 | g | -2 to +2 | 50 Hz | Lateral loads |
| stall_warning_active | bool | - | T/F | 50 Hz | Envelope context |
| stick_shaker_active | bool | - | T/F | 50 Hz | Stall proximity |
| alpha_floor_active | bool | - | T/F | 50 Hz | Protection status |

### 2.2 Configuration Envelope Impact

| Configuration | Vmin Impact | Vmax Impact | α Limit Impact |
|---------------|-------------|-------------|----------------|
| Flaps 0 (clean) | Highest | Highest | Lowest |
| Flaps 1 | Reduced | Reduced | Increased |
| Flaps 5 | Reduced | Reduced | Increased |
| Flaps FULL | Lowest | Lowest | Highest |
| Gear DOWN | +5 kts | -50 kts | No change |

---

## 3. Load Factor Monitoring

### 3.1 Normal Load Factor (G-load)

```
        +2.5g ─────────────────── Positive Limit
              │
        +1.0g ─────────────────── Level Flight
              │
         0.0g ─────────────────── Zero-G
              │
        -1.0g ─────────────────── Negative Limit
```

### 3.2 Load Factor Margin Calculation

```python
def calculate_load_factor_margin(current_g, config):
    limit_pos = get_positive_limit(config)
    limit_neg = get_negative_limit(config)
    
    margin_pos = limit_pos - current_g
    margin_neg = current_g - limit_neg
    
    return {
        "margin_positive_g": margin_pos,
        "margin_negative_g": margin_neg,
        "margin_positive_pct": (margin_pos / limit_pos) * 100,
        "margin_negative_pct": (margin_neg / abs(limit_neg)) * 100
    }
```

---

## 4. Stall Protection Interface

### 4.1 Stall Warning Cascade

| Level | Indication | α Proximity |
|-------|------------|-------------|
| 0 | None | > 5° from stall |
| 1 | Aural tone | 3-5° from stall |
| 2 | Stick shaker | 1-3° from stall |
| 3 | Alpha floor | At protection limit |

### 4.2 Integration with Envelope Analytics

- Stall warning status informs advisory level
- Envelope Analytics **does not duplicate** stall protection
- Provides **context** and **trend** information

---

## 5. Message Format

### 5.1 Flight Controls Status Message

```json
{
  "source": "ATA27_FLIGHT_CONTROLS",
  "timestamp": "2025-11-28T12:00:00.000Z",
  "configuration": {
    "flap_deg": 0,
    "slat_deg": 0,
    "gear": "UP",
    "speedbrake_pct": 0
  },
  "load_factor": {
    "normal_g": 1.02,
    "lateral_g": 0.01
  },
  "protections": {
    "stall_warning": false,
    "stick_shaker": false,
    "alpha_floor": false
  }
}
```

---

## Document Control

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT** – Subject to human review and approval.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: _2025-11-28_.
