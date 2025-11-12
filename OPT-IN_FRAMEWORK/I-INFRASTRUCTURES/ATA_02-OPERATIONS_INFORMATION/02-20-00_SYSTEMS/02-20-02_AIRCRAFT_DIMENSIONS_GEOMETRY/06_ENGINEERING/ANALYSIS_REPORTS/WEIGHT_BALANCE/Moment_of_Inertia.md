# Moment of Inertia Calculation

**Analysis ID:** 02-11-00-WB-003  
**Platform:** AMPEL360 BWB H₂ Hy-E Q100  
**Analysis Type:** Weight & Balance - Inertia Tensor  
**Status:** Planned  
**Date:** 2025-11-10

---

## 1. Objective

Calculate mass moments of inertia for:
- Flight dynamics simulation
- Flight control system design
- Handling qualities analysis
- Compliance with stability and control requirements

---

## 2. Coordinate System

- **Origin:** Aircraft CG
- **X-axis:** Forward (roll axis)
- **Y-axis:** Right (pitch axis)
- **Z-axis:** Down (yaw axis)

---

## 3. Inertia Tensor Calculation

### 3.1 Moments of Inertia

I_xx = Σ m_i × (y_i² + z_i²)  
I_yy = Σ m_i × (x_i² + z_i²)  
I_zz = Σ m_i × (x_i² + y_i²)

### 3.2 Products of Inertia

I_xy = Σ m_i × x_i × y_i  
I_xz = Σ m_i × x_i × z_i  
I_yz = Σ m_i × y_i × z_i

---

## 4. Results

### 4.1 Inertia Values (Representative Loading)

| Parameter | Value (kg·m²) | Unit |
|-----------|---------------|------|
| I_xx (Roll) | TBD | kg·m² |
| I_yy (Pitch) | TBD | kg·m² |
| I_zz (Yaw) | TBD | kg·m² |
| I_xy | TBD | kg·m² |
| I_xz | TBD | kg·m² |
| I_yz | TBD | kg·m² |

### 4.2 Radii of Gyration

r_x = √(I_xx / m) = TBD m  
r_y = √(I_yy / m) = TBD m  
r_z = √(I_zz / m) = TBD m

---

## 5. Loading Conditions

Inertia calculated for:
- [ ] OEW
- [ ] MTOW (full fuel, max payload)
- [ ] MLW (landing fuel, max payload)
- [ ] Various fuel states (for CG and inertia variation)

---

## 6. References

- `CALCULATIONS/WEIGHT_BALANCE/Inertia_Tensor_Calc.csv`
- `ANALYSIS_REPORTS/WEIGHT_BALANCE/CG_Envelope_Calculation.md`

---

**Document Control:**
- **Version:** 1.0 (Draft)
- **Date:** 2025-11-10
