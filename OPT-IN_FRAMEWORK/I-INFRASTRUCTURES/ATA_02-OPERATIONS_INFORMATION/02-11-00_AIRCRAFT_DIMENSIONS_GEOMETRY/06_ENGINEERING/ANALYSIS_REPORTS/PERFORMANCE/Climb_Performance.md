# Climb Performance Analysis

**Analysis ID:** 02-11-00-PERF-004  
**Platform:** AMPEL360 BWB H₂ Hy-E Q100  
**Analysis Type:** Performance - Climb  
**Status:** Planned  
**Date:** 2025-11-10

---

## 1. Objective

Calculate climb performance to:
- Determine time to climb to cruise altitude
- Assess climb gradients at various weights and altitudes
- Verify compliance with CS-25 climb requirements
- Support mission planning and fuel burn calculations

---

## 2. Climb Requirements (CS-25)

### 2.1 CS-25.121 – Climb: One-Engine-Inoperative (OEI)
- **Second segment (TO flaps, gear up):** > 2.4% (for 2 or 3 engines)
- **En-route (clean config):** > 1.2%
- **Approach (landing flaps, gear down):** > 2.1% (for 2 or 3 engines)

### 2.2 CS-25.119 – Landing Climb (All Engines)
- **Landing configuration:** > 3.2%

---

## 3. Climb Profile

### 3.1 Normal Climb (All Engines Operating)

**Climb Segments:**
1. **Initial climb:** Sea level to 10,000 ft (250 KIAS limit)
2. **Intermediate climb:** 10,000 ft to transition altitude (280 KIAS)
3. **High-altitude climb:** Transition altitude to cruise (constant Mach 0.78)

### 3.2 Climb Schedule

| Altitude (ft) | Speed (KIAS/Mach) | Rate of Climb (ft/min) | Time (min) | Fuel Burn (kg) |
|---------------|-------------------|------------------------|------------|----------------|
| 0 | 250 | TBD | - | - |
| 5,000 | 250 | TBD | TBD | TBD |
| 10,000 | 280 | TBD | TBD | TBD |
| 15,000 | 300 / M0.78 | TBD | TBD | TBD |
| 20,000 | M0.78 | TBD | TBD | TBD |
| 25,000 | M0.78 | TBD | TBD | TBD |
| 30,000 | M0.78 | TBD | TBD | TBD |
| 35,000 | M0.78 | TBD | TBD | TBD |
| 41,000 | M0.78 | TBD | TBD | TBD |
| **Total** | | | **TBD** | **TBD** |

---

## 4. Climb Performance Results

### 4.1 Time and Fuel to Altitude (MTOW)

| To Altitude (ft) | Time (min) | Distance (km) | Fuel Burn (kg) |
|------------------|------------|---------------|----------------|
| 10,000 | TBD | TBD | TBD |
| 20,000 | TBD | TBD | TBD |
| 30,000 | TBD | TBD | TBD |
| 41,000 (cruise) | TBD | TBD | TBD |

### 4.2 Maximum Altitude Capability
- **Service ceiling:** TBD ft (at MLW)
- **Absolute ceiling:** TBD ft (zero rate of climb)

---

## 5. One-Engine-Inoperative (OEI) Climb

### 5.1 Second Segment Climb (CS-25.121)

**Conditions:**
- Weight: MTOW
- Configuration: Take-off flaps (20°), gear up
- Speed: V2
- One engine inoperative

**Results:**
- **Climb gradient:** TBD % (requirement: > 2.4%)

### 5.2 En-Route OEI Climb (CS-25.121)

**Conditions:**
- Weight: Average cruise weight
- Configuration: Clean (flaps up, gear up)
- Altitude: 10,000 ft
- Speed: Best climb speed

**Results:**
- **Climb gradient:** TBD % (requirement: > 1.2%)

---

## 6. Drift-Down Analysis (Engine Failure at Cruise)

### 6.1 Scenario
- **Initial altitude:** 41,000 ft (cruise)
- **Engine failure:** Critical engine fails
- **Action:** Descend to OEI service ceiling

### 6.2 Drift-Down Profile

| Time (min) | Altitude (ft) | Speed (KIAS) | Distance (km) |
|------------|---------------|--------------|---------------|
| 0 | 41,000 | TBD | 0 |
| 5 | TBD | TBD | TBD |
| 10 | TBD | TBD | TBD |
| 15 | TBD | TBD | TBD |

**OEI service ceiling:** TBD ft

---

## 7. Step Climb Strategy

### 7.1 Purpose
Maintain optimal cruise altitude as aircraft weight decreases due to fuel burn.

### 7.2 Step Climb Schedule

| Weight (kg) | Optimal Cruise Altitude (ft) | Time into Cruise (hr) |
|-------------|------------------------------|----------------------|
| 220,000 (MTOW) | 39,000 | 0 |
| 200,000 | 41,000 | TBD |
| 180,000 | 43,000 | TBD |

---

## 8. References

- CS-25.119 – Landing Climb
- CS-25.121 – Climb: One-Engine-Inoperative
- `SIMULATIONS/FLIGHT_MECHANICS/q100_climb_descent.slx`
- `CALCULATIONS/PERFORMANCE/Breguet_Range_Model.csv`
- `ANALYSIS_REPORTS/AERODYNAMIC/Drag_Breakdown_Analysis.md`

---

**Document Control:**
- **Version:** 1.0 (Draft)
- **Date:** 2025-11-10
