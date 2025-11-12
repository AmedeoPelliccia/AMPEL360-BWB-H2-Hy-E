# Wing Box Stress Analysis

**Analysis ID:** 02-11-00-STR-002  
**Platform:** AMPEL360 BWB H₂ Hy-E Q100  
**Analysis Type:** Structural - Wing Box Detailed Stress  
**Status:** Complete  
**Date:** 2025-11-10  
**Reference Figures:** 02-11-00-STR-002-FIG-01_WingBox_Section.png, 02-11-00-STR-002-FIG-02_WingBox_Stress_Map.png

---

## 1. Objective

Perform detailed stress analysis of the BWB wing box structure to verify:
- Adequate strength under design loads (CS-25.305)
- Structural efficiency and weight optimization
- Panel buckling margins (compression surfaces)
- Compliance with damage tolerance requirements (CS-25.571)
- Identification of hot-spot locations requiring detailed analysis

---

## 2. Wing Box Description

### 2.1 Geometry
- **Wingspan:** 52.0 m (each side from centerline)
- **Root chord:** 16.2 m (at centerline BL 0.0)
- **Mid-span chord:** 9.8 m (at BL 13.0)
- **Tip chord:** 2.8 m (at BL 26.0)
- **Sweep angle:** 35° (quarter-chord)
- **Aspect ratio:** 3.2
- **Box depth:** 1.8 m (root), 1.2 m (mid-span), 0.4 m (tip)

### 2.2 Construction

**Primary Structure:**
- **Upper skin:** IM7/8552 carbon fiber composite, [±45/0/90]s layup, co-cured stringers
- **Lower skin:** IM7/8552 carbon fiber composite, [±45/0/90]s layup, co-cured stringers
- **Front spar:** C-channel section, IM7/8552 composite with titanium end fittings
- **Rear spar:** C-channel section, IM7/8552 composite with titanium end fittings
- **Stringers:** Blade-type, 24 stringers upper skin, 18 stringers lower skin, 0.25m spacing
- **Ribs:** Al 7075-T6 machined ribs, spacing 0.6 m (0.3 m at critical sections)

**Material Properties (from TN-004):**
- IM7/8552 composite: E₁ = 135 GPa, E₂ = 10 GPa, G₁₂ = 5 GPa, ρ = 1600 kg/m³
- Al 7075-T6: E = 71 GPa, F_tu = 503 MPa, F_cy = -455 MPa, ρ = 2810 kg/m³
- Ti-6Al-4V: E = 110 GPa, F_tu = 827 MPa, F_cy = -760 MPa, ρ = 4430 kg/m³

---

## 3. Load Cases

Critical load cases from CS25_Load_Case_List.csv and global FEM (STR-001):

| Load Case | Description | Limit Load Factor | Wing Root BM (kN·m) | Critical Section | Status |
|-----------|-------------|-------------------|---------------------|------------------|--------|
| LC-MNV-01 | Symmetric pull-up 2.5g @ MTOW | +2.5 | +182,400 | Wing root upper skin | Analyzed |
| LC-MNV-02 | Symmetric push-over -1.0g @ MTOW | -1.0 | -73,000 | Wing root lower skin | Analyzed |
| LC-GST-03 | Vertical gust +66 ft/s @ VC | +2.14 | +156,200 | Mid-span (BL 13m) | Analyzed |
| LC-MNV-04 | Rolling maneuver @ VD | +1.5 | +98,500 | Wing tip (BL 24-26m) | Analyzed |
| LC-CMB-05 | Combined maneuver + lateral gust | +2.3 | +168,800 | Wing root front spar | Analyzed |
| LC-GST-06 | Lateral gust @ VC | +1.8 | +125,600 | Rear spar web | Analyzed |

---

## 4. Section Properties

Extracted from Wing_Box_Section_Calcs.csv:

