# Load Case Definition and Combinations

**Document ID:** 02-11-00-TN-003  
**Platform:** AMPEL360 BWB H₂ Hy-E Q100  
**Status:** Draft  
**Date:** 2025-11-10

---

## 1. Purpose

Define structural load cases and load combinations per CS-25 requirements for use in finite element analysis and structural substantiation.

---

## 2. Load Categories

### 2.1 Flight Loads (CS-25.301)

**Maneuver loads (CS-25.331 to CS-25.351):**
- Symmetric pull-up and push-over
- Rolling maneuvers
- Yaw maneuvers

**Gust loads (CS-25.341):**
- Vertical gusts (up and down)
- Lateral gusts

**High-lift device loads (CS-25.345):**
- Take-off configuration
- Landing configuration

### 2.2 Ground Loads (CS-25.471 to CS-25.511)

**Landing loads:**
- Level landing
- Tail-down landing
- One-gear landing
- Side load conditions (drift)
- Rebound conditions

**Taxi and ground handling loads:**
- Taxi bump
- Turning
- Braking

### 2.3 Pressure Loads (CS-25.365)

**Cabin pressurization:**
- Maximum differential pressure (8.0 psi)
- Proof pressure (1.33 × design pressure)
- Negative pressure relief

---

## 3. Load Factors and Design Speeds

### 3.1 Flight Envelope (CS-25.333 through CS-25.337)

| Speed | Definition | Value (KEAS) | Notes |
|-------|-----------|--------------|-------|
| VS | Stall speed (clean) | TBD | Per CS-25.103 |
| VA | Design maneuvering speed | TBD | Speed at which full deflection of control surfaces will not exceed limit load |
| VB | Design speed for maximum gust | TBD | Minimum gust penetration speed |
| VC | Design cruise speed | TBD | Normal operating speed |
| VD | Design dive speed | 1.25 × VC | Maximum speed in any condition |

### 3.2 Limit Load Factors (CS-25.337)

| Condition | Positive Load Factor (n_pos) | Negative Load Factor (n_neg) |
|-----------|------------------------------|------------------------------|
| Flaps up | +2.5 | -1.0 |
| Flaps extended | +2.0 | 0.0 |

**Ultimate load factor:** 1.5 × limit load factor (per CS-25.303)

---

## 4. Critical Load Cases

### 4.1 Flight Load Cases

| Load Case ID | Description | Speed | Load Factor | Configuration |
|--------------|-------------|-------|-------------|---------------|
| LC-MAN-01 | Symmetric pull-up | VC | +2.5 | Clean |
| LC-MAN-02 | Symmetric push-over | VC | -1.0 | Clean |
| LC-MAN-03 | Rolling maneuver | VA | Variable | Clean |
| LC-GUST-01 | Vertical gust +56 fps | VC | Variable | Clean |
| LC-GUST-02 | Vertical gust -56 fps | VC | Variable | Clean |
| LC-HL-01 | High-lift take-off | V2 to VFE | +2.0 | Flaps 20° |
| LC-HL-02 | High-lift landing | VREF to VFE | +2.0 | Flaps 30° |

### 4.2 Ground Load Cases

| Load Case ID | Description | Weight | Vertical LF | Forward/Lateral |
|--------------|-------------|--------|-------------|-----------------|
| LC-LDG-01 | Level landing symmetric | MLW | 3.0 | 0.25 V_vert |
| LC-LDG-02 | Tail-down landing | MLW | 2.4 | 0.25 V_vert |
| LC-LDG-03 | One-gear landing | MLW | 3.0 | 0.25 V_vert |
| LC-LDG-04 | Side load (drift) | MLW | 3.0 | 0.5 V_vert lateral |
| LC-TAXI-01 | Taxi bump | MTOW | 2.0 | 0 |
| LC-TAXI-02 | Max braking | MTOW | 1.0 | 0.6 static weight |

### 4.3 Pressure Load Cases

