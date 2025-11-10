# Flutter Cases Overview

**Analysis ID:** 02-11-00-AERO-005  
**Platform:** AMPEL360 BWB H₂ Hy-E Q100  
**Simulation Type:** Aeroelastic – Flutter (SOL 145 / ZAERO)  
**Status:** Planned – Case Matrix Defined  
**Date:** 2025-11-10

---

## 1. Purpose

This document provides an overview of all aeroelastic flutter simulation cases
associated with `02-11-00-AERO-005 Flutter Analysis`.

It defines:

- The **case matrix** (Mach, altitude, speed, mass/CG/fuel configuration)
- The corresponding **input decks** (FEM, aero model, control surface setup)
- The **output files** and where they are stored

---

## 2. Case Naming Convention

Each flutter case uses the following ID pattern:

`FLUTTER_<Mach>_ALT<Alt_ft>_<MassConfig>_<Version>`

Where:

- `<Mach>` = M030, M060, M082, M085, …  
- `<Alt_ft>` = altitude in hundreds of feet (e.g. 410 for 41,000 ft)  
- `<MassConfig>` = CRUISE_FF, CRUISE_EF, MAXW_FWD, MINW_AFT, …  
- `<Version>` = v01, v02, … (incremented when model or inputs change)

**Example:**  
`FLUTTER_M082_ALT410_CRUISE_FF_v01`

---

## 3. Case Matrix (Planned)

| Case ID                               | Mach | Altitude (ft) | Config          | Description                          | Nastran/ZAERO Input |
|--------------------------------------|------|---------------|-----------------|--------------------------------------|---------------------|
| FLUTTER_M030_ALTXXX_MAXW_FWD_v01     | 0.30 | TBD           | MaxW, fwd CG    | Low-speed, high-mass                 | `SOL145_M030_...dat`|
| FLUTTER_M060_ALTXXX_MAXW_FWD_v01     | 0.60 | TBD           | MaxW, fwd CG    | Mid-subsonic                          | `SOL145_M060_...dat`|
| FLUTTER_M082_ALT410_CRUISE_FF_v01    | 0.82 | 41,000        | Cruise, full fuel | Cruise critical, nominal CG       | `SOL145_M082_FF.dat`|
| FLUTTER_M082_ALT410_CRUISE_EF_v01    | 0.82 | 41,000        | Cruise, empty fuel | Cruise, low mass / CG shift      | `SOL145_M082_EF.dat`|
| FLUTTER_M082_ALT410_MINW_AFT_v01     | 0.82 | 41,000        | MinW, aft CG    | Light, aft CG                        | `SOL145_M082_MINAFT.dat`|
| FLUTTER_M085_ALTXXX_MINW_AFT_v01     | 0.85 | TBD           | MinW, aft CG    | High Mach margin                     | `SOL145_M085_MINAFT.dat`|

*(Extend/modify this table as you finalize the envelope.)*

---

## 4. Input Data Sources

All flutter cases are based on the following inputs:

- **FEM:** `ANALYSIS_REPORTS/STRUCTURAL/FEM_Global_Model.md`  
- **Frozen geometry baseline:**  
  `02-11-00_AIRCRAFT_DIMENSIONS_GEOMETRY/01_OVERVIEW/baseline_dimensions.json`  
- **Flight envelope and speeds:** Performance / certification documentation (TBD)

Each input deck must document:

- FEM version (hash / revision)  
- Mass model version (including fuel and payload assumptions)  
- Aerodynamic model version (DLM panelization)  

---

## 5. Outputs and Post-Processing

For each case, store:

- Raw solver output (`*.f06`, `*.op2`, ZAERO output, etc.)  
- Processed **V–g** and **V–f** diagrams (plots, `*.png`)  
- Mode identification table (mode shapes / descriptions)  

Suggested directory structure:

```text
SIMULATIONS/AEROELASTIC/
  FLUTTER_M082_ALT410_CRUISE_FF_v01/
    input/
      SOL145_M082_FF.dat
    output/
      SOL145_M082_FF.f06
      SOL145_M082_FF.op2
      Vg_M082_FF.png
      Vf_M082_FF.png
      Mode_Summary_M082_FF.md
```

---

## 6. Traceability

Each simulation case shall reference:

- **Flutter methodology:**
  `ANALYSIS_REPORTS/AERODYNAMIC/Flutter_Analysis.md`
- **FEM definition:**
  `ANALYSIS_REPORTS/STRUCTURAL/FEM_Global_Model.md`
- **Relevant design changes / ECRs** affecting stiffness or mass.

This ensures consistent linkage between numerical results, structural models,
and certification documentation.

---

**Document Control:**

- **Version:** 1.0 (Draft – Case Matrix Defined)
- **Date:** 2025-11-10
- **Owner:** Aeroelasticity / Loads & Dynamics Team
