# 02-20-13-A-002 — Takeoff Performance Charts

**Asset ID:** 02-20-13-A-002  
**Title:** Takeoff Performance Charts  
**Subsystem:** [02-20-13_Performance_Computer](../README.md)  
**Type:** Engineering Charts (Visual Aid)  
**Format:** SVG + Markdown Description  
**Status:** PLACEHOLDER (DRAFT)  

---


<img width="1200" height="800" alt="image" src="https://github.com/user-attachments/assets/3adebb48-6eec-4d9d-a82e-e7b18ebc6202" />


## 1. Purpose

This asset groups the **engineering charts** used to:

- Visualize key **takeoff performance relationships** for AMPEL360 (Q80/Q100/Q120)
- Provide a **human-checkable view** of the underlying models used by  
  [02-20-13-002_Takeoff_Performance.md](../02-20-13-002_Takeoff_Performance.md)
- Support **verification & validation** activities in  
  [TEST_DATA/02-20-13-T-001_TO_RunwayCases.json](../TEST_DATA/02-20-13-T-001_TO_RunwayCases.json)  
- Provide **AFM-style views** for certification discussions and internal reviews

The charts are **informative** only; the **authoritative behavior** of the Performance Computer resides in the algorithms and associated datasets, not in these illustrations.

---

## 2. Files

Located under:

`.../02-20-13_Performance_Computer/ASSETS/`

- **[02-20-13-A-002_Takeoff_Charts.svg](./02-20-13-A-002_Takeoff_Charts.svg)**  
  Multi-panel SVG containing canonical takeoff performance views for the Q100 baseline.  

If later you split the SVG into multiple files, extend this section as:

- `02-20-13-A-002-01_TO_FieldLength_vs_Weight.svg`  
- `02-20-13-A-002-02_TO_FieldLength_vs_Temp.svg`  
- `02-20-13-A-002-03_Vspeeds_vs_Weight.svg`  
- `…`  

---

## 3. Chart Panel Overview (Suggested Layout)

The SVG is expected to contain **multiple panels**, for example:

1. **Panel A — Field Length vs Takeoff Weight (ISA, Sea Level)**  
   - **X-axis:** Takeoff weight (kg)  
   - **Y-axis:** Required field length (m)  
   - **Curves:** Different flap settings (e.g. TO1, TO2), possibly annotated with  
     “field-length limited” vs “climb limited” regions.  

2. **Panel B — Field Length vs Temperature (Fixed Weight)**  
   - **X-axis:** OAT / ISA deviation (°C)  
   - **Y-axis:** Required field length (m)  
   - **Curves:** Several **pressure altitudes** (e.g. SL, 3000 ft, 6000 ft)  
   - Optional annotations for **hybrid boost availability** regimes.  

3. **Panel C — V-Speeds vs Takeoff Weight**  
   - **X-axis:** Takeoff weight (kg)  
   - **Y-axis:** Speed (kt)  
   - **Curves:** V₁, Vᵣ, V₂ for a given configuration and runway condition.  

4. **Panel D — Hybrid Power Envelope (Takeoff Segment)**  
   - **X-axis:** Time from brake release (s)  
   - **Y-axis:** Power (kW)  
   - **Curves:**
     - Fuel-cell stack power  
     - CO₂ battery boost  
     - Total propulsive power vs required profile  
   - Intended to visually support requirements such as `RQ-10-02-HYB-TO-POWER`.  

> **Note:** Actual panel layout and exact variable selection is to be finalized by the Performance & Propulsion teams. This section is a **template / intent description**.

---

## 4. Relationship with Algorithms & Test Data

These charts are **visual projections** of the numerical models used in:

- [02-20-13-002_Takeoff_Performance.md](../02-20-13-002_Takeoff_Performance.md)  
  - `ALG-TO-01` Balanced field  
  - `ALG-TO-02` V-speeds  
  - `ALG-TO-03/04/05` Climb / obstacle / field-length limits  
  - `ALG-TO-07` Hybrid power constraints  

- [02-20-13-006_BWB_Specific_Calculations.md](../02-20-13-006_BWB_Specific_Calculations.md)  
  - BWB CL/CD/CM and hybrid effects influencing takeoff performance  

- [TEST_DATA/02-20-13-T-001_TO_RunwayCases.json](../TEST_DATA/02-20-13-T-001_TO_RunwayCases.json)  
  - Regression cases should **land on** or be consistent with the curves plotted here.  

Use the charts to:

- Quickly check if changes in models (aero, mass, hybrid envelope) cause  
  **expected shifts** in required field length and V-speeds.
- Provide **sanity checks** during tuning of AFM-consistent tables.

---

## 5. Intended Usage

- **Engineering reviews:**  
  - Slide decks, internal design reviews, discussions with certification teams.  

- **Documentation & AFM alignment:**  
  - Side-by-side with AFM draft figures to verify **shape and trends** of curves.  

- **Verification & debug:**  
  - When a regression test fails (e.g. `TO-RWY-002` hot-and-high case), engineers can  
    overlay that point on the corresponding chart to understand whether the issue  
    is a model, interpolation, or data input problem.

Charts are **not** to be used operationally (pilots / dispatch) without an AFM /  
Ops-approved editorial process.

---

## 6. Toolchain & Source

Recommended toolchain:

- **Authoring:**  
  - Python / Matplotlib, or equivalent plotting tool, exporting to `.svg`.  
- **Post-editing (optional):**  
  - Inkscape or similar, for cosmetic label adjustments.

> If a script is used to auto-generate the SVG, reference it here, e.g.:  
> `tools/perf_plots/generate_takeoff_charts.py`

---

## 7. Document Control

> **Originator:** AI prompted by Amedeo Pelliccia  
> **Asset:** 02-20-13-A-002 Takeoff Performance Charts  
> **Maintainer:** Digital Ops & Performance Group  

| Version | Date       | Author / Team                         | Notes                            |
| ------- | ---------- | ------------------------------------- | -------------------------------- |
| 0.1.0   | 2025-11-20 | AMPEL360 Digital Ops & Performance WG | Initial description (placeholder) |
```
