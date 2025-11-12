# Coordinate Systems and Reference Frames

**Document ID:** 02-11-00-TN-002  
**Platform:** AMPEL360 BWB H₂ Hy-E Q100  
**Status:** Draft  
**Date:** 2025-11-10

---

## 1. Purpose

Define coordinate systems and reference frames used in engineering analyses to ensure consistency across FEM, CFD, flight mechanics, and other simulations.

---

## 2. Aircraft Body-Fixed Coordinate System

### 2.1 Origin and Axes

**Origin:** Aircraft nose (fuselage station 0.0)

**Axes:**
- **X-axis (longitudinal):** Positive forward (toward tail)
- **Y-axis (lateral):** Positive right (toward starboard wing)
- **Z-axis (vertical):** Positive up (perpendicular to X-Y plane)

**Right-hand rule:** Curl fingers from X to Y, thumb points in Z direction.

### 2.2 Reference Stations

| Station | Description | X-coordinate (m) |
|---------|-------------|------------------|
| FS 0.0 | Aircraft nose | 0.0 |
| FS 12.5 | Cockpit | 12.5 |
| FS 25.0 | Forward cabin | 25.0 |
| FS 35.0 | Mid cabin | 35.0 |
| FS 45.0 | Aft cabin | 45.0 |
| FS 52.5 | Tail (aft extremity) | 52.5 |

### 2.3 Waterline (WL) and Buttline (BL)

**Waterline (WL):** Z-coordinate, measured vertically from reference plane
- WL 0.0 = Bottom of center body (belly)
- WL 4.2 = Top of center body (roof)

**Buttline (BL):** Y-coordinate, measured laterally from centerline
- BL 0.0 = Aircraft centerline
- BL ±19.0 = Wing tips (±26.0 m semi-span, projected to body)

---

## 3. FEM Coordinate System

### 3.1 Global FEM Reference Frame

**Aligned with aircraft body-fixed system:**
- **Origin:** FS 0.0, BL 0.0, WL 0.0 (nose, centerline, belly)
- **Axes:** Same as aircraft body-fixed (X forward, Y right, Z up)

### 3.2 Local Element Coordinate Systems

**Shell elements (wing skin, center body skin):**
- **Element normal:** Perpendicular to element surface (outward)
- **Material orientation:** Fiber direction for composite elements

**Beam elements (stringers, frames):**
- **Beam axis:** Along element length
- **Cross-section orientation:** Per element property definition

---

## 4. CFD Coordinate System

### 4.1 Flow Field Reference Frame

**Inertial frame for external flow:**
- **Origin:** Aircraft nose or far-field inlet boundary
- **Axes:** Aligned with aircraft body-fixed axes
- **Freestream direction:** Typically aligned with X-axis (0° angle of attack)

### 4.2 Angle of Attack (α) and Sideslip (β)

**Angle of attack (α):**
- Angle between freestream velocity and X-Y plane
- Positive α = nose up

**Sideslip angle (β):**
- Angle between freestream velocity and X-Z plane
- Positive β = nose right

---

## 5. Flight Mechanics Reference Frames

### 5.1 Earth-Fixed Inertial Frame

**NED (North-East-Down) convention:**
- **X_E:** North
- **Y_E:** East
- **Z_E:** Down (toward Earth center)

**Usage:** Trajectory, navigation, mission analysis

### 5.2 Wind Axes

**Origin:** Aircraft CG

**Axes:**
- **X_W:** Aligned with velocity vector (flight path direction)
- **Y_W:** Perpendicular to X_W in horizontal plane (right)
- **Z_W:** Perpendicular to X_W and Y_W (down)

**Usage:** Aerodynamic forces (lift, drag, side force)

### 5.3 Stability Axes

**Origin:** Aircraft CG

**Axes:**
- **X_S:** In X-Z plane, aligned with projection of velocity vector
- **Y_S:** Same as body-fixed Y-axis
- **Z_S:** Perpendicular to X_S and Y_S (down)

**Usage:** Longitudinal stability analysis

---

## 6. Weight and Balance Reference Frame

### 6.1 Reference Datum

**Datum:** Aircraft nose (FS 0.0)

**CG location:**
- **X_CG:** Distance from datum (m)
- **% MAC:** Percent Mean Aerodynamic Chord (from MAC leading edge)

### 6.2 Mean Aerodynamic Chord (MAC)

**MAC definition:**
- **Length:** c̄ = (2/S) ∫∫ c² dy (integrated over wing planform)
- **Leading edge location:** X_LE_MAC (m from datum)

**For AMPEL360 Q100:**
- MAC length: TBD m
- MAC LE location: TBD m from FS 0.0

---

## 7. Ground Reference Frame

### 7.1 Runway Coordinate System

**Origin:** Runway threshold

**Axes:**
- **X_R:** Along runway centerline (take-off direction)
- **Y_R:** Perpendicular to runway centerline (laterally)
- **Z_R:** Perpendicular to runway surface (up)

**Usage:** Ground clearance analysis, landing trajectory

---

## 8. Transformation Between Frames

### 8.1 Body to Wind Axes

**Rotation sequence:**
1. Rotate about Z-axis by sideslip angle β
2. Rotate about Y-axis by angle of attack α

**Transformation matrix:**
```
[X_W]   [cos(α)cos(β)   sin(β)   sin(α)cos(β)] [X_B]
[Y_W] = [-cos(α)sin(β)  cos(β)  -sin(α)sin(β)] [Y_B]
[Z_W]   [-sin(α)         0        cos(α)     ] [Z_B]
```

### 8.2 Body to Earth (NED) Axes

**Euler angles:** φ (roll), θ (pitch), ψ (yaw)

**Rotation sequence:** Z-Y-X (yaw-pitch-roll)

**Transformation matrix:** (3-2-1 Euler angle sequence)

---

## 9. Coordinate System Verification

### 9.1 Consistency Checks

- [ ] FEM model coordinate system matches aircraft body-fixed system
- [ ] CFD model coordinate system consistent with FEM
- [ ] Flight mechanics model uses correct transformation matrices
- [ ] Weight and balance CG calculation uses correct datum and MAC definition

### 9.2 Cross-Disciplinary Verification

- [ ] Aerodynamic loads from CFD correctly transferred to FEM
- [ ] Mass properties from weight/balance correctly input to flight mechanics
- [ ] Ground clearances calculated in correct reference frame

---

## 10. References

- ISO 1151-1:1988 – Flight Dynamics – Concepts, Quantities, and Symbols
- SAE AS755 – Axis and Sign Convention for Flight Dynamics
- `TECHNICAL_NOTES/Modelling_Assumptions_and_Conventions.md`

---

**Document Control:**
- **Version:** 1.0 (Draft)
- **Author:** Chief Engineer – Systems Integration
- **Reviewed by:** Program Chief Engineer
- **Date:** 2025-11-10
