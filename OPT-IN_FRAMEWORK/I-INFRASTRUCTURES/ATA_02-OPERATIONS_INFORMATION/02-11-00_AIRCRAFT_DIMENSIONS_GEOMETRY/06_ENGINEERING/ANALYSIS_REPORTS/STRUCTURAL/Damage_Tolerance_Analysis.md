# Damage Tolerance Analysis

**Analysis ID:** 02-11-00-STR-006  
**Platform:** AMPEL360 BWB H₂ Hy-E Q100  
**Analysis Type:** Structural - Damage Tolerance  
**Status:** Planned  
**Date:** 2025-11-10

---

## 1. Objective

Demonstrate compliance with CS-25.571(a) damage tolerance requirements:
- Show that structure can sustain damage (cracks, corrosion, manufacturing defects) and retain required residual strength
- Establish inspection program to detect damage before it becomes critical
- Provide analysis for slow crack growth and fail-safe capability

---

## 2. Damage Tolerance Philosophy

### 2.1 CS-25.571 Requirements

Per CS-25.571, the following must be shown:

1. **Slow crack growth:** The structure must be capable of sustaining damage (e.g., cracks) that may occur during manufacturing or service, and must be able to be detected by inspection before it grows to critical size.

2. **Fail-safe:** For multiple load path structures, failure of a single element must not result in loss of structural integrity. Remaining structure must sustain design loads.

3. **Inspection program:** Establish inspection thresholds and intervals based on crack growth analysis.

---

## 3. Damage Scenarios

### 3.1 Initial Flaw Assumptions (per CS-25.571)

| Structure Type | Initial Flaw Size | Location |
|----------------|-------------------|----------|
| Skin (surface) | 0.05 inch (1.27 mm) | Any location |
| Skin (internal) | 0.25 inch (6.35 mm) | Through-thickness |
| Fastener holes | Quarter-circle corner crack | Hole edge |
| Welds | 0.10 inch (2.54 mm) | Weld toe |

### 3.2 Critical Damage Locations

- Wing lower skin at root (high tension)
- Center body skin at door corners (stress concentration)
- Landing gear trunnion fittings (high stress)
- Wing spar cap splices (load transfer)

---

## 4. Crack Growth Analysis

### 4.1 Paris Law Equation

da/dN = C (ΔK)^m

Where:
- da/dN = crack growth rate (mm/cycle)
- ΔK = stress intensity factor range (MPa√m)
- C, m = material constants (from NASGRO database)

### 4.2 Stress Intensity Factor

ΔK = Δσ × √(π × a) × Y

Where:
- Δσ = stress range (MPa)
- a = crack length (mm)
- Y = geometry correction factor

---

## 5. Analysis Results

### 5.1 Crack Growth Life

| Component | Initial Flaw | Critical Crack Size | Cycles to Critical | Inspection Interval |
|-----------|--------------|---------------------|-------------------|---------------------|
| Wing lower skin | 1.27 mm | TBD mm | TBD | TBD |
| Center body door frame | 1.27 mm | TBD mm | TBD | TBD |
| Landing gear trunnion | 2.54 mm | TBD mm | TBD | TBD |

### 5.2 Residual Strength

Residual strength with critical crack present must be ≥ design ultimate load (1.5 × limit).

| Component | Critical Crack Size | Residual Strength | Ultimate Load | Status |
|-----------|---------------------|-------------------|---------------|--------|
| Wing lower skin | TBD mm | TBD kN | TBD kN | Pending |
| Center body skin | TBD mm | TBD MPa | TBD MPa | Pending |

---

## 6. Fail-Safe Considerations

### 6.1 Multiple Load Paths

BWB wing structure has multiple load paths:
- **Upper skin:** Redundant stringer arrangement
- **Lower skin:** Stringer and skin carry load independently
- **Spars:** Front and rear spars provide redundancy

**Analysis:** Failure of single stringer must not cause catastrophic failure. Remaining stringers and skin must sustain ultimate load.

### 6.2 Crack Arrestors

- **Tear straps** at critical locations to arrest skin cracks
- **Stringer splices** staggered to prevent simultaneous failure

---

## 7. Inspection Program

### 7.1 Inspection Thresholds
- **Threshold:** Half of calculated inspection interval
- **Interval:** Based on 2× safety factor on crack growth life

### 7.2 Inspection Methods
- **Visual:** Walk-around inspection
- **Ultrasonic:** Skin thickness measurement, crack detection
- **Eddy current:** Fastener hole inspection
- **Radiography:** Internal structure inspection

---

## 8. References

- CS-25.571 – Damage Tolerance and Fatigue Evaluation
- AC 25.571-1D – Damage Tolerance and Fatigue Evaluation
- NASGRO – Fracture Mechanics and Crack Growth Software
- ASTM E647 – Fatigue Crack Growth Rate Testing
- `ANALYSIS_REPORTS/STRUCTURAL/Fatigue_Analysis.md`

---

**Document Control:**
- **Version:** 1.0 (Draft)
- **Date:** 2025-11-10
