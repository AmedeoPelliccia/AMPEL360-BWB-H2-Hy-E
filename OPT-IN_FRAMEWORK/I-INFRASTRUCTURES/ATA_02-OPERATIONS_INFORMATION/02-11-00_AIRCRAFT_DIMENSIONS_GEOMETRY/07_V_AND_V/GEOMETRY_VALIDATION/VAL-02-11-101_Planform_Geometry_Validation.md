# VAL-02-11-101: Planform Geometry Validation

**Validation ID:** VAL-02-11-101  
**Component:** 02-11-00 Aircraft Dimensions Geometry  
**Element:** BWB Planform Geometry  
**Status:** Template Ready - Awaiting Validation

---

## 1. Objective

Validate that the BWB planform geometry accurately represents the design intent and meets all geometric requirements including:
- Wing area (845 m²)
- Aspect ratio (3.2)
- Sweep angles (LE: 37°, QC: 32°)
- Taper ratio (0.1)
- Planform shape and continuity

---

## 2. Scope

This validation covers the complete planform geometry from centerline (BL 0) to wingtips (BL ±26), including:
- Integrated wing area calculation
- Leading edge and quarter-chord sweep angles
- Chord distribution (root 35.0 m to tip 3.5 m)
- Mean Aerodynamic Chord (MAC) calculation and position
- Planform shape fairness and continuity

---

## 3. Reference Documents

| Document ID | Title | Location |
|-------------|-------|----------|
| REQ-02-11-007 | Wing Area Requirement | `03_REQUIREMENTS/BWB_Geometry_Requirements.csv` |
| REQ-02-11-008 | Aspect Ratio Requirement | `03_REQUIREMENTS/BWB_Geometry_Requirements.csv` |
| — | Planform Design | `04_DESIGN/BWB_GEOMETRY/PLANFORM/` |
| — | Geometry Parameters | `01_OVERVIEW/BWB_GEOMETRY/Geometry_Parameters.csv` |
| — | Wing Geometry Design | `04_DESIGN/BWB_GEOMETRY/WING/` |

---

## 4. Design Specifications

| Parameter | Design Value | Tolerance | Source |
|-----------|--------------|-----------|--------|
| Wing Area (S) | 845 m² | ±5 m² | Geometry_Parameters.csv |
| Aspect Ratio (AR) | 3.2 | ±0.05 | Calculated: b²/S |
| Wingspan (b) | 52.0 m | ±0.1 m | Principal_Dimensions |
| Root Chord | 35.0 m | ±0.2 m | At BL 0 |
| Tip Chord | 3.5 m | ±0.05 m | At BL 26 |
| Taper Ratio (λ) | 0.1 | — | Tip/Root |
| LE Sweep (Λ_LE) | 37° | ±0.5° | Leading edge |
| QC Sweep (Λ_QC) | 32° | ±0.5° | 25% chord line |
| MAC | 22.5 m | — | Calculated |
| MAC y-position | ~8.5 m | — | From centerline |

---

## 5. Validation Methods

### 5.1 CAD Model Analysis
- Extract planform geometry from master CAD model
- Generate planform cross-sections at 1 m BL intervals
- Calculate geometric properties using CAD integration tools
- Export geometry data for independent verification

### 5.2 Area Calculation
**Method 1: CAD Surface Area**
- Use CAD native surface area calculation tool
- Sum areas of all planform surfaces (excluding thickness)

**Method 2: Numerical Integration**
- Integrate chord distribution from BL 0 to BL 26
- Double for symmetry: Total Area = 2 × ∫₀²⁶ c(y) dy

**Method 3: Trapezoidal Rule**
- Discretize planform into spanwise strips
- Sum strip areas using trapezoidal approximation

### 5.3 MAC Calculation
```
MAC = (2/S) × ∫₀^(b/2) c²(y) dy
y_MAC = (2/S) × ∫₀^(b/2) y×c(y) dy
```

### 5.4 Sweep Angle Measurement
- Extract leading edge line from CAD
- Extract quarter-chord line from CAD
- Calculate sweep angles from geometry using trigonometry

---

## 6. Validation Procedure

