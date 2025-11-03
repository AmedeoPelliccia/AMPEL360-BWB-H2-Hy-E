# CG Location - Door L1 Forward

**Calculation:** CALC-52-10-01-WGT-002  
**Date:** 2025-11-03  
**Revision:** A  
**Method:** Moment Analysis (AI-Assisted)  
**Confidence:** ±15%

## 1. REFERENCE SYSTEM

### Coordinate System
```
Origin: Forward bottom hinge
X-axis: Along fuselage (aft positive)
Y-axis: Spanwise (outboard positive)
Z-axis: Vertical (up positive)
```

## 2. COMPONENT CG LOCATIONS

### Panel Components (from origin)
```
Face sheets: x=940, y=560, z=24 mm
Core: x=940, y=560, z=24 mm
Edge bands: x=940, y=0, z=24 mm
Inserts: x=940, y=0, z=24 mm (at latches)
Lightning protection: x=940, y=560, z=0 mm
Adhesive: Distributed evenly
Paint: x=940, y=560, z=48 mm
```

### Frame Assembly
```
Frame CG: x=0, y=560, z=940 mm
(At hinge line, mid-height)
```

## 3. CG CALCULATION

### X-Direction (Longitudinal)
```
ΣM_x = Σ(m_i × x_i)

Panel: 72 kg × 940 mm = 67,680 kg⋅mm
Frame: 42 kg × 0 mm = 0 kg⋅mm

Total: 67,680 kg⋅mm
Total mass: 114 kg

x_cg = 67,680 / 114 = 594 mm from hinge line
```

### Y-Direction (Spanwise)
```
All components symmetric about centerline
y_cg = 560 mm (mid-width)
```

### Z-Direction (Vertical)
```
ΣM_z = Σ(m_i × z_i)

Panel: 72 kg × 24 mm = 1,728 kg⋅mm
Frame: 42 kg × 940 mm = 39,480 kg⋅mm

Total: 41,208 kg⋅mm

z_cg = 41,208 / 114 = 361 mm from bottom
```

## 4. OVERALL CG

```
CG Location (from forward bottom hinge):
x_cg = 594 mm (53% of width)
y_cg = 560 mm (50% of height at mid-width)
z_cg = 361 mm (19% of height)
```

## 5. CG ENVELOPE

### Tolerance
```
Manufacturing variation: ±50 mm in all directions
Weight growth: Changes CG by ~20 mm
```

### Design CG Envelope
```
x: 544-644 mm
y: 510-610 mm
z: 311-411 mm
```

## 6. VALIDATION REQUIRED

- [ ] Weigh prototype door
- [ ] Measure actual CG (trifilar suspension)
- [ ] Update with as-built weights
- [ ] Verify inertia properties

---

**Status:** Preliminary Estimate  
**Confidence:** MEDIUM
