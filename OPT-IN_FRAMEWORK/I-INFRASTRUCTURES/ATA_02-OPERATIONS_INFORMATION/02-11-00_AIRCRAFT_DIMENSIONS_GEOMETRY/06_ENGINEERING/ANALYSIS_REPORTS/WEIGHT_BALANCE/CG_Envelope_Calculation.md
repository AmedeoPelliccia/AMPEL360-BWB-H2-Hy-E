# CG Envelope Calculation

**Analysis ID:** 02-11-00-WB-001  
**Platform:** AMPEL360 BWB H₂ Hy-E Q100  
**Analysis Type:** Weight & Balance - CG Envelope  
**Status:** Planned  
**Date:** 2025-11-10

---

## 1. Objective

Calculate center of gravity (CG) envelope for all loading conditions to:
- Verify stability and control requirements
- Establish operational CG limits
- Support flight control system design
- Demonstrate compliance with CS-25.21 through CS-25.27

---

## 2. Reference Frame

### 2.1 Coordinate System
- **Origin:** Nose of aircraft
- **X-axis:** Positive aft (longitudinal)
- **Y-axis:** Positive right (lateral)
- **Z-axis:** Positive up (vertical)

### 2.2 Reference Datum
- **Longitudinal datum:** Station 0.0 at nose
- **Mean Aerodynamic Chord (MAC):** TBD m
- **MAC leading edge:** TBD m from datum

---

## 3. Mass Breakdown

### 3.1 Operating Empty Weight (OEW)

| Item | Mass (kg) | CG X (m) | Moment (kg·m) |
|------|-----------|----------|---------------|
| Structure | TBD | TBD | TBD |
| Propulsion | TBD | TBD | TBD |
| Systems | TBD | TBD | TBD |
| Furnishings | TBD | TBD | TBD |
| **Total OEW** | **TBD** | **TBD** | **TBD** |

### 3.2 Payload

| Item | Mass (kg) | CG X (m) | Moment (kg·m) |
|------|-----------|----------|---------------|
| Passengers (400) | 32,000 | TBD | TBD |
| Baggage | 8,000 | TBD | TBD |
| Cargo | TBD | TBD | TBD |
| **Total Payload** | **TBD** | **TBD** | **TBD** |

### 3.3 Fuel (Liquid H₂)

| Tank | Capacity (kg) | CG X (m) | Moment (kg·m) |
|------|---------------|----------|---------------|
| Center body tank 1 | TBD | TBD | TBD |
| Center body tank 2 | TBD | TBD | TBD |
| Wing tank (left) | TBD | TBD | TBD |
| Wing tank (right) | TBD | TBD | TBD |
| **Total Fuel** | **TBD** | **TBD** | **TBD** |

---

## 4. CG Envelope

### 4.1 Loading Conditions

| Condition | Weight (kg) | CG X (m) | CG % MAC | Status |
|-----------|-------------|----------|----------|--------|
| OEW | TBD | TBD | TBD % | Pending |
| OEW + Max Payload | TBD | TBD | TBD % | Pending |
| Max Take-Off Weight (MTOW) | 220,000 | TBD | TBD % | Pending |
| Max Landing Weight (MLW) | 190,000 | TBD | TBD % | Pending |
| Max Zero Fuel Weight (MZFW) | 170,000 | TBD | TBD % | Pending |

### 4.2 CG Limits
- **Forward CG limit:** TBD % MAC (stability constraint)
- **Aft CG limit:** TBD % MAC (control authority constraint)
- **CG range:** TBD % MAC

**Target:** CG range ≥ 15% MAC for operational flexibility

---

## 5. CG Travel During Flight

### 5.1 Fuel Burn Sequence
Fuel consumed in sequence to maintain CG within limits:
1. Center body tanks (balanced burn)
2. Wing tanks (balanced burn)
3. Trim tank (if required for CG management)

### 5.2 CG Shift Analysis
- **Initial CG (MTOW, full fuel):** TBD % MAC
- **Final CG (Landing weight, reserves):** TBD % MAC
- **Total CG shift:** TBD % MAC

---

## 6. Compliance Verification

### 6.1 Stability Requirements (CS-25.143)
- **Static margin:** ≥ 5% MAC at most aft CG
- **Neutral point:** TBD % MAC (from stability analysis)

### 6.2 Control Authority (CS-25.145)
- Elevator authority adequate to trim at forward CG limit
- Elevator authority adequate to flare at aft CG limit

---

## 7. References

- `04_DESIGN/WEIGHT_BALANCE/Mass_Budget.md`
- `CALCULATIONS/WEIGHT_BALANCE/CG_Envelope_Tables.csv`
- CS-25.21 through CS-25.27 (Weight and Balance)

---

**Document Control:**
- **Version:** 1.0 (Draft)
- **Date:** 2025-11-10