| Station | y (m) | Chord (m) | Box Depth (m) | Upper Skin t (mm) | Lower Skin t (mm) | # Stringers U/L | Spar Cap Area (cm²) | Ixx (×10⁴ cm⁴) | Iyy (×10⁴ cm⁴) | Izz (×10⁴ cm⁴) | Mass (kg/m) |
|---------|-------|-----------|---------------|-------------------|-------------------|-----------------|---------------------|----------------|----------------|----------------|-------------|
| Root | 0.0 | 16.2 | 1.8 | 12.0 | 14.0 | 24/18 | 250 | 1244.0 | 1.245 | 0.855 | 198.6 |
| 25% | 6.5 | 13.5 | 1.5 | 10.0 | 12.0 | 20/16 | 200 | 944.0 | 0.682 | 0.518 | 150.6 |
| 50% | 13.0 | 9.8 | 1.2 | 8.0 | 10.0 | 16/12 | 150 | 582.0 | 0.365 | 0.286 | 98.4 |
| 75% | 19.5 | 5.2 | 0.8 | 6.0 | 7.0 | 12/10 | 85 | 218.0 | 0.148 | 0.122 | 52.2 |
| Tip | 26.0 | 2.8 | 0.4 | 4.0 | 5.0 | 8/6 | 35 | 48.5 | 0.042 | 0.038 | 22.8 |

---

## 5. Analysis Results

### 5.1 Critical Stresses (Limit Load)

#### 5.1.1 LC-MNV-01: 2.5g Pull-Up (Design Driver)

| Component | Station | Stress Type | Applied (MPa) | Allowable (MPa) | MS | Notes |
|-----------|---------|-------------|---------------|-----------------|-----|-------|
| Upper skin panel | Root, BL 0-3m | Compression | -285.4 | -324.0 | +0.14 | Hot-spot |
| Upper stringer | Root, BL 2.5m | Compression | -398.2 | -455.0 | +0.14 | Critical |
| Lower skin panel | Root, BL 0-3m | Tension | +312.8 | +434.0 | +0.39 | OK |
| Lower stringer | Root, BL 1.8m | Tension | +365.1 | +503.0 | +0.38 | OK |
| Front spar web | Root | Shear | 82.5 | 156.0 | +0.89 | OK |
| Rear spar web | Root | Shear | 68.2 | 156.0 | +1.29 | OK |
| Front spar cap | Root | Compression | -412.6 | -760.0 | +0.84 | Ti fittings |
| Rear spar cap | Root | Tension | +398.4 | +827.0 | +1.08 | Ti fittings |
| Rib post | BL 6.5m | Shear | 124.5 | 276.0 | +1.22 | Al 7075-T6 |
| Wing-body fairing | FS 0.5 | Von Mises | 198.5 | 276.0 | +0.39 | Al 7075-T6 |

#### 5.1.2 Panel Buckling Check (Upper Skin Compression Zones)

| Panel Location | Applied σ (MPa) | Panel Dimensions (mm) | Buckling σcr (MPa) | Interaction Ratio | MS | Status |
|----------------|-----------------|----------------------|-------------------|-------------------|-----|--------|
| Root LE (BL 0-2m) | -285.4 | 250×600×12t | -342.8 | 0.83 | +0.20 | PASS |
| Root TE (BL 0-2m) | -245.6 | 250×600×12t | -342.8 | 0.72 | +0.40 | PASS |
| Mid-span (BL 12-14m) | -188.2 | 250×600×8t | -224.5 | 0.84 | +0.19 | PASS |
| Tip (BL 24-26m) | -98.5 | 250×600×4t | -115.2 | 0.85 | +0.17 | PASS |

**Notes:** 
- Panel buckling analysis per NASA SP-8007 and Bruhn methods
- Interaction ratio includes combined axial + shear loads
- All panels show positive MS for buckling → ACCEPTABLE

### 5.2 Ultimate Load Analysis

Ultimate load factor = 1.5 × Limit load per CS-25.303

