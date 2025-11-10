# Safety Analysis Report

**Analysis ID:** 02-11-00-CERT-003  
**Platform:** AMPEL360 BWB H₂ Hy-E Q100  
**Analysis Type:** Certification - Safety Analysis  
**Status:** Planned  
**Date:** 2025-11-10

---

## 1. Objective

Conduct safety analysis per SAE ARP 4761 to:
- Identify hazards associated with aircraft geometry and dimensions
- Assess safety risks and failure modes
- Demonstrate compliance with CS-25.1309 (System Safety)
- Support overall aircraft safety case

---

## 2. Safety Analysis Process (Per ARP 4761)

### 2.1 Functional Hazard Assessment (FHA)
Identify hazards at functional level and classify by severity:
- **Catastrophic:** Prevents continued safe flight and landing
- **Hazardous:** Large reduction in safety margins
- **Major:** Significant reduction in safety margins
- **Minor:** Slight reduction in safety margins
- **No Safety Effect:** No impact on safety

### 2.2 Preliminary System Safety Assessment (PSSA)
Allocate safety requirements to systems and components.

### 2.3 Fault Tree Analysis (FTA) / Failure Modes and Effects Analysis (FMEA)
Analyze specific failure modes and combinations.

### 2.4 Common Cause Analysis (CCA)
Identify common cause failures that could affect multiple systems.

---

## 3. Geometry-Related Hazards

### 3.1 Landing Gear and Ground Clearance

| Hazard | Effect | Severity | Probability Target | Mitigation |
|--------|--------|----------|-------------------|------------|
| Insufficient tail clearance during rotation | Tail strike, structural damage | Major | Remote | Design clearance margins, pilot training |
| Gear collapse due to overload | Loss of control on ground | Hazardous | Extremely Remote | Adequate strength margins, regular inspection |
| Inadequate wingtip clearance | Ground contact during taxi/landing | Major | Remote | Design margins, ground handling procedures |

### 3.2 Structural Integrity

| Hazard | Effect | Severity | Probability Target | Mitigation |
|--------|--------|----------|-------------------|------------|
| Wing structural failure in flight | Loss of aircraft | Catastrophic | Extremely Improbable | Ultimate strength margins (1.5×), damage tolerance, inspection program |
| Pressure vessel failure (explosive decompression) | Injury to occupants, loss of control | Catastrophic | Extremely Improbable | Pressure vessel design per CS-25.365, proof testing, crack detection |
| Landing gear attachment failure | Loss of control during landing | Catastrophic | Extremely Improbable | Ultimate strength margins, damage tolerance, regular inspection |

### 3.3 Center of Gravity (CG) Exceedance

| Hazard | Effect | Severity | Probability Target | Mitigation |
|--------|--------|----------|-------------------|------------|
| Forward CG limit exceeded | Insufficient pitch control authority | Hazardous | Extremely Remote | Loading procedures, weight and balance checks, CG warning system |
| Aft CG limit exceeded | Reduced static stability, pitch-up tendency | Catastrophic | Extremely Improbable | Loading procedures, weight and balance checks, CG warning system |

### 3.4 H₂ Fuel System Integration

| Hazard | Effect | Severity | Probability Target | Mitigation |
|--------|--------|----------|-------------------|------------|
| H₂ tank rupture due to structural failure | Fire/explosion, loss of aircraft | Catastrophic | Extremely Improbable | Tank protection, crash-resistant design, separation from ignition sources |
| H₂ leak in wing box | Accumulation of explosive mixture | Catastrophic | Extremely Improbable | Leak detection, ventilation, isolation valves |
| CG shift due to H₂ fuel burn | Loss of control (CG out of limits) | Hazardous | Remote | Fuel management system, CG monitoring, automatic fuel transfer |

---

## 4. Quantitative Safety Analysis

### 4.1 Probability of Failure

Per CS-25.1309, the following probability targets apply:

| Effect Severity | Maximum Probability per Flight Hour |
|----------------|-------------------------------------|
| Catastrophic | ≤ 10⁻⁹ (Extremely Improbable) |
| Hazardous | ≤ 10⁻⁷ (Extremely Remote) |
| Major | ≤ 10⁻⁵ (Remote) |
| Minor | ≤ 10⁻³ (Probable) |

### 4.2 Fault Tree Analysis (Example: Wing Structural Failure)

**Top Event:** Wing structural failure in flight

**Intermediate Events:**
- Excessive load application
- Inadequate structural strength
- Undetected structural damage

**Basic Events:**
- Pilot exceeds flight envelope (probability: TBD)
- Manufacturing defect (probability: TBD)
- Fatigue crack exceeds critical size (probability: TBD)

**Computed Top Event Probability:** TBD (target: ≤ 10⁻⁹ per flight hour)

---

## 5. Safety Features and Mitigations

### 5.1 Design Features
- **Ultimate load margins:** 1.5× limit load per CS-25.303
- **Damage tolerance:** Structure can sustain cracks and retain ultimate strength
- **Fail-safe design:** Multiple load paths, crack arrestors
- **CG monitoring:** Weight and balance system with out-of-limits warning

### 5.2 Operational Procedures
- **Pre-flight weight and balance check**
- **Loading procedures to maintain CG within limits**
- **Regular structural inspections per maintenance program**
- **Pilot training on geometry-related limitations (tail strike, wingtip clearance)**

### 5.3 Monitoring and Detection
- **Structural health monitoring (SHM):** Sensors on critical structure
- **H₂ leak detection:** Gas sensors in fuel system compartments
- **CG indication:** Real-time CG display in cockpit

---

## 6. Safety Assessment Summary

| System/Function | Hazards Identified | Safety Analysis Completed | Compliance Status |
|----------------|-------------------|---------------------------|-------------------|
| Landing gear and clearances | 3 | Planned | TBD |
| Structural integrity | 3 | Planned | TBD |
| CG management | 2 | Planned | TBD |
| H₂ fuel system integration | 3 | Planned | TBD |

---

## 7. Compliance Statement

Upon completion of safety analysis:

> The AMPEL360 BWB H₂ Hy-E Q100 aircraft geometry and dimensional design complies with CS-25.1309 safety requirements. All identified hazards have been mitigated to acceptable levels, and the aircraft meets the safety objectives for catastrophic, hazardous, major, and minor failure conditions.

*(To be signed by Chief Safety Engineer and Program Chief Engineer upon completion.)*

---

## 8. References

- CS-25.1309 – Equipment, Systems, and Installations (Safety)
- SAE ARP 4761 – Guidelines and Methods for Conducting the Safety Assessment Process
- SAE ARP 4754A – Guidelines for Development of Civil Aircraft and Systems
- `ANALYSIS_REPORTS/STRUCTURAL/` (all structural analysis reports)
- `ANALYSIS_REPORTS/WEIGHT_BALANCE/CG_Envelope_Calculation.md`

---

**Document Control:**
- **Version:** 1.0 (Draft)
- **Date:** 2025-11-10