| Load Case ID | Description | ΔP (psi) | Flight Phase |
|--------------|-------------|----------|--------------|
| LC-PRESS-01 | Max cabin pressure | 8.0 | Cruise |
| LC-PRESS-02 | Proof pressure | 10.6 | Ground test |
| LC-PRESS-03 | Negative pressure relief | -0.5 | Ground |

---

## 5. Load Combinations

### 5.1 Combined Flight Loads

**Maneuver + Pressurization:**
- LC-COMB-01 = LC-MAN-01 + LC-PRESS-01 (2.5g + 8.0 psi)
- LC-COMB-02 = LC-MAN-02 + LC-PRESS-01 (-1.0g + 8.0 psi)

**Gust + Pressurization:**
- LC-COMB-03 = LC-GUST-01 + LC-PRESS-01 (Gust + 8.0 psi)

**Engine failure (OEI) + Maneuver:**
- LC-COMB-04 = Critical engine failure + maneuvering load

### 5.2 Combined Ground Loads

**Landing + Engine thrust:**
- LC-COMB-05 = LC-LDG-01 + Reverse thrust (if applicable)

**Turning + Braking:**
- LC-COMB-06 = LC-TAXI-03 (turning) + LC-TAXI-02 (braking)

---

## 6. Distributed Loads

### 6.1 Aerodynamic Pressure Distribution

**Source:** CFD analysis or handbook methods

**Application in FEM:**
- Distributed pressure on wing and center body surfaces
- Interpolated from CFD mesh to FEM mesh
- Sanity check: Total integrated force matches flight condition

### 6.2 Inertia Loads

**Application:**
- Distributed mass on structure (structural weight, fuel, payload)
- Acceleration field applied per load factor (e.g., 2.5g upward for pull-up)

---

## 7. Load Case Matrix

### 7.1 Critical Locations and Load Cases

| Structural Component | Critical Load Case(s) | Design Driver |
|----------------------|----------------------|---------------|
| Wing upper skin | LC-MAN-01 (2.5g pull-up) | Compression buckling |
| Wing lower skin | LC-MAN-02 (-1.0g push-over) | Tension yielding |
| Center body pressure vessel | LC-COMB-01 (2.5g + pressure) | Hoop stress |
| Landing gear attach | LC-LDG-03 (one-gear landing) | Ultimate strength |
| Vertical tail root | LC-MAN-04 (yaw maneuver) | Bending moment |

---

## 8. Load Application in FEM

### 8.1 Boundary Conditions

**Inertia relief method:**
- All 6 DOF (3 translations, 3 rotations) released at aircraft CG
- Inertia forces balance applied external loads

**Constrained method:**
- Fix one node (typically at CG or main gear attachment)
- Apply external loads as forces and pressures

### 8.2 Load Steps

**Static analysis:** All loads applied in single step

**Dynamic analysis (if required):** Time-varying loads for gust or landing impact

---

## 9. Verification and Validation

### 9.1 Load Case Verification

- [ ] All CS-25 required load cases defined
- [ ] Load factors consistent with certification specifications
- [ ] Load combinations include critical interactions

### 9.2 Analysis Validation

- [ ] FEM results compared to hand calculations for simple load cases
- [ ] Load paths are continuous and logical
- [ ] Reactions at supports match applied loads (equilibrium check)

---

## 10. References

- CS-25.301 – Loads
- CS-25.331 through CS-25.351 – Flight Maneuver and Gust Loads
- CS-25.365 – Pressurization Loads
- CS-25.471 through CS-25.511 – Ground Loads
- `CALCULATIONS/CERTIFICATION/CS25_Load_Case_List.csv`
- `ANALYSIS_REPORTS/STRUCTURAL/FEM_Global_Model.md`

---

**Document Control:**
- **Version:** 1.0 (Draft)
- **Author:** Chief Structural Engineer
- **Reviewed by:** Program Chief Engineer
- **Date:** 2025-11-10