| Component | Station | Ultimate Stress (MPa) | Allowable (MPa) | MS (Ultimate) | Status |
|-----------|---------|----------------------|-----------------|---------------|--------|
| Upper skin | Root | -428.1 | -486.0 | +0.14 | PASS |
| Upper stringer | Root | -597.3 | -682.5 | +0.14 | PASS |
| Lower skin | Root | +469.2 | +651.0 | +0.39 | PASS |
| Lower stringer | Root | +547.7 | +754.5 | +0.38 | PASS |
| Front spar cap | Root | -618.9 | -1140.0 | +0.84 | PASS |

**Assessment:** All ultimate load margins ≥ +0.14 → **MEETS CS-25.305 REQUIREMENTS**

---

## 6. Hot-Spot Analysis

### 6.1 Wing Root Upper Skin (BL 0-3m, FS 0.5-1.5m)

**Issue:** Minimum MS = +0.14 at 2.5g pull-up, compression-critical
**Contributing Factors:**
- High bending moment concentration at wing-body junction
- Load introduction from wing box into center body structure
- Geometric transition from airfoil to center body blend

**Detailed Analysis:**
- Local FEM refinement with 10mm element size (vs. 50mm global model)
- Peak stress -298.6 MPa (3% higher than global model -285.4 MPa)
- Stress concentration factor Kt = 1.05 at blend radius
- MS = +0.09 (refined analysis) → **REQUIRES ATTENTION**

**Recommendations:**
1. Increase upper skin thickness from 12mm to 14mm in BL 0-3m zone (+15% mass = +12 kg)
2. Add doublers at wing-body blend (300mm wide × 4mm thick × 3m span = +8 kg)
3. Optimize stringer spacing in root region (reduce from 250mm to 200mm for 8 stringers)
4. **Predicted MS improvement:** +0.09 → +0.25 with 20kg mass penalty

### 6.2 Front Spar Root Attachment (BL 2.5m)

**Issue:** Spar cap compression -398.2 MPa, MS = +0.14
**Analysis:**
- Titanium end fitting transfers load into rib/frame
- Bearing stress at bolt holes: 486 MPa (allowable 1034 MPa, MS = +1.13) → OK
- Tension/shear interaction in bolts: Interaction ratio = 0.68 → OK

**Recommendation:** Acceptable as designed, monitor during structural test

---

## 7. Ribs and Stringers

### 7.1 Critical Rib Identification

| Rib Location | Load Case | Critical Loading | Max Stress (MPa) | Allowable (MPa) | MS | Function |
|--------------|-----------|------------------|------------------|-----------------|-----|----------|
| BL 0.0 (centerline) | LC-MNV-01 | Shear + bending | 245.6 | 276.0 | +0.12 | Wing-body attachment |
| BL 6.5 | LC-MNV-01 | Shear (fuel load) | 124.5 | 276.0 | +1.22 | Fuel tank bulkhead |
| BL 13.0 | LC-GST-03 | Bending (gust) | 156.8 | 276.0 | +0.76 | Mid-span stiffness |
| BL 19.5 | LC-MNV-04 | Torsion | 98.4 | 276.0 | +1.81 | Aileron support |

**Assessment:** All ribs have positive MS, centerline rib is most critical (MS = +0.12)

### 7.2 Stringer Run-Out Analysis

**Upper Surface Stringers:**
- 24 stringers at root taper to 8 stringers at tip
- Stringer terminations at BL 6.5m (4 stringers), BL 13.0m (4 stringers), BL 19.5m (8 stringers)
- Load redistribution analyzed with local FEM models at termination ribs
- Peak stress at termination points: 215 MPa (allowable 276 MPa, MS = +0.28) → OK

**Recommendation:** Stringer run-out locations acceptable, ensure proper radius and doubler at terminations

---

## 8. Design Recommendations

### 8.1 Immediate Actions (Pre-Production)

1. **Wing Root Reinforcement:**
   - Implement 14mm upper skin thickness BL 0-3m (current: 12mm)
   - Add doublers at wing-body blend as specified in Section 6.1
   - **Impact:** +20 kg structural mass, MS +0.14 → +0.25

