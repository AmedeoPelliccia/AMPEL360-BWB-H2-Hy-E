# Pressure Vessel Analysis

**Analysis ID:** 02-11-00-STR-003  
**Platform:** AMPEL360 BWB H₂ Hy-E Q100  
**Analysis Type:** Structural - Pressure Vessel  
**Status:** Planned  
**Date:** 2025-11-10

---

## 1. Objective

Analyze the center body pressure vessel structure for compliance with CS-25.365 (Pressurization Loads):
- Verify hoop and longitudinal stress under design differential pressure
- Assess buckling stability
- Validate structural fatigue life for pressurization cycles

---

## 2. Pressure Vessel Description

### 2.1 Geometry
- **Configuration:** BWB center body, non-circular cross-section
- **Equivalent radius:** 2.1 m (local cylindrical approximation)
- **Length:** 52.5 m
- **Depth:** 4.2 m

### 2.2 Design Pressure
- **Max cabin altitude:** 8,000 ft (2,438 m)
- **Max operating altitude:** 41,000 ft (12,497 m)
- **Design differential pressure:** 8.0 psi (55.2 kPa)
- **Proof pressure (test):** 1.33 × design = 10.6 psi

---

## 3. Analysis Methodology

### 3.1 Hoop Stress
σ_hoop = (P × r) / t

Where:
- P = differential pressure (55.2 kPa)
- r = equivalent radius (2.1 m)
- t = skin thickness (TBD mm)

### 3.2 Longitudinal Stress
σ_long = (P × r) / (2t)

### 3.3 Buckling Analysis
Buckling under combined pressure and bending loads analyzed per FEM.

---

## 4. Results

### 4.1 Stress Summary
- **Hoop stress:** TBD MPa
- **Longitudinal stress:** TBD MPa
- **Von Mises equivalent:** TBD MPa
- **Allowable (Al 7075-T6):** 503 MPa (yield), 572 MPa (ultimate)

### 4.2 Margin of Safety
MS = (Allowable / Applied) - 1 = TBD

---

## 5. Fatigue Life

### 5.1 Design Life Requirements
- **Design service goal:** 60,000 flight hours
- **Pressurization cycles:** 60,000 (1 cycle per flight)
- **Inspection interval:** 10,000 cycles

### 5.2 Fatigue Analysis
Safe-life analysis per CS-25.571 TBD.

---

## 6. References

- `04_DESIGN/STRUCTURAL_DESIGN/Center_Body_Structure.md`
- `CALCULATIONS/STRUCTURAL/Pressure_Vessel_Hand_Calcs.csv`
- CS-25.365, CS-25.571

---

**Document Control:**
- **Version:** 1.0 (Draft)
- **Date:** 2025-11-10
