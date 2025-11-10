# Landing Performance Analysis

**Analysis ID:** 02-11-00-PERF-003  
**Platform:** AMPEL360 BWB H₂ Hy-E Q100  
**Analysis Type:** Performance - Landing  
**Status:** Planned  
**Date:** 2025-11-10

---

## 1. Objective

Calculate landing performance to:
- Verify landing field length < 2,500 m
- Determine approach speed (Vapp)
- Assess landing distance and braking performance
- Demonstrate compliance with CS-25 landing requirements

---

## 2. Requirements

### 2.1 Landing Field Length (CS-25.125)
- **Target:** < 2,500 m (at MLW, ISA, sea level)
- **Definition:** Distance from 50 ft screen height to full stop

### 2.2 Approach Speed (CS-25.125)
- **Vapp:** ≥ 1.23 × VS (landing configuration)
- **VREF:** Reference landing speed = 1.23 × VS

### 2.3 Climb Gradient (Go-Around, CS-25.119)
- **All engines:** > 3.2%
- **Configuration:** Landing flaps, gear down
- **Speed:** VREF

---

## 3. Landing Configuration

### 3.1 Aircraft State
- **Weight:** MLW = 190,000 kg
- **Flap setting:** 30° (landing flaps)
- **Gear:** Down
- **CLmax (Landing):** TBD (target: ≥ 2.4)

### 3.2 Environmental Conditions
- **Altitude:** Sea level (0 ft)
- **Temperature:** ISA (15°C, 288.15 K)
- **Runway:** Dry, paved, level
- **Wind:** Calm

---

## 4. Landing Speeds

| Speed | Value (KIAS) | Formula | Notes |
|-------|--------------|---------|-------|
| VS (stall, landing flaps) | TBD | √(2W/(ρSCLmax)) | Stall speed |
| VREF (reference) | TBD | 1.23 × VS | Reference speed |
| Vapp (approach) | TBD | VREF + wind correction | Approach speed |
| Vtd (touchdown) | TBD | ≈ VREF | Typical touchdown speed |

---

## 5. Landing Distance Analysis

### 5.1 Landing Distance Breakdown

| Segment | Distance (m) | Notes |
|---------|--------------|-------|
| Air distance (50 ft to touchdown) | TBD | Approach from 50 ft screen |
| Flare and touchdown | TBD | Flare maneuver |
| Free roll (no braking) | TBD | 3 seconds after touchdown |
| Braking (spoilers + wheel brakes) | TBD | Max manual braking |
| **Total landing distance** | **TBD** | **Target: < 2,500 m** |

### 5.2 Dry Runway Performance
- **Landing distance (dry):** TBD m
- **Margin to requirement:** TBD m

### 5.3 Wet Runway Performance
- **Landing distance (wet):** TBD m (typically 1.15× dry distance)

---

## 6. Deceleration Means

### 6.1 Aerodynamic Braking
- **Spoilers:** Deployed immediately at touchdown
- **Reverse thrust:** Not available (H₂ turbofan engines without reversers)
- **Drag (L/D ≈ 5):** TBD kN at VREF

### 6.2 Wheel Brakes
- **Braking coefficient (μ):** 0.4 (dry), 0.2 (wet)
- **Braking force:** TBD kN
- **Brake energy:** TBD MJ

---

## 7. Go-Around Performance

### 7.1 Go-Around Conditions
- **Weight:** MLW = 190,000 kg
- **Configuration:** Landing flaps (30°), gear down
- **Speed:** VREF
- **Thrust:** All engines at go-around thrust

### 7.2 Climb Gradient
- **All-engine climb gradient:** TBD % (requirement: > 3.2%)

---

## 8. Obstacle Clearance

### 8.1 Approach Path
- **Approach angle:** 3° (typical ILS glideslope)
- **Clearance over threshold:** 50 ft

---

## 9. Sensitivity Analysis

Impact of parameters on landing distance:

| Parameter Change | ΔLanding Distance (m) | % Change |
|------------------|-----------------------|----------|
| +10°C (hot day) | TBD | TBD % |
| +2000 ft altitude | TBD | TBD % |
| +5 kt approach speed | TBD | TBD % |
| Wet runway | TBD | +15% |

---

## 10. Crosswind Capability

### 10.1 Maximum Demonstrated Crosswind
- **Target:** ≥ 30 kt crosswind component
- **Demonstrated:** TBD kt (flight test)

---

## 11. References

- CS-25.125 – Landing
- CS-25.119 – Landing Climb: All-Engines-Operating
- `CALCULATIONS/PERFORMANCE/TO_LDG_Performance_Model.csv`
- `ANALYSIS_REPORTS/AERODYNAMIC/High_Lift_System_Analysis.md`

---

**Document Control:**
- **Version:** 1.0 (Draft)
- **Date:** 2025-11-10