2. **Centerline Rib Upgrade:**
   - Increase rib post thickness from 8mm to 10mm
   - Add stiffeners to web to prevent shear buckling
   - **Impact:** +5 kg, MS +0.12 → +0.30

### 8.2 Testing Requirements

1. **Full-Scale Wing Box Test:**
   - Test article: Root to 50% semi-span (BL 0-13m)
   - Load cases: LC-MNV-01 (2.5g), LC-GST-03 (gust)
   - Instrumentation: 200+ strain gauges, 50+ displacement sensors
   - **Objective:** Validate FEM predictions within ±10%, verify MS ≥ 0.0 at all locations

2. **Panel Buckling Tests:**
   - Test panels representing root, mid-span, and tip construction
   - Load to buckling + 20% for post-buckling behavior
   - **Objective:** Validate buckling predictions and knockdown factors

3. **Stringer Pull-Off Tests:**
   - Test co-cured stringer-to-skin interface strength
   - Load to failure, measure peel and shear strength
   - **Objective:** Validate allowables and damage tolerance assumptions

### 8.3 Follow-On Analyses

1. **Fatigue Spectrum Analysis** (link to STR-005)
2. **Damage Tolerance Analysis** (link to STR-006)
3. **Thermal Effects** (cryogenic H₂ tank in wing box)
4. **Aeroelastic Analysis** (flutter, divergence, control reversal per AERO-005)

---

## 9. References

### 9.1 Design Documents
- `04_DESIGN/STRUCTURAL_DESIGN/Wing_Box_Design.md`
- `04_DESIGN/STRUCTURAL_DESIGN/Wing_Structure_Drawings.pdf`

### 9.2 Input Data
- `CALCULATIONS/STRUCTURAL/Wing_Box_Section_Calcs.csv`
- `ANALYSIS_REPORTS/STRUCTURAL/FEM_Global_Model.md` (STR-001)

### 9.3 Standards and Methods
- CS-25.305 – Strength and Deformation
- CS-25.571 – Damage Tolerance and Fatigue Evaluation
- MIL-HDBK-5J – Metallic Materials and Elements for Aerospace Vehicle Structures
- CMH-17 – Composite Materials Handbook
- NASA SP-8007 – Buckling of Thin-Walled Circular Cylinders
- Bruhn, E.F., "Analysis and Design of Flight Vehicle Structures"

---

## 10. Conclusions

1. **Structural Adequacy:** Wing box structure meets CS-25.305 strength requirements with positive margins of safety for all limit and ultimate load cases.

2. **Critical Areas:** Two hot-spots identified requiring reinforcement:
   - Wing root upper skin (BL 0-3m): MS = +0.09 → recommend thickness increase
   - Centerline rib: MS = +0.12 → recommend web stiffeners

3. **Buckling:** All compression panels show positive buckling margins (MS ≥ +0.17)

4. **Mass Impact:** Recommended reinforcements add 25 kg to wing box mass (0.35% increase)

5. **Next Steps:** 
   - Implement design changes
   - Perform full-scale static test
   - Integrate with fatigue/DT analyses

---

**Supporting Figures:**
- **02-11-00-STR-002-FIG-01_WingBox_Section.png** – Cross-sections at root, mid-span, tip showing skins/spars/stringers/ribs
- **02-11-00-STR-002-FIG-02_WingBox_Stress_Map.png** – Contour of von Mises stresses along span at 2.5g pull-up
- **02-11-00-STR-002-FIG-03_Panel_Buckling_Margins.png** – Plot of buckling MS vs. span station
- **02-11-00-STR-002-FIG-04_Rib_Locations.png** – Plan view showing rib spacing and critical ribs
- **02-11-00-STR-002-FIG-05_HotSpot_Detail.png** – Detailed view of wing root upper skin with local mesh refinement

---

**Document Control:**
- **Version:** 1.0 (Complete)
- **Date:** 2025-11-10
- **Prepared by:** Structures Team
- **Reviewed by:** Chief Structural Engineer
- **Approved by:** Program Chief Engineer
