# Range Performance Analysis

**Analysis ID:** 02-11-00-PERF-001  
**Platform:** AMPEL360 BWB H₂ Hy-E Q100  
**Analysis Type:** Performance - Range  
**Status:** Planned  
**Date:** 2025-11-10

---

## 1. Objective

Calculate aircraft range performance to:
- Verify design range requirement (8,000 km)
- Assess payload-range trade-offs
- Support mission planning and operations
- Validate H₂ fuel capacity sizing

---

## 2. Design Requirements

### 2.1 Range Target
- **Design range:** 8,000 km (4,320 nm)
- **Reserves:** 5% contingency + 30 min hold + alternate (200 km)
- **Payload:** 400 passengers + baggage (40,000 kg)

### 2.2 Cruise Conditions
- **Cruise Mach:** 0.82
- **Cruise altitude:** 41,000 ft (12,497 m)
- **Cruise L/D:** TBD (target: > 23)

---

## 3. Range Calculation Method

### 3.1 Breguet Range Equation

R = (V / (g × SFC)) × (L/D) × ln(W_initial / W_final)

Where:
- R = range (km)
- V = cruise speed (m/s)
- g = gravitational acceleration (9.81 m/s²)
- SFC = specific fuel consumption (kg/N/s)
- L/D = lift-to-drag ratio
- W_initial = weight at start of cruise (kg)
- W_final = weight at end of cruise (kg)

### 3.2 Mission Profile

| Phase | Duration/Distance | Fuel Burn (kg) |
|-------|-------------------|----------------|
| Start-up and taxi | 10 min | TBD |
| Take-off | - | TBD |
| Climb to cruise | 25 min | TBD |
| Cruise | TBD km | TBD |
| Descent | 15 min | TBD |
| Landing and taxi | 5 min | TBD |
| **Total mission fuel** | | **TBD** |
| Reserves (5% + 30 min hold + alternate) | | **TBD** |
| **Total fuel required** | | **TBD** |

---

## 4. Performance Results

### 4.1 Nominal Mission (8,000 km)

| Parameter | Value | Unit |
|-----------|-------|------|
| MTOW | 220,000 | kg |
| OEW | 120,000 | kg |
| Payload | 40,000 | kg |
| Mission fuel | TBD | kg |
| Reserves | TBD | kg |
| Total fuel capacity | TBD | kg |
| Range | 8,000 | km |
| Cruise L/D | TBD | - |
| SFC | TBD | kg/kN/hr |

### 4.2 Maximum Range (Max Fuel, Reduced Payload)

| Parameter | Value | Unit |
|-----------|-------|------|
| MTOW | 220,000 | kg |
| OEW | 120,000 | kg |
| Payload | TBD | kg |
| Total fuel | TBD | kg |
| **Maximum range** | **TBD** | **km** |

---

## 5. Payload-Range Diagram

| Payload (kg) | Range (km) | Notes |
|--------------|------------|-------|
| 40,000 | 8,000 | Design point |
| 50,000 | TBD | Maximum structural payload |
| 30,000 | TBD | Reduced payload, more fuel |
| 20,000 | TBD | Ferry mission |
| 0 | TBD | Maximum range (ferry) |

---

## 6. Sensitivity Analysis

Impact of design parameters on range:

| Parameter Change | ΔRange (km) | % Change |
|------------------|-------------|----------|
| +1% cruise L/D | TBD | TBD % |
| -1% SFC | TBD | TBD % |
| +1000 kg OEW | TBD | TBD % |
| +5% fuel capacity | TBD | TBD % |

---

## 7. Comparison with Competitors

| Aircraft | Seats | Range (km) | Cruise Mach | Notes |
|----------|-------|------------|-------------|-------|
| AMPEL360 Q100 | 400 | 8,000 | 0.82 | H₂-powered BWB |
| A350-1000 | 366 | 14,800 | 0.85 | Conventional, Jet-A |
| B787-10 | 330 | 11,730 | 0.85 | Conventional, Jet-A |

---

## 8. References

- `CALCULATIONS/PERFORMANCE/Breguet_Range_Model.csv`
- `SIMULATIONS/FLIGHT_MECHANICS/Performance_Sim_Models.md`
- `ANALYSIS_REPORTS/AERODYNAMIC/Drag_Breakdown_Analysis.md`
- `04_DESIGN/PERFORMANCE_TARGETS/Range_Requirements.md`

---

**Document Control:**
- **Version:** 1.0 (Draft)
- **Date:** 2025-11-10
