# ATA 34 Navigation Interface

## Document Control

| Field | Value |
|-------|-------|
| **Document ID** | OFEC-97-40-40-IF34-001 |
| **Version** | 1.0 |
| **Status** | DRAFT |

---

## 1. Interface Overview

This document defines the interface between Envelope Analytics (97-40-40) and Navigation Systems (ATA 34).

### 1.1 Purpose

The Navigation interface provides:
- Primary air data (airspeed, altitude, Mach)
- Attitude data (pitch, roll, yaw)
- Angle of attack measurements
- Position and flight path data

---

## 2. Data Exchange

### 2.1 Air Data Parameters

| Parameter | Type | Unit | Range | Rate | Source |
|-----------|------|------|-------|------|--------|
| angle_of_attack | float32 | deg | -20 to +40 | 50 Hz | AOA vane |
| sideslip_angle | float32 | deg | -30 to +30 | 50 Hz | Sideslip vane |
| indicated_airspeed | float32 | kts | 0 to 500 | 50 Hz | Pitot-static |
| calibrated_airspeed | float32 | kts | 0 to 500 | 50 Hz | Computed |
| true_airspeed | float32 | kts | 0 to 600 | 50 Hz | Computed |
| mach_number | float32 | ratio | 0 to 1.2 | 50 Hz | Computed |
| pressure_altitude | float32 | ft | -1000 to 60000 | 50 Hz | Pitot-static |
| baro_corrected_alt | float32 | ft | -1000 to 60000 | 50 Hz | Computed |
| radio_altitude | float32 | ft | 0 to 5000 | 10 Hz | Radar altimeter |
| vertical_speed | float32 | ft/min | -10000 to +10000 | 25 Hz | Computed |
| total_air_temp | float32 | °C | -80 to +60 | 10 Hz | TAT probe |
| static_air_temp | float32 | °C | -80 to +60 | 10 Hz | Computed |

### 2.2 Attitude Parameters

| Parameter | Type | Unit | Range | Rate | Source |
|-----------|------|------|-------|------|--------|
| pitch_angle | float32 | deg | -30 to +60 | 50 Hz | AHRS |
| roll_angle | float32 | deg | -180 to +180 | 50 Hz | AHRS |
| heading_magnetic | float32 | deg | 0 to 360 | 50 Hz | AHRS |
| heading_true | float32 | deg | 0 to 360 | 50 Hz | Computed |
| pitch_rate | float32 | deg/s | -30 to +30 | 50 Hz | Rate gyros |
| roll_rate | float32 | deg/s | -60 to +60 | 50 Hz | Rate gyros |
| yaw_rate | float32 | deg/s | -30 to +30 | 50 Hz | Rate gyros |

### 2.3 Position Parameters

| Parameter | Type | Unit | Range | Rate | Source |
|-----------|------|------|-------|------|--------|
| latitude | float64 | deg | -90 to +90 | 10 Hz | GPS/INS |
| longitude | float64 | deg | -180 to +180 | 10 Hz | GPS/INS |
| ground_speed | float32 | kts | 0 to 600 | 10 Hz | GPS/INS |
| track_angle | float32 | deg | 0 to 360 | 10 Hz | GPS/INS |
| wind_speed | float32 | kts | 0 to 200 | 1 Hz | Computed |
| wind_direction | float32 | deg | 0 to 360 | 1 Hz | Computed |

---

## 3. Angle of Attack Processing

### 3.1 AOA Measurement

```
                          ▲ Relative Wind
                         ╱
                        ╱
    ─────────────────────────────────── Chord Line
                       α
                        ╲
                         ╲
                          ▼ Lift Vector
```

### 3.2 Alpha Margin Calculation

The α margin is calculated as:

```python
def calculate_alpha_margin(aoa_current, config, mach, altitude):
    # Get stall α from aerodynamic model
    alpha_stall = aero_model.get_stall_alpha(config, mach, altitude)
    
    # Apply safety margin
    alpha_limit = alpha_stall - SAFETY_MARGIN_DEG  # Typically 2-3 deg
    
    # Calculate margin
    margin_deg = alpha_limit - aoa_current
    margin_pct = (margin_deg / alpha_limit) * 100
    
    return {
        "current_deg": aoa_current,
        "limit_deg": alpha_limit,
        "margin_deg": margin_deg,
        "margin_pct": margin_pct
    }
```

---

## 4. Speed Envelope

### 4.1 V-Speed Definitions

| V-Speed | Description | Source |
|---------|-------------|--------|
| V<sub>S0</sub> | Stall speed, landing config | AFM |
| V<sub>S1</sub> | Stall speed, clean config | AFM |
| V<sub>min</sub> | Minimum operating speed | Computed |
| V<sub>mo</sub> | Maximum operating speed | AFM |
| M<sub>mo</sub> | Maximum operating Mach | AFM |
| V<sub>ne</sub> | Never exceed speed | AFM |

### 4.2 Speed Margin Calculation

```python
def calculate_speed_margins(cas, mach, config, altitude):
    # Get speed limits
    v_min = get_vmin(config, altitude)
    v_max = min(get_vmo(), mach_to_cas(get_mmo(), altitude))
    
    # Calculate margins
    margin_low = cas - v_min
    margin_high = v_max - cas
    
    return {
        "current_kts": cas,
        "vmin_kts": v_min,
        "vmax_kts": v_max,
        "margin_low_kts": margin_low,
        "margin_high_kts": margin_high,
        "margin_low_pct": (margin_low / (cas - 0)) * 100,
        "margin_high_pct": (margin_high / v_max) * 100
    }
```

---

## 5. Data Quality

### 5.1 Sensor Validity

| Sensor | Redundancy | Voting | Fallback |
|--------|------------|--------|----------|
| AOA vane | Triple | 2-of-3 | Last valid |
| Pitot-static | Triple | 2-of-3 | GPS backup |
| AHRS | Triple | 2-of-3 | Degraded mode |
| GPS | Dual | Best | INS only |

### 5.2 Validity Flags

Each parameter includes:
- `validity`: VALID / INVALID / STALE / TEST
- `source`: PRIMARY / BACKUP / COMPUTED
- `accuracy`: Estimated accuracy class

---

## 6. Message Format

### 6.1 Navigation Data Message

```json
{
  "source": "ATA34_NAVIGATION",
  "timestamp": "2025-11-28T12:00:00.000Z",
  "air_data": {
    "aoa_deg": 4.2,
    "ias_kts": 245,
    "cas_kts": 248,
    "tas_kts": 420,
    "mach": 0.72,
    "altitude_ft": 35000,
    "vs_fpm": -50
  },
  "attitude": {
    "pitch_deg": 2.5,
    "roll_deg": 0.3,
    "heading_mag_deg": 270
  },
  "validity": {
    "air_data": "VALID",
    "attitude": "VALID"
  }
}
```

---

## Document Control

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT** – Subject to human review and approval.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: _2025-11-28_.
