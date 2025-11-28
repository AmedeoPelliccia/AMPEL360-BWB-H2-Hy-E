# Envelope Analytics Interface Control Document

## Document Control

| Field | Value |
|-------|-------|
| **Document ID** | OFEC-97-40-40-ICD-001 |
| **Version** | 1.0 |
| **Status** | DRAFT |

---

## 1. Overview

This document defines the interfaces for the Envelope Analytics subsystem (ATA 97-40-40).

---

## 2. Input Interfaces

### 2.1 Navigation Data (ATA 34)

| Parameter | Type | Unit | Range | Rate |
|-----------|------|------|-------|------|
| angle_of_attack | float32 | degrees | -20 to +40 | 50 Hz |
| indicated_airspeed | float32 | knots | 0 to 500 | 50 Hz |
| true_airspeed | float32 | knots | 0 to 600 | 50 Hz |
| altitude_pressure | float32 | feet | -1000 to 60000 | 50 Hz |
| altitude_radio | float32 | feet | 0 to 5000 | 10 Hz |
| vertical_speed | float32 | ft/min | -10000 to +10000 | 25 Hz |
| mach_number | float32 | ratio | 0 to 1.2 | 50 Hz |
| pitch_angle | float32 | degrees | -30 to +60 | 50 Hz |
| roll_angle | float32 | degrees | -180 to +180 | 50 Hz |

### 2.2 Flight Controls Data (ATA 27)

| Parameter | Type | Unit | Range | Rate |
|-----------|------|------|-------|------|
| flap_position | float32 | degrees | 0 to 40 | 10 Hz |
| slat_position | float32 | degrees | 0 to 25 | 10 Hz |
| gear_position | enum | - | UP/DOWN/TRANS | 1 Hz |
| speedbrake_position | float32 | percent | 0 to 100 | 10 Hz |
| load_factor_normal | float32 | g | -3 to +5 | 50 Hz |
| load_factor_lateral | float32 | g | -2 to +2 | 50 Hz |

### 2.3 Auto Flight Data (ATA 22)

| Parameter | Type | Unit | Range | Rate |
|-----------|------|------|-------|------|
| autopilot_mode | enum | - | OFF/CMD/CWS | 1 Hz |
| flight_phase | enum | - | See §2.3.1 | 1 Hz |
| speed_target | float32 | knots | 0 to 500 | 1 Hz |
| altitude_target | float32 | feet | 0 to 50000 | 1 Hz |

#### 2.3.1 Flight Phase Enumeration

| Value | Phase |
|-------|-------|
| 0 | GROUND |
| 1 | TAXI |
| 2 | TAKEOFF |
| 3 | CLIMB |
| 4 | CRUISE |
| 5 | DESCENT |
| 6 | APPROACH |
| 7 | LANDING |

### 2.4 H₂ Fuel Data (ATA 28)

| Parameter | Type | Unit | Range | Rate |
|-----------|------|------|-------|------|
| fuel_temperature | float32 | Kelvin | 15 to 35 | 1 Hz |
| tank_pressure | float32 | bar | 0 to 10 | 1 Hz |
| boil_off_rate | float32 | kg/hr | 0 to 10 | 0.1 Hz |
| fuel_quantity | float32 | kg | 0 to 10000 | 1 Hz |

---

## 3. Output Interfaces

### 3.1 OFEC Telemetry

See [envelope_state.schema.json](../97-40-40-90_SCHEMAS/envelope_state.schema.json) for complete schema.

| Field | Type | Description |
|-------|------|-------------|
| envelope_id | uuid | Unique message ID |
| aircraft_id | string | Aircraft MSN |
| timestamp | ISO8601 | UTC timestamp |
| flight_phase | enum | Current phase |
| margins | object | All margin values |
| h2_specific | object | H₂ constraints |
| advisory | object | Advisory state |
| metadata | object | Message metadata |

### 3.2 CAOS Events

| Event Type | Trigger | Data |
|------------|---------|------|
| EXCEEDANCE | Margin < 0 | Parameter, value, limit |
| WARNING | Margin < warning_threshold | Parameter, value, margin |
| RECOVERY | Margin returns to normal | Parameter, new margin |

### 3.3 DPP Records

| Record Type | Frequency | Content |
|-------------|-----------|---------|
| FLIGHT_SUMMARY | Per flight | Statistics, events |
| EXCEEDANCE_LOG | Per event | Full exceedance data |
| PERFORMANCE_TREND | Daily | Fleet-wide trends |

---

## 4. Data Quality

### 4.1 Validity Flags

Each input parameter includes a validity flag:

| Flag | Value | Meaning |
|------|-------|---------|
| VALID | 0 | Data is good |
| INVALID | 1 | Data failed checks |
| STALE | 2 | Data not updated |
| UNKNOWN | 3 | Status unknown |

### 4.2 Fault Detection

| Check | Method | Action |
|-------|--------|--------|
| Range check | Compare to limits | Mark invalid |
| Rate check | Compare to max rate | Mark suspect |
| Consistency | Cross-check sources | Flag discrepancy |

---

## Document Control

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT** – Subject to human review and approval.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: _2025-11-28_.
