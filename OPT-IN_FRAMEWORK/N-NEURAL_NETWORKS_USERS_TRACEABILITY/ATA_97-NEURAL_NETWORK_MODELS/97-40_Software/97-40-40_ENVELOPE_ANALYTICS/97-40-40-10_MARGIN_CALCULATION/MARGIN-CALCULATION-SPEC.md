# Margin Calculation Specification

## Document Control

| Field | Value |
|-------|-------|
| **Document ID** | OFEC-97-40-40-10-SPEC-001 |
| **Version** | 1.0 |
| **Status** | DRAFT |

---

## 1. Overview

The Margin Calculation module (97-40-40-10) computes real-time flight envelope margins for all critical parameters.

---

## 2. Margin Types

### 2.1 Alpha Margin (Angle of Attack)

| Parameter | Description |
|-----------|-------------|
| Input | Current AOA, configuration, Mach, altitude |
| Output | Margin in degrees and percentage |
| Update Rate | 10-50 Hz |
| Accuracy | ±0.1° |

### 2.2 Speed Margin

| Parameter | Description |
|-----------|-------------|
| Input | CAS, Mach, configuration, altitude |
| Output | Low margin (Vmin), high margin (Vmax) |
| Update Rate | 10-50 Hz |
| Accuracy | ±1 kt |

### 2.3 Load Factor Margin

| Parameter | Description |
|-----------|-------------|
| Input | Current G-load, configuration |
| Output | Positive and negative margins |
| Update Rate | 50 Hz |
| Accuracy | ±0.01 g |

### 2.4 Altitude Margin

| Parameter | Description |
|-----------|-------------|
| Input | Current altitude, aircraft weight, temperature |
| Output | Margin to service ceiling |
| Update Rate | 1 Hz |
| Accuracy | ±100 ft |

### 2.5 Bank Angle Margin

| Parameter | Description |
|-----------|-------------|
| Input | Current bank angle, configuration, speed |
| Output | Margin to bank limit |
| Update Rate | 10 Hz |
| Accuracy | ±0.5° |

---

## 3. Calculation Methods

### 3.1 Margin Formula

For all margin types:

```
margin_absolute = limit - current_value
margin_percentage = (margin_absolute / limit) × 100
```

### 3.2 Sign Convention

| Condition | Margin Value |
|-----------|--------------|
| Within envelope | Positive |
| At limit | Zero |
| Exceeded | Negative |

---

## 4. Configuration Dependency

All margins are configuration-dependent:

| Configuration | Affects |
|---------------|---------|
| Flap position | Vmin, α limit |
| Slat position | α limit |
| Gear position | Vmax, drag |
| Weight | All margins |
| CG position | α limit |

---

## 5. Files

| File | Purpose |
|------|---------|
| margin_calculator.py | Main calculator class |
| alpha_margin.py | AOA margin calculation |
| speed_margin.py | Speed margins |
| load_factor_margin.py | G-load margins |
| altitude_margin.py | Altitude margin |
| bank_angle_margin.py | Bank angle margin |
| MARGIN-THRESHOLDS.yaml | Threshold configuration |

---

## Document Control

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT** – Subject to human review and approval.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: _2025-11-28_.
