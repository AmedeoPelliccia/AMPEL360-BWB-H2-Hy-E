# Take-Off Performance Analysis

**Analysis ID:** 02-11-00-PERF-002  
**Platform:** AMPEL360 BWB H₂ Hy-E Q100  
**Analysis Type:** Performance - Take-Off  
**Status:** Planned  
**Date:** 2025-11-10

---

## 1. Objective

Calculate take-off performance to:
- Verify take-off field length < 3,000 m
- Determine V-speeds (V1, VR, V2)
- Assess take-off climb gradients
- Demonstrate compliance with CS-25 take-off requirements

---

## 2. Requirements

### 2.1 Take-Off Field Length (CS-25.105)
- **Target:** < 3,000 m (at MTOW, ISA, sea level)
- **Definition:** Distance from brake release to 35 ft screen height

### 2.2 Take-Off Speeds (CS-25.107)
- **V1:** Decision speed (go/no-go)
- **VR:** Rotation speed
- **V2:** Take-off safety speed (≥ 1.13 × VS)
- **VLOF:** Lift-off speed

### 2.3 Climb Gradients (CS-25.121)
- **First segment (all engines):** > 0%
- **Second segment (OEI):** > 2.4% (for multi-engine aircraft)
- **Final segment (all engines, flaps up):** > 1.2%

---

## 3. Take-Off Configuration

### 3.1 Aircraft State
- **Weight:** MTOW = 220,000 kg
- **Flap setting:** 20° (take-off flaps)
- **CG position:** Most forward (critical for rotation)
- **CLmax (TO):** TBD (target: ≥ 1.8)

### 3.2 Environmental Conditions
- **Altitude:** Sea level (0 ft)
- **Temperature:** ISA (15°C, 288.15 K)
- **Runway:** Dry, paved, level
- **Wind:** Calm

---

## 4. Take-Off Analysis

### 4.1 V-Speeds Calculation

| Speed | Value (KIAS) | Formula | Notes |
|-------|--------------|---------|-------|
| VS (stall, TO flaps) | TBD | √(2W/(ρSCLmax)) | Stall speed |
| VR (rotation) | TBD | 1.05 × VS | Rotation speed |
| VLOF (lift-off) | TBD | 1.10 × VS | Lift-off speed |
| V2 (safety speed) | TBD | 1.13 × VS | Climb-out speed |
| V1 (decision) | TBD | VR - margin | Go/no-go speed |

### 4.2 Take-Off Distance Breakdown

| Segment | Distance (m) | Notes |
|---------|--------------|-------|
| Ground roll (brake release to VR) | TBD | Acceleration on ground |
| Rotation (VR to VLOF) | TBD | Nose-up rotation |
| Airborne (VLOF to 35 ft screen) | TBD | Initial climb |
| **Total take-off distance** | **TBD** | **Target: < 3,000 m** |

### 4.3 Accelerate-Stop Distance
Distance to accelerate to V1, then reject take-off and stop:
- **Accelerate-stop distance:** TBD m (must be ≤ available runway length)

---

## 5. Climb Performance

### 5.1 Second Segment Climb (OEI, Critical Engine Out)

| Parameter | Value | Requirement |
|-----------|-------|-------------|
| Weight | MTOW | 220,000 kg |
| Speed | V2 | TBD KIAS |
| Flap setting | Take-off (20°) | |
| Altitude | 0 ft (sea level) | |
| Climb gradient | TBD % | > 2.4% |

### 5.2 All-Engine Climb

| Altitude (ft) | Rate of Climb (ft/min) | Gradient (%) |
|---------------|------------------------|--------------|
| 0 | TBD | TBD |
| 1,000 | TBD | TBD |
| 5,000 | TBD | TBD |

---

## 6. Obstacle Clearance

### 6.1 Take-Off Flight Path (CS-25.111)
- **Net flight path:** Gross flight path minus 0.8% (for 2-engine) or 1.1% (for 3+ engines)
- **Obstacle clearance:** 35 ft vertical at end of take-off distance

---

## 7. Sensitivity Analysis

Impact of parameters on take-off distance:

| Parameter Change | ΔTO Distance (m) | % Change |
|------------------|------------------|----------|
| +10°C (hot day) | TBD | TBD % |
| +2000 ft altitude | TBD | TBD % |
| +5% weight | TBD | TBD % |
| +0.1 CLmax | TBD | TBD % |

---

## 8. References

- CS-25.105 – Take-Off
- CS-25.107 – Take-Off Speeds
- CS-25.111 – Take-Off Path
- CS-25.121 – Climb: One-Engine-Inoperative
- `CALCULATIONS/PERFORMANCE/TO_LDG_Performance_Model.csv`
- `ANALYSIS_REPORTS/AERODYNAMIC/High_Lift_System_Analysis.md`

---

**Document Control:**
- **Version:** 1.0 (Draft)
- **Date:** 2025-11-10
