# Wing Sweep and Aspect Ratio Trade Study

**Trade Study ID:** 02-11-00-TS-002  
**Platform:** AMPEL360 BWB H₂ Hy-E Q100  
**Status:** Draft  
**Date:** 2025-11-10

---

## 1. Objective

Optimize wing sweep angle (Λ) and aspect ratio (AR) to balance:
- Cruise aerodynamic efficiency (L/D)
- Structural weight
- Airport compatibility (wingspan constraints)
- High-lift performance

---

## 2. Requirements

### 2.1 Performance Requirements
- **Cruise Mach:** 0.82 at FL410
- **Target L/D:** > 23
- **Range:** 8,000 km with 400 passengers

### 2.2 Constraints
- **Wingspan:** ≤ 52 m (ICAO Code E, 52-65 m)
- **Wing area:** ~845 m² (for appropriate wing loading)

---

## 3. Options Evaluated

| Option | Sweep Λ (°) | Aspect Ratio | Wingspan (m) | Wing Area (m²) | Est. L/D | Structural Weight (kg) |
|--------|-------------|--------------|--------------|----------------|----------|------------------------|
| A | 30 | 2.8 | 49.0 | 858 | 21.5 | 24,500 |
| B | 33 | 3.0 | 50.5 | 851 | 22.8 | 25,200 |
| C | 35 | 3.2 | 52.0 | 845 | 23.6 | 26,100 |
| D | 38 | 3.5 | 52.0 | 773 | 24.2 | 27,500 |

---

## 4. Evaluation Criteria

### 4.1 Aerodynamic Performance (Weight: 50%)

| Option | Cruise L/D | Wave Drag | Induced Drag | Score (1-10) |
|--------|------------|-----------|--------------|--------------|
| A | 21.5 | High (low sweep) | Low (low AR) | 6 |
| B | 22.8 | Moderate | Moderate | 8 |
| C | 23.6 | Low | Moderate | 9 |
| D | 24.2 | Low | Low (high AR) | 10 |

### 4.2 Structural Weight (Weight: 30%)

**Wing root bending moment increases with AR:**
- Higher AR → Longer span → Higher bending moment → Heavier structure

| Option | Wing Weight (kg) | % of OEW | Score (1-10) |
|--------|------------------|----------|--------------|
| A | 24,500 | 20.4% | 10 |
| B | 25,200 | 21.0% | 9 |
| C | 26,100 | 21.8% | 7 |
| D | 27,500 | 22.9% | 5 |

### 4.3 Airport Compatibility (Weight: 15%)

| Option | Wingspan (m) | ICAO Code | Turning Radius (m) | Score (1-10) |
|--------|--------------|-----------|-------------------|--------------|
| A | 49.0 | E | 28.5 | 10 |
| B | 50.5 | E | 29.4 | 9 |
| C | 52.0 | E (max) | 30.3 | 8 |
| D | 52.0 | E (max) | 30.3 | 8 |

### 4.4 High-Lift Performance (Weight: 5%)

Higher sweep reduces CLmax:

| Option | Sweep (°) | Est. CLmax (TO) | Est. CLmax (LDG) | Score (1-10) |
|--------|-----------|-----------------|------------------|--------------|
| A | 30 | 1.95 | 2.55 | 10 |
| B | 33 | 1.88 | 2.48 | 9 |
| C | 35 | 1.82 | 2.42 | 8 |
| D | 38 | 1.72 | 2.32 | 6 |

---

## 5. Scoring Summary

| Option | Aero (50%) | Weight (30%) | Airport (15%) | High-Lift (5%) | **Total** |
|--------|------------|--------------|---------------|----------------|-----------|
| A | 3.0 | 3.0 | 1.5 | 0.5 | **8.0** |
| B | 4.0 | 2.7 | 1.4 | 0.5 | **8.6** |
| C | 4.5 | 2.1 | 1.2 | 0.4 | **8.2** ✓ |
| D | 5.0 | 1.5 | 1.2 | 0.3 | **8.0** |

---

## 6. Recommendation

**Selected Option: C (35° sweep, AR 3.2, 52 m span)**

### 6.1 Rationale
- Excellent cruise L/D (23.6, exceeds target of 23)
- Acceptable structural weight (26,100 kg)
- Maximum ICAO Code E wingspan (good airport access)
- Adequate high-lift performance (CLmax 1.82 TO, 2.42 LDG)

---

**Document Control:**
- **Version:** 1.0 (Draft)
- **Date:** 2025-11-10