**Step 1: CAD Model Preparation**
1. Open certified/baselined CAD model
2. Verify model version matches configuration baseline
3. Extract planform surface geometry
4. Generate planform projection (top view)

**Step 2: Geometric Property Extraction**
1. Calculate wing area using CAD tools (record method)
2. Measure root and tip chords
3. Extract leading edge and quarter-chord curves
4. Calculate sweep angles
5. Compute MAC and its position

**Step 3: Independent Verification**
1. Export chord distribution data (y-station vs. chord)
2. Perform independent numerical integration
3. Compare results from CAD vs. numerical methods
4. Verify aspect ratio: AR = b²/S

**Step 4: Geometry Quality Checks**
1. Verify planform edge continuity (G2 or better)
2. Check for discontinuities or kinks in leading/trailing edges
3. Validate smooth chord distribution
4. Inspect blend quality at center body transition

---

## 7. Acceptance Criteria

| Parameter | Target | Tolerance | Acceptance |
|-----------|--------|-----------|------------|
| Wing Area | 845 m² | ±5 m² | 840-850 m² |
| Aspect Ratio | 3.2 | ±0.05 | 3.15-3.25 |
| Taper Ratio | 0.1 | ±0.01 | 0.09-0.11 |
| LE Sweep | 37° | ±0.5° | 36.5°-37.5° |
| QC Sweep | 32° | ±0.5° | 31.5°-32.5° |
| MAC | 22.5 m | ±0.5 m | 22.0-23.0 m |
| Edge Continuity | G2 | Visual inspection | No discontinuities |

---

## 8. Data Recording

### 8.1 Geometric Properties

| Property | CAD Calculation | Numerical Integration | Hand Calculation | Mean | Status |
|----------|----------------|---------------------|------------------|------|--------|
| Wing Area (m²) | TBD | TBD | TBD | TBD | TBD |
| AR | TBD | TBD | TBD | TBD | TBD |
| MAC (m) | TBD | TBD | TBD | TBD | TBD |
| MAC y-pos (m) | TBD | TBD | TBD | TBD | TBD |
| LE Sweep (°) | TBD | TBD | TBD | TBD | TBD |
| QC Sweep (°) | TBD | TBD | TBD | TBD | TBD |

### 8.2 Chord Distribution Data (Sample Points)

| BL Station (m) | Chord (m) | LE X (m) | TE X (m) |
|---------------|----------|----------|----------|
| 0 (Centerline) | TBD | TBD | TBD |
| 5 | TBD | TBD | TBD |
| 10 | TBD | TBD | TBD |
| 15 | TBD | TBD | TBD |
| 20 | TBD | TBD | TBD |
| 26 (Tip) | TBD | TBD | TBD |

---

## 9. Results and Analysis

### 9.1 Summary

| Validation Item | Result | Target | Status |
|----------------|--------|--------|--------|
| Wing Area | TBD m² | 845 m² ±5 | TBD |
| Aspect Ratio | TBD | 3.2 ±0.05 | TBD |
| Taper Ratio | TBD | 0.1 ±0.01 | TBD |
| LE Sweep | TBD ° | 37° ±0.5 | TBD |
| QC Sweep | TBD ° | 32° ±0.5 | TBD |
| Planform Continuity | TBD | G2 minimum | TBD |

### 9.2 Disposition

**Validation Result:** [ ] PASS  [ ] FAIL  [ ] CONDITIONAL

**Justification:** TBD

---

## 10. Sign-Off

| Role | Name | Signature | Date |
|------|------|-----------|------|
| **Aerodynamics Engineer** | TBD | | TBD |
| **CAD Manager** | TBD | | TBD |
| **V&V Engineer** | TBD | | TBD |

---

## 11. Traceability

- REQ-02-11-007: Wing Area 845 m²
- REQ-02-11-008: Aspect Ratio 3.2
- REQ-02-11-010: Leading edge sweep
- VAL-02-11-103: Wing Geometry Validation (related)

---

## 12. Revision History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | 2025-11-11 | COPILOT Agent prompted by Amedeo Pelliccia | Initial template creation |
