# Dynamic Clearance Study

**Analysis ID:** 02-11-00-CLR-003  
**Platform:** AMPEL360 BWB H₂ Hy-E Q100  
**Analysis Type:** Clearance - Dynamic Clearances  
**Status:** Planned  
**Date:** 2025-11-10

---

## 1. Objective

Analyze dynamic clearances during:
- Landing impact (gear stroke, airframe dynamics)
- Taxi over rough surfaces (gear stroke, pitch/roll motion)
- Hard landing scenarios
- Ground handling with crosswinds

---

## 2. Landing Impact Dynamics

### 2.1 Landing Conditions
- **Descent rate:** 10 ft/s (3.05 m/s) per CS-25.473
- **Landing weight:** MLW = 190,000 kg
- **Gear stroke:** TBD mm (at design sink rate)

### 2.2 Airframe Response
- **Pitch motion:** TBD ° (nose-down rotation at touchdown)
- **Vertical CG acceleration:** TBD g
- **Aft body minimum clearance:** TBD m (at maximum pitch-down)

### 2.3 Hard Landing
- **Design limit sink rate:** 12 ft/s (3.66 m/s)
- **Gear stroke at limit:** TBD mm
- **Aft body clearance:** TBD m

---

## 3. Taxi Dynamics

### 3.1 Taxi Bump (CS-25.491)
**Condition:** Taxi over 4-inch (10 cm) bump at typical taxi speed

- **Vertical acceleration:** TBD g
- **Gear stroke:** TBD mm
- **Belly clearance:** TBD m (minimum)

### 3.2 Rough Runway
- **Pitch oscillation amplitude:** TBD °
- **Roll oscillation amplitude:** TBD °
- **Wingtip clearance (min):** TBD m

---

## 4. Crosswind Ground Handling

### 4.1 Crosswind Taxi
- **Crosswind velocity:** 30 kt (design case)
- **Roll angle:** TBD ° (due to side load on vertical tail)
- **Wingtip clearance:** TBD m (on upwind side)

### 4.2 Crosswind Landing
- **Crab angle:** TBD ° (max crosswind component)
- **Drift at touchdown:** TBD m/s
- **Lateral gear loads:** TBD kN

---

## 5. Simulation Results

### 5.1 Multibody Dynamics Model
- **Software:** Adams or Simscape Multibody
- **Model includes:** Gear suspension, airframe flexibility, runway profile
- **Time-domain simulations:** Landing, taxi bump, turning

### 5.2 Critical Clearances Summary

| Scenario | Location | Minimum Clearance (m) | Required (m) | Margin (m) | Status |
|----------|----------|----------------------|--------------|------------|--------|
| Landing (design sink) | Aft body | TBD | 0.1 | TBD | Pending |
| Hard landing | Aft body | TBD | 0.05 | TBD | Pending |
| Taxi bump | Center body belly | TBD | 0.1 | TBD | Pending |
| Crosswind taxi | Wingtip (upwind) | TBD | 0.2 | TBD | Pending |

---

## 6. References

- CS-25.473 – Landing Load Conditions
- CS-25.491 – Taxi and Ground Handling Loads
- `SIMULATIONS/GROUND_DYNAMICS/Dynamic_Clearance_Sim_Models.md`
- `ANALYSIS_REPORTS/CLEARANCE/Ground_Clearance_Calculations.md`

---

**Document Control:**
- **Version:** 1.0 (Draft)
- **Date:** 2025-11-10
