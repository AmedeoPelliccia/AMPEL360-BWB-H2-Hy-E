# Fatigue Analysis

**Analysis ID:** 02-11-00-STR-005  
**Platform:** AMPEL360 BWB H₂ Hy-E Q100  
**Analysis Type:** Structural - Fatigue Life  
**Status:** Planned  
**Date:** 2025-11-10

---

## 1. Objective

Perform fatigue analysis to demonstrate compliance with CS-25.571 (Damage Tolerance and Fatigue Evaluation):
- Determine fatigue-critical locations
- Calculate safe-life or safe-crack-growth life
- Establish inspection intervals

---

## 2. Design Life Requirements

### 2.1 Operational Life
- **Design service goal (DSG):** 60,000 flight hours
- **Design service objective (DSO):** 90,000 flight hours
- **Average flight duration:** 4 hours
- **Flights:** 15,000 (DSG), 22,500 (DSO)

### 2.2 Load Spectrum
- Gust loads per operational environment
- Maneuver loads per mission profile
- Pressurization cycles: 1 per flight
- Landing cycles: 1 per flight

---

## 3. Fatigue-Critical Locations

### 3.1 Wing Structure
- Wing root attachment to center body
- Wing spar cap splices
- Stringer run-outs

### 3.2 Center Body
- Pressure vessel skin at door cutouts
- Frame-to-skin attachment points
- Floor beam attachments

### 3.3 Landing Gear Attachments
- Main gear trunnion fittings
- Side-brace attachments
- Drag-brace attachments

---

## 4. Analysis Methodology

### 4.1 S-N Approach (Safe-Life)
For non-inspectable or difficult-to-inspect structure:
- Use material S-N curves (stress vs. cycles to failure)
- Apply scatter factor of 4 on life
- Calculate cycles to failure for each critical location

### 4.2 Crack Growth Approach (Damage Tolerance)
For inspectable primary structure:
- Assume initial flaw size (per CS-25.571)
- Calculate crack growth using Paris law: da/dN = C(ΔK)^m
- Determine inspection intervals based on detectable crack size

---

## 5. Results

### 5.1 Fatigue Life Summary

| Component | Critical Location | Life (Flights) | Inspection Interval | Status |
|-----------|-------------------|----------------|---------------------|--------|
| Wing box | Root spar cap | TBD | TBD | Pending |
| Wing box | Mid-span lower skin | TBD | TBD | Pending |
| Center body | Door frame | TBD | TBD | Pending |
| Pressure vessel | Skin at window cutout | TBD | TBD | Pending |
| Landing gear attach | Trunnion fitting | TBD | TBD | Pending |

### 5.2 Safety Factors
- **Safe-life:** 4× on life (per CS-25.571)
- **Damage tolerance:** 2× inspection interval

---

## 6. Inspection Program

### 6.1 Inspection Methods
- **Visual:** External walk-around
- **NDT:** Ultrasonic, eddy current, radiography
- **Teardown:** Periodic fleet leader teardown inspection

### 6.2 Inspection Intervals
TBD based on crack growth analysis.

---

## 7. References

- CS-25.571 – Damage Tolerance and Fatigue Evaluation
- ASTM E1049 – Rainflow Cycle Counting
- ASTM E647 – Fatigue Crack Growth Rate Testing
- NASGRO – Crack Growth Analysis Software
- `04_DESIGN/STRUCTURAL_DESIGN/`

---

**Document Control:**
- **Version:** 1.0 (Draft)
- **Date:** 2025-11-10
