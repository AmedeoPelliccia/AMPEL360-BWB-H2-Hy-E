# Ground Clearance Calculations

**Analysis ID:** 02-11-00-CLR-001  
**Platform:** AMPEL360 BWB H₂ Hy-E Q100  
**Analysis Type:** Clearance - Ground Clearances  
**Status:** Planned  
**Date:** 2025-11-10

---

## 1. Objective

Calculate ground clearances for all critical conditions to ensure:
- No contact with ground during normal operations
- Compliance with CS-25.231 (Longitudinal Stability and Control)
- Compliance with CS-25.477 (Landing Gear Arrangement)
- Adequate clearance for rotation, taxi, and ground handling

---

## 2. Requirements

### 2.1 CS-25.477 Landing Gear Arrangement

- **Tail-down angle:** ≥ 10° with MLW at most aft CG
- **Ground clearance angle:** ≥ 15° between ground and most forward part of aircraft at tail-down attitude
- **Lateral tip-over angle:** ≥ 25° with most critical lateral CG

### 2.2 Operational Requirements

- **Rotation clearance:** Adequate clearance during take-off rotation to VR
- **Obstacle clearance:** Sufficient clearance for runway lights, markings, and debris

---

## 3. Aircraft Geometry

### 3.1 Key Dimensions
- **Main landing gear (MLG) height:** 3.2 m (compressed)
- **Nose landing gear (NLG) height:** 2.8 m (compressed)
- **Wheelbase:** 18.0 m (NLG to MLG)
- **Main gear track:** 12.5 m
- **Center body belly clearance:** TBD m (static, level attitude)
- **Wingtip ground clearance:** TBD m (static, level attitude)
- **Vertical tail clearance:** TBD m (static, level attitude)

---

## 4. Ground Clearance Analysis

### 4.1 Static Level Attitude

| Location | Height Above Ground (m) | Minimum Required (m) | Margin (m) | Status |
|----------|-------------------------|----------------------|------------|--------|
| Center body belly | TBD | 0.5 | TBD | Pending |
| Wingtip | TBD | 0.3 | TBD | Pending |
| Vertical tail | TBD | 1.0 | TBD | Pending |
| Engine nacelle | TBD | 0.8 | TBD | Pending |

### 4.2 Tail-Down Attitude

**Condition:** MLW, aft CG, gear fully extended

- **Pitch angle:** TBD ° (nose up)
- **Aft fuselage clearance:** TBD m
- **Tail strike protection:** Required? TBD

**Requirement:** Tail-down angle ≥ 10° per CS-25.477

### 4.3 Rotation Attitude (Take-Off)

**Condition:** MTOW, rotation to VR

- **Rotation angle:** TBD ° (at VR)
- **Aft body clearance during rotation:** TBD m
- **Adequate clearance?** TBD

### 4.4 Lateral Tip-Over

**Condition:** Aircraft on level ground, MLW, lateral CG offset

- **Tip-over angle:** TBD ° (wheels on one side lifting off)
- **Requirement:** ≥ 25° per CS-25.477
- **Status:** TBD

---

## 5. Landing Gear Stroke Effects

### 5.1 Gear Compression
- **MLG static stroke:** TBD mm
- **MLG dynamic stroke (landing):** TBD mm
- **NLG static stroke:** TBD mm
- **NLG dynamic stroke (landing):** TBD mm

### 5.2 Ground Clearance at Maximum Compression
- **Center body belly:** TBD m (at max gear compression)
- **Wingtip:** TBD m (at max gear compression)
- **Status:** Must remain > 0 m (no ground contact)

---

## 6. Over-Rotation Protection

### 6.1 Tail Strike Protection
- **Tail skid or bumper:** Required? TBD
- **Location:** TBD
- **Load capacity:** TBD kN

---

## 7. Airport Compatibility

### 7.1 Pavement Classification Number (PCN)
- **Aircraft Classification Number (ACN):** TBD
- **Target airports:** PCN ≥ TBD

### 7.2 Turning Radius
- **Minimum turning radius:** TBD m (with max nose wheel steering)
- **Taxiway width required:** TBD m

---

## 8. References

- CS-25.231 – Longitudinal Stability and Control
- CS-25.477 – Landing Gear Arrangement
- `TRADE_STUDIES/Gear_Height_Trade_Study.md`
- `CALCULATIONS/CLEARANCE/Ground_Clearance_Geom_Calc.csv`
- `04_DESIGN/STRUCTURAL_DESIGN/Landing_Gear_Design.md`

---

**Document Control:**
- **Version:** 1.0 (Draft)
- **Date:** 2025-11-10
