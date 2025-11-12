# Structural Substantiation Report

**Analysis ID:** 02-11-00-CERT-002  
**Platform:** AMPEL360 BWB H₂ Hy-E Q100  
**Analysis Type:** Certification - Structural Substantiation  
**Status:** Planned  
**Date:** 2025-11-10

---

## 1. Objective

Provide comprehensive structural substantiation to demonstrate compliance with CS-25 Subpart C (Structure):
- Verify structural integrity under all design loads
- Demonstrate adequate strength and stiffness
- Show compliance with damage tolerance requirements
- Support Type Certificate application

---

## 2. Certification Basis

### 2.1 Applicable CS-25 Requirements

| Regulation | Title | Compliance Strategy |
|------------|-------|---------------------|
| CS-25.301 | Loads | Analysis per global FEM |
| CS-25.305 | Strength and Deformation | Analysis + component tests |
| CS-25.307 | Proof of Structure | Ultimate load test of critical components |
| CS-25.571 | Damage Tolerance | Analysis + full-scale fatigue test |
| CS-25.603 | Materials | Material qualification per standards |
| CS-25.605 | Fabrication Methods | Process qualification |
| CS-25.613 | Material Strength Properties | A-basis and B-basis allowables |
| CS-25.619 | Special Factors | Casting and fitting factors applied |

---

## 3. Structural Design Overview

### 3.1 Primary Structure

| Component | Material | Construction | Load Path |
|-----------|----------|--------------|-----------|
| Wing box | Carbon/epoxy composite | Stiffened skin, multi-spar | Wing bending and torsion |
| Center body | Aluminum 7075-T6 + composite | Semi-monocoque, frames and stringers | Cabin pressure, floor loads |
| Vertical stabilizers | Composite | Multi-spar, stiffened skin | Lateral and directional loads |
| Landing gear attachments | Titanium forgings | High-strength fittings | Landing and taxi loads |

### 3.2 Load Cases Summary

| Load Case | Description | Limit Load Factor | Analysis Method |
|-----------|-------------|-------------------|-----------------|
| LC-01 | Symmetric pull-up (2.5g) | 2.5 | FEM |
| LC-02 | Symmetric push-over (-1.0g) | -1.0 | FEM |
| LC-03 | Gust loads (+56 ft/s) | Variable | FEM + dynamic analysis |
| LC-04 | Landing impact | 3.0 | FEM + drop test |
| LC-05 | Cabin pressurization (8.0 psi) | ΔP = 8.0 psi | FEM + pressure test |

**Ultimate loads:** 1.5 × Limit loads (per CS-25.303)

---

## 4. Structural Analysis Summary

### 4.1 Global FEM Results

**Model:** MSC Nastran, 500,000+ nodes, 450,000+ elements

| Load Case | Critical Location | Applied Stress (MPa) | Allowable (MPa) | MS | Status |
|-----------|-------------------|----------------------|-----------------|-----|--------|
| 2.5g maneuver | Wing root upper skin | TBD | TBD | TBD | Pending |
| -1.0g maneuver | Wing root lower skin | TBD | TBD | TBD | Pending |
| Pressurization | Center body skin | TBD | TBD | TBD | Pending |
| Landing | MLG trunnion fitting | TBD | TBD | TBD | Pending |

**All margins of safety (MS) must be ≥ 0.0 for limit load and ultimate load.**

### 4.2 Damage Tolerance

**Per CS-25.571:**
- Initial flaw size: 0.05 inch (1.27 mm) surface crack
- Crack growth analysis: Paris law (NASGRO software)
- Inspection intervals: Based on 2× safety factor on crack growth life

**Critical locations:**
- Wing lower skin at root (high tension)
- Center body at door frames (stress concentration)
- Landing gear trunnion fittings

---

## 5. Structural Testing

### 5.1 Component Tests

| Test | Component | Objective | Status |
|------|-----------|-----------|--------|
| Pressure test | Center body barrel section | Verify hoop stress analysis | Planned |
| Landing gear drop test | MLG assembly | Verify energy absorption | Planned |
| Wing box ultimate test | Wing root section | Verify ultimate strength | Planned |

### 5.2 Full-Scale Tests (If Required)

- **Static test:** Ultimate load test of complete airframe
- **Fatigue test:** 2× design life (120,000 flight hours equivalent)
- **Damage tolerance validation:** Crack growth in full-scale structure

---

## 6. Material Qualification

### 6.1 Materials Used

| Material | Application | Specification | Allowables Basis |
|----------|-------------|---------------|------------------|
| Aluminum 7075-T6 | Center body skin, frames | AMS 4045 | MIL-HDBK-5J (B-basis) |
| Titanium Ti-6Al-4V | Landing gear fittings | AMS 4928 | MIL-HDBK-5J (A-basis) |
| Carbon/epoxy (IM7/8552) | Wing box, vertical tails | CMH-17 | CMH-17 (A-basis) |

### 6.2 Material Testing
- **Static properties:** Tension, compression, shear, bearing
- **Environmental effects:** Temperature, moisture, UV exposure
- **Fatigue properties:** S-N curves, crack growth (da/dN)

---

## 7. Fabrication and Quality Control

### 7.1 Manufacturing Processes
- **Composite lay-up:** Hand lay-up or automated fiber placement (AFP)
- **Aluminum machining:** CNC machining of plate and extrusions
- **Titanium forging:** Forgings per AMS specifications

### 7.2 Quality Assurance
- **Non-destructive testing (NDT):** Ultrasonic, X-ray, eddy current
- **Process control:** Statistical process control (SPC)
- **Traceability:** Material lot tracking and certification

---

## 8. Compliance Statement

Upon completion of all analyses and tests:

> The AMPEL360 BWB H₂ Hy-E Q100 aircraft structure complies with all applicable requirements of CS-25 Subpart C (Structure) as demonstrated by analysis and test. All structural margins of safety are positive, and the structure is substantiated for safe operation throughout the design life.

*(To be signed by Chief Structural Engineer and Program Chief Engineer upon completion.)*

---

## 9. References

- All structural analysis reports in `ANALYSIS_REPORTS/STRUCTURAL/`
- CS-25 Subpart C – Structure
- MIL-HDBK-5J – Metallic Materials and Elements for Aerospace Vehicle Structures
- CMH-17 – Composite Materials Handbook

---

**Document Control:**
- **Version:** 1.0 (Draft)
- **Date:** 2025-11-10
